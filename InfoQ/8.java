<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Challenges Performing Background Compilation in V8</h3><p>This article includes details on the recently background compilation introduced in V8, Chrome’s JavaScript engine.</p>
<p>The latest browser from Google, Chrome Beta v. 33, includes an important change in the JavaScript V8 engine: the ability to run the optimizing compilation process in a background thread, letting the main thread continue to be responsive and gaining a performance boost. There are <a href="http://blog.chromium.org/2014/02/compiling-in-background-for-smoother.html">two types of compilations done by V8</a>, according to Yang Guo, a Google Engineer working on it:</p>
<blockquote> 
 <p>To reduce the overall time spent compiling, V8 defers compilation of JavaScript functions until immediately before they are executed the first time. This compilation phase is fast but doesn’t focus on optimizing the code, just on getting it done quickly. In V8, pieces of code that are executed very often are compiled a second time by a specialized <a href="http://blog.chromium.org/2010/12/new-crankshaft-for-v8.html">optimizing compiler</a> [Crankshaft]. This second compilation pass makes use of many advanced optimization techniques, meaning it takes more time than the first pass but delivers much faster code.</p> 
</blockquote>
<p>By doing the optimization compilation in a separate thread, the application is not only more responsive, but it is faster by 27% on Nexus 5 in the <a href="https://developers.google.com/octane/benchmark#mandreel">Mandreel</a> test from the <a href="https://developers.google.com/octane/">Octane 2.0</a> benchmark suite, according to Guo.</p>
<p>InfoQ performed some tests on Chrome 33, with (--js-flags=&quot;--concurrent-recompilation&quot;) and without concurrent recompilation (--js-flags=&quot;--no-concurrent-recompilation&quot;), and noticed the following performance improvements in the Octane 2.0 benchmarks, considering the average results from 5 consecutive runs of the tests having restarting the browser between each run:</p>
<table cellspacing="0" cellpadding="2" width="316" border="1" unselectable="on"> 
 <tbody> 
  <tr> 
   <td valign="top" width="200"><strong>Test</strong></td> 
   <td valign="top" width="114"><strong>Improvement</strong></td> 
  </tr> 
  <tr> 
   <td valign="top" width="200">Octane 2.0 (all 17 tests)</td> 
   <td valign="top" width="114"> <p align="right">7.12%</p> </td> 
  </tr> 
  <tr> 
   <td valign="top" width="200">Mandreel</td> 
   <td valign="top" width="114"> <p align="right">18%</p> </td> 
  </tr> 
  <tr> 
   <td valign="top" width="200">Box2DWeb</td> 
   <td valign="top" width="114"> <p align="right">32%</p> </td> 
  </tr> 
  <tr> 
   <td valign="top" width="200">zlib</td> 
   <td valign="top" width="114"> <p align="right">11%</p> </td> 
  </tr> 
 </tbody> 
</table>
<p>Higher improvements were noticed for 2D and 3D physics engines, while for the entire Octane suite of benchmarks we got a 7% improvement.</p>
<p>We asked Guo why optimizing compilation was not introduced when <a href="http://www.infoq.com/news/2010/12/Google-Chrome-OS/">Crankshaft was released in December 2010</a>. Making sure that we know he’s not speaking for Google and at that time he was not with the team, Guo said that improvements are done based on an actual need:</p>
<blockquote> 
 <p>When Crankshaft was designed, latency was not much of an issue. JavaScript code still have yet to reach sizes where compilation time became noticeable, so low latency was neither an issue nor a design goal for Crankshaft. IMO, introducing concurrency at that time would have made designing a then fledgling optimizing compiler unnecessarily complicated and as such would have been a premature optimization without any immediate benefit.</p> 
 <p>Clearly, that changed over the recent years. If you look at the <a href="https://code.google.com/p/octane-benchmark/source/browse/#svn%2Ftrunk">newest version of the Octane benchmark suite</a>, you'll notice that some parts are over 1MB in size. This is to reflect some of the real world applications that push JavaScript engines to their limits. The Mandreel benchmark consists of 4.8MB of minimized code. In comparison, <a href="http://computerhistory.org/atchm/adobe-photoshop-source-code/">Photoshop 1.0 source code</a> unzipped has a size of 4.4MB. Churning through that amount of code does take noticeable time, and especially becomes a problem when, for example, animation rendering is expected to complete in a blink of an eye.</p> 
</blockquote>
<p>Without attempting to be exhaustive, Guo also told us what were some of the challenges to be dealt with in order to implement background compilation in V8:</p>
<blockquote> 
 <p>- As every computer scientist can tell you, multithreading is hard to get right. Good test coverage is hard to get. Bugs may be hard or impossible to reproduce due to the inherent non-deterministic behavior. Having a good set of test cases, using invariants guarded by assertions, fuzz testing and last but not least Canary test coverage can give much confidence that it's correct. Kudos to the <a href="https://code.google.com/p/data-race-test/wiki/ThreadSanitizer">ThreadSanitizer team</a> btw.</p> 
 <p>- With compilation blocking execution, we can be sure that the state of the JavaScript heap, including all its objects, stays the same before and after compilation. With concurrent compilation, this assumption no longer holds. That has some implications:</p> 
 <p style="margin-left: 40px;">- V8 has a relocating GC, meaning whenever GC kicks in, objects may be moved, so references to it have to be updated. That could very well happen while a compile job is underway. If object references kept by the compile job are not updated, we end up with invalid memory accesses.</p> 
 <p style="margin-left: 40px;">- Execution continues during concurrent compilation. That means that the state of the VM and object content and layout can change arbitrarily. Assumptions made upon those facts at the start of the compile job may not hold at the end any longer. The code produced at the end may not even be valid. Running it would cause bugs and crashes. This has to be dealt with correctly.</p> 
 <p style="margin-left: 40px;">- In fact, having the background thread accessing the heap at any time will very likely lead to race conditions. We avoid that by gathering all necessary information for the compile job upfront.</p> 
 <p>- Finding the correct time to kick of a compilation job in the background thread is tricky: there is just no way to foresee for sure whether investing time in optimizing a piece of code is worthwhile, and whether it should have been done earlier to reap the benefits. Formulating a heuristic solution to take care of that is even harder. A lot of fine tuning was necessary, and it is still work in progress.</p> 
 <p>- The life cycle of a piece of source code has already been complicated, with it going through interconnected states, like being lazily parsed, compiled for the first time using the fast compiler, then optimized by the optimizing compiler, then maybe deoptimized (if assumptions made at compile time break later on), etc.. With concurrent compilation, a couple of new states are added to this life cycle. Keeping track of all of them and ensure that transitioning between them is bug-free and efficient is non-trivial. Unexpected corner cases may cause problems.</p> 
</blockquote>
<p>According to Guo, “V8 is under active development and being steadily improved”, and that can be seen in the <a href="https://www.dartlang.org/performance/">live performance chart maintained by Dart</a> where V8 jumped 30% in the DeltaBlue benchmark on Feb. 11th, improvement resulting from compiler optimizations, not being related to background compilation.</p><br><br><br><br><br><br></body></html>
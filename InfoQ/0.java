<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Google, Opera Fork WebKit. Samsung Joins Firefox to Push Servo</h3><p> </p>
<p>There are two major browser developments recently announced, both targeting parallel architectures: Google and Opera with <a href="http://www.chromium.org/blink">Blink</a>, a WebKit fork, while Samsung joins Mozilla to push <a href="https://github.com/mozilla/servo">Servo</a> forward.</p> 
<p>Six weeks ago <a href="http://www.infoq.com/news/2013/02/Opera-WebKit-Presto;jsessionid=D70FE36F71A9AA3133220DEC004AAE1D">Opera embraced WebKit </a>leaving behind Presto, their own browser engine. Some wondered how less diversity is going to impact the web. They should worry no more because Google has forked WebKit, creating an abstract browser engine called <a href="http://www.chromium.org/blink">Blink</a>, whose development is to be integrated with Chromium which will provide one implementation of the platform. <a href="http://www.brucelawson.co.uk/2013/hello-blink/">Opera is joining Google in developing Blink</a>, announced Bruce Lawson, a Web Evangelist for Opera.</p> 
<p>Why would Google fork WebKit, a rendering engine that gained considerable momentum and had the chance to become perhaps the most important engine out there? <a href="http://www.chromium.org/blink/developer-faq">Google thinks</a> that while “monocultures seem good for developer productivity”, however, “monocultures inevitably lead to stagnation” on the long term, and “more options in rendering engines will lead to more innovation and a healthier web ecosystem.”</p> 
<p>According to Google, the two main technical reasons for forking WebKit are:</p> 
<ul> 
 <li>Chrome uses “a different multi-process architecture than other WebKit-based browsers” which has introduced complexity both in WebKit and Chrome, slowing down innovation.</li> 
 <li>Blink offers Google the option to improve the performance of their browser however they want, one of the main directions being parallel processing.</li> 
</ul> 
<p>In short, Google wants “to do for networking, rendering and layout what V8 did for JavaScript. Remember JS engines before V8? We want the same sort of healthy innovation that benefits all users of the web, on all browsers.”</p> 
<p>It seems that Google wants the freedom to move forward any way they want, not having to abide to WebKit’s development protocol, but rather enforcing the Chromium one where they have a lot more control. Other developers will have to comply with their guidelines in order to become <a href="http://dev.chromium.org/getting-involved/become-a-committer">committers</a> or <a href="http://dev.chromium.org/developers/owners-files">Owners</a> of Blink.</p> 
<p>The first step is to restructure the inherited WebKit code by removing “7 build systems and delete more than 7,000 files—comprising more than 4.5 million lines.” On the long term, Google has a list of improvements they want to introduce in Blink:</p> 
<ul> 
 <li><a href="http://www.chromium.org/developers/design-documents/oop-iframes">Out-of-process iframes</a>, enabling running different page components in separate sandboxed processes.</li> 
 <li>Faster and simpler networking which currently is limited by “old Mac WebKit API obligations which cannot be changed”.</li> 
 <li>Moving the “entire Document Object Model (DOM) into JavaScript. This has the potential to make JavaScript DOM access dramatically faster.”</li> 
</ul> 
<p>Google also considers the following <a href="http://www.chromium.org/blink#new-features">possible improvements</a>:</p> 
<blockquote> 
 <ul> 
  <li>Teach WebCore about multi-process history (currently it assumes same-process synchronous History access)</li> 
  <li>Delete the Widget tree (a Mac WebKit1 constraint)</li> 
  <li>Split WebCore into modules</li> 
  <li>Move code to directly using the sandbox Platform API directly instead of WebCore/platform where possible</li> 
  <li>Establish a simpler, stricter tree-gardening system that does not require 2 full time engineers per day</li> 
  <li>Experiment with moving the DOM into the JS heap</li> 
  <li>Increase multicore use (e.g., html parser, style engine, javascript parser)</li> 
  <li>Removing obscure parts of the DOM and make backwards incompatible changes to obscure parts of the DOM that benefit performance or remove complexity.</li> 
  <li>Use a modern, faster tcmalloc throughout all of Mac chrome</li> 
  <li>Experiment with incremental or parallel layout</li> 
  <li>Fix memory leaks by removing the ScriptValue/ScriptState abstractions now that there’s only one JavaScript engine.</li> 
  <li>Replace WebKitIDL with WebIDL and remove custom JavaScript bindings code</li> 
  <li>Bring WebCore up to speed with DOM3 Events / [DOM] UI Events.</li> 
 </ul> 
</blockquote> 
<p>A new browser engine raises concern among web developers who now have to make sure their code runs properly on yet another browser. Google tries to alleviate their fears by introducing development mechanisms similar to those implemented by Mozilla for Firefox:</p> 
<blockquote> 
 <p>Our goal is to drive innovation and improve the compatible, open web platform, not to add a ton of features and break compatibility with other browsers. We're introducing strong developer-facing policies on <a href="http://www.chromium.org/blink#new-features">adding new features</a>, the <a href="http://www.chromium.org/blink#vendor-prefixes">use of vendor prefixes</a>, and when a <a href="http://www.chromium.org/blink#compatibility">feature should be considered stable enough to ship</a>.</p> 
 <p>Today Firefox uses the Gecko engine, which isn’t based on WebKit yet the two have a high level of compatibility. We’re adopting a similar approach to Mozilla by having a distinct yet compatible open source engine. We will also continue to have open bug tracking and <a href="http://chromestatus.com/">implementation status</a> so you can see and contribute to what we’re working on at any time.</p> 
</blockquote> 
<p>An important policy is related to vendor prefixes, Google intending not to use them for new features:</p> 
<blockquote> 
 <p>Instead, we’ll expose a single setting (in about:flags) to enable experimental DOM/CSS features for you to see what's coming, play around, and provide feedback, much as we do today with <a href="https://plus.google.com/+GoogleChromeDevelopers/posts/ffDPaPAMkMZ">the “Experimental WebKit Features” flag</a>. Only when we're ready to see these features ship to stable will they be enabled by default in the dev/canary channels.</p> 
 <p>For legacy vendor prefixed features, we will continue to use the <code>-webkit-</code> prefix because renaming all these prefixes to something else would cause developers unnecessary pain. We've <a href="https://plus.google.com/+GoogleChromeDevelopers/posts/Rh1aMkzucgV">started looking into</a> real world usage of HTML5 and CSS3 features and hope to use data like this to better inform how we can responsibly deprecate prefixed properties and APIs. As for any non-standard features that we inherited (like <code>-webkit-box-reflect</code>), over time we hope to either help standardize or deprecate them on a case-by-case basis.</p> 
</blockquote> 
<p>Regarding Android and the mobile development in general,&nbsp;Google intends “to see that entire mobile web platform keeps pace with, and even anticipates [it].”</p> 
<p>One of Blink’s side effects is that WebKit will remain mainly in the hands of Apple. Will they be able to advance it fast enough to keep the pace with other browsers? We’ll see.</p> 
<p>A few hours before Google’s announcement regarding Blink, <a href="http://blog.mozilla.org/blog/2013/04/03/mozilla-and-samsung-collaborate-on-next-generation-web-browser-engine/">Mozilla announced</a> a partnership with Samsung to push forward the development of <a href="https://github.com/mozilla/servo">Servo</a>, a parallel browser project developed in <a href="http://www.infoq.com/news/2012/08/Interview-Rust;jsessionid=D70FE36F71A9AA3133220DEC004AAE1D">Rust</a>&nbsp;in an attempt to “take advantage of tomorrow’s faster, multi-core, heterogeneous computing architectures.” Servo is a “rebuild [of] the Web browser from the ground up” incorporating security mechanisms and support for massively parallel hardware.</p> 
<p>The first step is to make it run on Android/ARM, and Samsung’s main contribution so far has been an “ARM backend to Rust and the build infrastructure necessary to cross-compile to Android.”</p> 
<p>Servo is currently a prototype browser engine running on Mac OS X and Linux 64-bit, and will probably suffer from growing pains since the language it was written in is not yet mature. Mozilla has announced <a href="https://github.com/mozilla/rust/wiki/Doc-releases">Rust 0.6</a>&nbsp;the same day, but it will take at least a year until the language will reach stability, and during this time they are “racing to complete the first major revision of Rust – cleaning up, expanding and documenting the libraries, building out our tools to improve the user experience, and beefing up performance.”</p> 
<p></p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
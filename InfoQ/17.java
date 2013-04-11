<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Google's Go Readies 1.1 Release</h3><p style="margin-bottom: 0in"><span lang="en-US">As Google's Go programming language version 1.1 nears release, the developers have <a href="https://groups.google.com/d/msg/golang-nuts/bQDzp4IYI1o/zHOiBy5BvO0J" target="_top">announced</a> the release of the latest beta, providing a working preview of its new features. Not least among these is an estimated speed increase of 30%-40% in several use cases. Version 1.0 of Go was released a little over a year ago in March 2012, and to this point Google has released bug fixes </span><span lang="en-US">but </span><span lang="en-US">v</span><span lang="en-US">ersion 1.1 will bring <a href="http://tip.golang.org/doc/go1.1">new features</a> while upholding their commitment to backwards compatibility with 1.X version. The updates </span><span lang="en-US">affect</span><span lang="en-US"> the toolset, language features, and changes to the standard library.</span></p> 
<p style="margin-bottom: 0in"><b>New Language Features</b></p> 
<ul> 
 <li>Integer division by zero</li> 
 <li><a href="http://tip.golang.org/ref/spec#Method_values">Method values</a></li> 
 <li><span lang="en-US">Return requirements – Previously functions that returned a value required an explicit “return” or call to panic, this has been relaxed with the addition of <a href="http://tip.golang.org/ref/spec#Terminating_statements">terminating statements</a>.</span></li> 
</ul> 
<p style="margin-bottom: 0in"><b>Tools / Implementation</b></p> 
<ul> 
 <li>gccgo – <a href="http://www.infoq.com/news/2013/03/gcc48_released;jsessionid=3ECC5B5C4AB446BBCF20068385A2FAE8">Version 4.8 of GCC</a> (GNU Compiler Collection) released in March 2013 has partial Go 1.1 support, while the upcoming GCC 4.8.1 scheduled for release in May should provide complete 1.1 support.</li> 
 <li>int/unit on 64-bit implementations now defined as 64-bit. This could issues for programs expecting these types to only be 32-bit.</li> 
 <li>Heap size - On 64-bit systems this has been expanded to tens of gigabytes (exact size system dependent and not finalized)</li> 
 <li>go command 
  <ul> 
   <li>Error messages for compiling, testing, and running code are more descriptive</li> 
   <li>$GOPATH must be set in order to use go get, and it is no longer acceptable for it to be equal to $GOROOT</li> 
  </ul> </li> 
 <li>go fix has been adjusted to support migrating of code from 1.0.X to 1.1. (Pre 1.0.X code cannot be upgraded directly to Go 1.1)</li> 
 <li>Race detection – developers battling with race conditions will benefit from using new option<a href="http://tip.golang.org/doc/articles/race_detector.html"> -race</a> with go test. It is currently available for the 64-bit platforms Linux, OS X, and Windows.</li> 
</ul> 
<p style="margin-bottom: 0in">Go's developers report significant performance increases in several (but not all use cases). These increases are brought about by improvements to the compiler's code generation, a better map implementation, fewer context switches in networking applications, and an improved garbage collector.</p> 
<p style="margin-bottom: 0in"><span lang="en-US">Downloads for major platforms (Windows, Linux, OS X, etc) are <a href="https://code.google.com/p/go/downloads/list?q=go1.1beta2" target="_top">available</a> now for 1.1 Beta 2. Keep in mind that development is progressing at a brisk pace so newer versions can and will appear. Developers should be able to take advantage of the new 1.1 features by recompiling their existing code.</span></p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
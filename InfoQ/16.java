<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Rust 0.9 Released With Revised Threading Model</h3><p class="MsoNormal" style="margin-bottom: 0.0001pt;"><a href="http://www.rust-lang.org/">Rust</a>, the Mozilla-backed systems programming language, has released version 0.9, bringing with it a host of improvements as the language progresses towards the 1.0 milestone.&nbsp; Rust has been undergoing significant changes as it evolves into a language ready for long-term support and stability.&nbsp; Rust's creator Graydon Hoare has said the language targets <a href="http://www.infoq.com/news/2012/08/Interview-Rust"><span class="InternetLink">“frustrated C++ developers”</span></a> as it focuses on its goal to be a modern replacement for C/C++.</p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">
 <o:p></o:p></p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">&nbsp;</p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">Rust is an open source language with a <a href="http://static.rust-lang.org/dist/rust-0.9-install.exe">binary installer</a> available for Windows and a <a href="http://static.rust-lang.org/dist/rust-0.9.tar.gz">source package</a> available for UNIX based systems (FreeBSD, Mac OS X, and Linux). 
 <o:p></o:p></p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">&nbsp;</p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">Release 0.9 marks the inclusion of several features:
 <o:p></o:p></p>
<ul> 
 <li>Rust now provides the <a href="http://static.rust-lang.org/doc/master/rust.html#linkage">choice</a> for developers to choose whether to build dynamic or statically linked libraries.
  <o:p></o:p></li> 
 <li>Native libraries are now first-class citizens, allowing a Rust library to be built and distributed without requiring the accompaniment of native libraries.
  <o:p></o:p></li> 
 <li>The I/O infrastructure has been completely revised.&nbsp; Logistically, all I/O functionality is now located in the module <b>std::io</b>.&nbsp; The comm module (providing high level communication abstractions) has been rewritten.
  <o:p></o:p></li> 
 <li>Several of the I/O changes come from the creation of two new libraries, libgreen and libnative.&nbsp; The Rust standard library is no longer set to a particular scheduling method, so your program can run m:n (m application threads map onto n kernel threads) or 1:1&nbsp; (one application thread for each kernel thread).&nbsp; This allows developers to choose the threading model that will provide the best performance for their application.
  <o:p></o:p></li> 
 <li>Rust developers should note the deprecation of managed pointers (signified by the @ sigil) and transition code to using Rc (reference counted pointers) or Gc (garbage collected pointers).
  <o:p></o:p></li> 
</ul>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">For complete details refer to the official Rust 0.9 <a href="https://github.com/mozilla/rust/wiki/Doc-detailed-release-notes#09-january-2014">release notes</a>.&nbsp; Developers looking to learn more about this language have several different resources available in addition to the official <a href="http://static.rust-lang.org/doc/0.9/tutorial.html">Rust Tutorial</a>:&nbsp; Rust is being taught at the University of Virginia in an <a href="http://rust-class.org/pages/using-rust-for-an-undergraduate-os-course.html">undergraduate OS course</a> and Steve Klabnik has recently prepared “<a href="http://words.steveklabnik.com/a-30-minute-introduction-to-rust">A 30 minute introduction to Rust</a>”.&nbsp;&nbsp;
 <o:p></o:p></p><br><br><br><br><br><br></body></html>
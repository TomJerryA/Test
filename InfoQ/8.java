<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Visual Studio's C++14 Support Grows</h3><p class="Standard">Back in July, Microsoft had <a href="http://www.infoq.com/news/2013/07/vs2013_CPP_compliance">released</a> a roadmap for the integration of modern C++ into Visual Studio.&nbsp; At that time it solidified what C++ language features would be available in VS2013, and now a new CTP is available bringing VC++ closer to C++14 compliance.
 <o:p></o:p></p>
<p class="Standard">Titled <a href="http://www.microsoft.com/en-us/download/details.aspx?id=41151">Visual C++ Compiler November 2013 CTP</a>, this package provides the following features: 
 <o:p></o:p></p>
<blockquote> 
 <ul> 
  <li>Implicit move special member function generation (thus also completing =<i>default</i>) 
   <o:p></o:p></li> 
  <li>Reference qualifiers on member functions (a.k.a. <i>&quot;&amp; and &amp;&amp; for *this&quot;</i>) 
   <o:p></o:p></li> 
  <li>Thread-safe function local static initialization (a.k.a. &quot;magic statics&quot;) 
   <o:p></o:p></li> 
  <li>Inheriting constructors 
   <o:p></o:p></li> 
  <li><i>alignof/alignas</i> 
   <o:p></o:p></li> 
  <li><i>__func__</i> 
   <o:p></o:p></li> 
  <li>Extended <i>sizeof</i> 
   <o:p></o:p></li> 
  <li><i>constexpr</i> (except for constructors) 
   <o:p></o:p></li> 
  <li><i>noexcept</i> (unconditional) 
   <o:p></o:p></li> 
  <li>C++14 <i>decltype</i>(auto)
   <o:p></o:p></li> 
  <li>C++14 <i>auto</i> function return type deduction 
   <o:p></o:p></li> 
  <li>C++14 generic lambdas (with explicit lambda capture list) 
   <o:p></o:p></li> 
  <li>(Proposed for C++17) Resumable functions and <i>await</i>
   <o:p></o:p></li> 
 </ul> 
</blockquote>
<p class="Standard">An important detail for early-adopters interested in this package—it does not include a “Go Live” license meaning it cannot be used for production code deployment.&nbsp; According to Microsoft’s Stephen T. Lavavey, a “Go Live” license will not be available with this or future VC++ CTPs for VS2013.&nbsp; In short VS Next will be the soonest these features will be available for use in a production setting.&nbsp; Also per <a href="http://blogs.msdn.com/b/vcblog/archive/2013/11/18/announcing-the-visual-c-compiler-november-2013-ctp.aspx?PageIndex=2#comments">Lavavey</a>, the following C++11 core language features remain outstanding: “expression SFINAE, attributes (including those for data-dependency ordering), constexpr on member functions, char16_t/char32_t, Unicode string literals, universal character names in literals, user-defined literals, inline namespaces, unrestricted unions, conditional noexcept, thread_local, [and] a C99-conformant preprocessor…”
 <o:p></o:p></p>
<p class="MsoNormal">Microsoft has <a href="http://aka.ms/I0w822">produced</a> a document listing some of the pain points that you may encounter when using this CTP.&nbsp; Notably the new keywords are not supported by IntelliSense and some areas of the IDE.&nbsp; Additional areas to be aware of are that the <i>await</i> keyword requires Windows 8.1 and when using destructors with the CTP, avoid throwing exceptions.</p><br><br><br><br><br><br></body></html>
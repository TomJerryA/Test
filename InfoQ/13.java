<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Unsafe at any Speed; Oracle Surveys community about promoting sun.misc.Unsafe</h3><p>Oracle software engineer Paul Sandoz posted a message on the <a href="http://mail.openjdk.java.net/pipermail/core-libs-dev/2014-January/024650.html">OpenJDK mail list </a>and sent <a href="https://twitter.com/PaulSandoz/status/426732263888662528"> a tweet</a> last week asking the public to weigh in on the library <a href="http://www.docjar.com/docs/api/sun/misc/Unsafe.html">sun.misc.Unsafe</a> by responding to a Survey Monkey <a href="https://www.surveymonkey.com/s/sun-misc-Unsafe">survey</a>.</p>
<p>The debate centers around whether pieces of Unsafe should be mainstreamed. The controversial class is under scrutiny due to its divergence from the Java credo of safe memory management.</p>
<p>sun.misc.Unsafe has over 100 methods, in categories such as synchronization, direct memory access, object and member manipulation, and other categories antithetical to the Java credo of safe memory management. Some of these methods such as&nbsp;volatile reads and writes, ordered writes and compare-and-swap operations are heavily used by the java.util.concurrent libraries.</p>
<p>According to the Java doc, Unsafe contains &quot;A collection of methods for performing low-level, unsafe operations. Although the class and all methods are public, use of this class is limited because only trusted code can obtain instances of it.&quot;</p>
<p>For a &quot;quick overview of&nbsp;sun.misc.Unsafe&nbsp;<em>public</em>&nbsp;API and few interesting cases of its usage.&quot; refer to Mykhailo Kozik's <a href="http://mishadoff.github.io/blog/java-magic-part-4-sun-dot-misc-dot-unsafe/">blog on the topic.</a></p>
<p>The survey questions are:</p>
<ol> 
 <li>Have you ever used the Java class &quot;sun.misc.Unsafe&quot;?</li> 
 <li>What project(s) did you use Unsafe for?</li> 
 <li>What methods on Unsafe did you use?</li> 
 <li>What reasons did you use Unsafe for? Responses include: 
  <ul> 
   <li>Atomic access to fields and array elements (such as compare-and-swap)</li> 
   <li>Off-heap memory operations (such as to emulate structures or packed objects)</li> 
   <li>Deserialization hacks</li> 
   <li>Fencing (to constrain re-ordering of memory operations)</li> 
   <li>Access to private fields of another class</li> 
   <li>Array access without bounds checks</li> 
   <li>Other (please specify)</li> 
  </ul> </li> 
 <li>What features (if any) are missing from Unsafe?</li> 
 <li>Do you have an optional dependency on Unsafe to ensure code is portable across multiple Java platforms?</li> 
 <li>If there was a &quot;safe unsafe&quot; standard (cross-platform) alternative for your use-cases (perhaps a new API, perhaps language changes, or both) would you be prepared to replace Unsafe with that alternative? If so under what conditions?</li> 
</ol>
<p>In addition to soliciting community response to determine usage metrics, Sandoz says Oracle is also planning to &quot;trawl stuff on repos.&quot;</p>
<p>The low-latency world seems particularly passionate about the topic. Peter Lawrey is Principal Consultant at <a href="http://www.linkedin.com/company/higher-frequency-trading-ltd">Higher Frequency Trading Ltd.</a> and lead developer of the low-latency <a href="https://github.com/OpenHFT">OpenHFT libraries</a>. He told InfoQ:</p>
<blockquote>
 While Unsafe should be hidden from most developers and most of the code, it provided some particularly useful low level, thread safe access to memory which is more efficient than JNI calls. i.e. there really is no other way to do what Unsafe does efficiently. &nbsp;What we need is a replacement which is standard across JVMs and can be extended for newer technologies such as Hardware Transaction Memory e.g. Intel TSX.
</blockquote>
<p>Ben Cotton, an active member of the <a href="https://groups.google.com/forum/#!forum/mechanical-sympathy">Mechanical Sympathy low-latency</a>&nbsp;community forum, told InfoQ:</p>
<blockquote>
 FUD (and, frankly, outright technical bigotry) results when the only route to the most complete memory allocation management capabilities is exposed through a package named 'Unsafe'. As proposed by the new 
 <a href="http://openjdk.java.net/jeps/0">JEPs</a> for 
 <a href="https://groups.google.com/forum/#!forum/jep-off-heap">Off-Heap</a> and 
 <a href="https://groups.google.com/forum/#!forum/jvm-ffi">FFI</a> (Foreign Functional Interface), let's get rid of this awful name and instead promote the competent (and thus safer) usage of this package as a means to solve important Java performance problems;
</blockquote>
<p>Christoph Engelbert solution architect at <a href="http://www.hazelcast.com/">Hazelcast</a>, the popular open source in-memory data grid vendor told InfoQ:</p>
<blockquote>
  A public API with the feature set of sun.misc.Unsafe will be for Java 9 what Lambdas is for Java 8 - not as commonly used but just as important. Apache DirectMemory and Lightning as well as Hazelcast heavily using sun.misc.Unsafe for speeding up serialization, memory access and lowering pressure on the Garbage Collector (with off heap data structures). It is a must have feature!&quot; 
</blockquote>
<p>&nbsp;</p>
<p>According to Sandoz the survey will close on Feb 7, 2014.</p><br><br><br><br><br><br></body></html>
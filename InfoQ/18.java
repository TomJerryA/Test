<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Will Java 8 solve PermGen OutOfMemoryError?</h3><p>As part of Oracle's ongoing project to merge the HotSpot and JRockit codebases, Oracle has announced that <a href="https://blogs.oracle.com/java/entry/java_7_questions_answers">they will remove PermGen</a> from the Java 8 version of the HotSpot JVM. Many people however have interpreted this announcement in a way that all their PermGen errors will disappear. Because the effects of the removal of PermGen can now be checked with <a href="http://jdk8.java.net/download.html">Java 8 Early Access</a> builds, it is time to find out if all PermGen problems have been resolved.</p> 
<h3>What is the PermGen?</h3> 
<p>Jon Masamitsu, JVM developer at Oracle, explained 2006 in his blog the <a href="https://blogs.oracle.com/jonthecollector/entry/presenting_the_permanent_generation">purpose of the permanent generation</a>: The permanent generation contains information about classes, such as bytecode, names and JIT information. It is stored in a separate space, because it is mostly static and garbage collection can be much more optimized by separating it.</p> 
<h3>The Problems with PermGen</h3> 
<p>Many developers find their system showing &quot;java.lang.OutOfMemoryError: PermGen space&quot; at some time. When it does, it is very often caused by a memory leak related to classloaders, and creation of new classloaders, which generally happens during hot deployments of code. This is why it is more frequent on development machines, than in production. When it occurs in production, developers can take the generated heap dump and use a tool like <a href="http://www.eclipse.org/mat/">Eclipse Memory Analyzer Toolkit</a> to look for classloaders that should be gone but are not. The permanent collection is garbage collected, unless specific configuration prevents it. However, in the case of leaks, there is just nothing to collect. In production the most common &quot;problem&quot; is that the default value 64MB is way too low. Setting it to 256MB is the usual band aid to resolve it.</p> 
<h3>What Java 8 changes</h3> 
<p>In his <a href="http://mail.openjdk.java.net/pipermail/hotspot-dev/2012-September/006679.html">mail on the HotSpot development list</a>, Jon now explains what Java 8 will change: with Java 8, there is no PermGen anymore. Some parts of it, like the interned Strings, have been moved to regular heap already in Java 7. In 8 the remaining structures will be moved to a native memory region called &quot;Metaspace&quot;, which will grow automatically by default and will be garbage collected. There will be two flags: <code>MetaspaceSize</code> and <code>MaxMetaspaceSize</code>.</p> 
<p>Jon Masamitsu explains the design goal behind this on request by InfoQ:</p> 
<blockquote> 
 <p>A goal for removing perm gen was so that users do not have to think about correctly sizing it.</p> 
 <p>Set MetaspaceSize to a value larger than the default, if you know that your applications needs more space for class data. Setting it to a larger size will avoid some number of GC's at startup. It is not necessary and I do not particularly recommend it unless you want to avoid as many GC's as possible.</p> 
 <p>Set MaxMetaspaceSize if you want to limit the space for class data. You might want to do this if you suspect you are leaking classloaders and want the application to stop before it uses up too much native memory. Another case might be where you have multiple applications running on a server and you want to limit how much space each uses for class data.</p> 
</blockquote> 
<p>So <code>MetaspaceSize</code> falls in the category of potentially affecting the first few Garbage Collections and should not be important in most cases. In that way it reflects the purpose of the old <code>PermSize</code>; flag.</p> 
<p>When <code>MaxMetaspaceSize</code> is set, the space can still run out of memory, which will cause a &quot;java.lang.OutOfMemoryError: Metadata space&quot;. Due to the fact that classloader leaks exist, and consuming unlimited native memory is something Java typically does not do, it seems sensible to set a similar limit to what was set with <code>MaxPermSize</code>. Similar to the PermGen, verbose GC logging will print the current consumption of Metaspace. Using the command line flags <code>PermSize</code> or <code>MaxPermSize</code> will result in a warning, instructing the user to switch to the Metaspace flags.</p> 
<h3>Conclusion</h3> 
<p>Because the concept of Metaspace and perm is mostly the same, an administrator performing a Java 7 to Java 8 upgrade can change the flags simply by running <code>sed 'e/Perm/Metaspace/g'</code>.</p> 
<p>Overall, this change looks underwhelming. For most cases, it is just a name change. Making the Metaspace unbounded by default prevents choosing a too small default, but requires setting a maximum to ensure system stability. Luckily, we can reuse the configuration of PermSize and MaxPermSize almost everybody already uses and just rename the flag. Unfortunately the move from managed java heap to native memory means that there is a lot less valuable troubleshooting information in a heap dump, as also Kirk Pepperdine <a href="http://mail.openjdk.java.net/pipermail/hotspot-dev/2012-September/006684.html">raised as concern</a>.</p> 
<p>In the end, classloader leaks can still occur as before.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
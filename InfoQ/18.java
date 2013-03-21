<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Interview with Neil Bartlett about OSGi and the new Bndtools 2.0 release</h3><p>Neil Bartlett, preeminent OSGi expert and current maintainer of the popular Bndtools Eclipse plugin for OSGi <a href="http://njbartlett.name/2013/02/11/bndtools2-released.html">has announced the release of Bndtools 2.0</a>. Some of the features he has highlighted are:</p> 
<ul> 
 <li>Support for OSGi Release 5 Resolver and Repository specifications</li> 
 <li>Export run descriptors as standalone executables</li> 
 <li>Baselining (build errors for incorrectly versioned bundles)</li> 
 <li>Enhanced Semantic Versioning, using annotations for Consumer and Provider roles</li> 
 <li>Exported Package Decorations</li> 
 <li>Improved Incremental Builder</li> 
 <li>Support for Apache ACE</li> 
 <li>Lots of bug fixes and performance improvements.</li> 
</ul> 
<p>This is a long awaited release. The previous release 1.1 became available in March 2012.</p> 
<p>InfoQ spoke to Neil Bartlett about Bndtools and about OSGi in general.</p> 
<p><b>Can you please explain a bit about OSGi and Bndtools to the non-OSGi audience?</b></p> 
<blockquote> 
 <p>OSGi is a way of developing modular applications on the JVM. It allows you to build modules (which we call &quot;bundles&quot;) that are cleanly isolated from each other, and with explicit, managed dependencies. Because of our focus on dependencies, we can always tell whether a particular bundle can be installed into our environment, whether additional dependencies will need to be added as well, what effect it will have on other modules, and so on.</p> 
 <p>Bndtools is an IDE for developing OSGi bundles and applications. It is based on Eclipse, and can be installed from the Eclipse Marketplace.</p> 
</blockquote> 
<p><b> Is OSGi important to Java projects of all sizes and kinds, or is it more appropriate to larger or smaller projects? </b></p> 
<blockquote> 
 <p>OSGi means modularity, which is beneficial to almost all sizes of projects. It should be clear enough why large projects benefit from modularity: it helps to isolate complexity and divide the work into manageable chunks. But even small projects benefit, for example if you write a small piece of code it's likely that you will want to reuse it later in another project. If you develop that as an OSGi bundle then it will be much easier to reuse.</p> 
 <p>Having said that, some very small projects don't really need modularity; for example &quot;Hello World&quot; doesn't benefit much from a modular approach!</p> 
</blockquote> 
<p><b> OSGi seems to have some loyal followers, but it does not seem to have huge traction. What is the reason for that?</b></p> 
<blockquote> 
 <p>Well, the traction is increasing fast, but I agree it's not mainstream yet. OSGi is actually very ambitious because it aims to improve the entire software development process, therefore it has an impact on everything from code repositories through testing to team structures. So it takes time for the benefits to be realized, and many businesses are understandably nervous about taking on a known up-front cost in return for uncertain future gains. However this is changing as more businesses become successful with it.</p> 
 <p>Another problem is technical, in that OSGi has had quite poor tool support for a long time. Bndtools – and the ecosystem of tools that can integrate with it – have started to improve that situation.</p> 
</blockquote> 
<p><b> There is a lot of focus on Android right now, is OSGi relevant for Android development?</b></p> 
<blockquote> 
 <p>Yes, I think that as Android applications get bigger and more complicated, they are going to need to look at modularity seriously as well. OSGi has been used successfully in some Android projects, however Android is sufficiently different from standard Java – in subtle but important ways – that this is still a bit of an experimental area right now.</p> 
</blockquote> 
<p><b> How does Bndtools help in OSGi projects?</b></p> 
<blockquote> 
 <p>OSGi has a reputation for being difficult to use, however it really just needs certain information about our code to be stated explicitly. Nearly all of this information is available inside the Java classes that we put into the bundle... it just needs to be teased out. Bndtools does this as part of the build process, which allows developers just to concentrate on their own code and not repeat anything they have already written into the source.</p> 
 <p>Bndtools also hooks into the Eclipse build system, which means that as soon as you save a change in a source file, your bundle will be immediately built and ready. Then if you happen to have an OSGi runtime going already (e.g. in debugging or testing) then we push the new bundle straight into it, by taking advantage of OSGi's ability to dynamically update modules at runtime. This leads to an extremely fast code/run/test workflow, since basically your code is already running as soon as you save it.</p> 
 <p>Finally in Bndtools 2.0 we added support for the new Resolver and Repositories specifications from OSGi Release 5. This lets you compose applications by focusing on the small number of &quot;top-level&quot; modules that provide your core functionality – the resolver takes care of providing all of the static and runtime dependencies from that core. So you no longer have to manage long lists of JARs that need to go on your classpath.</p> 
</blockquote> 
<p><b> Does Bndtools provide any collaboration tools?</b></p> 
<blockquote> 
 <p>Yes. One of the major difficulties in collaborating with other developers is maintaining compatibility of shared APIs, and how to coordinate when those APIs need to change. The key to getting this right is a proper versioning strategy, but most developers apply versions to their artifacts in a manual and fairly arbitrary way. Bndtools has the ability to analyze your classes and work out the changes that were made compared with the previously released version. Then it can automatically bump the version for you. Also for consumers of an API it works out what range of versions your code is going to be compatible with, and automatically generates an import of that range.</p> 
</blockquote> 
<p><b> Are there any competitors?</b></p> 
<blockquote> 
 <p>Probably the closest competitor is PDE, the Plug-in Development Environment, which is also an Eclipse-based IDE but takes a very different approach. Naturally I believe that Bndtools is much better and more productive; in fact I'm confident of this because I used PDE for many years before Bndtools existed.</p> 
</blockquote> 
<p><b> Is Eclipse required, or does it standalone? Do you support other IDEs such as IntelliJ and Netbeans?</b></p> 
<blockquote> 
 <p>Yes and no. Bndtools is built on top of bnd, developed by Peter Kriens. Bnd is a headless tool that can be used from the command line, or from ANT, or from Maven, and so on. Therefore developers using NetBeans, IDEA or even a plain text editor can still work with the projects because they are just using bnd.</p> 
 <p>Bndtools does require Eclipse and it isn't directly usable in other IDEs. However those IDEs could build their own support for OSGi by using bnd themselves. Most of the smarts are in bnd, and Bndtools only provides things like pretty editors for the bnd descriptor files, a launcher, hooks into the Eclipse build lifecycle, and so on.</p> 
 <p>I hope that other IDEs spend some effort on this, because really I just want people to use OSGi. I have no interest in forcing them to use Eclipse if that is not their preference.</p> 
</blockquote> 
<p>As well as the <a href="http://bndtools.org/tutorial.html">Bndtools Tutorial</a> Bartlett recommends the books &quot;Java Application Architecture&quot; by Kirk Knoernschild (<a href="http://www.infoq.com/articles/java-application-architecture;jsessionid=A13391743906C744C8E206C6FD97D9A8">previously covered on InfoQ</a>) and &quot;Enterprise OSGi in Action&quot; by Tim Ward and Holly Cummins, which discusses tooling options for OSGi including bnd and Bndtools, as good sources for further information.</p> 
<p>InfoQ has also run a series of articles discussing modularity in general:&nbsp;<a href="http://www.infoq.com/articles/modular-java-what-is-it;jsessionid=A13391743906C744C8E206C6FD97D9A8">Modular Java: What is it?</a>, <a href="http://www.infoq.com/articles/modular-java-static-modularity;jsessionid=A13391743906C744C8E206C6FD97D9A8">Modular Java: Static Modularity</a>, <a href="http://www.infoq.com/articles/modular-java-dynamic-modularity;jsessionid=A13391743906C744C8E206C6FD97D9A8">Modular Java: Dynamic Modularity</a>, <a href="http://www.infoq.com/articles/modular-java-declarative-modules;jsessionid=A13391743906C744C8E206C6FD97D9A8">Modular Java: Declarative Modularity</a>.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Groovy Now Runs on Android</h3><p>During the recent <a href="http://gr8conf.eu/#/">GR8Conf Europe 2014</a>, C&eacute;dric Champeau, Senior Software Engineer working on Groovy for SpringSource/Pivotal, has performed a <a href="https://plus.google.com/116089789718222474948/posts/1CrdnBP3tuF">live merging of the pull request that brings support for Groovy on Android</a>.&nbsp;</p>
<p>Groovy developers have waited for this option for several years, its implementation being delayed by difficulties introduced by the different bytecode format used by Android Dalvik' VM and the dynamic nature of Groovy's code. Official support for Android will be made available in Groovy 2.4.</p>
<p>InfoQ has interviewed Champeau to find out more about this and the future of Groovy on Android.</p>
<p><b>InfoQ: What was the hardest part in making Groovy work on Android?</b></p>
<blockquote> 
 <b>CC:&nbsp;</b>There were actually multiple issues, and that's the combination that made it a bit hard. The first issue is that Groovy is a dynamic language which is generating classes at runtime. The problem is that those classes are generated using the &quot;standard&quot; JVM format, although Android uses its own class format (for the Dalvik VM). The Dalvik VM is not meant to create classes at runtime, and it makes it very hard, because each file using the standard JVM bytecode needs to be processed through the &quot;dex&quot; tool to be loadable. Even if you manage to do it on the device, it's still a pain to load a class at runtime. It requires, for example, writing a class in a jar file, then loading this jar. In the end, we decided that it wasn't the main focus for Groovy on Android, and that we would rather focus on writing a full application in Groovy, without involving the creation of any class at runtime. This means that there are some limitations, but they should be invisible for most of the users. In the end, if you use the @CompileStatic to have statically compiled Groovy on Android, performance, as well as memory consumption, is comparable, or the same as native Android applications.
 <br /> 
 <br /> The second issue was actually with the build system. The new Android build system uses Gradle and a custom plugin, &quot;android&quot;, which bypasses the normal &quot;java&quot; and &quot;groovy&quot; plugins to offer functionalities like the application variants. It required a bit of work to figure out how we could plug into it to add Groovy support. The good thing is that since the announcement, a Gradle plugin for Groovy and Android was released and makes things easier [1]. Last but not least, I learnt Android as I was writing support for Groovy. That was a good thing, because I could see where you could benefit from using Groovy, but it actually took me more time than adapting Groovy itself! 
</blockquote>
<p><b>InfoQ: Any chance to extend this work to iOS or at least Windows Phone for a cross platform solution?</b></p>
<blockquote> 
 <b>CC:&nbsp;</b>I would definitely love to see Groovy on iOS, but I have no hardware to test it ;) Even if the recently announced Swift language looks very close to Groovy and is far more appealing than Objective-C, people could use it as a substitute for Groovy. But, there's one thing to consider: Swift is closed software and in the line of vendor lock-in. Groovy is totally open-source, and if you could use the same code for both iOS and Android, people would mostly only have to rewrite the UI part of their applications for example, making it a better fit for generic mobile development. As for Windows Phone, I have no idea if it is doable, I'm lacking knowledge on the platform actually :)
</blockquote>
<p><b>InfoQ: What are the current shortcomings? What's not working yet?</b></p>
<blockquote> 
 <b>CC:&nbsp;</b>Until very recently, only @CompileStatic classes could run on Android. But it is now possible to run dynamic code too, so pretty much everything works, including builders. It should be known that using dynamic code should be limited to non CPU intensive parts of the application, since it involves reflection. That said, the current limitation is that it is not (easily) possible to generate classes at runtime, so some specific constructs like map to class coercion or runtime traits will not work. The good thing is that there are workarounds for this. Eventually, there's also the problem of the number of method descriptors. Android, by default, has a limitation of 65536 methods in total, which is pretty low, and Groovy would consume around 8k without optimizations (with ProGuard, for example). So this means that you can reach the limit faster than with a normal Java application, even though there are ways to work around thing (such as using the multidex option).
</blockquote>
<p><b>InfoQ: Any plans for the future of Groovy/Android?</b></p>
<blockquote> 
 <p><b>CC: </b>Official support for Android will come with a first beta of Groovy 2.4. Currently, you can already use it for your own applications, and it's actually already on production, as the first example app shows ([2]). Only it's based on a snapshot version of Groovy. But what I would really like to see is new libraries or frameworks written in Groovy that facilitate Android application development. Android is very verbose and Groovy can make things much easier to write. For that, we can rely on a large community of developers who have already written lots of libraries like this for Java, so it's only a matter of time. I am convinced that once users will have tasted Groovy on Android, it's pretty unlikely they will switch back to Java ;)</p> 
</blockquote>
<p>[1] <a href="https://github.com/melix/groovy-android-gradle-plugin">https://github.com/melix/groovy-android-gradle-plugin</a></p>
<p>[2] <a href="https://play.google.com/store/apps/details?id=me.champeau.gr8confagenda.app">https://play.google.com/store/apps/details?id=me.champeau.gr8confagenda.app</a></p><br><br><br><br><br><br></body></html>
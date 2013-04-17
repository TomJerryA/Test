<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>IntelliJ IDEA 12.1 Lands with JavaFX 2.0 Support</h3><p>JetBrains has begun shipping IntelliJ IDEA 12.1 which sees the IDE gaining full support for JavaFX 2.0, the latest incarnation of the Java client platform. This includes &quot;support for FXML mark-up, custom CSS, code completion, navigation and search, refactoring, packaging tools and integration with scene builder&quot; the <a href="http://www.youtube.com/watch?v=omuW5M1_s2E&amp;feature=player_embedded">accompanying video</a> states.</p> 
<p>With Java 7 installed, the IDE offers a template for creating a new &quot;hello world&quot; type sample JavaFX application. The sample comprises an .fxml file describing the layout, a controller with handler, and a main class. You can immediately click &quot;run&quot; to see the results. Working with the project provides all the support you would expect with code completion, &quot;quick fix&quot; suggestions, and so on.</p> 
<p>JetBrains doesn't provide its own graphical UI designer tool for JavaFX. Instead it has opted to integrate Oracle's <a href="http://www.oracle.com/technetwork/java/javafx/tools/index.html">Scene Builder</a>. So you can open a scene in Scene Builder, make changes and have those reflected in IDEA. You can, of course, edit a scene manually directly in the IDE.</p> 
<p>IntelliJ comes with some packaging capabilities for JavaFX built in as well, although this still feels a little like work in progress. As it stands, for example, the IDE doesn't directly support native packaging via the UI; you need to resort to using JavaFX Ant tasks for this. We contacted JetBrains for clarification on plans here, but haven't had a response at the time of publication. <a href="http://blogs.jetbrains.com/idea/2013/03/packaging-javafx-2-applications-in-intellij-idea-121/#comments">This blog thread</a>, however, suggests that this will be addressed in version 12.1.2. We will update the post if we hear back from JetBrains.</p> 
<p>It is also worth noting that, whilst JavaFX support is included in the free Community Edition of IDEA, JavaFX CSS support is not. This is because it relies on CSS support, which is an Ultimate only feature.</p> 
<p>Aside from JavaFX 2, Gradle support has also received attention with a couple of new options:</p> 
<p><a href="/resource/news/2013/04/idea-121/en/resources/gradle.jpg;jsessionid=D25D332127CC604AE3549F0036E30080"><img src="http://www.infoq.com/resource/news/2013/04/idea-121/en/resources/gradle.jpg;jsessionid=D25D332127CC604AE3549F0036E30080" alt="Gradle Properties" _href="img://gradle.jpg" _p="true" /></a></p> 
<p>If &quot;Use Gradle Wrapper&quot; is selected, the IDE automatically detects if the linked Gradle project is <a href="http://www.gradle.org/docs/current/userguide/userguide_single.html#gradle_wrapper">wrapper-aware</a> and uses it for refreshing the project and running tasks. &quot;Use auto-import&quot; means that every project structure change is automatically picked up by the IDE on Gradle project refresh (e.g. when a new library is added/removed at build.gradle, it's added/removed at the IDE as well).</p> 
<p>There are also a number of smaller improvements, with lots of specific items for individual JVM languages. Both Community and Ultimate versions gain:</p> 
<ul> 
 <li>Full screen mode for Windows</li> 
 <li>Groovy 2.1 support, including new annotations and compilation customisation.</li> 
 <li>Improved Scala support (statement completion and a new compiler)</li> 
</ul> 
<p>The Ultimate version also sees:</p> 
<ul> 
 <li>Spring Framework 3.2 and Play Framework 2.1 support</li> 
 <li>Adobe Gaming SDK support</li> 
 <li>Debugger for CoffeeScript, Dart and TypeScript via Source Maps</li> 
 <li><a href="http://sass-lang.com/">Sass</a> (&quot;Syntactically Awesome Stylesheets&quot;) support improvements (custom function definition, completion, rename refactoring, nested properties, etc.)</li> 
</ul> 
<p>Finally, adopters of Apple's MacBook Pro Retina will no doubt be pleased to hear that the Darkula theme has <a href="http://www.jetbrains.com/idea/features/darcula_retina.html">improved support</a> for high-DPI displays.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Creating Single Page Apps With Angular.JS and ASP.NET</h3><p class="MsoNormal">Wednesday’s Build sessions included a presentation by David Catuhe and Jon Galloway on incorporating <a href="http://angularjs.org/">AngularJS</a> into ASP.NET applications.&nbsp; The resulting setup provides a way for developers to quickly build modern single-page web applications.&nbsp; 
 <o:p></o:p>
 <o:p>
  &nbsp;
 </o:p></p>
<p class="MsoNormal">Angular was created by Google and is now operated as an open source project that they support.&nbsp; As its name implies, it is a JavaScript-based library that follows the Model View Controller (MVC) design pattern.&nbsp; As Catuhe and Galloway explain, Angular uses dependency injection to power your ASP.NET application.&nbsp; A single file, <code>angular.min.js</code>, is the only one needed to enable support.&nbsp; (NuGet users can <a href="http://www.nuget.org/packages/angularjs/">grab</a> the latest version (beta) or the stable release.)
 <o:p></o:p></p>
<p class="MsoNormal">They point out that Angular usage is not an all-or-nothing approach, if you prefer to only utilize its functionality on selected portions of your page that is a supported possibility.&nbsp; In any event, Catuhe and Galloway recommend creating an “apps” directory under your Scripts folder for your project to help organize your files.
 <o:p></o:p></p>
<p class="MsoNormal">An important word of caution about minification:&nbsp; by default using minification on your app’s code will break as it will interfere with Angular’s dependency injection.&nbsp; (The tutorial documentation for Angular has <a href="http://docs.angularjs.org/tutorial/step_05">more details</a> on this under the “A Note on Minification” section.)
 <o:p></o:p></p>
<p class="MsoNormal">To actually activate Angular within your webpage, add “ng-app” to your html tag:
 <o:p></o:p></p>
<p><code> </code></p>
<p class="MsoNormal"><code>&lt;html ng-app … &gt;
  <o:p></o:p></code></p>
<p><code> </code></p>
<p>&nbsp;This lets Angular know it should get ready to do something.&nbsp; Angular uses <code>$http</code> for loading files by using its own lightweight version of jQuery.&nbsp; If your project already has a copy of jQuery installed, Angular will instead use that version to be consistent.
 <o:p></o:p>
 <o:p>
  &nbsp;
 </o:p></p>
<p class="MsoNormal">Catuhe and Galloway proceeded to demo their sample application, a single page application (SPA) based on displaying and storing information about Magic: The Gathering cards.&nbsp; SPA’s use a view to build the UI, and Angular itself uses routing to define these views</p>
<p class="MsoNormal">Since deep links in Angular can conflict with MVC Routes, they suggest using a Catchall route:
 <o:p></o:p></p>
<p>&nbsp;</p>
<blockquote>
 <code> <p class="MsoNormal">routes.MapRoute(<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; name: &quot;Catch all route for SPA&quot;,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; url: &quot;App/{*catchall}&quot;,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; defaults: new{<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; controller = &quot;Home&quot;, <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; action = &quot;Index&quot;});
   <o:p></o:p></p> </code>
</blockquote>
<p>&nbsp;</p>
<p class="MsoNormal">Another tip for displaying HTML.&nbsp; If the HTML is generated from a view, proceed without difficulty.&nbsp; However if the HTML is coming from a file (MyHTML.html) then use an IIS Rewrite rule to change the URL:
 <o:p></o:p></p>
<p><code> </code></p>
<p class="MsoNormal"><code>/myHTML.html -&gt; /myHTML
  <o:p></o:p></code></p>
<code> </code>
<p></p>
<p class="MsoNormal">To see their demo application in action, consult the presentation’s <a href="http://channel9.msdn.com/Events/Build/2014/3-644">Channel9 page</a> for more information.
 <o:p></o:p></p>
<p>&nbsp;</p><br><br><br><br><br><br></body></html>
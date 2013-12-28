<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Ionic HTML5 Mobile Framework Alpha Preview</h3><p><a href="http://ionicframework.com/">Ionic</a> is a new user interface framework for building hybrid mobile applications with HTML5 that bills itself as the &quot;bond between native and HTML5&quot;. It provides many of the essential mobile user interface paradigms, such as simple items like <a href="http://ionicframework.com/docs/components/">lists</a>, <a href="http://ionicframework.com/docs/components/">tab bars</a> and <a href="http://ionicframework.com/docs/components/">toggle switches</a>. It also provides more complex visual layout examples such as <a href="http://ionicframework.com/docs/angularjs/controllers/side-menu/">menus that slide out to reveal content underneath</a>.</p>
<p>Ionic says that it has a heavy emphasis on performance and looks to maximize its speed through limiting DOM interaction, eliminating jQuery altogether and using specific hardware accelerated CSS transitions like `translate(z)` to trigger the GPU on mobile devices, which provides hardware accelerated interactions as opposed to those provided by the underpowered mobile browser.</p>
<p>The focus on performance means that Ionic only supports iOS6 and above and Android 4.1 and above. &quot;Devices have gotten much faster in the last year or so, but HTML5 Frameworks are still pretty conservative&quot;, said Max Lynch, CTO at Drifty, the company behind Ionic . &quot;With Ionic, we are being aggressive about only supporting newer devices, and adding lots of support for touch gestures, animations, and native-style UI elements.&quot;</p>
<h2>AngularJS Foundation</h2>
<p>Built on top of the popular <a href="http://angularjs.org/">AngularJS framework</a> from Google, Ionic utilizes AngularJS to provide the application structure, while Ionic itself focuses on the user interface. This means that all views, application routing and controllers are handled by AngularJS. Ionic does provide a set of directives for it's components so the developer can define Ionic UI components using Angular's ability to create custom HTML elements. For instance, an Ionic mobile list with inertia scrolling can be created using the `list` directive.</p>
<pre>
&lt;list&gt;
&lt;item ng-repeat=&quot;item in items&quot; item=&quot;item&quot;&gt;&lt;/item&gt;
&lt;/list&gt;</pre>
<p>Ionic also depends on Angular for touch support, animations between views, sanitizing HTML for safe input, and XHR calls.</p>
<p>Ionic does mention that in the future they plan to support other frameworks <a href="http://ionicframework.com/docs/guide/installation.html">like EmberJS and Knockout</a>.</p>
<h2>Response</h2>
<p>The <a href="https://news.ycombinator.com/item?id=6780535">response to the release</a> included the <a href="http://venturebeat.com/2013/11/20/html5-vs-native-vs-hybrid-mobile-apps-3500-developers-say-all-three-please/">usual debate</a> about trying to build native applications with HTML5, along with some concern about lack of support for versions of Android prior to 4.1. User ValentineC wrote:</p>
<blockquote> 
 <p>&quot;While I agree with the decision to support iOS 6 and up, I believe Android upgrade paths aren't as clear cut. I'm working on a project with China-designed phones and many of them are using older versions of Android as a point of product differentiation.</p> 
 <p>Hope it's something you guys will reconsider.&quot;</p> 
</blockquote>
<h2>Availability</h2>
<p>The current version of Ionic is an <a href="https://github.com/driftyco/ionic/releases">Alpha release</a>. It's installable via the command line as an NPM library, which will generate your project for you using the Ionic seed, and includes everything you need to build an application with Ionic and AngularJS:</p>
<ul> 
 <li>sudo npm install –g ionic</li> 
 <li>ionic start myproject</li> 
</ul>
<p>Ionic is open source and offered under the <a href="https://github.com/driftyco/ionic/blob/master/LICENSE">MIT license</a>.</p><br><br><br><br><br><br></body></html>
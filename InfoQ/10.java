<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Blossom Switches to Dart</h3><p>In <a href="http://www.ramen.io/post/46936028144/we-are-switching-to-dart-why">a blog post</a>, Thomas Schranz has announced that his company will be porting their <a href="http://blossom.io">Blossom</a> product, a web-based Kanban board for product teams, to <a href="http://www.dartlang.org">Dart</a>, Google's new web programming language and platform that can be used as a replacement of JavaScript.</p> 
<p>The company's move follows after a long period of frustration with the fragmentation of the JavaScript ecosystem. <a href="http://www.ramen.io/post/46936028144/we-are-switching-to-dart-why">Schranz writes</a>:</p> 
<blockquote> 
 <p>At <a href="https://www.blossom.io">Blossom</a> we are huge fans of JavaScript and in many ways it is a wonderful language if you know how to avoid its dark corners. That said, I feel the JavaScript ecosystem is severely lacking in many areas. Especially when it comes to core plumbing.</p> 
 <p>I find it pretty frustrating that you have to jump through so many hoops in order to arrive at a situation where you can start to get things done. I don’t know how this must feel for newbies to the ecosystem, but I guess the learning curve is rather steep and the question marks are plenty.</p> 
</blockquote> 
<p>As a result, the company decided to gradually migrate over the front-end of the application to Dart. Previously, the front-end was built using a combination of <a href="http://coffeescript.org">CoffeeScript</a>, <a href="http://backbonejs.org">Backbone.js</a>, <a href="http://underscorejs.org">Underscore.js</a> and <a href="http://jquery.com">jQuery</a>, assembled using <a href="http://brunch.io">Brunch</a>.</p> 
<p>InfoQ spoke to Schranz to learn more about the switch.</p> 
<p><b>Dart is still a young language, why did you make the decision to make this move now?</b></p> 
<blockquote> 
 <p>Dart is still young if you compare it to other languages, but the tooling, standard library and the package management system it provides already make it way easier to work with compared to JavaScript's ecosystem.</p> 
 <p>There is a lot of fragmentation in the JavaScript world. Especially when it comes to building blocks. We've got a ton of competing ways to manage packages, handle modularity, work with async code, dependencies or even iterate over collections. This leads to libraries that don't mix and match very well. Some force you into a specific ecosystem others try to stay agnostic and reinvent the wheel. I feel that the JavaScript community suffers from <a href="http://en.wikipedia.org/wiki/Not_invented_here">NIH syndrome</a> way more than other programming language communities like Ruby, Python or Dart.</p> 
 <p>This not only creates unnecessary complexity and confusion for beginners, but also for people who have been writing JavaScript for years. Switching to Dart might look like a risky move on the surface, but from my point of view it would be riskier for us to stick around in JavaScript land.</p> 
</blockquote> 
<p><b>What makes Dart a good fit for Blossom?</b></p> 
<blockquote>
  We were looking for a way to become more productive in working with our front-end code base. Dart provides a great foundation in that regard. Thanks to the Dart VM we get very quick save-reload development cycles and a powerful code analyzer. This makes the Dart editor a pleasure to work with. It supports auto-completion, refactoring and debugging on a level that's just not available for JavaScript. Also, the package manager, optional typing and consistency in the standard library make it way easier for us to reason about our code base. I think it is important to understand that Dart is not only a programming language, it comes with batteries included. Having a cohesive development experience feels amazing. 
</blockquote> 
<p><b>Dart is still in an alpha stage of development. As a result APIs are still changing, has this been an issue for you?</b></p> 
<blockquote>
  The language semantics and syntax feel pretty stable to me already. That said, there are a lot of improvements happening on the API level as the Dart team is working towards the 1.0 milestone. Fortunately Dart comes with great tooling support as I've already mentioned. The editor shows methods that are marked as deprecated and even comes with a 
 <a href="http://www.youtube.com/watch?v=P7htQQQmpGM">clean up tool for automatically updating your code base</a>, if possible. But even updating things by hand is not too much of a hassle if you follow the blog and the mailing list. 
</blockquote> 
<p><b>You are in the process of switching over, migrating the application piece by piece. What has your experience been with Dart code interacting with JavaScript and vice versa?</b></p> 
<blockquote>
  There is a 
 <a href="http://www.dartlang.org/articles/js-dart-interop/">js-interop package</a> that you can use to create JavaScript objects, call functions or even expose Dart functions you want to call from JavaScript. This already gets you pretty far in terms of interoperability. For Blossom itself we actually don't need the interop library much, because the components of our existing Backbone.js code base are fairly independent and are easy to migrate widget by widget. We also use 
 <a href="http://pub.dartlang.org/packages/route">Justin Fagnani's routing package</a>, which lets us take over parts of the application with Dart. So far migrating is easier than we've expected. 
</blockquote> 
<p><b>What has your experience been developing on the Dart platform thus far, compared to JavaScript?</b></p> 
<blockquote>
  It is a joy to work with. It feels incredible to have a consistent development experience where you can actually focus on improving your product instead of bike-shedding about fundamental building blocks of your ecosystem. Previously, our JavaScript code was littered with checks for 
 <tt>undefined</tt>, because JavaScript has the tendency keep on trucking when saner languages would throw an exception. The last time I felt that liberated was years ago when I was switching from PHP to Ruby and the Rails framework. Back then this was also considered risky and insane. 
</blockquote> 
<p><b>How much code have you ported to Dart until now, more or less?</b></p> 
<blockquote>
  We are at about 5% right now. We're writing new functionality in Dart and are porting existing parts every week. 
</blockquote> 
<p><b>Are you aware of any other production applications that are making the switch?</b></p> 
<blockquote>
  I am not aware of other applications in production that have switched from JavaScript to Dart, but I wouldn't be surprised to see more announcements in that direction in the future. The Dart community is growing and a lot of people can't wait for the 1.0 milestone. In addition, some service providers are starting to support Dart. For example there is 
 <a href="http://drone.io">drone.io</a>, a continuous integration service is used for testing by many Dart open source packages. 
</blockquote> 
<p><b>Do you recommend other companies to switch over to Dart today?</b></p> 
<blockquote>
  It might be a bit early to switch, but I would definitely recommend to look into Dart and to play around with the language, the tooling and especially Web UI. Just give it a try next weekend. 
</blockquote> 
<p><b>How do you see the future of Dart, will it see widespread adoption?</b></p> 
<blockquote>
 I see a bright future for Dart. It brings the joy back to web development. The people behind the platform are top notch, as are the the early community and the packages that are available. It's an exciting time to build applications for the web.
</blockquote> 
<p>When Dart was <a href="http://blog.chromium.org/2011/10/dart-language-for-structured.html">first announced</a> a year and a half ago, there was <a href="http://www.sitepoint.com/google-dart-fail/">significant</a> <a href="http://www.quirksmode.org/blog/archives/2011/10/dart_or_why_jav.html">critisism</a> of the language and approach. Since then, the Dart platform has been iterating steadily, third-party IDEs including JetBrains' WebStorm and IntelliJ <a href="http://plugins.jetbrains.com/plugin/?id=6351">added support for Dart</a>, and it is now <a href="https://github.com/igrigorik/heroku-buildpack-dart">possible to deploy</a> server-side Dart applications to <a href="http://www.heroku.com">Heroku</a>.</p> 
<p>Blossom is the first publically available production application that is making the switch. Time will tell whether this is the proverbial one sheep's leap that makes the rest follow.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
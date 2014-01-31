<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>L20n: JavaScript Localization Framework From Mozilla</h3><p><a href="http://l20n.org/">L20n</a> is an open source, JavaScript localization framework from Mozilla. It is designed to be very expressive along with several features such as adapting to Screen sizes, good separation of concerns, graceful handling of pluralization, support for default when there are multiple variants, and more.&nbsp;</p>
<p><a href="https://twitter.com/stas">Staś Małolepszy</a> <a href="http://informationisart.com/19/">explains</a> the motivation behind the project -</p>
<blockquote> 
 <p>Localizing Mozilla projects has taught us that as many as 90-95% of messages found in the UI are simple key-value pairs that won't require any advanced knowledge of L20n's features.</p> 
</blockquote>
<blockquote> 
 <p>So why develop L20n at all? Because it's the remaining 5% that make or break the UI of your app. They're too important to ignore and they are responsible for the experience of your user.</p> 
</blockquote>
<p>As such, the project tries to keep simple scenarios simple, but also supports complex localizations when needed.</p>
<p>Below are some interesting features of L20n -</p>
<ul> 
 <li>Expressiveness - L20n has support for <a href="http://l20n.org/learn/working-with-text-multiline-interpolation/">interpolations</a> (to build more complex entities), <a href="http://l20n.org/learn/plural-forms-introduction-to-macros/">pluralizations</a>, <a href="http://l20n.org/learn/using-variants-to-define-grammatical-cases/">handling of grammatical cases</a>, having <a href="http://l20n.org/learn/translations-with-multiple-variants/">multiple variants</a> of the same entity, and so on, which combine to create a very expressive format.</li> 
 <li><a href="http://l20n.github.io/tinker/">Responsiveness to screen sizes</a> - you can name various screen sizes and then have different variants of the entities targeted for these specific screen sizes</li> 
 <li>Good separation of concerns - localization related <a href="http://informationisart.com/21/">complexities can be isolated</a> in the language under consideration without affecting other languages used in the app or even the app source code.</li> 
 <li><a href="https://github.com/l20n/l20n.js/blob/master/docs/api.md">Non-blocking, secure API</a> in addition to the ability to <a href="https://github.com/l20n/l20n.js/blob/master/docs/html.md">bind HTML elements</a> to make them localizable</li> 
</ul>
<p>A simple but powerful concept that L20n introduces is the concept of <a href="http://l20n.org/learn/defining-the-default-variant/">Defaults</a> - this allows you to define multiple variants for an entity but also define a default value in case any specific variant is not asked for. This enables translators to progressively tweak their content and even add more variants, while ensuring that existing code using these entities are not affected (by just choosing a default). This is what also allows different localizations to have different degrees of complexity without having to complicate all other localizations.</p>
<p>Here are a few resources to learn more about the project -</p>
<ul> 
 <li>The project <a href="https://github.com/l20n/l20n.js/blob/master/README.md">ReadMe</a></li> 
 <li><a href="https://github.com/l20n/demo">A demo project</a> that shows how an HTML file can be localized using L20n</li> 
 <li><a href="http://l20n.org/learn/">Step-by-step tutorial</a> introducing various concepts</li> 
 <li><a href="https://github.com/l20n/l20n.js/tree/master/docs">Documentation</a></li> 
 <li>A Set of <a href="http://informationisart.com/19/">FAQs and Answers</a></li> 
</ul>
<p align="left">L20n has been in development since 2012 and the release candidate for 1.0 has been out since November 2013.</p><br><br><br><br><br><br></body></html>
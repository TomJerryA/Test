<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PayPal Switches from Java to JavaScript</h3><p>PayPal has decided to use JavaScript from browser all the way to the back-end server for web applications, giving up&nbsp;legacy code written in JSP/Java.</p>
<p>Jeff Harrell, Director of Engineering at PayPal, has explained in a couple of blog posts (<a href="https://www.paypal-engineering.com/2013/06/17/set-my-ui-free-part-1-dust-javascript-templating-open-source-and-more/">Set My UI Free Part 1: Dust JavaScript Templating, Open Source and More</a>, <a href="https://www.paypal-engineering.com/2013/11/22/node-js-at-paypal/">Node.js at PayPal</a>) why they decided&nbsp;and some conclusions&nbsp;resulting from switching their web application development&nbsp;from Java/JSP to a complete JavaScript/Node.js stack.</p>
<p>According to Harrell, PayPal’s websites had accumulated a good deal of technical debt, and they wanted a “technology stack free of this which would enable greater product agility and innovation.” Initially, there was a significant divide between front-end engineers working in web technologies and back-end ones coding in Java. When a UX person wanted to sketch up some pages, they had to ask Java programmers to do some back-end wiring to make it work. This did not fit with their Lean UX development model:</p>
<blockquote> 
 <p>At the time, our UI applications were based on Java and JSP using a proprietary solution that was rigid, tightly coupled and hard to move fast in. Our teams didn’t find it complimentary to our Lean UX development model and couldn’t move fast in it so they would build their prototypes in a scripting language, test them with users, and then later port the code over to our production stack.</p> 
</blockquote>
<p>They&nbsp;wanted a “templating [solution that] must be decoupled from the underlying server technology and allow us to evolve our UIs independent of the application language” and that would work with multiple environments. They&nbsp;decided to&nbsp;go with&nbsp;<a href="https://github.com/linkedin/dustjs">Dust.js</a>&nbsp;– a templating framework backed up by LinkedIn&nbsp;– , plus Twitter’s <a href="https://github.com/twitter/bootstrap">Bootstrap</a>&nbsp;and <a href="https://github.com/bower/bower">Bower</a>, a package manager for the web. Additional pieces added later were <a href="http://lesscss.org/">LESS</a>, <a href="http://requirejs.org/">RequireJS</a>, <a href="http://backbonejs.org/">Backbone.js</a>, <a href="http://gruntjs.com/">Grunt</a>, and <a href="http://visionmedia.github.io/mocha/">Mocha</a>.</p>
<p>Some of PayPal’s pages have been redesigned but they still had some of the legacy stack:</p>
<blockquote> 
 <p>… we have legacy C++/XSL and Java/JSP stacks, and we didn’t want to leave these UIs behind as we continued to move forward. JavaScript templates are ideal for this. On the C++ stack, we built a library that used V8 to perform Dust renders natively – this was amazingly fast! On the Java side, we integrated Dust using a Spring ViewResolver coupled with Rhino to render the views.</p> 
</blockquote>
<p>At that time, they also started using Node.js for prototyping new pages, concluding that it was “extremely proficient” and decided to try it in production. For that they also built <a href="https://github.com/paypal/kraken-js">Kraken.js</a>, a “convention layer” placed on top of <a href="http://expressjs.com/">Express</a>&nbsp;which is a&nbsp;Node.js-based web framework. (PayPal has recently open sourced Kraken.js.) The first application to be done in Node.js was the account overview page, which is one of the most accessed PayPal pages, according to Harrell. But because they were afraid the app might not scale well, they decided to create an equivalent Java application to fall back to in case the Node.js one won’t work. Following are some conclusions regarding the development effort required for both apps:</p>
<table cellspacing="0" cellpadding="2" width="500" border="1" unselectable="on"> 
 <tbody> 
  <tr> 
   <td valign="top" width="166">&nbsp;</td> 
   <td valign="top" width="166"><strong>Java/Spring</strong></td> 
   <td valign="top" width="166"><strong>JavaScript/Node.js</strong></td> 
  </tr> 
  <tr> 
   <td valign="top" width="166">Set-up time</td> 
   <td valign="top" width="166">0</td> 
   <td valign="top" width="166">2 months</td> 
  </tr> 
  <tr> 
   <td valign="top" width="166">Development</td> 
   <td valign="top" width="166">~5 months</td> 
   <td valign="top" width="166">~3 months</td> 
  </tr> 
  <tr> 
   <td valign="top" width="166">Engineers</td> 
   <td valign="top" width="166">5</td> 
   <td valign="top" width="166">2</td> 
  </tr> 
  <tr> 
   <td valign="top" width="166">Lines of code</td> 
   <td valign="top" width="166">unspecified</td> 
   <td valign="top" width="166">66% of unspecified</td> 
  </tr> 
 </tbody> 
</table>
<p>The JavaScript team needed 2 months for the initial setup of the infrastructure, but they created with fewer people an application with the same functionality in less time. Running the test suite on production hardware, they concluded that the Node.js app was performing better than the Java one, serving:</p>
<blockquote> 
 <p>Double the requests per second vs. the Java application. This is even more interesting because our initial performance results were using a single core for the node.js application compared to five cores in Java. We expect to increase this divide further.</p> 
</blockquote>
<p>and having</p>
<blockquote> 
 <p>35% decrease in the average response time for the same page. This resulted in the pages being served&nbsp;200ms faster— something users will definitely notice.</p> 
</blockquote>
<p>As a result, PayPal began using the Node.js application&nbsp;in beta in production, and have decided that “all of our consumer facing web applications going forward will be built on Node.js,” while some of the existing ones are being ported to Node.js.</p>
<p>One of the benefits of using JavaScript from browser to server&nbsp;is, according to Harrell, the elimination of a divide between front and back-end development by having one team “which allows us to understand and react to our users’ needs at any level in the technology stack.”</p><br><br><br><br><br><br></body></html>
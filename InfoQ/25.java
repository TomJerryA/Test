<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Koa Web Framework 0.2.0 Release</h3><p>The NodeJS based <a href="http://koajs.com/">Koa</a> web application framework has <a href="https://medium.com/code-adventures/a3a046a04836">released version 0.2.0</a>. Koa is the successor of the popular <a href="http://expressjs.com/">Express</a> MVC platform, but relies heavily on newer ES6 constructs. Project lead <a href="https://twitter.com/tjholowaychuk">TJ Holowaychuck</a> describes Koa as “a chance to take what I learned from Connect/Express and do things ‘right’ this time.”</p>
<p>This release is dubbed &quot;short but sweet&quot;, and is marked as an important one in that that it reaffirms the team’s design choices from the initial 0.1.0 release, solidifying Koa's API for future releases and production use.</p>
<h2>0.2.0 Changes</h2>
<p>The biggest update in this release is actually to the <a href="https://github.com/koajs/compose">koa-compose</a> module, which allows developers to debug requests that are being passed to middleware by logging the content of the request to standard out (stdout) both before and after the middleware has manipulated it.</p>
<p>Some additional smaller changes include routing of socket errors to prevent crashing the node server since sockets are handled at the Node level, and a refactoring of the functionality that is currently shared between <a href="http://expressjs.com/">Express</a> and Koa into modules that both frameworks can use. An example of this is the “accepts” module, which does <a href="https://developer.mozilla.org/en-US/docs/HTTP/Content_negotiation">content negotiation</a>, allowing the server to respond to requests with different types of content based on the value of the Accepts HTTP Headers.</p>
<h2>Built on Generators</h2>
<p>Koa calls itself a &quot;next generation web framework&quot; and leverages the <a href="https://github.com/visionmedia/co">co</a> library, which uses generators from the <a href="http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts">ECMAScript 6</a> language specification (also known as &quot;Harmony&quot;) to create non-blocking synchronous processing for Node. Prior Node frameworks have relied on callbacks and promises to achieve the same sort of &quot;stack processing&quot; that is required for HTTP Requests.</p>
<p>While generators are really a “factory” for creating Harmony iterators, Koa uses them to turn functions into synchronous operations. A Koa app can pass requests through several layers of middleware. Each invoked middleware function must yield its result before the caller will continue.</p>
<pre>
var koa = require('koa');
var app = koa();

app.use(route.get('/', google));

function *people() {
 &nbsp;&nbsp;// “get” is an asynchronous HTTP call
 &nbsp;&nbsp;var result = yield get('http://www.google.com');
 &nbsp;&nbsp;// this line will not execute until the above yield returns
 &nbsp;&nbsp;this.body = result;

}</pre>
<h2>No Middleware</h2>
<p>Koa includes no middleware itself, allowing its footprint to stay light. &quot;We had originally bundled a lot of middleware into <a href="https://github.com/senchalabs/Connect">Connect</a> for convenience, not only for the end-user, but for ourselves since Node and the entire eco-system was changing so rapidly, it made maintenance easier. Fast forward a few years and most people agree that bundling them was a mistake&quot;, explained Holowaychuk. Holowaychuk went on to say that this realization led to the decision not to bundle any middleware with Koa, but to provide it via separate modules that can be bundled for convenience.</p>
<p>The <a href="https://github.com/koajs/common">koa-common</a> module bundles most of the commonly required middleware for a web application. A developer can add all of this middleware to their Koa application via <a href="https://npmjs.org/">NPM</a>.</p>
<pre>
$ npm install koa-common</pre>
<h2>The Future of Koa And Express</h2>
<p>Holowaychuk mentioned that Koa is considered to be in a finished state barring the odd feature request now and again.</p>
<p>User “deif” <a href="https://news.ycombinator.com/item?id=6933833">had concerns</a> about the future of Express given the release of Koa.</p>
<blockquote> 
 <p>I have some questions about this:</p> 
 <ol> 
  <li>The FAQ gives a political answer about the status of Express but I imagine that Express will not be actively maintained any more. Correct?</li> 
  <li>If focus is now on Koa, why the name change from Express when it is already a huge name for node frameworks?</li> 
  <li>If a new developer sees Express and Koa, would they immediately know which one is being focused on?</li> 
 </ol> 
 <p>Basically I'm wondering why it couldn't be called Express 3.0 (or 4.0).</p> 
</blockquote>
<p>Holowaychuk explained the name change saying</p>
<blockquote> 
 <p>The migration path from Express to Koa is non-trivial, even though they look similar they're fundamentally quite different so I figured instead of calling it Express 4.0 we would be best to give it a new name…there are still several people maintaining Express, and we're open to adding more people to the team if they're interested!</p> 
</blockquote><br><br><br><br><br><br></body></html>
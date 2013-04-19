<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Meteor Introduces Tighter NPM Integration, Overhauled Package Management</h3><p>The <a href="http://meteor.com/about/people">Meteor Development Group</a> released <a href="http://meteor.com/blog/2013/04/04/meteor-060-brand-new-distribution-system-app-packages-npm-integration">Meteor 0.6.0</a> on April 4th as a major overhaul to its package management system as well as growing <a href="https://npmjs.org/">NPM</a> package support. Since then, <a href="http://meteor.com/blog/2013/04/16/meteor-062-d3js-v3-debugging-improvements-experimental-server-to-server-ddp">version 0.6.2</a> dropped on April 16th with <a href="https://github.com/meteor/meteor/blob/devel/History.md">continued enhancements and bug fixes</a>.</p> 
<p>Because it enforces synchronicity in <a href="http://nodejs.org/">Node.js</a> with the use of <a href="https://npmjs.org/package/fibers">Fibers</a> and leverages its own package management system, Meteor has bucked conventional asychronous node development and vanilla NPM package management in favor of its own opinionated approaches, garnering both <a href="https://news.ycombinator.com/item?id=3824908">praise and skepticism</a> along the way. Version 0.6.0 puts both of these issues at the fore, refining its relationship with the node.js ecosystem. <a href="https://github.com/avital">Avital Oliver</a> serves as the main impetus behind 0.6.0, with significant contributions from <a href="https://twitter.com/glasser">David Glasser</a> and the rest of the Meteor team. InfoQ caught up with Avital to discuss the impact of 0.6.0 on the Meteor and Node.js communities.</p> 
<p><strong>INFOQ: One of the criticisms leveled against Meteor has been its 'proprietary packaging system' -- with Meteor 0.6.0, how does that story change?</strong></p> 
<blockquote> 
 <p><strong>Avital:</strong> Well, I'm not quite sure what makes smart packages more 'proprietary' than NPM, <a href="https://github.com/twitter/bower">Bower</a>, <a href="https://github.com/component/component">Component</a>, and the other lesser-known package managers. Smart packages *are* different than NPM modules, for example. One of the unique properties of smart packages are that run on client, server, during build time and even hook into our production environment. This is what makes <code>meteor add coffeescript</code>, <code>meteor add appcache</code> and <code>meteor add email</code> just work. <a href="https://twitter.com/immir">Geoff Schmidt</a> [one of the Meteor core developers] wrote a <a href="https://github.com/meteor/meteor/pull/516#issuecomment-12919473">short essay on these differences</a>.</p> 
</blockquote> 
<p><strong>INFOQ: Given the disparate kinds of NPM packages, which ones are the 'lowest hanging fruit' for Meteor wrapping via <code>NPM.depend</code>s? Does the NPM namespace inside Meteor do any additional wrapping of the NPM functionality (ensuring that async processes are rolled up into Futures, etc), or is that the job of the NPM-Meteor wrapper?</strong></p> 
<blockquote> 
 <p><strong>Avital:&nbsp;</strong>We will definitely build some sort of generic wrapper, like <code>Future.wrap</code> but better. It'll work around some edge cases with Future.wrap, and supply a callback-optional interface, like the ones we have for server-side <code><a href="http://docs.meteor.com/#meteor_call">Meteor.call</a></code> and <code><a href="http://docs.meteor.com/#meteor_http_call">Meteor.http.call</a></code>. In the meanwhile, using <code>future.resolver()</code> seems to be the easiest way to go (as is done in the <a href="https://github.com/avital/meteor-xml2js-npm-demo/blob/master/packages/xml2js/xml2js.js">XML2JS example</a>).</p> 
 <p>As for which NPM modules to wrap -- I'd just say wrap whichever ones you want to use! That will help the community use the tools they need within Meteor, and it will help us learn which functionality we should focus our efforts on.</p> 
</blockquote> 
<p><strong>INFOQ: When is documentation coming for the NPM stuff?</strong></p> 
<blockquote> 
 <p><strong>Avital:</strong> It'll be documented as part of documenting the more final Package API, which is an active work-in-progress (which can be seen on the <a href="https://github.com/meteor/meteor/tree/linker">linker branch on our Github repo</a>.)</p> 
</blockquote> 
<p><strong>INFOQ: What is the Engine package management system that ships with 0.6.0? Why is this different from previous iterations?</strong></p> 
<blockquote> 
 <p><strong>Avital:</strong> We were tackling two main problems -- (1) apps should be pinned to releases, and ideally you wouldn't have to download every package when switching releases, and (2) Meteor should have native support for third party packages. In order to achieve these goals, we release the Meteor command line tools and packages separately. A release just points to revisions of tools and each package. When you run a new Meteor release, we only fetch the artifacts that have changed, and cache then in a warehouse, which can be found in ~/.meteor.</p> 
</blockquote>
<blockquote> 
</blockquote> 
<p><strong>INFOQ: David Glasser <a href="http://www.youtube.com/watch?feature=player_detailpage&amp;v=mXJgOwn5FbY#t=121s">said recently</a> that you guys always wanted to support NPM, but you wanted to do it 'right' -- can you explain what this means?</strong></p> 
<blockquote> 
 <p><strong>Avital:</strong> We definitely didn't want to ask people to run npm commands directly, just like we don't ask people to run their own instance of MongoDB. So we run <code>npm install</code> and such behind the scenes for you. We also want to make use of <code>npm shrinkwrap</code> to ensure that every time you use a smart package you are running the exact same code. In order to achieve all of these in a seamless way, we had to do a certain dance around running NPM. There are a bunch of additional small details, such as the fact that <code>npm shrinkwrap</code> doesn't allow you to upgrade the version of only one dependency. Anyway, for those who are curious, the code to implement all of this can be found at <a href="https://github.com/meteor/meteor/blob/master/tools/meteor_npm.js">here</a>.</p> 
</blockquote> 
<p><strong>INFOQ: How do you justify making tough decisions in the face of convention? (Going with your own package management system versus the status quo [vanilla NPM]).</strong></p> 
<blockquote> 
 <p><strong>Avital:</strong> There is always one motivating factor: the best experience for our users.</p> 
</blockquote> 
<p><strong>INFOQ: What's next for NPM support?</strong></p> 
<blockquote> 
 <p><strong>Avital:</strong> We have to do more work to support packages with binary dependencies. We'll build them on all platforms on our servers so that when you use 'meteor deploy' it will work even if your machine runs a different architecture (such as Mac). As described above, we'll also build a general wrapper to make it easier to convert node-style async APIs to ones with optional callbacks.</p> 
</blockquote> 
<p><strong>INFOQ: How close is Meteor 1.0 now?</strong></p> 
<blockquote> 
 <p><strong>Avital:</strong> It's neither too close nor too far :)</p> 
</blockquote> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
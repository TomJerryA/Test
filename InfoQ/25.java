<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Socket.IO 1.0 Release Brings Binary Support, new Engine.IO module</h3><p>Guillermo Rauch has released version 1.0 of <a href="http://socket.io/">Socket.IO</a>, a JavaScript library for realtime web applications.</p>
<p>The new release brings the new Engine.IO module, support for sending binary data, and a simplified approach towards multi-node scalability.</p>
<p>The start of Socket.IO coincided with the beginnings of the specification of the WebSocket protocol. Rauch says that, at the time, having a bi-directional socket in the browser was &quot;impossible&quot;. Because of this, building realtime applications involved cumbersome and slow alternatives, with developers used to Socket APIs from other languages and programming environments.&nbsp;</p>
<p>Socket.IO lets clients and servers exchange events with any type of data structure. This helps enable chat rooms, realtime analytics platforms, and multi-user document collaboration apps.</p>
<p>The Engine.IO module in Socket's latest release implements a WebSocket-like API. This means that the codebase no longer deals with transports and browser incompatibilities. Rauch says this separation has led to innovation of the transport layer.</p>
<p>In his article &quot;<a href="http://socket.io/blog/introducing-socket-io-1-0">Introducing Socket.IO 1.0</a>&quot;, Rauch says that the benefits of this particular modularisation includes a &quot;simplification for codebase size and testing surface.&quot; The server is now 1,234 lines of code, the client 976 lines.</p>
<p>Addressing the updates to the transport layer, Rauch said the release has introduced &quot;transport feature detection&quot;, directly testing APIs to ensure that they behave as expected.</p>
<blockquote>
 Checking that the JSON global is present does not mean that JSON.stringify works, or even exists. It could mean that the user defined a JSON global of their own, or the environment could have a broken JSON implementation. 
 <p>Socket.IO never assumes that WebSocket will just work, because in practice there's a good chance that it won't. Instead, it establishes a connection with XHR or JSONP right away, and then attempts to upgrade the connection to WebSocket.</p> 
</blockquote>
<p>Binary support for Socket.IO has been a requested feature among users, but although Rauch considers the support to be &quot;genuinely useful&quot; he says that if it had been modelled after the WebSocket API, support would be limited. This is because of how the Websocket API requires Socket is put into either “string mode” or “binary mode.” Rather than compromise, Socket.IO now supports emitting Buffer (from Node.JS), Blob, ArrayBuffer, and File, as part of any datastructure.</p>
<p>Socket.IO's approach to multi-node scalability is simpler in 1.0. With the new release, Socket.IO is concerned only with passing events around, rather than with the storing and/or replicating data across nodes. This means scaling Socket.IO to multiple nodes can be done in only <a href="http://socket.io/blog/introducing-socket-io-1-0/">two steps</a>:</p>
<blockquote> 
 <ol> 
  <li>Turn on sticky load balancing (for example by origin IP address). This ensures that long-polling connections, for example, always route requests to the same node where buffers of messages could be stored.</li> 
  <li>Implement the socket.io-redis adapter.</li> 
 </ol> 
</blockquote>
<p>Socket.IO 1.0 deprecates the Socket#set and Socket#get APIs, with packets now getting encoded and distributed to other nodes whenever broadcast.</p>
<p>Rauch says the reaction to the release has been &quot;amazing&quot;, but coming more than two years since the last major release, for some it has been a long wait. Liam Kaufman, founder of Understoodit.com, <a href="https://news.ycombinator.com/item?id=7811729">commented</a> on the announcement on Hacker News. He said:</p>
<blockquote>
 This was a long time coming! I'm very happy to see Socket.IO 1.0 finally released. Pre-1.0 had some deal-breaking technical issues.
</blockquote>
<p>Not everyone in the community was sure it would be worth the wait. User Philip Wang <a href="https://news.ycombinator.com/item?id=7811814">said</a>:</p>
<blockquote>
 I've since switched to SockJS for all my projects (after struggling with memory issues in Socket.IO 0.9.*). Any compelling reasons to give Socket.IO another try?
</blockquote>
<p>Marco Aur&eacute;lio, software engineer at Automattic, <a href="https://news.ycombinator.com/item?id=7811880">replied</a>:</p>
<blockquote>
 The new Engine.IO module used behind the scenes is amazing. It will start with long polling, and upgrade to WebSockets seamlessly (so you get a very fast start every time, even in old browsers or proxied envs). As far as I know, this is the opposite of what was happening previously (trying WebSockets, then falling back to long polling). Engine.IO is also much more scalable and robust.
</blockquote>
<p>Other features announced in Socket.IO 1.0 include Automated Testing, better integration, improved debugging and streamlined APIs.</p>
<p>Socket.IO is open source and released under the MIT license. InfoQ readers interested to contribute to the project can find all the repositories on Github <a href="https://github.com/automattic">here</a>, and should follow <a href="http://twitter.com/socketio">@SocketIO</a> on Twitter.</p><br><br><br><br><br><br></body></html>
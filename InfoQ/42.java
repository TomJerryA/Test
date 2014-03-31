<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>RESTistential Crisis over Hypermedia APIs</h3><p>Software developer <a href="http://stackoverflow.com/users/374460/evan-cordell">Evan Cordell</a> initiated a debate about how the hypermedia constraint of REST is at odds with common web APIs requirements in the <a href="https://groups.google.com/forum/#!topic/api-craft/7c1tyHv2VQ4">API-Craft</a> mailing list a few weeks ago.</p>
<p>In discussing his &quot;RESTistential crisis&quot;, Cordell noted that the REST style has finally started to reveal its best hidden secret, the hypermedia constraint, after years of debates and practice. While perfectly adapted to human-driven interaction as demonstrated by the Web, there appears to be growing concerns within the web API community about its usefulness for programmable web APIs in general.</p>
<p>He started the conversation with a description of REST and hypermedia limitations when applied to domain-specific web APIs, then considers the need for alternate architecture styles, taking the best of REST but replacing some constraints to obtain different benefits, such as efficient and reliable machine-to-machine communication.</p>
<p>The main concerns cited mention the various ways to deal with changes of an interface over a long period of time. The first solution requires running several API versions in parallel and even several orchestration APIs dedicated to specific client experiences <a href="http://www.infoq.com/news/2013/12/api-orchestration-layer">as illustrated by Netflix</a>. Its flexibility comes with significant design and operation challenges.</p>
<p>The second solution requires putting much more effort upfront by designing a RESTful hypermedia API that would more easily cope with changes, limiting the impact on the clients, in a way similar to how HTML browsers and servers work and evolve. But some participants, especially web engineer <a href="https://twitter.com/mikekelly85">Mike Kelly</a>, voice concerns about the complexity involved and additional burden on API consumers.</p>
<p>Here is a summary of the conversation including large excerpts of Evan's initial message including section titles:</p>
<h2>1) A good API doesn't change</h2>
<ul> 
 <li>Thinking about Joshua Bloch's experience regarding the design of public Java API, it seems valid to say that the same rules apply for programmable web APIs.</li> 
 <li>APIs are interfaces, following the facade pattern, that shouldn't change on the surface for clients. However, multiple or evolving implementations including the runtime data can be exposed, without requiring the API contract itself to change.</li> 
</ul>
<h2>2) Versioning doesn't work</h2>
<blockquote>
 A &quot;Web API&quot; exposes far more than a &quot;traditional&quot; API. It exposes data, and more often than not it exposes the current state of a large set of constantly-changing data. How can you effectively version when your domain model has two versions, which share some subset of data, but are accessed in different ways? You force the clients to break.
</blockquote>
<ul> 
 <li>Hypermedia can help an API being less fragile and evolve, but if the data and domain model fundamentally changes. Clients won't be able to automatically adapt to all those change without human intervention from a developer.</li> 
</ul>
<h2>3) Hypermedia destroys resource location</h2>
<ul> 
 <li>REST prevents fixed URIs and any prior knowledge from clients about the server resources. In practice clients remember URIs (e.g. bookmarks) and servers need to deal with evolution of their URI space (redirections).</li> 
 <li>Hypermedia can't isolate the API providers from the laziness of API users who will not follow the proper hypermedia flow but instead will directly target specific resources and URIs.</li> 
 <li>As hypermedia APIs tend to be very complex to understand and consume, developers will inevitably optimize their clients and take short-cuts, defeating the whole point of isolating clients from API changes.</li> 
</ul>
<h2>4) Hypermedia make sense for human users, not machines</h2>
<ul> 
 <li>Machines don't deal well with change over time but humans are very good at interpreting changes and deciding what they want to do next. Hypermedia is very natural to humans, much less so to machine.</li> 
 <li>Changes in the domain model require changes in the way it is consumed by clients, hypermedia doesn't buy you anything special here.</li> 
</ul>
<blockquote>
 A true REST/hypermedia client is really a form of HCI, rather than an API (an AHI - Application Human Interface, if you will)
</blockquote>
<h2>5) What's so bad about out-of-band?</h2>
<ul> 
 <li>Does an API really need to be inherently discoverable?</li> 
 <li>Why should the API be self documenting, when the format of the API responses are difficult to read at high levels of complexity?</li> 
 <li>Nicely structured HTML, rendered by a browser, with interactive examples and articulate descriptions is easier to read.</li> 
</ul>
<h2>6) Are hypermedia APIs really that different from a WADL?</h2>
<blockquote>
 What's so different about a discoverable, hypermedia API? A &quot;HAPI&quot; just seems like an API with the WADL distributed throughout. You still have to start with a single endpoint, and you still have to figure out what you can with the API based on that response.
</blockquote>
<ul> 
 <li>Something has to have a description of the domain models, and that's something that will change over time.</li> 
</ul>
<h2>7) A Web analogue</h2>
<ul> 
 <li>REST in native mobile apps would require Android ML and iOSML languages with code on demand.</li> 
 <li>Use of domain specific hypermedia media types still requires you to write custom client code that understands this domain.</li> 
</ul>
<h2>8) What seems to really be good about REST</h2>
<ul> 
 <li>Beside hypermedia and the Web of documents, REST: 
  <ul> 
   <li>enforces a stateless server, making it very easy to scale</li> 
   <li>encourages decoupling of information via resources</li> 
  </ul> </li> 
</ul>
<blockquote>
 The basics are so simple that you can talk to servers in a semantically meaningful way with nothing but the http library included on every platform and language.
</blockquote>
<p>The above summary contains several excerpts from the participants, especially Evan Cordell, and also Mike Amundsen, Jorn Wildt and Mike Kelly among others. As a disclaimer, note that I also participated in the beginning of the conversation.</p>
<p>Based on your own experience do you think we need to better differentiate the REST and the web API architecture styles, as well as between human-driven hypermedia and machine-to-machine communication use cases?</p><br><br><br><br><br><br></body></html>
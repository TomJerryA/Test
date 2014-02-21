<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Prismatic Adds Data Type Coercion to Schema 0.2</h3><p><a href="http://getprismatic.com/">Prismatic</a> have added <a href="http://en.wikipedia.org/wiki/Type_conversion">data coercion</a> in the <a href="http://blog.getprismatic.com/blog/2014/1/4/schema-020-back-with-clojurescript-data-coercion">0.2 release</a> of their <a href="http://clojure.org/">Clojure</a> data description library, <a href="https://github.com/prismatic/schema">Schema</a>. The addition of coercion means that the library doesn’t just reject data that has the wrong types, but it can be configured to modify instances to fit the schema.</p>
<p>In Clojure it is idiomatic to use <a href="http://clojure.org/data_structures#Data%20Structures-Keywords">keywords</a> for Map keys, meaning there is often some boilerplate code to perform the conversion when receiving <a href="http://www.json.org/ ">JSON</a> objects. Previously this conversion would have needed to be performed before attempting to validate the request. Now, if your schema defines the keys as keywords, <a href="https://github.com/prismatic/schema">Schema</a> will handle that for you. Of course, you can write your own coercers for your own specific needs. Along with this added capability, Prismatic claims the changes have reduced the time required to validate data by five times.</p>
<p>Schema’s goal, when first <a href="http://blog.getprismatic.com/blog/2013/9/4/schema-for-clojurescript-data-shape-declaration-and-validation ">released in September,</a> was to “get many of the benefits of type systems in Clojure with less hassle”. When released it seemed it could compete with <a href="https://github.com/clojure/core.typed ">core.typed</a>, a Clojure library also bringing types to the language. This view <a href="https://news.ycombinator.com/item?id=6339607">was refuted</a> by core.typed’s author <a href="https://twitter.com/ambrosebs">Ambrose Bonnaire-Sergeant</a> at the time, arguing that they will in fact complement one another, a view he repeated during a later <a href="http://www.infoq.com/news/2013/10/core-typed">InfoQ interview on core.typed</a>.&nbsp;</p>
<div>
 InfoQ had the chance to talk with 
 <a href="http://getprismatic.com/profile/w01fe">Jason Wolfe</a>, the library's lead author, about the future of Schema.
</div>
<div>
 &nbsp;
</div>
<p><b>InfoQ:</b> When Schema was originally released, it was suggested a combination of core.typed and Schema could be very powerful. Has your thinking progressed on this idea since then?</p>
<blockquote>
 I've been excited about gradual types in Clojure since I saw my first Qi program a few years ago, and I think Ambrose is doing a great job of making that a reality. There are a few ways we've talked about that Schema could play well with core.typed, the most interesting of which is probably using Schema as a bridge between core.type-checked code and unchecked code. &nbsp; 
 <div>
  &nbsp;
 </div> 
 <div>
  That said, I'm sad to say that we haven't had the time to explore core.typed in depth yet, so I don't have much more to say on this just yet.&nbsp;
 </div> 
</blockquote>
<p><strong>InfoQ:</strong> Expanding to test data generation sounds challenging, are you integrating with <a href="https://github.com/reiddraper/simple-check ">simple-check</a>, making use of <a href="https://github.com/clojure/test.generative ">test.generative</a> or does Schema require a different approach?</p>
<blockquote>
 We're still exploring the options. I've read a lot of really great things about simple-check, and I think this should be doable, but we're still trying to understand its implementation and figure out how to incorporate additional constraints into the generation process. There will also probably be a simple generator for pseudo-randomly fleshing out a partial datum, which is something we end up using often in tests.
</blockquote>
<p><strong>InfoQ:</strong> What further ideas do you have on extracting value from Schema definitions?</p>
<blockquote> 
 <p>Coercions and transformation are extremely powerful and I think we're still figuring out all the applications they will enable. &nbsp;My colleague Dave Golland will be speaking at Clojure West on a new library “fnhouse” that ties together graph and schema to make building web APIs easy. Following this release will be “coax”, which automatically generates Objective C and ClojureScript model classes and client API libraries from fnhouse APIs. &nbsp;</p> 
 <p>After that, we have lots of crazy ideas, but nothing we're ready to talk about yet.</p> 
</blockquote>
<p><a href="https://github.com/prismatic/plumbing ">Graph</a> is Prismatics Clojure library, <a href="http://blog.getprismatic.com/blog/2013/2/1/graph-abstractions-for-structured-computation">released in 2013,</a> for expressing structured computation in a declarative style.</p><br><br><br><br><br><br></body></html>
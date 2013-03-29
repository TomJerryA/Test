<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>MongoDB Gets Better Security, Text Search, Performance Improvements – What’s Next?</h3><p><a href="http://www.mongodb.org/">MongoDB</a> 2.4 was recently released with new features such as Text Search, hash-based sharding, better geo-spatial capabilities with GeoJSON support and several performance and tooling improvements. We also discussed with 10gen about what’s next on the roadmap.</p> 
<p>Some of the key improvements are as follows –</p> 
<ul> 
 <li><a href="http://docs.mongodb.org/manual/release-notes/2.4/#text-search">Text Search</a> is introduced as a beta-feature, supporting stemming and tokenization in 15 languages</li> 
 <li><a href="http://docs.mongodb.org/manual/release-notes/2.4/#new-hashed-index-and-sharding-with-a-hashed-shard-key">Hash-based sharding</a>, for cases where data spread across any natural sharding key cannot be easily predicted</li> 
 <li><a href="http://docs.mongodb.org/manual/release-notes/2.4/#new-geospatial-indexes-with-geojson-and-improved-spherical-geometry">Geo-spatial indexes</a> with GeoJSON support</li> 
 <li>Security Improvements – new <a href="http://docs.mongodb.org/manual/release-notes/2.4/#new-modular-authentication-system-with-support-for-kerberos">modular authentication system</a>, integration with Kerberos, <a href="http://docs.mongodb.org/manual/release-notes/2.4/#role-based-access-control-and-new-privilege-documents">Role-based Access control</a></li> 
 <li>Several Performance improvements, significant ones for some specific scenarios such as Count or Aggregation</li> 
 <li>V8 as the default JavaScript engine in the mongo shell (replaces SpiderMonkey); leads to performance and concurrency improvements for JavaScript based actions</li> 
 <li>Additional metrics for monitoring cluster status</li> 
</ul> 
<p>10gen also introduced an <a href="http://www.10gen.com/products/mongodb-enterprise">enterprise version of MongoDB</a> along with the 2.4 release.&nbsp;</p> 
<p>We got in touch with <a href="http://www.linkedin.com/in/kellystirman">Kelly Stirman</a>, director of product marketing at 10gen, to know more about the new features and what to expect next.</p> 
<p>Kelly explains why collection-level locks may not make sense for MongoDB –</p> 
<blockquote> 
 <p>The improvements to lock yielding in 2.2 provide substantial benefits to write throughput by reducing lock contention. There was a <a href="http://blog.serverdensity.com/goodbye-global-lock-mongodb-2-0-vs-2-2/">good write up on this subject</a> by David Mytton.</p> 
 <p>MongoDB 2.4 does not include any additional granularity of locks beyond the improvements provided in 2.0 and 2.2. We are considering document-level locks for 2.6. The lock yielding improvements were substantial enough that collection-level locks might not provide a major additional improvement, and so document-level locks may be the next step.</p> 
</blockquote> 
<p>About when to use range-based sharding instead of the the new hash-based sharding -</p> 
<blockquote> 
 <p>When using range-based sharding, if your application requests data based on a shard key range, then those queries will be routed to the appropriate shards, which is typically just one shard, or perhaps a few shards. The same query in a system that has used hash-based sharding will route the request to a greater number of shards, perhaps all the shards. Ideally, queries are routed to a single shard or as few shards as possible as this scales better than routing all queries to all shards. So, if you understand your data and queries well, it is possible range-based sharding is the best option.</p> 
</blockquote> 
<p>With MongoDB 2.4, Counts can be up to 20x faster, and the Aggregation Framework is 3 - 5 times faster on average. Kelly explains that the improved count performance relies on some improvements to traversing the B-trees in MongoDB – low cardinality index-based counts are where you see the biggest improvements. The improvements to the Aggregation Framework are a reflection of many smaller changes in MongoDB internal implementation that add up to big benefits.</p> 
<p>On what’s coming next in the enterprise features –</p> 
<blockquote> 
 <p>MongoDB 2.4 makes some major steps forward in the areas of security and monitoring, but we have much more planned for future releases. We think of security along the dimensions of authentication, authorization, and auditing. Future releases of MongoDB will continue to focus in these areas, and we will continue to enhance the tooling we provide with MongoDB. <a href="http://www.10gen.com/products/mongodb-monitoring-service">MongoDB Monitoring Service</a> (MMS) has been hugely popular in the MongoDB community with over 15,000 users and growing quickly. We will continue to invest in MMS and to provide both free, cloud-based tools as well as on-prem offerings as part of our Enterprise subscriptions.</p> 
</blockquote> 
<p>You can read more about the new features in MongoDB 2.4 in the <a href="http://docs.mongodb.org/manual/release-notes/2.4/">release notes</a>&nbsp;as well as <a href="http://docs.mongodb.org/manual/release-notes/2.4-overview/">the overview</a>.&nbsp;&nbsp;</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Insight into the Phases of Scaling</h3><p>Christopher Smith shared insight into approaching and solving the problems of scaling web applications in his presentation &quot;<a href="http://www.socallinuxexpo.org/scale11x/presentations/five-stages-scale">The Five Stages of Scale</a>&quot; at <a href="http://www.socallinuxexpo.org/scale11x">Scale11x</a> last month. In Christopher's presentation he made a case for approaching scaling in a stages with well defined components that are either added or optimized to improve the overall scale of a web application. &nbsp;He took the audience through an <a href="http://www.socallinuxexpo.org/sites/default/files/presentations/SCALE11.pdf">entertaining and informative journey</a> from load balancing through optimized usage of the UDP protocol.</p> 
<p class="MsoNormal">The most important basic scaling architecture is to have the ability to add web application servers behind a load balancer. A load balancer allows for linear scaling of a web application by partitioning requests and sessions across application servers. This technique amounts to adding application servers to increase scale linearly, however it just delays the inevitable <a href="http://www.facebook.com/pages/C10k-problem/120373131343187">C10K problem</a> because it does not increase the responsiveness of individual requests.</p> 
<p class="MsoNormal">Christopher spoke about how caching systems placed in front of web applications can provide for scaling by handling read operations. Multiple caching systems can be used in combination to maximize scale. Memcache servers and the like can <a href="http://www.infoq.com/news/2007/11/cfrp;jsessionid=53D3F7179F43DFDB153A126B01ED5B7D">store data in memory for quick retrieval by application servers</a>. A reverse proxy can be placed in front of the load balancer and serve cached resources. Finally a content delivery network (or CDN) can be used to put cached resources closer to end users. Caching however has its limitations in the writing of data.</p> 
<p class="MsoNormal">An optimized persistence framework will take your ability to scale writes to a new phase in scale. According to Christopher, succeeding in this phase in combination with the before mentioned will be sufficient for most people. <a href="http://cloud.dzone.com/news/sql-vs-nosql-cloud-which">Choosing the proper SQL database or NoSQL databases</a> to match the application data structures will significantly improve scale. The ability to do concurrent read/writes will increase throughput and responsiveness of write operations. Finally if you can &quot;Cheat on <a href="http://www.techopedia.com/definition/23949/atomicity-consistency-isolation-durability-acid">ACID (Particularly C &amp; D)</a>&quot; you can get more writes done faster.</p> 
<p class="MsoNormal">The underpinnings of these scaling techniques is the minimization of the latency of data reads/writes by web applications. Christopher shared the <a href="http://norvig.com/21-days.html#answers">latency times for different operations on computers</a>:&nbsp;</p> 
<ul> 
 <li>L1 cache reference - 0.5 ns</li> 
 <li>Branch mispredict - 5 ns</li> 
 <li>L2 cache reference - 7 ns&nbsp;</li> 
 <li>Mutex lock/unlock - 25 ns</li> 
 <li>Main memory reference - 100 ns&nbsp;</li> 
 <li>Compress 1K bytes with Zippy - 3,000 ns</li> 
 <li>Send 1K bytes over 1 Gbps network - 10,000 ns (or 0.01 ms)</li> 
 <li>Read 4K randomly from SSD* - 150,000 ns (or 0.15 ms)</li> 
 <li>Read 1 MB sequentially from memory - 250,000 ns (or 0.25 ms)</li> 
 <li>Round trip within same datacenter - 500,000 ns (or 0.5 ms)</li> 
 <li>Read 1 MB sequentially from SSD* - 1,000,000 ns (or 1 ms)</li> 
 <li>Disk seek - 10,000,000 ns (or 10 ms)</li> 
</ul> 
<div>
 The remainder of Christopher's presentation covered advanced scaling phases including:&nbsp;
</div> 
<ul> 
 <li>Passing code instead of data using commodity servers: <a href="http://www-01.ibm.com/software/data/infosphere/hadoop/mapreduce/">Map/Reduce (Hadoop)</a>, DHT, (Cassandra, HBase, Riak)</li> 
 <li>Routing data through data partitions: <a href="http://www.complexevents.com/2006/08/01/what%E2%80%99s-the-difference-between-esp-and-cep/">ESP/CEP</a>, Eigen, Storm, Esper, StreamBase, 0mq, etc.</li> 
 <li>Using UDP instead of TCP&nbsp;</li> 
</ul> 
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">The most advanced techniques are in use by companies that manage hyperscale web applications, for example <a href="http://www.facebook.com/note.php?note_id=39391378919">Facebook uses UDP to perform hundreds of thousands of requests/second against Memcached</a>.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
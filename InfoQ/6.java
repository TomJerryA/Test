<p><a href="http://www.greenplum.com">EMC Greenplum</a> has announced <a href="http://www.greenplum.com/blog/topics/hadoop/introducing-pivotal-hd">Pivotal HD</a>, a new Hadoop distribution including a fully compliant SQL MPP database running on HDFS and being “hundreds of times faster than Hive”.</p> 
<p><a href="http://www.greenplum.com/blog/topics/hadoop/introducing-pivotal-hd">Pivotal HD</a> contains the usual suspects of a standard Hadoop distribution – HDFS, Pig, Hive, Mahout, Map-Reduce, etc. – but adds a number of other components shown in the architectural snapshot below:</p> 
<blockquote> 
 <p class="image-wide"><a href="$image[7].png;jsessionid=C5CD3C292BED361B588EC83AB584B85B"><img title="image" style="border-left-width: 0px; border-right-width: 0px; background-image: none; border-bottom-width: 0px; padding-top: 0px; padding-left: 0px; display: inline; padding-right: 0px; border-top-width: 0px" border="0" alt="image" src="/resource/news/2013/02/Pivotal-HD-SQL-Hadoop/en/resources/Pivotal1.png;jsessionid=C5CD3C292BED361B588EC83AB584B85B" _href="img://Pivotal1.png" _p="true" /></a></p> 
</blockquote> 
<p>The main component of Pivotal is <a href="http://www.greenplum.com/blog/dive-in/hawq-the-new-benchmark-for-sql-on-hadoop">HAWQ</a>, a MPP (Massively Parallel Processing) relational database running directly on HDFS in Hadoop through a dynamic pipelining mechanism and featuring:</p> 
<ul> 
 <li>SQL Compliant – supporting all versions of SQL:&nbsp; ‘92, ‘99, 2003 OLAP, etc. 100% compatible with PostgreSQL 8.2.</li> 
 <li>Row or column-oriented data storage</li> 
 <li>Query Optimizer – queries can be run on hundreds of thousands of nodes</li> 
 <li>Fully ODBC/JDBC compliant</li> 
 <li>?Interactive Query – complex queries on large data sets are solved in seconds or even sub-seconds</li> 
 <li>Data management – provides table statistics, table security</li> 
 <li>Supports data stored in HDFS, Hive, HBase, Avro, ProtoBuf, Delimited Text and Sequence Files</li> 
 <li>Deep analytics – including data mining or machine learning algorithms</li> 
</ul> 
<p>Gavin Sherry, Sr. Director of Engineering at Greenplum, demoed (see <a href="http://www.greenplum.com/webcasts?commid=68121">video</a> at ~42’42”) running the following SQL SELECT statement on 1B rows totaling several TB of data on a 60-nodes HDFS cluster in ~13 seconds, providing close to real-time querying capabilities:</p> 
<p><code> </code></p> 
<p><code>SELECT gender, count (*)</code></p> 
<p><code> </code></p> 
<p><code>FROM retail.order JOIN customers ON retail.order.customer_ID = customers.customer_ID</code></p> 
<p><code>GROUP BY gender;</code></p> 
<p>According to <a href="http://www.greenplum.com/blog/author/donald-miner">Donald Miner</a>, Solutions Architect at EMC Greenplum, “<a href="http://www.greenplum.com/blog/topics/hadoop/introducing-pivotal-hd">HAWQ is hundreds of times faster than Hive</a>”, as show in the next graphic from Greenplum (<a href="http://public.brighttalk.com/resource/core/9757/hadoop-the_foundation_for_change_15465.pdf">PDF</a>):</p> 
<blockquote> 
 <p class="image-wide"><a href="$image[5].png;jsessionid=C5CD3C292BED361B588EC83AB584B85B"><img title="image" style="border-left-width: 0px; border-right-width: 0px; background-image: none; border-bottom-width: 0px; padding-top: 0px; padding-left: 0px; display: inline; padding-right: 0px; border-top-width: 0px" border="0" alt="image" src="/resource/news/2013/02/Pivotal-HD-SQL-Hadoop/en/resources/Pivotal2.png;jsessionid=C5CD3C292BED361B588EC83AB584B85B" _href="img://Pivotal2.png" _p="true" /></a></p> 
</blockquote> 
<p>HAWQ solves queries with “sub-second response time, while at the same time running over much larger datasets and processing with the full expressiveness of SQL, in the same engine.” Miner explains how they made it possible:</p> 
<blockquote> 
 <p>We have what we call “segment servers” manage a shard of each table. Several segment servers run on each data node of your cluster. This shard of data, however, is completely stored within HDFS. We have a “master” node that has the job of storing the top-level metadata, as well as building the query plan and pushing the node-local queries down to the segment servers.</p> 
 <p>When a query starts up, the data is loaded out of HDFS and into the HAWQ execution engine. HAWQ follows MPP architecture, streaming data through stages in a pipeline, instead of spilling and check pointing to disk (like MapReduce). Also, the segment servers are always running, so there is no spin-up time.</p> 
</blockquote> 
<p>Pivotal HD comes in three flavors (<a href="http://public.brighttalk.com/resource/core/9707/pivotal_hd_enterprise_datasheet-1_15391.pdf">PDF</a>): Enterprise, Database Services and a Community Edition for evaluation purposes.</p> 
<p id="lastElm"></p>
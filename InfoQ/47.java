<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Cassandra Gains Momentum On Enterprise Adoption Around 2.1 Release</h3><p>Cassandra is rapidly heading towards 2.1 release, with 2.1.0-beta1 already <a href="http://cassandra.apache.org/download/">available</a> for evaluation. Incubated and open sourced by <a href="http://pi1.informatik.uni-mannheim.de/filepool/big-data-seminar-pdfs/7_3_Cassandra%20-%20A%20Decentralized%20Structured%20Storage%20System.pdf">Facebook</a>, it is currently used by <a href="http://www.redditblog.com/2010/03/she-who-entangles-men.html">Reddit</a>, <a href="http://news.techworld.com/applications/3437514/netflix-foretells-house-of-cards-success-with-cassandra-big-data-engine/">Netflix</a>, <a href="http://www.slideshare.net/jaykumarpatel/cassandra-at-ebay-cassandra-summit-2013">Ebay</a>, <a href="http://www.slideshare.net/kevinweil/rainbird-realtime-analytics-at-twitter-strata-2011">Twitter</a> and others. Supported by <a href="http://www.datastax.com/">DataStax</a>, Cassandra is expanding its reach towards the enterprise world.</p>
<p>Cassandra version <a href="http://www.datastax.com/wp-content/uploads/2013/09/WP-DataStax-WhatsNewC2.0.pdf">2.0</a> delivered <a href="http://www.datastax.com/documentation/cassandra/2.0/cassandra/dml/dml_ltwt_transaction_c.html">lightweight transactions</a>, <a href="http://www.datastax.com/documentation/cql/3.1/cql/cql_reference/trigger_r.html#reference_ds_blw_qct_1l">triggers</a>, atomic batch <a href="http://www.datastax.com/documentation/cql/3.1/cql/cql_reference/prepared_stmt_c.html#concept_ds_yj5_13t_1l">guarantees</a> for a large set of prepared statements and <a href="http://www.datastax.com/dev/blog/whats-under-the-hood-in-cassandra-2-0">performance improvements</a>. The <a href="http://www.datastax.com/documentation/cql/3.1/cql/cql_intro_c.html">Cassandra Query Language</a> used in addition to the native drivers is based off SQL in the sense that data is put in tables containing rows of columns. Version 2.1 adds indexes on <a href="https://issues.apache.org/jira/browse/CASSANDRA-4511">collections</a> and <a href="https://issues.apache.org/jira/browse/CASSANDRA-5590">User Defined Functions</a>.</p>
<p>Cassandra 2.1 also uses <a href="http://www.datastax.com/dev/blog/improving-compaction-in-cassandra-with-cardinality-estimation">cardinality estimation</a> for data files compaction. The algorithm results in reducing <a href="https://wiki.apache.org/cassandra/MemtableSSTable">MemTable</a> memory usage by 85% and improving write performance by around <a href="http://www.slideshare.net/planetcassandra/apache-cassandra-20-21-by-jonathan-ellis-tokyo-cassandra-summit-2014/83">50%</a>. The algorithm used is <a href="https://github.com/addthis/stream-lib">HyperLogLog</a>, originally developed and open sourced by <a href="http://www.addthis.com/">AddThis</a>.</p>
<p>DataStax, as a <a href="http://en.wikipedia.org/wiki/DataStax">contributor</a> to the Apache Cassandra project and boasting a lineup of enterprise <a href="http://www.datastax.com/customers">clients</a> is one of the companies trying to bring Cassandra to a larger audience. Chief Evangelist for DataStax, <a href="https://twitter.com/PatrickMcFadin">Patrick McFadin</a> published an article <a href="http://patrickmcfadin.com/2014/02/11/mongodb-this-is-not-the-database-you-are-looking-for/">throwing the glove</a> on <a href="http://www.mongodb.com">MongoDB</a> on scaling issues. To reinforce his point, Mr. McFadin included testimonials from several Cassandra users including no other than <a href="http://www.linkedin.com/in/christoskalantzis">Chris Kalantzis</a>, Cloud Database Engineering Manager at <a href="http://www.netflix.com">Netflix</a>.</p>
<p>DataStax recently <a href="http://www.datastax.com/2014/02/datastax-announces-partner-network-program-with-accenture-google-cloud-platform-and-other-technology-service-providers-and-big-data-vendors">announced</a> a <a href="http://www.datastax.com/partners">partner network program</a>. Partnering up with <a href="http://www.accenture.com">Accenture</a> means that its clients will have better access to Cassandra technology. <a href="https://cloud.google.com/">Google Cloud Platform</a>, <a href="http://thedisruption.com/">HP Moonshot</a> and <a href="http://www.gogrid.com/">GoGrid</a> on the other hand will expand the available platforms and IaaS on which DataStax and Cassandra can be deployed on.</p>
<p>Along with expanding its reach in the enterprise through alliances, DataStax is entering the in-memory database sector by claiming up to 100 times better in-memory <a href="http://www.datastax.com/2014/02/datastax-adds-in-memory-option-to-cassandra-database-enables-companies-to-process-data-up-to-100x-faster-in-online-applications-2">performance</a> with its commercial offering, <a href="http://www.datastax.com/what-we-offer/products-services/datastax-enterprise">DataStax Enterprise 4</a>. DataStax enterprise edition <a href="http://www.datastax.com/wp-content/uploads/2011/09/DS-DataStax-Enterprise.pdf">also adds</a> enterprise search with Solr, integration with Hadoop, visual management and support. DataStax or not, Cassandra is gaining enterprise adoption that can not be ignored.</p><br><br><br><br><br><br></body></html>
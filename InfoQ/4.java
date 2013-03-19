<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>DataStax Brings Enterprise Security To Cassandra, Hadoop, Solr</h3><p><a href="http://3.datastax.com/datastax-enterprise.php" style="text-align: justify;">DataStax Enterprise</a>&nbsp;(DSE) 3.0 was announced last month with several Enterprise security features for a cluster using <a href="http://cassandra.apache.org/">Cassandra</a>, <a href="http://hadoop.apache.org/">Hadoop</a> and <a href="http://lucene.apache.org/solr/">Solr</a>. InfoQ caught up with <a href="http://www.linkedin.com/profile/view?id=11113193&amp;trk=tab_pro">Robin Schumacher</a>, VP of Products at DataStax to learn more.&nbsp;</p> 
<p align="justify">DSE is an integrated platform combining a production-certified version of Cassandra with Apache Solr for Enterprise Search and Apache Hadoop for batch analytics. The recently announced <a href="http://www.datastax.com/2013/02/datastax-enterprise-3-available-today">DSE 3.0</a>&nbsp;brings <a href="http://www.datastax.com/2013/02/a-closer-look-at-datastax-enterprise-3-0-%E2%80%93-part-1">several security features</a> that works across all three products. Robin explains that depending on how the customer wants to implement security, they can either</p> 
<ul> 
 <li> 
  <div align="justify">
   Choose an all-internal approach where security metadata is fully contained within the DataStax Enterprise cluster or
  </div> </li> 
 <li> 
  <div align="justify">
   Decide to use trusted 3rd party security software packages like Kerberos and LDAP with DataStax Enterprise to maintain their security information in an external manner.
  </div> </li> 
</ul> 
<p align="justify">Explaining how the security features go beyond Cassandra –</p> 
<blockquote> 
 <p align="justify">DSE features many different security features including transparent data encryption and Kerberos/LDAP external authentication, which are two big things that enterprises look for. Our security features are also integrated into the analytics and search dimensions as well as real time, which is something no other NoSQL vendor has.</p> 
</blockquote> 
<p align="justify">Robin also shared some of the challenges in making security work in a distributed cluster –</p> 
<blockquote style="text-align: start;"> 
 <p align="justify">In a &quot;master-less&quot; or peer-to-peer architecture, there is no master or namenode like what you see in some RDBMS's or standard Hadoop. So, with DataStax Enterprise, we needed to ensure that security was smartly configured and managed across the cluster so that each node is secure and enabled with the security features a customer wants to deploy (e.g. data auditing, client-to-node encryption, etc.) Further, because DataStax Enterprise supplies enterprise search with Solr and batch analytics with Hadoop (in addition to NoSQL scalability with Cassandra), we also needed to ensure those domains were covered from a security perspective. So we had cross-technology security considerations to tackle as well as handling general data protection matters across a large database cluster.</p> 
</blockquote> 
<p>The new version also improves manageability through <a href="http://www.datastax.com/2013/02/a-closer-look-at-datastax-enterprise-3-0-%E2%80%93-part-2">various tooling improvements</a> in <a href="http://www.datastax.com/products/opscenter">OpsCenter</a> 3.0, such as easier provisioning, granular control for backup/restore, better diagnostics, and more.&nbsp;</p> 
<p>Datastax also shared an interesting case study about <a href="http://www.datastax.com/resources/casestudies/healthcareanytime">HealthCare AnyTime</a> which already uses DSE 3.0 after moving from a relational database. The study claims $750k in projected savings over 5 years after shifting to DSE.&nbsp;</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
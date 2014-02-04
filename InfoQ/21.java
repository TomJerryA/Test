<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>DataFu Enters Incubation Status at Apache</h3><p><a href="https://www.linkedin.com/">LinkedIn</a>’s <a href="https://github.com/linkedin/datafu">DataFu</a> project, a collection of libraries for Hadoop, has now officially entered the <a href="http://datafu.incubator.apache.org/">incubation status</a> at the <a href="http://www.apache.org/">Apache Software Foundation (ASF)</a> since the first week of January.</p>
<p>The project was initially centered on being a collection of User-Defined Functions (UDFs) for Pig since its inception in January 2012. Compared to a more generic UDF collection like <a href="https://cwiki.apache.org/confluence/display/PIG/PiggyBank">Piggybank</a>, Datafu focuses on data-mining and statistics functions, such as quantiles computation or sampling methods. But since October 2013, a new library called DataFu <a href="http://datafu.incubator.apache.org/blog/2013/10/03/datafus-hourglass-incremental-data-processing-in-hadoop.html">Hourglass</a> was added to the project. Hourglass is a library for MapReduce that allows jobs to process incremental data. This is typically done by keeping the state of the previous job in HDFS and using that to process the new input. Both projects are now part of the incubator.</p>
<p>Entering incubation at Apache is no small feat for DataFu, and each project has to go through a <a href="http://incubator.apache.org/incubation/Incubation_Policy.html">rigorous scrutiny</a> and through a voting process before it is accepted in the incubator. DataFu had been around since early 2012 and only managed to get accepted in the incubator in early 2014. Graduation for a typical Apache project in incubation takes time, and once the infrastructure for the project is completed (wiki, mailing lists, tutorials, etc) DataFu will be able to graduate as its own top-level project in the ASF or as a sub-project of Hadoop.</p>
<p>With its recent introduction to the Apache incubator, DataFu has lots of plans for growth in the near future. One of the most critical functionality is to add the same set of UDFs for <a href="http://hive.apache.org/">Hive</a> and <a href="https://crunch.apache.org/">Crunch</a> to have a more widespread adoption. Part of this includes migrating the project build system to <a href="http://www.gradle.org/">Gradle</a>, something the DataFu community <a href="https://issues.apache.org/jira/browse/DATAFU-27">is currently working on</a>. Moving from <a href="http://ant.apache.org/">Ant</a> to Gradle will make it easier for DataFu to consolidate its community around a simpler process to add new functionality.</p>
<p>The DataFu community is still small but growing steadily. A recent contribution from Russell Jurney made the <a href="http://opennlp.apache.org/">Open NLP</a> project available as part of DataFu 1.3.0. The focus on the mailing list is on adding more UDFs and making DataFu “The WD-40 of Big Data”, as described by project contributors Matthew Hayes and Sam Shah.</p><br><br><br><br><br><br></body></html>
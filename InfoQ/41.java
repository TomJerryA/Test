<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Spring for Apache Hadoop 1.0</h3><p> SpringSource has released <a href="http://www.springsource.org/spring-data/hadoop">Spring for Apache Hadoop 1.0</a>. Spring for Apache Hadoop allows developers to write Hadoop applications under the Spring Framework. It also allows easily integration with Spring Batch and Spring Integration. Spring for Apache Hadoop is a subproject of the Spring Data umbrella project, and is released under the open source Apache 2.0 license. </p> 
<p> Hadoop applications generally are a collection of command line utilities, scripts and code. Spring for Apache Hadoop provides a consistent programming and declarative configuration model for developing Hadoop applications. Hadoop applications can now be implemented using the Spring programming model (Dependency Injection, POJOs, Helper Templates) and run as standard Java applications instead of command line utilities. Spring for Apache Hadoop supports reading from and writing to HDFS, running MapReduce, Streaming or Cascading jobs, and interacting with HBase, Hive and Pig. </p> 
<p> The key features of Spring for Apache Hadoop include: </p> 
<ul> 
 <li> Declarative configuration to create, configure, and parameterize Hadoop connectivity and MapReduce, Streaming, Hive, Pig, and Cascading jobs. There are &quot;runner&quot; classes that execute the different Hadoop interaction types, namely JobRunner, ToolRunner, JarRunner, HiveRunner, PigRunner, CascadeRunner and HdfsScriptRunner. </li> 
 <li> Comprehensive HDFS data access support using any JVM based scripting language, such as Groovy, JRuby, Jython and Rhino. </li> 
 <li> Template classes for Pig and Hive, named PigTemplate and HiveTemplate. These helper classes provide exception translation, resource management, and lightweight object mapping features. </li> 
 <li> Declarative configuration for HBase, and the introduction of HBaseTemplate for DAO support. </li> 
 <li> Declarative and programmatic support for Hadoop Tools, including File System Shell (FsShell) and Distributed Copy (DistCp). </li> 
 <li> Security support. Spring for Apache Hadoop is aware of the security constraints of the running Hadoop environment so moving from a local development environment to a fully Kerberos-secured Hadoop cluster is transparent. </li> 
 <li> Spring Batch support. With Spring Batch, multiple steps can be coordinated in a stateful manner and administered using a REST API. For example, Spring Batch's ability to manage the processing of large files can be used to import and export files to and from HDFS. </li> 
 <li> Spring Integration support. Spring Integration allows for the processing of event streams that can be transformed or filtered before being read and written to HDFS or other storage. </li> 
</ul> 
<p> Here are sample configuration and code snippets, mostly taken from the Spring for Hadoop blog or reference manual. </p> 
<p> MapReduce </p> 
<pre>
	&lt;!-- use the default configuration --&gt;
	&lt;hdp:configuration /&gt;

	&lt;!-- create the job --&gt;
	&lt;hdp:job id=&quot;word-count&quot; 
		input-path=&quot;/input/&quot; output-path=&quot;/ouput/&quot;
		mapper=&quot;org.apache.hadoop.examples.WordCount.TokenizerMapper&quot;
		reducer=&quot;org.apache.hadoop.examples.WordCount.IntSumReducer&quot; /&gt;

	&lt;!-- run the job --&gt;
	&lt;hdp:job-runner id=&quot;word-count-runner&quot; pre-action=&quot;cleanup-script&quot; post-action=&quot;export-results&quot; job=&quot;word-count&quot; run-at-startup=&quot;true&quot; /&gt;
</pre> 
<p> HDFS </p> 
<pre>
	&lt;!-- copy a file using Rhino --&gt;
	&lt;hdp:script id=&quot;inlined-js&quot; language=&quot;javascript&quot; run-at-startup=&quot;true&quot;&gt;
		importPackage(java.util)
		
		name = UUID.randomUUID().toString()
		scriptName = &quot;src/main/resources/hadoop.properties&quot;
		// fs - FileSystem instance based on 'hadoopConfiguration' bean
		fs.copyFromLocalFile(scriptName, name)
	&lt;/hdp:script&gt;
</pre> 
<p> HBase </p> 
<pre>
	&lt;!-- use default HBase configuration --&gt;
	&lt;hdp:hbase-configuration /&gt;
		
	&lt;!-- wire hbase configuration --&gt;
	&lt;bean id=&quot;hbaseTemplate&quot; class=&quot;org.springframework.data.hadoop.hbase.HbaseTemplate&quot; p:configuration-ref=&quot;hbaseConfiguration&quot; /&gt;
</pre> 
<pre>
	// read each row from HBaseTable (Java)
	List
 <string>
   rows = template.find(&quot;HBaseTable&quot;, &quot;HBaseColumn&quot;, new RowMapper
  <string>
   () { @Override public String mapRow(Result result, int rowNum) throws Exception { return result.toString(); } })); 
  </string>
 </string></pre> 
<p> Hive </p> 
<pre>
	&lt;!-- configure data source --&gt;
	&lt;bean id=&quot;hive-driver&quot; class=&quot;org.apache.hadoop.hive.jdbc.HiveDriver&quot; /&gt;
	&lt;bean id=&quot;hive-ds&quot; class=&quot;org.springframework.jdbc.datasource.SimpleDriverDataSource&quot; c:driver-ref=&quot;hive-driver&quot; c:url=&quot;${hive.url}&quot; /&gt;

	&lt;!-- configure standard JdbcTemplate declaration --&gt;
	&lt;bean id=&quot;hiveTemplate&quot; class=&quot;org.springframework.jdbc.core.JdbcTemplate&quot; c:data-source-ref=&quot;hive-ds&quot;/&gt;
</pre> 
<p> Pig </p> 
<pre>
	&lt;!-- run an external pig script --&gt;
	&lt;hdp:pig-runner id=&quot;pigRunner&quot; run-at-startup=&quot;true&quot;&gt;
		&lt;hdp:script location=&quot;pig-scripts/script.pig&quot;/&gt;
	&lt;/hdp:pig-runner&gt;
</pre> 
<p> To get started, you can <a href="http://www.springsource.com/download/community?project=Spring%20Data%20Hadoop">download Spring for Apache Hadoop</a>, or use the <em>org.springframework.data:spring-data-hadoop:1.0.0.RELEASE</em> Maven artifact. The <a href="http://static.springsource.org/spring-hadoop/docs/current/reference/html/batch-wordcount.html">WordCount example</a> for Spring for Hadoop is also available. There is also the <a href="http://www.youtube.com/watch?v=wlTnBzQ6KDU">Introducing Spring Hadoop</a> webinar on YouTube. </p> 
<p> Spring for Apache Hadoop requires JDK 6.0 and above, Spring Framework 3.0 (3.2 recommended) and above, and Apache Hadoop 0.20.2 (1.0.4 recommended). Hadoop YARN, NextGen or 2.x, is NOT supported at this time. Any Apache Hadoop 1.0.x distribution should be supported, and this includes distributions such as vanilla Apache Hadoop, Cloudera CDH3 and CDH4, Greenplum HD. </p> 
<p> For in-depth information, you can read the <a href="http://static.springsource.org/spring-hadoop/docs/1.0.0.RELEASE/reference/html/">Spring for Apache Hadoop Reference Manual</a> and <a href="http://static.springsource.org/spring-hadoop/docs/current/api/">Javadoc</a>. The Spring for Apache Hadoop <a href="https://github.com/SpringSource/spring-hadoop">source code</a> and <a href="https://github.com/SpringSource/spring-hadoop-samples/">examples</a> are hosted on GitHub. </p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
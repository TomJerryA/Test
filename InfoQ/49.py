<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Spring for Apache Hadoop 1.0リリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/spring-for-apache-hadoop-1.0;jsessionid=ABA412CA3C58BC03BFC84DD7E04CB914"><em>原文(投稿日：2013/03/13)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>SpringSourceは<a target="_blank" href="http://www.springsource.org/spring-data/hadoop">Spring for Apache Hadoop 1.0</a>をリリースした。Spring for Apache Hadoopを使えば、開発者はSpring Frameworkを使ってHadoopアプリケーションを開発できる。また、Spring BatchとSpring Integrationとも簡単に統合できる。Spring for Apache HadoopはSpring Data umbrella projectのサブプロジェクトであり、オープンソースのApache 2.0ライセンスでリリースされている。</p> 
 <p>一般的に、Hadoopアプリケーションはコマンドラインユーティリティやスクリプトやコードの塊だ。Spring for Apache Hadoopが提供するのは、Hadoopアプリケーションを開発するための一貫性のあるプログラミングと宣言的構成モデルだ。HadoopアプリケーションをSpringのプログラミングモデル(依存性注入、POJO、ヘルパーテンプレート)を使って開発し、コマンドラインユーティリティではなく、Javaのアプリケーションとして実行できる。また、Spring for Apache HadoopはHDFSへの読み書き、MapReduceの実行、ジョブのストリーミングと化すケーディング、HBase、Hive、Pigを使った操作ができる。</p> 
 <p>主な特徴は、</p> 
 <ul> 
  <li>Hadoopの連結やMapReduce、ストリーミング、Hive、Pig、Cascadingジョブの作成、構成、変数化を宣言的に構成できる。&quot;ランナー&quot;クラスが用意されており、Hadoopの操作を実行する。JobRunner、ToolRunner、JarRunner、HiveRunner、PigRunner、 CascadeRunner、HdfsScriptRunnerだ。</li> 
  <li>Groovy、JRuby、Jython、RhinoのようなJVMスクリプト言語を使ったHDFSへの包括的なデータアクセスのサポート。</li> 
  <li>PigとHive用のテンプレート、PigTemplateとHiveTemplate。このふたつのヘルパークラスは例外を解釈し、リソースを管理し、軽量オブジェクトマッピング機能を持つ。</li> 
  <li>HBaseの宣言的構成。また、HBaseTemplateでDAOをサポートする。</li> 
  <li>File System Shell (FsShell)やDistributed Copy (DistCp)のようなHadoop Toolsの宣言的なサポート。またプログラミングもできる。</li> 
  <li>セキュリティのサポート。Spring for Apache HadoopはHadoop実行環境のセキュリティの一貫性を認識する。したがって、ローカルの開発環境からケルベロス認証で守られたHadoopクラスタ環境への移行も透過的に実行できる。</li> 
  <li>Spring Batchのサポート。複数のステップが状態を維持しながら調整され、REST APIを使って管理されます。例えば、Spring Batchの大規模なファイルの処理を管理する能力はHDFSへファイルをインポートしたりエクスポートしたりするのに使える。</li> 
  <li>Spring Integrationのサポート。Spring Integrationを使えば、HDFSへ他のストレージに書き込まれたり読み込まれたりする前に変換されたりフィルタリングされたりするイベントストリームを処理できる。</li> 
 </ul> 
 <p>次の記述は、Spring for Hadoopのブログと参照マニュアルから抜粋したサンプルだ。</p> 
 <p>MapReduce</p> 
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
 <p>HDFS</p> 
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
 <p>HBase</p> 
 <pre>
	&lt;!-- use default HBase configuration --&gt;
	&lt;hdp:hbase-configuration /&gt;
		
	&lt;!-- wire hbase configuration --&gt;
	&lt;bean id=&quot;hbaseTemplate&quot; class=&quot;org.springframework.data.hadoop.hbase.HbaseTemplate&quot; p:configuration-ref=&quot;hbaseConfiguration&quot; /&gt;
</pre> 
 <pre>
	// read each row from HBaseTable (Java)
	List
  <string></string> rows = template.find(&quot;HBaseTable&quot;, &quot;HBaseColumn&quot;, new RowMapper
  <string></string>() {
		@Override
		public String mapRow(Result result, int rowNum) throws Exception {
			return result.toString();
		}
	}));
</pre> 
 <p>Hive</p> 
 <pre>
	&lt;!-- configure data source --&gt;
	&lt;bean id=&quot;hive-driver&quot; class=&quot;org.apache.hadoop.hive.jdbc.HiveDriver&quot; /&gt;
	&lt;bean id=&quot;hive-ds&quot; class=&quot;org.springframework.jdbc.datasource.SimpleDriverDataSource&quot; c:driver-ref=&quot;hive-driver&quot; c:url=&quot;${hive.url}&quot; /&gt;

	&lt;!-- configure standard JdbcTemplate declaration --&gt;
	&lt;bean id=&quot;hiveTemplate&quot; class=&quot;org.springframework.jdbc.core.JdbcTemplate&quot; c:data-source-ref=&quot;hive-ds&quot;/&gt;
</pre> 
 <p>Pig</p> 
 <pre>
	&lt;!-- run an external pig script --&gt;
	&lt;hdp:pig-runner id=&quot;pigRunner&quot; run-at-startup=&quot;true&quot;&gt;
		&lt;hdp:script location=&quot;pig-scripts/script.pig&quot;/&gt;
	&lt;/hdp:pig-runner&gt;
</pre> 
 <p>利用するには<a target="_blank" href="http://www.springsource.com/download/community?project=Spring%20Data%20Hadoop">Spring for Apache Hadoopをダウンロード</a>するか、<em>org.springframework.data:spring-data-hadoop:1.0.0.RELEASE</em> Mavenアーティファクトを使うかする。Spring for Hadoopの<a target="_blank" href="http://static.springsource.org/spring-hadoop/docs/current/reference/html/batch-wordcount.html">WordCountのサンプル</a>も利用できる。YouTubeで<a target="_blank" href="http://www.youtube.com/watch?v=wlTnBzQ6KDU">紹介動画</a>も見られる。</p> 
 <p>Spring for Apache HadoopにはJDK 6.0以上、Spring Framework 3.0 (推奨は3.2)以上、Apache Hadoop 0.20.2 (推奨は1.0.4)が必要。Hadoop YARN、NextGenまたは2.xは現時点ではサポートされていない。vanilla Apache Hadoop、Cloudera CDH3、CDH4、Greenplum HDなどのApache Hadoop 1.0.xのディストリビューションもサポートされないだろう。</p> 
 <p>より詳細な情報は、<a target="_blank" href="http://static.springsource.org/spring-hadoop/docs/1.0.0.RELEASE/reference/html/">Spring for Apache Hadoop Reference Manual</a>と<a target="_blank" href="http://static.springsource.org/spring-hadoop/docs/current/api/">Javadoc</a>で確認できる。Spring for Apache Hadoopの<a target="_blank" href="https://github.com/SpringSource/spring-hadoop">ソースコード</a>と<a target="_blank" href="https://github.com/SpringSource/spring-hadoop-samples/">サンプル</a>はGitHubで入手できる。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
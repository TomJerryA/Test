<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>オープンソースのSQL-in-Hadoopソリューション:我々はいまどこに？</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/open-source-sql-hadoop-solutions"><em>原文(投稿日：2013/12/10)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Facebookが最近<a href="http://www.infoq.com/news/2013/11/Presto">Prestoをオープンソース化</a>してリリースしたことで、既に飽和状態だったSQL-in-Hadoopマーケットがさらに錯綜している。多数のオープンソースツールが開発者の関心を集めようとしのぎを削っているのだ。Hortonworks社によるHive関連の<a href="http://hortonworks.com/labs/stinger/">Stinger initiative</a>, <a href="http://incubator.apache.org/drill/">Apache Drill</a>, <a href="http://tajo.incubator.apache.org/">Apache Tajo</a>, Cloudera社の<a href="http://www.cloudera.com/content/cloudera/en/products-and-services/cdh/impala.html">Impala</a>, Salesforce社の<a href="https://github.com/forcedotcom/phoenix">Phoenix</a> (for HBase), そして今回のFacebook社のPrestoがこれに挙げられる。</p> 
  <p>既に稼働中のシステムでHadoopを使っている組織はインタラクティブなSQLクエリのサポートと既存のBIツールからの円滑な移行を必要としている。Vijay Madhavan氏（eBay社）は、ブログ記事<a href="http://zettanalytics.blogspot.ie/2013/06/sql-in-hadoop.html">SQL in Hadoop landscape</a>でこう述べた。</p> 
  <blockquote> 
   <p>現在MapReduceベースの分析システムのほとんどにおいて、現行のHive, Pig, CascadingはSLA要素のうち非インタラクティブ領域、バッチ領域についてはうまく作用しています。よって多くのプロダクトはインタラクティブな&quot;SQL in Hadoop&quot;ソリューションを提供することで、SLA要素のうち残りのインタラクティブ領域とリアルタイム領域のサポートを試みているのです。</p> 
  </blockquote> 
  <p>SQL-in-Hadoopソリューションのユースケースにはインタラクティブでアドホックなクエリのサポート、MicroStrategyやTableau等のBIシステムのようなレポート/視覚化機能、マルチソースデータ（HDFS内の行動データとRDBMSやその他のデータソース内の人口統計データとを結合する場合など）のサポートが含まれる。</p> 
  <p>これらSQL-in-Hadoopソリューションの多くは下記のような共通の側面を持つ。</p> 
  <ol> 
   <li>メタデータレベルにおいては<a href="http://www.infoq.com/articles/HadoopMetadata">HCatalog</a>やHive Metastoreが複数のデータソース間のスキーマを管理するデファクトスタンダードとなりつつある。</li> 
   <li>さらに、特定の作業負荷においては<a href="$parquet.io">Parquet</a>や<a href="http://www.bigdatarepublic.com/author.asp?section_id=2840&amp;doc_id=262757">ORC</a>のようなデータフォーマットが現在においてもますます人気を集め、より広く使われるようになっている。</li> 
   <li>ソリューションの多くは（<a href="http://en.wikipedia.org/wiki/SQL-92">1992</a>, <a href="http://en.wikipedia.org/wiki/SQL:1999">1999</a>, <a href="http://en.wikipedia.org/wiki/SQL:2003">2003</a>など異なるバージョンにおける）広範囲のANSI SQLをサポートしているようである。</li> 
  </ol> 
  <p>上記のポイントにより、異なるSQL-in-Hadoopソリューションへの移行はさほど苦にはならないだろう。</p> 
  <p>しかし、下記のように顕著な違いも見られる。</p> 
  <ul> 
   <li>Stinger, Drill, TajoのようなApacheコミュニティベースのソリューションもあれば、Impala, Phoenix, Prestoのように独立した媒体のものもある。</li> 
   <li>問い合わせ可能なデータソースがHadoop エコシステムに限られているものがある一方、Presto, DrillのようによりフレキシブルでリレーショナルデータベースとNoSQLデータソースにその場で問い合わせ可能なものもある。</li> 
   <li>その他には、データに対するオペレーションの許可の違いも挙げられる。更新処理が可能なものがある一方、単なる（分散）クエリエンジンのものもある。</li> 
  </ul> 
  <p>過去10ヶ月から18ヶ月の間、ますます多くの開発者や企業がSQL-in-Hadoopソリューションを<a href="http://hadapt.com/blog/2013/10/02/classifying-the-sql-on-hadoop-solutions/">試し</a>、Hadoop上のデータへのアドホックなSQLアクセスや低遅延を実感出来ているようである。しかしながら、各ソリューションのユースケースや環境設定を考慮すると、長い目で見れば複数のSQL-in-Hadoopソリューションを検討する余地がありそうだ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
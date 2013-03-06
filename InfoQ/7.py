<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>GreenplumのPivotal HDがSQLのパワーとHadoopを結合する</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/02/Pivotal-HD-SQL-Hadoop;jsessionid=E9EE7807A8117027C84A176559CF8674"><em>原文(投稿日：2013/02/27)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://www.greenplum.com">EMC Greenplum</a> が新しいHadoopディストリビューションの <a target="_blank" href="http://www.greenplum.com/blog/topics/hadoop/introducing-pivotal-hd">Pivotal HD</a> を発表した。HDFS上で &quot;Hiveより数百倍高速&quot; に動作するという，SQL完全準拠のMPPデータベースを備える。</p> 
 <p><a target="_blank" href="http://www.greenplum.com/blog/topics/hadoop/introducing-pivotal-hd">Pivotal HD</a> は標準的なHadoopディストリビューション – HDFS，Pig，Hive，Mahout，MapReduceなど – の持つ特徴に加えて，下記のアーキテクチャ・スナップショットに示すような多数のコンポーネントを含んでいる。&nbsp;</p> 
 <p><img alt="" _p="true" _href="img://Pivotal1.png" src="/resource/news/2013/03/Pivotal-HD-SQL-Hadoop/ja/resources/Pivotal1.png;jsessionid=E9EE7807A8117027C84A176559CF8674" /></p> 
 <p>Pivitalのメインコンポーネントは，MPP (Massively Parallel Processing/超並列処理) リレーショナルデータベースの<a target="_blank" href="http://www.greenplum.com/blog/dive-in/hawq-the-new-benchmark-for-sql-on-hadoop">HAWQ</a>だ。動的パイプライン機構を通じてHadoopのHDFS上で直接動作するこのデータベースは，次のような特徴を持っている。</p> 
 <ul> 
  <li>SQL準拠 – '92，'93，2003 OLAPなど，全バージョンのSQLをサポートする。PostgreSQL 8.2と100%互換。</li> 
  <li>行または列指向のデータストレージ。</li> 
  <li>クエリ・オプティマイザ – 数十万のノード上でクエリの分散実行が可能。</li> 
  <li>ODBC/JDBC完全準拠。</li> 
  <li>インタラクティブ・クエリ – 巨大なデータを扱う複雑なクエリでも，秒ないしサブ秒のオーダで解析する。</li> 
  <li>データ管理 – テーブルの統計情報とセキュリティを提供する。</li> 
  <li>HDFS，Hive，HBase，Avro，ProBufに格納されたデータ，区切りテキスト，シーケンスファイルをサポートする。</li> 
  <li>Deep Analytics – データマイニング，機械学習アルゴリズムなどを備える。</li> 
 </ul> 
 <p>Greenplumのシニアディレクタ兼エンジニアであるGavin Sherry氏が行ったデモ (<a target="_blank" href="http://www.greenplum.com/webcasts?commid=68121">ビデオ</a>: 42'42&quot;付近) では，60ノードHDFSクラスタ上の10億行，合計で数TBに及ぶデータを対象として，以下のSQL SELECT文を13秒以内で実行するという，ほぼリアルタイムのクエリ機能が披露されている。</p> 
 <p>&nbsp;</p> 
 <p><code>SELECT gender, count (*)</code></p> 
 <p>&nbsp;</p> 
 <p><code>FROM retail.order JOIN customers ON retail.order.customer_ID = customers.customer_ID</code></p> 
 <p><code>GROUP BY gender;</code></p> 
 <p>EMC Greenplumのソリューションアーキテクトである <a target="_blank" href="http://www.greenplum.com/blog/author/donald-miner">Donald Miner</a> 氏によると，同社が提供する次の図(<a target="_blank" href="http://public.brighttalk.com/resource/core/9757/hadoop-the_foundation_for_change_15465.pdf">PDF</a>)に示すように，&quot;<a target="_blank" href="http://www.greenplum.com/blog/topics/hadoop/introducing-pivotal-hd">HAWQはHiveの数百倍高速</a>” だ。&nbsp;</p> 
 <p><img alt="" _p="true" _href="img://Pivotal2.png" src="/resource/news/2013/03/Pivotal-HD-SQL-Hadoop/ja/resources/Pivotal2.png;jsessionid=E9EE7807A8117027C84A176559CF8674" /></p> 
 <p>HAWQは&quot;巨大なデータセットを対象に，SQLの機能をフル活用するような処理を，単一エンジン上で複数同時に実行するような場合でも，１秒未満のレスポンスタイムで&quot; クエリを処理することができる。そのようなことが可能な理由を，Miner氏は次のように説明する。</p> 
 <blockquote> 
  <p>このシステムでは，各テーブルの部分を管理する &quot;セグメントサーバ&quot; という概念を持っています。クラスタの各データノードで複数のセグメントサーバが動作します。データの各セグメントはすべてHDFS内部に格納されています。&quot;マスタ&quot;ノードがトップレベルのメタデータの格納を行うと同時に，クエリプランを構築し，各ノードで実行するクエリをセグメントサーバに配信するのです。</p> 
  <p>クエリが起動するとデータがHDFSから読み出されて，HAWQ実行エンジンへと渡されます。HAWQはMPPアーキテクチャに従って，パイプラインの各ステージ経由でデータをストリーミングします。ディスクへの保存やチェックポイントの記録 (MapReduceのような) は行いません。さらにセグメントサーバは常時実行していますので，スピンアップの時間も不要になります。</p> 
 </blockquote> 
 <p>Pivotal HDは３種類のパッケージ (<a target="_blank" href="http://public.brighttalk.com/resource/core/9707/pivotal_hd_enterprise_datasheet-1_15391.pdf">PDF</a>: Enterprise，Database Services， 評価用のCommunity Edition) で提供されている。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
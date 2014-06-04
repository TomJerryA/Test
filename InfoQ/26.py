<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>SplunkがHunk 6.1をリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/splunk-hunk-6.1"><em>原文(投稿日：2014/05/21)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://www.splunk.com">Splunk</a>は機械が生成したデータを検索や監視、分析することに特化した企業だ。同社はHunk 6.1のリリースを<a href="http://www.splunk.com/view/splunk-introduces-hunk-6-1/SP-CAAAMTB">発表</a>した。<a href="http://www.splunk.com/view/hunk/SP-CAAAH2E">Hunk</a>はビッグデータ分析のプラットフォームを提供する。</p> 
  <p>ビックデータ上でアドホック分析を実施し、有益な情報を取り出すのは難しいことだ。Hunkは<a href="http://hadoop.apache.org">Hadoop</a>やほかの<a href="http://en.wikipedia.org/wiki/NoSQL">NoSQL</a>を使って素早くデータを探索し、分析し、視覚化することでこの難しさに対処する。</p> 
  <p>Hunkは<a href="http://hive.apache.org">Hive</a>に似ている。HiveはHadoop上のデータに対する問い合わせを処理するためのSQLエンジンだ。HiveもHunkもユーザの問い合わせを受け付けて、<a href="http://en.wikipedia.org/wiki/MapReduce">MapReduce</a>のジョブにコンパイルし、クラスタ上でそのジョブを実行する。しかし、HunkはHiveとはいくつかの点で異なる。</p> 
  <ul> 
   <li>HunkはSQLではなく<a href="http://en.wikipedia.org/wiki/SPL_(Search_Processing_Language)">Search Processing Language</a> (SPL)と呼ばれる独自の言語の問い合わせを処理する。</li> 
   <li>Hunkはスキーマを事前に定義しておくが必要ない。そのかわり、問い合わせが行われた段階でスキーマを作成する。</li> 
   <li>HunkはMapReduceのジョブの完了を待たずに結果を表示する。インタラクティブな操作を実現するため、MapReduceのジョブがバックグラウンドで動いている間に中間の結果を即時にストリームする。</li> 
   <li>問い合わせエンジンに加え、Hunkには組み込みのビジュアライゼーションレイヤが含まれており、ユーザは検索結果からインタラクティブなチャートを作成して保存することができる。</li> 
  </ul> 
  <p>SplunkにはHunkの最新のバージョンにいくつか<a href="http://www.splunk.com/view/hunk-whats-new/SP-CAAAMSE">新しい機能</a>を追加した。</p> 
  <ul> 
   <li><a href="http://docs.splunk.com/Documentation/Splunk/latest/Report/Acceleratereports">レポートアクセラレーション</a>はHadoopの検索結果をキャッシュすることで応答時間と性能を改善する。レポート単位で設定できる。</li> 
   <li>ダッシュボードとチャートがインタラクティブになり、チャートのオーバレイをサポートした。また、パンアンドズームコントロールとドリルダウンをサポートした。</li> 
   <li>チャートとレポートをサードパーティのアプリケーションに組み込めるようになった。</li> 
   <li>Hadoopに依存しなくなった。<a href="http://docs.splunk.com/Documentation/Hunk/6.1/Hunk/StreamingLibraries">ストリーミングリソースライブラリ</a>を使うことで開発者はHunkをどのようなNoSQLエンジンにも接続できるようになった。<a href="http://cassandra.apache.org">Apache Cassandra</a>や<a href="http://www.mongodb.org">MongoDB</a>や<a href="http://www.neo4j.org">Neo4j</a>などだ。</li> 
   <li><a href="http://docs.splunk.com/Documentation/Hunk/6.1/Hunk/Userimpersonation">パススルー認証</a>の改善によって、管理者はどのユーザがMapReduceジョブを実行するか、<a href="http://hadoop.apache.org/docs/r2.3.0/hadoop-project-dist/hadoop-hdfs/HdfsUserGuide.html">HDFS</a>ファイルにアクセスできるかを管理できるようになった。</li> 
   <li><a href="http://wiki.apache.org/hadoop/SequenceFile">シーケンスファイル</a>、<a href="http://en.wikipedia.org/wiki/RCFile">RCFile</a>、<a href="http://docs.hortonworks.com/HDPDocuments/HDP2/HDP-2.0.0.2/ds_Hive/orcfile.html">ORC files</a>、<a href="http://parquet.io">Parquet</a>などのファイルフォーマットをサポートした。</li> 
  </ul> 
  <p>今回のリリースに対するコミュニティの反応は良好だ。以下のようなツイートが見られた。</p> 
  <blockquote> 
   <p>Splunk、Hunk、hadoopがひとつのシステムになたt。ギーク女子にとってはとっても楽しい。@mskerryschaffer - Kerry Schaffer、Marketing Associatesの情報技術ディレクター</p> 
  </blockquote> 
  <blockquote> 
   <p>#SplunkLiveの新しい製品リリース。Splunk EnterpriseとHunkはAppDevの世界にも提供される。競争力の強化につながる。@aconcolino - Anthony Concolino氏、コンサルタント</p> 
  </blockquote> 
  <blockquote> 
   <p>@splunkには賢い製品名をつけたね。&quot;Splunk Hunk for Hadoop&quot;って言いやすい。@tobingilman - Tobin Gilman氏、Bootstrap Marketing and Business Developmentのビックデータリード</p> 
  </blockquote> 
  <p>機能の一覧は<a href="http://www.splunk.com/web_assets/pdfs/secure/Hunk_Product_Data_Sheet.pdf">Hunkの製品シート</a>で確認できる。また詳細は<a href="http://www.splunk.com/view/hunk/SP-CAAAH2E">ここ</a>で確認できる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
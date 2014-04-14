<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>セルベースのセキュリティが導入されたHBase 0.98</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/hbase-098"><em>原文(投稿日：2014/03/21)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Apacheは<a href="https://blogs.apache.org/hbase/entry/apache_hbase_0_98_0">HBase 0.98</a>をリリースした。セルベースのセキュリティを通じてApache <a href="http://accumulo.apache.org/">Accumulo</a>との共通化を計ると同時に，230以上のJIRAイシューを解決することを主な目的としている。新たに導入されたセキュリティ機能は，Accumuloをモデルとしたものだ。</p> 
  <p>HBaseとAccumuloは，ともにApacheのプロジェクトである。いずれもApache Hadoopを稼働するGoogleの<a href="http://research.google.com/archive/bigtable.html">BigTable</a>インフラストラクチャをモデルとして，分散型のデータストアを提供する。</p> 
  <p>セルはHBaseの最小ユニットで，キーを使用してアドレスすることができる。これまでのバージョンでは，セルのアクセス権は列ファミリから継承するようになっていた。そのパーミッションは，さらにテーブルから継承する構造だった。</p> 
  <p>同様のデータモデルを採用するAccumuloは，一般的なACL(Access Control List)とは違うものの，さらに詳細なセルベースのセキュリティモデルを備えている。Accumuloのキーはラベルから構成され，セルレベルにおける異なるデータ部分へのアクセスに対して，非常に詳細な判断を可能にしている。この方式により，ラベルの内容の参照を通じて，同じデータに対する複数の情報アクセスレベルを設定することができるのだ。</p> 
  <p>HBase 0.98は，イシュー<a href="https://issues.apache.org/jira/browse/HBASE-8496">HBASE-8496</a>と<a href="https://issues.apache.org/jira/browse/HBASE-7663">HBASE-7663</a>に対処している。セルベースセキュリティの実装にはタグを採用した。タグには任意のメタデータを格納することができる。これによってACLセキュリティモデルをテーブルからカラムファミリ，セルに拡張することが可能になる。さらにタグには，可視性の定義を格納することもできる。さまざまな情報単位へのアクセスに対して，Accumuloのセルと同程度の詳細レベルを提供することが可能だ。</p> 
  <p><a href="https://hbase.apache.org/book.html#hbase.accesscontrol.configuration">API</a>の面からは，以下のようなコールを行うことで，セルにuser1のアクセス権を設定することができる。</p> 
  <pre>
put.setACL(“user1”, new Permission(Permission.Action.READ))
</pre> 
  <p>&nbsp;</p> 
  <p>Intelの主席アーキテクトで，HBaseに長く貢献しているAndrew Purtell氏は，“Apache HBase 0.98のリリースは，エンドユーザの観点によるいくつかのセキュリティ機能を収束したものです。”と述べている。“HBaseではこれまで，ACLをサポートしてきました。今回のリリースではAccumuloスタイルの可視性ラベルもサポートすることで，ユーザに対して，両プロジェクトの機能のスーパーセットを提供します。” Purtell氏によるリリースのプログラム管理については，氏の<a href="https://communities.intel.com/community/itpeernetwork/datastack/blog/2013/10/29/hbase-cell-security">セルベースのセキュリティに関するブログ</a>に概要が紹介されている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
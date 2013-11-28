<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Amazon RDS、PostgreSQLをサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/amazon-rds-postgresql"><em>原文(投稿日：2013/11/18)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Amazon RDSがサポートするデータベースに<a href="http://aws.typepad.com/aws/2013/11/amazon-rds-for-postgresql-now-available.html">PostgreSQLが追加された</a>。まずはPostgresの<a href="http://www.postgresql.org/docs/9.3/static/release-9-3-1.html">version 9.3.1</a>をサポートし、新しいバージョンが利用可能なればサポートしていく計画だ。</p> 
  <p>Postgres RDSのシングルインスタンスはデータ3 TBおよび30,000 IOPSまでスケールアップすることができる。サポートする重要な機能は以下の通り。</p> 
  <ul> 
   <li>通常サポートされる全RDS機能。Multi-AZデプロイメント、Provisioned IOPS、仮想プライベートクラウド、自動バックアップ、Point-in-timeリカバリ、クロスリージョン・スナップショットコピーなど。</li> 
   <li><a href="http://www.postgis.net/">PostGIS</a>空間データベース拡張</li> 
   <li>PL/Perl、PL/Tcl、PL/pgSQL言語</li> 
   <li>全文検索辞書（<a href="http://www.postgresql.org/docs/9.3/static/dict-int.html">dict_int</a>、<a href="http://www.postgresql.org/docs/9.3/static/dict-xsyn.html">dict_xsyn</a>、<a href="http://www.postgresql.org/docs/9.3/static/unaccent.html">unaccent</a>）</li> 
   <li>先進的なデータ型。<a href="http://www.postgresql.org/docs/9.2/static/hstore.html">Hstore</a>、JSONなど。</li> 
   <li><a href="http://www.postgresql.org/docs/9.3/static/dblink.html">dblink</a>。データベースセッション内から他のPostgreSQLデータベースへの接続をサポートする。</li> 
  </ul> 
  <p>サポートしている全拡張について、詳しくは<a href="http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_PostgreSQL.html">公式ドキュメント</a>を参照。</p> 
  <p><a href="http://aws.amazon.com/rds/">RDS</a>(Amazon Relational Database Service)とは、クラウドにおけるリレーショナルデータベースのセットアップ、運用、スケーリングを簡単にするWebサービスだ。RDSはすでに別のデータベースエンジン、MySQL、Oracle、SQL Serverなどもサポートしている。.&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
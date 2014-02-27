<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>GoogleのBigQueryが勢いづく</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/bigquery-gaining-momentum"><em>原文(投稿日：2014/02/14)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="https://developers.google.com/bigquery/what-is-bigquery">Googleが提供するSaaS型のデータストア</a>であるBigQueryが勢いづいているようだ。BigQueryを使うとクラウド上の<a href="https://cloud.google.com/developers/articles/bigquery-in-practice">大規模な列指向のデータ構造</a>に問い合わせが実行できる。開発者はデータを<a href="https://developers.google.com/storage/">Google Cloud Storage</a>(Amazon S3のようなもの)経由でBigQueryへロードするか、<a href="https://developers.google.com/bigquery/streaming-data-into-bigquery">ストリームとしてデータを投入</a>し、SQLライクな言語を使ってOLAPスタイルの問い合わせを実現できる。</p> 
  <p>実際に利用した人がBigQueryの利用経験を共有し始めている。例えば、Shine TechnologiesのGraham Polley氏に<a href="http://blog.shinetech.com/2014/01/18/reeling-in-big-data-using-googles-bigquery/">よれば</a>、</p> 
  <blockquote>
   テストでBigQueryを使ってみることにしました。データは15億行もあります。とても面白そうなテストになると思いました。果たしてGoogleの&quot;数十億行の大規模データをインタラクティブに分析できる&quot;というセールストークは本当なのか。結果は驚くべきことに本当でした。本当に驚きました。キャッシュを使っていなくても(キャッシュはドグルで有効無効を切り替えられます)、15億行のデータに対する比較的複雑な集計問い合わせが20秒から25秒で返ってきました。
  </blockquote> 
  <p>BigQueryはスタンドアロンでも使えるが、<a href="https://developers.google.com/apps-script/articles/bigquery_tutorial">Google Apps Script</a>やGoogle Analyticsと連携させることもできる。Analyticsとの連携については、Jonathan Weber氏(LunaMetricsのデータエバンジェリスト)が<a href="http://www.lunametrics.com/blog/2014/01/27/google-analytics-bigquery-whys-hows/">有益な情報</a>を提供している。</p> 
  <blockquote>
   まず、BigQueryのエクスポートはGoogle Analyticsのプレミアムカスタマーだけが使えいます。プレミアムアカウントの管理者にお願いして、BigQueryのエクスポート機能を有効にしてもらう必要があります。また、BigQueryのストレージとプロセッシングにはコストがかかることも知っておかなければなりません。しかし、Google Analyticsのプレミアムユーザの場合は月額500ドルのクレジットを使って支払いができます。多くの場合、500ドルもあれば十分です。BigQueryを利用している私たちの顧客の場合、サイトには月間で600万の訪問があり、5000万のページビューがあります。データは9月からエクスポートしていますが、今月の請求は12.86ドルでした。
   <br /> 
  </blockquote> 
  <p>BigQueryはクラウドベースのソリューションとして利用できるが、BigQueryの基盤となっている技術(<a href="http://research.google.com/pubs/pub36632.html">Dremel</a>)は多くのApache DrillやImpalaのような<a href="http://www.infoq.com/news/2013/12/open-source-sql-hadoop-solutions">オープンソースのSQL-in-Hadoopソリューション</a>で使われている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
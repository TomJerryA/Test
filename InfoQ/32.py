<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>HerokuとSalesforce.comのデータリポジトリをリンクする新たなコネクタを発表</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/salesforce-heroku-connector"><em>原文(投稿日：2014/05/23)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Heroku（2010年にSalesforce.comが買収）が2つのクラウドプラットフォームの最初のビルトイン統合サービスを発表した。この<a href="https://www.heroku.com/postgres">Heroku Postgres</a>とSalesforce (<a href="http://siliconangle.com/blog/2013/11/20/salesforces-benioff-explains-grand-vision-behind-salesforce1/">Oracle</a>) データベースの双方向データ同期は、Herokuにホストされたモバイル顧客向けアプリケーションをSalesforceで動いているビジネスシステムにつなげる手段として位置づけられている。</p> 
  <p>HerokuとForce.comはまったく異なるアプリケーション開発環境だ。Herokuはオープンソースのフレームワークとアドオンのアプリケーションサービスを使った、カスタムビルドのスケーラブルなＷebアプリケーションであるのに対し、Salesforceはコード拡張にプロプライエタリなプログラミング言語を用いた、マウス操作によるアプリケーション設計を提供する。Salesforceはこの言語を補完的なものとして<a href="https://developer.salesforce.com/platform/overview">位置づけている</a>。最近まで、開発者がSalesforceとHerokuを統合したければ、APIもしくはコマンドラインインターフェイスを介してやるしかなかった。昨年11月に<a href="https://blog.heroku.com/archives/2013/11/19/tools-for-integrating-heroku-apps-with-salesforce">Herokuが統合プロダクトに関する発表</a>を行って、状況は変化した。そして先週、Herokuは<a href="https://www.heroku.com/connect">Salesforce1 Heroku Connect</a>を発表し、ブログにこう書いた。</p> 
  <blockquote> 
   <p>この新しいHerokuプロダクトは同期サービスです。概念的にはDropboxやiCloudと似ていて、SalesforceデプロイメントとHeroku Postgresデータベース間でデータを同期します。Force.comとHerokuのプラットフォームのデータ層を1つにする、すなわち、同じデータが各クラウドネイティブなデータベースにシームレスに反映されるようにすることで、あなたは1つのアプリケーションでそれぞれのプラットフォームの機能を使うことができます。変換したり、統合したりする必要はありません。</p> 
  </blockquote> 
  <p><a href="http://techcrunch.com/2014/05/13/heroku-and-salesforce-aim-to-link-business-process-and-customer-experience/">TechCrunchとのインタビュー</a>で、 Salesforceのマーケティング担当VPであるScott Holden氏は、顧客はそれぞれの環境で動作するアプリに緊密な統合と認知度の増大を求めている、と説明した。</p> 
  <blockquote> 
   <p>現在の企業は顧客とインタラクトするアプリを作ろうとしていますが、そのときに何がおこるのかよくわかっていない、とHolden氏は説明しています。「ビジネスにつなげずに、アプリを動かしているのです」</p> 
   <p>こうしたプロダクトやるべきことは、エンタープライズ分析やビジネスアプリへの接続を提供することです。これによりビジネスは自分たちが作ったアプリで顧客がやっていることを知ることができます。マーケティング自動化アプリにつなげることで、メッセージを配信したり、個々の顧客の行動に基づいた提案をすることもできるでしょう。ビジネスプロセスとカスタマーエンゲージメントを1つのパッケージにするのです。Holden氏はこのように語っています。</p> 
  </blockquote> 
  <p>開発者 (あるいはテクノロジに精通したビジネスユーザ) はWebベースのコンソールを使って、Salesforceデータベースからコピーするために標準あるいはカスタムのオブジェクトのサブセットを定義することができる。デフォルトでは、<a href="https://devcenter.heroku.com/articles/herokuconnect#synchronization-frequency">データはSalesforceから10分毎に取得されて</a>、Heroku Postgres内の複製されたスキーマにロードされるようになっている。双方向の読み書き同期を設定した場合には、変更が5分毎にSalesforceに戻されるようになる。コンフリクトを減らすため、<a href="https://devcenter.heroku.com/articles/herokuconnect#how-heroku-connect-works">Heroku Postgresで変更されたカラムだけがSalesforceにコピーされる</a>よう設計されている。Heroku ConnectアドオンはHerokuアプリケーションが動いているのと同じデータセンターにセットアップされるが、HerokuデータセンターがSalesforce自体とどう配置されているかははっきりしていない。</p> 
  <p>データを同期するため、Heroku ConnectはSalesforde APIにセキュアに接続し、データサイズに応じてSalesforce <a href="http://www.salesforce.com/us/developer/docs/api/index.htm">SOAP</a>か<a href="http://www.salesforce.com/us/developer/docs/api_asynch/index.htm">Bulk</a> APIを自動的に選択するようになっている。このコネクタの売り文句の1つは、API経由ではなく従来のSQL構文を使ってSalesforceをクエリできることだ。モバイルアプリはSystem of Recordに負担をかけるおそれがあり、Herokuはこのコネクタを<a href="https://blog.heroku.com/archives/2014/5/13/introducing_heroku_connect">アプリのパフォーマンスを改善する</a>1つの手段だと考えている。</p> 
  <blockquote> 
   <p>すべてのデータはデータベースにステートフルに格納されるため、Heroku ConnectはPostgresをAPIキャッシュとして使えるようにします。Salesforceへのコールバックをする必要なしに、読み出しリクエストにすばやく応答することができます。データのリアルタイムアクセスをスケールするのに、あなたはインデックス、拡張、特殊データ型を含むPostgresのすべての機能を利用することができます。</p> 
  </blockquote> 
  <p>開発者はここで<a href="https://www.heroku.com/connect">Heroku Connect</a>にサインナップすることができる。その機能については<a href="https://devcenter.heroku.com/articles/herokuconnect">Heroku Dev Center</a>で調べることができる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
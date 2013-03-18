<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>FTP, NGINXキャッシング, Apache TomEE, MarinaDB 10をサポートするJelastic 1.9</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Jelastic-1-9;jsessionid=CE07B6AB832361B828946629E476CA28"><em>原文(投稿日：2013/03/11)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>JavaとPHPをPaaS(Platform-as-a-Service) 提供するクラウドサーバホスティング用プラットフォームの <a target="_blank" href="http://jelastic.com/press-releases/jelastic-launches-new-version-1-9">Jelastic</a> がバージョン1.9をリリースした。FTP/FTPSと <a target="_blank" href="http://wiki.nginx.org/Main">NGINX</a> キャッシュのサポートに加えて，今回のリリースではTomcatのエンタープライズ版である <a target="_blank" href="http://tomee.apache.org/apache-tomee.html">Apache TomEE</a>，マルチソース・レプリケーションと動的列，さらに <a target="_blank" href="http://blog.mariadb.org/mariadb-galera-cluster-5-5-29-stable-ga-released/">MarinaDB Galera Cluster</a> も利用可能な <a target="_blank" href="http://blog.mariadb.org/tag/mariadb-10/">MariaDB 10</a> のサポートが提供される。</p> 
 <p>Jelasticには先進的なレポートダッシュボードも装備されている。ユーザの契約状況や解約率，アクセス率，機能別の人気，ユーザ単位での利益など，<a target="_blank" href="http://searchcloudcomputing.techtarget.com/definition/Platform-as-a-Service-PaaS">PaaS</a> ビジネスの状況やユーザ行動をあらゆる面から分析することが可能だ。ログ管理システムも刷新され，ブラウザベースの新ユーザインターフェースを利用するJelasticユーザを効率的にサポートできるようになった。</p> 
 <p>Jelastic 1.9を使うことによって，RPMからのテンプレートの構築や，データベース管理用WebページでのセキュアなSSL(HTTPS)利用が可能になる。さらにJelastic クラスタ管理(Jelastic Cluster Admin / JCA)では，スマート・ライブ・インテグレーションやダッシュボードのカスタマイズ，ユーザ課金の回収歴，料金表管理，システム監視などの機能も利用可能だ。</p> 
 <p>Jelasticフレームワークは，JavaあるいはPHPアプリケーションの使用状況に応じてサーバがリソースを割り当てるように設計されている。</p> 
 <p>チーフオペレーティングオフィサのDmitry Sotnikov氏がInfoQの独占インタビューに応じて，Jelastic 1.9に関する詳細な内容を説明してくれた。<br /> <br /> <strong>InfoQ: PaaSは本来，どのような意味なのでしょう？</strong></p> 
 <blockquote>
  IT管理の負担をなくすためのホスティング自動化がPaaS(Platform-as-a-Service)です。通常のホスティングや Infrastructure-as-a-Service は，基本的に仮想マシンを提供してくれますが，その時点からアプリケーションを稼働させるまでには，まだ多くの管理作業が残っています - サーバやデータベースのセットアップ，ロードバランシング設定などに加えて，高可用性が必要ならばクラスタの構成も必要です。すべてのサーバに対して，設定変更やアプリケーション，ライブラリのバージョンなどの一貫性を確保しなければなりません。アプリケーションを更新したり必要なサーバを追加したりする度に，このような作業を何度も何度も繰り返さなければならないのです。
  <br /> &nbsp;
  <br /> PaaSでは，これらはすべてプラットフォームが自動化します。サーバ管理やスケーリングといったことはすべてプラットフォームに任せて，素晴らしいアプリケーションの開発に専念できるのです。
  <br /> 
  <br /> それらに加えて，開発者や業務用IT関係者に喜ばれるような機能もたくさんあります。例えば， 
  <ul> 
   <li>ソースコードリポジトリから直接，クラウド上にアプリケーションを構築することが可能。</li> 
   <li>アプリケーション開発ライフサイクルのサポート。環境のクローン作成(データもすべて同時に！)や入れ替え(開発とステージング，といったように)も可能。</li> 
   <li>権限管理，役割管理を持ったチーム作業のサポート。</li> 
   <li>一般的な開発ツールとの統合。</li> 
   <li>リモートデバッグ。</li> 
   <li>モニタリングやログ管理など，一般的なサードパーティサービスとの統合。</li> 
  </ul> 
 </blockquote> 
 <p><strong>InfoQ: Jelasticと通常の共有ホスティングとの違いについて説明して頂けますか？</strong></p> 
 <blockquote>
  Jelasticは，単にWebサーバの一部を使える，というものではありません。ダッシュボードにログインして数回マウスをクリックするだけで，アプリケーションサーバやロードバランサ，データベース，Memcachedなど，すべての環境が構築できるのです。あとは普通にアプリケーションのアップロードを行うか，GITまたはSVNコードリポジトリの接続情報を指定するだけです - あとはJelasticがアプリケーションを起動して，クラウドへと自動的にスケーリングしてくれます。
  <br /> 
  <br /> つまり共有ホスティングとは違って，アプリケーションを多数のサーバに容易に展開できるパワーに加えて，設定の変更やアプリケーションライブラリのアップロードといった，サーバを完全に管理できるフレキシビリティも手に入るのです。
 </blockquote> 
 <p><strong>InfoQ: Jelasticにはいくつのサイトをホストできるのでしょう？</strong></p> 
 <blockquote>
  制限はありません。Jelasticの提供するセルフサービス・ダッシュボードを使用すれば，サーバが何台必要か，その中から何台使用するのか，それをJelasticがスケールするかどうか，どのようにスケールするのかなど，ユーザ自身で指定できます。
 </blockquote> 
 <p><strong>InfoQ: .NET Frameworkはサポートされていますか？</strong></p> 
 <blockquote>
  現時点では，PHPとJavaアプリケーションのフルサポートを提供しています。ClosureやGroovy，Scala，Jruby，JythonなどJVMベース言語も含んでいます。
  <br type="_moz" /> 
 </blockquote> 
 <p><strong>InfoQ: サイトあたりの費用はどの程度なのでしょう？</strong></p> 
 <blockquote>
  Jelasticでは，時間課金と自動スケーリング (垂直スケーリング - オンザフライでのメモリと処理能力の追加 - も含みます) を採用しています。したがって実際に使用しているものだけに支払えばよく，必要のないもののために余分に支払う必要はありません。費用はわずか２セント/時間からとなっています。実際のアプリケーションで必要な費用を知るのは簡単です - まず無料トライアルに申し込んでください。そこでアプリケーションを実行すると，&quot;仮想料金&quot; というものが表示されます。これは支払う必要のないものですが，正確な費用です。推測する必要はまったくありません。
  <br type="_moz" /> 
 </blockquote> 
 <p><strong>InfoQ: WordPressのような，PHPベースのブログアプリをインストールすることは可能でしょうか？</strong></p> 
 <blockquote>
  JelasticはPHPまたはJavaベースであれば，どのアプリケーションでもホストあるいはクラウドにスケールできます。さらにWordpressやJoomla，Drupal，Magnolia，Liferayなど人気のアプリケーションについては，いくつかのホスティングパートナからワンクリックデプロイのサービスが提供されています。
 </blockquote> 
 <p><strong>InfoQ: 1日20万ビジターを処理することは可能でしょうか？</strong></p> 
 <blockquote>
  Jelasticは数十万のユーザ，１日数百万のWeb要求を処理可能な 
  <a target="_blank" href="http://jelastic.com/customers">ホスティングアプリケーション</a> です。
  <br type="_moz" /> 
 </blockquote> 
 <p><strong>InfoQ: Internet Explorerなど，主要なブラウザはすべてサポートされているのでしょうか？</strong></p> 
 <blockquote>
  アプリケーションの開発者がサポート対象として選択したブラウザならば，どれでもサポートすることができます。
 </blockquote> 
 <p><strong>InfoQ: Jelasticにはダウンタイムを通知するアプリはあるのでしょうか？</strong></p> 
 <blockquote>
  基本的なモニタリング機能は組み込みで用意しています。外部の監視ソリューションの組み込みも可能です。
 </blockquote> 
 <p><strong>InfoQ: Jelastic内にPOP3メールボックスを作成することはできますか？</strong></p> 
 <blockquote>
  Jelasticはアプリケーションホスティングであって，メールボックスをホストするサービスではありません。ただしアプリケーションにメール送信機能が必要ならば，メールサーバ (Sendmailなど) を追加することも，あるいは外部のメールボックス (Google Appsなど) を使用することもできます。
 </blockquote> 
 <p><strong>InfoQ: JelasticとWindows Azureに共通点はありますか？</strong></p> 
 <blockquote>
  Platform-as-a-Serviceである，という点ですね。ただしAzureは，非Microsofシステムもいくつかサポートしてはいますが，基本的なターゲットはASP.NETアプリケーションです。さらに提供しているのはMicrosoftのみです。JelasticはJavaとPHPアプリケーションのためのPlatform-as-a-Serviceで，米国やブラジル，イギリス，ドイツ，スウェーデン，フィンランド，ロシア，日本など世界中のホスティングプロバイダによって提供されています。
  <br type="_moz" /> 
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
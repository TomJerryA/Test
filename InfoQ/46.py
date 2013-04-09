<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>AWSクラウド、Node.jsアプリケーションサービスを提供</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/aws-node-elastic-beanstalk;jsessionid=D414B1040FCE3048F923B5CFF6360C37"><em>原文(投稿日：2013/04/09)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>AWS（Amazon Web Services）チームは<a target="_blank" href="http://aws.amazon.com/elasticbeanstalk/">Elastic Beanstalkサービス</a>にNode.jsのサポートを追加し、業界最高レベルのプラットフォームサポートを実現した。AWS Elastic Beanstalkを使うことで、開発者はNode.jsだけでなく、Java、PHP、.NET、Ruby、Pythonで書かれたアプリケーションのパッケージング、デプロイ、管理が可能になる。AWSは競合ひしめくNode.jsフレンドリーなクラウドに参入したが、ほかのAWSサービスとの統合によって差異化をはかろうとしている。</p> 
 <p>AWS Elastic Beanstalkへの<a target="_blank" href="http://www.allthingsdistributed.com/2013/03/beanstalk-a-la-node.html">Node.jsサポート追加に関するブログ記事</a>において、AWS CTOであるWerner Vogels氏は、この人気が高まっているプラットフォームを追加する理由をこう述べた。</p> 
 <blockquote> 
  <p>かなりの時間をかけて、AWS開発者、ゲームやモバイル業界で仕事をしている人たちと話をしました。その大部分が、WebアプリケーションにはNode.jsが適している思っていました。Node.jsの非同期でイベント駆動なプログラミングモデルのおかげで、開発者は大量の並列コネクションを低遅延で処理できます。こうした開発者は通常、データ検索のためのWebサービスや動的なモバイルインターフェイスを作るのに、EC2インスタンスをデータベースサービスの1つと組み合わせて使っています。</p> 
 </blockquote> 
 <p>AWSチームのJeff Barr氏は、Elastic BeanstalkのNode.jsサポートで<a target="_blank" href="http://aws.typepad.com/aws/2013/03/aws-elastic-beanstalk-for-nodejs.html">お気に入りの機能をいくつか紹介した</a>。</p> 
 <ul> 
  <ul> 
   <li>Node.jsアプリへのリバースプロキシとして、<a target="_blank" href="http://nginx.org/">Nginx</a>か<a target="_blank" href="http://httpd.apache.org/">Apache</a>を選べること。クライアントが直接接続する必要のあるアプリケーションの場合、プロキシを使わないことも可能だ。</li> 
   <li>アプリケーション要求に基づいたHTTPおよびTCPロードバランシング設定ができること。WebSocketを使うアプリケーションの場合、TCPロードバランシングが適切だろう。</li> 
   <li>アプリケーションが必要とするNode.jsの特定バージョンを指定できること、またNode.jsアプリケーションを起動するのに使うコマンドを指定することでNode.jsスタックを設定できること。<a target="_blank" href="https://npmjs.org/">npm</a>を使って依存関係を管理することもできる。</li> 
   <li>NginxやApacheを使ったgzip圧縮や静的ファイルを設定することで、パフォーマンス改善を支援すること。gzip圧縮を使うことで、クライアントへの応答のサイズを削減し、より高速な転送速度を可能にする。静的ファイルを使うことで、Node.jsアプリケーションのデータ処理時間を奪うことなく、NginxやApacheによって静的アセット（画像やCSSなど）を高速に提供できる。</li> 
   <li>リレーショナルデータストアへのデータ格納および取得のための<a target="_blank" href="http://aws.amazon.com/rds/">Amazon RDS</a>とシームレスに統合できること。</li> 
   <li>EC2インスタンスのカスタマイズおよびElastic Beanstalk設定ファイルを使ったアプリのAWSリソースへの接続（設定ファイルについて、詳しくは<a target="_blank" href="http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs_custom_container.html">AWS Elastic Beanstalk Developer Guide</a>を参照）ができること。</li> 
   <li>追加ネットワーク制御のための<a target="_blank" href="http://aws.amazon.com/vpc/">Amazon Virtual Private Cloud</a>内でNode.jsアプリケーションが実行できること。</li> 
  </ul> 
 </ul> 
 <p>ここに挙げたもの以外にも、Elastic Beanstalkは<a target="_blank" href="http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs.sdlc.html">Gitの統合</a>、<a target="_blank" href="http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs_express_elasticache.html">高可用性のためのクラスタリング</a>、<a target="_blank" href="http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_nodejs_custom_container.html">環境固有変数</a>の利用もサポートしている。AWSがNode.jsに進出したのは、Node.js開発者向けに<a target="_blank" href="http://aws.amazon.com/about-aws/whats-new/2012/12/04/introducing-the-aws-sdk-for-node-js/">SDKをローンチ</a>した2012年12月にさかのぼる。このSDKは、Amazon DynamoDB、Amazon Simple Storage Service (S3)、Amazon Relational Database Service (RDS)、Amazon Simple Queue Service (SQS)、Amazon Elastic Compute Cloud (EC2)など、利用可能なAWSサービスのほとんどにアクセスすることができる。</p> 
 <p>AWSはNode.jsアプリケーションサービスを提供している多数のクラウドの仲間入りをした。Google App Engineを除いて、主要なPaaSベンダーのほとんど（<a target="_blank" href="https://devcenter.heroku.com/articles/nodejs">Heroku</a>、<a target="_blank" href="http://www.windowsazure.com/en-us/develop/nodejs/">Windows Azure</a>, <a target="_blank" href="https://www.openshift.com/paas">Open Shift</a>、<a target="_blank" href="https://www.engineyard.com/products/cloud/features">Engine Yard</a>、<a target="_blank" href="http://docs.cloudfoundry.com/frameworks/nodejs/nodejs.html">Cloud Foundry</a>プロバイダの多数）がNode.jsをサポートしている。これらのプロバイダはみな、思想的指導者で<a target="_blank" href="https://www.nodejitsu.com/">熱心なNode.jsプラットフォームプロバイダであるNodejitsu</a>と競合している。では、こうしたベンダーはどのように差異化するのだろうか？ その1つの方法がツールだ。Werner Vogels氏は、いかにElastic BeanstalkがトッププラットフォームであるAWSの多数の開発ツールと密に統合されているか説明した。</p> 
 <blockquote> 
  <p>どんなAWSリージョン（GovCloudを除く）にあるアプリケーションもデプロイして管理できます。これにはたくさんのツールが利用でき、お好みで選べます。Javaアプリケーションを構築しているなら、AWS Toolkit for Eclipseが使えます。NETアプリケーションを構築しているなら、AWS Toolkit for Visual Studioが使えます。ターミナルが使いたければ、Gitと「eb」というコマンドラインツールが使えます。eXoCloud IDEのような、Elastic Beanstalkとの統合環境を提供しているパートナーもいます。</p> 
 </blockquote> 
 <p>exoCloudは現在<a target="_blank" href="https://codenvy.com/features">Codenvy</a>としてスピンオフし、開発者にNode.jsデプロイメント向けElastic Beanstalkがターゲットになるクラウドベースの開発環境を提供している。</p> 
 <p>Node.jsアプリケーションの構築およびデプロイのためのツールを開発者に提供することに加え、クラウドプロバイダは無償サービスとの統合や、アプリケーション管理の「難題」に対するソリューションを提供することにより、ほかとの差異化をはかっている。Elastic BeanstalkにおけるNode.js実行が魅力的なところは、AWSが提供する多数のアプリケーションサービスと簡単に統合できることだ。AWS環境で動くNode.jsアプリケーションは、データベース、ストレージ、計算、キューイング、キャッシングなどに低遅延でアクセスできる。Windows Azureのようなクラウドも同様に、<a target="_blank" href="http://www.windowsazure.com/en-us/develop/nodejs/">Node.jsアプリケーションをデプロイする開発者</a>に、 データベース、ストレージ、メッセージングなどさまざまなネイティブサービスにアクセスできるという価値を提案している。<a target="_blank" href="https://addons.heroku.com/">Heroku</a>や<a target="_blank" href="https://www.nodejitsu.com/paas/addons/">Nodejitsu</a>といったプロバイダには独自の無償サービスはないが、彼らのプラットフォームで動作するアプリケーションと統合可能なサービスのカタログを用意している。</p> 
 <p>差異化としての無償サービス提供に加えて、クラウドプロバイダはアプリケーションのデプロイメントと管理が簡単になると宣伝している。これは、Webベースのソースコード管理リポジトリのサポート（AWS、Windows Azure、Nodejitsuのようなクラウド）や、継続的デプロイメントサービス（NodejitsuのTravisCIサポートなど）を意味している。高品質なモニタリング・レスポンスシステムは、クラウド開発者および管理者のキャパシティ管理をシンプルにしてくれる。AWSには、クラウド利用をモニタリングし、アプリケーション環境を自動的にリサイズするプロダクトもある。<a target="_blank" href="http://www.allthingsdistributed.com/2013/03/beanstalk-a-la-node.html">Werner Vogels氏</a>はこうした管理機能によって、Elastic Beanstalkがアプリケーションのプロビジョニングにどのように役立つかを説明した。</p> 
 <blockquote> 
  <p>Elastic Beanstalkはプロビジョニング、モニタリング、Elastic Load Balancing、Auto Scaling、EC2などの多数の基本AWSリソースの設定を自動化します。また、アプリケーションのデプロイ、ログのローテーション、EC2インスタンスのカスタマイズも自動化できます。</p> 
 </blockquote> 
 <p>この分野は要注目だ。クラウドプロバイダは、自身のプラットフォームで動くアプリケーションの有用性を高めるネイティブあるいは統合サービスを提供しつつ、自身のプラットフォームのアプリケーション管理機能を強化している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
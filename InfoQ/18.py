<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>スマートクライアント・Dumbサーバを実現？AWSがWebブラウザのJavaScript向けSDKをリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/aws-sdk-javascript"><em>原文(投稿日：2013/11/07)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>ここ数年、開発者は何らかの力仕事をサーバサイドのコードに頼り続けていたものの、クライアントサイドのコードにより多くの仕事をするよう求めていた。AWSは、ブラウザからAWSのサービスへの安全なアクセスを行うJavaScript SDKのリリースによって、そのモデルを刷新している。これにより、いくつかのケースでは、サーバサイドのコードを<em>まったく</em>必要としなくなっているのである。</p> 
  <p><a href="http://aws.typepad.com/aws_japan/2013/11/developer-preview-aws-sdk-for-javascript.html" target="_blank">開発者プレビュー版をアナウンスしているブログ記事</a>の中で、AWSチームはSDKがサポートしている4つのAWSサービスについての概要を述べた。</p> 
  <blockquote> 
   <p>開発者は下記のAWSサービスを直接呼び出すことが可能です。</p> 
   <ul> 
    <li><a href="http://aws.amazon.com/jp/s3/">Amazon S3</a>：任意の規模でオブジェクトの格納と取得を行う</li> 
    <li><a href="http://aws.amazon.com/jp/sqs/">Amazon SQS</a>：読み出しと書き込みをメッセージキューに対して行う</li> 
    <li><a href="http://aws.amazon.com/jp/sns/">Amazon SNS</a>：モバイル端末およびその他の分散サービスに対する、通知の生成と処理を行う</li> 
    <li><a href="http://aws.amazon.com/jp/dynamodb/">Amazon DynamoDB</a>：任意のアクセス速度で、あらゆる量のデータを格納・取得する</li> 
   </ul> 
   <p>SDKは、上述の各サービスが提供している全機能へのアクセスをサポートしています。開発者はS3のバケットの生成とデータ追加、メッセージキューの管理、生成、追加、そしてDynamoDBのテーブルへの問い合わせなどなど、その他さまざまなことができます！</p> 
  </blockquote> 
  <p>一部のアプリケーションにおいては、この機能はWebサーバの必要性を完全に排除することができるだろう。Amazon S3は静的なWebアプリケーションのホスティングをサポートしており、Webサイトをバケットにアップロードし、Webに公開することを可能にしている。静的なアプリケーションは<a href="http://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html" target="_blank">S3</a>や<a href="https://www.dropbox.com/help/201/ja" target="_blank">Dropbox</a>といったサービスや、<a href="http://nginx.org/ja/" target="_blank">nginx</a>のようなハイパフォーマンスのHTTPサーバを通じて簡単に拡張することができる。</p> 
  <p>ソフトウェア業界の草分け的存在であるDave Winer氏は、<a href="http://scripting.com/2013/11/01/amazonBreaksThroughOnStaticJavascriptApps" target="_blank">このリリースについて楽観的</a>であり、我々が『真の技術的ブレークスルー』の最前線にいると考えている。Webサービスをコールし、リクエストをさばくためのスケールを要するプロキシサーバを構築する代わりに、静的なアプリケーションの開発者は、必要な規模を提供してくれるWebサービスプロバイダだけに頼ることが可能である。Dropboxはこのモデルを2012年に採用しており、そこにWiner氏はこれからの未来を見出した。</p> 
  <blockquote> 
   <p>そして1年以上前、<a href="https://tech.dropbox.com/2012/08/some-love-for-javascript-applications-2/">Dropboxは驚くべきことを行いました</a>。</p> 
   <p>基本的に彼らは中間サーバを構築する必要をなくすために、プロキシサーバの機能をdropbox.comに吸収しました。それにより、ある日突然、Dropboxに接続するアプリのためにサーバソフトウェアのコードを書く必要はなくなります。スケーリング問題はフッと消えてしまいます。資金調達、もしくはユーザを広告主に売る必要も。</p> 
   <p>スケーリングは引き続き行われなければなりません。しかし、それはDropboxによって行われます。彼らはそれを広告主にユーザーを売ることによってでなく、むしろ彼らのサービスを利用するユーザに請求することによって行うのです。完璧ですね。このような経済は、まさしく正しいと感じます。</p> 
  </blockquote> 
  <p>Winer氏は、競合他社もこのモデルに追随することを強く勧めていたため、このAWS SDKの発表を知り、喜んだ。</p> 
  <blockquote> 
   <p>Dropboxが行ったようなことを実施するよう強く勧めるために、私は競合他社のあらゆる人と話してきました。そのうちたった数社でも実現すれば、―私は説得しました―普及率はすぐにクリティカルマスに達し、その後いくつかの本当に面白いことが起こるでしょう。あらゆる種類のアプリケーションに適用可能です。悲しいかな、それはどこも実現しませんでした。―AmazonがWebブラウザの<a href="http://aws.typepad.com/aws_japan/2013/11/developer-preview-aws-sdk-for-javascript.html">JavaScript向けAWS SDK</a>を発表した、昨日までは。理論的には、Dropboxと同様に、これは彼ら自身のためのWebサービスと言えるでしょう。彼らの主張としては、開発者が今までプロキシを必要としていたような何がしかのことを行うために、直接彼らのサーバをコールすることができるというものです。</p> 
  </blockquote> 
  <p>公開されたすべてのWebサービスが認証の仕組みを持つとは限らないが、AWSは確実にその仕組みを持っている。AWSは、単純なクライアントサイドアプリケーションにおける<a href="http://aws.typepad.com/aws_japan/2013/11/developer-preview-aws-sdk-for-javascript.html" target="_blank">認証の課題に、どのように取り組んだ</a>のだろうか？</p> 
  <blockquote> 
   <p>過去にAWSのSDKとAPIを使ったことがあれば、各リクエストにAWS credentilasによる署名が必要ということはご存知かと思います。誰にでも見られ、使われる可能性があるHTMLやJavaScriptに、あなたのcredentilasを含めたくないはずです。その代わり、あなたのアプリケーションのユーザを認証するために、<a href="http://aws.typepad.com/aws_japan/2013/05/aws-iam-now-supports-amazon-facebook-and-google-identity-federation.html">WebのID連携</a>を使用しなくてはいけません。WebのID連携をアプリケーションに組み込むことにより、一時的なセキュリティ証明書のセットを発行するにあたって、公開認証プロバイダ（<a href="https://www.facebook.com/about/login/">Facebook</a>、<a href="https://developers.google.com/+/">Google</a>もしくは<a href="http://login.amazon.com/">Login with Amazonサービス</a>）を使用することができます。</p> 
  </blockquote> 
  <p>AWSのIdentity and Access Management（IAM）サービスは、<a href="http://docs.aws.amazon.com/STS/latest/UsingSTS/CreatingWIF.html" target="_blank">定義済みのロールを引き継いで</a>ユーザを認証できるよう、個別の認証プロバイダでアプリケーションを登録できるようにするものである。彼らが最近リリースした<a href="https://web-identity-federation-playground.s3.amazonaws.com/index.html" target="_blank">Web Identity Federation Playground</a>では、認証のインタラクションのシミュレーション、および出力結果の確認が簡単にできるようになっている。このサービスは、AWSリソースに対する認証ポリシーを作成し、ユーザがアクセスするシナリオをテストしたい開発者を支援するものとなるだろう。</p> 
  <p>AWSの典型的なやり方にならって、<a href="https://aws.amazon.com/jp/sdkforbrowser/" target="_blank">SDKを学ぶ専用のWebサイト</a>や、基本的な<a href="http://aws.amazon.com/jp/developers/getting-started/browser/" target="_blank">ハウツーもののウォークスルー</a>、そして<a href="https://forums.aws.amazon.com/forum.jspa?forumID=148#" target="_blank">サポートフォーラム</a>がすでに用意されている。最初にサポートされたサービスはあくまでAWSファミリーの一部に過ぎないが、ストレージやメッセージングのような性能を必要とするアプリケーション開発者を対象としている。今後、さらなるサービス―ElastiCache、Simple Email Service、もしくはEC2も―のサポートがSDKに追加されることを期待するのは、理不尽なことではない。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
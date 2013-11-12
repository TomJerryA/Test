<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Phusion Passengerアプリサーバ、Node.jsをサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/phusion-nodejs"><em>原文(投稿日：2013/11/05)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>もともとRubyをターゲットにしていた人気のあるWebアプリケーションサーバ、Phusion PassengerがNode.jsアプリをサポートした。この機能は今年初めに、Passengerのエンタープライズ版で取り入れられたが、フリー版の4.0.21リリースでオープンソース化された。</p> 
  <p>Passengerは、ApacheやNginxといったWebサーバと組み合わせて、Webアプリケーションの提供、モニタリング、スケーリングのための完全なソリューションになることを目的としている。<a href="http://www.phusion.nl/">オランダを拠点とするPhusion</a>によると、Passengerで<a href="http://nodejs.org/">Node.js</a>アプリを動かすことには、次のようなメリットがあるという。</p> 
  <ul> 
   <li>マルチテナント性 – 最小構成で複数のアプリを動かすことができる</li> 
   <li>監視 – 自動的にNode.jsプロセスを開始し、クラッシュ時に再開させることができる</li> 
   <li>スケーリング – 処理すべきリクエスト数に応じて、プロセスを増減させることができる</li> 
   <li>統計情報 – プロセスの動作状態を知るのに役立つツールを提供する</li> 
  </ul> 
  <p>Passengerの開発者たちは、Apache/Nginxと組み合わせることで、静的ファイル配信の高速化、大量のアクセス攻撃や遅いクライアントに対する防御といったメリットも得られると<a href="https://github.com/phusion/passenger/wiki/Node.js">述べている</a>。</p> 
  <p>この発表はPhusionが自ら課した、Passengerを「究極の多言語アプリサーバ」にするという目標に向けた一歩だ。昨年、Passengerの<a href="http://blog.phusion.nl/2012/10/24/phusion-passenger-4-0-beta-1-is-here/">Pythonサポートがベータになった</a>が完成したようだ。Node.jsサポートの発表に続いて、PhusionはNodeベースのアプリフレームワークである<a href="http://www.meteor.com/">Meteor</a>のサポートも<a href="http://blog.phusion.nl/2013/11/01/will-meteor-kill-rails-i-dont-know-but-phusion-passenger-open-sources-meteor-support/">明らかにした</a>。</p> 
  <p>Passenger自体はC++で書かれており、Rubyやその他の言語と密に結合してはいない。バージョン4のリリースでは、いくつかのアーキテクチャ上の変更がなされた。Passengerの内部I/OハンドラはNode.jsとよく似たイベント駆動になり、エンタープライズ版はマルチプロセスおよびマルチスレッドのハイブリッド実行をサポートする。これにより、WebSocket上のライブストリーミングといった機能を可能にしつつ、リソースを最大限に活用することができる。</p> 
  <p>Rubyアプリに関して、Passengerはたとえば、リクエスト間までガベージコレクションを遅延させることができる&quot;out of band&quot;実行のような機能や、サブスクリプションベースのアプリモニタリングおよび分析サービスである<a href="https://www.unionstationapp.com/">PhusionのUnion Station製品</a>とのインテグレーションも提供する。</p> 
  <p>人気のあるRubyアプリサーバのうち、ThinやUnicornのようなイベント駆動のサーバアーキテクチャよりもスレッド化を好むという点において、PumaはPassengerとよく似ている。Phusionチームは最近、<a href="https://github.com/phusion/passenger/wiki/Puma-vs-Phusion-Passenger">PassengerとPumaの比較</a>を公表し、Pumaの開発者であるEvan Phoenix氏が<a href="https://news.ycombinator.com/item?id=5991407">HackerNewsでこれに反応した</a>。</p> 
  <p>InfoQでは、Passengerの最近のアップデートについて、PhusionのCTO、Hongli Lai氏から話を聞いた。</p> 
  <p><b>PassengerはRubyユーザにout-of-band実行のような、言語ランタイムに密接に関係した独自機能を提供していますね。Node.jsやPythonユーザにも同様のメリットはありますか？</b></p> 
  <blockquote>
    ほとんどの機能は、Node.jsとPythonを含むサポートしている言語すべてで利用できます。当初より、私たちはRubyへの依存関係を最小限にしてきました。最初のリリースから数ヶ月ですでにPythonをサポートしていたのですが、積極的な売り込みをしていなかっただけです。次のリリースでは
   <a href="http://www.meteor.com/">Meteor</a>のサポートを計画しています。 
   <p>Node.jsとPythonで利用できない機能がわずかにありますが、これらはその言語では意味がないか、必要な言語固有のサポートコードがまだ書かれていないためです。NodeとPythonのガベージコレクタは通常、Rubyのような長いGCポーズに苦しむことはありません。そのため、Node.jsとPythonユーザにはout-of-band work機能は必要ないと思います。</p> 
  </blockquote> 
  <p><b>現時点で、Node.jsのサポートはどれくらい安定していますか？</b></p> 
  <blockquote>
   安定していると思います。私たちのテストアプリケーションはすべてパスしており、テスターのアプリケーションもすべてうまく動いています。既知の問題はありません。
  </blockquote> 
  <p><b>もともとPassengerの目標は、RubyのデプロイメントをPHPと同じくらい簡単にすること、適切なディレクトリにアプリを置くだけにすることでしたよね。Passengerはその約束を達成できたと思いますか？</b></p> 
  <blockquote>
   アプリのデプロイメントには、OSや言語ランタイムのプロビジョニングからライブラリ依存関係の管理やアプリケーションプロセスの監視まで、あらゆることが関係しています。PHPのデプロイが簡単な理由の1つは、mod_phpモジュールを通して、Webサーバが自動的にPHPアプリケーション実行の面倒を見てくれるためです。
   <br /> Passengerを最初に開発した当時、Rubyアプリケーションの実行、監視、管理は大変な苦痛でした。複数のアプリケーションサーバプロセスを実行し、ローカルソケットをリッスンし、このソケット集合にプロキシが向かうようWebサーバをセットアップし、プロセスがクラッシュしたときに再開するようプロセス監視ツールをセットアップする必要がありました。Passengerで、私たちはmod_phpに似た仕組みを開発することで、この部分を解決しました。ですから、バージョン1.0の時点で、適切なディレクトリに置くだけでRubyアプリを実行するという目標はすでに達成しています。
   <br /> 
   <br /> それでもPHPの方がデプロイするのが簡単だと思われている理由は、多くの人気のあるPHPアプリケーションがアプリ実行以上のことを自動的に世話してくれるためです。たとえば、
   <a href="http://wordpress.org/">Wordpress</a>には依存関係がなく、ユーザが設定ファイルを編集する必要もなく、きれいなGUIを通してデータベースのクレデンシャルを求めます。でも自分でPHPアプリを書く場合には、RubyやNode、Pythonアプリで経験するのと同じ問題が起こります。
  </blockquote> 
  <p><b>実際のところ、Passengerがすぐに使えるホスティング会社はありますか？</b></p> 
  <blockquote>
   Passengerがすぐに使える知名度の高いホスティング会社には、
   <a href="http://aws.amazon.com/elasticbeanstalk/">Amazon Elastic Beanstalk</a>や
   <a href="https://www.openshift.com/"> Red Hat OpenShift</a>があります。
   <a href="http://heroku.com/">Heroku</a>のような多くのプロバイダはアプリサーバの選択にとらわれていませんが、ユーザは簡単にPassengerを使うことができます。
   <a href="http://www.brightbox.com">BrightBox</a>や
   <a href="https://www.speedyrails.com/">SpeedyRails</a>など、デフォルトでPassengerを使っている小さなホスティング会社もたくさんあります。
  </blockquote> 
  <p><b>Rubyアプリサーバには、強い競合がいくつかありますね（Thin、Unicorn、Puma）。この時点で、Passengerはどんな位置にいますか？</b></p> 
  <blockquote>
   他のRubyアプリサーバは、Passengerよりもスコープが限定されています。ユーザはプロセスを開始し、ソケットをリッスンするようセットアップし、リバースプロキシルールを設定したりする必要があります。システム全体を細かくコントロールしたいエキスパートにとって、これは必ずしも悪いアプローチではありませんが、私たちの哲学とは違います。私たちの好みは、安定して柔軟性がありながら、インストール、利用、管理がシンプルなソフトウェアです。
   <br /> 
   <br /> そうは言っても、私たちは他からたくさんのことを学んでいます。たとえば、Passengerの&quot;smart spawning&quot;機能はUnicornよりも先でしたが、Passengerのout-of-band work機能は独自に改善しているものの、Unicornをベースにしています。それぞれのサーバには強みと弱みがあるのです。
  </blockquote> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
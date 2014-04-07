<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Meteor 0.7.1がリリース，開発者アカウントなど多数を改良</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/meteor-071"><em>原文(投稿日：2014/03/28)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Matt DeBergalis氏が<a href="http://www.meteor.com">Meteor</a>バージョン0.7.1をリリースした。<a href="http://docs.mongodb.org/manual/reference/glossary/#term-oplog">oplog</a>と<a href="https://github.com/meteor/meteor/tree/master/packages/minimongo">minimongo</a>の改善，CSSプリプロセス，Meteor開発者アカウントなどを備える。</p> 
  <p>バージョン0.7.1ではminimongoのサポートが追加された。<a href="https://www.meteor.com/blog">Meteorブログ</a>での氏の説明によれば，これは&quot;MongoDBクエリ言語の更なる秘所&quot;とでも表現すべきものだ。また，ドキュメントに配列のある場合の挙動や$nin, $ne, $notのサポート改良など，Mongoの動作と一致する部分もさらに増えている。</p> 
  <p>minimongo(Meteroのクライアント用Mongoエミュレータ)の改善の他にも，次のようなCSS処理やソースマップの改善が行われている。</p> 
  <ul> 
   <li>CSSスタイルシートプロセッサにソースマップのサポートが追加された。 LESSによるスタイルシートのコンパイルに使用される。</li> 
   <li>CSSミニフィケーションが@import文を正しく扱えるように改善された。</li> 
   <li>不正な@ディレクティブのためのCSSファイルのLint機能。</li> 
   <li>インポートしたLESSファイルの推奨サフィックスが.lessimportから.import.lessに変更された。スタイルをインポートするための.import.stylが追加された。.lessimportも引き続き利用可能だが，非推奨となっている。</li> 
  </ul> 
  <p>OplogはMeteor 0.7.0から利用できるようになった機能だが，DeBergails氏によると，0.7.1リリースでは&quot;oplogドライバのサポートするMongoDBのクエリセットが拡張されて，製品版アプリで一般的に必要なクエリの大部分がサポートされるように&quot;なった。</p> 
  <p>バージョン0.7.1では，MongoDBのリアルタイムなデータベース更新を可能にするように，oplog tailingの実装が改良されている。MongoDBからの不要なデータフェッチを回避する最適化機能と同時に，&quot;$whereと$nearを覗く全操作のサポート&quot;も追加された。</p> 
  <p>Meteor 0.7.1では開発者アカウント(Developer Accounts)がローンチされた。デプロイしたアプリの管理や，アプリのデプロイ時にアプリ毎の旧パスワードの置き換えを行う，開発者用の新しいログインシステムだ。</p> 
  <p>アプリのデプロイ時，開発者はEメールアドレスの入力を要求されるようになった。Meteor開発者アカウントのメリットはさまざまだ，とDeBergalis氏は述べている。コマンドラインからのログインとログアウトを可能にすることで，&quot;Unix的な優しい感覚でMeteorのwhoamiを入力可能にすると同時に，他のMeteor開発者にアプリのデプロイやデータベース，ログへのアクセス許可を与える認証動作を実行&quot;できる。スイート全体のオプションを確認するには，コマンドラインからMeteorのヘルプを入力してみるとよいだろう。</p> 
  <p>Meteorコミュニティでアプリケーションを開発する開発者たちに対しては，Meteor開発者アカウントでサインイン可能であることが通知される。accounts-githubあるいはaccounts-facebookパッケージでGitHubやFacebookのアカウントにサインインできるのと同じような方法だ。</p> 
  <p>バージョン0.7.1では，依存性に関する定義も多数更新されている。例えばnode: 0.10.25 (0.10.12から更新)については，0.7.0にあった特定のNodeバージョンに対するワークアラウンドが削除された結果，0.10.25以降がサポート対象となったものだ。その他の更新としてはcoffeescript: 1,7,1 (1.6.3から)，websocket-driver: 0.3.2 (0.3.1から)，jquery-waypoints: 2.0.4 (1.1.7から)などがある。jquery-waypointsに関しては，後方互換性のない変更になる。</p> 
  <p><a href="https://news.ycombinator.com/item?id=7293860">Hacker News</a>でのDeBergails氏の0.7.1リリース発表へのコメントで展開された，単純なRailsアプリに対するリアルタイム機能の追加に関する議論の中では，user igiana氏が &quot;Meteor.jsはとてもクールだが，製品レベルに達していない&quot;と<a href="https://news.ycombinator.com/item?id=7294214">評している</a>。</p> 
  <p>それに対して氏は，&quot;そんなことはありません - - Meteorはすでに実用的に運用されているし，複数のサーバで稼働しています&quot; と<a href="https://news.ycombinator.com/item?id=7294251">反論している</a>。</p> 
  <p>0.7.1のリリース直後に0.7.1.2がリリースされた。コミュニティからの反応に対応して，コンピュータ名を設定した際にMac OSX上でクラッシュが発生するバグを修正したものだ。同時に非oplogコレクション上でTailable Cursorを使用した場合にアサーションが発生するという，MongoDBに起因するバグも回避されている。</p> 
  <p>本体から独立したアップデートとして，Meteorの新しいUIエンジンである&quot;blaze&quot;のrc-0が発表された。これに伴ってバージョン0.8では，Sparkが完全に排除される予定だ。</p> 
  <p>Googleの<a href="https://groups.google.com/forum/#!forum/meteor-talk">meteor talk</a>グループではユーザのGadi Cohen氏が，次のように<a href="https://groups.google.com/d/msg/meteor-talk/fFPWxgNVFE4/xrokbh9YCw4J">コメントしている</a>。&quot;まさにこれですよ！今回のリリースは，0.7.1での改善とともにMeteorが成熟したことの確かな証拠であり，Meteorトレインの早期採用というリスクを負う意思のあるスタートアップにとっては，究極的に快適かつ刺激的です。&quot;</p> 
  <p>Meteor 0.7.1リリースの発表 -- そしてMeteor開発者アカウントの発表 -- には，Twitterでのフォロワーを含む広範なJavaScriptコミュニティから，極めて肯定的な反応が寄せられている。</p> 
  <p><a href="http://www.meteorpodcast.com/">The Meteor Podcast</a>のホストのひとりであるRy Walker氏は，今回のアップデートへの感想を聞かれて，&quot;0.7.xアップデートもすばらしいですが，私は0.8や1.0を心待ちにしているのです -- その頃にはさらに多くの人たちが，@meteorjsに注目してくれているでしょう&quot;と答えている。</p> 
  <p>Meteorコミュニティ内で４月ないし５月と想定されている1.0リリースを控えて，Meteorコミュニティはますますの拡がりを見せている。Meteorは2012年，GitHubレポジトリとしては第３番目にスターが付けられたオープンソースプロジェクトであり，そのリリースは，<a href="http://www.infoq.com/news/2014/03/">Hacker Newsの歴史</a>上で最大のものだった。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
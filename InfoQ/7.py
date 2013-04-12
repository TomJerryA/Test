<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>BlossomがDartに移行</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/blossom-dart-switch;jsessionid=FDE796277A073BA4D30C4BB12C9E551B"><em>原文(投稿日：2013/04/08)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Thomas Schranz氏は自社製品の <a target="_blank" href="http://blossom.io">Blossom</a> を，<a target="_blank" href="http://www.dartlang.org">Dart</a> に移植すると <a target="_blank" href="http://www.ramen.io/post/46936028144/we-are-switching-to-dart-why">ブログ記事</a> に発表した。Blossom は開発チームのための製品で，Webベースのカンバン方式ボードである。DartはGoogleの開発した，JavaScriptの代替として利用可能な新しいWebプログラミング言語とプラットフォームだ。</p> 
 <p>今回の決定について氏は，JavaScriptエコシステムのフラグメンテーションに対して同社がこれまで長く抱いていた不満の結果だ，と <a target="_blank" href="http://www.ramen.io/post/46936028144/we-are-switching-to-dart-why">書いている</a>。</p> 
 <blockquote> 
  <p><a target="_blank" href="https://www.blossom.io">Blossom</a> ではJavaScriptを積極的に利用しました。JavaScriptはいろいろな面で素晴らしい言語です。ただし，その暗黒面を回避する手段を知っているならば，ですが。というのは，JavaScriptのエコシステムには，多くの面で重要なものが欠けていると思うからなのです。コア部分に関しては特にです。</p> 
  <p>何か事を始めようするとき，スタート地点に立つまでに乗り越えなければならない障害が多すぎます。この点が非常に不満なのです。エコシステムの新参者の目には，これがどう映っているのかは分かりません。学習曲線の上昇率としては比較的高い反面，疑問に感じる部分もたくさんあるのではないのでしょうか。</p> 
 </blockquote> 
 <p>結果として同社は，アプリケーションのフロントエンドを段階的にDartへ移行することを決定した。それまでのフロントエンドは <a target="_blank" href="http://coffeescript.org">CoffeeScript</a>, <a target="_blank" href="http://backbonejs.org">Backbone.js</a>, <a target="_blank" href="http://underscorejs.org">Underscore.js</a>, <a target="_blank" href="http://jquery.com">jQuery</a> を採用して，これらを <a target="_blank" href="http://brunch.io">Brunch</a> で組み立てる，という構成だった。</p> 
 <p>InfoQではSchranz氏に，今回の変更について詳しく聞くことにした。</p> 
 <p><b>Dartはまだ若い言語です。なぜ今，このような移行をしようと決意したのでしょう？</b></p> 
 <blockquote> 
  <p>Dartは確かに，他の言語と比べれば新しい言語です。しかしツーリングや標準ライブラリ，パッケージ管理システムなどが充実しているので，JavaScriptのエコシステムよりも使いやすいものに仕上がっています。</p> 
  <p>JavaScriptの世界にはフラグメンテーションが多すぎます。コンポーネントに関しては特にそうです。パッケージの管理，モジュール操作，非同期コードや依存性，コレクションの反復処理にさえ，競合する方法が山のように作られています。その結果が，ライブラリ同士の相性の悪さになって現れているのです。独自のエコシステムに引き込もうとするものがあり，それを無視しようと「車輪の再発明」を試みるものがある，といった具合です。私はJavaScriptコミュニティが，RubyやPython，Dartなどの言語のコミュニティに比べて，<a target="_blank" href="http://en.wikipedia.org/wiki/Not_invented_here">NIHシンドローム</a> に冒されている度合いが強いのではないか，と思っています。</p> 
  <p>そのことが不要な複雑さを生み出しているのです。初心者を困惑させるだけではありません。何年もJavaScriptを書いてきた人たちさえも混乱させているのです。Dartに移行するというのは，表面的にはリスクを伴った行動に思えるかも知れません。しかし私には，JavaScriptに固執することの方がよほどリスクが多いように思えてなりません。</p> 
 </blockquote> 
 <p><b>Dartのどのような部分がBlossomに向いているのでしょうか？</b></p> 
 <blockquote>
  フロントエンドのコードベースを開発するに当たって，私たちはより生産性の高い方法をずっと探していました。Dartはその点，非常に優れた基盤を提供してくれます。Dart VMのおかげでセーブ・リロードの開発サイクルが非常に短縮されますし，パワフルなコードアナライザも提供されています。このため，Dartエディタでの作業は快適です。自動補完やリファクタリング，デバッグなどの機能が，JavaScriptでは実現できていないレベルでサポートされています。さらにパッケージマネージャや選択的な型付け，一貫性のある標準ライブラリなどのおかげで，コードベースを論理的に検討することも容易です。Dartは単なるプログラミング言語ではなく，さまざまな補助機構を装備しているのです。それを理解することが大切です。結合された開発エクスペリエンスがあるという点が，Dartのすばらしさです。
 </blockquote> 
 <p><b>ですがDartはまだ，開発のアルファ段階です。</b><b>APIもまだ確定ではありません。それが問題になることはないのでしょうか？</b></p> 
 <blockquote>
  言語のセマンティクスやシンタクスはすでに，かなり安定していると思っています。とは言っても，Dartチームは1.0に向けて作業していますから，その過程でAPIレベルでも数多くの改善が実施されています。ただし幸運なことにDartには，先程述べたような充実したツールサポートがあります。非推奨とマークされたメソッドはエディタが教えてくれますし，必要ならば 
  <a target="_blank" href="http://www.youtube.com/watch?v=P7htQQQmpGM">コードベースを自動的にアップデートしてくれるクリーンアップツール</a> も提供されています。もっとも，ブログやメーリングリストをフォローさえしていれば，手作業で更新を行うのも大した手間ではありません。
 </blockquote> 
 <p><b>今は切り替えプロセスの真っ只中で，アプリケーションをひとつひとつ移行しているところだと思いますが，</b><b>JavaScriptからDartコードへの対応，あるいはその逆で，どのようなことを経験しましたか？</b></p> 
 <blockquote>
  <a target="_blank" href="http://www.dartlang.org/articles/js-dart-interop/">js相互運用パッケージ</a> というものが用意されています。これを使えば，JavaScriptオブジェクトの生成や関数のコール，さらにはDart関数をJavaScriptから呼び出すことも可能です。これだけで相互運用性については，かなりの部分がカバーされます。ただしBlossomに関しては，相互運用ライブラリはさほど必要ではありませんでした。 既存のBackbone.jsコードベースの独立性がもともと高く，ウィジェットからウィジェットに置き換える作業も比較的簡単だったからです。アプリケーションの一部については，Dartで置き換えるために 
  <a target="_blank" href="http://pub.dartlang.org/packages/route">Justin Fagnani氏のルーティングパッケージ</a> も使用しています。今のところ，移行は予想したよりも簡単です。
 </blockquote> 
 <p><b>これまでDartプラットフォームで開発作業を続けてきて，JavaScriptの場合と比べてどうでしたか？</b></p> 
 <blockquote>
  とても快適ですよ。一貫性のある開発エクスペリエンスのおかげで，エコシステムの基本的なビルディングブロックに無駄な作業を強いられることもなく，自分たちの製品開発に集中することができています。本当に信じられないくらいです。JavaScriptでコードを書いていた頃は，
  <tt>undefined</tt> をチェックする処理があちらこちらに散らばっていました。まともな言語ならば例外をスローするような場合でも，JavaScriptでは動作を続けようとする傾向があるからです。こんなに解放感を味わえたのは，何年も前，PHPからRubyとRailsフレームワークに切り替えた時以来です。当時はその作業も，リスキーで非常識だと言われたものです。
 </blockquote> 
 <p><b>これまでにDartに移植されたコードは，おおよそどの位ですか？</b></p> 
 <blockquote>
  現時点では５％程度です。新しい機能をDartで実装していますし，既存部分の移植も継続的に行っています。
 </blockquote> 
 <p><b>同じような移植を行っている製品アプリケーションで，何か知っているものはありますか？</b></p> 
 <blockquote>
  JavaScriptからDartに移行しているアプリケーションは，これ以外には知りません。ですが今後，もっと同じような発表があったとしても，驚きはしないと思います。Dartコミュニティは拡大していますし，1.0マイルストーンを待ちきれない人たちもたくさんいます。Dartをサポートするサービスもいくつか始まりました。例えば 
  <a target="_blank" href="http://drone.io">drone.io</a> という継続的インテグレーションサービスは，たくさんのDartのオープンソースパッケージが，テストのために使用しています。
 </blockquote> 
 <p><b>現時点で，Dartへの移行を他の企業にも奨めますか？</b></p> 
 <blockquote>
  移行するには少し早いかも知れませんが，Dartに注目して，その言語やツール，特にWeb UIに関していろいろ試してみることは，間違いなく奨められます。次の週末にでもぜひ試してみてください。
 </blockquote> 
 <p><b>Dartの将来性についてはどうでしょう，広く普及すると思いますか？</b></p> 
 <blockquote>
  Dartの将来には期待できると思います。Web開発のおもしろさを思い出させてくれます。プラットフォームに関係する人たちも最高で，コミュニティとパッケージがすでに立ち上がってきています。Webのアプリケーションを開発するのは楽しいですよ。
 </blockquote> 
 <p>Dartが <a target="_blank" href="http://blog.chromium.org/2011/10/dart-language-for-structured.html">最初に発表された</a> 1年半前には，その言語やアプローチに対して <a target="_blank" href="http://www.quirksmode.org/blog/archives/2011/10/dart_or_why_jav.html">批判的な</a> 声が <a target="_blank" href="http://www.sitepoint.com/google-dart-fail/">非常に多かった</a>。しかしそれ以降，Dartプラットフォームは着実に進歩している。JetBrainsのWebStormやIntelliJなど，サードパーティのIDEにも <a target="_blank" href="http://plugins.jetbrains.com/plugin/?id=6351">Dartのサポートが追加されている</a>。サーバサイドDartアプリケーションを <a target="_blank" href="http://www.heroku.com">Heroku</a> にデプロイすることも可能になった。</p> 
 <p>Blossomは一般公開されている製品アプリケーションとして，初めてDartに移植されたものだ。これが諺で言う「最初に跳ぶ羊」になり，他が追随することになるのかどうか。それは時が経てば分かるだろう。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
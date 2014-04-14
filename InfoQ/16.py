<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Ratchetが真のフレームワークに，新たなホスト先も</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/04/ratchet-2-real-framework-new-hom"><em>原文(投稿日：2014/04/07)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>モバイルアプリのプロトタイピングツール<a href="http://goratchet.com/">Ratchet</a>が拡張されて，完全なアプリケーションフレームワークになった。今回リリースされたバージョン2.0.2は，<a href="http://sass-lang.com/">SASS</a> CSSプリプロセッサを使用するように(バージョン1から)完全に書き直されている。オーバーホールに合わせて，既存のBase Ratchetテーマに加え，iOSとAndroidの２つのスタイルがサポートされた。&quot;Ratcheticons&quot;という新しいアイコンフォント，さまざまなテーマを示すための<a href="http://goratchet.com/examples/">3つのサンプルアプリケーション</a>も新たに提供される。ドキュメントも新リリースに合わせてオーバーホールされた。さらにはプロジェクトそのものも移動して，<a href="https://github.com/twbs">GitHubのBootstrapフレームワーク</a>の一部になっている。</p> 
  <p>Ratchetはもともと，TwitterのiOS用ネイティブアプリケーション用のHTML/CSSプロトタイプのセットとしてスタートした。それらプロトタイプが開発プロセスにおいて非常に重要であることに気付いた開発チームは，モバイル用プロトタイプキットとしてオープンソース化することを決定した。するとすぐに，Ratchetが単なるモバイルプロトタイプ構築に留まらず，本格的なモバイルアプリケーションの構築に適していることが明らかになったのだ。</p> 
  <p>当初のRatchetはプレーンなCSSで記述されていたが，バージョン2.0.2では<a href="http://sass-lang.com/">SASS</a>プリプロセッサ言語を使用するように変更されている。開発者のひとりである<a href="http://www.twitter.com/connors">Connor Sears</a>氏はこの書き直しについて，&quot;プリプロセッサの柔軟性&quot;を求めた結果だと述べている。またSASSを選択した理由については，単にもっとも慣れていたからだ，と説明している。なおBootstrapプロジェクト自体(現在はRatchetもその一部である)では，CSSに<a href="http://lesscss.org/">LESS</a>プリプロセッサを使用している。</p> 
  <p>Ratchetはもともと，CSSを微調整するためのスタイルをひとつしか持っていなかった。これが３つになり，複数のフォームファクタをサポートできるようになった。オリジナルのBaseスタイルは引き続き存在するが，iOSとAndroidの各スタイルが追加され，それぞれのオペレーティングシステムへの適応性が向上している。これは基本的にはスタイルのみに関係するものだが，Popoverなど一部のコンポーネントは，プラットフォームによって挙動に大きな違いがある。</p> 
  <p><img alt="" src="http://www.infoq.com/resource/news/2014/04/ratchet-2-real-framework-new-hom/en/resources/ratchet-themes.jpg" _href="img://ratchet-themes.jpg" _p="true" /></p> 
  <p>Ratchetは，プラットフォームやブラウザの観点からCSSを使って，具体的に何かを成し遂げようとするものではない。目標とするのはシンプルさを維持すること，理解と実装をより容易にすることだ。</p> 
  <p>新しいRatcheticonsアイコンフォントには，4５の一般的なアプリケーションアイコンが含まれている。これらはHTMLの<a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements">仮想エレメント(Pseudo-element)</a>を使って表示する。例えば歯車のアイコンは，単純な<small><b>span</b></small>とCSSクラスを使って表示できる。</p> 
  <pre>
&lt;span class=&quot;icon icon-gear&quot;&gt;&lt;/span&gt;
</pre> 
  <p>歯車アイコンのクラスには，<small><b>:before</b></small>仮想エレメントで表示されるフォント文字を指定するUnicodeが含まれている。</p> 
  <pre>
.icon-code:before {     content: '＼e812'; }
</pre> 
  <p>改訂版のRatchetのドキュメントでは，３つの本格的なアプリケーション例が公開されている。これらの例を使って，開発者のモバイルデバイス上でRatchetをテストすることができると同時に，新たなアプリケーション開発時の出発点としての利用も可能だ。Ratchetには今のところ，<a href="http://goratchet.com/examples/app-movies/">Movie Finder</a>(Baseテーマ)，<a href="http://goratchet.com/examples/app-ios-mail/">iOS Mail</a>(iOSテーマ)，<a href="http://goratchet.com/examples/app-android-notes/">Android Notes App</a>(Androidテーマ)というサンプルプログラムがある。</p> 
  <p>さらにRatchetは，BootstrapのGitHubレポジトリに移動された。 Sears氏はこの移動について，&quot;Ratchetはかねてから，Bootstrapの’弟分’というべき存在でした。ですからBootstrap orgへの移行はごく自然なものだと思います。&quot;と説明している。またRatchetをBootstrap orgに移動はしたが，&quot;統合&quot;される計画はないことも強調する。&quot;私たちは今後も，(RatchetとBootstrapという)２つのCSSアーキテクチャを同等に扱っていくつもりです。基本としてはBootstrapに慣れた人たちに，RatchetのCSSの使用に慣れて頂きたいですね。&quot;</p> 
  <p>Ratchetの人気はGithubでも急上昇していて，7,900以上のスターを集めている。 これに対して，Bootstrap自体のスター数は66,000以上だ。プログラムは<a href="http://goratchet.com/">Ratchetの公式サイト</a>，あるいは<a href="https://github.com/twbs/ratchet">twbs/Githubディレクトリ</a>からダウンロードできる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
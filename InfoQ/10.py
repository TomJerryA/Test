<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Firefox OS向け開発を始めるための資料</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/firefox-os-dev-resources"><em>原文(投稿日：2014/02/06)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Mozillaが開発するFirefox OSは“<a href="http://groups.google.com/group/mozilla.dev.platform/browse_thread/thread/7668a9d46a43e482?pli=1">オープンなウェブのための完璧でスタンドアロンなオペレーティングシステムを構築するという目的</a>”を追求しており、HTML、CSS、JavaScriptを使ってアプリケーションをインストールして実行できるようにしようとしている。LinuxとMozillaのGeckoをベースにしており、<a href="http://www.knowyourmobile.com/products/16409/mozillas-boot-2-gecko-and-why-it-could-change-world">100％完全にオープンなスタック</a>で作られている。</p> 
  <h2><strong>Firefox OSへの貢献</strong></h2> 
  <p>Firefox OSは完全にオープンソースであり、<a href="https://www.cms.infoq.com/mag4media/scripts/FCKeditor/editor/git%20clone%20git://github.com/mozilla-b2g/B2G.git">GitHubで複製</a>できる。Mozillaの開発者ポータルに行けば、エミュレータ上や<a href="https://developer.mozilla.org/en-US/docs/Mozilla/Firefox_OS/Dual_boot_of_B2G_and_Android_on_SGS2">デュアルブートできるように構成されたAndroidハンドセット</a>のような<a href="https://developer.mozilla.org/en-US/Firefox_OS/Installing_on_a_mobile_device">モバイルでバイス</a>で<a href="https://developer.mozilla.org/en-US/Firefox_OS/Building_and_installing_Firefox_OS?redirectlocale=en-US&amp;redirectslug=Firefox_OS/Building_and_installing_Firefox_OS">ビルドとインストールの詳細な方法が解説されている</a>。</p> 
  <p>Firefox OSの中核の技術は<a href="https://developer.mozilla.org/en-US/Firefox_OS/Platform/Architecture">3つの主要なレイヤ</a>でできている。</p> 
  <ul> 
   <li><a href="https://developer.mozilla.org/en-US/docs/Mozilla/Firefox_OS/Gaia">Gaia</a>。Firefox OSのユーザインターフェイス。Gaiaにはロック/ホームスクリーン、電話ダイヤル、コンタクトアプリケーション、従来のメール、カレンダー、電卓などの従来のアプリが含まれている。Gaiaは完全にHTML、CSS、JavaScriptで書かれている。</li> 
   <li><a href="https://developer.mozilla.org/en-US/docs/Gecko">Gecko</a>はOSのアプリケーションランタイムであり、HTML、CSS、JavaScriptで書かれている。Geckoにはネットワークスタック、グラフィックスタック、レイアウトエンジン、JavaScriptの仮想マシンが含まれている。</li> 
   <li><a href="https://developer.mozilla.org/en-US/docs/Mozilla/Firefox_OS/Gonk">Gonk</a>はLinuxカーネルとユーザスペースハードウエア抽象レイヤ(HAL)で構成されており、OSの低レイヤ。Geckoはこの上で動作する。GonkはGeckoにインターフェイスを提供する。例えば、電話スタックやディスプレイフレームバッファへ直接アクセスできるインターフェイスを提供する。ほかのOSではGeckoからはアクセスできない。</li> 
  </ul> 
  <p>GonkとGeckoへ貢献するにはC++の知識が必要だ。Gaiaに貢献するにはJavaScriptとHTML/CSSの知識が必要だ。</p> 
  <p>Firefox OSへ貢献するための基礎的なリソースは<a href="https://bugzilla.mozilla.org/query.cgi">bugzilla</a>だ。bugzillaは Mozillaのデファクトのデータベースだ。bugzilla上のバグを選んで修正するのとは別に、Mozillaは新参者はプラットフォームに簡単に参入できるように<a href="http://www.joshmatthews.net/bugsahoy/">メンター付きバグ</a>を用意した。メンター付きバグには参入を助けてくれるメンターを取り上げたり、参入するための十分な情報を提供する。適切なメンター付きバグがないのなら、“<a href="https://bugzil.la/sw:[good%20first%20bug]">good first bug</a>”リストは便利なスタートポイントになるだろう。</p> 
  <p>バグを修正したら、<a href="https://developer.mozilla.org/en-US/docs/Developer_Guide/How_to_Submit_a_Patch">レビューを受けるためにパッチを提出</a>し、十分な権限のある人によって最終的にチェックインされる。</p> 
  <h2><strong>Firefox OS向けアプリの開発</strong></h2> 
  <p>OSのローレベルのコンポーネントに労力を費やしたくないなら、Firefox OSで動作するアプリを作ることのもいいだろう。Firefox OSアプリの基本的なツールは最新の<a href="http://www.mozilla.org/en-US/firefox/new/">Firefox</a>と<a href="https://getfirebug.com/">Firebug</a>と<a href="http://people.mozilla.com/%7Emyk/r2d2b2g/">Firefox OS Simulator Addon</a>だ。</p> 
  <p>さらに便利なリソースは、</p> 
  <ul> 
   <li><a href="https://hacks.mozilla.org/2013/01/introducing-the-firefox-os-boilerplate-app/">ボイラープレートアプリ</a>: アプリの構造と<a href="https://wiki.mozilla.org/WebAPI">WebAPI</a>を示すテンプレートアプリ。</li> 
   <li><a href="https://developer.mozilla.org/en/docs/IndexedDB">IndexedDB</a>: クライアント側のストレージ用API。構造化データを保持できる。<a href="https://developer.mozilla.org/en-US/docs/Web/Guide/API/DOM/Storage?redirectlocale=en-US&amp;redirectslug=Web/Guide/DOM/Storage">DOM Storage</a>はより小さいデータを保持するのに適している。</li> 
   <li><a href="https://developer.mozilla.org/en-US/Apps/Developing/Manifest?redirectlocale=en-US&amp;redirectslug=Web/Apps/Manifest#appcache_path">アプリマニュフェスト</a>: マニュフェストとはオープンウェブアプリを配信するための重要なコンポーネントだ。JSONファイルであり、アプリの名前と説明が記載されている。アプリのオリジン、アイコン、アプリに必要なパーミッションなども記載される。</li> 
   <li><a href="https://developer.mozilla.org/en-US/Firefox_OS/Using_the_App_Manager">アプリマネージャ</a>: ローカルのアプリ、デバイス、開発ツールボックス(インスペクタ、デバッガ)などを管理する。</li> 
   <li><a href="https://hacks.mozilla.org/2013/08/introducing-brick-minimal-markup-web-components-for-faster-app-development/">ブロックウェブコンポーネント</a>: コンポーネントを使ってHTML5を再利用をするための仕様。</li> 
   <li><a href="http://www.mozilla.org/en-US/styleguide/products/firefox-os/">Firefox OSスタイルガイド</a>: ユーマンインタラクションガイドライン。すべてのアピアランスとUIの振る舞いについて記述している。</li> 
  </ul> 
  <p>Mozilla RepのShafiul Azam氏も<a href="http://shafiul.github.io/slides/kickstart_fxos.html">Firefox OSアプリを開発するための基本的なステップを解説するプレゼンを提供している</a>。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
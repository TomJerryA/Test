<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>OracleがHTML5向けにNetBeansをアップデート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/02/netbeans73;jsessionid=B3516E6DC32298A7B37FA6A7E70064CC"><em>原文(投稿日：2013/02/26)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>NetBeansの最新リリースの7.3で、OracleはIDEをアップデートしたので、開発者はモバイルとウェブアプリケーション用の HTML5ベースのユーザーインターフェースをもっと容易に作成できるようになる。</p> 
 <p>新しいHTML5プロジェクトタイプによって、自動的に人気のある<a target="_blank" href="http://backbonejs.org">Backbone</a> と <a target="_blank" href="http://jquery.com">jQuery</a>のようなJavaScriptフレームワークが公開のCDNからダウンロードされ、取り込まれる。幾つかのサンプルHTML5 アプリケーションも New Projectウィザードから直接開くことができる。これらのあるものは、NetBeansに含まれており、他のものはGitHubから即座にダウンロードできる。</p> 
 <p>IDEには、またサーバー側のJavaベースのRESTサービスにアクセスできるJavaScriptクライアントコードを生成できるウィザードが含まれている。ウィザードがJSコードを生成するのに、 Backbone.jsライブラリと（オプションで）HTMLファイルを使っている。HTMLファイルは、生成されたコードがどのようにカスタマイズできるか、について指示を与えるスケルトンを含んでいる。もしRESTサービスがデータコレクション周りのインターフェースを持ち、テーブルソーターUIが選ばれたら、RESTデータは、 Tablesorter jQueryプラグインを使って、テーブルグリッドとしてレンダリングされる。</p> 
 <p>コーディング時には、エディタが HTML5, JavaScript, jQuery, CSS3(<a target="_blank" href="http://wiki.netbeans.org/html5">Project Easel</a>)用の補完機能を提供する。JavaScriptのエディタとデバッガは、 Oracleの Nashorn JavaScriptエンジンを使って完全に書き直された。Java 8におけるJavaのデフォルトのJavaScriptエンジンは、Rhinoに代わってこのNashornになる。このエディタは、共通のJavaScriptドキュメントオプションとして、<a target="_blank" href="https://wiki.appcelerator.org/display/tis/scriptdoc%2b(sdoc)%2b2.0%2bspecification">ScriptDoc</a>, <a target="_blank" href="http://code.google.com/p/ext-doc/">Ext-Doc</a>、<a target="_blank" href="http://code.google.com/p/jsdoc-toolkit/">JsDoc</a>をサポートする。</p> 
 <p>IDEの狙いの1つは、開発者がウェブインターフェースをデバッグするのを助けることである。IDEのHTMLプレビューは、内部のWebKitベースのブラウザによって提供されている。また Chromeブラウザ拡張は、WebKitリモートデバッグプロトコルを使うので、NetBeans内からウェブアプリケーションのデバッグができる。デバッガは、HTML5アプリケーションに含まれているローカルファイルとアプリケーションにリンクされている、しかしソースに含まれているではない、リモートのJavaScriptファイルの両方のデバッグをサポートしている。デバッガは4つのビューを提供する。</p> 
 <ul> 
  <li><strong>ブレークポイント</strong>:ラインブレークポイント（スクリプトが特定のコード行に達した時にトリガーされる）、DOMブレークポイント（特定のDOMノードに変更があった時にトリガーされる）、イベントブレークポイント（ページで特定のイベントが起きた時にトリガーされる）、XMLHttpRequestブレークポイント（ XMLHttpRequestを使って、ネットワーク通信が行われた時にトリガーされる）。</li> 
  <li><strong>コールスタック</strong>: JavaScriptプログラムの現在の実行スタックを表示する。コールスタックウィンドウには、3つのコンテキストアクションがある：&quot;Make Current&quot; （変数が評価されている現在のフレームを変更する）, &quot;Go to Source&quot; そして &quot;Copy Stack&quot;（スタックトレースをクリップボードにコピーする）。</li> 
  <li><strong>変数</strong>: 変数は、変数ウィンドウで検査できる現在のスコープ内で有効である。評価器も含まれており、任意の式を評価できる。</li> 
  <li><strong>ブラウザログ</strong>: ブラウザで発生したあらゆる例外、エラー、警告などを表示する。</li> 
 </ul> 
 <p>JavaScriptの単体テストも js-test-driver（これは Eclipse と IntelliJでもサポートされている）によってサポートされている。JavaScriptのユニットテストを走らせ、デバッグするのは、他の言語でのと同じである。</p> 
 <p>ウェブプログラミングの他には、NetBeans 7.3には、新規のスタンドアロンのJPQL (Java Persistence Query Language)エディタがあり、開発者はIDEから直接JPQLクエリをテストすることができる。最後に、新バージョンは、Raspberry Piを含む Linux ARMシステム上のJavaアプリケーションのプロファイリングをサポートしている。</p> 
 <p>NetBeansは、オープンソースのIDEで、 CDDL v1.0とGPLv2のもとで<a target="_blank" href="http://netbeans.org/cddl-gplv2.html">ライセンス</a>されている。Javaの他に Groovy（このバージョンにはGroovy 2.0 のサポートが追加された）、PHP, C, C++が追加されている。 Windows,OS X, Solaris 、Linuxプラットフォーム版が<a target="_blank" href="http://netbeans.org/community/releases/73/">ダウンロード</a>できる。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
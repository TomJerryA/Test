<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Angular.JS と ASP.NET を利用した Single Page アプリケーションの作成</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/04/asp_net-angular"><em>原文(投稿日：2014/04/04)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p class="MsoNormal">Build の水曜日セッションにて、David Catuhe 氏と Jon Galloway 氏が <a href="http://angularjs.org/">AngularJS</a> を ASP.NET アプリケーションで利用する方法をプレゼンテーションした。これにより、開発者はモダンな Single Page アプリケーションを高速に作成する方法を提供された。</p> 
  <p class="MsoNormal">Angular は Google によって作成され、現在はオープンソースプロジェクトとして扱われてサポートされている。名前の示す通り JavaScript ベースのライブラリであり、Model View Controller (MVC) 設計パターンにしたがっている。Catuhe 氏と Galloway 氏の説明する通り、Angular は DI（依存注入）を利用して ASP.NET アプリケーションを機能強化する。単一ファイルである <code>angular.min.js</code> は、機能を有効化するために一度だけ読み込む必要がある。(NuGet ユーザは最新版（β）か安定板を <a href="http://www.nuget.org/packages/angularjs/">取得</a> することができる）。</p> 
  <p class="MsoNormal">Angular の利用方法としては、全てに適用／全てに適用しないという二者択一のアプローチではないことを指摘しており、作成しているサイトに対し選択要素の機能のみを利用するといった方法も考えられる。 どのイベントでも Catuhe 氏と Galloway 氏は Scripts フォルダの下に “apps” を作成して体系化することを推奨している。</p> 
  <p class="MsoNormal">JavaScript の圧縮についての重要な警告：標準で利用される圧縮の場合、コード内の Angular における依存注入を破壊する恐れがある（Angular のチュートリアルドキュメントである <a href="http://docs.angularjs.org/tutorial/step_05">XHRs &amp; Dependency Injection</a> の“A Note on Minification”に記載されている）。</p> 
  <p class="MsoNormal">Angular を自身のサイト内で利用する場合、html タグ内に “ng-app” を追加する必要がある。</p> 
  <p><code> </code></p> 
  <p class="MsoNormal"><code>&lt;html ng-app … &gt;
    <o:p></o:p></code></p> 
  <p><code> </code></p> 
  <p>上記を記載することが Angular の実行準備となる。Angular は <code>$http</code> を利用し、jQuery の軽量バージョンのファイルをロードする。すでに jQuery を配置して利用している場合、Angular は一貫性を維持するために配置済みの jQuery を利用する。
   <o:p></o:p>
   <o:p>
    &nbsp;
   </o:p></p> 
  <p class="MsoNormal">Catuhe 氏と Galloway 氏はマジック：ザ・ギャザリング のカードのサンプルアプリケーションを利用し、Single Page アプリケーション（SPA）ベースでの表示／情報格納についてデモを実施した。UI 構築時に SPA はビューを利用するが、Angular 自身はそれらのビューで定義されたルーティングを利用する。</p> 
  <p class="MsoNormal">Angular で MVC Route を用いる際にディープリンクが衝突する場合があるので、彼らは Catch All Route の利用を提案している。
   <o:p></o:p></p> 
  <p>&nbsp;</p> 
  <blockquote>
   <code> <p class="MsoNormal">routes.MapRoute(<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; name: &quot;Catch all route for SPA&quot;,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; url: &quot;App/{*catchall}&quot;,<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; defaults: new{<br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; controller = &quot;Home&quot;, <br /> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; action = &quot;Index&quot;});
     <o:p></o:p></p> </code>
  </blockquote> 
  <p>&nbsp;</p> 
  <p class="MsoNormal">HTML表示における他のTIPSが存在する。ビューから生成されたHTMLの場合は複雑な処理は必要な一方で、単一のファイル（MyHTML.html）からなる HTML の場合は IIS Rewrite ルールを利用して URL を変更することだ。
   <o:p></o:p></p> 
  <p><code> </code></p> 
  <p class="MsoNormal"><code>/myHTML.html -&gt; /myHTML
    <o:p></o:p></code></p> 
  <code> </code> 
  <p>&nbsp;</p> 
  <p class="MsoNormal">彼らのデモアプリケーションの動作を閲覧したい場合、<a href="http://channel9.msdn.com/Events/Build/2014/3-644">Channel9 ページ</a> に情報提供を相談して欲しい。
   <o:p></o:p></p> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
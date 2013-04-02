<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Canvasベースのチャートライブラリ、Chart.js 0.1がリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/chartjs-v.0.1-released;jsessionid=37ADFF38DADB24A90C0812847B99E953"><em>原文(投稿日：2013/03/19)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>3月17日、<a target="_blank" href="http://www.nickdownie.com/">Nick Downie</a>氏がcanvasを使ったJavaScriptチャートライブラリ、<a target="_blank" href="http://www.chartjs.org/">Chart.js</a>をMITオープンソースライセンスで公開した。これはSVGベースのチャートライブラリに代わるものだ。</p> 
 <p>「理解しやすいシンプルなAPIによってWebデザイナーが求める美しさを実現でき、なおかつ開発者が複雑なWebアプリケーションに組み込むことができるような、軽量でポータブルですぐに使えるチャートライブラリを作りたかったんです」Downie氏は語る。</p> 
 <p>Chart.jsは、データとチャートをレンダリングするAPIにより、<a target="_blank" href="http://www.chartjs.org/docs/">6種類のチャート</a>を提供している。Downie氏は大学最後のプロジェクトとして、1ヶ月かけてライブラリを構築し、ドキュメントをまとめた。17日にオープンソースにして以来、「あまりの反応に圧倒されています。Hacker newsにリンクを投稿したのですが、1日後には何万ものアクセスがあり、Githubはイシューとコントリビューションでいっぱいです」とDownie氏は言う。</p> 
 <p>SVGのチャートライブラリのようにチャート要素ごとに複数のDOMノードをレンダリングするのではなく、Chart.jsは単一のcanvasノードを使っている。この単一ノードレンダリングのため、Chart.jsにはイベントリスナーのフックが1つしかない。その結果、「メモリ上のやり取りが必要な領域を記録し、現在のマウス位置をチェックする間に、それら領域をイテレートします。ユーザがマウスを動かすたびにこれを繰り返すのは負荷がかかります。canvas上にツールチップを直接描画すると、定期的にcanvasのクリア/再描画をすることになるのです」Downie氏は言う。「こうしたカスタマイズについて、全員のニーズを実現するシンプルなAPIを考え出すのはなかなか難しいことです。ツールチップを必要とする人もいれば、チャートに線を引きたかったり、データポイントをハイライトしたい人もいます。そうやっていくと、すぐに複雑になっていきます」 Downie氏は言う。彼はツールチップの追加を受け入れるだろうが、「サイトやアプリにシンプルで静的なグラフを入れたい開発者にとって、かなりの負荷を伴う複雑なソリューション（SVGによるチャート）」の代わりとして、Chart.jsをプロモートしたいと思っているようだ。</p> 
 <p>シンプルなAPIというのはcanvasを使ったアプローチの利点の1つだが、Chart.jsはcanvasが生成するラスターイメージに依存するため、ベクターベースのSVGチャートツールにあるようなスケーラビリティがない。これについてDownie氏は「レスポンシブレイアウトのためには、（canvas上の）CSS widthに基づいたパーセントを宣言してください。Hi-DPIディスプレイの場合、Chart.jsは自動的に正しいdevicePixelRatioにスケールし、CSSによる正しいデバイスピクセルサイズにスケールダウンします」と言っている。</p> 
 <p>canvasならではの機能は、<a target="_blank" href="https://developer.mozilla.org/en-US/docs/DOM/HTMLCanvasElement">toDataUrl</a>によって、base64画像をエクスポートできることだ。「将来のリリースでは、生成後のチャートに対するユーティリティ関数をいくつか追加するつもりです。これにより、ユーザは簡単にチャートのクリア、アップデート、エクスポートすることができます。基本的に、Chart.jsはこの関数のラッパーを提供することになります」Downie氏は言う。</p> 
 <p>彼はこの春卒業し、いくつかの機能をChart.jsに追加するとともに、卒業後はフルタイムの仕事に専念するつもりだ。「（Chart.jsは）Webデザインコミュニティの人たちにとって非常にエレガントで（願わくば）役に立つものを作るために、デザインと開発をミックスするよい口実になりました。」</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
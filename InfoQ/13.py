<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Dart2jsがDeltaBlueベンチマークで手書きJavaScriptコードのパフォーマンスを上回る</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/dart2js-outperforms-js;jsessionid=A1036B21393104415B9A9C21E8D353DC"><em>原文(投稿日：2013/04/10)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Googleが <a target="_blank" href="http://news.dartlang.org/2013/03/why-dart2js-produces-faster-javascript.html">Dart2jsコンパイラの新バージョン</a> をリリースした。生成されるJavaScriptコードのパフォーマンスは，オブジェクト指向言語で一般的に利用されている <a target="_blank" href="http://www.cs.washington.edu/research/constraints/deltablue/">DeltaBlueベンチマーク</a> において，手書きのJavaScroptを上回っている。手書きJavaScriptコード以上のパフォーマンスの実現がDart2jsプロジェクトの目標ではなかったが，メソッドのインライン化やプリコンパイルなどの最適化を実施した結果，いくつかのプログラムにおいてDartプログラムの方が，慣用的な記法のJavaScriptコードより速く動作するようになったのだ。<a target="_blank" href="http://www.dartlang.org/performance/">Dartサイトで公開されている</a> もうひとつのベンチマークであるRichardsベンチマークでも，両者の値は徐々に接近してきている。ただし現在はまだ，Dartの生成するJavaScriptのパフォーマンスが手書きのコードよりも 26%遅い。</p> 
 <p>以下のグラフからは，DeltaBlueベンチマークによるDartのパフォーマンスが徐々に向上している様子が見て取れる。<br /> <img alt="" src="http://www.infoq.com/resource/news/2013/04/dart2js-outperforms-js/ja/resources/dartperformance.png;jsessionid=A1036B21393104415B9A9C21E8D353DC" _href="img://dartperformance.png" _p="true" /><br /> グラフの紫色のラインは，Dart2jsの生成したJavaScriptコードをGoogleのv8 JavaScriptエンジンで動作させた場合を表している。黄色のラインはv8で実行した一般的なJavaScriptコード，一番上にある青色はDart <a target="_blank" href="http://en.wikipedia.org/wiki/Virtual_machine">VM</a> 上でDartコードをネイティブ実行した場合である。値が大きいほどパフォーマンスがよい。</p> 
 <p>Googleが大規模Webアプリケーション用に開発した新言語 <a target="_blank" href="http://dartlang.org">Dart</a> は，さまざまなコンテキストで動作可能である。</p> 
 <ol> 
  <li><em>ブラウザ組込のDart VM内</em>。Dartプロジェクトはまだバージョン1.0をリリースしていない。そのため現時点でDart VMを組み込んでいるブラウザは，Dart SDKに付属している <a target="_blank" href="http://www.dartlang.org/dartium/">Chromium &quot;Dartium&quot; ビルド</a> のみである。</li> 
  <li><em>サーバ上で動作するDart VM</em>。サーバサイド・アプリケーションのみ使用可能な <a target="_blank" href="http://api.dartlang.org/docs/releases/latest/dart_io.html">dart:io</a> ライブラリが，ファイルシステムへのアクセス，プロセス管理，サーバ構築 (HTTPサーバまたはwebsocketサーバ) を行うAPIを提供する。これによって<a target="_blank" href="http://nodejs.org">Node.js</a>に非常に近いユースケースでDartを使用可能になり，アプリケーションのフロントからエンドまでをDartで開発することができる。</li> 
  <li><em>アプリケーションへの組込。</em> Dart VMを任意の (C/C++) アプリケーションに組み込んで，Dartスクリプティングをサポートすることができる。</li> 
  <li><em>ブラウザ内でJavaScriptへコンパイルする。</em> 現時点でDartをサポートする製品版ブラウザはなく，Chrome以外のブラウザが将来的にDart VMを組み込むかどうかも明確ではない。そのようなブラウザ上でもDartコードを実行可能にするため，Dart2jsコンパイラでDartプログラムをJavaScriptに変換する。したがってDartが成功するためには，生成されたコードのパフォーマンスは非常に重要だ。</li> 
 </ol> 
 <p>新しいDart2jsコンパイラは，それ自身がDartで実装されている。<em>大域 <a target="_blank" href="http://en.wikipedia.org/wiki/Type_inference">型推論</a> (global type inferencing)</em> と呼ばれる技術を用いて，変数や引数が実行時に所持する型の情報をより多く収集することによって，従来よりもコンパクトで高速なJavaScriptコードの生成が可能になった。 興味深いことにDart2jsでは，Dartがサポートしている Optional Type Annotation を利用しない。その理由は，型制約の違反がエラーとして通知される <em>チェックモード</em> でDartを実行しない限り，アノテーションによる型指定は実行時には適用されないからだ。たとえば <tt>String name = 10;</tt> のように書いたとしても，困惑はするにせよ，文としては完全に有効なのだ。このことから，生成されたコードの正しさを保証するためにコンパイラでは，型アノテーションを無視するようにしている。</p> 
 <p>数多くの最適化処理が可能なのは，DartがJavaScriptほど自由な言語ではないためだ。たとえばJavaScriptでは，オブジェクトにメソッドを動的に追加することや，メソッドの置き換え，動的なコードのダウンロード，<tt>eval</tt> や <tt>with</tt> 文の使用が可能である。これらがv8などのJavaScript VMでの最適化の実行範囲を狭くしている。Dartでは，これらの機能の多くがサポートされていないため，Dart2jsコンパイラの実行時に，どのコードが実行されるかを正確に把握できるのだ。使用されていないコードを取り除く，いわゆるデッドコード削除 (dead-code elimination) あるいはツリーシェイキング (tree shaking) も可能になる。さらにメソッドをインライン化できる場合もある。JavaScriptとは違い，Dartはオブジェクトへのモンキーパッチ (実行時のコード修正) をサポートしないからだ。</p> 
 <p>ベンチマーク結果は多少割り引いて受け取るべきものではあるが，Dart開発チームがパフォーマンスを着実に改善している様子が見られるのは興味深いことだ。Dartはまだ大規模な開発の途上にあるが，<a target="_blank" href="http://www.infoq.com/jp/news/2013/04/blossom-dart-switch;jsessionid=3206D02F6169350AE2C254CDB515A0BF;jsessionid=A1036B21393104415B9A9C21E8D353DC">適用例もいくつか見られるようになってきた</a>。Dart2jsの生成するコードのパフォーマンスとサイズは，現在DartコードをWebに展開しようと考えている人たちすべてにとって，重要な意味を持っている。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Math.js: 多機能JavaScript Mathライブラリ</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/mathjs"><em>原文(投稿日：2014/01/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>&nbsp;<a href="http://mathjs.org/">Math.js</a>はJavaScriptおよびNode.js向けのオープンソースMathライブラリで、数値、ビッグナンバー、複素数、単位、行列を扱うことができる。これは柔軟な式パーサも備えている。さらに詳しく知るため、InfoQはプロジェクトの創始者である<a href="http://josdejong.com/">Jos De Jong</a>氏にコンタクトした。</p> 
  <p align="justify">Jos氏はプロジェクトの背景について、次のように説明する。</p> 
  <blockquote> 
   <p align="justify">JavaScriptには、行列、複素数、統計などに使える優れたライブラリがすでにあります。でも、そこには先進的な数学処理をするための統合ソリューションが欠けていました。既存のライブラリの多くは<i>chained</i> APIを備えています。これは非常にわかりやすいのですが、ライブラリ自身が知っているデータ型しか受け付けません。そのため、統合が問題になります。行列のライブラリは複素数を扱えないといった具合に、組み合わせることができないのです。Math.jsのAPIは、JavaScriptのMathオブジェクトのAPIと組み込みオペレータ、各種入力を受け付けるスタティック関数、と同じです。Math.jsでは、先進的なデータ型、関数、定数をサポートするようAPIを拡張しています。</p> 
   <p align="justify">Math.jsがアプリケーション開発における数学を、もっと簡単に、もっと楽しいものにすること、そして、開発者の世界とアカデミックな世界とのギャップを橋渡しをするのに役立つことを期待しています。</p> 
  </blockquote> 
  <p align="justify">Math.jsには3種類の使い方がある。</p> 
  <ol> 
   <li> 
    <div>
     スタティック関数と定数を使う（JavaScriptのMathオブジェクトのように） 
     <pre>
math.add(2, 3); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 5 
math.sqrt(-4); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // 2i 
math.pow([[-1, 2], [3, 1]], 2); &nbsp;// [[7, 0], [0, 7]]</pre> 
    </div> </li> 
   <li> 
    <div align="justify">
     文字列式を評価する 
     <pre>
math.eval('1.2 * (2 +  4.5)'); //7.8
math.eval('5.08 cm to inch'); //2 inch </pre> 
    </div> </li> 
   <li> 
    <div align="justify">
     chainingオペレーションを使う
     <br /> 
     <pre>
math.select(3)
    .add(4)
    .multiply(2)
    .done();      //14</pre> 
    </div> </li> 
  </ol> 
  <p align="justify"><a href="http://mathjs.org/">Math.jsのWebサイト</a>や<a href="https://github.com/josdejong/mathjs/tree/master/examples/">そのドキュメント</a>にサンプルが載っている。</p> 
  <p align="justify">Jos氏はこの2か月以内に、最初の安定バージョンである1.0をリリースするつもりだ。</p> 
  <blockquote> 
   <p align="justify">残っているのは、リファレンスドキュメントを書くこと、ユニットテストによるコードカバレッジを100%にすること、あちこちにある荒削りなところを解消することです。</p> 
  </blockquote> 
  <p align="justify">1.0ではAPIが安定化され、その後は最適化にフォーカスが移ることになる。Jos氏は性能改善のために、型付き配列、並行処理、asm.jsなどを使う可能性を検討している。</p> 
  <p align="justify">なぜJos氏は、すでにNumPi/SciPiといったライブラリのあるPythonなどではなく、JavaScriptを選んだのだろうか。</p> 
  <blockquote> 
   <p align="justify">ここ最近、私たちはクラウドとWebアプリケーションへ大きく動いているのを目の当たりにしています。私もすっかり夢中になっています。ブラウザとJavaScriptエンジンはどんどん高速になり、この数年で、<a href="http://nodejs.org/">node.js</a>を使ってJavaScriptをサーバサイドで動かせるようになりました。これは多くの新たな可能性を広げ、その結果、JavaScriptエコシステムとその人気は<a href="http://resin.io/happy-18th-birthday-javascript/">爆発的に拡大</a>しました。JavaScriptは<i>これまでで</i>最もユビキタスな言語になっているように見えます。JavaScriptは完璧な言語から程遠いものですが、私はJavaScriptとそのコミュニティが大好きです。</p> 
  </blockquote> 
  <p align="justify">すでにmath.jsを使ったエンドユーザのプロジェクトがいくつもある。Jos氏のプロジェクト、<a href="http://mathnotepad.com/">mathnotepad</a>もmath.jsを使っていて、開発の初期段階にある。Math.jsは人気のある計算機プロジェクト、<a href="http://numerics.info/">numerics</a>でも使われている。</p> 
  <p align="justify">Math.jsを始めるには、まずは<a href="https://github.com/josdejong/mathjs/blob/master/docs/getting_started.md">ドキュメント</a>を読んでみよう。&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Facebook製UIライブラリ『React』の不変性をパワーアップさせる『Om』について</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/om-react"><em>原文(投稿日：2014/01/17)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>David Nolen氏が、Facebook製<a href="http://facebook.github.io/react/">React</a>のClojureScriptインタフェースである<a href="https://github.com/swannodette/om">Om</a>をリリースした。この組み合わせがどのようにしてパフォーマンスの大幅改善を実現できるのかについて、David氏は自身の<a href="http://swannodette.github.io/2013/12/17/the-future-of-javascript-mvcs/ ">Om紹介記事</a>で、現在の標準的なアプリケーションとされている<a href="http://todomvc.com/">TODOアプリケーション</a>を用いて説明している。この改善は2つの主な要因によるものである。</p> 
  <ol> 
   <li>アプリケーションの状態変数に不変なデータ構造を用いるということは、土台となっているReactライブラリの<a href="http://facebook.github.io/react/docs/component-specs.html#updating-shouldcomponentupdate ">shouldComponentUpdate</a>の実装のために、<a href="http://www.ecma-international.org/ecma-262/5.1/#sec-11.9.4">参照等価性</a>を利用できるという意味である。このことは、Reactの仮想DOMの差分チェック（ブラウザに描画させる必要がある変更を検知する処理）パフォーマンスを向上させる。David氏によると、結果的にアプリケーションのパフォーマンスは、標準的なデータ型を使用する場合に比べて2～3倍速くなるという。</li> 
   <li><a href="http://www.w3.org/TR/animation-timing/">requestAnimationFrame</a>はブラウザのビューを再描画するタイミングの決定を委譲するために用いる。その結果、ビューの表示効果処理を一括して実行することができるため、再描画の回数を削減することができる。パフォーマンスが30～40倍になったというDavid氏の<a href="https://twitter.com/swannodette/status/412033352699744256">ツイート</a> の背景には、この２つ目の要因が関係しているように思われる。この２つ目のベンチマークは終了時の状態が開始時と同じであるため、Omがあらゆる状態変化においても動作することが可能であるなら、新しいフレームをブラウザがリクエストする前に、Reactの仮想DOMはビューを実際には何も変更しなくても良いと判断するだろう。変更の必要がないという判断は、当然のことながら、状態変化のたびに再描画を要求するよりも大幅にパフォーマンスを改善する。</li> 
  </ol> 
  <p>とはいえ、David氏はハイパフォーマンスを実現することに彼自身の努力は必要ないということを強調したがっている。彼の<a href="http://swannodette.github.io/2013/12/17/the-future-of-javascript-mvcs/ ">記事</a>によると</p> 
  <blockquote>
   これらのベンチマークは、Omが世界で一番速いUIコンポーネントシステムであると証明することを目的にしたものではありません。これらのベンチマークは、次のような実装上の決定を避けることが重要である、ということを示すために設計されています―すなわち、グローバルな最適化を阻むような実装や、ユーザ自身が同じような問題のある設計をしてしまうことを防ぐことができないような、ガイダンス（正しい誘導）が少なすぎる実装などです。
  </blockquote> 
  <p>InfoQは、Omについてと、どの程度Clojurescriptの採用が進んでいるのかについてDavid氏と対談する機会を得た。</p> 
  <p><b>InfoQ: </b>これから追加する主要な機能がまだあるのでしょうか、それとも、今のライブラリが成熟するのを待っているのでしょうか？</p> 
  <blockquote> 
   <b>David氏: </b>OmはシンプルかつReact上のさらに関数型的なレイヤーです。公開しているAPIはまだ開発中ですが、大きな影響を与えるような機能追加は予定していません―Omはフレームワークではなく、ユーザインタフェースプログラミングに対する、より関数型的なアプローチの土台となることを意図しています。
  </blockquote> 
  <p><b>InfoQ: </b>Reactには古典的な設計方針をWebプログラミングに持ち込んでいるような感覚があり、例えば、Pete Hunt氏は彼の<a href="http://2013.jsconf.eu/speakers/pete-hunt-react-rethinking-best-practices.html ">アーキテクチャ概要</a>の中で凝集度と結合度を引き合いに出しています。このことは、JavaScriptが十分に成熟したため、今やそれらの基本コストは仮想マシンのパフォーマンスによって埋め合わせするに足りている、もしくはそれらのアイデアを前面に持ってくるようにユーザインタフェースプログラミングを取り巻く文化が変化していることを象徴しているのでしょうか？</p> 
  <blockquote> 
   <strong>David氏: </strong> 私が思うに、開発者はJavaScriptのみの開発やjQuery、ましてやBackbone、Angular、Emberなどといったより構造化されたソリューションを用いた開発の限界に気付きはじめています。結果として明らかに、ReactはDOM問題に対する新鮮なアプローチに思えます。私の記事に対する反響は、私が想像していたよりもはるかに大きいものであったため、このアイデアはブラウザ上で開発を行う開発者の琴線に触れるものだったと考えます。
  </blockquote> 
  <p><b>InfoQ: </b><a href="http://swannodette.github.io/mori/ ">Mori</a>を通じて最近のJSフレームワークを使うことによって、不変データ構造を採用したくなるような何らかの利点が生じるのでしょうか？もしくは、Reactの仮想DOMのような新しいアプローチが別のデータ構造の必要性―理想的な構造をもったデータ―を生み出していくのでしょうか？</p> 
  <blockquote> 
   <strong>David氏: </strong> Reactのアプローチは既にかなりの恩恵をもたらしていますが、不変的なデータ構造を活用した時に真の輝きを放ちます。それというのも、ReactのReconciliationプロセスは、プログラムが実行すべき処理を減らしてくれるからです。我々はOmの発表から、不変的なデータ構造に対する関心の高さを目の当たりにしました。それに加えて、Omユーザかその他開発者かに関わらず、不変的なデータ構造は強力なアンドゥ機能を簡単に実装するための入り口をも開きます。
  </blockquote> 
  <p><b>InfoQ: </b>ClojureScriptは確かにClojureコミュニティの<a href="http://cemerick.com/2013/11/18/results-of-the-2013-state-of-clojure-clojurescript-survey/ ">注目を集めています</a> が、JavaScriptから直接ClojureScriptに来る多くの人々のことを知っていますか？</p> 
  <blockquote>
   <strong>David氏: </strong>ClojureScriptは、Clojureコミュニティの需要を満たすことにしっかりと注力しています。しかしながら、Omのようなプロジェクトが示すように、我々のアプローチにはいくつかの面白い利点があり、幅広いWeb開発コミュニティへの関心の高まりがあると考えます。
  </blockquote> 
  <p>David氏が上記で述べたように、彼の発表はコミュニティからかなりの反響があった。何人かは、Omを実戦投入した感想を記事にした。</p> 
  <p>Fredrik Dyrkell氏は純粋なReactからClojureScript、そして最終的にはOmに書き換えたコードサンプルを<a href="http://www.lexicallyscoped.com/2013/12/25/slice-of-reactjs-and-cljs.html ">紹介</a> し、最後に『まとめると、総じてReactに、とりわけClojureScriptとともに使うことにとてもワクワクします』と締めくくっている。</p> 
  <p>Adam Solove氏は、ステートフルな地図生成ライブラリと連携する必要がある伝統的なブラウザUIをOmで開発する<a href="http://adamsolove.com/js/clojure/2014/01/06/om-experience-report.html">概要を公開</a>し、『私は次のことを学びました。Omは関数型言語でWebユーザインタフェースを構築する実用的な方法であり、そしてとても楽しいものです』と結論づけた。</p> 
  <p>Josh Lehman氏はOmによる<a href="http://facebook.github.io/react/docs/tutorial.html">Reactチュートリアル</a>を<a href="http://www.joshlehman.me/rewriting-the-react-tutorial-in-om/ ">書き</a>、『Omは今まで出会ったリッチなインタフェースを構築するライブラリの中で、最も有望なClojureScriptライブラリです』と述べている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
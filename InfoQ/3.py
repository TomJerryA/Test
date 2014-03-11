<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PrismaticがSchema 0.2にデータ型強制変換を追加</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/prismatic-schema-coercion"><em>原文(投稿日：2014/02/19)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://getprismatic.com/">Prismatic</a>では，同社の<a href="http://clojure.org/">Clojure</a>データ記述ライブラリである<a href="https://github.com/prismatic/schema">Schema</a>の<a href="http://blog.getprismatic.com/blog/2014/1/4/schema-020-back-with-clojurescript-data-coercion">0.2リリース</a>に，<a href="http://en.wikipedia.org/wiki/Type_conversion">データの強制型変換(coercion)</a>を追加した。これにより，不正な型のデータを単にリジェクトするのではなく，スキーマに適合させてインスタンスを変換するような設定が可能になる。</p> 
  <p>ClojureではMapのキーとして<a href="http://clojure.org/data_structures#Data%20Structures-Keywords">キーワード</a>が慣用的に使用される。そのため<a href="http://www.json.org/">JSON</a>オブジェクトの受信時には，変換を実施するために頻繁に使用されるボイラプレートコードが存在する。従来このような変換は，リクエストを検証する前に実行する必要があった。今回の変更により，キーをキーワードとして定義しておけば，<a href="https://github.com/prismatic/schema">Schema</a>がその処理を実行してくれるようになる。自分自身のニーズに合わせて，独自の変換処理を定義することももちろん可能だ。この追加機能などによってPrismaticでは，データ検証の所要時間が5分の1に短縮されたと説明している。</p> 
  <p><a href="http://blog.getprismatic.com/blog/2013/9/4/schema-for-clojurescript-data-shape-declaration-and-validation">9月の初回リリース時</a>にSchemaが目標として挙げたのは，&quot;より少ない手間で，Clojureの型システムのメリットをより多く享受する&quot;ことだった。リリースの時点では，同じくClojureに型システムを導入するライブラリである<a href="https://github.com/clojure/core.typed">core.typed</a>と競合する可能性が指摘されていた。この見方に対しては，core.typedの作者である<a href="https://twitter.com/ambrosebs">Ambrose Bonnaire-Sergeant</a>氏が反論した。両ライブラリは互いに補完し合うものだという氏の主張は，後に<a href="http://www.infoq.com/news/2013/10/core-typed">core.typedに関してInfoQがインタビュー</a>した時にも改めて述べられている。</p> 
  <div>
   InfoQではライブラリの開発リーダである
   <a href="http://getprismatic.com/profile/w01fe">Jason Wolfe</a>氏と，Schemaの今後について話す機会を得ることができた。
  </div> 
  <div>
   &nbsp;
  </div> 
  <p><b>InfoQ:</b> Shemaが最初にリリースされたとき，core.typedと組み合わせることで非常に強力なものになる可能性が示唆されました。それ以降，このアイデアに進展はあったのでしょうか？</p> 
  <blockquote>
   数年前にQiプログラムを初めて見て以来，Clojureの漸進的型付け(gradual types)には強い興味を持っていました。それを実現したという意味で，Ambroseは素晴らしい仕事をしたと思います。Schemaとcore.typedを組み合わせる方法はいくつかありますが，もっとも興味深いのは多分，core.typedでチェックしたコードとそうでないコードとのブリッジとして，Schemaを使う方法だろうと思います。 
   <div>
    &nbsp;
   </div> 
   <div>
    そうなのですが，残念なことにまだcore.typedを十分に調査する時間が取れていないので，今の時点でご報告できることはほとんどありません。
   </div> 
  </blockquote> 
  <p><strong>InfoQ:</strong> テストデータ生成への展開は意欲的なテーマだと思うのですが，<a href="https://github.com/reiddraper/simple-check">simple-check</a>を取り込んだり，<a href="https://github.com/clojure/test.generative">test.generative</a>を利用したりするのでしょうか。あるいは別のアプローチを考えていますか？</p> 
  <blockquote>
   選択肢を探している段階です。simple-checkについては素晴らしい評価をたくさん目にしていますから，何とか取り入れたいと思うのですが，今はまだ実装内容を理解して，その生成プロセスに追加の制約を組み込み方法を見つけようとしているところです。個別のデータを疑似ランダムに具体化するような，もっとシンプルなジェネレータも存在するでしょう。テストでは結構，そういったものを多く使用しています。
  </blockquote> 
  <p><strong>InfoQ:</strong> Schemaの定義からもっと価値を引き出すために，どのような考えをお持ちですか？</p> 
  <blockquote> 
   <p>強制型変換と変換は非常に強力ですから，今はまだその可能性をすべて引きだそうとしている段階です。同僚のDave GollandがClojure Westで&quot;fnhouse&quot;という，グラフとスキーマを結合してWeb APIを容易に構築可能にする新ライブラリについて話をする予定です。今回のリリースに続いて，fnhouseのAPIからObjective Cと ClojureScriptのモデルクラス，クライアントAPIライブラリを自動生成する&quot;coax&quot;をリリースする予定です。</p> 
   <p>その後もクレイジーなアイデアがたくさんありますが，まだお話できる段階ではありません。</p> 
  </blockquote> 
  <p><a href="https://github.com/prismatic/plumbing">Graph</a>は<a href="http://blog.getprismatic.com/blog/2013/2/1/graph-abstractions-for-structured-computation">2013年にリリースされた</a>PrismaticsのClosureライブラリで，構造化された計算を宣言型のスタイルで表現するものだ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
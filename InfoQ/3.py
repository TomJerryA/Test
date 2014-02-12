<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ビッグデータ: 言語は本当に重要か?</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/bigdata-languages"><em>原文(投稿日：2014/01/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>ビッグデータの分野では、数十億ものイベントの中で、たった1ミリセコンドの損失が重大な影響を与える。それにもかかわらず、Pythonのような遅いと考えられている言語が、この1年で非常に人気が出ている。ビッグデータコミュニティの最近の記事や議論では、データサイエンスとビッグデータのプログラミング言語の選択について、論争を始めている。</p> 
  <p><a href="http://www.adroll.com/">AdRoll</a>の主席エンジニアであるVille Tuulos氏によると、言語のパフォーマンスそのものは問題ではない。Ville氏の調査結果は、2013年9月にサンフランシスコで開催された<a href="http://tuulos.github.io/sf-python-meetup-sep-2013/#/">ミートアップ</a>で発表され、Pythonで構築されたAdRollのバックエンドスタックと、<a href="http://aws.amazon.com/redshift/">AmazonのRedshift</a>のような巨大なシステムよりも優れたパフォーマンスをどのように発揮できるかを示した。ここで重要なのは、AdRollは、自分たち特有のユースケースに基づき、システムを構築していることだ。そのため、その1つのユースケースのために最適化できる。Ville氏は次のように述べた。</p> 
  <blockquote>
   どの言語を使うかに関わらず、ハイレベルな言語を使い、一般的なソリューションよりも優れている、ドメイン特化言語のソリューションを実装できます。
  </blockquote> 
  <p>これは、言語がまったく関係ないという意味ではない。データサイエンスやビッグデータにはどの言語が最適かについて、最近、数多くの議論が行われている。何度も議論されているのは、PythonやRだ。<a href="http://inside-bigdata.com/2013/12/09/data-science-wars-python-vs-r/">データサイエンス戦争</a>について話す人もいる。LinkedInのトピックでは、<a href="http://www.linkedin.com/groups/R-vs-Python-35222.S.239919420">興味深い議論</a>が始められ、全般的な意見では、Rは学問的な言語であり、データサイエンティストにとっては、大量のパッケージとその多様性によって、Rがより優れたものになっている。</p> 
  <p>しかし、すべてを考慮すると、Pythonのほうがプログラマたちの心に訴えかけるものがあり、大量のデータを扱う場合について、<a href="http://www.dish.com/">Dish Network</a>のデータサイエンティスト、Tom Rampley氏は以下のように述べている。</p> 
  <blockquote>
   私は、様々なパッケージの統計的機能を利用するため、広範囲に渡ってRを利用します。また、小さなデータセットの操作にもRを使います。しかし、テキストのパースや大規模データセットの操作、自分のアルゴリズムをコーディングする場合は、
   <a href="http://www.numpy.org/">Numpy</a>、
   <a href="http://scipy.org/">Scipy</a>、
   <a href="http://pandas.pydata.org/">Pandas</a>のパッケージと組み合わせて、Pythonを使うほうがずっと良いと思います。
  </blockquote> 
  <p>ここ数か月は、Pythonが勝者になっているようだ。<a href="http://karissamck.com/blog/2013/10/30/big-data-is-big-because-it-doesnt-load-into-r/">Karissa McKelvey</a>氏は、2013年10月に「私のデータは大きく、Rではロードできない」というブログを書いているし、<a href="http://readwrite.com/2013/11/25/python-displacing-r-as-the-programming-language-for-data-science">Matt Asay</a>氏は、「Rはデータサイエンスの博士号を持つ人たちには人気があるが、データが主流になるにつれて、Pythonが優位になっている」と述べた。</p> 
  <p>複雑なアーキテクチャの中でどの言語を使うか決める時、その言語のパフォーマンスは重要な要素になる。そして、このことは、誇張されがちだ。本当に大切なのは、その言語をどう使うかであり、Linus Torvalds氏は次のように述べている。「悪いプログラマはコードに悩む。良いプログラマはデータ構造とその関係性に悩む。」</p> 
  <p><a href="http://www.cloudera.com/">Cloudera</a>の最近のオープンソースプロジェクトである<a href="https://github.com/cloudera/impala">Impala</a>を例に見てみよう。Impalaは、クエリを劇的に速く実行するために、<a href="http://hive.apache.org/">Hive</a>から置き換えるように提案されている。残りの<a href="http://hadoop.apache.org/">Hadoop</a>スタックはJavaで書かれているが、ImpalaはC++で書くことを選んだ。この変更の理由は、しばしばパフォーマンスのためだと言われている。しかし、パフォーマンスの向上は、単にJavaからC++への切り替えのためだけではない。Impalaは、<a href="http://en.wikipedia.org/wiki/MapReduce">MapReduce</a>を使わずに、データをメモリにキャッシュする。異なるデータ構造と制限を持った、完全に別のパラダイムを使うため、初めからパフォーマンスが良いのは明らかなのだ。JavaからC++に切り替えられたのは、さらに先を行くために素晴らしいことではあるが、パフォーマンス向上の大きな要因ではないだろう。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
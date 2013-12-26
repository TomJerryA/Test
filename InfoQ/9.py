<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>技術的負債を清算するときのアドバイス</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/repay-technical-debt"><em>原文(投稿日：2013/12/11)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Spotifyでコーチを務める<a href="http://blog.crisp.se/author/henrikkniberg">Henrik Knibert氏</a>は、最近書いた<a href="http://blog.crisp.se/2013/10/11/henrikkniberg/good-and-bad-technical-debt">記事</a>の中で、ある種の技術的負債を持つことが利点となり、システムの品質の指標となることを説明している。</p> 
  <p>氏は避けるべきであり、生産するべきなのは“古い負債”だという。正しい機能を導き出し、ソリューションを理解するには、実験的な取り組みと問いが必要であり、その後、“単一のエレガントな解決策”が見つかる。古い負債はすぐにでも清算するべきで、ソフトウエアを腐らせ、価値提供を累積的に遅くしてしまう。氏はこれを日常にたとえて次のように説明する。</p> 
  <blockquote> 
   <p>新しいことを始めようとしてパソコンを立ち上げたら、昨日使っていた多くのウィンドウやドキュメントがすでに開いていて、作業するのが遅くなってしまう、または、台所で夕飯を作ろうとしたら昨日の片付けが終わっていないままだった、というような状態です。</p> 
  </blockquote> 
  <p>Yahoo!のリサーチエンジニアであり、Israeli International Association of Software Architectsの創設者のひとりである<a href="http://labs.yahoo.com/author/makabee/">Hayim Makabee氏</a>は“<a href="http://effectivesoftwaredesign.com/2013/10/18/avoiding-technical-debt-how-to-accumulate-technical-savings/">Avoiding Technical Debt: How to Accumulate Technical Savings</a>”と題した記事を書いている。氏は、技術的貯蓄について説明し、適応可能な設計をすることで負債を事前に清算することができるという。リファクタリングに時間が割かれすぎているということ“Refactoring Distractor”という言葉を引き合いに出して説明し、<a href="http://effectivesoftwaredesign.com/category/adaptable-design/">Adaptable Design Upfront</a> (ADUF)のパラダイムを支持する。ADUFを通じて<a href="http://en.wikipedia.org/wiki/SOLID_(object-oriented_design)">SOLID</a>の原則によって初期に理解した高レベルの概念の周辺にコンポーネントベースの設計を構築できるのだ。これによって、しっかりした実装とコンポーネント間の相互通信の中で変更に対処できるようになる。ADUFは<a href="http://martinfowler.com/">Martin Fowler氏</a>の進化的設計に対する<a href="http://martinfowler.com/articles/designDead.html">考え</a>に似ている。Fowler氏は以前、“設計者はシンプルな設計方法、リファクタリングで設計をきれいに保つ方法、進化的スタイルの中でパターンを使う方法を学習する必要がある&quot;と<a href="http://martinfowler.com/articles/designDead.html">書いている</a>。</p> 
  <p>ADUFについて書くなかで、Hayim氏は実践的な実装方法を説明している。</p> 
  <blockquote> 
   <p>フレームワーク内の各コンポーネントの凝集度を高め、フレームワーク自体はコンポーネントの結合度が弱くなるように設計します。コンポーネントのインターフェースが抽象的でコンポーネント間の結合が弱ければ、フレームワーク内の各タイプのコンポーネントがある種のプラグインのようになります。</p> 
  </blockquote> 
  <p>“技術的負債”という言葉の生みの親である、Ward Cunningham氏は今年のはじめ、<a href="http://www.ontechnicaldebt.com/blog/ward-cunningham-capers-jones-a-discussion-on-technical-debt/">OnTechnicalDebt.com</a>の<a href="http://www.ontechnicaldebt.com/blog/ward-cunningham-capers-jones-a-discussion-on-technical-debt/">インタビュー</a>に答えている。技術的負債を事前に清算することについて、氏は“持っていないお金を使うリスクやファンクションポイント半分に満たないコードを出荷するリスク”を背負いたくない場合の選択肢になりうると指摘している。また、現在の継続的デリバリの世界には、受け入れられるレベルのバグと悪い設計がある、という。</p> 
  <blockquote> 
   <p>...動いているソフトウエアに対するアプローチはたくさんありますが、私ですら驚くのは、大規模なウェブサイトを運営しており、素早くログインを検知する人が、品質よりも弾力性を重視する傾向があることです。弾力性というのは、ミスがあってもそのまま進んでいく能力のことです。</p> 
  </blockquote> 
  <p>Henrik氏はソフトウエアは決して完璧にならないこと、負債のないコードを書くことで機会費用が発生してしまうことを説明する。</p> 
  <blockquote> 
   <p>理論的には、各機能実装が完了した後に技術的負債がゼロになっていることは素晴らしいことです。しかし、現実には、80/20ルールが存在します。技術的負債を低いレベルに抑えておくにはそれなりの努力が必要です。そして、技術的負債をすべて取り除こうとすれば、ありえないくらいの労力が必要です。</p> 
  </blockquote> 
  <p>氏は債務上限を導入し、プロセスの裂け目から染み出す負債に対処することを提案する。ほとんどの新しい負債はすぐに清算されるが、債務上限に達した場合は、すべてのリソースを使って負債解消に取り組むべきだ。</p> 
  <blockquote> 
   <p>債務上限は十分に高く設定するべきです。日常的に上限に達していては困りますから。そして、解消できないくらいつみあがってしまうことを避けられるくらい低く設定しておくことです。</p> 
  </blockquote> 
  <p>ADUFパターンは、負債ゼロの状態にはならないものの、事前の貯蓄をするための方法を提供してくれる。Henrik氏もWard氏も技術的負債を受け入れることは、意図的に妥協して実現可能な製品を現実的な時間内で提供することだということを思い起こさせてくれる。Hendrik氏は負債を抱え込めば抱え込むほど未来の開発とチームのモラルを停滞させると指摘する。技術的負債をモニタリングすることでリスクやプラットフォームの健全度をより深く理解できる。技術的負債のレベルを管理し、清算の計画を立てることは積極的に優先度をつけるべきタスクなのだ。</p> 
  <p>Henrik氏は次のように書く。</p> 
  <blockquote> 
   <p>きれいなコードベースは楽しいです(もしくは、めんどくさくありません)。モチベーションの高い開発者は優れた製品を素早く開発する傾向があります。そうなれば顧客も開発者も幸せです。</p> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
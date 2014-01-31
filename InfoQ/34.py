<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>JavaScriptのためのSOLID設計原則</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/solid-principles-javascript"><em>原文(投稿日：2014/01/22)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>多くの開発者がオブジェクト指向言語で仕事をしてきた。そして今、多くの開発者がJavaScriptで仕事をしているが、ほとんどの人はオブジェクト指向の原則をJavaScriptで使っていない。JavaScriptを中心に本も書いている開発者の<a href="http://lostechies.com/derickbailey/">Derick Bailey</a>氏が<a href="http://codemash.org/">CodeMash</a>での<a href="http://www.youtube.com/watch?v=TAVn7s-kO9o">プレゼンテーション</a>でこのように語った。オブジェクト指向プログラミングの場合、私たちは基礎や原則を仕事の基本として話すが、クラスベースの静的言語から型付けのゆるいクラスベースでない言語に移ると、同じ原則を適用するのは難しいと思ってしまいがちだ。<br /> 優れた安定したJavaScriptコードを書くのに役立つ、素晴らしい原則、プラクティス、パターンがたくさんあると、Derick氏は言う。その1つの例が、2000年代前半に<a href="http://en.wikipedia.org/wiki/Robert_c_martin">Robert C. Martin</a>氏によって言及された<a href="http://en.wikipedia.org/wiki/SOLID">SOLID</a>原則だ。<br /> Derick氏はSOLID原則を、「組み合わせることでうまく機能する5つのパターン」だと説明した。そして、JavaやC#のような言語で使うのと比べて、適用を多少困難にするJavaScriptの特異性について調べながら、サンプルコードを使ってこれらの原則を説明した。<br /> Derick氏は5つの原則を次のように定義する。</p> 
  <ul> 
   <li><b>単一責務の原則</b>。すべてのものは変更の理由が1つであるべきだ。この原則は、開発者が何を構築し、いつ変更を必要とするのか、そのコンテキストと責務を理解するのに役立つ。</li> 
   <li><b>オープン・クローズドの原則</b>。既存のコードを変更せずに、振る舞いを変更できるべきだ。拡張ポイントを使ったり、プラグイン可能なコードを作るなど。</li> 
   <li><b>リスコフの置換原則</b>。派生したオブジェクトや型はそのベースとなるオブジェクトや型と置換可能でなくてはならない。Derick氏によると、これはオープン・クローズドの原則のよりフォーカスしたバージョンだ。</li> 
   <li><b>インターフェイス分離の原則</b>。クライアントは使っていないインターフェイスに依存することを強いられるべきではない。問題はJavaScriptに明示的なインターフェイスがないことだが、これをうまく回避する方法がある。</li> 
   <li><b>依存関係逆転の原則</b>。これは2つの概念から構成されている。1つは抽象化であり、具体的な実装ではなく抽象化したものに依存すべきだということだ。もう1つはオーナーシップで、低レベルの実装は高レベルの概念に依存すべきだということだ。</li> 
  </ul> 
  <p>Derick氏は最後にこう言った。もしあなたのシステムに巨大な一枚岩のコードがあれば、それを部品に分割するのにSOLIDが役に立ちます。複雑さを軽減するわけではありませんが、抽象化をもたらし、詳細を論理的に考えることのできる大きな概念にまとめるのに役立つでしょう。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
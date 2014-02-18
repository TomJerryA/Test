<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>CoffeeScript 1.7</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/coffescript-17"><em>原文(投稿日：2014/02/08)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Jeremy Ashkenas氏は<a href="https://gist.github.com/aseemk/8637896">CoffeeScriptバージョン1.7</a>をリリースした。長らく期待されていた新しい機能がいくつか追加された。</p> 
  <p>このバージョンでは最も多かった要望である丸括弧なしのチェーニングがサポートされた。以前までのバージョンでは、開発者が関数をチェーンさせたいときは、丸括弧を使わなければならなかった。</p> 
  <pre><p>// prior to 1.7 - parenthesis required to chain<br />$('#element').addClass('active').css({ left: 5 });</p>
<p>// as of 1.7 - no parenthesis<br />$ '#element'<br />.addClass 'active'<br />.css { left: 5 }</p></pre> 
  <p>また複数行の文字列もサポートした。以前のバージョンでは、新しい行や空白を表す文字列リテラルは、ふたつの文字列が同じ1行に含まれることを示す`\`演算子を無視していた。バージョン1.7では、修正され、開発者は複数行の文字列をきれいに記述できるようになった。</p> 
  <pre><p>console.log '''The quick brown fox jumped over the \<br />lazy dog'''</p>
<p>// prior to 1.7 outputs<br />The quick brown fox jumped \nover the lazy dog</p>
<p>// as of 1.7 now outputs<br />The quick brown fox jumped over the lazy dog</p></pre> 
  <p>配列の分割代入にも拡張が追加された。これはCoffeScriptで<a href="https://github.com/jashkenas/coffee-script/pull/3268">長らく問題になっていた</a>ものだ。</p> 
  <pre><p># get the last item in the animals array<br />animals = [ 'cat', 'dog', 'hippopotamus' ]</p>
<p># prior to 1.7<br />hippo = animals[animal.length - 1]</p>
<p># as of 1.7<br />[..., hippo] = animals</p>
<p># ...both of which transpile to...<br />hippo = animals[animals.length - 1];</p></pre> 
  <p>新しい演算子も追加された。power演算子、floor division、剰余演算(割り算の余りを返す)。</p> 
  <pre><p># power<br />2 ** 2<br /># transpiles to...<br />Math.pow(2, 2);</p>
<p># floor division<br />2 // 3<br />#transpiles to...<br />Math.floor(2 / 3)</p>
<p># modulo<br />2 %% 3<br />#transpiles to...<br />var __modulo = function(a, b) { return (a % b + +b) % b; };<br />__modulo(2, 1);</p></pre> 
  <p>Node.jsでも適切に使えるようになったので、ディレクトリ内の文が自動的に実行されるのではなく、Nodeのように動作し、index.coffeeファイルだけが動作するようになっている。</p> 
  <p>1.7の開発の大多数(そしてCoffeeScriptの過去数年の開発)はコミュニティによってなされてきた。&quot;100人以上の開発者が開発を行い、パッチをマージしています。&quot;とJeremy氏は言う。&quot;CoffeeScriptはさまざまな使われ方をしています。JavaScriptプログラマにとって魅力的だからです。&quot;1.7のリリースについては、Jeremy氏は<a href="https://github.com/xixixao">Michael Srb氏</a>の貢献に対して<a href="https://twitter.com/jashkenas/status/428243869487362048">特別な謝意</a>を示している。</p> 
  <p>CoffeeScriptは確かに人気があり、GitHub上でも<a href="http://en.wikipedia.org/wiki/CoffeeScript">10番目に人気のあるプロジェクト</a>だ。Ruby on Rails(バージョン3.1以上)のようなフレームワークでもサポートされている。MicrosoftのVisual Studioでも<a href="http://vswebessentials.com/">Web Essentialsプラグイン</a>経由で利用できる。JavaScriptの開発者である<a href="http://en.wikipedia.org/wiki/Brendan_Eich">Brenden Eich氏</a>も自身の<a href="https://brendaneich.com/tag/javascript-ecmascript-harmony-coffeescript/">未来のJavaScriptに対する考え方</a>がCoffeeScriptに影響を受けていることを表明している。</p> 
  <p>GitHubのユーザである<a href="https://gist.github.com/stefanpenner">stefanpenner</a>はCoffeeScriptでは、“…ECMAScript6のimport、exportが重要になるだろう…”と書いている。</p> 
  <p>Jeremy氏はES6について次のように言う。</p> 
  <blockquote> 
   <p>CoffeeScriptはほとんど完成しています。ここ数年とても安定しています。しかし、未来に向かって成長していく必要があります。例えば、新しいJavaScriptの機能をサポート、ソースマップのサポートや、プログラミングスタイルの改善などです。</p> 
  </blockquote> 
  <p>CoffeeScriptコンパイラを書き直す<a href="https://www.kickstarter.com/projects/michaelficarra/make-a-better-coffeescript-compiler">Kickstarterプロジェクト</a>が立ち上がっている。資金調達は成功し、<a href="http://github.com/michaelficarra/CoffeeScriptRedux">CoffeeScriptRedux</a>という名前のプロジェクトになったようだ。 Jeremy氏は新しいコンパイラを作ることの利点について、&quot;ある言語の優れたコンパイラが多ければ多いほど、その言語は健全です。別のコンパイラがあることはCoffeeScriptにとっても良いことなのです。&quot;</p> 
  <p>1.7は<a href="https://github.com/jashkenas/coffee-script">GitHub</a>または<a href="http://coffeescript.org/">CoffeeScriptの公式サイト</a>から入手できる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
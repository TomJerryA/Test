<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>C#でSOLIDにする</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/solid-c-sharp"><em>原文(投稿日：2014/05/23)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://asirobots.com/">Autonomous Solutions Inc.</a>のソフトウェア開発者Brannon B. King氏は<a href="http://msdn.microsoft.com/en-us/magazine/dn683788.aspx">2014年5月</a>の<a href="http://www.infoq.com/jp/news/2013/09/solid-principles-revisited">MSDN Magazine</a>で<a href="http://msdn.microsoft.com/en-us/magazine/dn683797.aspx">C#でSOLIDの原則に反することの危険性</a>と題した記事を公開した。著者は、開発者のミスでC#コードが<a href="http://en.wikipedia.org/wiki/SOLID_(object-oriented_design)">SOLIDの原則</a>を破ることで、拡張または維持することがより難しくなる概要を説明した。</p> 
  <p>King氏は、カウンターコードのサンプルとすべてのSOLIDの原則のためのアドバイスを提供したが、簡潔にするためにオープン・クローズドの原則(OCP)に関係した一部を抽出した。<a href="http://en.wikipedia.org/wiki/Open/closed_principle#cite_note-1">OCP</a>では、&quot;<i>ソフトウェア エンティティ (クラス, モジュール, 関数など)は、拡張のためにオープンでだが、変更にはクローズであるべき</i>&quot;と位置づけている。King氏によると、以下のコードはOCPを破壊する。</p> 
  <pre><p>void DrawNerd(Nerd nerd) {<br />&nbsp;&nbsp; if (nerd.IsSelected) DrawEllipseAroundNerd(nerd.Position, nerd.Radius);<br />&nbsp;&nbsp; if (nerd.Image != null) DrawImageOfNerd(nerd.Image, nerd.Position, nerd.Heading);<br />&nbsp;&nbsp; if (nerd is IHasBelt) // a rare occurrence<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; DrawBelt(((IHasBelt)nerd).Belt);<br />&nbsp;&nbsp; // Etc.<br />}</p></pre> 
  <p>なぜなら“あなたが、顧客が新しいものを表示するニーズがあるたびにこのメソッドを変更する必要がある”ため、代わりに描画するための汎用的なプロシージャーを提案する:</p> 
  <pre>
readonly IList&lt;IRenderer&gt; _renderers = new List&lt;IRenderer&gt;();
void Draw(Nerd nerd) {
   foreach (var renderer in _renderers)<br /> &nbsp;&nbsp;&nbsp; renderer.DrawIfPossible(_context, nerd);
}</pre> 
  <p>このアイディアは</p> 
  <blockquote> 
   <p>…よく知られたインターフェイスを実装した描画クラス(または描画に関するクラス)を書きます。レンダラーは、入力に応じてなにを書くかを判断するために、賢くある必要があります。たとえば、ベルトを描画するコードは、インターフェイスをチェックして、必要に応じて進める“ベルトレンダラー”に移動することができます。</p> 
  </blockquote> 
  <p>OCPを破壊するその他の例は、継承クラスを参照するクラスである。</p> 
  <pre><p>class Nerd {<br />   public void DanceTheDisco() {<br />      if (this is ChildOfNerd)<br />         throw new CoordinationException(&quot;Can't&quot;);<br />   &nbsp;&nbsp; ...<br />   }</p><p>}<br />class ChildOfNerd : Nerd { ... }</p></pre> 
  <p>著者のアドバイスは“基底クラスを直接継承先から参照してはならない。”ということである。この問題はピアクラスで表すことができる:</p> 
  <pre><p>class NerdsInAnArc {<br />   public bool Intersects(NerdsInAnLine line) {<br />&nbsp;&nbsp;&nbsp; ...<br />&nbsp;&nbsp; }<br />&nbsp;&nbsp; ...<br />}</p></pre> 
  <p>King氏は説明する:</p> 
  <blockquote> 
   <p>Arcsとlinesは一般的にはオブジェクト階層でピアです。相互について親密に知るべきではなく、それらの詳細は、最適な共有アルゴリズムで必要になることがあります。他を変更することなく、自由に変更できるようにしておきます。これはまた、単一責務の原則に違反します。あなたはarcsをストアしますか、それともそれを分析しますか？独自のユーティリティクラスに分析操作を含めます。</p> 
  </blockquote> 
  <p>小さなプロジェクトでは、SOLIDの原則を厳格に適用する必要はないかもしれないが、大きなコードベースでは、さらに重要になり、“スパゲッティ”コードを避けることは非常に望ましい。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
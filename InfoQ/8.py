<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>LightTable IDEがオープンソース化</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/lighttable-open-source"><em>原文(投稿日：2014/02/03)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Chris Granger氏が<a href="http://www.lighttable.com">LightTable IDE</a>のバージョン0.6リリースに伴い、<a href="http://www.chris-granger.com/2014/01/07/light-table-is-open-source/">オープンソース</a>にした。このリリースではサードパーティのプラグインがサポートされた。</p> 
  <p>コミュニティは追加の言語プラグインへの貢献を始めている。<a href="https://github.com/jetaggart/light-haskell">Haskell</a>, <a href="https://github.com/darthdeus/LightTable-Ruby">Ruby</a>、<a href="https://github.com/enricosada/LightTable-FSharp ">F#</a>、<a href="https://github.com/rschroll/litex">LaTex</a>、<a href="https://github.com/MarcoPolo/lt-markdown">Markdown</a>などの言語のサポートであり、また、編集のエクスペリエンスに注力している人もいる(<a href="https://github.com/Gozala/lt.plugins.bracketglow">Bracket Glow</a>、<a href="https://github.com/cndreisbach/lighttable-base16-themes">base16 theme</a>、<a href="https://github.com/Gozala/lt.plugins.match-highlighter">match highlighter</a>など)。これらはすべてLightTableに組み込まれているプラグインマネージャで利用できる。</p> 
  <p>もともと、<a href="http://worrydream.com">Bret Victor氏</a>の<a href="http://vimeo.com/36579366">Inventing on Principle</a>と題した講演に<a href="http://www.chris-granger.com/2012/02/26/connecting-to-your-creation">啓発</a>された。Bret氏は自身の原則を“クリエータは自身の作るものにすぐに接続できなければならない”と説明している。Chris氏は開発者がコードに対してすぐにフィードバックできるIDEを作り始めた。<a href="https://www.kickstarter.com/projects/ibdknox/light-table">Kickstarterのキャンペーン</a>で成功し、多くの開発者がそのようなツールの開発に興味を示した。キャンペーン中、このプロジェクトは<a href="http://ycombinator.com">YCombinator</a>の2012年の夏のバッチのひとつとして<a href="http://www.chris-granger.com/2012/05/17/light-table-is-in-yc">受理</a>された。</p> 
  <p>InfoQはChris氏にLightTableの未来について話を聞いた。</p> 
  <p><strong>InfoQ:</strong>プラグインが大量に現れることでLightTable自体が薄まったり、身動きがとれなくなることは心配していませんか。</p> 
  <blockquote>
    Chris: 一般的言えば、エコシステムというものは自分自身を制御するのは得意だと思います。emacs/vim/sublime/textmateにはたくさんのプラグインがあり、すべてうまく動いているようです。私たちが違うのは、さらに自由な変化をもたらすことができるということです(私たちが作ったものに対してどんな批判をして置き換えてもいいのです)。しかし、コミュニティは良い働きをしてくれると思います。 
   <p>より改善したいことのひとつは、使える環境にするためにたくさんのプラグインを管理しなければならないということです。例えば、EmacsやVimはあるエクスペリエンスを提供するプラグインのパックという仕組みはありません。LTのプラグインシステムを使えば、あるプラグインがほかのプラグインに依存するようにできます。つまり、キュレートした&quot;ディストリビューション&quot;を作成することができます。ほかのたくさんのプラグインに依存するプラグインがいくつかのコンフィギュレーションを提供することで、すべてがきちんと動作するようになっています。</p> 
   <p>またこのような仕組みによって、BOTアーキテクチャに光が当たります。エンドユーザは競合する動きを排除し、コードに手を入れなくてもプラグインが正常に動作させることができます。したがって、あなたの質問に対して短く答えれば、心配ありません、ということです。しかし、このプラグインを中心にした仕組みの欠点については引き続き改善をしています。</p> 
  </blockquote> 
  <p>BOTとは、Behaviour-Object-Tagの略で、この言葉は、Chris氏が<a href="http://www.chris-granger.com/2013/01/24/the-ide-as-data">LightTableのアーキテクチャを説明するときに使った</a>。</p> 
  <p><b>InfoQ:</b>当初のKickstarterの計画では、プロジェクトのオープンソース化について、“ある種の水準では、これはオープンソースとビジネスをどのように混ぜ合わせるかについての実験です。私たち全員にとって教育的な経験になるでしょう。”としています。いまのところ、どのように混ぜ合わせていますか。有料のプラグインや有料ライセンスによって解除できる先進的な機能なども今後現れるでしょうか。</p> 
  <blockquote>
   しばらくの間、試行錯誤を続けています。LTをビジネス化する戦略はたくさんありますが、自然に適用できる方法を見つけました。Light Tableを直接、マネタイズするのではなく、マネタイズを促進するサービスを作ることにしました。これを会社の燃料にするつもりです。
  </blockquote>
  <blockquote> 
   <p>どのようなサービス化はまだ正確には言えません。でも、私たちのプログラミングに対する考え方を劇的に変えるでしょう。Light Tableは私たちのプラットフォームであり、私たちの当初のミッションを実現するものだと考えるのがいいと思います。ミッションとは、人々が問題を解決し世界を作るする手助けをするということです。</p> 
   <p>私たちの最新のリリースはこの方向への第1歩です。しかし、近い未来にやってくることに比べれば小さな1歩なのです。</p> 
  </blockquote> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
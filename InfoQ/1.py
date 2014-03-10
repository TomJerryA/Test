<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>IDE組み込み検索エンジン</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/coding_by_web"><em>原文(投稿日：2014/02/25)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p class="MsoNormal">&nbsp;</p> 
  <p class="MsoNormal">Google検索の使いやすさとStackOverflowのようなコードアドバイスコミュニティのメッセージボードの人気は，Web検索を使用したコーディングに対するニーズの所在を明確に示している。Scott Hanselman氏は，コピーによって生じるプログラミングアイデアの相似性に<a href="http://www.hanselman.com/blog/AmIReallyADeveloperOrJustAGoodGoogler.aspx">関して</a>記事を書いている。これらの動向に注目したMicrosoft Researchは，IDEから直接コードを検索可能にするVisual Studio 2013用のプラグインを作り出すことで，新たな進化の一歩を踏み出した。
   <o:p></o:p></p> 
  <p class="MsoNormal"><a href="http://visualstudiogallery.msdn.microsoft.com/a1166718-a2d9-4a48-a5fd-504ff4ad1b65">Bing Code Search for C#</a>はVisual StudioとBing，そしてMicrosoft Researchの各チームのコラボレーションによって開発されたプラグインだ。VS2013のエディタに統合され，IntelliSenseのドロップダウンメニューに新設された &quot;How do I...&quot; オプションを選択して起動する。それによって拡張ウィンドウが開き，Bingで分析する検索語の入力が可能になる。クエリを入力すれば，BingがMSDN, StackOverflow, Dotnetperls, CSharp411から関連性の高い回答が検索される。検索結果全体には簡単なインデックスが付加され，各サンプルの出自が明確に示されている。
   <o:p></o:p></p> 
  <p class="MsoNormal">Microsoftの広報担当者によると，これらのコンテンツをVisual Studioユーザに提供することについては，各Webサイトの合意を得ているということだ。StackOverflowからの検索結果にはさらに，コードスニペットのオリジナル提供者へのリンクも含まれている。情報を提供するプロバイダの追加も可能だが，今のところその予定はない。
   <o:p></o:p></p> 
  <p class="MsoNormal">プラグインには意味的文脈や作業中のプロジェクトの種類など，有効と思われる回答を取得するためのさまざまな”マジック”が使われている。MicrosoftのプログラムマネージャであるAla Shiban氏はこのプラグインについて，Roslynコンパイラプロジェクトの利用法のひとつだと<a href="http://blogs.msdn.com/b/visualstudio/archive/2014/02/17/introducing-bing-code-search-for-c.aspx">述べている</a>。
   <o:p></o:p></p> 
  <p class="MsoNormal">興味深いのは，クエリを受信するために入力されたコードのセキュリティや保護がどうなるのかという点だ。プロプライエタリなソフトウェアプロジェクトに従事する開発者の場合，コードを社外に送信することが企業ポリシに反する可能性がある。この記事を執筆している時点では，プライバシ保護に関しては何も発表されていない。</p> 
  <p class="MsoNormal">Visual Studio 2013ユーザ用にプラグインを<a href="http://visualstudiogallery.msdn.microsoft.com/a1166718-a2d9-4a48-a5fd-504ff4ad1b65">公開</a>したMicrosoft Researchではさらに，インストール前のプラグイン試用に興味を持つ人のための<a href="http://codesnippet.research.microsoft.com/">オンラインデモ</a>も提供している。プログラミング特有のカスタマイズが可能な検索エンジンはMicorosftのBingだけではない。The Hacker Newsの先日の<a href="http://thehackernews.com/2014/02/programming-tutorials-with-DuckDuckGo_21.html">レポートによると</a>，DuckDuckGo検索エンジンもプログラマ指向の検索ツールを<a href="https://duckduckgo.com/goodies#Programming">公開している</a>(ただしIDEプラグインは用意されていない)。
   <o:p></o:p></p> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
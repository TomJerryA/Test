<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Visual Commander Professional v1.3リリース，99のコマンドと50のエクステンション，C#対応の構文強調機能を導入</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/visual-commander-pro-1-3"><em>原文(投稿日：2013/12/02)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://vlasovstudio.com/visual-commander/professional_edition.html">Visual Commander Professional v1.3</a>がリリースされた。Commandsウィンドウで追加ボタンを押下するか，あるいはインポートすることにより，99のコマンドと50のエクステンションを生成することができる。構文の強調表示が導入され，Visual Studioのテキストエディタを統合したコード編集も可能になった。Edit.FindNextSelected, Edit.FindPreviousSelected, Edit.FindNext, Edit.FindPreviousコマンド用の記録も追加されている。</p> 
  <p>マクロ言語の選択によって新しいコマンドやエクステンション用のデフォルト言語を定義することも可能になった。複数バージョンのVisual Studioが同じマシンにインストールされている場合にReflectionTypeLoadExceptionの発生する問題もフィックスされている。カスタムアセンブリがフルパスで指定されているときにFileNotFoundExceptionがスローされる点も修正された。コード内のCRを保存するためのストレージ処理の改善や，例外操作に対するいくつかの拡張も今回のリリースに含まれている。</p> 
  <p>新しいコマンドまたはエクステンションをC#やVBで作成するか，あるいは以前のバージョンから既存のVisual Studioマクロを再利用することで，開発者がVisual Studio 2013/2012/2010で行っている繰り返しタスクを自動化することができる。Visual Studioテキストエディタのキーボードコマンドの記録と再生も可能だ。</p> 
  <p>Visual Commanderを利用すれば，VCmd.RecordMacroとVCmd.RunMacroコマンドをVisual Studioのキーボードオプションに手作業で割り当てることで，Record Macro (コントロール+シフト+R)コマンドとRun Macro(コントロール+シフト+P)コマンドの再割り当てが可能になる。 コマンドやエクステンション，一時的なマクロを含むすべての設定は，&quot;%APPDATA%\Sergey Vlasov\Visual Commander\1.0\snippets.vcmd&quot; にストアされる。</p> 
  <p>&quot;Visual Commanderには現在，APIがありません。コマンドにショートカットを設定した上で，Visual Studioの標準インタフェースを使って，ツールバーにそのショートカットを設定してください。&quot; と話すのは，Visual Commanderの開発リーダを務めていた<a href="http://vlasovstudio.com/about.html">Sergey Vlasov</a>氏だ。<br /> <br /> InfoQでは氏と会話して，今回リリースされたVisual Studio エクステンションについて詳しく聞いた。</p> 
  <p><strong>InfoQ – Visual Commander開発の背景となった目的について説明してください。</strong></p> 
  <blockquote>
   Visual Commanderの大きな目標は，既存のマクロコマンドをVisual Studio 2012/2013で実行可能にすることでした。Visual StudioではVS6の頃からマクロコマンドがサポートされていて，生産性向上のためにたくさんのカスタムコマンドが開発されました。Visual Studio 2012でこの機能がなくなったため，多くの開発者はその手段を失ってしまったのです。この機能を提供するサードパーティ製ツールも，今のところありません。 
  </blockquote> 
  <p><strong>InfoQ – Visual Commanderが開発者の生産性を向上する，ということでしょうか？</strong></p> 
  <blockquote>
   もちろんです。コード編集やVisual Studioのオプション変更，あるいはソリューション修正などといった，通常の作業を行うコマンドシーケンスを作成できます。後はマウスのクリックやキーボードショートカットで，それを起動するだけです。
  </blockquote> 
  <p><strong>InfoQ – 製品テストの成功例として，何かケーススタディがあれば教えてください。</strong></p> 
  <blockquote> 
   <a href="http://visualstudio.uservoice.com/forums/121579-visual-studio/suggestions/2650757-bring-back-macros">Jeff Relf</a>氏が，VS ユーザボイス上の &quot;Bring back Macros&quot; スレッドにVisual Commander Professionalを使用した自身の経験について記事を書いています。
   <a href="http://visualstudiogallery.msdn.microsoft.com/deda8ac1-75e6-4068-89ab-b607cee38f2d">Visual Studio Gallery</a>のVisual Commanderのページにも，３件のレビューとQ&amp;Aが掲載されています。
  </blockquote> 
  <p><strong>InfoQ – Visual Commanderの将来的なロードマップについて教えてください。</strong></p> 
  <blockquote>
   Visual Studioとの統合をさらに改善して，より使いやすいものにしたいと思っています: 
   <ol> 
    <li>VCmdメニューにあるVisual Commanderのコマンドの順序変更を可能にする。</li> 
    <li>Visual Studioキーボードオプションでのキーボードバインディング用に，カスタムコマンド名を追加する。</li> 
    <li>レコードマクロをコマンドとして保存するための，明示的なメニューコマンドを追加する。</li> 
    <li>コマンド編集にインテリセンスを有効にする手段を見出す。しかしながら，Visual Studioの拡張性の限界に行き当たっているのが現状です。</li> 
   </ol> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
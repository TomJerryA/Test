<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Visual Studio  "14"  Previewは大きな機能パックである</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/06/vs2014_ctp1"><em>原文(投稿日：2014/06/04)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p class="Standard">Microsoftは、Visual Studio 2013の後継の最初のプレビューをリリースし、これはいくつかの機能領域で長期プロジェクトの統合を特徴にしている。このリリースにはまだ正式な名前がなく、現在は(引用符付きで)Visual Studio “14”と呼ばれている。新しいエディションのVisual Studioには、C#とVisual Basic用のRoslynプロジェクト、2013年11月のコンパイラーCTPでプレビューされた強化されたC++コンパイラ、ASP.NET vNextが含まれている。
   <o:p></o:p></p> 
  <p class="Standard"><b>C#とVB用Roslyn
    <o:p></o:p></b></p> 
  <p class="Standard">MicrosoftのProgram Manager、Anthony D. Green氏が<a href="http://blogs.msdn.com/b/csharpfaq/archive/2014/06/03/visual-studio-14-ctp-now-available.aspx">述べている</a>ように、C# (とVisual Basic)のコンパイラーは、Roslynテクノロジーで基礎から構築されている。結果、“14”でのC#コードでは、リファクタリングサポートの拡張から<a href="https://visualstudio.uservoice.com/forums/121579-visual-studio/suggestions/3990187-add-operator-to-c">条件付きアクセス演算子?.</a>の追加がある。
   <o:p></o:p></p> 
  <p class="Standard">同様にVisual BasicプログラマーもRoslynの基礎から同じような<a href="http://blogs.msdn.com/b/vbteam/archive/2014/06/03/visual-studio-14-ctp-now-available.aspx">メリット</a>がある。これには、リファクタリングの拡張、複数行文字列サポート、(“定義へ移動”の有用性を改善する)metadata-as-sourceが含まれる。
   <o:p></o:p></p> 
  <p class="Standard"><b>C++11/14の拡張サポート
    <o:p></o:p></b></p> 
  <p class="Standard">Microsoft CorporateのVice President、S. Somasegar氏の“14”の<a href="http://blogs.msdn.com/b/somasegar/archive/2014/06/03/first-preview-of-visual-studio-quot-14-quot-available-now.aspx">発表</a>にはまた、C++言語機能の追加に関する詳細が含まれている: ユーザー定義リテラル、C++14汎用的なラムダキャプチャー、C++14 libs::std:: ユーザー定義リテラル、インライン名前空間、(条件付きを含む)noexcept。これらは2013年11月にリリースされたVC++ CTPリリースの一部としてリリースされた言語機能が含まれている。
   <o:p></o:p></p> 
  <p class="Standard">MicrosoftのEric Battalio氏は、C++11/14遵守を超えたC++追加機能の<a href="http://blogs.msdn.com/b/vcblog/archive/2014/06/03/visual-studio-14-ctp.aspx">広範囲のリスト</a>にコメントした。コンパイラーはC99以上に準拠しており、前回のリリースから400以上のコンパイラーバグが修正されている。Cランタイムはリファクタリングされ、MSVCR140.DLLはVCRUNTIME140.DLL, APPCRT140.DLL, DESKTOPCRT140.DLLにリプレースされている。これとは別にWindowsデスクトップアプリケーションは、メモリの使用量と比較のための新しい診断ツールを利用することができる。
   <o:p></o:p></p> 
  <p class="Standard"><b>ASP.NET vNext
    <o:p></o:p></b></p> 
  <p class="Standard">Visual Studio “14”で新しいASP.NETプロジェクトテンプレートに“ASP.NET vNext”の名前が含まれている。Webアプリケーション、空のWebアプリケーション、クラスライブラリー、コンソールアプリケーションを選択できる。これらの新しいテンプレートを使ったときは、Microsoftの“クラウドに最適化された”ランタイムを使った.NET Core Frameworkの追加フレームワークが提供されている。
   <o:p></o:p></p> 
  <p class="Standard">Project.jsonファイルの編集により依存関係補完の解決をアシストするNuGetを使ったIntelliSenseサポートを容易にする。プロジェクトで必要な<a href="http://blogs.msdn.com/b/webdev/archive/2014/06/03/announcing-web-features-in-visual-studio-14-ctp.aspx">すべてのもの</a>は、アプリケーションのプロジェクトフォルダーに含まれている。これは、デプロイ時にweb.cmdを通じてすべての起動できることを意味する。IISもIIS Expressも必要ない。
   <o:p></o:p></p> 
  <p class="Standard"><b>入手方法</b>
   <o:p></o:p></p> 
  <p class="Standard">
   <o:p></o:p></p> 
  <p>CTPは<a href="http://www.visualstudio.com/en-us/downloads/visual-studio-14-ctp-vs">Visual Studioホームページ</a>からダウンロード(ISOとWebインストーラーの両方が提供されている)できる。 このCTPは、製品コードを書いたり、本番環境にデプロイしたり、既存コピーのVisual Stduioと同居させたりすることができないことをMicrosoftは警告している。 (これは仮想マシンにインストールするかなにもしないのがベストだという意味である。)実際に、以前のバージョンのVisual Studioが存在する場合、デフォルトでCTPはインストールされない。 CTPの<a href="http://support.microsoft.com/kb/2967191">完全なリリースノート</a>には、この動作を無効にする方法が含まれている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
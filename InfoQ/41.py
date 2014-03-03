<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Project Helios: IIS上のASP.NET OWINベースのWebホスト ランタイム</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/helios"><em>原文(投稿日：2014/02/19)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Microsoftは、IISの上で実行される軽量の<a href="http://owin.org/spec/owin-1.0.0.html">OWIN</a>をベースにしたWebホストであるHeliosと呼ばれるプロジェクトをリリースした。</p> 
  <p>Heliosは、<a href="http://www.asp.net/aspnet/overview/owin-and-katana/an-overview-of-project-katana">昨年の夏にMicrosoftによって発表された</a>別のプロジェクト<a href="http://katanaproject.codeplex.com/">Katana</a>のステップに続いている。これは、インストールして、使用して、分離して管理できるよりも、いくつかの独立した小さなコンポーネントを提供することで、.NET Web開発者がASP.NET/IISモノリスを避けて、OWIN仕様を実装したWebホストで実行することができる。</p> 
  <p>ASP.NETの問題のひとつは、.NET Frameworkに含まれているため、数年かかるメジャーバージョンアップのリリースサイクルに紐付いており、特定のテストとバグフィックスのプロセスに影響を受けることである。より機敏に、反応よくWebツールを開発するために、ASP.NETチームはSystem.Web.dllに依存しない、はるかに早い開発サイクルで、迅速に修正を適用できる、いくつかのより小さなコンポーネント (ASP.NET MVC、 ASP.NET Web API) を開発した。それだけでなく開発者はカスタムOWIN上または、OWINのリファレンス実装であるKatana上にホストされたWebアプリケーションをデプロイすることができる。</p> 
  <p>Heliosは、Microsoftの本格的なWebサーバーではなく、IIS上で動作するWebランタイムである。<a href="http://weblog.west-wind.com/posts/2013/Nov/23/Checking-out-the-Helios-IIS-Owin-Web-Server-Host">Rick Strahl氏は以下のように説明する</a>:</p> 
  <blockquote> 
   <p>Heliosは、OWINベースのインターフェイスとコンテキスト セマンティクスをベースに提供するために、System.Webを使わず、直接IISのネイティブ・インターフェイスをフックしています。これは、既存のASP.NET実行環境とは完全に切り離されており、モジュールのパイプラインとデフォルトのASP.NETランタイム プロセスをバイパスして実行されます。… Heliosは、非常に軽量で、生のIIS上で起動するWebホストのショートサーキットされたバージョンです。IISとASP.NETは密接に紐付いていますが、IISコアはかなり軽量で、完全にネイティブコードで実行されることを覚えておいてください。ASP.NETモジュールやハンドラーがインストールされている場合、ASP.NETは相互作用のみがキックされ、それらはネイティブコードとネイティブモジュールのみの場合と比べて遅くなります。</p> 
  </blockquote> 
  <p>Heliosの背景は、IISが提供している成熟していて、豊富な環境を、従来のASP.NETなしで提供しようというアイディアである。 これらのゴールは、「Webサーバーの高密度化」「Webホストの模倣よりも自己ホストの模倣」「Webアプリケーションのデプロイ摩擦の減少」を提供することであると、ASP.NETのセキュリティエンジニアである<a href="http://social.msdn.microsoft.com/profile/levibroderick/">Levi Broderick氏は言う</a>。しかし「それらは既存のアプリケーションの100%互換を提供しようとしていません。具体的にはHeliosプロジェクトは、.aspxや.ashxエンドポイントなどのASP.NETイズムはサポートしていません」</p> 
  <p>開発については、Heliosは次の基本要件がある: Windows 8かWindows Server 2012、.NET Framework 4.5.1、Visual Studio 2012か2013。Broderick氏は、Windows 7で開発している開発者のために「この要件は将来のプレリリースで」緩和する可能性があると述べた。Heliosアプリケーションは、Windows Azureまたは、Windows Server 2012、.NET Framework 4.5.1と完全信頼を持つ任意のホスティング環境にデプロイすることができる。</p> 
  <p>パフォーマンスの面で言うと、ASP.NETの“Hello World”アプリケーションと比較して、Heliosは2～3倍以上のスループットを実現しているが、実際のアプリケーションはこれよりもはるかに複雑であるため、2つのWebソリューションの比較のベースとして採用することはできないとBroderick氏は言う。しかしメモリ消費量の面では、<a href="http://blogs.msdn.com/b/webdev/archive/2014/02/18/supplemental-to-asp-net-project-helios.aspx#_On_performance_and">Heliosは、System.Webよりもよい</a>:</p> 
  <blockquote> 
   <p>絶対数では、Heliosアーキテクチャは、私たちのサンプルアプリケーションにおいて、標準のASP.NETパイプラインと比較しておよそ1 GB少なく、50,000の同時リクエストを達成しました。サンプルアプリケーションは、最小のベースラインで設計されており、重要なアプリケーションにも同様の絶対値を期待することができます。</p> 
  </blockquote> 
  <p>注意: Broderick氏の<a href="http://blogs.msdn.com/b/webdev/rsscomments.aspx?WeblogPostID=10500903">コメント</a>の通り、MicrosoftはまだHeliosにコミットしていない:</p> 
  <ul>
   <!--EndFragment-->
  </ul> 
  <ul> 
   <p>
    <!--EndFragment-->私たちはこの作業をやめて、リリースされない可能性があります。例えば、人々が実際にそれを望んでいなかったとき、チームが解散してしまったとき、よりよい何かが現れたとき、その他私たちが想像つかない多くの理由があり得ます。チームは、これがAzure専用になることには興味がありません。</p> 
  </ul> 
  <p>開発者は<a href="https://www.nuget.org/packages/Microsoft.Owin.Host.IIS/">Microsoft.Owin.Host.IIS NuGetパッケージ</a>をインストールした後で、Visual Studioから直接HeliosベースのASP.NETアプリケーションを開発することができる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
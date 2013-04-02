<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>GitプロトコルとVisual Studio 2012をサポートしたGitSync for Plastic SCM</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/gitsync-for-plastic-SCM;jsessionid=CA0684A227DD192469856223FF5CAF56"><em>原文(投稿日：2013/03/19)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>ネイティブのWindowsベースの分散バージョン管理システム(DVCS)の<a target="_blank" href="http://plasticscm.com/gitsync/index.html">GitSync for Plastic SCM</a>はhttps://とGitのプロトコルであるgit://を直接サポートし、Gitリポジトリと統合できる。</p> 
 <p>Plastic SCMの機能を利用してGitHubだけではなく、CodeplexやBitBucket、Gitプロトコルを利用しているあらゆるGitサーバへもコードの変更をプッシュしたりプルしたりできる。また、Visual Studio 2012と統合されるので単一のIDE上ですべての機能を利用できる。</p> 
 <p>GitSync for Plastic SCMにはGitリポジトリを複製し、後から変更をプッシュすることができる。開発者はブランチを作成し、Gitへプッシュするか、Git上にブランチを作成してそこへプルすることができる。変更の競合も効率的に扱うことができるので、開発者はふたつのシステム上にある同じブランチで作業して変更を統合できる。単一のPlastic SCMとGitを使って開発しているのと同じだ。</p> 
 <p>Plastic SCMには分散ブランチエクスプローラが含まれている。これを使うとリモートのリポジトリをローカルのリポジトリのように見ることができ、リモートの変更とローカルの変更をダイアグラム上で引き合わせることができる。さらに、開発者は移動されたコードを検出するXdiffやXmergeを使って簡単にコードの追跡できる。</p> 
 <p>GUIの注釈ビューでmethodhistoryを起動できる。GUIはEclipseをサポートする。複数の言語もサポートし、C#のサポートは改善されている。リファクタリングしたコードの履歴も追跡できる。</p> 
 <p>&quot;GitSyncは別の製品ではなく、Gitコミュニティへ提供するPlastic SCMであるということを強調したいと思います。したがって、クライアントサイドでPlasticを利用し、変更をGitサーバへプッシュ/プルできます。GitツールのWindowsサポートはMacOS Xと比べ貧弱であり、一方、Plastic SCMはWindowsに強い製品なので、GitSyncを提供することでGitユーザを助け、Plastic SCMの導入をより簡単にできると考えました。&quot;とPlastic SCMのプレジデントであるPablo Santos氏は言う。</p> 
 <p>InfoQはこの製品のプロダクトチームのメンバであるManuel Lucio Dallo氏に話を聞いた。<br /> <br /> <strong>InfoQ: GitSync for Plastic SCMは生産性を上げますか。</strong></p> 
 <blockquote>
  Git &quot;クライアント&quot;としてのPlasticを使うことで、素早い開発と効率的なソース管理とコーディングが実現できます。Plastic SCMは完全にグラフィカルで直観的です。時間と煩雑なコマンドが必要なGitの複雑で定型的作業はPlasticでは2、3回のクリックで実現できます。
 </blockquote> 
 <p><strong>InfoQ: GitSync for Plastic SCMは実際はどのようなシナリオで使われますか。</strong></p> 
 <blockquote>
  Gitを使っていると想像してください。Gitを使わなければならない状況です。開発機でPlastic SCMを使うと、プッシュ、プルを行っても開発は完全にPlastic SCMの下で行われます。これは評価段階にリソースを割かずに運用環境でPlasticのテストをしたいチームにとってはとても便利です。
  <br /> 
  <br /> また、Gitがコマンドラインインターフェースしか提供しないのに不満を持っている開発者もいるでしょう。そのような開発者にもPlasticは役立ちます。強力なGUIを提供することで開発者のワークフローをシンプルにします。開発者がPlasticをGitと同等かそれ以上に使いやすいと感じてくれたら、そのチームは完全にPlastic SCMへ移行できると思います。
  <br /> 
  <br /> 必要最低限のリソースも特にありません。ラップトップで十分に動作します。サーバには.NET Framework 3.5と、デフォルトのデータベースとしてSQL Server CEが必要です。
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
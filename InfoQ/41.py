<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PowerShellのDesired State Configuration，プッシュモードとプルモードをサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/powershell-dsc-push-and-pull"><em>原文(投稿日：2013/12/16)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://blogs.msdn.com/b/powershell/">Windows PowerShell Blog</a>に現在，PowerShellのDSC(Desired State Configuration)に関する記事が掲載されている。DSCはWindowsでコンピュータの構成管理を行うための，Microsoftからの提案だ。最新の記事のひとつではプッシュとプルという，DSCで選択可能な２つのコンフィギュレーションモードについて<a href="http://blogs.msdn.com/b/powershell/archive/2013/11/26/push-and-pull-configuration-modes.aspx">説明されている</a>。</p> 
  <p>DSCは指定されたノードあるいはマシンに必要な構成を宣言的に指定する，PowerShellツールの追加機能である。これはPowerShellが元々備えている，命令型のスタイルとは異なったアプローチだ。マシン設定のために実行するステップに注目するのではなく，DSCを利用したスクリプトでは，必要な設定をただ単に記述すればよい。それを実施する方法は，PowerShell DSCシステムが決定してくれるのだ。</p> 
  <p>PowerShell DSCはリソースという概念を持っている。リソースはユーザやグループ，サーバロール，レジストリエンティティといった項目を設定するブロックを構成するものだ。<a href="http://technet.microsoft.com/en-us/library/dn249921.aspx">組み込み</a>でいくつかのリソースが用意されている他に，<a href="http://technet.microsoft.com/en-us/library/dn249927.aspx">独自の</a>リソースを<a href="http://blogs.msdn.com/b/PowerShell/archive/2013/11/19/resource-designer-tool-a-walkthrough-writing-a-dsc-resource.aspx">作成</a>することもできる。以下の例では<a href="http://technet.microsoft.com/en-us/library/dn282129.aspx">File</a>リソースを使用して，<code>localhost</code>の<code>C:＼inetpub＼wwwroot</code>の内容が<code>C:＼SiteFiles</code>の正確なレプリカであることを定義している。</p> 
  <pre>
Configuration SiteConfig
{
   # A Configuration block can have zero or more Node blocks
   Node &quot;localhost&quot;
   {
      # File is a built-in resource you can use to manage files and directories
      # This example ensures files from the source directory are present in the destination directory
      File MyFileExample
      {
         Ensure = &quot;Present&quot;  # You can also set Ensure to &quot;Absent&quot;
         Type = &quot;Directory“ # Default is “File”
         Recurse = $true
         SourcePath = &quot;C:＼SiteFiles&quot; # This is a path that has web files
         DestinationPath = &quot;C:＼inetpub＼wwwroot&quot; # The path where we want to ensure the web files are present
      }
   }
}</pre> 
  <p>コンフィギュレーションの適用に関して，PowerShellにはプッシュとプルという２つのモードが用意されている。プッシュモードは，<code>Start-DscConfiguration</code> cmdletを実行することで即時に起動される。例えば下記のコマンドでは，カレントパスにあるコンフィギュレーションが，スクリプトで指定されたすべてのノードに対して適用される。</p> 
  <pre>
Start-DscConfiguration -Wait -Verbose -Path .</pre> 
  <p>プルモードでは，イニシアティブが与えられるのはノード自身だ。プルサーバを監視して，新しいコンフィギュレーションをチェックするのはノードの責任になる。新しいコンフィギュレーションが用意されると，LCM(Local Configuration Manager) - PowerShell DSCのエンジン - がダウンロードと適用を行う。プルモードの設定は少し複雑だ。プルサーバとなるWebサイトの設定や，各ターゲットノードのLCMを，<a href="http://technet.microsoft.com/en-us/library/dn521621.aspx"><code>DscLocalConfigurationManager</code></a>を使って<a href="http://blogs.msdn.com/b/powershell/archive/2013/11/26/push-and-pull-configuration-modes.aspx">設定</a>する必要がある。Windows PowerShellチームでも，プルサーバの設定を簡単にするための<a href="http://blogs.msdn.com/b/powershell/archive/2013/11/21/powershell-dsc-resource-for-configuring-pull-server-environment.aspx">記事</a>とヘルパツールを公開している。</p> 
  <p>ほとんどのツールが両方のモードをサポートするが，<a href="http://www.ansibleworks.com/">Ansible</a>など<a href="http://www.ansibleworks.com/wp-content/uploads/2013/05/AnsibleAgentless.pdf">プッシュ用</a>のものや，<a href="http://puppetlabs.com/">Puppet</a>や<a href="http://www.getchef.com/">Chef</a>のように<a href="http://docs.opscode.com/chef_overview_server.html">プル用</a>のものもある。どちらのモードにも賛成と反対，さまざまな議論がある。プッシュモードはシンプルで，制御性に優れる。ターゲットノード上に特別なソフトウェアをインストールする必要がない上に，コンフィギュレーションがユーザの要求に従って起動するからだ。一方のプルモードはスケーラビリティに優れ，メタデータ機能が豊富だ。ターゲットノードは自分自身で，非同期的に設定を実行する。またプルサーバには，各ノードの状態に対応するメタデータを集中的に配置することができる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
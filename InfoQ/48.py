<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>LLBLGen Pro v4.0 Betaリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/llblgen-pro-v-4-0-beta;jsessionid=D24E9ACEFF8B0BAF33BC710C23D984C0"><em>原文(投稿日：2013/03/13)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://weblogs.asp.net/fbouma/archive/2013/03/07/llblgen-pro-v4-0-beta-released.aspx">LLBLGen Pro v4.0</a>のベータ版がリリースされた。<a target="_blank" href="http://msdn.microsoft.com/en-in/library/ms191165(v=sql.105).aspx">Table-Valued Function</a>、<a target="_blank" href="http://msdn.microsoft.com/en-IN/library/ff878091.aspx">SQL Server 2012 Sequence</a>がサポートされており、<a target="_blank" href="http://www.microsoft.com/visualstudio/eng/whats-new">Visual Studio 2010/2012</a>と統合されている。デザイナは追加名前空間の割り当てをサポートし、ルールシステムに基づいてエレメントをモデリングするインターフェースを提供する。タイピングのショートカットも調整されているので、デフォルトの長さや精度の設定ができる。</p> 
 <p>さらに、デザイナを閉じずに列挙型のタイプインポートファイルを再スキャンできる。今回のリリースにはデザイナ内のプロジェクトの状態に基づき、アクションをハイライトするアクションサジェスチョンウィンドウが含まれる。<br /> &nbsp;<br /> LLBLGen Pro v4.0のランタイムフレームワークのエンティティフェッチパイプラインは30%速くなり、問い合わせ結果キャッシュや<a target="_blank" href="http://github.com/SolutionsDesign/LLBLGenProExamples_4.0">データスコープ</a>、XMLへの<a target="_blank" href="http://tech.pro/tutorial/798/csharp-tutorial-xml-serialization">シリアライズ</a>のような新しい機能をと際している。また、QuerySpecを使った型付きリストを取り出す機能も搭載している。 <br /> <br /> さらに、QuerySpecとLINQのアセンブリがORMSupportClassesアセンブリへ統合され、ODataをサポートしたクラスが<a target="_blank" href="http://www.microsoft.com/en-us/download/details.aspx?id=35840">WCF Data Services 5.3 </a>向けに用意されている。そして<a target="_blank" href="http://www.odata.org/documentation">OData v3</a>をサポートする。</p> 
 <p>リード開発者のFrans Bouma氏によれば、LLBLGen Pro v4のリリースは今年4月の前半に予定されている。<br /> &nbsp;<br /> InfoQは氏にLLBLGen Proについて話を聞いた。<br /> <br /> <strong>InfoQ:LLBLGen Proを使う利点を教えてください。<br /> </strong></p> 
 <blockquote>
  LLLGen Proを使えばエンティティモデルに注力できます。エンティティモデルはエンティティクラスとエンティティクラスにマッピングされるテーブルから成ります。O/Rマッピングの両方のサイドから生まれるものです。LLBLGen Proのデザイナを使うとこのモデルを簡単にかつ直接的に扱うことができます。モデルの検証やコードの生成機能を使えば、クラスとマッピングが上手くいかなかったり、元のモデルを表現できなかったりすることがなくなります。ユーザは機能を記述する手間を省くことができるのです。
 </blockquote> 
 <p><strong>InfoQ: LLBLGen Pro v4.0は以前のバージョンと何が違うのですか。</strong></p> 
 <blockquote>
  各バージョンでいくつかの大きな機能、小さな機能を導入していますが、v4はデザイナとランタイムはv3.5を引き継いでいます。しかし、デザイナはVisual Studio 2010/2012と完全に統合されます。つまり、デザインの仕方は(Visual Studio 2012の提供する機能に組み込まれるので)変わります。
  <br /> これが見た目上の最も大きな変更でしょう。
  <br /> 
  <br /> ランタイムには Table-Valued-Functionのサポートのような大きな機能追加がされ、接続されない'context'や'session'と見なすことができるDataScopeという機能も追加されています。これらを使えば、エンティティマネージャと作業単位をひとつにして、開発者がLoBアプリをとても少ないコードで開発することができます。
  <br /> &nbsp;
  <br /> すべての新しいバージョンで既存のアプリケーションを壊さないようにしながら、以前のバージョンのリファイン/リファクタをしつつ、新しい機能を追加しようとしています。
 </blockquote> 
 <p><strong>InfoQ: 無償バージョンを提供する計画はありますか。</strong></p> 
 <blockquote>
  商用製品なので無償版はありません。Visual Studio.NETが商用製品なのと同じです。V4 RTMの無償バージョンを提供する計画はありますが、詳細はまだ明らかにしていません。
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
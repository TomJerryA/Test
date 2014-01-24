<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ログとトレースにLINQを使用する</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/tx-release"><em>原文(投稿日：2014/01/09)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Microsoft Open Technologiesは先頃，ログやトレースを使ったデバッグ作業と，リアルタイム監視および警告システムの開発を支援するオープンソースプロジェクトである<a href="http://tx.codeplex.com/">Tx</a>のリリースを<a href="http://blogs.msdn.com/b/interoperability/archive/2014/01/06/new-release-tx-linq-to-logs-and-traces.aspx">発表した</a>。</p> 
  <p>注目すべき機能としては，</p> 
  <ul> 
   <li>生のイベントソースに<a href="http://msdn.microsoft.com/en-us/library/bb397926.aspx">LINKQ</a>が使用可能。</li> 
   <li>リアルタイムのイベントソースに対して<a href="http://msdn.microsoft.com/en-us/data/gg577609.aspx">リアクティブエクステンション</a>を使用可能にするとともに，多重化されたイベントシーケンス(異なったタイプのイベントを発生順に格納する単一のシーケンス)をサポート。</li> 
   <li>複数のソースを対象とする単一クエリ，リアルタイム情報と履歴情報を同じAPIでサポート。</li> 
   <li>履歴ログとトレースファイルを対象に，１回の読み込み処理で複数のクエリ – 例えば，“警告” イベントの総数の取得，“Begin” と “End” に一致するイベントの検索，各アクティビティの平均期間の算出 – を実行可能。</li> 
  </ul> 
  <p>簡単な解析は<a href="http://www.linqpad.net/">LINQPad</a>で実行できる。あるいは.NETアプリケーションとして監視アプリケーションを開発することも可能だ。LINQPadで操作する場合は，データベースに格納されているようにイベントを取り扱うことができる。</p> 
  <p>リリースは４つのNuGetパッケージで構成されている。</p> 
  <ul> 
   <li><a href="http://www.nuget.org/packages/Tx.Core/">Tx.Core</a>&nbsp;– 特定のトレース形式に依存しない共通コンポーネント。</li> 
   <li><a href="http://www.nuget.org/packages/Tx.Windows/">Tx.Windows</a>&nbsp;– ETW(Event Tracing For Windows)やイベントログ，ファイルおよびリアルタイムカウンタAPIをソースとするパフォーマンスカウンタ，W3CフォーマットのIISテキストログをサポート。</li> 
   <li><a href="http://www.nuget.org/packages/Tx.SqlServer/">Tx.SqlServer</a>&nbsp;– SQL Server拡張イベントをサポート。</li> 
   <li><a href="http://www.nuget.org/packages/Tx.All/">Tx.All</a>&nbsp;– 上記すべてに使用可能なユーティリティパッケージ。</li> 
  </ul> 
  <p>Microsoftが<a href="http://tx.codeplex.com/SourceControl/latest#Doc/WhenToUse.md">Txを使用しないケース</a>についてアドバイスしている点にも注意が必要だ。</p> 
  <ul> 
   <li>リアルタイムなフィードに関連せず，データがすべてメモリあるいは<a href="http://tx.codeplex.com/SourceControl/latest#Source/Tx.Windows/IIS/W3CEnumerable.cs">解析の容易な単一ファイル</a>に格納されている場合は，TxよりもLINQ-To-Objectsを使用した方がよい。</li> 
   <li>リアルタイムフィードが存在する場合でも，各フィードあるいはファイルに格納されているイベントが単一形式ならば，リアクティブエクステンションを単独で使用すればよい。</li> 
  </ul> 
  <p>このツールはこれまで，Microsoft社内でWCFチームやService Busチームが使用していた。それが今回，.NET開発者のプロジェクトに利用できるように公開されたものだ。まずは<a href="http://tx.codeplex.com/documentation">資料</a>を確認することから始めるとよいだろう。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
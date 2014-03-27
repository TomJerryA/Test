<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Entity Framework 6.1リリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/ef-6-1"><em>原文(投稿日：2014/03/21)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>近頃、<a href="http://blogs.msdn.com/b/adonet/archive/2014/03/17/ef6-1-0-rtm-available.aspx">リリース</a>されたEntity Framework 6.1は多くの興味深い改善がなされている。例えば、ツーリングの改良、CommitFailureHandler、IndexAttribute、Public Mapping APIなどだ。</p> 
  <p>EF 6には<a href="http://www.infoq.com/news/2013/11/ef-6-performance-issues">起動時間の遅さとエンティティのマテリアライゼーションの問題</a>があった。これらの問題は6.1で<a href="https://entityframework.codeplex.com/workitem/1829">解消</a><a href="https://entityframework.codeplex.com/workitem/1778">される</a>ようだ。また、ビューの生成などの性能改善やLINQクエリのnull比較の改善もされている。また、その他の改善は、</p> 
  <ul> 
   <li><a href="http://msdn.microsoft.com/en-US/data/jj591583#Index">Index Attribute</a> - EF Code-Firstを使用してひとつ以上のカラムにインデックスを設定できる。ユニークインデックスと非ユニークインデックスの両方をサポートする。</li> 
   <li><a href="https://entityframework.codeplex.com/wikipage?title=Public%20Mapping%20API">Public Mapping API</a> - マッピングのメタデータにアクセスできる。</li> 
   <li><a href="https://entityframework.codeplex.com/wikipage?title=Handling%20of%20Transaction%20Commit%20Failures%20&amp;version=13">トランザクションのコミット失敗の処理</a> - コミット時のネットワーク障害は難しい問題になりがちで、アプリケーションがトランザクションが成功したか失敗したかわからなくなってしまう。処理に冪等性があるなら、簡単にリトライできるが、そうでない場合、トランザクションをコミットしていいかどうかチェックする方法が必要だ。今回の新しいリリースによって構成ファイルを変更するだけでこの機能が利用できる。この機能はEF 6で導入されたリトライ機能を利用する。<br /> <br /> この機能にはコミットの情報を保持するテーブルが必要。テーブルは手動でパージする必要がある。</li> 
   <li>LINQクエリでのToString、String.Concat、HasFlagsのサポート。</li> 
   <li><a href="http://msdn.microsoft.com/en-US/data/jj556606#Interceptors">app/web.configを使ったインタセプタの構成</a>によるデバッグの簡易化。いくつかの新しいインタセプタ(DatabaseLogger、IDbTransactionInterceptor)も追加されている。</li> 
   <li><a href="https://entityframework.codeplex.com/wikipage?title=Tooling%20Consolidation">ツーリングの強化</a> - データモデル作成のための単一のエントリポイント(Designer、Code-first、データベースからのインポート)</li> 
  </ul> 
  <p>変更について詳細が知りたい場合は<a href="https://entityframework.codeplex.com/wikipage?title=specs">ここ</a>で確認できる。また、<a href="https://entityframework.codeplex.com/workitem/list/advanced?keyword=&amp;status=Closed&amp;type=All&amp;priority=All&amp;release=EF%206.1.0&amp;assignedTo=All&amp;component=All&amp;sortField=LastUpdatedDate&amp;sortDirection=Descending&amp;page=0&amp;reasonClosed=Fixed">課題管理</a>でもすべての課題を確認できる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Brent Ozar氏，SQL Serverの生産性向上について語る</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/02/brent-ozar-sql-server;jsessionid=9F5400EA340E2BC28F13C4D7D13B1E6C"><em>原文(投稿日：2013/02/26)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>SQL Serverコンサルタントの <a target="_blank" href="http://www.brentozar.com/archive/2013/02/7-things-developers-should-know-about-sql-server">Brent Ozar</a> 氏は先日，すべての <a target="_blank" href="http://www.microsoft.com/en-in/SQLserver/default.aspx">SQL Server</a> 開発者が日々のプログラミングタスクで実践するべきだという，７つのテクニックを公表した。その中で氏は，<a target="_blank" href="http://msdn.microsoft.com/en-IN/library/ms188385.aspx">ORDER BY</a> 句はできる限り使用せずに，クエリ結果をメモリ上に格納して，アプリ側でデータソートを実行するべきだ，としている。<br /> <br /> もしデータベースがデータ処理，ソート，ロード，キャッシュなど複数の処理を行っているならば，それぞれのタスクごとに別のデータベースを用意することが理想的だ。さらに各データベースは単純復旧モードで運用して，毎日１回バックアップを取得することが望ましい。</p> 
 <p>氏はまた，<a target="_blank" href="http://msdn.microsoft.com/en-us/library/ms188754.aspx">DMV(Dynamic Management Views)</a> の効率的な利用を提案するとともに，例えばアプリケーションの書き込み，5～15分前に更新されたデータの参照，昨日のデータの参照といったさまざまなシナリオに対して，アプリ内で３つ別々の接続文字列を使用するようにアドバイスしている。SQL Serverには複数サーバによる書き込み処理をスケールアウトするための選択肢が少ないので，この最初のシナリオはスケールが難しい，という理由からだ。<br /> <br /> &quot;<a target="_blank" href="http://blog.sqlauthority.com/2011/05/08/sql-server-what-kind-of-lock-with-nolock-hint-takes-on-object/">With(Nolock(</a> よりも <a target="_blank" href="http://blogs.technet.com/b/sql_server_isv/archive/2010/12/21/using-read-committed-snapshot-isolation-mini-lab.aspx">READ COMMITTED スナップショット分離</a> の方が，一貫性のあるデータを少ないブロックで取得することができるという面で，アプリケーションとしてはよい選択です。&quot; と氏は述べている。<br /> <br /> さらには，定期的に更新されないような古い版の書籍やオンライン記事は参考にならない，とも言う。&quot;優れたアドバイスに見えるものであっても，アンチ-ドクターPhil (Phil McGraw：米国の心理学者) 戦略を採用すべきです&quot; というのが氏の意見だ。<br /> <br /> そして最後に氏は，コードの再利用には関数よりも，<a target="_blank" href="http://msdn.microsoft.com/en-us/library/aa174792(v=sql.80).aspx">ストアドプロシージャ</a> と <a target="_blank" href="http://msdn.microsoft.com/en-in/library/ms187956.aspx">ビュー</a> を使用するように勧めている。関数はデータベース層において性能的なデメリットが大きい，ということがその理由だ。</p> 
 <p>氏のアドバイスに対しては反対者もいる。<br /> <br /> 例えば Tyler Burd氏の</p> 
 <blockquote>
  #2 (&quot;ORDER BYは使うな: アプリ内でソートせよ&quot;) には，無条件には賛成できません。
 </blockquote> 
 <p>というコメントに対して，氏は次のように答えている。</p> 
 <blockquote>
  データセット全体をアプリ層に落とし込んで，そこでキャッシュしてはどうでしょう？
 </blockquote> 
 <p>関数に代えてビューやストアドプロシージャを使うべき，という提案に対しても，何人かの開発者からコメントが投稿されている。<br /> <br /> Brentのアドバイスや提案に対して，読者は賛成あるいは反対，いずれの立場だろうか？氏の提案に対する意見をコメントしてほしい。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PostgreSQLのNoSQL機能が大幅に向上</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/postgresql-9-4"><em>原文(投稿日：2014/05/23)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>PostgreSQL 9.4 Beta版には待望の&quot;バイナリJSON&quot;型，JSONBが実装されている。この文書データのための新しいストレージ形式には，JSONデータをハイパフォーマンスに操作するためのインデックス処理，関数，演算子が用意される。</p> 
  <p>JSONB型は<a href="http://obartunov.livejournal.com/177247.html">２つのプロジェクト</a>，HStoreとJSONが統合されたものだ。JSONの持つ特長をすべて備えるだけでなく，バイナリ表現の採用やインデックスによって，ストレージの効率化や検索の高速化も実現している。現在HStoreとJSONを使用しているユーザはすべて，最終的にはJSONBに移行すると期待されている。</p> 
  <p>PostgreSQLのユーザベースはこれまで，堅牢なリレーショナル機能を求める開発者や，Oracleなどエンタープライズデータベースから転向したユーザだった。それが今，NoSQL機能を重視するのはなぜだろう？<a href="http://www.databasesoup.com/2014/02/why-hstore2jsonb-is-most-important.html?showComment=1393181805085#c8222906176754761423">疑問に答えてくれた</a>のは，<a href="http://www.postgresql.org/community/contributors/">コアチームメンバ</a>のひとりであるJosh Berkus氏だった。</p> 
  <blockquote> 
   <p>Oracleのマーケットは，現在は大規模ですが，まったく成長していません。PostgreSQLに移行するユーザの実数はそれよりも小さいのです。PostgreSQLが今後どれほど多くの機能を追加したとしても，Oracleに追いつくことを目標にしている限り，Oracleを越えることは絶対にできません。</p> 
   <p>革新的な技術を採り入れることで，新たなユーザの獲得とマーケットの拡大が可能になります。</p> 
  </blockquote> 
  <p>そのスレッドの他のコメントからも，Node, Python, Go, Rubyといった技術でPostgreSQLを使用するいくつかのスタートアップ企業が，パフォーマンスに優れたJSONサポートを待ち望んでいた様子がうかがえる。</p> 
  <p>これらの点を考慮して確実に言えるのは，PostgreSQLが新たなユースケースを手に入れるためには，これまでの特長である信頼性などを損なうことなく，JSONのファーストクラスでのサポートを実現することが必要だということだ。</p> 
  <p>PostgreSQLよりもNoSQLデータベースが適している領域は他にもある。例えば，EnterpriseDBの上級データベースアーキテクトでコアチームメンバのBruce Momijan氏は，次のように指摘する(Eメールより抜粋)。</p> 
  <blockquote>
   PostgreSQLの機能や性能が向上しても，NoSQLソリューションの方が適しているエッジケースはやはり存在します。列指向(columnar)データベースであるCassandraは，ログファイルのような重複の多い非構造データに適していますし，新しいノードの追加も容易です。ただし，NoSQLの機能の恩恵を望む一方でACID準拠も必要なアプリケーションには，PostgreSQLがやはり有利でしょう。
  </blockquote> 
  <p>有力なコントリビュータであり，EnterpriseDBの上級データベースアーキテクトであるRobert Haas氏も，次のように述べている。</p> 
  <blockquote>
   MapReduceを使用して高度な並列クエリを実行している場合を例にしましょう。この場合はHadoopなどを使った方がよいかも知れません。もうひとつの例は，データモデルが，大規模なJSONオブジェクトに細かな修正を何度も行う必要のある場合です。NoSQLソリューションの中に，このようなケースをもっと効率よく扱えるものがあるかも知れません。
  </blockquote> 
  <p>このような特定のユースケース以外にも，スキーマレスとリレーショナルストレージをデータタイプによって柔軟に使い分ける必要のあるアプリケーションや，ACIDを保証が必要な場合に対して，PostgreSQLは説得力のある選択肢になろうとしている。</p> 
  <p>バージョン9.4で導入される重要な新機能は，JSONBの他にもいくつかある。</p> 
  <ul> 
   <li><a href="http://www.postgresql.org/docs/0.0/static/logicaldecoding.html">Data Change Streaming API</a> –&nbsp; レプリケーションストリームのデコードと変換を可能にする。新しいレプリケーションツールの基本機能として，高速かつ柔軟なレプリケーションとスケールアウトソリューションをサポートしている。</li> 
   <li>&quot;並行リフレッシュ&quot;を備えたマテアライズドビュー。</li> 
   <li>ALTER SYSTEM SET –&nbsp; 管理作業を容易にするために，リモートクライアントのSQLコマンドラインによってpostgresql.confが変更可能になる。</li> 
  </ul> 
  <p>その他の新機能としては，</p> 
  <ul> 
   <li><a href="http://www.postgresql.org/docs/devel/static/bgworker.html">ダイナミック・バックグラウンドワーカ</a></li> 
   <li><a href="http://www.postgresql.org/docs/devel/static/warm-standby.html#STREAMING-REPLICATION-SLOTS">レプリケーションスロット</a></li> 
   <li>書き込み処理のスケーラビリティ向上</li> 
   <li>アグリゲート，<a href="http://www.postgresql.org/docs/devel/static/gin.html">GIN</a>インデックスの縮小化，WALボリュームの削減など，いくつかのパフォーマンス向上。</li> 
   <li>更新可能なセキュリティバリアビュー</li> 
   <li>新たな配列操作とテーブル機能</li> 
   <li>遅延スタンバイ</li> 
   <li>MVCCシステムカタログの更新</li> 
   <li>いくつかのALTER TABLEコマンドでロックレベルを低下</li> 
   <li>バックアップのスロットリング</li> 
   <li>WITHIN GROUP句</li> 
  </ul> 
  <p>変更点のリストは<a href="http://www.postgresql.org/docs/devel/static/release-9-4.html">リリースノート</a>で確認することができる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
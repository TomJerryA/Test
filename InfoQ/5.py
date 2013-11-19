<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>SQLの復活</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/sql-newsql-nosql"><em>原文(投稿日：2013/11/08)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>データベース開発の新潮流はSQLへの回帰を示している。しかし、従来のリレーショナルデータベースをより優れたハードウエアに乗せるのではなく、シャードを使ったアーキテクチャでもなく、NewSQLを通じてだ。</p> 
  <p align="left">“No <em>more</em> SQL”そして“Not only SQL”と解されたNoSQLによる失墜の後、従来のSQLが復活してきているようだ。復活の要因のひとつにはシャーディングがあるが、これだけでは説明がつかない。SQLとNoSQLを組み合わせる技術や従来の関係データベースの性能とスケーラビリティを改善する動きがある。これらの動きはNewSQLと呼ばれている。GoogleはかつてはNoSQLの最初の支持者だったが、F1という、BigTableの可用性とスケーラビリティを持つ分散関係データベースを構築した。これは“一貫性と使いやすさ”を備えるSQLが使える。Googleはホワイトペーパー<a href="http://static.googleusercontent.com/external_content/untrusted_dlcp/research.google.com/en/us/pubs/archive/41344.pdf">F1: A Distributed SQL Database That Scales</a>&nbsp;(PDF)でF1を次のように説明する。</p> 
  <blockquote> 
   <p>… GoogleのAdWords向けに新しいストレージシステムとして、耐障害性を持ち世界的に分散するOLTP、OLAPデータベースが開発された。これは、Googleの要求するスケーラビリティと信頼性を満たせない、シャーディングされたMySQLの実装を置き換えるものとして設計された。</p> 
  </blockquote> 
  <p align="left">このようなNewSQLのソリューションのひとつに<a href="http://www.memsql.com/">MemSQL</a>がある。これは完全なインメモリソリューションで構造化データや準構造化データ(JSON)のリアルタイム分析に使われる。列指向のデータストアではないが、素早くデータアクセスするために“ロックフリーのスキップリストとロックフリーのハッシュテーブル”を使っている。また、シェアード・ナッシング・アーキテクチャ上での並列処理を採用している。</p> 
  <p align="left">また、<a href="http://www.clustrix.com/">ClustrixDB</a>もNewSQLの一種と言えるだろう。ピアツーピアのシェアード・ナッシング分散データベースで、トランザクション処理やリアルタイム分析に利用される。ClustrixのCEOであるRobin Purohit氏によれば、ClustrixDBは<a href="http://www.twoo.com/">Twoo.com</a>で日に44億トランザクションを処理し、21ノード(1ノード8コアで48GBのメモリ)で平均して5ミリ秒から10ミリ秒の遅延しか発生していないそうだ。</p> 
  <blockquote> 
   <p>単一の調整者がない、ピアツーピアの分散SQLデータベースをスクラッチで開発しました。ClustrixDBは分散トランザクションをPaxosコンセンサスプロトコルを使って実現しています。また、書き込みと分散化されたマルチバージョン並列コントロールのために2フェーズロッキングを使って読み込みと書き込みが干渉しないようにしています。これによって、単一ノードのデータベースの厳密なACID属性を分散環境で実現できるのです。</p> 
   <p>ClustrixDBはシェアード・ナッシング・アーキテクチャを使っています。リニアにスケールできる唯一のアーキテクチャです。ClustrixDBはいままではデータウェアハウスでしか実現できなかったリアルタイム分析を実現するために大規模並列処理(Massively Parallel Processing,MPP)を行います。</p> 
  </blockquote> 
  <p align="left">Twoo.comのCTOであるToon Coppens氏に最初に使ったMySQLソリューションはなぜ成功しなかったか、NewSQLを選んだのはなぜか、話を聞いた。</p> 
  <blockquote> 
   <p>数百のMySQLを使っていた<a href="http://netlog.com/">Netlog.com</a>で学んだように、シャードをリバランスしたり管理したりするオーバーヘッドや、クエリの変更の柔軟性のなさを考えると、MySQLを使うのは好ましい方法ではないように思えました。データが問い合わせ可能な1カ所にあることが好ましいのです。</p> 
   <p>NoSQLはスケーラビリティを提供してくれますが、普通は隠蔽されている低いレベルのデータ形式を直接扱うのは避けたかったのです。データレイヤをリフォームする必要はなく、柔軟に変更できる製品を求めていました(Clustrixは重い負荷がかかっているときに素早く変更できます)。</p> 
  </blockquote> 
  <p align="left">NoSQLは性能やスケーラビリティ、可用性に優れているが、開発とデータリファクタリングの努力はSQLを使うデータベースより大変そうだ。それゆえ、NewSQLというNoSQLの利点にSQLの力を組み合わせたソリューションが生まれたのだろう。最終的に問題になるのはニーズを満たすソリューションを使うということだ。</p> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
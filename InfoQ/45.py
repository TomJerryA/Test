<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>CQRSフレームワークのAxon 2がMongoDBをサポート，パフォーマンスも向上</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/axon-2-release;jsessionid=BED7CE2209035AB822CE7DB06D048DF0"><em>原文(投稿日：2013/03/19)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><span lang="SV"><span lang="EN-GB"><font color="#0000ff"><a target="_blank" href="http://www.axonframework.org/">Axon</a></font></span></span> の <a target="_blank" href="http://martinfowler.com/bliki/CQRS.html">CQRS</a> フレームワークの最新バージョンでは，<a target="_blank" href="http://www.mongodb.org/">MongoDB</a> をバックストアとして使用する <a target="_blank" href="http://www.axonframework.org/docs/2.0/repositories-and-event-stores.html#d4e1032">MongoEventStore</a> がサポートされている。さらにAPIがシンプルなものになり，パフォーマンスも向上している。先日リリースされたこの <a target="_blank" href="http://www.axonframework.org/news/axon-2-0-released/">バージョン2.0</a> は，イベントオブジェクトがPOJOベースになると同時に，メッセージやペイロード，メタデータを定義するアノテーションも備えている。その他の新機能は次のようなものだ。</p> 
 <ul> 
  <li>高性能なコマンドバス。ロックレスアルゴリズムを使用して並列的にコマンドを処理することにより，単位時間あたり４倍以上のコマンドを処理できるようになった。</li> 
  <li>イベントのシリアライズ実行が１度だけであること，イベントが実際に使用される場合にのみデシリアライズされることを保証するロジック。</li> 
  <li>多数のイベントを対象とするリプレイの大幅な高速化。</li> 
  <li>複数のマシンへの水平スケーリングと各マシンの負荷調整が可能な分散コマンドバス。</li> 
  <li>イベントのアップキャストと <a target="_blank" href="http://blog.trifork.com/2012/04/17/refactoring-in-an-event-sourced-world-upcasting-in-axon-2/">逆多重化</a> のサポート。新たなイベントを実装した後に，以前のイベントを複数の新イベントに変換する処理などが可能になる。</li> 
  <li>分散イベントに <a target="_blank" href="http://www.amqp.org/">AMQP</a> (Advanced Message Queuing Protocol) を使用可能。</li> 
 </ul> 
 <p>リリースに合わせて，Axonベースのシンプルなシステムを構築するためのステップが <a target="_blank" href="http://www.axonframework.org/axon-2-quickstart-guide/">クイックスタートガイド</a> として公開された。また，フレームワークの変更を反映して <a target="_blank" href="http://www.axonframework.org/docs/2.0/single.html">リファレンスガイド</a> もアップデートされている。</p> 
 <p>このフレームワークでは，CQRS (Command Query Responsibility Segregation) と <a target="_blank" href="http://martinfowler.com/eaaDev/EventSourcing.html">イベントソーシング</a> という，２つのアーキテクチャ・パターンをベースとしたシステムのビルディングブロックを提供している。いずれも今，注目を集めつつあるパターンだ。<a target="_blank" href="http://domaindrivendesign.org/books/evans_2003">DDD reference book</a> の著者であるEric Evans氏らの運営するDDD(Domain-Driven Design)コミュニティのWebサイトには，その重要性が特に <a target="_blank" href="http://domaindrivendesign.org/">指摘されている</a>。</p> 
 <p>&quot;CQRSとイベントソーシングの２つは，非常に密接な関連を持ったDDDへのアーキテクチャ的アプローチです。DDDに関しては，ここ数年で一番ホットな話題でしょう。&quot;</p> 
 <p>Axon Framework は <a target="_blank" href="http://blog.trifork.com/author/allard/">Allard Buijze</a> 氏が設立したオープンソース製品である。Apache License バージョン2.0 によってライセンスされ，有償サポートも選択できる。</p> 
 <p>約200名のメンバを持つAxon ユーザ <a target="_blank" href="https://groups.google.com/forum/?fromgroups=#!forum/axonframework">フォーラム</a> には，これまでに約300のトピックがある。 <a target="_blank" href="http://stackoverflow.com/questions/9646884/real-life-experience-with-the-axon-framework">実務上の経験</a> に関する議論からは，フレームワークに対して肯定的，否定的の両方のフィードバックのあることが確認できる。<br /> &nbsp;</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
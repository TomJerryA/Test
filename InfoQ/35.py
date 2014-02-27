<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Elasticsearch 1.0.0リリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/elasticsearch_1.0.0_released"><em>原文(投稿日：2014/02/14)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>オープンソースアナリティクスツールであるElasticsearchのバージョン1.0.0が<a href="http://www.elasticsearch.org/blog/1-0-0-released/">リリース</a>された。Elasticsearchはビッグデータ環境でのリアルタイム分析を実現する分散検索エンジンだ。<a href="http://lucene.apache.org/">Apache Lucene</a>を利用し、ReST APIを公開することで実現している。HTTP経由で直接アクセスできる以外に、Java、JavaScript、Pythonなどの言語向けのライブラリからもアクセスできる。また、<a href="http://hadoop.apache.org/">Apache　Hadoop</a>とも統合できる。Elasticsearchはすでに大規模データを扱っている企業で採用されている。GitHub、Foursquare、SoundCloudといった企業だ。</p> 
  <p>Elasticsearchは拡張性、高可用性、リアルタイム分析の3つに注力している。データはすぐにインデックスされ、クラスタ内で複製され、分析できる状態になる。</p> 
  <ul> 
   <li><strong>拡張性:</strong> Elasticsearchはクラスタ環境で動作するよう設計されている。ノードがスタートするとすぐに、ノットワーク上の他のノードを探して接続する。インデックスはシャード内に作成され、クラスタ上に分散されるので、インデックスの検索は分散処理になり、並列で行われる。性能が必要な場合はノードをさらに追加するだけで自動的にシャードが再構成される。</li> 
   <li><strong>可用性:</strong> データベースシャードは水平的なスケーリングだけでなく、可用性のためにも使われている。各シャードは異なるクラスタに保存されているので、ノードが落ちても、データは失われない。動作不良になったノードはElasticsearchが検知してクラスタから除外する。除外した後、シャードは弾力性と拡張性を考慮して再構成される。<br /> 全クラスタの再起動をサポートするため、Elasticsearchに必要なすべてのメタデータはさまざまなストレージ上に保存されている。データはゲートウェイと呼ばれる仕組みを使って保存される。ゲートウェイは現時点ではローカルのストレージか共有ファイルシステムをサポートする。</li> 
   <li><strong>リアルタイム:</strong> Elasticsearchはスキーマにとらわれない。任意のJSONドキュメントを保存できる。ドキュメントの構造は分析される。タイムスタンプのようなデータ型ですら自動的に検知される。既定では、ドキュメントに含まれるすべてのフィールドがインデックスされ検索可能になる。単純な全文検索、ファセットがインデックスに適用される。ファセットとは分析関数でバケッティング(データの幅、距離、ヒストグラムなど)とメトリクス(合計、平均、統計値など)を提供する。</li> 
  </ul> 
  <p>&nbsp;</p> 
  <h3>Elasticsearch 1.0.0の新しい機能</h3> 
  <p>バージョン1.0.0はさまざまな関数の強化とAPIの変更が行われており、Elasticsearchがより直感的に使えるようになっている。また、インデックスのバックアップ、復元、データの分析、Elasticsearchの弾力性の強化などの機能が搭載されている。</p> 
  <ul> 
   <li><strong>スナップショット/リストア:</strong> 新しいバージョンでは、クラスタ全体のスナップショットを取り、バックアップを作成できる、シンプルなAPIがある。メタデータとインデックスを含む、Elasticsearchのクラスタ全体をスナップショットリポジトリに保存できる。組み込みのフェイルオーバシステムが正常に動作しない場合、クラスタをスナップショットから復元できる。</li> 
   <li><strong>アグリゲーション:</strong> アグリゲーションによって、バージョン1.0.0以前のファセットよりも強力なデータ分析ができる。ファセットは分析関数の結果だけを提供するが(例えば、ある距離に含まれている店舗の数)、アグリゲーションは特定の問い合わせでどのドキュメントが見つかったかを保持し、新しい問い合わせのインプットにそれらのドキュメントを利用できる(例えば、ある距離に含まれている店舗の四半期の平均売り上げ)。</li> 
   <li><strong>サーキットブレーカー:</strong> サーキットブレーカーは検索インデックスに致命的な被害を与える処理エラーや実行エラーを回避するために追加された。Elasticsearch1.0.0に追加された最初のセーフガードはフリーメモリを監視し、検索と分析に必要なメモリ量を見積もる仕組みだった。検索や分析に必要なメモリが利用できるメモリを上回るとき、処理をブロックしてOutOfMemory例外が発生しないようにする。将来のリリースではより多くの種類のサーキットブレーカーが追加される予定。</li> 
  </ul> 
  <p>&nbsp;</p> 
  <p>Elasticsearchはメジャーバージョンを変え、既存のAPIをきれいに整理した。後方互換性は維持されていない。バージョン1.0.0にアップグレードする前に、ユーザは<a href="http://www.elasticsearch.org/guide/en/elasticsearch/reference/1.x/breaking-changes.html">破壊的な変更</a>一覧にあるすべてのデータをバックアップする必要がある。</p> 
  <p>またElasticsearchはデータのキャプチャと分析に使えるツールも提供している。<a href="http://www.elasticsearch.org/overview/logstash">Logstash</a>と<a href="http://www.elasticsearch.org/overview/kibana">Kibana</a>を使うと、Elasticsearchは<a href="http://www.infoq.com/news/2014/02/">ELK-stack</a>として使え、ログファイルを解析し、分析しさまざまな方法で視覚化できる。<br /> また、<a href="http://www.elasticsearch.com/">商用ブランチ</a>経由でサポートを購入することもできる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
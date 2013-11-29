<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ActiveMQ 5.9：LevelDB ストアのレプリケーション、およびHawtio ウェブコンソールに対応</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/activemq-5-9-release"><em>原文(投稿日：2013/11/07)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>最新版の<a href="http://activemq.apache.org/">Apache ActiveMQ</a><a href="http://en.wikipedia.org/wiki/Message_broker">メッセージブローカ</a>は<a href="http://activemq.apache.org/leveldb-store.html">LevelDB データストア</a>のレプリケーション機能をサポートし、さらに新しい <a href="http://hawt.io/">Hawtio</a> ウェブコンソールを含んでいる。前回のリリースから８ヶ月経過した最新リリースのバージョン5.9 には、以下のような新しい機能と改良が含まれている。</p> 
  <ul> 
   <li><a href="http://activemq.apache.org/replicated-leveldb-store.html">レプリケーション対応の LevelDBデータストア</a>は、キー・バリュー型のファイルベースの永続化<a href="https://code.google.com/p/leveldb/">データベース</a>である。レプリケーションは<a href="http://zookeeper.apache.org/">Apache ZooKeeper</a> を使って行う。ここではブローカノード群から一つのマスターを選び、そのマスターブローカから残りのブローカにすべての更新情報を複製することで同期を実行する。</li> 
   <li>新しいブローカプラグインは、ブローカのXML設定の部分的な変更に対応した。これによりリスタートなしで設定変更を反映させることが可能となり、ダウンタイムを避ける事ができる。ただし、いつくかの設定項目についてはブローカのリスタートが必要となるものがまだ残っている。</li> 
   <li>Howtio ウェブコンソールはプラグイン対応の管理用 HTML5ウェブコンソールである。JVMをサポートしており、ActiveMQや、<a href="http://camel.apache.org/">Camel</a>, <a href="http://tomcat.apache.org/">Tomcat</a> などの多数のプラグインに対応している。このコンソールのサーバ側は <a href="http://jolokia.org/">Jolokia</a> に依存している。Jolokia は、HTTP上のJSON 通信をベースにした JMXとHTTPのブリッジである。旧版のコンソールはまだ可動しているが廃止予定である。</li> 
   <li><a href="http://en.wikipedia.org/wiki/WebSocket">WebSocket</a>上の<a href="http://mqtt.org/">MQTT</a>プロトコルによる、遠隔監視トランスポートをサポート。</li> 
   <li>Apache Camel ブローカコンポーネントを ActiveMQ内部の Camel 機能のために利用。</li> 
   <li>マスターノードのステータス情報をロストした際のブローカの自動再起動に対応。</li> 
   <li>LevelDBと AMQP の強化。</li> 
  </ul> 
  <p>開発チームは、これらの新しい機能とともに<a href="https://issues.apache.org/jira/secure/ReleaseNote.jspa?projectId=12311210&amp;version=12323932">２００</a>以上もの課題を解決している。そのほとんどはバグフィクスと改良であり、そのバグの多くは深刻なものであった。<br /> <a href="http://activemq.apache.org/amq-message-store.html">AMQメッセージストア</a>は廃止され今後使われることはない。</p> 
  <p>Apache Software Founation のコミッター、Christian Posta 氏は、<a href="http://www.christianposta.com/blog/?p=326">これらの新しい機能について</a>デモやビデオを交えたブログ記事を公開している。</p> 
  <p>Apache ActiveMQ は、オープンソースのメッセージ処理、および<a href="http://www.enterpriseintegrationpatterns.com/index.html">エンタープライズ統合パターン</a>を完全にサポートした統合パターンサーバである。<br /> <a href="http://activemq.apache.org/apollo/">ActiveMQ Apollo</a> は新しいメッセージブローカであり、『ActiveMQ の次世代メッセージング機構』と呼ばれ、ActiveMQ基盤によって構築されたものである。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Hadoop-as-a-Service提供のQuboleがGoogle Compute Engine上で稼働可能に</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/qubole-on-gce"><em>原文(投稿日：2013/12/28)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>マネージドHadoop-as-a-Serviceを提供する<a href="http://www.qubole.com">Qubole</a>がGoogle Compute Engine (GCE)上で<a href="http://googlecloudplatform.blogspot.com/2013/12/qubole-helps-you-run-hadoop-on-google-compute-engine.html">利用可能となった</a>。QuboleはこれまでAmazon社のAWS上のみで<a href="http://www.qubole.com/company/partners/">利用可能</a>だったが、この発表は<a href="http://www.infoq.com/news/jp/2013/12/gcega">Google Compute Engineの一般提供</a>が開始されたほんの数日後に行われた。</p> 
  <p>コニュニティの反応は概して好調で、皆<a href="http://nosql.mypopescu.com/post/69829120078/google-compute-engine-and-data">ビッグデータのテーマ</a>をGCEの<a href="http://gigaom.com/2013/12/13/maybe-big-data-is-the-killer-app-for-googles-cloud/">キラー・アプリケーションとなる見込みがある</a>と見なしているようだ。DataStax社のAlex Popescu氏はこのように見ている。</p> 
  <blockquote>
   Google Compute Engineに関連する各社の発表を見ていると、あるテーマに気付くだろう。OLTPにはDataStax社のCassandra/DSE, ストリーム処理にはDataTorrent, HadoopにはQubole, HadoopライクなソリューションにはMapR…など、あらゆる角度からデータを扱うということだ。この流れを見ていると、Google Compute EngineはAmazon Web Servicesの強力なライバルとなるであろうことが伺える。
  </blockquote> 
  <p>Hadoop-as-a-Service（HaaS、またはクラウド上のHadoop）と並ぶ選択肢は下記のようになる。</p> 
  <ul> 
   <li>GCEやEC2のようなIaas環境にてApache Hadoop, もしくはCloudera, Hortonworks, MapRなどのディストリビューションをインストールする、独自でのデプロイ管理。稼働しているものに対するきめ細やかなコントロールが可能だが、デプロイや管理の複雑性を伴う。</li> 
   <li>デプロイ時の複雑性の軽減に役立ち、インストールされたサービス上での中間レベルの制御を提供する、Amazon社のEMRやSavvis社の提供するBig Dataサービスのようなプレパッケージ型サービス。</li> 
   <li><a href="https://vimeo.com/80872062">デプロイや管理の複雑性を軽減することが期待できる</a>、Quboleや<a href="http://mortardata.com/">Mortar</a>のようなマネージドHaaS</li> 
  </ul> 
  <p>HaaSとオンプレミスデプロイの<a href="https://vimeo.com/80872062">決定的な違い</a>は、融通性、スポット価格、処理とストレージ（たとえば、Amazon社のS3や<a href="https://cloud.google.com/products/cloud-storage/">Google社のCloud Storagee</a>のような一貫性のあるオブジェクトストア）との分離、そしてセキュリティ基準の強化にある。QuboleのようなマネージドHaaSは開発時に、評価やテスト、短時間解析ジョブやハイブリッドクラウドセットアップを実現する用途で<a href="https://vimeo.com/80872062">よく利用される</a>。しかし、下記のような独自の制限もある。</p> 
  <ul> 
   <li>クラウドへのデータ投入とデータ再出力は独自価格となる</li> 
   <li>法的要件に起因するプライバシーとデータ保護の問題がユースケースを防止または制限する可能性がある</li> 
   <li>TCOの24時間オペレーションは個々の状況に応じて判断する必要がある</li> 
   <li>Hadoop, Hive等と一貫性のあるオブジェクトストアとの間に一般的な不整合が存在する</li> 
  </ul> 
  <p>Ashish Thusoo氏とJoydeep Sen Sarma氏はFacebook在職中にデータインフラストラクチャチームを管理し、HadoopとHiveを稼働させる経験を積んだ。その後2012年6月にQuboleを立ち上げ、2013年4月には<a href="http://gigaom.com/2013/04/23/hadoop-startup-qubole-raises-7m-for-hive-as-a-service/">シリーズAラウンドで700万ドルもの資金調達を受ける</a>までに至った。Joydeep氏はHive London Meetupでの講演「<a href="http://sdrv.ms/11XQ5K6">クラウドフレンドリーなHadoop &amp; Hive</a>」にて、HaaS提供を実施するにあたって直面した課題とその内部についての見識を掘り下げて分析している。さらに、Christian Prokopp氏（Rangespan社のデータサイエンティスト）は最近、詳細な概要報告と、QuboleとEMRの比較について<a href="http://www.bigdatarepublic.com/author.asp?section_id=2840&amp;doc_id=266304">まとめている</a>。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
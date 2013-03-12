<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>スケーリングに関する段階的考察</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Insight-Phases-Scaling;jsessionid=FE20639EEF9306AF6283196AF1ACB7C8"><em>原文(投稿日：2013/03/05)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Christopher Smith氏は先月，<a target="_blank" href="http://www.socallinuxexpo.org/scale11x">Scale 11x</a> で行なった &quot;<a target="_blank" href="http://www.socallinuxexpo.org/scale11x/presentations/five-stages-scale">スケールの５段階 (The Five Stages of Scale)</a>&quot; と題するプレゼンテーションで，Webアプリケーションのスケーリング問題解決に関する自身の考察を披露した。プレゼンテーションの中で氏が論証したのは，明確に定義されたコンポーネントを追加，あるいは最適化する段階的なスケーリングによって，Webアプリケーション全体の規模を拡大するアプローチだ。ロードバランシングからUDPプロトコルの最適化利用にまで及ぶ幅広い話題で，氏は参加者を <a target="_blank" href="http://www.socallinuxexpo.org/sites/default/files/presentations/SCALE11.pdf">有益な情報に満ちた快適な旅</a> へと招待した。</p> 
 <p class="MsoNormal">スケーリングアーキテクチャの基本としてもっとも重要なのは，ロードバランサの背後にあるWebアプリケーションサーバの増設が可能であることだ。ロードバランサが要求やセッションをアプリケーションサーバ間に振り分けることで，Webアプリケーションのリニアなスケーリングが現実のものになる。このテクニックが使えれば，アプリケーションサーバの増設によってリニアにスケールを拡大することができるが，しかし <a target="_blank" href="http://www.facebook.com/pages/C10k-problem/120373131343187">C10K(クライアント１万台)問題</a> を避けることはできず，単に先延ばしされるだけだ。サーバを増やしても個々の要求に対する応答性が向上するわけではない，というのがその理由だ。</p> 
 <p class="MsoNormal">次に氏は，キャッシュシステムを使用したスケーリングについて説明した。Webアプリケーションの前段に設置したキャッシュ上で参照要求を処理する，という方法である。複数のキャッシュシステムを組み合わせて使用することで，最大限のスケール効果が得られる。また，Memcacheなどのサーバを導入して <a target="_blank" href="http://www.infoq.com/news/2007/11/cfrp;jsessionid=9A3A6047647A882481DE0825939A5005;jsessionid=FE20639EEF9306AF6283196AF1ACB7C8">データをメモリ内に格納しておけば，アプリケーションサーバによる検索の高速化が可能になる</a>。ロードバランサの前段にリバースプロキシを配置してキャッシュされたリソースを提供する，という方法も有効だ。さらにCDN (Content Delivery Network) を使って，キャッシュされたリソースをよりエンドユーザの近くに配置することも考えられる。ただしデータ更新に関して言えば，キャッシュによる効果は限定的なものだ。</p> 
 <p class="MsoNormal">更新処理のスケール性を新たな段階まで引き上げるためには，永続化フレームワークを最適化して使用する方法が有効である。氏の説明によれば，このフェーズでの成功と先程説明した内容を組み合わせれば，ほとんどの人にとって十分なものになるはずだ。アプリケーションのデータ構造に適した <a target="_blank" href="http://cloud.dzone.com/news/sql-vs-nosql-cloud-which">SQLデータベースあるいはNoSQLデータベースを選択</a> することで，スケール性はさらに大きく向上する。さらに参照／更新の並列性を確保できれば，更新操作のスループットと応答性の向上に寄与するだろう。その上で &quot;<a target="_blank" href="http://www.techopedia.com/definition/23949/atomicity-consistency-isolation-durability-acid">ACID (特にCとD)</a> をうまくごまかす&quot; ことができるならば，更新処理のさらなる高速化も不可能ではない。</p> 
 <p class="MsoNormal">このようなスケーリング技術の土台となるのが，Webアプリケーションによるデータ参照／更新のレイテンシの最小化だ。ここまで説明して氏は，コンピュータにおける <a target="_blank" href="http://norvig.com/21-days.html#answers">さまざまな処理のレイテンシ</a> を披露した。</p> 
 <ul> 
  <li>L1 キャッシュ参照 – 0.5 ns</li> 
  <li>分岐予測ミス – 5 ns</li> 
  <li>L2 キャッシュ参照 – 7 ns</li> 
  <li>ミューテックスのロック／アンロック – 25 ns</li> 
  <li>メインメモリ参照 – 100 ns</li> 
  <li>1KバイトのZip圧縮 – 3,000 ns</li> 
  <li>1Gbpsネットワーク上の1Kバイト送信 – 10,000 ns (0.01 ms)</li> 
  <li>SSDから 4K のランダム読み込み – 150,000 ns (0.15 ms)</li> 
  <li>メモリから 1MB の順次読み込み – 250,000 ns (0.25 ms)</li> 
  <li>同一データセンタ内のラウンドトリップ時間 – 500,000 ns (0.5 ms)</li> 
  <li>SSDから 1MB の順次読み込み – 1,000,000 ns (1 ms)</li> 
  <li>ディスクシーク時間 – 10,000,000 ns (10 ms)</li> 
 </ul> 
 <div>
  以降のプレゼンテーションでは，さらに高度なスケーリングフェーズの話題が取り上げられた。
 </div> 
 <ul> 
  <li>データではなく，コモディティサーバを使用してコードを受け渡す方法: <a target="_blank" href="http://www-01.ibm.com/software/data/infosphere/hadoop/mapreduce/">Map/Recude (Hadoop)</a>，DHT，(Cassandra，HBase，Riak)</li> 
  <li>データパーティションを経由してデータをルーティングする方法: <a target="_blank" href="http://www.complexevents.com/2006/08/01/what%E2%80%99s-the-difference-between-esp-and-cep/">ESP/CEP</a>，Eigen，Storm，Esper，StreamBase，0mqなど</li> 
  <li>TCPに代えてUDPを使用する方法</li> 
 </ul> 
 <p style="margin-bottom: 0pt" class="MsoNormal">このような高度なテクニックのほとんどは，ハイパースケールなWebアプリケーションを管理する企業で導入されているものだ。例えば <a target="_blank" href="http://www.facebook.com/note.php?note_id=39391378919">Facebookでは，Memcached で毎秒数十万のリクエストを処理するためにUDPを使用している。</a></p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
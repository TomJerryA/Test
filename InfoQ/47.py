<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Googleが新開発のCloud Storage ConnectorでHadoopパフォーマンスを改善</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/google-hadoop"><em>原文(投稿日：2014/01/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Hadoopを使ったビッグデータ処理は現在，さまざまなクラウド環境上で行われている。しかしGoogleは，ストレージサブシステムへの投資によって，そこから一歩抜き出ようとしている。同社が新たに開発したコネクタを使えば，従来の分散ファイルシステムに代えて，Google Cloud Storage上でHadoopを直接実行できるようになるのだ。これにより，ストレージコスト低減とデータレプリケーション数の削減が実現できると同時に，プロセス全体がこれまでより簡略化される。</p> 
  <p><a href="http://research.google.com/archive/gfs.html" target="_blank">2003年にGoogle File System</a>の，<a href="http://research.google.com/archive/mapreduce.html" target="_blank">2004年にはMapReduce</a>の研究成果を発表して以来，GoogleはHadoopにおいてひとつの役割を果たしてきた。同社の商用Hadoopサービスである<a href="https://developers.google.com/hadoop/" target="_blank">Hadoop on Google Cloud Platform</a>には，&quot;Googleインフラストラクチャに最適化されたセットアップスクリプトとソフトウェアライブラリのセット&quot; という<a href="https://developers.google.com/hadoop/" target="_blank">説明がある</a>。Hadoopジョブでは，<a href="https://hadoop.apache.org/docs/r1.2.1/hdfs_user_guide.html" target="_blank">HDFS (Hadoop Distributed File System)</a>の動作するローカルディスクベースのストレージを使用するのが一般的である。しかしこの新しい<a href="https://developers.google.com/hadoop/google-cloud-storage-connector" target="_blank">Google Cloud Storage Connector for Hadoop</a>では，それを簡略化しようとしている。このコネクタを使うことで，データをHDFSストアにコピーしなくても，Google Cloud Storage上でHadoopを直接実行することが可能になるのだ。<a href="https://developers.google.com/storage/" target="_blank">Google Cloud Storage</a> – ベースとなっているのは<a href="http://static.googleusercontent.com/media/research.google.com/en/us/university/relations/facultysummit2010/storage_architecture_and_challenges.pdf" target="_blank">Colossus</a>という同社の最新ストレージ技術である – は，大容量データの保存を目的とした高可用性オブジェクトストレージサービスで，米国と欧州のデータセンタで提供されている。</p> 
  <p><a href="http://googlecloudplatform.blogspot.com/2014/01/easier-faster-lower-cost-big-data-processing-with-the-google-cloud-storage-connector-for-hadoop.html" target="_blank">コネクタ発表のブログポスト</a>中でGoogleは，Hadoop処理において，HDFSに代えてGoogle Cloud Storageを使用することのメリットをいくつも説明している。ジョブ開始の高速化，データ可用性の向上，データコピーの減少によるコスト削減，Hadoopクラスタ削除後のデータ維持，ファイルシステムのメンテナンス作業の排除，総合的なパフォーマンス向上といった具合だ。</p> 
  <p>Hadoopのパフォーマンスは，AccentureのTechnology LabsがGoogle Cloud Platformブログに寄せた<a href="http://googlecloudplatform.blogspot.com/2014/01/performance-advantages-of-the-new-google-cloud-storage-connector-for-hadoop.html" target="_blank">ゲスト記事</a>の中心的な話題だった。記事の中で同社は，新しいGoogle Cloud Storage Connector for Hadoopを試用して，その結果を公表している。Accentureでは，物理的なサーバとクラウド環境上のHadoopパフォーマンスを比較するために，ひとつのベンチマークを考案した。Google Compute Engine上の最初のセットアップは，Hadoopのベストプラクティスには沿っているが，かなり複雑なものだった。</p> 
  <blockquote> 
   <p>実験を行うために私たちは，Google Compute Engineインスタンスとローカルディスク，Hadoopクラスタ内でローカルHDFSとデータのコピー入出力を行うストリームMapReduceジョブを用意しました。</p> 
   <p>Figure 1に示すように，このデータフロー方法でベンチマーク用のデータを取得するには，追加的なコピー入出力フェーズを含んだすべてが実行時間として必要になります。実行時間の増加以外にも，このデータフローモデルでは，実験の起動や管理のために，かなり複雑なコードが必要になります。テストベンチスクリプトを修正して必要なコピー処理を加えなければなりませんし，修正したスクリプトが正常に動作することを確認するためのデバッグやテストの時間も確保しなければなりません。</p> 
  </blockquote> 
  <p>Googleから新しいコネクタを使ったテストを提案されたAccentureチームは，そのメリットを活用できるようにHdoopのセットアップを変更した。</p> 
  <blockquote> 
   <p>コネクタを導入することにより，データフローモデルを変更してコピー処理を不要にすることができました。Google Cloud Storageに直接アクセスしてデータを入力することや，出力データを書き込むことも可能になりました。</p> 
   <p>Figure 2はMapReduceジョブによる入力データの直接アクセスと，Google Cloud Storageへの直接書き込みを示しています。ストリームMapReduceジョブでコピーを行う必要はまったくありません。入出力コピーの削除による実行時間短縮だけではありません。入力データをGoogle Cloud Storageからアクセス可能になったことで，予想外のパフォーマンス的なのメリットもありました。既存のHDFSアクセスに比較して，入力データの可用性が向上したことで，実行時間をさらに短縮することができたのです。</p> 
  </blockquote> 
  <p>新しいコネクタは，Hadoopテスト全般で実行時間を大幅に短縮している。この結果はコピー入出力の不要化，ノード間の一環したデータ分散，データ転送の高速化によるものだ。最後にもうひとつ，リモートストレージがローカルストレージを性能的に凌駕するとは思われない，という意味から見て，極めて意外な結果がある。</p> 
  <blockquote> 
   <p>Google Cloud Storageが実現するリモートストレージのスケールと容量は，大容量のデータを移動し保存する上で，物理的なサーバでは実現できないユニークな方法を可能にします。</p> 
   <p>…</p> 
   <p>直感には反しますが，私たちの実験では，データの可用性向上を目的としたリモートストレージの方が，ローカルデータに依存するローカルディスクHDFSよりも，性能の面で優れていたのです。</p> 
  </blockquote> 
  <p>Accentureによる今回の調査は，Google Cloud Platform上のHadoop処理が性能価格比の面で物理的サーバより優れていることと同時に，クラウドサーバのパフォーマンスチューニングは複雑だが価値のある行為であることを示している。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>毎秒10億件以上のリアルタイムイベントを処理するDataTorrent 1.0</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/06/datatorrent"><em>原文(投稿日：2014/06/03)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="https://www.datatorrent.com/">DataTorrent</a>はリアルタイムストリーミングおよび解析用のプラットフォームである。毎秒10億件以上のリアルタイムイベントを処理することができる。</p> 
  <p><a href="https://blog.twitter.com/2013/new-tweets-per-second-record-and-how">Twitterの平均である毎秒～6,000ツイート</a>と比較すれば，先日リリースされた<a href="https://www.datatorrent.com/">Data Torrent 1.0</a>の持つ毎秒10億リアルタイムイベント以上というのは，ニーズをはるかに超えていることが分かる。DataTorrentは，256GBのRAMと12ハイパースレッドCPUコアを備えた<a href="https://www.datatorrent.com/scaling-up-event-ingestion/">ノード37台からなるクラスタを使用してテストを実施している</a>。その結果から同社では，CPUが飽和状態に達した時点において，毎秒16億イベントまでの直線的なスケーラビリティを達成したと報告している。DataTorrentの創設者のひとりであるCEOのPhu Hoang氏がInfoQに語ったところでは，同社のソリューションは，同じハードウェア上で動作するApache Sparkよりも&quot;桁違いに&quot;パフォーマンスが高いということだ。</p> 
  <p>DataTorrentはHdoop 2.xをベースに開発された，リアルタイムのフォールトトレラント・データストリーミングと解析のプラットフォームである。バッチプロセスなど，別タスクを行うアプリケーションとも共存可能なネイティブHadoopアプリを使用する。プラットフォームのアーキテクチャは下図のようなものだ。</p> 
  <p><a href="/resource/news/2014/06/datatorrent/ja/resources/datatorrent-arch-1.png" target="_blank"><img src="http://www.infoq.com/resource/news/2014/06/datatorrent/ja/resources/datatorrent-arch-1.png" _href="img://datatorrent-arch-1.png" _p="true" alt="" /></a></p> 
  <p>StrAM(Streaming Application Master)は論理DAG(Direct Acyclic Graph)の管理を担う，ネイティブなYARNアプリケーションマスタである。Hadoopクラスタ上で動作し，リソースの確保やパーティショニング，スケーラビリティ，スケジューリング，Webサービス，ランタイム変更，統計，SLA(Service Level Agreement)，セキュリティといった処理を行う。</p> 
  <p>ユーザアプリケーションはダイアグラムの上位レベルに位置し，<em>オペレータ</em>あるいは/または<em>テンプレート</em>に接続する。オペレータには例えば，InputReceiver – 入力データの受信をシミュレートする，Average – 指定された次元にあるキーのデータ平均を計算する，RadusAverageOutput - 計算した平均値をRedisデータストアに記録する，SmtpAvgOperator – 警告Eメールを送信する，といったものがある。これらのオペレータはいずれも<a href="https://github.com/DataTorrent/Malhar">Mahlhar</a>ライブラリの一部である。同ライブラリには400以上のアイテムが収納されていて，GitHubで公開されているものも多い。その他のオペレータも，必要に応じてユーザ自身で作成可能だ。</p> 
  <p>我々はHoang氏に，Data TorrentがSparkより高性能な理由を聞いた。</p> 
  <blockquote> 
   <p><strong>PH: </strong> アーキテクチャ上は大きな違いが２つあります。DataTorrentはストリーミングを通じて，リアルタイムなアクションを実行可能にすることを重視しています。それに対してSparkの要件は，ストリーム処理に対してSparkエンジンを汎用化することにあり，それが違いを生んでいるのです。注目すべき重要領域は，パフォーマンスとステートフルなフォールトトレランス，この2つです。</p> 
   <p>&nbsp;</p> 
   <p>1.パフォーマンス - DataTorrent RTSはパフォーマンスと高可用性を重視して，ネイティブなHadoop 2.0サービスとして基本部分から設計，開発されました。その結果が，イベント・バイ・イベントの処理における0.1秒単位のレイテンシに現れています。Data Torrent RTSは起動時にアプリケーションをHadoop上でスケジュールします。その後はアプリケーションが変更を要求するまでマッピングが固定されます。したがって，スケジュールによるオーバーヘッドは発生しません。一方のSparkはHadoop 2.0以前に開発されました。Sparkエンジンを使用して，多数の&quot;map reduce&quot;ジョブを小さなバッチないし&quot;ミニバッチ&quot;として効率的に実行します。このような設計判断のため，現在のSparkは (アプリケーションマスタを通じて) 個々のミニバッチをそれぞれクラスタ上で実行しなければなりません。これには非常に大きなオーバーヘッドを伴うため，システムをスローダウンさせています。</p> 
   <p>&nbsp;</p> 
   <p>2．ステートフルなフォールトトレランス - DataTorrent RTSは複雑で<i>ステートフルな計算処理</i>を，フォールトトレランス機能を備えながら高いパフォーマンスで実行できるように設計されました。これは企業において重要な要件です。機能停止状態から，データや状態を一切損失することなく回復できることは必須なのです。これに関するDataTorrent RTSの設計上の中心は，プログラム言語としてJavaを使用すること，エンタープライズ開発者と(開発者のDataTorrent RTSが扱う)ISVからフォールトトレラント設計の&quot;重荷&quot;を取り除くこと，この２つです。Sparkもフォールトトレランスを実行しますが，<i>対象とするのはステートレス処理のみです。</i>Sparkの設計上の中心は，関数型言語であるScala言語を使用すること，ストリームを処理するオペレータがステートレスであることです。Sparkにステートフルな処理を追加したければ，アプリケーションの一部としてそのようなコードを書く必要がありますが，これは難しい上に，パフォーマンスにも影響を与えるでしょう。</p> 
  </blockquote> 
  <p>Hoang氏によると，DataTorrentは &quot;オンプレミス，クラウドベースを問わず(Cloudera, Hortonworks, MapRなど，クラウドではAmazon AWSとGoogle Cloud)，すべての主要なHadoopディストリビュータでの動作を&quot; 保証するという。&quot;ユーザ企業に対して，摩擦を生じることなくHadoopベンダとデプロイメントオプションを変更可能にするフレキシビリティを実現します。&quot;</p> 
  <p>DataTorrentは有償製品だが，全機能を備えた小中規模アプリケーション用のものが無償で提供されている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>TwitterがMapReduceストリーミングフレームワークSummingbirdをオープンソースに</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/twitter-summingbird"><em>原文(投稿日：2014/01/16)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Twitterは，<a href="https://github.com/twitter/summingbird">Summingbird</a>と呼ぶ自社のMapReduceストリーミングフレームワークを<a href="https://blog.twitter.com/2013/streaming-mapreduce-with-summingbird">オープンソース</a>にした。Apache 2ライセンスで公開されるSummingbirdは，コードをバッチモード(Hadoop/MapReduceをベースとする)でもストリームモード(<a href="http://storm-project.net/">Storm</a>をベースとする)でも，あるいはハイブリッドモードと呼ばれる２つの組み合わせでも同じように実行することができる，大規模データ処理システムだ。</p> 
  <p>Twitterが<a href="http://strata.oreilly.com/2013/09/how-twitter-monitors-millions-of-time-series.html">5億を越えるツィート</a>を今後も処理し続けるためには，MapReduce(Pig/Scalding)とストリームベース(Storm)のコードを手動で統合する必要のある既存のスタックに代わるものを見つけなければならない。Summingbirdを開発した最大の動機は，Twitterのエンジニア達が<a href="https://blog.twitter.com/2013/streaming-mapreduce-with-summingbird">言及している</a>ように，Storm上で完全なリアルタイムシステムを動作させることが，次のような理由から困難である，という認識からだ。</p> 
  <ul> 
   <li>過去数ヶ月分の履歴ログを再計算するには，Hadoopによるコーディネートか，あるいは特別なログローディング機能を使用したStormを通じてストリーミングする必要がある。</li> 
   <li>メッセージパッシング重視であるStormでは，ランダム書き込みを行うデータベースのメンテナンスが難しい。</li> 
  </ul> 
  <p>このような洞察がSummingbirdという，既存のアプローチにおいて技術者たちが抱える実践的問題に対処する，柔軟で汎用性のあるソリューションへと結び付いたのだ。</p> 
  <ul> 
   <li>2つの異なるシステム間では，2組のアグリゲーションロジックを同期しなければならない</li> 
   <li>キーと値は，各システムおよびクライアントの間で一貫性を持ってシリアライズする必要がある</li> 
   <li>両方のデータストアからデータを読み取り，最終的な集計を実行し，組み合わせた結果を提供するのはクライアントの役割である</li> 
  </ul> 
  <p>Summingbirdは，オープンソース公開された<a href="http://lambda-architecture.net/">ラムダアーキテクチャ(Lambda Architecture)</a>準拠のシステムとして<a href="http://gigaom.com/2013/09/03/twitter-open-sources-storm-hadoop-hybrid-called-summingbird/">最初のもののひとつ</a>でもある。同様のプロジェクトとしてはYahooの<a href="http://developer.yahoo.com/blogs/ydn/storm-yarn-released-open-source-143745133.html">Storm-YARN</a>の他，スペインの新興企業が公開予定の<a href="http://www.slideshare.net/Datadopter/lambdoop-a-framework-for-easy-development-of-big-data-applications">Lambdoop</a>という，ラムダアーキテクチャ準拠の方法でビッグデータアプリケーションを開発するためのフレームワークなどがある。ラムダアーキテクチャの特徴 – 不変のマスタデータセット，バッチ・サービス・スピードの各レイヤ – により，バッチとストリーム処理のどちらも処理可能で，ソーシャルメディアプラットフォーム(TwitterやLinkedInなどのような)からモノのインターネット(スマートシティやウェラブル，製造業など)，さらには金融セクタ(不正検出やリコメンデーション)までをユースケースとして備えた，堅牢な大規模データ処理システムの構築が現実のものになる。</p> 
  <p>Summingbirdの中心的開発者たち – Oscar Boykin氏，Sam Ritchie氏(コンピュータ科学のレジェンドであるDennis Ritchie氏の<a href="http://www.wired.com/wiredenterprise/2013/11/twitter-summingbird/">甥</a>), Ashutosh Singhal氏 – はさらに，Summingbirdのロードマップを公開している。</p> 
  <ul> 
   <li>Apache <a href="http://spark.incubator.apache.org/">Spark</a>と列指向データストレージフォーマット<a href="http://parquet.io/">Parquet</a>のサポート</li> 
   <li>SummingbirdのProducerプリミティブ上での高度数学ライブラリや機械学習コードの開発</li> 
   <li>AlgebirdやStorehausなど，<a href="https://engineering.twitter.com/opensource/projects">関連するオープンソース</a>プロジェク との統合性向上</li> 
  </ul> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ビッグデータ技術を用いたグラフ処理</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/graph-bigdata-tapad"><em>原文(投稿日：2014/03/17)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>極度に大きなグラフの処理は現在でもなお難しい問題だ。しかし最近のビッグデータ技術の進歩は，このようなタスクをより実用的なものにしている。ニューヨークを拠点にクロスデバイスなコンテント配信を手掛けている<a href="http://www.tapad.com/">Tapad</a>はビッグデータを活用して，テラバイトサイズのデータにまで拡張可能なグラフ処理を，ビジネスモデルの中心とするスタートアップだ。</p> 
  <p>FacebookやTwitterなどソーシャルネットワークには，グラフ表現に適したデータが含まれている。一方でグラフは，Tapadのデバイスグラフのように，もっと不明確なデータの表現に使用することもできる。Tapadの共同創設者でCTOの<a href="http://www.tapad.com/team-member/dag-liodden/">Dag Liodden</a>氏は，デバイスの表現方法としてグラフが合理的である理由を，次のように説明する。</p> 
  <blockquote>
   Tapadではデバイス間の関係をモデル化するために，グラフ指向のアプローチを採用しています。このDevice Graph上では，匿名の識別子(クッキーIDなど)がノードとして表現されます。これらのノードを，マーケティング情報として追跡しているのです。ノード間のエッジには，決定論的データおよび統計的確率論モデルと機械学習技術とを組み合わせて，採点や重み付けが行われます。&quot;デバイス&quot;というコンセプトは，開始デバイス / ノード(例えばあるブラウザのクッキーID)とノードのコレクション(例えばタブレットとネット接続テレビのクッキーID)を使って，特定のエッジ制約のセットに到達可能な開始点，というように定義されるものです。単に情報をひとつのノードに集めるのではなく，実際のグラフ構造として保持することで，正確性と拡張性の動的なバランスをとる柔軟性が生まれるのに加えて，新たなエッジ推測モデルによるグラフの強化も容易になります。
  </blockquote> 
  <p>適切なツールを適切な作業に使用することは重要である。グラフ処理も同じことだ。氏が言うように，従来的なワークロードで処理可能なグラフであれば，ビッグデータ技術を使用する必要はまったくない。</p> 
  <blockquote>
   私にとって&quot;ビッグデータ&quot;とは，データの保存や解析が汎用的な既製ツールの小さなセットでは間に合わなくなり，個々のユースケースに合わせた技術を用いる必要が生まれる，その境界値のことです。ソフトウェアとハードウェアのソリューションの進化と成熟に伴って，この境界値は毎年移動しています。一方で私たちの扱うデータサイズや，実施すべき分析の高度化のレベルも同じように変わってきています。
  </blockquote> 
  <p>Facebookの場合，この境界値は一桁のペタバイトの位置にあると，<a href="http://www.sigmod.org/2013/">ニューヨークで行われた2013 ACM SIGMODカンファレンス</a>の<a href="http://borthakur.com/ftp/sigmod2013.pdf">提出資料</a>に詳述されている。 Tapadがグラフで扱うデータはこれよりも少ないが，それでも従来の方法で処理するのは不可能な量だ。</p> 
  <blockquote>
   米国のグラフには現在，携帯電話やタブレット，ノートPC，ゲーム機やTVなど，全部で11億ほどのノードがあります。中には一時的なノードもあります。例えばブラウザの非永続的なクッキーによるものなどは，データ量も少ないですしエッジもありません。一時的でないノードは平均で５つのエッジと，行動セグメントやそれに関連した500程度の固有情報を保持しています。ライブグラフのデータには数TBの容量があり，複数のデータセンタに渡って毎秒数十万回の読み取り／書き込みが行われています。最新のグラフデータは地理的に相互複製されます。各データセンタは現在，20TBのフラッシュSSDストレージと2TBのRAMを搭載したサーバ群で運用されています。
  </blockquote> 
  <p>大規模なグラフ処理に使用される技術の数は，ここ数年間で急増している。特に2013年には，いくつもの新技術がこのエコシステムに登場した。システムとして考えた場合，これらは２つのクラスに分類される。</p> 
  <ul> 
   <li>グラフデータのごく一部に少ない遅延で素早くアクセスする，OLTPワークロード用のグラフデータベース。</li> 
   <li>グラフの大半をバッチ処理可能な，OLAPワークロード用のグラフ処理エンジン。</li> 
  </ul> 
  <p>グラフデータベースにはすでに<a href="http://en.wikipedia.org/wiki/Graph_database#Graph_database_projects">多数の</a>製品があるが，さらにいくつかのプロジェクトが登場し，最近では差別化も行われている。<a href="http://www.neo4j.org/">Neo4j</a>はもっとも古く，もっとも成熟したグラフデータベースのひとつだが，<a href="http://stackoverflow.com/a/21566766/1332690">シャーディングをサポートしていない</a>ことによるスケール性の問題をいまだ残している。その他のデータベースでは，かなり新しい製品ではあるが，2013年に多くの支持を得るようになったのが<a href="http://thinkaurelius.github.io/titan/">Titan</a>だ。バックエンド非依存のデータベースとして<a href="https://hbase.apache.org/">HBase</a>，<a href="http://cassandra.apache.org/">Cassandra</a>などスケーラブルなアーキテクチャを活用可能であると同時に，最適化された頂点とエッジによる表現を内部で使用することにより，数十億のエッジまでスケール可能であると，<a href="http://thinkaurelius.com/2013/05/13/educating-the-planet-with-pearson/">2013年のブログ記事</a>には発表されている。</p> 
  <p>しかしながら，グラフ用の特別なデータベースは必須ではない。もっと汎用的でスケーラブルなNoSQLデータベースでも，問題に対する効果的なソリューションとなり得る。Googleの<a href="http://research.google.com/archive/bigtable.html">BigTable</a>をベースとして2011年にオープンソース公開された<a href="https://accumulo.apache.org/">Aapche Accumulo</a>は，大規模なグラフ保存に適した汎用データベースの一例である。柔軟なレコード構造によってグラフの型付きエッジやウェイトの保存が可能なこのデータベースは，NSAで実際に使用されている，と<a href="http://www.pdl.cmu.edu/SDI/2013/slides/big_graph_nsa_rd_2013_56002v1.pdf">2013年に出版されたテクニカルレポート</a>にはある。その他の例としては，Cassandraあるいは<a href="http://www.aerospike.com/">Aerospike</a>なども，適切なデータモデルを使用することで，グラフのエッジや頂点やウェイトのモデル化が可能だ。Facebookもまた，MySQLとMemcacheを使用した独自のソリューションを<a href="https://www.facebook.com/notes/facebook-engineering/tao-the-power-of-the-graph/10151525983993920">Tao</a>と呼ばれるシステム内に構築して，ユーザへのソーシャルグラフ提供に利用している。Tapadのデバイスグラフ設計でもこれと同じ原理を使用している，と氏はいう。</p> 
  <blockquote>
   トラバースと更新を高速化するため，ライブグラフはキーバリューストアに保存されています。また定期的にスナップショットグラフをHDFSに保存して，より複雑なグラフ処理や，他のデータストリームによる補填に使用できるようにしています。その結果は，後で&quot;ライブグラフ&quot;にフィードバックされます。グラフ専用のデータベースを使うことにもメリットはあります。ですが私たちは現在，キーバリューストアを用いた非常に高速かつシンプルなグラフのトラバースと，Hadoopの提供する低速だが非常にフレキシブルなトラバースと分析を併用する方法を採用しています – 現時点では，ですが。
  </blockquote> 
  <p>データベースに格納されたグラフを使用するにしても，実行可能なオペレーションは，おそらく参照や限定的なトラバースに限られるだろう。グラフの大部分をもっと複雑に解析するには，バッチ処理用の分散フレームワークが不可欠だ。<a href="http://graphlab.org/projects/source.html">GraphLab</a>フレームワークは，パフォーマンスを最大化するために<a href="http://en.wikipedia.org/wiki/Message_Passing_Interface">MPI (Message Passing Interface}</a>モデルを採用して，HDFS内のデータを対象とした複雑なアルゴリズムを大規模に実行可能としている。より新しい<a href="https://giraph.apache.org/">Apache Giraph</a>や<a href="https://hama.apache.org/">Apache Hama</a>などのフレームワークでは，Googleの<a href="http://googleresearch.blogspot.com/2009/06/large-scale-graph-computing-at-google.html">Pregel</a>プロジェクトで有名になった<a href="http://en.wikipedia.org/wiki/Bulk_synchronous_parallel">BSP(Bulk Synchronous Parallel)</a>パラダイムを基盤とする。さらに最新のエコシステムには，2013年に公開された<a href="https://spark.incubator.apache.org/">Spark</a>上で動作する<a href="https://amplab.cs.berkeley.edu/publication/graphx-grades/">GraphX</a>プロジェクトや，<a href="http://hadoop.apache.org/">Hadoop</a>を使って<a href="http://en.wikipedia.org/wiki/MapReduce">MapReduce</a>ジョブを実行し，Titanデータベース上でグラフ処理を行う<a href="http://thinkaurelius.github.io/faunus/">Faunus</a>などが加わっている。Tapadではオフライングラフデータの処理に，これら新しい技術を使用している。氏によれば，</p> 
  <blockquote>
   今のところ，グラフ処理フレームワークとしてはApache Giraphを中心に使用していますが，Spark GraphXやGraplabについても試験中です。これらのフレームワークはどれもかなり若いのですが，学習曲線の上昇率は非常に高く，いずれも長所と短所，注意すべき点があります。例えば，GiraphとGraphXにHadoopインフラストラクチャとの相性がよいという利点がある一方で，Graphlabはそのパフォーマンスそのものが非常に魅力的である，というようにです。
  </blockquote> 
  <p>OLTPとOLAPクエリの両方に対応可能な，統合的なフレームワークを提供しようとしているプロジェクトもある。<a href="http://lab41.co/">Lab41</a>の<a href="https://github.com/Lab41/Dendrite">Dendrite</a>は，そのようなプロジェクトのひとつだ。ストレージとプロセッシングにTitanとGraphLabを，ビジュアル処理に<a href="http://angularjs.org/">AngularJS</a>を使用する。2014年初めに発表されたばかりの非常に若いプロジェクトであるため，コミュニティの評価も限定的だが，すべてのユースケースをカバーしようという点が，今後の採用を後押しするに違いない。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
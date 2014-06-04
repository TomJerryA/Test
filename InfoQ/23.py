<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Cascading 3.0 が複数のフレームワークをサポート。 Concurrent Driven によるビッグデータアプリケーションの管理</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/driven"><em>原文(投稿日：2014/05/13)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p class="MsoNormal">ビッグデータアプリケーションを実装するにあたり、企業は<span style="mso-ascii-font-family:Calibri;mso-hansi-font-family:Calibri;mso-bidi-font-family:
&quot;Helvetica Light&quot;;color:#343434">Apache </span><a href="http://hadoop.apache.org/"><span style="mso-ascii-font-family:Calibri;
mso-hansi-font-family:Calibri;mso-bidi-font-family:&quot;Helvetica Light&quot;">MapReduce</span></a><span style="mso-ascii-font-family:Calibri;mso-hansi-font-family:Calibri;mso-bidi-font-family:
&quot;Helvetica Light&quot;;color:#343434">、Apache </span><a href="http://tez.incubator.apache.org/"><span style="font-family:&quot;Calibri Light&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:&quot;Times New Roman&quot;;
mso-hansi-theme-font:major-latin">Tez</span></a><span class="MsoHyperlink"><span style="font-family:&quot;Calibri Light&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;
mso-fareast-font-family:&quot;Times New Roman&quot;;mso-hansi-theme-font:major-latin"> </span></span><span style="mso-ascii-font-family:Calibri;mso-hansi-font-family:Calibri;mso-bidi-font-family:
&quot;Helvetica Light&quot;;color:#343434">、Apache </span><a href="http://spark.apache.org/"><span style="font-family:&quot;Calibri Light&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-fareast-font-family:&quot;Times New Roman&quot;;
mso-hansi-theme-font:major-latin">Spark</span></a><span style="mso-ascii-font-family:
Calibri;mso-hansi-font-family:Calibri;mso-bidi-font-family:&quot;Helvetica Light&quot;;
color:#343434"> あるいは Apache </span><a href="http://storm.incubator.apache.org/"><span style="mso-ascii-font-family:Calibri;mso-hansi-font-family:Calibri;mso-bidi-font-family:
&quot;Helvetica Light&quot;">Storm</span></a> など、数々のフレームワークを選ぶことができる。 <span class="MsoHyperlink"><span style="mso-ascii-font-family:Calibri;mso-hansi-font-family:Calibri;mso-bidi-font-family:
&quot;Helvetica Light&quot;;color:windowtext;text-decoration:none;text-underline:none">これらのフレームワークには一長一短があり、どれが最適かはアプリケーション次第である。全てのフレームワークを一つの Apache YARN クラスタで実行することは可能であるが、各フレームワークには少しづつ違ったプログラミングモデルがあり、互換性のない API を使わなければならず、アプリケーションをフレームワークからフレームワークへと移植するのは容易ではない。</span></span></p> 
  <p class="MsoNormal">Concurrent の主要製品であり、新製品でもある <a href="http://www.cascading.org/%20">Cascading 3.0</a> はこれらの問題の多くを解決する。Cascading は人気のある Java <a href="http://ja.wikipedia.org/wiki/%E3%83%89%E3%83%A1%E3%82%A4%E3%83%B3%E5%9B%BA%E6%9C%89%E8%A8%80%E8%AA%9E">ドメイン固有言語</a><span style="mso-spacerun:yes">&nbsp; </span>(DSL) の一つであり、MapReduce API を使用した大規模データワークフローのための関数プログラミングを定義し、実装するためのDSLとして２００７年後半に登場した。 Cascading は “配管” のイメージで、データのパイプラインを構築する: 構成要素はデータの流れを分配したり、合流したり、取り付けることができ、さらには演算処理を一連の流れとして実行することができる。</p> 
  <p class="MsoNormal">このためユーザは Cascading アプリケーションを<a href="http://ja.wikipedia.org/wiki/%E9%96%89%E8%B7%AF">閉路</a>を持たない<a href="http://ja.wikipedia.org/wiki/%E6%9C%89%E5%90%91%E3%82%B0%E3%83%A9%E3%83%95">有向グラフ</a> (DAG) として表すことができる。 これは Cascading の planner によって、元はMapReduceである基礎的なフレームワークに変換されたものである。</p> 
  <p class="MsoNormal">Cascading 3.0 は MapReduce 以上のものを提供する。企業の開発者はデータ処理をするアプリケーションを一度開発し、それを業務目的に最も適したフレームワーク上で実行することができる。 Cascading 3.0 がまずサポートするのは: ローカルのインメモリ、 Apache MapReduce ( Hadoop 1 と 2 どちらもサポートされる)、 そして Apache Tez である。 まもなくコミュニティの支援を用いて、 Apache Spark™、 Apache Storm その他のフレームワークが、プラグイン可能でカスタマイズできる新しい planner を通じてサポートされる予定である。</p> 
  <p class="MsoNormal">Cascading 3.0 から導入される新しい planner は、実行時にローカルトポロジに基づいたメタデータを用いてグラフの正確性を確認したり、グラフのノードをアノテートすることができる。　この planner はグラフを変換してノードを平衡化、挿入、削除及び並び替えをすることができる。 さらにはグラフを分割して、再帰的により小さい計算単位（例えば Map や Reduce ノード、あるいは Tez プロセス）に対応する部分グラフを探す。</p> 
  <p class="MsoNormal">一旦適切な計算単位が定義されると、Cascading は実行時の設定を構築する。これにはフレームワークの全てのAPI群を切り分ける jar （と Maven POM） が用いられる。これらの jar と POM は Cascading　が提供する。</p> 
  <p class="MsoNormal">Cascading 3.0 が実装するオープンでプラグイン可能な構造により、製品は容易にサポートするフレームワークを追加できるようになる。 これを行うには指定されたフレームワークとそのフレームワークに必要な jar や POM のための新しいルールセットを実装する。</p> 
  <p class="MsoNormal">Cascading 3.0 をオープンソースにしたのに加えて、Concurrent は最近商用製品 <a href="http://cascading.io/">Driven</a> を発表した。 これはリアルタイム監視や、運用のためのコントロール、そして Cascading アプリケーションのパフォーマンス管理機能を提供する。 Driven には次の機能をサポートするためにいくつかの画面がある:</p> 
  <ul> 
   <li>Understand – 実行中のデータ・アプリケーションをリアルタイムに可視化し、各処理をさらに視覚的に掘り下げる。</li> 
   <li>Diagnose – 失敗した処理（とその理由）や、パフォーマンスの悪いアプリケーションを素早く確認する。</li> 
   <li>Optimize – 視覚的にアプリケーションの処理状況を分析し、パフォーマンスの問題や異常を発見する。</li> 
   <li>Track – アプリケーションのリアルタイムなパフォーマンスを視覚化や、過去のデータとの比較をする。</li> 
  </ul> 
  <p class="MsoNormal">Concurrent の新しい製品によって、アプリケーションは Apache Tez 等の優れた新しいフレームワークへ移行しやすくなる。これによって企業はビジネスの要求に合う一つのAPIで標準化を行い、様々な業務上の問題に対処することができる。また、より新しく、より問題に適したビッグデータフレームワークを大量の書き直しをすることなく導入できる。Driven は新規及び既存のビッグデータアプリケーション運用状況を、開発から本番環境に至るまで可視化する。</p> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Java 8ニュース:新しいアトミックナンバーを含むRC版を公開、モジュール化は外れる</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/java8-release-candidates"><em>原文(投稿日：2014/02/16)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Java8の最初のRC版が2月の始めにリリースされた。<a href="http://mail.openjdk.java.net/pipermail/jdk8-dev/2014-February/003990.html">第1版</a>のb128は2月4日、第2版は1週間後にOpenJDKのメーリングリストで<a href="http://mail.openjdk.java.net/pipermail/jdk8-dev/2014-February/004005.html">発表された</a>。</p> 
  <p>Java 8 RC2は、新しいComparator APIの重大な不具合を修正している。新しい<em>thenComparing()</em>に不要な型制限があり、<a href="https://bugs.openjdk.java.net/browse/JDK-8033590">不具合報告</a>では次のように報告された。</p> 
  <blockquote>
    java.util.Comparatorの以下のメソッドでは、型のUはjava.lang.Comparableを継承しなければなりません。 
   <pre>
&lt;U extends Comparable&lt;? super U&gt;&gt; Comparator&lt;T&gt; thenComparing( 
  Function&lt;? super T, ? extends U&gt; keyExtractor, 
  Comparator&lt;? super U&gt; keyComparator);
</pre> しかし、keyComparatorは抽出されたkeyオブジェクトを比較するのに使われるため、この制限は不要です。
  </blockquote> 
  <p>Java 8 RC2では、Mac OS Xの<a href="https://bugs.openjdk.java.net/browse/JDK-8033642">readパーミッションの問題</a>も修正されている。Java 8 RC版は、<a href="https://jdk8.java.net/download.html">https://jdk8.java.net/download.html</a>からダウンロードできる。</p> 
  <p><a href="https://bugs.openjdk.java.net/browse/JDK/fixforversion/11815">JDK 8のバグトラッカー</a>によると、リリースは3月17日の聖パトリック祭の日だ。この記事を執筆している時点で、ドキュメントに関する3つの問題がまだ解決されていない。</p> 
  <p>もう1つのJava 8に関するニュースとして、Java 8のアトミックナンバーが相当速いことを示す数値を、最近、Drew Stephens氏が公表したことがある。また、Mark Reinhold氏は法律問題を引き合いに出し、モジュール化をJava 8から外すように提案した。</p> 
  <h2>新しいアトミックナンバーの実装</h2> 
  <p>Java 8のラムダ (<a href="https://jcp.org/en/jsr/detail?id=335">335</a>) と新しいDateとTimeのAPI (<a href="http://jcp.org/en/jsr/detail?id=310">JSR 310</a>) に加えて、マルチスレッドのアプリケーションの特定クラスにとって、とても重要なアトミックナンバーの実装がある。Palamino Labsの主任である<a href="http://www.linkedin.com/in/drewgstephens">Drew Stephens</a>氏は、最近、<a href="http://blog.palominolabs.com/?p=255">LongAdderとDoubleAdderについて追記した</a>。</p> 
  <blockquote> 
   <p>マルチスレッドのアプリケーションのあまり目立たないが、とても重要なクラスは、<a href="http://download.java.net/jdk8/docs/api/java/util/concurrent/atomic/LongAdder.html">LongAdder</a> と <a href="http://download.java.net/jdk8/docs/api/java/util/concurrent/atomic/DoubleAdder.html">DoubleAdder</a>、アトミックナンバーの実装です。<a href="http://download.java.net/jdk8/docs/api/java/util/concurrent/atomic/AtomicInteger.html">AtomicInteger</a> と <a href="http://download.java.net/jdk8/docs/api/java/util/concurrent/atomic/AtomicLong.html">AtomicLong</a>は、マルチスレッドで競合が起きたときに、優れたパフォーマンスを提供します。</p> 
   <p>Intel Xeon E5-2670の8つのコアすべてにアクセスできる<a href="http://aws.amazon.com/ec2/instance-types/instance-details/">m3.2xlarge EC2 インスタンス</a>を使ったベンチマークで、LongAdderとAtomicLongのパフォーマンスの違いを示します。</p> 
   <p><img src="http://www.infoq.com/resource/news/2014/03/java8-release-candidates/ja/resources/1graph.jpg" alt="" _href="img://1graph.jpg" _p="true" /></p> 
   <p>シングルスレッドでは、新しいLongAdderは3分の1遅くなりますが、スレッドがフィールドを増やそうと争っている場合、LongAdderはその価値を現します。各スレッドはただカウンタを増やそうとしているだけであり、これはもっとも極端な人工的とも言えるベンチマークです。実世界のアプリケーションで見られるよりも、差がはっきり示されていますが、このような共有カウンタは、時々、<em>必要になる</em>でしょう。そのような場合、LongAdderがとても役に立ちます。</p> 
  </blockquote> 
  <p>Drew氏は、さらにAtomicLongがシングルスレッドでは少し速いことを示している。しかし、スレッドが2つの場合は4倍遅く、スレッド数がコア数と同じ場合は、ほぼ5倍遅くなる。そして、スレッド数が物理コアのCPU数を超えるまで、LongAdderのパフォーマンスは一定であると述べている。</p> 
  <h2>モジュール化は外れる</h2> 
  <p>モジュール化は、Java8で提案されていた機能であり、実行されるアプリケーションでパッケージ化されたJava SEの実装をカスタマイズ可能にする。アプリケーションが使う、コードに依存しない要素は取り除くことができる。このような実装は、家庭電化製品のようなデバイスにJavaを組み込む場合に役に立つだろう。</p> 
  <p><a href="www.linkedin.com/in/markreinhold">Mark Reinhold</a>氏は、最近、Java SE 8からモジュール化を外すことを<a href="http://mail.openjdk.java.net/pipermail/java-se-8-spec-observers/2014-February/000064.html">提案した</a>。その原因として、法律的な問題を挙げた。</p> 
  <blockquote> 
   <p>互換性とフラグメンテーションに対するガードを保護するために、<a href="http://cr.openjdk.java.net/~mr/se/8/java-se-8-fr-spec-01/#s9">Java SE 8のモジュール化の機能</a>には、TCKライセンスにいくつかの重大な変更が必要です。</p> 
   <p>私は、これまでかなりの期間、これらの見直しに関して、Oracleの法務部と取り組んできました。その草稿はありますが、今の時点で、残念ながら、専門家グループ、JCP 執行委員会メンバ、その他関心のある人たちが、これらの変更をレビューしたり、コメントしたりする十分な時間がありません。</p> 
   <p>そのため、Java SE 8からモジュール化を外すように提案します。これは、仕様とTCKルールだけ変更すればよく、RIや実際のTCKテストの変更は必要ありません。</p> 
  </blockquote> 
  <p>Reinhold氏は、モジュール化はJavaプラットフォームの将来のために重要であり、Java SE 9より前のリリースで追加されるかもしれないと述べた。</p> 
  <p>Java 8のリリースはもうすぐだ。もっと簡単なdateやクロージャ、より良いコンカレンシ、新しいJavaScriptエンジンまでわずか1カ月だ。あなたはアップグレードするだろうか? アップグレードしないならば、アップグレードしない技術的な問題があるのだろうか?</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
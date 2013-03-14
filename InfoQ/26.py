<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Java 8でPermGenのOutOfMemoryError問題は解決されるのか？</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/java-8-permgen-metaspace;jsessionid=34ADD534D08065A0C629C62E16191E94"><em>原文(投稿日：2013/03/06)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>HotSpotとJRockitのコードベース統合を目指して進行中のプロジェクトの一部として，OracleはHotSpot JVMのJava 8バージョンから <a target="_blank" href="https://blogs.oracle.com/java/entry/java_7_questions_answers">PermGenを削除する</a> と発表した。しかし多くの人たちは，PermGen関連のすべてのエラーを消滅させる手段としてこれを受け止めている。PermGen廃止の効果は <a target="_blank" href="http://jdk8.java.net/download.html">Java 8 Early Access</a> ビルドで確認することができる。本当にすべての問題が解決されているのか，ここで検証してみたい。</p> 
 <h3>PermGenとは何か</h3> 
 <p>OracleのJVM開発者であるJon Masamitsu氏は <a target="_blank" href="https://blogs.oracle.com/jonthecollector/entry/presenting_the_permanent_generation">永続世代(Permanent Generation)の目的</a> について，2006年のブログ記事で次のように説明している – 永続世代領域にはバイトコードや名称，JIT情報といったクラス情報が格納されている。独立した領域を用意しているのは，これらがほぼ静的な情報であるため，分離することによってガベージコレクションのさらなる最適化が可能となるからだ。</p> 
 <h3>PermGenの問題</h3> 
 <p>多くの開発者たちが，開発中のシステムで &quot;java.lang.OutOfMemoryError: PermGen space&quot; というエラーを何度も経験している。その原因としてクラスローダに関連するメモリリークと共に非常に多いのが，新たなクラスローダの生成だ。これは一般的にコードのホットデプロイ中に発生するもので，運用時より開発マシン上での発生頻度が高い理由もここにある。運用時にこれが発生した場合には，開発者はヒープダンプをまず取得する。それから <a target="_blank" href="http://www.eclipse.org/mat/">Eclipse Memory Analyzer Toolkit</a> などのツールを使って，消滅したはずのクラスローダを探すことになる。永続的なコレクションは特別な設定を行わない限りガベージコレクションの対象になるのだが，リークが発生している場合には何も回収されない。運用時の &quot;問題&quot; としてもっとも多いのは，デフォルトの64MBが小さすぎるというもので，256MBへの設定が応急処置として行われるのが一般的だ。</p> 
 <h3>Java 8では何が変わるのか</h3> 
 <p>前出のJon Masamitsu氏は <a target="_blank" href="http://mail.openjdk.java.net/pipermail/hotspot-dev/2012-September/006679.html">HotSpot開発メールリスト</a> で，Java 8で実施される変更について次のように説明している – Java 8にはPermGenはもはや存在しない。internされた文字列などについては，すでにJava 7の時点で通常のヒープに移動されている。したがって8では，残りの構造が &quot;Metaspace&quot; と呼ばれるネイティブメモリ領域に移動される。この領域はデフォルトで自動的に拡張され，ガベージコレクションの対象である。<code>MetaspaceSize</code> と <code>MaxMetaspace</code> という２つのフラグの追加が予定されている。</p> 
 <p>氏はInfoQの求めに応じて，今回の変更の背景にある設計目標を説明してくれた。</p> 
 <blockquote> 
  <p>PermGenを削除したのは，ユーザがその適切なサイズを考えなくて済むようにしたかったからです。</p> 
  <p>アプリケーションのクラスデータにより多くのスペースが必要だと分かっている場合には，MetaspaceSizeをデフォルトより大きな値に設定します。大きめの値にしておけば，起動時のGC実行回数を少なくすることができますが，可能な限りGCを回避したいような理由でもない限り，そのような設定をする必要はありませんし，お勧めもしません。</p> 
  <p>クラスデータの領域を制限するためには MaxMetaspaceSize を設定します。クラスローダにリークの疑いがある場合や，ネイティブメモリを多く使い過ぎる前にアプリケーションを停止させたいような場合に使うとよいでしょう。サーバ上で複数のアプリケーションを動作させていて，それぞれが使用するクラスデータのスペースを制限したい，というケースも考えられます。</p> 
 </blockquote> 
 <p>要するに <code>MetaspaceSize</code> は最初の数回のガベージコレクションに潜在的に影響する類いのものであって，ほとんどの場合には重要ではない，ということだ。そういった意味では，以前の <code>PermSize</code> フラグの目的と同じである。</p> 
 <p><code>MaxMetaspaceSize</code> が指定された場合は，メモリ不足となる可能性が依然として存在し， &quot;java.lang.OutOfMemoryError: Metadata space&quot; が発生する。事実としてクラスローダにリークが存在し，Javaの利用可能なネイティブメモリの容量が無制限ではない以上，<code>MaxPermSize</code> 指定と同じような制限を設定することは賢明な方法だろう。PermGenの場合と同じように，詳細なGCログを指定することでMetaspaceの現在の使用量が出力される。また，コマンドラインでフラグ <code>PermSize</code> あるいは <code>MaxPermSize</code> を使用すると警告が表示されて，Metaspaceフラグに変更するように指示される。</p> 
 <h3>結論</h3> 
 <p>MetaspaceとPermは概念上はほとんど同じなので，Java 7からJava 8へのアップグレードを行う管理者は <code>sed 'e/Perm/Metaspace/g'</code> を実行して，単にフラグを変更するだけでよい。</p> 
 <p>全体的に今回の変更は期待外れだ。ほとんどの面から見て，単なる名前の変更に過ぎない。Metaspaceのデフォルトを無制限にしたことによって，小さすぎるデフォルト値の選択は回避できるが，システムの安定性を確保するためには，最大値の設定は必要だ。幸運なのは，ほとんど誰もがすでに使用しているPermSizeとMaxParmSizeの設定が，単に名称を変えるだけで再利用できることだ。逆に残念なのは，Kirk Pepperdine氏が <a target="_blank" href="http://mail.openjdk.java.net/pipermail/hotspot-dev/2012-September/006684.html">懸念点として指摘している</a> ように，管理されたJavaヒープからネイティブメモリへ移行することで，トラブルシュートにおいて貴重な情報のほとんどが失われることだ。</p> 
 <p>そして結局，クラスローダのリークが発生するのは以前と同じなのだ。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
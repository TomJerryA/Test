<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Netty 4がTwitterのGCオーバーヘッドを1/5に削減</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/netty4-twitter"><em>原文(投稿日：2013/11/06)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Netty Projectは７月，Netty 4の最初のバージョンをリリースした。おもにガベージコレクションのオーバーヘッドを削減することによって，大幅なパフォーマンスの向上を実現している。TwitterはNetty 4を組み込むことで５倍のパフォーマンス向上を実現したが，いくつか問題もあった。</p> 
  <p><a href="http://netty.io">Netty Project</a>を立ち上げた<a href="http://www.linkedin.com/in/trustin">Trustin Lee</a>氏が，Twitterのソフトウェアエンジニアと共同でネットワークアプリケーション用フレームワークの開発を始めたのは，2003年のことだ。最初のリリースは<a href="http://www.theserverside.com/news/thread.tss?thread_id=26416">2004年7月</a>に公開された。プロジェクトの<a href="http://netty.io/">ホームページ</a>ではNettyについて，&quot;高パフォーマンスを維持するプロトコルサーバおよびクライアントを迅速に開発するための，非同期のイベント駆動ネットワークアプリケーションフレームワーク&quot; である，と説明している。</p> 
  <p>Twitterでは多くの場所でNettyを使用してネットワーク機能を実装している，と &quot;<a href="javascript:void(0);">Netty 4 at Twitter: Reduced GC Overhead</a>&quot; にLee氏は書いている。</p> 
  <blockquote> 
   <ul> 
    <li>当社の<a href="https://blog.twitter.com/2011/finagle-protocol-agnostic-rpc-system">プロトコル非依存のRPCシステム</a>である<a href="http://twitter.github.io/finagle/">Finagle</a>は，トランスポート層をNetty上に構築しています。このシステムは<a href="https://blog.twitter.com/2011/twitter-search-now-3x-faster">Search</a>など，大部分のサービスの実装で内部的に使用されています。</li> 
    <li>当社独自の<a href="http://wiki.squid-cache.org/SpoonFeeding">スプーンフィーディング(spoon-feeding)</a><a href="http://en.wikipedia.org/wiki/Reverse_proxy">リバースプロキシ</a>であるTFE (Twitter Front End)では，一般向けのHTTPおよび<a href="http://en.wikipedia.org/wiki/SPDY">SPDY</a>トラフィックの大部分をNettyで提供しています。</li> 
    <li><a href="https://github.com/twitter/cloudhopper-smpp">Cloudhopper</a>は，全世界の数百というモバイルキャリアに対して，Nettyを使って毎月数十億のSMSメッセージを送信しています。</li> 
   </ul> 
  </blockquote> 
  <p>Reactorパターンを実装したNettyは，<a href="http://www.playframework.com/">Play Framework</a>のコア部分でも使用されている。PlayやGrailsといった多くのWebフレームワークは<a href="http://www.jamesward.com/2011/08/23/war-less-java-web-apps">WARレスのWebアプリ</a>を採用することで，ベースとなるHTTPサーバとのより強固な統合を実現している。Nettyのようなサーバを内部的に使用することで，非同期プログラミングは極めて簡単なものになる。非同期プログラムと非ブロックI/Oは，<a href="http://www.reactivemanifesto.org/">Reactive Manifesto</a> にとして中核のテクニックだ。この新たなパターンについては，InfoQでも &quot;<a href="http://www.infoq.com/jp/news/2013/09/reactive-programming-emerging">注目を集めるリアクティブプログラミング</a>&quot; という記事にしている。</p> 
  <p>Netty 3では，I/Oイベントを表すためにJavaオブジェクトを使用していた。その点について，Lee氏は次のように言う：</p> 
  <blockquote> 
   <p>この方法はシンプルですが，当社のような規模においては大量の<a href="http://en.wikipedia.org/wiki/Garbage_collection_(computer_science)">ガベージ</a>を発生させることにもなります。Netty 4新リリースでは，これまでの短命なイベントオブジェクトに代えて，寿命の長いチャネルオブジェクトのメソッドを使用してI/Oイベントを処理するように変更されました。プールを使用する専用のバッファアロケータも用意されています。</p> 
   <p>... Netty 3では新たなメッセージを受信したり，あるいはリモート側にメッセージを送信すると，その都度ヒープバッファが生成されています。そしてこの新たなバッファそれぞれに ‘new byte[capacity]’ が実行されるのです。このように生成されたバッファはGC圧力を高め，メモリ帯域を消費します - 新たにアロケートされたバイト配列毎が安全のためにゼロ埋めされることが，メモリ帯域を消費しているのです。しかもゼロ埋めされた配列はほとんどの場合，後に実際データが詰められますから，同じ量のメモリ帯域を再び消費することになります。もしJava仮想マシン(JVM)にゼロを埋める必要のない配列を新規生成する方法があれば，メモリ帯域を半分に削減することができるはずです。しかし今のところそのような手段はありません。</p> 
  </blockquote> 
  <p>Netty 4ではイベントオブジェクトの生成に代えて，さまざまなイベントタイプを扱うことのできる，より粒度の小さなAPIを定義している。また，新たなバッファプール実装として，<a href="https://www.facebook.com/notes/facebook-engineering/scalable-memory-allocation-using-jemalloc/480222803919">jemalloc</a>のピュアJavaバージョンも装備している (これはFacebookでも使用されている)。これらによって，バッファを０で埋めるというメモリ帯域の無駄はなくなったが，GCによって管理されない部分であるため，リークには注意が必要だ。ハンドラがバッファのリリースを忘れていると，メモリ使用量が無制限に増大することもある。</p> 
  <p>これらの変更はNetty 3と互換性を持たないが，バッファの生成と回収の速度は５倍になる。</p> 
  <p>Lee氏によると：</p> 
  <blockquote> 
   <p>私たちはNetty 3と4をそれぞれを使用して構築した<a href="http://en.wikipedia.org/wiki/Echo_Protocol">echo</a>プロトコルサーバを比較しました (echoは非常にシンプルで，ガベージがプロトコルではなくNettyのフォールトによって生成されたものと見なすのに十分です)。これらのサーバそれぞれに対して，分散配置したechoプロトコルクライアントから16,384の並列的な接続を行い，256バイトのペイロードをランダムに送信します。ギガビットイーサネットがほぼ輻輳するまでこれを繰り返したのです。</p> 
   <p>このテストの結果，Netty 4は：</p> 
   <ul> 
    <li>GCによる停止回数が1/5 – <strong>45.5回/分 : 9.2回/分</strong></li> 
    <li>ガベージ生成が1/5 – <strong>207.11MiB/秒 : 41.81 MiB/秒</strong></li> 
   </ul> 
  </blockquote> 
  <p>氏はNetty 4をTwitterに適用する上でいくつかの障害があったことに触れている。具体的にはバッファリークとコードの複雑さだ。同プロジェクトではHTTP/2や非同期DNS名前解決，HTTPとSOCKSプロキシサポートなど，クライアント側の機能なども取り込みたいと考えている。</p> 
  <p>Yahoo Engineeringにも同じような記事があり，Nettyが同社の<a href="https://github.com/nathanmarz/storm">Storm</a>クラスタのスピード倍増に寄与した状況が紹介された。その記事 &quot;<a href="http://yahooeng.tumblr.com/post/64758709722/making-storm-fly-with-netty">Making Storm fly with Netty</a>&quot; では，Bobby Evans氏が次のように述べている：</p> 
  <blockquote> 
   <p>Yahooでは自社開発したシステムを使用していましたが，NettyをStormクラスタの既定メッセージレイヤとする前には，現在のデフォルトであるzeromqと比較した数値を取得しておく必要がありました。そのためには，Stormのメッセージレイヤを明確に凌駕する証拠としてのベンチマークが必要でしたので，それを<a href="https://github.com/yahoo/storm-perf-test">書きました</a>。Stormの異なるBoltとSpoutの間でメッセージをプッシュする速さを確認するための単純な瞬間速度計測テストで，複雑度の異なる複数のトポロジをローンチした上で，固定サイズのメッセージを送信できるようになっています。</p> 
  </blockquote> 
  <p>Evans氏は(リソースが競合しない)小さなテストを使用して，Nettyがzeromqより高速(40%～100%)であることを示した。より規模の大きなテストを実施した際にパフォーマンス上の問題が発生したが，スレッド数を制限することで解決できたという。</p> 
  <blockquote>
    Nettyのデフォルト設定は，たとえノードがひとつだけだったとしても，小さなメッセージを多数扱うのには適切ではありません。しかしスレッドをひとつに制限することで，ネットワークが再び輻輳するまでの間に，zeroqよりも１秒当たり111%から85%多いメッセージを取得することが可能になります。 
  </blockquote> 
  <p>氏によるとNettyは現在，YahooのStormクラスタのデフォルトになっている。</p> 
  <p>Netty 4の改善は，多くのオープンソースプロジェクトにメリットがあるだろう。フレームワークに<a href="http://netty.io/wiki/related-projects.html">関連するものとして挙げられた一覧</a>の中には，<a href="http://akka.io/">Akka</a>や<a href="http://james.apache.org/">Apache James</a>，<a href="http://www.jboss.org/hornetq">HometQ</a>, <a href="http://vertx.io/">Vert.x</a>など，多数のプロジェクトの名前が見える。Netty 4について詳しくは <a href="http://netty.io">netty.io</a>あるいは<a href="javascript:void(0);">Lee氏のブログ記事</a>を参照してほしい。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
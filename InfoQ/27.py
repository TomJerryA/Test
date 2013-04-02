<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>いつWPFをAsyncとReactive Extensionsと一緒に使うべきか</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/WPF-Async;jsessionid=4B14B973DA3FB144096F8B516235AEF4"><em>原文(投稿日：2013/03/22)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Ian Griffiths氏は、WPFで.NET 4.5の非同期フィーチャをいつ使い、いつ使わないべきかに関する6回シリーズを公開した。シリーズは<a target="_blank" href="http://www.interact-sw.co.uk/iangblog/2013/02/14/wpf-async-too-fast">WPFとAsyncは余りに良く、余りに早い</a>と題する記事で始まっている。</p> 
 <p>非同期を使って、好きなようにアプリケーション中にそれを振り分けて、それでお終いとしたくなるかもしれない。不幸にして、バッチサイズ、すなわち各非同期呼び出し間の時間差がタスクオブジェクトの生成コストと関連するコンテキストスイッチのコストよりも小さければ、これは上手くいかない。</p> 
 <p>大きなバッチは完了するまでの時間を短縮できるが、UIの応答性を妨げる可能性がある。氏は次のように書いている。</p> 
 <blockquote> 
  <p>これは8.5秒のケースよりも随分早いですが我々は何かを失いました。もっと遅い例は、UIでもっと早くなる、という役立つ結果を産みました。事実、ユーザーは実際、その遅いバージョンの方を好むでしょう。なぜなら、もし有用なデータが即座に現れたら、リストを埋め終わるのに3倍長く時間がかかるのに気が付かないかもしれない。おそらく、とにかく全リストをスクロールダウンするのに8.5秒よりずっと長くかかるでしょう。なので1つの重要な手段によって、ネイティブ非同期メソッドはより優れています。それは、ユーザーにより早く有益な情報を提供します。</p> 
 </blockquote> 
 <p>Ian Griffiths氏は、また<a target="_blank" href="http://www.interact-sw.co.uk/iangblog/2013/02/19/wpf-threads-too-fast">スレッドプールと WPF 4.5の新しい Collection Synchronizationフィーチャ</a>を使うことに注目している。もしConfigureAwait(false) を使って、処理がUIスレッド上で起きるように強制することを避けたいなら、このテクニックは必要である。</p> 
 <blockquote> 
  <p>ConfigureAwaitへのその呼び出しは、メソッドがどのコンテキストで継続するのかは気にしていない、と宣言しています。結論は、すぐに完了できない読み取りが結局終了しない場合、メソッドの残りの部分の遅延実行は、スレッドプールのスレッドで起こるということです。これは、我々のawait は、もはやWPFディスパッチャのオーバーヘッドを被ることがない、ということです。しかし、もちろん、それはまた、すべてのリストの更新がワーカースレッド上で起きることを意味しますので、我々は問題を回避するために、以前と同じトリックを使用する必要があります。どちらもリストをデータバインディングに見えるようにする前に、私達が終わるまで、待つ必要があります。あるいは、我々は、スレッド間の変更通知処理を可能にする必要があります。</p> 
 </blockquote> 
 <p>氏が示した別のテクニックは、<a target="_blank" href="http://www.interact-sw.co.uk/iangblog/2013/02/20/wpf-rx-threads-chunking">Reactive Extensionsを使ってデータをまとめる</a>ことだ。これはBuffer関数を使ってバッチサイズを100 ms ないし 5000 項目のいずれか最初の方に制限する。そして ObserveOnDispatcher関数は、UIスレッド上にそれをマーシャリングして戻す。このパターンは他のテクニックよりも冗長だが、「ほぼ瞬時に、データを表示し始め、全データをロードして、表示するのに2.3秒で終わります」、また元の同期実装に対する改善である。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
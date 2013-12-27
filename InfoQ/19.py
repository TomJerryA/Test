<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Reactive Extensions for C++の紹介</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/rx-cpp"><em>原文(投稿日：2013/12/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Rx.cppとしても知られる<a href="http://msopentech.com/blog/2013/12/05/ms-open-tech-hub-releases-rx-2-2/">Reactive Extensions for C++</a>が、WinRTでも（C++/CXを使って）、OS Xでも（clangを使って）利用できるようになった。まだ初期段階だが、最後のプレビュー以来、多くの仕事がなされている。</p> 
  <p>スケジューリングはReactive Extensionsの基盤だ。WindowsのHWNDメッセージループに特化したものも含めて、このリリースでは5つのスケジューラが利用できる。</p> 
  <ul> 
   <li>Immediate</li> 
   <li>CurrentThread</li> 
   <li>EventLoop</li> 
   <li>NewThread</li> 
   <li>Window</li> 
  </ul> 
  <p>OrderBy、ForEach、Using、Scan、Throttle、TakeUntil、Skip、SkipUntil、ToVector、ToList、Zip、Concat、CombineLatest、Merge、ToAsyn、Using、ConnectableObservable、Multicast、Publish、PublishLast、RefCount、ConnectForever、SubscribeOn、ObserveOnといった「STLアルゴリズムの非同期等価」なオペレータは、Rx開発者にとっておなじみだろう。</p> 
  <p>BindCommand、DeferOperation、CoreDispatcherScheduler、FromEventPattern、FromAsyncPattern、ReactiveCommandはWinRTのC++/CXに特有なものだ。最後のReactiveCommandは<a href="http://www.reactiveui.net/">Paul Betts氏のReactiveUI</a>に由来する。</p> 
  <p>以下に、RangeからObservableを生成する例を示す。</p> 
  <pre><p>//Declare an observable</p><p>auto values1 = rxcpp::Range(1, 10);</p><p>rxcpp::from(values1)</p><p>.for_each(</p><p>[](int p) {</p><p>cout &lt;&lt; p &lt;&lt; endl;</p><p>});</p></pre> 
  <p><a href="http://rxcpp.codeplex.com/">Rx.cppのソースコード</a>はCodePlexからApache License 2.0ライセンスで利用できる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
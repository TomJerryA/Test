<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Dartの M4リリースがコアライブラリを安定化</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/dart-m4-release;jsessionid=3131C8F26AA6053323E897E0E561F6AD"><em>原文(投稿日：2013/04/17)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Google DartがDart SDKの<a target="_blank" href="http://news.dartlang.org/2013/04/core-libraries-stabilize-with-darts-new.html">マイルストーン 4をリリースした</a>。言語は既に、以前のマイルストーンで安定化したが、このM4リリースは幾つかのコアライブラリを安定化させた。特に <tt>dart:core</tt>, <tt>dart:collection</tt>、<tt>dart:async</tt>。パフォーマンスも向上した。Dartをネイティブで動かすDartVMは、160% (DeltaBlueベンチマークで)から200% (Richardsベンチマークで)Chromeを動かしているJavaScriptエンジンの<a target="_blank" href="https://code.google.com/p/v8/">v8</a>よりも早くなった。このリリースには、<a target="_blank" href="http://www.infoq.com/news/2013/04/dart2js-outperforms-js;jsessionid=93370A9187738AFCCC4C1323FBBE898A;jsessionid=3131C8F26AA6053323E897E0E561F6AD">以前我々がレポートした、高速化されたdart2jsコンパイラー</a>が含まれている。</p> 
 <p><a target="_blank" href="https://groups.google.com/a/dartlang.org/d/msg/misc/rIKbw3AVNxo/oJZvxo_1SEAJ">このリリースにおけるAPIの変更</a>のまとめ</p> 
 <blockquote> 
  <ul> 
   <li>Iterable.joinの区切り引数のデフォルトが <tt>null</tt> から &quot;&quot;になった。</li> 
   <li>全ての<tt>DateTime</tt>定数が非省略になり、<tt>DAYS_IN_WEEK</tt>が<tt>DAYS_PER_WEEK</tt>になった。</li> 
   <li>非推奨のクラスとメソッドを削除した。 
    <ul> 
     <li><tt>CollectionSink</tt></li> 
     <li><tt>Stream.pipeInto</tt></li> 
     <li><tt>Iterable/Stream.max/min</tt></li> 
     <li><tt>Collection</tt> (List, Set、QueueはIterableから直接拡張された。)</li> 
     <li><tt>Datetime.&lt;/&lt;=/&gt;/&gt;=</tt></li> 
     <li><tt>IOSink.writeStream</tt> (IOSink.addStreamへ名称変更)</li> 
     <li><tt>IOSink.writeBytes</tt> (IOSink.addへ名称変更)</li> 
     <li><tt>StreamSink</tt> (EventSinkへ名称変更)</li> 
    </ul> </li> 
   <li>導入された<tt>Iterable.reduce/Stream.reduce</tt>は、引数を必要としない。</li> 
   <li>List 範囲関数がリファクタリングされた。 
    <ul> 
     <li><tt>List.getRange</tt>は、<tt>endIndex</tt>を引数にとり、<tt>Iterable</tt>を返す。</li> 
     <li><tt>List.setRange</tt>は、<tt>endIndex</tt>と<tt>iterable</tt>を引数にとる (プラス　オプションでskipCount)。</li> 
     <li><tt>List.removeRange</tt>endIndexを引数にとる</li> 
     <li><tt>List.insertRange</tt>は削除された。</li> 
     <li><tt>List.replaceRange</tt>が追加された。</li> 
     <li><tt>List.fillRange</tt> が追加された。</li> 
     <li><tt>List.setAll</tt>が追加された。(厳密に言えば範囲関数ではない)。</li> 
    </ul> </li> 
   <li><tt>Stream.hasSubscribers</tt>が<tt>Stream.hasListener</tt>に名称変更</li> 
   <li><tt>async:EventSinkView</tt>が削除</li> 
   <li><tt>AsyncError</tt>クラスが削除</li> 
   <li><tt>StreamController.broadcast</tt>が削除</li> 
   <li><tt>dart:html</tt>によってほとんどWeb Worker関連のAPIが削除された。正しいAPIがちゃんと機能するので。 Workerクラスは、そのままでJavascriptワーカーを生成する。</li> 
   <li><tt>InvocationMirror</tt>は、<tt>Invocation</tt>に名称変更。</li> 
   <li><tt>Function.apply</tt>は、<tt>Symbol</tt>を名前付き引数に使用。</li> 
   <li><tt>dart:mirror</tt>は、<tt>String</tt> の代わりに<tt>Symbol</tt>を使って名前を表すようになった。</li> 
  </ul> 
 </blockquote> 
 <p>頻繁に変わるAPIは、Dart開発者にとって重荷であるが、ユーザーは<a target="_blank" href="https://groups.google.com/a/dartlang.org/forum/#!searchin/misc/breaking$20change">重大な変更</a>がないか<a target="_blank" href="http://www.infoq.com/news/2013/04/blossom-dart-switch;jsessionid=93370A9187738AFCCC4C1323FBBE898A;jsessionid=3131C8F26AA6053323E897E0E561F6AD">メーリングリストを常によく見る</a>必要がある。チームは、夏に1.0のリリースを予定しているが、それまではずっと重大な変更があり得る。1.0が出れば、APIの変更はずっと少なくなるだろう。これらの変更の数は、夏が近づくにつれて、減っていくものと予想される。</p> 
 <p><a target="_blank" href="http://www.dartlang.org/tools/sdk/">Dart SDK M4 リリースは、Dartウェブサイトからダウンロードでき</a> 、Windows, Linux、Mac版がある。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
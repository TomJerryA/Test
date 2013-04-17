<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Dart's M4 Release Stabilizes Core Libraries</h3><p>The Google Dart team <a href="http://news.dartlang.org/2013/04/core-libraries-stabilize-with-darts-new.html">has released milestone 4</a> of its Dart SDK. While the language had already stabilized in previous milestones, this M4 release stabilizes some core libraries, specifically: <tt>dart:core</tt>, <tt>dart:collection</tt> and <tt>dart:async</tt>. Performance has also improved. The DartVM, which runs Dart natively, is now between 160% (for the DeltaBlue benchmark) and 200% (for the Richards benchmark) faster than <a href="https://code.google.com/p/v8/">v8</a>, the JavaScript engine that powers Chrome. The release also includes the <a href="http://www.infoq.com/news/2013/04/dart2js-outperforms-js;jsessionid=97B83D560AF790E192AF73A076107B80">faster dart2js compiler that we reported on before</a>.</p> 
<p>A summary of <a href="https://groups.google.com/a/dartlang.org/d/msg/misc/rIKbw3AVNxo/oJZvxo_1SEAJ">the API changes in this release</a>:</p> 
<blockquote> 
 <ul> 
  <li>The separator argument in Iterable.join defaults to &quot;&quot; (instead of <tt>null</tt>).</li> 
  <li>All <tt>DateTime</tt> constants are non-abbreviated. Also changed <tt>DAYS_IN_WEEK</tt> to <tt>DAYS_PER_WEEK</tt>.</li> 
  <li>Removed deprecated classes and methods 
   <ul> 
    <li><tt>CollectionSink</tt></li> 
    <li><tt>Stream.pipeInto</tt></li> 
    <li><tt>Iterable/Stream.max/min</tt></li> 
    <li><tt>Collection</tt> (List, Set and Queue now extend Iterable directly)</li> 
    <li><tt>Datetime.&lt;/&lt;=/&gt;/&gt;=</tt></li> 
    <li><tt>IOSink.writeStream</tt> (renamed to IOSink.addStream)</li> 
    <li><tt>IOSink.writeBytes</tt> (renamed to IOSink.add)</li> 
    <li><tt>StreamSink</tt> (renamed to EventSink)</li> 
   </ul> </li> 
  <li><tt>Iterable.reduce/Stream.reduce</tt> introduced that does not require an initial value.</li> 
  <li>List range functions were refactored: 
   <ul> 
    <li><tt>List.getRange</tt> takes an <tt>endIndex</tt> argument and returns an <tt>Iterable</tt>.</li> 
    <li><tt>List.setRange</tt> takes an <tt>endIndex</tt> and an <tt>iterable</tt> (plus an optional skipCount).</li> 
    <li><tt>List.removeRange</tt> takes an endIndex.</li> 
    <li><tt>List.insertRange</tt> got removed.</li> 
    <li><tt>List.replaceRange</tt> was added.</li> 
    <li><tt>List.fillRange</tt> was added.</li> 
    <li><tt>List.setAll</tt> was added. (not strictly speaking a range function).</li> 
   </ul> </li> 
  <li><tt>Stream.hasSubscribers</tt> renamed to <tt>Stream.hasListener</tt></li> 
  <li>Removed <tt>async:EventSinkView</tt>.</li> 
  <li>Removed the <tt>AsyncError</tt> class.</li> 
  <li>Removed <tt>StreamController.broadcast</tt>.</li> 
  <li><tt>dart:html</tt> has had most Web Worker related APIs removed while the correct API is worked out. The Worker class remains for spawning Javascript workers</li> 
  <li>Renamed <tt>InvocationMirror</tt> to <tt>Invocation</tt></li> 
  <li><tt>Function.apply</tt> uses <tt>Symbol</tt> for named arguments</li> 
  <li><tt>dart:mirror</tt> now uses <tt>Symbol</tt> instead of <tt>String</tt> to represent names</li> 
 </ul> 
</blockquote> 
<p>Frequently changing APIs is one of the challenges of developing with Dart today, requiring users to <a href="http://www.infoq.com/news/2013/04/blossom-dart-switch;jsessionid=97B83D560AF790E192AF73A076107B80">keep a close eye on the mailing list</a> for <a href="https://groups.google.com/a/dartlang.org/forum/#!searchin/misc/breaking$20change">breaking changes</a>. As the team aims for a summer 1.0 release, it will continue to add breaking changes while it still can, once 1.0 is hit, APIs will change less often. The number of these changes is expected to decrease as summer draws closer.</p> 
<p>The <a href="http://www.dartlang.org/tools/sdk/">Dart SDK M4 release can be downloaded</a> from the Dart website and is available for Windows, Linux and Mac.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
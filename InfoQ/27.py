<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>C#の非同期の落とし穴</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/async-csharp-fsharp;jsessionid=F0A6948611B1B7C76D04C2836026F761"><em>原文(投稿日：2013/04/23)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>時々 1 つの言語の落とし穴を理解する最良の方法は、別の言語がそれらをどのように防いでいるかを参考にすることである。Real-World Functional Programmingの著者であるTomas Petricek氏は、非同期なC# コードに見られる６つの一般的な誤りについて説明し、どのように F# がそれらの発生する可能性を少なくしているかを示している。</p> 
 <p>彼の<a target="_blank" href="http://tomasp.net/blog/csharp-async-gotchas.aspx">Async in C# and F#: Asynchronous gotchas in C#</a>という題名の記事を全て読むことを薦めるが、以下がその概要である。</p> 
 <p><strong>Asyncは、非同期に動かない</strong>: 最初のawait ステートメントの後に出てきたコードだけが非同期に動く。</p> 
 <p><strong>結果を無視する</strong>: 関数によって返されるタスク上でawaitすることを忘れると、順番のでたらめな結果になる。</p> 
 <p><strong>Async void メソッド</strong>: “async Task”でなく“async void”を返す関数は、awaitできないので、結果を無視した場合と同じ問題を起こすことになる。</p> 
 <p><strong>Async void ラムダ関数</strong>: これは、関数が Action delegateを受け付けて、 Func&lt;…, Task&gt; delegateを受け付けない時に起こる。またしても、非同期関数はawaitされない。</p> 
 <p><strong>入れ子のタスク</strong>: “await Task.Factory.StartNew(async () =&gt; { await Task.Delay(1000); });” というステートメント中の最初と２番目の await ステートメントは完全に無関係である。すなわち最初のawaitが２番目のawaitの前に終了する。関連付けられた1000 msの遅延は、有効である。</p> 
 <p><strong>非同期に走らない</strong>: Task.Wait()を使うと、全コールスタックは、強制的に同期モードになる。</p> 
 <p>F#に不慣れな人は、F#の非同期ワークフローがTask と Task&lt;T&gt; 型をベースにしていないのを知って驚くだろう。代わりに F# Async&lt;T&gt;として知られている独自の型を使っている。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
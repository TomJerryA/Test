<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>さらにパフォーマンスを向上したDart 1.1</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/dart-1-1"><em>原文(投稿日：2014/01/17)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>先日リリースされたDart 1.1は，dart2jsコンパイラのパフォーマンスが向上し，サーバ側の開発サポートが改善されている。言語自体はほとんどそのままだ。</p> 
  <p>昨年11月にリリースされた<a href="http://www.infoq.com/news/2013/11/dart-10">Dart 1.0</a>マイルストーンに続いてGoogleは，言語のパフォーマンスをさらに向上したDart 1.1を公開した。dart2jsコンパイラが生成するJavaScriptコードは，2ヶ月前のRichardsベンチマークよりも25%高速になった。Googleの誇るV8と比較しても，差は10%未満だ。</p> 
  <p>FluidMotionベンチマークによるdart2jsのパォーマンスは，11月の時点から倍増して，V8と同等になった。Tracerベンチマークにはさほどの変化はないが，V8よりも1/3以上高速だ。DeltaBlueベンチマークはまったく変わっていない。どのベンチマークでもネイティブで動作するDart VMが，dart2jsとV8のいずれよりも上回っている。(過去のベンチマーク結果はすべて，<a href="https://www.dartlang.org/performance/">Dartのパフォーマンスに関するWebページ</a>に公開されている。)</p> 
  <p>GoogleでDartのDeveloper Advocateを務めるSeth Ladd氏は，<a href="http://news.dartlang.org/2014/01/dart-11-features-up-to-25-faster.html">サーバに関連するDart 1.1の進展</a>をいくつか指摘する。</p> 
  <blockquote> 
   <p>大容量のファイル，ファイルのコピー，プロセスシグナルハンドラと端末情報のサポート。今回のリリースでは新たにUDPがサポートされました。これにより，例えば効率のよいメディアストリーミングアプリケーションを書くことができるようになります。</p> 
  </blockquote> 
  <p>Dartエディタはパフォーマンスの改善に加えて，デバッグやコード補完，ツールチップなどの分野でも進歩している。</p> 
  <p><a href="https://www.dartlang.org/docs/spec/latest/dart-language-specification.html">言語仕様の更新バージョン</a>も公開された。ただしBob Nystrom氏によると，言語仕様は現在保留中で，<a href="http://www.ecma-international.org/">Ecma International</a>によって委員会が組織されるのを待っている段階だ。<a href="http://to%20standardize%20the%20syntax%20and%20semantics%20of%20a%20modern%2C%20object%20oriented%20programming%20language%20called%20dart%20as%20well%20as%20standardizing%20core%20libraries%20and%20complementary%20technologies%20that%20support%20the%20language.%20this%20work%20should%20not%20use%20patents%20or%20if%20so%20then%20only%20royalty%20free%20patents.%20%20to%20aid%20in%20achieving%20that%20objective%2C%20this%20tc%20will%20use%20an%20experimental%20tc52%20rf%20patent%20policy%20similar%20that%20has%20been%20developed%20for%20use%20by%20tc39./">その委員会では，</a></p> 
  <blockquote> 
   <p>Dartという名の近代的なオブジェクト指向プログラム言語のシンタクスとセマンティクスの標準化，並びにコアライブラリと言語をサポートする補完的技術の標準化を行います。この作業においては特許を使用しないか，あるいはロイヤリティフリーの特許のみを使用します。目的達成を支援するため本TCでは，TC39で使用するために開発されたものと同様の，実験的なTC52 RF特許方針を採用します。</p> 
  </blockquote> 
  <p><a href="http://news.dartlang.org/2013/12/ecma-forms-tc52-for-dart-standardization.html">EcmaがTC52委員会を最初に発表したのは12月</a>で，GoogleがDartの言語と実装を安定させるのを待って行われた。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
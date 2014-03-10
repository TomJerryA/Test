<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Mono，JITとGCを改良</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/mono-3-2-7"><em>原文(投稿日：2014/02/26)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://news.mono-project.com/2014/02/25/mono-3-2-7-is-out/">Mono 3.2.7が公開された</a>。改良されたJIT，LINQ用の新しいインタプリタ，64bitネイティブ命令の使用など，数多くの新機能を備える。</p> 
  <p>５ヶ月に及ぶ開発の成果を蓄積した大規模な機能リリースだ。最大の改良点は内部的なパフォーマンス改善と最適化，互換性の向上だろう。注目すべきものをいくつか挙げると -</p> 
  <ul> 
   <li>ARMのHardFP ABI(Application Binary Interface)が初めてサポートされた。より新しいバージョンのLinux上でmonoが利用可能になるとともに，それらのターゲットに，よりよいコードを生成する。詳細を理解するには，<a href="http://www.gurucoding.com/en/rpi_cross_compiler/diff_hardfp_softfp.php">HardFPとSoftFPの違い</a>について読んでみてほしい。</li> 
   <li>ABCREM(<a href="https://github.com/mono/mono/blob/master/mono/mini/abcremoval.c">Array Bound Checks Removal</a>)最適化の<a href="https://github.com/mono/mono/commit/6c0fa0d567f69e58bba4603f5b14435a7d827ab4">64bitシステムでの動作が向上した</a>。</li> 
   <li>２つの新しい最適化 - <a href="http://en.wikipedia.org/wiki/Loop-invariant_code_motion">Loop Invariant Code Motion</a>(ループ内不変式の移動)パスと<a href="http://llvm.org/docs/AliasAnalysis.html">Alias Analysis</a>(エイリアス解析)。いくつかの機能において，最大20%のパフォーマンス向上を実現している。</li> 
   <li>64bit CAS命令が32bitシステム上でサポートされた。これにより，マルチコアでのPLINGワークロードが大きく向上している。</li> 
   <li>最新バージョンのLLVMを採用したことにより，高速なTLS(Thread Local Storage)アクセスコードが生成可能になった。</li> 
   <li>GCのマイクロ最適化 - 内部データ構造の最適化，および組み込み関数(intrinsics)利用によるコアループの速度向上。</li> 
   <li><a href="http://www.mono-project.com/AOT">FullAOT</a>ランタイムから利用可能なLINQおよび動的ステートメント用のインタプリタ。</li> 
   <li><a href="https://github.com/mono/mono/commit/3b664f331fe8a1920e88437d91b715775dc789f6">Task Awaiters</a>によるカスタムタスクスケジューラのサポート向上。</li> 
   <li>C#コンパイラの到達可能性およびフロー解析の大幅な向上と，それによるコード警告の改善。</li> 
  </ul> 
  <p>リリースにはいくつかのバグ修正も含まれている。改良点の全リストは<a href="http://www.mono-project.com/Release_Notes_Mono_3.2#New_in_Mono_3.2.7">リリースノート</a>で見ることができる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
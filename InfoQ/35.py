<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>GCC 4.8でC++に完全移行</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/gcc48_released;jsessionid=E3373EF6481F2039C13BC8EAEB8F218E"><em>原文(投稿日：2013/03/28)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p style="margin-bottom: 0in" class="western"><span lang="en-US">GNU Compiler Collection (GCC) の<a class="western" target="_blank" href="http://gcc.gnu.org/gcc-4.8/">最新バージョン</a>は、C++への変換の完了を記して、リリースされた。このプロセスは複数年に渡るプロジェクトで、GCCチームは、保守しやすいコードによってプロジェクトメンバーを維持し、新しいメンバーを惹きつけるために必要だった、と述べている。<a class="western" target="_blank" href="http://gcc.gnu.org/wiki/cxx-conversion">C++が選ばれた</a>のは、部分的には、標準ベースの言語であり、プロジェクトによれば、「より綺麗なコードをサポートするほうが、より綺麗なインターフェースを書いたり、強制するのが、より簡単であり、そして万能薬ではないが、（Cベースのレガシーコードに対する）改善である。」ほとんどの開発者に対する最終結果は、単にソースから4.8をコンパイルすることに興味のある人達は、C++2003を理解するコンパイラーを使わなければならない、ということである。一般的なユーザーは、単に、アップデートするのがもっと効率的で簡単であるように設計されたコンパイラースイートから恩恵を受けるだろう。</span></p> 
 <p style="margin-bottom: 0in" class="western"><b>新コンパイラーのフィーチャ</b></p> 
 <p style="margin-bottom: 0in" class="western">一般的なコンパイラーの改善として、「新世代最適化レベルが導入され、これが高速コンパイルと優れたデバッグ機能のニーズに応えている。また実行時パフォーマンス用の合理的なレベルも提供している。」更に、4.8には、メモリエラー検知用の<a class="western" target="_blank" href="https://code.google.com/p/address-sanitizer/">AddressSanitizer</a>とデータ競合を検知するために、命令にインストラメントできる<a class="western" target="_blank" href="https://code.google.com/p/data-race-test/wiki/ThreadSanitizer">ThreadSanitizer</a>が含まれている。（ThreadSanitizerは現在、x86-64 GNU/Linuxでのみ利用可能である。）</p> 
 <p style="margin-bottom: 0in" class="western">注目すべき新しいコンパイラのターゲットには、64ビットのARM（AArch64）と32ビットARMv8アーキテクチャが含まれている。</p> 
 <p style="margin-bottom: 0in" class="western"><b>言語固有の改善</b></p> 
 <p style="margin-bottom: 0in" class="western">C++への切り替えを終えたことだけが、このリリースの注目すべき成果ではない。コンパイラーの幾つかの領域で改善が行われた。GCCは、複数のアーキテクチャで、 GNU/Linux と Solaris向けに Go 1.1の先行バージョンをサポートしている。 Fortran と Cも、もしこれらを言語で開発しているなら、調査する価値のある、幾つものアップデートが行われた。</p> 
 <p style="margin-bottom: 0in" class="western"><span lang="en-US">C++ユーザーには、<a class="western" target="_blank" href="http://gcc.gnu.org/gcc-4.8/cxx0x_status.html">C++11サポートの改善</a>がある。</span></p> 
 <ul> 
  <li>thread_localキーワード</li> 
  <li>属性シンタックス</li> 
  <li>アラインメント指定子</li> 
  <li>継承コンストラクタ</li> 
  <li>forward_listは、アロケータ対応のコンテナの要件を満たしている</li> 
 </ul> 
 <p style="margin-bottom: 0in" class="western">GCC4.8のC++11サポートは、<a class="western" target="_blank" href="http://clang.llvm.org/cxx_status.html">Clang 3.2</a>と比較して非常に優位であり、これらのコンパイラーの両方共、<a class="western" target="_blank" href="http://www.infoq.com/news/2012/11/nov12CTP;jsessionid=16D4D66395D8F55EB94B26C15F4A5D8E;jsessionid=E3373EF6481F2039C13BC8EAEB8F218E">Visual Studio 2012の November CTP</a>の最新のサポートを引き離している。将来のC++の変更に対応する計画が始まっており、 <a class="western" target="_blank" href="http://isocpp.org/std/status">2017年頃</a>に予定される、標準の次の主要な改定に提案されているフィーチャの実験実装用に<i>-std=c++1y</i>オプションが追加されている。</p> 
 <p style="margin-bottom: 0in" class="western">C++ランタイム標準ライブラリ (libstdc++) では、C+11のサポートが強化され、乱数生成（新X86プロセッサーでのハードウェアサポートを含めて）が改善され、新しい乱数分布が追加された。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
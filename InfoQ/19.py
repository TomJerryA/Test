<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Googleの Goが近々1.1をリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/go_beta1_1;jsessionid=ED5A1FCF78B954AE6A14C246AF2664CD"><em>原文(投稿日：2013/04/11)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p style="margin-bottom: 0in"><span lang="en-US">Googleの Goプログラミング言語バージョン1.1のリリースが近いので、開発者チームは、最新ベータのリリースを<a target="_blank" href="https://groups.google.com/d/msg/golang-nuts/bQDzp4IYI1o/zHOiBy5BvO0J">アナウンス</a>した。これには、新フィーチャの動作するプレビューが提供されている。特に、幾つかのユースケースでは、予想スピードが30%-40%増加した。Goのバージョン1.1は、1年ちょっと前の2012年3月にリリースされ、これまでGoogleは、バグ修正をリリースしてきたが、バージョン1.1は、 <a target="_blank" href="http://tip.golang.org/doc/go1.1">新フィーチャ</a>をもたらすとともに、1.Xバージョンとの後方互換性を維持している。アップデートは、ツールセット、言語フィーチャ、標準ライブラリへの変更に影響する。 </span></p> 
 <p style="margin-bottom: 0in"><b>言語の新フィーチャ</b></p> 
 <ul> 
  <li>0 による整数除算</li> 
  <li><a target="_blank" href="http://tip.golang.org/ref/spec#Method_values">メソッド値</a></li> 
  <li><span lang="en-US">Returnの要求 – 以前は、値を返す関数は、明示的に “return”あるいは panicを呼び出す事が必要だったが、これが<a target="_blank" href="http://tip.golang.org/ref/spec#Terminating_statements">ステートメントを終了させること</a>の追加によって緩和された。</span></li> 
 </ul> 
 <p style="margin-bottom: 0in"><b>ツール/実装</b></p> 
 <ul> 
  <li>gccgo – <a target="_blank" href="http://www.infoq.com/news/2013/03/gcc48_released;jsessionid=3A861514DDE9FC467269B4FFD5020CF7;jsessionid=ED5A1FCF78B954AE6A14C246AF2664CD">バージョン4.8 GCC</a> (GNU Compiler Collection)、２０１３年３月にリリースされたは、Go 1.1を部分的にサポートしているが、５月にリリース予定のGCC 4.8.1は、1.1を完全にサポートする。</li> 
  <li>64ビット実装上でのint/unitは、64ビットとして定義された。このことがこれらの型が32ビットのみであると期待しているプログラムでは問題になる可能性がある。</li> 
  <li>64ビットシステム上でのヒープサイズ – これは数十GBに拡張された（正確なサイズはシステムに依存し、最終決定していない）。</li> 
  <li>go コマンド 
   <ul> 
    <li>コンパイル、テスト、およびコードを実行する際のエラーメッセージがもっと分かりやすくなった。</li> 
    <li>go getを使うために$GOPATH をセットしなければならない。$GOROOTと等しくするのは認められなくなった。</li> 
   </ul> </li> 
  <li>go fix は、1.0.X から 1.1にコードを移行できるように調整された。（1.0.X 以前のコードは、直接 Go 1.1にアップグレードできない）</li> 
  <li>競合の検出 – 競合状態に悩まされている開発者は、go testで新しいオプション<a target="_blank" href="http://tip.golang.org/doc/articles/race_detector.html"> -race</a>の恩恵が受けられる。Linux、OS X と Windows の 64 ビットプラットフォームで現在利用可能だ。</li> 
 </ul> 
 <p style="margin-bottom: 0in">Goの開発者は、いくつか（しかしすべてではない）ユースケースでパフォーマンスの大幅な増加を報告している。これらの増加は、コンパイラのコード生成の改善、より良いマップ実装、ネットワーク アプリケーションにおけるコンテキスト切り替えの削減、ガベージ コレクターの改善によってもたらされた。</p> 
 <p style="margin-bottom: 0in"><span lang="en-US">主要なプラットフォーム(Windows, Linux, OS X,など) で<a target="_blank" href="https://code.google.com/p/go/downloads/list?q=go1.1beta2">利用できる</a>ダウンロードは、バージョン 1.1 Beta 2である。 開発のペースが非常に早いので、より新しいバージョンが出る可能性があり、そして出るだろう、ということに注意して欲しい。開発者は、既存のコードを再コンパイルすることで、新しい1.1のフィーチャを利用できる。</span></p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Erlang/OTP R16Bが並列性を改善</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/erlangR16B_released;jsessionid=BB5C1D5B371B57F614701C5BBCDB4961"><em>原文(投稿日：2013/03/14)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p style="margin-bottom: 0in" class="western">Erlangは並行性とリアルタイム分散システムをサポートすることに重点を置いた汎用目的の関数型プログラミング言語である。先週、Erlang R16Bのリリースされたが、言語の仮想マシンの様々な領域に並列化を増すいくつもの改良がもたらされた。</p> 
 <p style="margin-bottom: 0in" class="western"><span lang="en-US">Erlangは、分散データベース、通信システム、Webサーバ、ウォールストリートにおける高頻度取引プラットフォームを含む、幾つもの異なるプロジェクトで使用されている。Erlangを使った著名なプロジェクトや企業には、<a class="western" target="_blank" href="https://github.com/blog/112-supercharged-git-daemon">GitHub</a>、高頻度取引、そしてマルチプレイヤーゲームサーバー（すなわち<a class="western" target="_blank" href="http://lanyrd.com/2011/erlang-factory-london/sgwyq/">Call of Duty</a>）がある。</span></p> 
 <p style="margin-bottom: 0in" class="western"><span lang="en-US">Erlangもこの新リリースには、<a class="western" target="_blank" href="http://www.erlang.org/download/otp_src_R16B.readme">リリースノート</a>に記載されている広範な変更があり、改善点の中に注目すべき幾つもの項目がある。第一は、Erlangの仮想マシンは、プロセスの内部処理を改善したということである。これによって、並列に読み出しと書き込みができるので、プロセスの生成と終了中に競合を削減することによって、パフォーマンスが改善される。</span></p> 
 <p style="margin-bottom: 0in" class="western">ポート処理が大幅に改善され、この領域で並列に読み出しと書き込みができるようになった。これは、動的にポートを割り当てられるErlangの新機能と1023から65536にデフォルトのポート上限の引き上げたことの組み合わによる。プログラマーは、新しいシステムの一つの結果は、信号が本当に非同期に配信されるようになったことに注意すべきである。以前、信号が特定の配信順序を持っていたかもしれないが、その順序は、もはや想定しないか、依存することはできない。結果として、 「...これは、信号送出順序について誤った仮定をしたErlangのプログラムが、以前成功した場合でも失敗する、原因になり得ます。」</p> 
 <p style="margin-bottom: 0in" class="western">Erlangランタイムシステム（ERTS）は、非ブロッキングにおけるコードのローディングサポートを改善した。以前は、Erlangのモジュールをロードするのに、シングルスレッドモデルが使われ、ローディングプロセス中にVMを停止した。このリリースでは、Erlangは非ブロッキング操作をサポートするため、コードの実行を停止させずにコードを読み込むことができるようになった。新しいモジュールのロード中に、SMPシステム上での実行時に、これがVMのパフォーマンスを向上するはずである。</p> 
 <p style="margin-bottom: 0in" class="western">この新リリースは、Windowsの32ビットおよび64ビット、両プラットフォーム用のコンパイル済みバイナリをサポートする。他のプラットフォームでは、それらの適切なパッケージマネージャを介してサポートされる。<a class="western" target="_blank" href="https://github.com/erlang/otp">ソースコード</a>は、GitHubで閲覧することがでる。（R16Bソースの<a class="western" target="_blank" href="http://www.erlang.org/download/otp_src_R16B.tar.gz">アーカイブ</a>もダウンロードすることもできる。）</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
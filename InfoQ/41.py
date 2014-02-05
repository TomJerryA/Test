<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>スレッドモデルを変更したRust 0.9がリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/rust09"><em>原文(投稿日：2014/01/16)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p class="MsoNormal" style="margin-bottom:0.0001pt">Mozillaが支援するシステムプログラム言語<a href="http://www.rust-lang.org/">Rust</a>のバージョン0.9がリリースされた。1.0マイルストーンに向けて，言語として多数の改良が加えられている。Rustはこれまで，長期にわたるサポートと安定性を備えた言語へと進化すべく，多数の変更を受け続けてきた。開発者であるGraydon Hoare氏は，Rustのターゲットは<a href="http://www.infoq.com/news/2012/08/Interview-Rust"><span class="InternetLink">&quot;C++に不満を持つ開発者&quot;</span></a>であり，現代的なプログラム言語でC/C++を置き換えることが目標だ，と語っている。</p> 
  <p class="MsoNormal" style="margin-bottom:0.0001pt">
   <o:p></o:p></p> 
  <p class="MsoNormal" style="margin-bottom:0.0001pt">&nbsp;</p> 
  <p class="MsoNormal" style="margin-bottom:0.0001pt">Rustはオープンソースのプログラム言語で，Windows用には<a href="http://static.rust-lang.org/dist/rust-0.9-install.exe">バイナリインストーラ</a>が，UNIXベースのシステム(FreeBSD, Mac OS X, Linux)用には<a href="http://static.rust-lang.org/dist/rust-0.9.tar.gz">ソースパッケージ</a>が公開されている。
   <o:p></o:p></p> 
  <p class="MsoNormal" style="margin-bottom:0.0001pt">&nbsp;</p> 
  <p class="MsoNormal" style="margin-bottom:0.0001pt">Release 0.9には注目すべき機能がいくつかある。
   <o:p></o:p></p> 
  <ul> 
   <li>動的リンクライブラリと静的リンクライブラリのどちらをビルドするか，開発者が<a href="http://static.rust-lang.org/doc/master/rust.html#linkage">選択</a>できるようになった。
    <o:p></o:p></li> 
   <li>ネイティブライブラリのサポートが拡張された。Rustライブラリのビルドと配布が，ネイティブライブラリを添付することなくできるようになった。
    <o:p></o:p></li> 
   <li>I/Oインフラストラクチャが完全に改訂された。論理的には，すべてのI/O機能が<b>std:io</b>モジュールに配置されている。commモジュール(高レベルの通信を抽象化する)も書き直された。
    <o:p></o:p></li> 
   <li>libgreenとlibnativeという２つのライブラリが新たに作成されたことで，I/Oがいくつか変更されている。Rust標準ライブラリが特定のスケジュール方法にセットされることがなくなった。プログラムをm:n (m個のアプリケーションスレッドをn個のカーネルスレッドにマップする)あるいは1:1(各カーネルスレッドに対してひとつのアプリケーションスレッド)で実行することができる。これによって開発者は，アプリケーションに最高のパフォーマンスを提供するスレッディングモデルを選択可能になった。
    <o:p></o:p></li> 
   <li>マネージドポインタ(@マークで示される)が非推奨となった。Rust開発者はRc (参照カウント付きポインタ)，またはGc(ガベージコレクション対象ポインタ)を使用するコードへの移行を検討する必要がある。
    <o:p></o:p></li> 
  </ul> 
  <p class="MsoNormal" style="margin-bottom:0.0001pt">詳細については，Rust 0.9の公式な<a href="https://github.com/mozilla/rust/wiki/Doc-detailed-release-notes#09-january-2014">リリースノート</a>を参照してほしい。 この言語についてもっと詳しく学びたい開発者には，オフィシャルな<a href="http://static.rust-lang.org/doc/0.9/tutorial.html">Rust Tutorial</a>以外にもさまざまなリソースがある&nbsp;–&nbsp;バージニア大学の<a href="http://rust-class.org/pages/using-rust-for-an-undergraduate-os-course.html">学部向けOSコース</a>ではRustが教えられている。また，Steve Klabnik氏は “<a href="http://words.steveklabnik.com/a-30-minute-introduction-to-rust">A 30 minute introduction to Rust</a>” というドキュメントを準備中だ。
   <o:p></o:p></p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
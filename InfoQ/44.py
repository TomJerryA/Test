<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Internet Explorer 11、新しいF12ツール、タッチ改善、WebGL、WebCrypto 、ハードウェア3Dサポートを追加</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/ie11-developer-features"><em>原文(投稿日：2013/11/07)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>最近リリースされたWindows 8.1に搭載された<a href="http://windows.microsoft.com/en-us/internet-explorer/ie-11-release-preview">Internet Explorer 11</a>には、高速なHTTP転送に加えて、新しいF12ツール、WebGL、ハードウェア3Dサポートが含まれている。F12ツールは、リンクや画像などのページ要素の確認とレポートを可能にし、開発とデバッグをすばやく簡単にするための新しいUIおよび機能を含んでいる。F12ツールには、DOM Explorer、Console、Debugger、Network、UI Responsiveness、Profiler、Memory、Emulationといった8つのツールが含まれており、各ツールごとにタブが用意され、Windows 8のミニマリストインターフェイスで提供される。</p> 
  <p>IE 11には、セキュリティ問題の対策が施された<a href="http://en.wikipedia.org/wiki/WebGL">WebGL</a>のサポートが含まれている。また、高品質のフルスクリーンビデオ再生をもたらすHTML Full Screen API、TTML(クローズドキャプションのSDP標準)、動的TextTracks、Simple Delivery Profile、ストリーミングのXHRキャッシュコントロール、Media Source Extensions (MSE)、Encrypted Media Extensions (EME)を含む最新のHTML5ビデオメディアストリーミング標準、SPDY、さらにはWebCryptoのサポートも提供する。<br /> <br /> IE 11には国際化された日付や時刻フォーマットを扱う<a href="http://www.ecma-international.org/ecma-402/1.0/">ECMAScript Internationalization API</a>のサポートや、ディスクにキャッシュせずにビデオデータをダウンロードする機能も含まれている。これはバッテリーの持ちを良くするのにつながる。</p> 
  <p>またタッチによるhoverシミュレートもサポートしている。さらに開発者は、新しい<a href="http://msdn.microsoft.com/en-us/library/ie/dn254949(v=vs.85).aspx">msZoomTo()</a> APIを使うことで、プログラムからパンとズームをトリガーし、あるエリアをアニメーション付きでスクロールやズームイン、アウトすることができる。またIE 10で取り入れられたタッチ対応HTML5ドラッグ・アンド・ドロップもサポートしている。<br /> <br /> 入ってきた報告によると、IE 11の最終版はプレフィックスなしのポインターイベントをサポートしているようだ。MicrosoftはMSIEおよび互換トークンを削除するのに加え、既存のisIE()コードブランチのような古い機能を削除した。さらに、document.allを削除して、document.getElementById()を利用するようになった。これには以下のIE固有ハンドラの削除も含まれている。</p> 
  <ul> 
   <li>attachEvent()</li> 
   <li>detachEvent()</li> 
   <li>window.execScript()</li> 
   <li>window.doScroll()</li> 
   <li>document.fileSize</li> 
   <li>img.fileSize</li> 
   <li>script.onreadystatechange</li> 
   <li>script.readyState</li> 
   <li>document.selection</li> 
   <li>document.createStyleSheet</li> 
   <li>style.styleSheet</li> 
   <li>window.createPopup</li> 
  </ul> 
  <p>なお、Internet Explorer 11はWindows 7でも利用可能だが、多くのタッチ向けの機能はWindows 8でしか動かないため無効化されている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
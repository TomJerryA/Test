<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>モバイルHTML5の問題は？</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/mobile-html5"><em>原文(投稿日：2013/11/09)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>最近のリサーチによると、HTML5の主な問題は一般的に信じられているパフォーマンスではなく、むしろプロファイルやデバッグのためのツール不足と確かなAPIの欠如にあるようだ。</p> 
  <p>世界中から6,000名を超える開発者からの調査、30,000以上のAndroid Playアプリの分析、42のHTML5フレームワークおよびツールの調査、モバイルHTML5 vs. ネイティブに関する32名のトップエキスパートとのインタビュー結果をもとに、VisionMobileは<a href="http://www.developereconomics.com/downloads/can-html5-compete-native/">How can HTML5 compete with Native?</a>というレポートを公表した。本記事では、そこから重要なところを取り上げる。このレポートでは、HTML5アプリケーションで用いられる市場へのルートを以下の4つに分類している。</p> 
  <ol> 
   <li>モバイルブラウザ – モバイルデバイス向けに、モバイルブラウザで動作するWebアプリやWebサイト</li> 
   <li>ネイティブラッパー – ネイティブラッパーにパッケージ化され、アプリストア経由で配信されるWebアプリ</li> 
   <li>Webからネイティブへのコンバータ – JavaScriptで書かれ、ネイティブコードにコンパイルされたアプリ</li> 
   <li>ネイティブJavaScript API – Firefox OS、Windows 8、Chrome OSなど、ネイティブにサポートするプラットフォーム向けに書かれたHTML5アプリ</li> 
  </ol> 
  <p>レポート結果</p> 
  <ul> 
   <li>開発者の61%はモバイルブラウザ向けに書いている。</li> 
   <li>米国のAndroid Playアプリケーションの63%は、ブラウザに未実装なAPIがあるために、モバイルブラウザ向けのHTML5で書くことが<em>できない</em>。</li> 
   <li>米国のAndroidアプリの37%はHTML5で実装できるが、もしブラウザがPower ManagementとWiFi APIをサポートすると、それは58%になるだろう。</li> 
   <li>開発者の39%はモバイルブラウザ以外の3つの市場へのルート向けにHTML5アプリを作っている。</li> 
   <li>米国のAndroidアプリのうち、49%はネイティブラッパーで、63%はWebからネイティブへのコンバータで、98%はネイティブJavaScriptで、実装することができる。</li> 
  </ul> 
  <p>次のチャートは、HTML5の魅力について示している。</p> 
  <blockquote> 
   <p><a href="/resource/news/2013/11/mobile-html5/ja/resources/html5-native-1 (1).png" target="_blank"><img src="http://www.infoq.com/resource/news/2013/11/mobile-html5/ja/resources/html5-native-1 (1).png" _href="img://html5-native-1 (1).png" _p="true" alt="" /></a></p> 
  </blockquote> 
  <p>次のチャートは、開発者から見たHTML5の不満について示している。</p> 
  <blockquote> 
   <p><a href="/resource/news/2013/11/mobile-html5/ja/resources/1html5-native-2.png" target="_blank"><img src="http://www.infoq.com/resource/news/2013/11/mobile-html5/ja/resources/1html5-native-2.png" _href="img://1html5-native-2.png" _p="true" alt="" /></a></p> 
  </blockquote> 
  <p>多くの開発者はパフォーマンスがHTML5の主な問題だと考えているが、この分野のエキスパートたちをインタビューした結果、このレポートの作者はそれは間違いだと考えた。というのも、新世代のハードウェア、JavaScriptコンパイラの改善、Asm.jsを使うという選択肢などにより、パフォーマンスは自然と改善されつつあるためだ。これには政治が関係している。もっと言うと、主要なブラウザベンダーはモバイルOSベンダーでもあり、各自のアプリストア経由でアプリケーションを配布することに関心があるということだ。GoogleはネイティブのChromeアプリを推奨し、Appleは最新のHTML5を実装しているように見えるが、「WebGLなどのパフォーマンス絡みのAPIは取り残されている」。またレポートによると、HTML5の神話の1つは開発が簡単であることだが、実際には十分なデバッグおよびプロファイルのツールがないため、開発は非常に困難だ。</p> 
  <p>米国のGoogle Playアプリで最も使われているAPIは以下である。</p> 
  <blockquote> 
   <p><a href="/resource/news/2013/11/mobile-html5/ja/resources/html5-native-3.png" target="_blank"><img src="http://www.infoq.com/resource/news/2013/11/mobile-html5/ja/resources/html5-native-3.png" _href="img://html5-native-3.png" _p="true" alt="" /></a></p> 
  </blockquote> 
  <p>現在のHTML5 API標準化状況とブラウザへの導入を以下に示す。</p> 
  <blockquote> 
   <p><a href="/resource/news/2013/11/mobile-html5/ja/resources/html5-native-4.png" target="_blank"><img src="http://www.infoq.com/resource/news/2013/11/mobile-html5/ja/resources/html5-native-4.png" _href="img://html5-native-4.png" _p="true" alt="" /></a></p> 
  </blockquote> 
  <p>次の表は、市場へのルートごとに、実装されると効果があるAPIと、もしそうなれば、どれくらいのアプリがHTML5で実装されるかを示している。</p> 
  <table width="500" border="1" cellspacing="0" cellpadding="2"> 
   <tbody> 
    <tr> 
     <td width="166" valign="top"> <p style="margin-right: 0px;" dir="ltr">市場へのルート</p> </td> 
     <td width="166" valign="top">API</td> 
     <td width="166" valign="top">アプリの%</td> 
    </tr> 
    <tr> 
     <td width="166" valign="top">モバイルブラウザ</td> 
     <td width="166" valign="top">Power management</td> 
     <td width="166" valign="top">13%</td> 
    </tr> 
    <tr> 
     <td width="166" valign="top">ネイティブラッパー</td> 
     <td width="166" valign="top">Power management</td> 
     <td width="166" valign="top">12%</td> 
    </tr> 
    <tr> 
     <td width="166" valign="top">Webからネイティブへの変換</td> 
     <td width="166" valign="top">WiFi</td> 
     <td width="166" valign="top">21%</td> 
    </tr> 
    <tr> 
     <td width="166" valign="top">ネイティブJavaScript API</td> 
     <td width="166" valign="top">Calendar</td> 
     <td width="166" valign="top"> <p>1.4%</p> </td> 
    </tr> 
   </tbody> 
  </table> 
  <p>このレポートは結論として、次のような見解とHTML5への提言を述べている。</p> 
  <ul> 
   <li>ブラウザはPower ManagementとWiFiをはじめとして、もっとHTML5 APIを実装すべきだ。開発者はブラウザベンダーにもっとAPIを実装するようプッシュすべきだ。</li> 
   <li>ネイティブJavaScriptアプリのための標準化されたパッケージング方法が開発されるべきだ。それによって、一度アプリをパッケージ化すれば、それをサポートしている任意のプラットフォームで動かすことができる。</li> 
   <li>クッキー関連の不安やプライバシー懸念を軽減するため、デバイスアイデンティティAPIが開発されるべきだ。</li> 
   <li>開発者はHTML5によりもたらされる可能性、真の利点と欠点について、もっと知識を得るべきだ。</li> 
   <li>デバッグツールの生成を可能にするDebug APIが開発されるべきだ。</li> 
  </ul> 
 </div> 
</div><br><br><br><br><br><br></body></html>
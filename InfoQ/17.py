<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PhoneGap 2.5は、アプリケーションキャッシュとInAppBrowserジオロケーションが使える</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/phone-gap;jsessionid=EAF9906873EF75A09AE0C6B6B7B03575"><em>原文(投稿日：2013/03/05)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://phonegap.com/blog/2013/02/28/pg-250-released/">PhoneGap 2.5</a>がリリースされた。<a target="_blank" href="http://wiki.apache.org/cordova/InAppBrowser">InAppBrowser</a> でアプリケーションキャッシュとジオロケーションが可能となる。またアプリが起動中にユーザーが戻りボタンをクリックすると起きる、ヌルポインター例外の改修が含まれている。更にこのリリースには、また disallowOverscrollと呼ばれる新しい設定パラメータが含まれており、画面の最上部/下部を越えてスクロールしようとしたときの青い輝きを削除できるようになる。</p> 
 <p>PhoneGap 2.5は、config.xmlドキュメントが &lt;widget&gt;の代わりに&lt;cordova&gt; を使うように更新され、<a target="_blank" href="http://docs.phonegap.com/en/2.2.0/guide_plugin-development_ios_index.md.html">CDVPlugin</a>に pluginInitializeメソッドを追加した。更に、<a target="_blank" href="https://github.com/apache/incubator-cordova-ios/blob/master/CordovaLib/Classes/CDVCapture.m">CDVCapture</a>, <a target="_blank" href="https://github.com/hollyschinsky/PGPushNotificationSample/blob/master/platforms/ios/CordovaLib/Classes/CDVSound.m">CDVSound</a>、CDVLocationから<a target="_blank" href="https://github.com/apache/incubator-cordova-ios/blob/master/CordovaLib/Classes/CDVViewController.m">CDVViewController</a>を削除し、CommandDelegateにホワイトリスト方式を追加した。</p> 
 <p>PhoneGap 2.5では、設定を使わずに useSplashScreenを実装し、トップレベルをサブフレームのナビゲーションと区別できるようになった。この最新リリースには、アセットライブラリの応答のための、www/ コピーや正しいMIMEタイプ用のカスタムスクリプトを利用できる機能が提供されている。また<a target="_blank" href="http://mail-archives.apache.org/mod_mbox/cordova-commits/201302.mbox/%3C20130220221628.A371882D71F@tyr.zones.apache.org%3E">CB-571</a>メディアアップデートに対する修正も提供されている。</p> 
 <p>PhoneGap 2.5 は、また CDVPlugin上で<a target="_blank" href="http://uncrustify.sourceforge.net/">uncrustify</a>を走らせることができ、自動的に通知を追加できるので、プラグインがページのロードがいつ起きたかを知ることができ、 FileTransferErrorオブジェクトにbodyプロパティを追加できる機能もある。</p> 
 <p>また、FileTransfer.upload, copyTo, moveTo, getMetadata, readAsDataURL、getFileMetadata メソッドに NATIVE_URIが追加され、アプリテンプレートに<a target="_blank" href="https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSURLCache_Class/Reference/Reference.html">NSURLCache</a>が追加された。この最新リリースは、CDVViewController のユーザーエージェントのロックに対する改修とWindows Phone 7, <a target="_blank" href="http://www.bada.com/">Bada</a>, BadaWac, <a target="_blank" href="http://en.wikipedia.org/wiki/WebOS">WebOS</a>, Tizen, QT, <a target="_blank" href="http://phonegap.com/2012/03/21/introducing-cordova-js/">CordovaJS</a>、<a target="_blank" href="https://github.com/apache/cordova-cli">Cordova CLI</a>へのアップデートを提供している。</p> 
 <p>PhoneGap 2.5は、 AppCacheのサポートを提供し、クイックリターンロジックにNATIVE_URIを追加している。またジオロケーションデータベースエラーの改修も含んでいる。<a target="_blank" href="http://www.windowsphone.com/en-in/how-to/wp8/start/whats-new-in-windows-phone">Windows Phone 8</a> へのアップデートが同梱されおり、ISOファイルが存在するかアップリソースをチェックする。また html+js mimeタイプを追加した。さらに、アイテムがリソースであり、ISOストアの代わりにストリーム使うインスタンスを検知する。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
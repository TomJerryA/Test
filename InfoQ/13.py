<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Cordova 3.3.0を使ってChromeアプリをAndroidとiOSにデプロイする</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/chrome-apps-android-ios-cordova"><em>原文(投稿日：2014/01/29)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>開発者はApache Cordova 3.3.0を使って、ChromeアプリをAndroidとiOSにデプロイできるようになった。</p> 
  <p><a href="http://www.infoq.com/news/2013/12/PhoneGap-3.3">AdobeがPhoneGap 3.3をリリース</a>してから6週間、Cordova 3.3.0が<a href="https://build.phonegap.com/">PhoneGap Build</a>で利用可能になった。Android KitKatのサポートに加えて、Cordova 3.3.0には、Androidにおける<a href="https://developers.google.com/chrome-developer-tools/docs/remote-debugging">ChromeからのリモートWebViewdデバッギング</a>、iOSにおける<a href="http://moduscreate.com/enable-remote-web-inspector-in-ios-6/">Safariを使ったリモートデバッギング</a>のサポートも追加された。リリースノートにはサポートするOSの詳細（<a href="https://github.com/apache/cordova-ios/blob/master/RELEASENOTES.md">iOS</a>、<a href="https://github.com/apache/cordova-android/blob/master/RELEASENOTES.md">Android</a>、<a href="http://cordova.apache.org/announcements/2013/12/16/cordova-330.html#whats_new_in_windows_phone_7__8">Windows</a>）が含まれている。Cordova 2.5.0と2.7.0は近い将来サポートされなくなり、Blackberry、WebOS、Symbian開発者はバージョン2.9.0を使うよう推奨されている。</p> 
  <p>去年の9月に、Googleは<a href="http://chrome.blogspot.ro/2013/09/a-new-breed-of-chrome-apps.html">デスクトップにデプロイできるChromeアプリケーション</a>を生成できることについて発表した（アプリのサンプルが<a href="https://chrome.google.com/webstore/category/collection/for_your_desktop">ここ</a>にある）。これらのアプリはWindows、Mac、Linux上で、オンラインもしくはオフラインモードで動かせる。最近、GoogleはCordova 3.3.0を使って、<a href="http://blog.chromium.org/2014/01/run-chrome-apps-on-mobile-using-apache.html">ChromeアプリをAndroid、iOSといったモバイルプラットフォームにまで拡張した</a>。</p> 
  <p>開発者がモバイル向けのChromeアプリを作るためには、Node.jsと、Android向けにJDK 7、Android SDK 4.4.2、Apache Antを、iOS向けにXcode 5、ios-deploy、ios-simをベースとしたツールチェーンを利用して、Cordovaによってアプリケーションをネイティブシェルにラップし、それからGoogle PlayもしくはApple App Storeに公開する必要がある。</p> 
  <p>次のChrome APIがモバイルアプリ向けに利用可能になっている。</p> 
  <blockquote> 
   <ul> 
    <li><a href="http://developer.chrome.com/apps/identity.html">identity</a> - パスワードプロンプトなしにOAuth2を使ってユーザをサインインする</li> 
    <li><a href="http://developer.chrome.com/apps/google_wallet.html">payments</a> （現在のところAndroidのみ） - モバイルアプリ内で仮想グッズを販売する</li> 
    <li><a href="http://developer.chrome.com/apps/pushMessaging.html">pushMessaging</a> - サーバからアプリにメッセージをプッシュする</li> 
    <li><a href="http://developer.chrome.com/apps/socket.html">sockets</a> - TCPおよびUDPを使ってネットワーク上にデータを送受信する</li> 
    <li><a href="http://developer.chrome.com/apps/notifications.html">notifications</a> （現在のところAndroidのみ） - モバイルアプリからリッチな通知を送る</li> 
    <li><a href="https://developer.chrome.com/apps/storage.html">storage</a> - キー・バリューデータをローカルに格納、取得する</li> 
    <li><a href="https://developer.chrome.com/apps/syncFileSystem.html">syncFileSystem</a> - Google Driveを使ってファイルを格納、取得する</li> 
    <li><a href="http://developer.chrome.com/apps/alarms.html">alarms</a> - タスクを周期的に実行する</li> 
   </ul> 
  </blockquote> 
  <p>このほか、開発者は<a href="http://plugins.cordova.io/#/_browse/all">膨大なCordova API</a>を利用して、さまざまなネイティブ機能にアクセスすることができる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
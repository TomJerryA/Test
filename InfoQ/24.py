<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Androidに関するMicrosoftとAmazonからの最新ニュース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Microsoft-Azure-Amazon-Android;jsessionid=115E0269353062141799DC5E0D24C821"><em>原文(投稿日：2013/03/05)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Microsoft Azureに <a target="_blank" href="https://github.com/WindowsAzure/azure-mobile-services">Android SDK</a> が追加された。Android デバイスを対象とするプッシュ通知を備えている。Amazonも <a target="_blank" href="https://developer.amazon.com/sdk/mobileads.html">Mobile Ads API</a> の提供を開始した。任意のAndroidデバイス上でGoogle AdMobと並行して，同社のネットワークからの広告が表示可能になる。</p> 
 <p><strong>Microsoft Azure Android SDK</strong></p> 
 <p>MicrosoftがAndroid SDK for <a target="_blank" href="http://www.windowsazure.com/en-us/develop/mobile/">Windows Azure Mobile Services</a> を <a target="_blank" href="http://blogs.msdn.com/b/interoperability/archive/2013/03/04/ms-open-tech-develops-the-open-source-android-sdk-for-windows-azure-mobile-services.aspx">発表した</a>。Windows 8とWP8，iOS，Adnroid 用のアプリケーションが，モバイルサービスの支援により，Microsoftクラウドのスケーラブルな環境で動作するさまざまなサービスと通信可能になる。現時点ではデータテーブルの生成と管理，ユーザ認証，プッシュ通知がサポートされている。</p> 
 <p>これらのサービスをAndroidアプリに追加するには，Azureポータルでアプリケーションのスケルトンを作成した上で，そのコードをダウロードしてEclipseにロードすればよい。詳細は <a target="_blank" href="http://www.windowsazure.com/en-us/develop/mobile/tutorials/get-started-android/">このチュートリアル</a> に解説されている。</p> 
 <p>Azure Android SDKには以下の３つのAPIが含まれる。</p> 
 <ul> 
  <li>データ – &quot;クエリとJSONの自動シリアライズ／デジリアライズを備えた，洗練されたAPI&quot; を使用して，Azureテーブルに接続する。</li> 
  <li>Microsoft，Facebooｋ，Twitter，Googleの各アカウントに対応するユーザ認証。</li> 
  <li>サービスフィルタリング – フィルタを備えたパイプラインを生成して，サービス要求／応答の順序付き配信に使用する。</li> 
 </ul> 
 <p>新機能の中で興味深いのは，<a target="_blank" href="http://www.infoq.com/jp/news/2012/08/GoogleCMReplacesC2Dm;jsessionid=757017019B4BAAE96247AD2485891AA2;jsessionid=115E0269353062141799DC5E0D24C821">GCM (Google Cloud Messaging)</a> を通じたAndroidデバイスへのプッシュ配信が提供されることだ。Azure上で動作するサーバがGCMにメッセージを送信し，それがデバイスに転送される仕組みだ。</p> 
 <p>Android SDKはWindows 8やWindows Phone 8，iOS用の他のSDKと同様，<a target="_blank" href="https://github.com/WindowsAzure/azure-mobile-services">GitHubで提供される</a> ことになるはずだ。本記事の執筆時点では，ソースコードはまだGitHubにアップロードされていないが，間もなくそうなるだろう。Android 2.2以降がサポートされる。</p> 
 <p><strong>Amazon Mobile Ads API</strong></p> 
 <p>Amazonが<a target="_blank" href="https://developer.amazon.com/sdk/mobileads.html">Mobile Ads API</a>(ベータ版) をリリースした。Amazonと同社のパートナによる広告を表示することができる。基本的なターゲットは Kindle Fire/HD だが，その他のAndroid携帯やタブレットもサポート対象に含まれる。Amazonの設定した唯一の条件は，必ず同社の <a target="_blank" href="https://developer.amazon.com/welcome.html">Mobile App Distribution Portal</a> を通じてアプリを配信する，というものだ。それさえ満たせば，Google Playなど他のチャネル経由での提供も可能のようだ。APIを利用することで，Amazonの広告と <a target="_blank" href="http://www.google.com/ads/admob/">Google AdMob</a> の両方をアプリで表示できる。</p> 
 <p>Amazonでは，自社製品および他のブランド広告主の&quot;質の高い&quot; 広告によって，&quot;競争力を持った <a target="_blank" href="http://adsense.blogspot.ro/2006/02/ecpm-what-exactly-is-that.html">eCPM</a>&quot; を提供すると約束している。このような明らかに競合する広告がGoogle Play Storeで配信されることに対して，Googleがそれを防ぐために何らかの対抗措置を取るのかどうか，現時点ではまだ分かっていない。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
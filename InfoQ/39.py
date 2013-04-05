<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>共通APIを伴う Windows Azure 通知ハブ</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/01/windows-azure-notification-hubs;jsessionid=5D6F94F7BEADE4F34B6D7C9A8712F991"><em>原文(投稿日：2013/03/24)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="https://manage.windowsazure.com/">Windows Azure 管理ポータル</a>の改善として<a target="_blank" href="http://msdn.microsoft.com/library/jj927170.aspx">Windows Azure 通知ハブ</a> がリリースされ、<a target="_blank" href="http://windows.microsoft.com/en-IN/windows/home">Windows 8</a> や <a target="_blank" href="http://www.apple.com/in/ios/">iOS</a>等のマルチデバイスプラットフォーム向けにビルドされたアプリケーションに対し、プッシュ通知を送るための共通 API を提供する。Microsoft によると、近々<a target="_blank" href="http://www.android.com/">Android </a>と <a target="_blank" href="http://www.windowsphone.com/en-in">Windows Phone</a> もサポートに加える予定だ。</p> 
 <p>Microsoft は数百万の<a target="_blank" href="http://en.wikipedia.org/wiki/Push_technology">プッシュ通知</a>を行う通知ハブを改善した。ユーザを指定するタグの機能をもつメッセージを通知ハブに登録し、メッセージをプッシュ通知する。</p> 
 <p>上記のタグはアプリケーションを指定する文字列（ユーザID、株式銘柄記号等）から構成され、デバイスハンドルの格納/管理や独自のユーザー別通知ルーティング情報の実装を不要とする。さらに、Subルーティング機構により、独自の通知ルーティング・インフラの構築も不要となる。</p> 
 <p>Windows Azure プッシュ通知ハブは、Windows と Linux どちらも選択可能な<a target="_blank" href="http://blogs.msdn.com/b/windowsazure/archive/2012/06/25/infrastructure-as-a-service-series-virtual-machines-and-windows.aspx">Infrastructure-as-a-Service</a>(IaaS) Virtual Machines、Cloud Servie、Web サイトからも利用可能だ。</p> 
 <p>「プッシュ通知を利用することで、ロジックはきわめてシンプルでスケーラブルになるだろう」と、Microsoft社 Server and Tools Business の Corporate Vice President である <a target="_blank" href="http://weblogs.asp.net/scottgu/about.aspx">Scott Guthrie</a> 氏は発言している。</p> 
 <p>Windows Azure 管理ポータルで通知ハブを新規に作成するためには <strong>アプリサービス</strong> カテゴリの配下に存在する<a target="_blank" href="http://msdn.microsoft.com/en-us/library/ee732537.aspx">Service Bus</a>通知ハブを選択する。通知ハブの作成後、通知ハブに登録されたデバイス数、通知ハブにプッシュされたメッセージ数、通知ハブを介して配信に成功したメッセージ数、失敗したメッセージ数を確認できる。</p> 
 <p>同通知ハブはMicrosoft <a target="_blank" href="http://msdn.microsoft.com/en-in/library/windows/apps/hh913756.aspx">Windows Notification System</a> と <a target="_blank" href="http://developer.apple.com/library/mac/#documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/ApplePushService/ApplePushService.html">Apple Push Notification service</a> (APNS) を登録することが可能であり、管理ポータルから<strong>構成</strong>タブをクリックすることで設定可能となる。登録が成功した後、通知ハブに対して任意のクライアントアプリケーション／デバイスを登録可能であり、関連付けたタグでフィルタリングが可能である。この処理を一度実行すれば、少量のコードでユーザに対してブロードキャスト通知をすることが可能となる。</p> 
 <p>Claus Nielsen氏は以下の質問をした。</p> 
 <blockquote>
  Scott、これは凄いニュースだと思います。しかし、Windows7 におけるプッシュ通知やスムースストリーミングの領域では何があるんでしょうか。
 </blockquote> 
 <p>Service Bus の Program Manager である Elio Damaggio 氏は以下の様にコメントしている。</p> 
 <blockquote>
  プッシュ通知ハブの機能は、同機能をサポートしているプラットフォーム（Windows 8、Windows Phone、Android、iOS 等のモバイルプラットフォーム）の OS に対して直接プッシュ通知を行うよう設計されている。
  <br /> 
  <br /> Windows 7 や他の OS で動作しているアプリケーションに対してメッセージをプッシュするためには、Service Bus Topicsを利用できる。2000 サブスクリプション以上を共有できるよう取り扱うか、SignalR (http://signalr.net/)を利用する必要があるが、同機能はすでに Service Bus を利用したスケールアウト構成が可能なよう設計されている。 
 </blockquote> 
 <p>Tomasz Wisniewski氏は、Elio氏がコメントしたように Windows Azure モバイルサービスがプッシュ通知がどの様に通知ハブと協調するか知ろうとしている。</p> 
 <blockquote>
  通知ハブはWindows Azureモバイルサービスのプッシュ機能を置き換えるものではなく、補完するするものだ。間もなく、通知ハブは任意のモバイルサービスのバックエンドから利用可能になるだろう。さらに、高スケールのブロードキャスト機能とタグがサポートされる予定だ。 
  <br type="_moz" /> 
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
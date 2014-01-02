<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Twitter、CocoaSPDYをオープンソースに</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/cocoa-spdy"><em>原文(投稿日：2013/12/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Twitterが<a href="https://github.com/twitter/CocoaSPDY">CocoaSPDY</a>を開発し、それをオープンソース化した。CocoaSPDYはOSX (Cocoa)とiOS (Cocoa Touch)向けのSPDYフレームワークで、彼らが以前<a href="http://netty.io/">Netty</a>に寄贈した実装に基づいている。時を同じくして、<a href="https://itunes.apple.com/en/app/twitter/id333903271">彼らのiOSアプリケーション</a>も素のHTTPの代わりにSPDYを使うようアップデートされた。Twitterはこれにより通信遅延を最大30%削減でき、「ユーザのネットワーク状況が悪いとき」ほど改善が顕著に見られると説明している。</p> 
  <p>Twitterは他にも次のような利点があると述べている。リクエストを多重化できること – 連続したリクエストを送信できる、単一のTCPセッションでバラバラのレスポンスを受信できること、サーバからクライアントへメッセージをプッシュできること、リクエストとレスポンスのヘッダを圧縮できること。</p> 
  <p>SPDYフレームワークをプロジェクトに組み込むには、ソースコードもしくはARMかx86/64バイナリを使えばよい。以下のどちらかのコードを使うことで、他のコードを変更することなく簡単にSPDYを有効化し、アプリケーションで利用することができる。</p> 
  <pre><code>SPDYURLConnectionProtocol registerOrigin:@<a href="https://api.twitter.com/">https://api.twitter.com:443</a>];</code></pre> 
  <pre><code>configuration.protocolClasses = @[[SPDYURLSessionProtocol class]];</code></pre> 
  <p><a href="https://github.com/twitter/CocoaSPDY/issues/1">Server Push</a>と<a href="https://github.com/twitter/CocoaSPDY/issues/2">Discretionary/Deferrable Request Scheduling</a>はまだ動かないが、今後実装される予定だ。</p> 
  <p>SPDYは<a href="http://www.belshe.com/">Mike Belshe</a>氏によって開発され、今では多くのGoogleサービスとChromeとの間で使われている。SPDYは<a href="http://www.infoq.com/news/2012/11/http20-first-draft">現在進行中のHTTP 2.0標準化</a>の土台となっている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
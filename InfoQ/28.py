<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>NetflixがSilverlightを見限り，HTML5を選択</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/Netflix-Silverlight-HTML5;jsessionid=D6FBC4549550C6A145DF762C267D89DB"><em>原文(投稿日：2013/04/18)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Netflixは自社のビデオプレーヤを，SilverlightからHTML5に切り替えると発表した。新しいプレーヤは最初Chrome/Chrome OSに実装されるが，間もなくWindowsとMac OS Xにも用意されるという。</p> 
 <p>Netflixでクラウドシステムアーキテクチャのディレクタを務めるAdrian Cockcroft氏によれば，Netflixは北米の <a target="_blank" href="http://www.infoq.com/presentations/Netflix-Architecture;jsessionid=EA262CFEDEC8BB625A2753A2B49A9520;jsessionid=D6FBC4549550C6A145DF762C267D89DB">ダウロードトラフィックの1/3を占めている</a> という。それだけの量のデータが，すべてひとつのSliverlightアプリケーションにストリームされているのだ。しかし今回，それが変わろうとしている。</p> 
 <p>Netflixは先日，Silverlightから <a target="_blank" href="http://techblog.netflix.com/2013/04/html5-video-at-netflix.html">HTML5に切り替える意向</a> を発表した。最大の理由として同社が挙げているのは，Microsoftが <a target="_blank" href="http://support.microsoft.com/gp/lifean45#sl5">2021年にSilverlight 5のサポートを終了</a> すると発表しながら，Silverlight 6については何も述べていないことだ。同社はまた，コンテントのストリーミングを行うのにSilverlightプラグインをインストールしなければならない点にも不満を表明している。この種のプラグインのインストールは，セキュリティ上の理由から拒否するユーザもいるのだ。さらにiOS用のSafariやWindows 8/Metro用IEなど，最新のブラウザがプラグインをサポートしていないことも問題視している。<a target="_blank" href="http://www.microsoft.com/getsilverlight/locale/en-us/html/installation-win-SL5.html">Windows 8とLinuxがSilverlight互換オペレーティングシステムに含まれていない</a> ことも，別の問題として加えられるだろう。今回のNetflixの発表に対してもっとも多かったコメントも，Linuxの公式サポートを要求するものだった。</p> 
 <p>Netflixはこれらの問題を，HTML5を採用することで解決するつもりだ。最初のアプリケーションはChrome OS上で開発，テストが行われている。Netflixの要求する数多くのHTML5拡張を実装することにはGoogleも関心を持っていて，それらを &quot;HTML5 Premium Video Extensions&quot; と名付けている。</p> 
 <ul> 
  <li><a target="_blank" href="http://www.w3.org/TR/media-source/">Media Source Extensions</a> – JavaScriptを使用したコンテントのストリーミングを可能にする。これによりWebアプリケーションには，ストリーミングのための適切なCDNの選択手段と合わせて，最初の選択に問題があった場合に変更を行う柔軟性が提供される。</li> 
  <li><a target="_blank" href="https://dvcs.w3.org/hg/html-media/raw-file/tip/encrypted-media/encrypted-media.html">Encrypted Media Extensions</a> – DRMサポートを追加する。</li> 
  <li><a target="_blank" href="http://www.w3.org/TR/WebCryptoAPI/">Web Cryptography API</a> – 暗号化サポートを提供するJavaScript API。視聴者のプライバシを保護するため，Netflixはバックエンドサーバとのほとんどの通信を暗号化している。Netflixは大量のログ情報をサーバに返送している。Cockcroft氏によると，正確には北米の全アップロードトラフィックの約4.5%を占める量だ。</li> 
 </ul> 
 <p>GoogleがWeb Cryptography APIをChromeに実装し終わるまで，現行のNetflixは暗号化にPepperプラグインを使用する。実装完了の時点でHTML5ビデオアプリケーションを公開して，WindowsおよびMac OS Xでテストを行う予定だ。</p> 
 <p>Silverlight終了に関する噂は，少なくとも <a target="_blank" href="http://www.infoq.com/jp/news/2010/09/Silverlight-Web-Apps;jsessionid=EA262CFEDEC8BB625A2753A2B49A9520;jsessionid=D6FBC4549550C6A145DF762C267D89DB">その将来性が取り沙汰された</a> 2010年には始まっていた。各プラットフォーム用のSliverlight 5を2011年にリリースする，と <a target="_blank" href="http://www.infoq.com/jp/news/2011/09/Silverlight-5-RC;jsessionid=EA262CFEDEC8BB625A2753A2B49A9520;jsessionid=D6FBC4549550C6A145DF762C267D89DB">Microsoftは一旦はコミットした</a> が，後にそれを否定する発表した上，<a target="_blank" href="http://www.infoq.com/jp/news/2011/09/Metro-Plug-ins;jsessionid=EA262CFEDEC8BB625A2753A2B49A9520;jsessionid=D6FBC4549550C6A145DF762C267D89DB">IE Metroでは一切のプラグインをサポートしないと決定している</a> のだ。すでにこのような疑念が持たれている以上，Silverlightには将来性がないというのは，確信を持って言えることだろう。似たような問題を抱えたFlashとも合わせると，今後RIAの領域はHTML5に占有されることになりそうだ。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
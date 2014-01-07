<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Glass Developer KitでXamarin Androidを使ったGoogle Glassアプリ開発が可能に</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/glass-developer-kit"><em>原文(投稿日：2013/12/17)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="https://components.xamarin.com/view/googleglass">Glass Developer Kit</a>(GDK)が先日のGoogle開発者イベントでリリースされた。C#とXamarin.Androidを使用して，Google Glass上で動作するネイティブアプリケーションを開発することができる。公式発表によると，APIの大部分は現在すでにAndroidアプリで使用できるものであるため，キット内のツールや機能を探し出すことは容易だという。</p> 
  <p>Glass Developer Kitは，GoogleのGlass Explorer Programに参加する開発者に対して，無償で提供される。Android SDKの<a href="http://developers.google.com/glass/develop/gdk/index">アドオン</a>であるこのキットは，クロスプラットフォームなGlassware APIへのアクセスと合わせて，Google Glassで動作するアプリをC#で記述するためのサンプルデモを提供する。</p> 
  <p>InfoQでは，Xamarinのソフトウェア開発者でASPInsiderの<a href="https://twitter.com/chrisntr">Chris Hardy</a>氏から，Xamarin.AndroidとGoogle Glass Developer Kitに関する詳細を聞くことにした。<br /> <br /> <strong>InfoQ: Xamarin.Androidとは何ですか？</strong></p> 
  <blockquote>
   Xamarin.Androidは，C#言語とCLR(Common Language Runtime)/.NETフレームワークのパワーを使った，ネイティブなAndroidアプリケーションのプログラムを可能にする開発ツールです。
  </blockquote> 
  <p><strong>InfoQ: Google Glassはどのような役割のものなのでしょう？</strong></p> 
  <blockquote>
   Google Glassの目的は，利用者に対して，ポケットからモバイルデバイスを取り出す手間を強いることなく，有益な情報を提供することにあります。この情報は，視野の右上の小さなスクリーンに表示されます。カメラと骨伝導スピーカも内蔵しています。
  </blockquote> 
  <p><strong>InfoQ: Xamarin.Androidベースのアプリケーションを開発するには，どのようなツールが必要なのでしょう？</strong></p> 
  <blockquote>
   <a href="http://xamarin.com/android">Xamarin</a>の公式サイトに，必要なツールの概要が紹介されています。ですがXamarin.Androidの他に，MacではXamarin Studio，WindowsではXamarin StudioかVisual Studio 2010, 2012, 2013のいずれかがあれば作業が可能です。ほとんどの人たちはVisual StudioでXamarin.Androidアプリケーションを開発しています。Visual Studio IDEに慣れている人は多いですから。
  </blockquote> 
  <p><strong>InfoQ: 私がGDKでアプリを開発したとしましょう。Google Glassでどのような情報を見ることができますか？</strong></p> 
  <blockquote>
   スクリーンに表示される情報はすべて見ることができます。スクリーンのすべてにアクセスできますから，何か特別なものを描くことも，WebViewでWebサイトを表示することも， ビデオの再生や付属するカメラの画像を表示する(アプリケーション内でQRコードのスキャンを行う場合は便利でしょう)ことも可能です。一般的には，利用者が見ているものを明確にするために，大きめのテキストで簡潔な情報を表示することになるでしょう。このGoogle Glassディスプレイの表示は，”25インチの高解像度ディスプレイを8フィート離れて見た場合と同等の高精細画面” だと言われています。
  </blockquote> 
  <p><strong>InfoQ: Glass Developer Kitには，Google Glassを所持しないユーザ用のエミュレータは付属しているのでしょうか？</strong></p> 
  <blockquote>
   今のところGoogleは，Google Glassを持たない開発者用のエミュレータを提供していません。私たちとしては，次のリンク: http://www.google.com/glass/start/how-to-get-one/?source=xamarinを通じてサインアップすることをお勧めします。サインアップ後１週間以内(この期間はGoogle次第ですが)に，Google Glass Explorersに参加するための招待状が届くように手配します。
  </blockquote> 
  <p><strong>InfoQ: Xamarin.Androidで開発したGoogle Glassアプリケーションのサンプルプログラムは入手可能なのでしょうか？</strong></p> 
  <blockquote>
   Xamarin.Androidを使った
   <a href="https://www.dropbox.com/s/f1z1r5lzohgsly2/GoogleGlassSampleStopwatch.zip">ストップウォッチ</a>のサンプルプログラムがあります。
  </blockquote> 
  <p><strong>InfoQ: どのようなタイプのアプリケーションが開発できますか？</strong></p> 
  <blockquote>
   あらゆる種類のアプリケーションが開発可能です。特別なタイプのAPIによって制約されたり，Xamarinプラットフォームのために制限を受けたりすることはありません。アプリケーションの例をいくつか挙げてみましょう:
   <br /> 
   <br /> 
   <a href="http://xamarin.com/apps#rdio">Rdio</a>: - このアプリはiOSとWinodws PhoneでもC#で開発されています。
   <br /> 
   <a href="http://xamarin.com/apps#direct-energy">Direct Energy</a>: このアプリはiOS用にもC#で開発されています。
   <br /> 
   <a href="https://play.google.com/store/apps/details?id=com.fds.infiniteflight&amp;hl=en">Infinite Flight</a>: このアプリはiOSとWinodws PhoneでもC#で開発されています。
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
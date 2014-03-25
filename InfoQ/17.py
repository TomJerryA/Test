<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>AmazonがAppStreamの提供を開始</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/amazon-appstream"><em>原文(投稿日：2014/03/13)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Amazonは<a href="http://aws.amazon.com/appstream/">AppStream</a>の提供を開始した。これを使えば、開発者はアプリケーションをAWS上で動かし、さまざまなデバイスへ配信できる。</p> 
  <p>2013年11月の限定公開から4ヶ月後、Amazonはすべての開発者に<a href="http://aws.amazon.com/appstream/">AppStream</a>の提供を開始した。AppStreamを使うと、アプリケーションはAmazonのクラウド上で動作し、インターネット上のさまざまなデバイス上で動作するクライアントアプリケーションに動画や音声、データをストリーミングできる。クライアントアプリは情報のストリームを受け取り表示し、ユーザの入力を捉えてサーバへ送り返す。このアプローチには多くの利点がある。</p> 
  <ul> 
   <li>アプリケーションは単一のプラットフォームで開発、テストできる</li> 
   <li>シンプルなので、クライアントアプリはさまざまなプラットフォーム向けに開発できる</li> 
   <li>アプリケーションはデバイスで制限されないパワフルなサーバで動作させられる</li> 
   <li>アプリケーションの更新はサーバを更新することであり、ユーザに影響を与えずに実行できる</li> 
   <li>ユーザはアプリをダウンロードする必要がない。これは大規模なアプリの場合に効果的</li> 
  </ul> 
  <p>既存のアプリケーションも<a href="http://docs.aws.amazon.com/appstream/latest/developerguide/appstream-downloads.html">AppStream SDK</a>を使ってストリーミングをサポートするようにできる。現時点では、AppStreamはWindowsアプリケーションしかサポートしていないが、クライアントアプリはすべての主要なプラットフォームをサポートしている。Android、iOS、OS X、Windows、Kindle/FireOSだ。また、AmazonはAppStreamの認証や認可、エラー処理などを提供するRESTful APIをラップする<a href="https://github.com/awslabs/aws-appstream-sdk-java/">Java SDK</a>も提供する。AppStreamアプリはAmazonのサービスであるS3、RDS、NoSQL、SQS、SNSを利用できる。</p> 
  <p>AWS上のストリーミングを使うには、アプリケーションはWindows Server 2008以降で動いていなければならない。32ビットアプリケーションもWoW64上で動作する。.NETアプリも大丈夫だ。アプリケーションは<a href="http://en.wikipedia.org/wiki/Yuv">YUV 420動画形式</a>でストリームされる必要がある。Amazonはこのようなアプリケーションのために<a href="http://aws.typepad.com/aws/2013/11/build-3d-streaming-applications-with-ec2s-new-g2-instance-type.html">EC2 G2</a>インスタンスを提供している。これは、3Dグラフィクスのインスタンスで、10つのEC2計算ユニットと2.5 GHzの仮想コア、15 GBのRAM、50 GBのストレージ、4GBのRAMを搭載したNVIDIA GK104 GPUがひとつ搭載されている。</p> 
  <p>しかし、問題もある。クライアントでバイスは通信状態が良好でなければならない。Amazonは秒間720pを30フレームストリーミングするのに3Mbpsの接続を推奨している。アプリケーションがオフラインで動作する場合、オンラインとオフラインの両方の機能をハンドリングしなければならない。</p> 
  <p>またAmazonは11月以降に投入した<a href="http://aws.typepad.com/aws/2014/03/amazon-appstream-now-available.html">サービスの改善</a>も発表した。</p> 
  <blockquote> 
   <ul> 
    <li>自動バージョン解決 - AppStreamはクライアントで使われているSDKのバージョンを検知する。これによって自動的に互換性のあるバックエンドのサービスを構築する。これによって、AppStreamとSDKはクライアント側のアップグレードなしに進化できる。</li> 
    <li>Macクライアントのサポート - OSX SDKが利用できるようになった。これによってMacで動作するクライアントの開発が可能になった。</li> 
    <li>クライアントSDKの改善 - クライアントSDKが改善され、ゲームコントローラーも利用できるようになった。また、キーボードとタッチイベントの入力マッピングモデルも改善された。</li> 
    <li>始めやすさ - ドキュメントとパッケージモデルを改善して、始めてのアプリケーションを簡単に作り動かせるようにした。</li> 
   </ul> 
  </blockquote> 
  <p>AmazonはAppStreamを使って、開発者が軽量なクライアントで動作するグラフィクスをふんだんに使ったアプリケーションを開発するよう呼びかけている。ゲーム、CAD、動画などのアプリだ。一部をサーバで、一部をクライアントで動かすというようなハイブリッドな構成も可能。<a href="http://www.ccpgames.com/en/home">CCPのEve Online</a>は<a href="http://aws.typepad.com/aws/2014/01/amazon-appstream-can-improve-the-new-user-experience-for-eve-online.html">AppStreamを使った大規模なマルチプレイヤーのゲーム</a>だ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Appleが新しいiOS 8 SDKと開発者ツールを発表</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/06/apple-ios8-sdk"><em>原文(投稿日：2014/06/04)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Appleは2014年のWorldwide Developer Conferenceで、新しいモバイルOSであるiOS 8を新しいSDKと開発ツールとともに発表した。4000を超える新しいAPIには、HealthKit、HomeKit、CloudKitなどの新しいフレームワークが含まれており、ゲーミングのプラットフォームとしても強化されている。</p> 
  <ul> 
   <li> <p><strong>Swift</strong></p> <p>The Vergeによれば今回のWWDCでの最大のサプライズは<a href="https://developer.apple.com/swift/">Swift</a>だった。<a href="http://www.infoq.com/news/2014/06/apple-swift">この言語についてはInfoQでもすでに取り上げている</a>。Swiftは完全に新しい言語で、表現力に優れ、クロージャ、複数返却値、ジェネリクス、マップやフィルタなどの関数型プログラミングのパターンをサポートする。また、型推論のようなモダンなプログラミング言語の特徴を取り入れる一方、Objective Cの名前付きパラメータを受け継ぎ、名前空間を導入する。同じプロジェクトで既存のObjective Cのコードと共存できるので、導入しやすい。詳細は<a href="https://itunes.apple.com/us/book/the-swift-programming-language/id881256329?mt=11">&quot;The Swift Programming Language&quot;</a>を見るといいだろう。</p> </li> 
   <li> <p><strong>HealthKit</strong></p> <p><a href="https://developer.apple.com/healthkit">HealthKit</a>は新しいフレームワークであり、ユーザのヘルス情報へアクセスできる。フィットネスアプリはデータをiOS 8に搭載される新しい<a href="http://www.apple.com/ios/ios8/health/">Healthアプリ</a>と共有できる。また、ヘルス情報へはユーザが構成したかたちでもアクセスできるようになる。例えば、栄養管理アプリがフィットネスアプリにカロリー消費などを通知できる。</p> </li> 
   <li> <p><strong>HomeKit</strong></p> <p><a href="https://developer.apple.com/homekit/">HomeKit</a>は家庭での通信と接続デバイスの制御に使われる新しいフレームワークであり、ユーザはアプリを通じて、家庭でデバイスを検知し、構成し、制御用のアクションを作成できる。アクションをグループ化し、Siri経由で実行もできる。また、HomeKit Accessoryプロトコルを定義する。このプロトコルは家庭でのデバイスの構成や家庭を自動化するアプリで利用される。</p> </li> 
   <li> <p><strong>CloudKit</strong></p> <p>CloudKitを使うとアプリはiCloudにユーザのApple IDを使って個人情報を共有せずにログインできる。<a href="http://techcrunch.com/2014/06/02/apple-introduces-cloudkit-toolkit-for-cloud-apps/">TechCrunchによれば</a>、これができなかったが故に、&quot;多くの開発者は、Microsoft Azure、Google Cloud Platform、Amazon Web Servicesのようなサードパーティのソリューションを使わざるを得ず、とても苦しい思いをしていた&quot;。&quot;CloudKit認証、検索、通知のような機能&quot;が加わったおかげでとても楽になる。</p> </li> 
   <li> <p><strong>SpriteKit</strong></p> <p><a href="http://www.apple.com/ios/ios8/developer">SpriteKit</a>はiOS 7で導入され、開発者が2Dゲームを作成できるようになった。iOS 8では、Appleはいくつかの拡張を行い、ゲーム内キャラクタがより自然に動作し、開発者がフォースフィールドや、衝突検知を簡単にできるようにした。また、新しいライディンク効果を生成できるようにした。</p> </li> 
   <li> <p><strong>SceneKit</strong></p> <p><a href="http://www.apple.com/ios/ios8/">SceneKit</a>はiOS 8の新しいフレームワークであり、開発者が3Dでゲームを描画することができる。カジュアルな3Dゲーム開発向けに設計されたようだ。SceneKitは物理エンジン、パーティクルジェネレータと連携し、3Dオブジェクトの動作をスクリプトで記述する簡単な方法を提供する。SpriteKitと完全に統合されているので、開発者はSpriteKitのアセットを3Dゲームに含むことができる。</p> </li> 
   <li> <p><strong>Metal</strong></p> <p>没入度が高いコンソール向け開発者用に開発されたMetalは、A7チップの性能を最高まで引き出すための仕組みだ。<a href="http://toucharcade.com/2014/06/02/ios-8s-new-metal-feature-may-greatly-boost-game-performance/">Touch Arcadeによれば</a>、&quot;専用のゲームコンソールに比べた場合、iOSハードウェアのデメリットはハードウエアに直接アクセスできないことです。iOS上での処理はすべてOpenGLを経由してしまいます&quot;。Metalのおかげで、OpenGLのオーバヘットは少なくなり、&quot;ほとんど問題にならない&quot;。また、<a href="http://www.extremetech.com/gaming/183567-apple-unveils-metal-api-for-ios-8-will-shave-off-opengl-overhead-just-like-mantle-dx12">Appleは10倍</a>の描画性能を実現している。Crytek、Unity、Epic Gamesなどのいくつかのゲームエンジンメーカが<a href="http://www.extremetech.com/gaming/183567-apple-unveils-metal-api-for-ios-8-will-shave-off-opengl-overhead-just-like-mantle-dx12">Metalのサポートを発表している</a>。</p> </li> 
   <li> <p><strong>Touch ID API</strong></p> <p><a href="http://en.wikipedia.org/wiki/Touch_ID">Touch ID</a>は指紋認識機能、現在はiPhone 5Sでのみ利用できる。iOS 8で初めて開発者がTouch IDを使いサードパーティアプリで認証を行えるようになる。</p> </li> 
   <li> <p><strong>PhotoKit</strong></p> <p>iOS 8では、開発者は自分が作った写真アプリを使って、Camera Rollで写真を直接編集できる。事前に写真をインポートする必要はない。</p> </li> 
   <li> <p><strong>Camera API</strong></p> <p>iOS 8では、サードパーティのカメラアプリでエクスポージャ、フォーカス、ホワイトバランスを正確に制御できる。</p> </li> 
  </ul> 
  <p>iOS 8とともに、<a href="https://developer.apple.com/xcode/">AppleはXcode 6のベータ版を披露した</a>。新しいバージョンでは、iOS 8のすべての新しい機能をサポートする。Swiftもサポートする。Xcode 6にはいくつかの改善がなされている。</p> 
  <ul> 
   <li>ビューのスタックの各レイヤの3Dレンダリング。ビューのデバッグや、クリップビュー、オーバラッピングビューの特定を簡単にする。</li> 
   <li>XCTestユニットテストフレームワークを使った性能テストのサポート</li> 
   <li>Interface Builderカンバス内部のSwiftコードのライブレンダリング。プログラムの変更を反映する。</li> 
  </ul> 
  <p>AppleはiOS 8 SDKとXcode 6のベータ版を<a href="https://developer.apple.com/devcenter/ios/index.action">何らかのiOS Developer Programのメンバである登録済み開発者</a>が利用できるようにしている。</p> 
  <p><a href="http://www.apple.com/pr/library/2014/06/02Apple-Releases-iOS-8-SDK-With-Over-4-000-New-APIs.html">Appleの発表によれば</a>iOS 8の最終のリリースは秋に予定されている。互換性のiOSデバイスはすべて無償でアップデートできる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
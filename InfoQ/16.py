<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>アプリのiOS 7対応期限が2月1日に</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/ios7-compatible-apps-by-february"><em>原文(投稿日：2014/01/16)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Appleは先日，iOSのアプリケーションに関して，2月1日までにiOS 7に対応しなければならない，という<a href="https://developer.apple.com/news/">告知を行った</a>。iTunes Storeに新たなアプリケーションやアップデートを提出する場合には，開発にXCode 5を使用することと，アプリケーションをiOS 7に最適化することが必須となる。iOS7に対応するには，現行の<a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/index.html#//apple_ref/doc/uid/TP40006556">iOS Human Interface Guidelines</a>と<a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/TransitionGuide/index.html#//apple_ref/doc/uid/TP40013174">iOS 7 UI Transition Guide</a>に従ったUIの変更や，iOS APIの新バージョンを採用することなどが必要だ。</p> 
  <h3>ユーザーインターフェイスの変更</h3> 
  <p>iOSの7のユーザーインターフェイスでは，コンテンツを明確に表現することが重視されている。開発者はスキューモーフィズム(現実の物を模したユーザインターフェース)や影，枠線といったグラフィック要素の使用を避けて，画面全体をユーザへのデータ提示に使用しなければならない。また，ユーザインターフェース要素は中心的な存在であったり，表示されるコンテントからユーザの気をそらすものであったりしてはならない。コンテント表示の明確化を目指すのに加えて，新しいiOSインターフェースデザインのコントロールは画面上に占めるスペースも少なくなり，これまでより多くのコンテント表示が可能になっている。Appleは開発者に対して，プログラムでUI要素を配置するのではなく，可能な限り自動レイアウト機能を使用するようにアドバイスしている。</p> 
  <p>UILabel, UITextField, UITextViewのテキスト処理が<a href="https://developer.apple.com/library/ios/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/CustomTextProcessing/CustomTextProcessing.html">TextKit</a>をベースとしたものになった。これによってカーニングやハイフネーション，あるいはテキスト要素への画像埋め込みなどの機能が実現されている。また，ポイントやピクセルを使用したフォント指定に代えて，テキストのスタイルによる指定を行うことが可能になった。iOSのテキストスタイルはHTMLのものに近く，”headline” や “body” といった値を指定することができる。実際にレンダリングされるサイズは，ユーザの設定するズーム設定などに従ってiOSが計算する。</p> 
  <p>さらにiOS7は，新しい設計要素やテクニックもUIデザイナに提供する。</p> 
  <ul> 
   <li>半透明: ビューの半透明化が可能になった。 不透明なビューとは違って，コンテントの下にあるものをユーザに意識させることができる。iOS User Interface Guidelinesによれば，これはスライドインメニューや設定パネルのように，一時的にオーバーレイするビューで特に有効な機能だ。</li> 
   <li>奥行き: User Interface Guidelineではデザイナに対して，ユーザに提示するオブジェクト間の関連性を表現する手段として，奥行きと階層化の使用を推奨している。奥行きの印象を与えるため，iOSはユーザインターフェースに疑似3D効果を備える。デバイスを前後や左右に傾けることで，ユーザはコンテント上に浮かんでいるオブジェクトの下をのぞくことができる。</li> 
  </ul> 
  <p>&nbsp;</p> 
  <h3>iOS APIの拡張</h3> 
  <p>iOS 7では，アプリケーションの状態を最新にする手段として，新たに３つの<a href="https://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS7.html#//apple_ref/doc/uid/TP40013162-SW10">マルチタスクモード</a>が提供されている。&quot;フェッチ&quot; モードでは，アプリは定期的にデータ更新をチェックすることができる。開発者がアプリケーションの最小更新間隔を定義すると，iOSがバックグラウンドでアプリをローンチしてデリゲートメソッドを呼び出してくれるので，その中で新しいデータを受信すればよい。ネットワーク状態が良好であるなどの状況をiOSが判断して，更新時間に到達する前にアプリを起動する場合もある。&quot;リモート通知&quot;モードでは，アプリケーションの更新にプッシュ通知が使用される。 iOS 7までは，ユーザが通知を受信してアプリケーションを起動し，アプリがコンテントを更新するまで待たなければならなかった。今後は通知を受信したアプリケーションがバックグラウンドで状態を更新して，それが完了した後にユーザへの通知を行うようになる。</p> 
  <p><a href="https://developer.apple.com/library/ios/documentation/MapKit/Reference/MapKit_Framework_Reference/_index.html#//apple_ref/doc/uid/TP40008210">MapKit</a>は高度なオーバレイ処理を提供する。マップにオーバーレイを追加する場合にも，さまざまなレベルを定義できるようになった。また，MKOverlatViewが廃止されたので，新クラスMKOverlayRenderedに置き換える必要がある。MKDirectionsを使えば，マップアプリケーションにスイッチしなくても，アプリに経路情報を問い合わせることができる。さらにはMKMapSnapshotterを使って，マップリージョンのUIImageを座標や高度，ピッチといったパラメータに基づいて生成，表示することができる。</p> 
  <p>アプリケーションはAirdropやピアツーピア接続を使って，相互に通信することが可能だ。どちらのAPIも近接デバイス検出をベースとしているので，インターネット接続は必要ない。アプリに特定のファイルタイプを登録しておいて，Airdrop経由でそれを受信することもできる。ファイルが新たに受信されるとiOSがアプリケーションをローンチして，デリゲートメソッドをコールしてくれる。ピアツーピア接続を使うことで，近接するデバイス間でサービスの公開と検出が可能になる。一度セッションが確立されれば，デバイス間でメッセージやデータを交換することができるようになる。</p> 
  <p>デバイスがiOS 7をサポートしていなくてもアップデートを提供することは可能だ。その場合は，ユーザがApp Storeからアプリケーションの<a href="http://www.infoq.com/news/2013/09/previous-version-ios-apps">旧バージョンをダウンロード</a>することになる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
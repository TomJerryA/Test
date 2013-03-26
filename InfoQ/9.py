<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PeerJS 0.1.7: ブラウザにおけるP2PのためのWebRTCラッパー</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/peerjs-0.1.7-released;jsessionid=0EF1D87B8E6A0368CA7006B47CE98EA3"><em>原文(投稿日：2013/03/16)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://github.com/michellebu">Michelle Bu</a>氏と<a target="_blank" href="http://github.com/ericz">Eric Zhang</a>氏は3月6日、<a target="_blank" href="http://dev.w3.org/2011/webrtc/editor/webrtc.html">WebRTC</a>のラッパーとして<a target="_blank" href="http://peerjs.com/">PeerJS 0.1.7</a>のリリースを発表した。WebRTCはW3CがブラウザでのP2P通信をやりやすくするために作っているものだ。</p> 
 <p>最近、<a target="_blank" href="http://www.w3.org/TR/2011/WD-websockets-20110929/">WebSocket</a>の役割が大きくなっているが、PeerJSはサーバ中心のデータ転送を抜本的に変革するものだ。Bu氏は次のように語っている。</p> 
 <blockquote>
  &quot;WebSocketとWebRTC DataChannelは同じように見えます。どちらもバイナリをサポートしており、あるクライアントから任意のデータを送って、最終的には別のクライアントに届けることができます。ところが、両者には根本的な違いがあります。WebRTC DataChannelを使うと、中央サーバに至る情報がなくても、ピアはお互いにデータを送り合うことができます。たとえば、FacebookやGoogleのチャットを考えてみましょう。すぐとなりに座っている人にメッセージを送るのにも最低1秒はかかります。あなたのコンピュータからFacebookのサーバまで、メッセージは物理的に50、60ホップ経るためです。ネットワークの観点から見て、これは最適であるとは言えません。理想を言えば、このパケットは20フィートほどで届くべきです。WebRTCを使えば、それが可能になります。ネットワークのトポロジーは、1匹の蜘蛛ようなものから、蜘蛛の巣のようなものへと変わっていくのです。」
 </blockquote> 
 <p>この新たなエコシステムを促進すべく、PeerJSは複雑なWebRTC使用をわかりやすいAPIにラップするために作られた。</p> 
 <ul> 
  <li><i>Chromeのバージョン26以降を用意する。</i> 現時点では、<a target="_blank" href="https://www.google.com/intl/en/chrome/browser/canary.html">canary</a>または<a target="_blank" href="https://www.google.com/intl/en/chrome/browser/beta.html">beta</a>バージョンでしか動かない。今後数ヶ月、<a target="_blank" href="http://peerjs.com/status">ブラウザ互換性アップデート</a>でWebRTC実装状況をウォッチしておこう。Bu氏は、この2、3ヶ月でFirefoxの最新版対応できると見積もっている。 <br /> &nbsp;</li> 
  <li><i>PeerServerをセットアップする。</i>ホストされているサービスに<a target="_blank" href="http://peerjs.com/peerserver">サインナップする</a>か、<a target="_blank" href="https://github.com/peers/peerjs-server">ソースを取得</a>して自分でビルドするか、node.jsで<code>npm install peer</code>をしよう。「一度ピアにつながれば、さらなるピアにつなぐ予定がなければもうサーバは不要です」とBu氏は言う。 <br /> &nbsp;</li> 
  <li><i>コードを動かす。</i><a target="_blank" href="https://github.com/peers/peerjs/blob/master/examples/helloworld.html">hello worldのサンプル</a>を見てみよう。「PeerJSは、仲介サーバの構築と実行、複雑なWebRTC PeerConnectionおよびDataChannel仕様の理解、といった問題を軽減します。これにはセットする必要のある無数のハンドラ、考慮する必要のあるエッジケース、ハンドルする必要のあるブラウザの違いが含まれます」Bu氏は言う。</li> 
 </ul> 
 <p>わずかなチャットデモを除き、PeerJSのサンプルは流動的なWebRTC仕様の影響をほとんど受けていない。例外は、<a target="_blank" href="http://peerkit.com/">PeerKit</a>だ。これはP2P CDNとしてZhang氏が立ち上げた新しいプロジェクトだ。「ネバダの中央サーバからではなく、喫茶店で同じサイトをたまたま閲覧している隣の人から、猫画像が提供される世界を想像してみてください」とBu氏は言う。</p> 
 <p>この1、2年で、ブラウザ間の安全な双方向データ転送に基づく次世代アプリが出てくるだろうが、当面は「（WebRTCは）開発者のお祭りみたいなものです」Bu氏は言う。「クライアントの状態をすべて考えると、取り組むべき技術的課題はたくさんあります。」</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
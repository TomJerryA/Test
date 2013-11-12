<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>EclipseのM2Mプロジェクト</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/eclipse-m2m"><em>原文(投稿日：2013/11/01)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>EclipseConでBenjamin Cab&eacute;氏が<a href="http://m2m.eclipse.org">Eclipseの</a>マシン to マシン(m2m)プロジェクトを<a href="http://www.slideshare.net/kartben/a-guided-tour-of-eclipse-m2m-eclipsecon-europe-2013">紹介</a>した。(InfoQは以前に<a href="http://www.infoq.com/interviews/Benjamin-Cabe-Eclipse-M2M">氏にインタビュー</a>してM2Mプロジェクトの状況について話を聞いている)。</p> 
  <p>2011年、EclipseでM2Mのワーキンググループが立ち上がって以来、さまざまなモノのインターネット(Internet of Things,IoT)プロジェクトが成長してきた。そして、それらのプロジェクトを分類するためのトップレベルのM2Mプロジェクトを作ることが議論され、今年のはじめには少数のプロジェクトだけが残っていたが、その後の半年でM2Mプロジェクトのスコープが大きくなってきた。現時点(またはこれからの予定)では次のようなプロジェクトがある。</p> 
  <ul> 
   <li>組み込み機器向けのLinux上で動くLuaベースのランタイムを提供する<a href="http://eclipse.org/mihini/">Mihini</a>。</li> 
   <li>Luaベースの開発環境を提供する<a href="http://www.eclipse.org/koneki/">Koneki</a>。Mihiniやその他のクラスのマシン向け。OMA-DMプロトコルのためのシュミレータもある。</li> 
   <li><a href="http://mqtt.org">MQTT</a>プロトコルに基づくクライアントを提供する<a href="http://www.eclipse.org/paho/">Paho</a>。MQTTは軽量なメッセージングベースのプロトコル(JMSに似ているがオーバヘッドが少なく、複数の言語に対応)で、目下、OASISで標準化中。また、オープンソースの<a href="http://mosquitto.org">Mosquito</a> MQTTブローカをEclipseへ移行するプロジェクトも行われている。</li> 
   <li>ウェブベースの制御システムとハードウエアデバイス向けのさまざまなドライバ(<a href="http://www.infoq.com/news/2013/10/eclipse-smarthome">InfoQのオーバビュー</a>も参照)を搭載した小型デバイス(Raspberry Piのような)向けランタイムEquinoxをベースにした<a href="http://eclipse.org/proposals/technology.smarthome/">Eclipse SmartHome</a>。</li> 
   <li>EquinoxのようなOSGiランタイムコンテナをベースにした<a href="http://www.eclipse.org/proposals/technology.kura/">Eclipse Kura</a>。組み込み機器向けのOSGi実行環境を提供する。USBやBluetoothで通信して組み込み機器がほかのハードウエアサービスと連携することを可能にする。</li> 
   <li>MQTTやCoAPのようなM2M向けプロトコルに統合されるRESTライブラリ<a href="http://eclipse.org/proposals/technology.ponte/">Eclipse Ponte</a>。<a href="http://github.com/mcollina/qest">Quest project</a>からのコントリビューション。</li> 
   <li>標準的なSCADAハードウエアデバイスの制御やデータ転送を可能にするライブラリ<a href="http://www.eclipse.org/proposals/technology.eclipsescada/">Eclipse SCADA</a>。SNMP、Modbus、OPCのような低いレベルのプロトコルも提供する。</li> 
   <li>デバイス間の相互運用を実現するライブラリセットを提供する<a href="http://eclipse.org/proposals/technology.krikkit/">Eclipse Krikkit</a>。JSONやRESTfulなエンドポイントを利用できる。</li> 
  </ul> 
  <p>更なる情報は<a href="http://m2m.eclipse.org">Eclipse M2M</a>のページで確認できる。上で紹介したプロジェクトへのリンクもある。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
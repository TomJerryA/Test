<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Webix 1.4がリリース，WebSocket, IndexedDB, Data/Grid Suggestをサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/webix-1-4"><em>原文(投稿日：2014/01/15)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://docs.webix.com/desktop__whats_new_1_4.html">Webix 1.4</a>がリリースされた。Data SuggestとGrid Suggestに加えて，WebSoketとIndexedDBをサポートする。Data Suggest機能を使えば，イメージや複雑なHTMLコンテントを選択オプションとして使用することができる。<br /> <br /> <img src="http://www.infoq.com/resource/news/2014/02/webix-1-4/ja/resources/1Figure_1_Webix.png" alt="" _href="img://1Figure_1_Webix.png" _p="true" /></p> 
  <p>またGrid Suggestでは，編集とソート，フィルタをサポートするテーブルからのデータ選択が可能になる。<br /> <br /> <img src="http://www.infoq.com/resource/news/2014/02/webix-1-4/ja/resources/Figure_2_Webix.png" alt="" _href="img://Figure_2_Webix.png" _p="true" /></p> 
  <p>新しくなったWebixでは，WebSocketとindexedDBによるデータの読み込みと保存がサポートされている。WebSocketプロトコルでは，ユーザあるいは他のサーバ上のアクション発生によってデータが更新されたとき，サーバからクライアントに対して通信を行うことができる。一方のIndexedDB機能は，アプリケーションがオフラインで動作するためのものだ。</p> 
  <p>最新リリースには，zindexBaseプロパティやonReadyイベントに加えて，フルスクリーンモード表示などにおけるウィンドウ配置の改善も含まれている。autoConfigオプションや，リストコンポーネントでのキーボードナビゲーション，アイコンボタンのスタイル向上，イベントを自動的に追跡するデータプロセッサなども追加された。</p> 
  <p>InfoQは最新リリースの詳細を知るため，xbsoftwareのVeronica Lindorenko氏と短い会話を交わした。<br /> <strong><br /> InfoQ: 新しい機能は.NETアプリケーションでも動作しますか？</strong></p> 
  <blockquote>
   クライアント側の機能はすべて，.NETを含むすべてのプラットフォームでご利用頂けます。 V1でクライアント側以外に導入されたのはただひとつ，WebSocketのサポートだけです。node.jsを使用した
   <a href="http://weblogs.asp.net/cibrax/archive/2011/12/12/transform-your-iis-into-a-real-time-pub-sub-engine-with-faye-node.aspx">Faye</a>ライブラリをベースとしているので，直接的には.NETに適合しないのですが，
   <a href="http://weblogs.asp.net/cibrax/archive/2011/12/12/transform-your-iis-into-a-real-time-pub-sub-engine-with-faye-node.aspx">IIS</a>とAzureクラウドがあれば使用することが可能です。
  </blockquote> 
  <p><strong>InfoQ: IndexedDBについての情報を詳しく教えて頂けますか？</strong></p> 
  <blockquote>
   IndexDBはブラウザの内部データベースです (Safari以外のすべての最新ブラウザでサポートされています)。バージョン1.4以降はサーバ側のデータベースと同じように，データの読み込みと保存に使用することができます。サーバ側データベースとブラウザデータベースの切り替えは，コード１行で可能です。これを追加した大きな目的は，アプリケーションのオフラインサポートを改善することです。ページがオフラインの場合，すべてのデータ操作はindexDBを使用して行うことができます。その後で接続がオンラインになれば，サーバ側にデータベースと同期を取得することが可能です。
   <br type="_moz" /> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
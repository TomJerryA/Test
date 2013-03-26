<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>StripeがA/BテストフレームワークのAbbaをオープンソース化</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Abba;jsessionid=A0044DA2B7C8D41F1655A2CC0D7D86E6"><em>原文(投稿日：2013/03/15)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="https://stripe.com/">Stripe</a> は，同社の <a target="_blank" href="https://github.com/maccman/abba">Abba</a> というJavaScript A/B テストフレームワークをオープンソースにした。このテスト用にWebアプリケーションをセットアップするには，メインページに次のようなコードを挿入する必要がある。</p> 
 <pre>
&lt;script&gt;
  Abba('test name')
    .control('Test A', function(){ /* ... */ })
    .variant('Test B', function(){ /* ... */ })
    .start();
&lt;/script&gt;</pre> 
 <p>このスクリプトでは <code>Test A</code> というコントロールテストを定義して，すべての処理結果の報告対象にすると同時に，<code>Test B</code>という別のバリアントを定義している。バリアントは複数あってもよい。テストでハンドラが参照される度に，必要に応じてこれがフレームワークからコールされる。コントロールテストではハンドラのない場合もある。</p> 
 <p>テストが開始されると，Abbaは別々のテストに関連付けられたハンドラをランダムに呼び出す。通常はこれによって，サイトで使用されているページが別々に呼び出される。フレームワークが各ユーザ毎に，テスト開始と終了ステータスを保持する。ユーザが改めてWebサイトを参照した時，前回と同じページを表示するようにAbbaを設定しておくことも可能だ。</p> 
 <p>データはMongoDBにストアされ，日毎のビジター数やコンバージョン率 (テストを完了したビジター) を，指定された時間範囲でグラフ表示によって可視化することができる。各バリアントの値は重み付けされ，テスト精度を評価するための<a target="_blank" href="http://en.wikipedia.org/wiki/Standard_score">標準スコア</a> が計算される。結果を日付ないし使用ブラウザでフィルタリングすることも可能だ。</p> 
 <p>Abbaはローカルでもサーバ上でも実行可能である。Heroku上で動作させるための手順書も用意されている。動作にはRuby 1.9.3とMongoDBが必要だ。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
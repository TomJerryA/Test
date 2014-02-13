<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>jQuery 1.11 & 2.1がnpmとBowerで公開</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/jquery-1-11-2-1-0"><em>原文(投稿日：2014/01/24)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>最新のjQueryがnpmとBowerから入手可能だ。パフォーマンスが改善され，いくつかのバグが修正されている。</p> 
  <p>jQueryチームは，人気のJavaScriptライブラリの新たなバージョンとして，1.11と2.1.0を同時にリリースした。ソースと縮小版(minified)ファイルは<a href="http://jquery.com/download/">ダウンロード</a>ページの他に，<a href="https://npmjs.org/package/jquery/">npm</a>と<a href="http://bower.io/">Bower</a>からも入手することができる。その他のパッケージ管理ツールについては，現時点でサポートの予定はない。</p> 
  <p>最新のjQueryは，<a href="http://blog.jquery.com/2014/01/24/jquery-1-11-and-2-1-released/">強制的レイアウトとスタートアップ時のオーバーヘッドの削減</a>によって，パフォーマンスが向上している。</p> 
  <blockquote> 
   <p><b>強制的レイアウトの削減:</b> 今回のリリースで私たちは，時間のかかるレイアウト処理をブラウザに対して不注意に強制している部分の撲滅を目指しました。いくつか発見した中から特に，クラス名を変更する際に発生する可能性のある部分を排除しました。一部のページでは，これによってパフォーマンスが大きく向上します。</p> 
   <p><b>細やかなカスタムビルド:</b>モジュールの定義に<a href="http://en.wikipedia.org/wiki/Asynchronous_module_definition">AMD</a>が使われるようになりました。スペースが限られている場合，ライブラリの小さなサブセットが容易に構築できます。詳しく知りたいのでしたら，詳細を記述した<a href="https://github.com/jquery/jquery#readme">READMEファイル</a>を，誰も見たことのない場所に隠してあります。</p> 
   <p><b>スタートアップオーバーヘッドの低減:</b> 新しいモジュール構造と強制的レイアウトの回避に伴って，機能検出が必要な場合にのみ実行されるようにリファクタを実施しました。機能検出を必要とするAPIを呼び出さない限り，そのコードが実行されることはありません。 従来はページ読み込み時にすべての機能検出が実施されていたため，それが遅れを発生させていました。一般的に小さいのですが，特にモバイルプラットフォームでは余分な時間を加算していたのです。</p> 
  </blockquote> 
  <p>縮小ファイルでは<a href="http://bugs.jquery.com/ticket/14415">開発者の混乱</a>を避けるために，<a href="https://docs.google.com/document/d/1U1RGAehQwRypUTovF1KRlpiOFze0b-_2gc6fAH0KY0k/edit">ソースマップコメント</a>が削除されている。</p> 
  <blockquote> 
   <p>今回のリリースでは，縮小ファイルにはソースマップコメントが含まれていません。 ... ソースマップの生成と配布は引き続き実施しますが，ブラウザがマップファイルのマニュアルでの関連付けをサポートしていない(現時点でサポートしているブラウザはありません)場合には，縮小ファイルの最後に適切なソースマップコメントを追加する必要があります。カスタムビルドプロセスを使用して独自のjQueryファイルを生成する場合，縮小ファイルにはソースマップコメントが含まれているので，マップが生成されます。そのままにしてソースマップを利用することも，編集してマップファイルを完全に無視することも可能です。</p> 
  </blockquote> 
  <p><a href="http://blog.jquery.com/2014/01/16/jquery-1-11-0-rc1-and-2-1-0-rc1-released/">バグ</a>もいくつか修正されている。</p> 
  <p>1.11ブランチが古いブラウザ(IE 6,7,8)をサポートするのに対して，2.1.0ブランチではNode.jsでの開発，ChromeとFirefoxの拡張機能など，従来とは異なるWeb環境のサポートを加えている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
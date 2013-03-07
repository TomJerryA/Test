<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Eclipse Orion 2.0，Node.js を利用したローカル動作をサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Eclipse-Orion-2;jsessionid=25022678CA6197881524232DBADB5C13"><em>原文(投稿日：2013/03/04)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://download.eclipse.org/orion/drops/R-2.0-201302221257/index.html">Eclipse Orion 2.0</a> が先頃リリースされた。Node.js，Projectsなどのサポート，シェルコマンドの改良に加えて，JavaScriptコードアシストとパフォーマンスが改善されている。</p> 
 <p>WebベースのJavaScript IDEとしてOrionが<a target="_blank" href="http://www.infoq.com/jp/news/2012/11/Eclipse-Orion-1;jsessionid=DB9708F7E43B352CB0C87167C3168672;jsessionid=25022678CA6197881524232DBADB5C13">初めてリリースされてから</a> ４ヶ月後，当初予定のとおり，<a target="_blank" href="http://download.eclipse.org/orion/drops/R-2.0-201302221257/index.html">第２の安定バージョン</a> がリリースされたことになる。今回新たに加えられた機能は次のようなものだ。</p> 
 <p><strong>Orionode：</strong> IDEのサーバサイド部分が，ローカルで運用可能なように Node.js を使って再実装された。これによって，ファイルをローカル編集する場合に必要なサーバ上のフットプリントが非常に小さくなった。</p> 
 <p><a target="_blank" href="https://npmjs.org/package/orion">Orionode</a> はまだJavaで書かれたサーバの初期段階程度に過ぎず，サポートする機能も限られている – 基本的なナビゲータ，エディタおよびプラグイン操作，rpmのサポートとNodeアプリケーションの実行が可能なシェルコマンド，静的コンテキストのクライアントキャッシュ，gzip圧縮などだ。OrionodeはJavaサーバを置き換えようというものではなく，ローカルインストレーションのみを対象とするものだ。</p> 
 <p><strong>プロジェクト：</strong> <a target="_blank" href="http://planetorion.org/news/2013/03/orion-2-0-release/">プロジェクトプラグイン</a> を使用して，作業ユニットを定義できるようになった。作業ユニットは，大規模プロジェクトのリソース管理改善を目的とするもので，外部ソースやターゲットにリンクしたさまざまなリソースで構成される。現時点でOrionがサポートするのはHTML5プロジェクトと，<a target="_blank" href="http://www.hickory.ca/2013/01/28/managing-an-sftp-type-website-using-orion/">SFTPサーバ上のリソースをリモートで参照および編集する</a> SFTPプロジェクトの２つだ。</p> 
 <p><strong>シェル： </strong>シェルに多数のコマンドが追加された – プラグインを扱う <em>plugins</em>，利用可能なサービスのインスタンスを一覧表示する <em>service</em>，画面をクリアする <em>clear</em> などだ。</p> 
 <p><a target="_blank" href="http://planetorion.org/news/2013/02/orion-2-0-whats-new-for-shell-page-plug-ins/">シェルコマンドには新たに２つのパラメータ型/戻り値型</a> – JSオブジェクトをバイナリデータで表現する <em>blob</em>，ワークスペースに属するファイルあるいはフォルダを表す <em>file</em> – が追加された。コマンドの出力タイプが <em>file</em> であれば，処理結果はファイルにダンプされる。ディレクトリを含む複数のファイルや，そのコンテンツ全体をパラメータとしてコマンドに渡すことも可能だ。</p> 
 <p><strong>コンテントアシスト： </strong><a target="_blank" href="http://planetorion.org/news/2013/01/orion-2-0-m2-new-and-noteworthy/">JavaScript のコンテントアシスト</a> が改良され，いくつかのケースが追加された。配列値と連想配列の型推論，宣言に先立った変数の推測，使用状況に基づくオブジェクトプロパティの推測などが可能になっている。</p> 
 <p>その他，細かな拡張やパフォーマンスの改善なども実施されている。編集作業のOrionおよびJavaScriptページのロードは，<a target="_blank" href="http://planetorion.org/news/2013/01/orion-2-0-m2-new-and-noteworthy/">要求数で45%，バイト転送サイズで80%削減されている</a>。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
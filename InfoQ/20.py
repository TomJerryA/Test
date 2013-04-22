<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>CouchDB 1.3.0が新しいフィーチャとアルゴリズムの改善を追加</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/couchdb-1-3-0;jsessionid=94A140004B4FA74889B9DA068CC72E36"><em>原文(投稿日：2013/04/11)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://couchdb.apache.org/">CouchDB 1.3.0</a>が<a target="_blank" href="https://blogs.apache.org/couchdb/entry/apache_couchdb_1_3_0">Apache</a> Software Foundationからリリースされたが、IE7のFix _session、<a target="_blank" href="http://www.w3.org/TR/cors/">Cross Origin Resource Sharing</a> (CORS)をサポートし、またURLリライターにおける再起の深さを最大１００呼び出しに制限した。リライターへの再帰呼び出し中に X-CouchDB-Requested-Pathを書き換えることはしなくなり、DB変更のAPIに<a target="_blank" href="http://www.w3.org/TR/eventsource/">Server-Sent Events</a>を追加した。また、最新のリリースでは、 /_config/admins APIを使用するときにパスワードハッシュを同期することができ、 show/list ETagsにユーザー名を含んでいる。</p> 
 <p>CouchDB 1.3.0は、同じバッチでドキュメントを生成し、削除する時に発生する不要なコンフリクトに対する解決を提供している。そしてデータベースに含まれているレプリケータは、IDのチェックポイントで新しいサーバ全域のUUIDを利用して、効率的レジュームの可能性を改善している。また、JS<a target="_blank" href="http://lenaherrmann.net/2010/04/28/writing-a-testsuite-for-the-couchdb-api">テストスイート</a>をCLIに移し、トラックバックとテストの信頼性を改善している。</p> 
 <p>この最新リリースは、<a target="_blank" href="http://answers.oreilly.com/topic/1395-introduction-to-couchdbs-futon-administration-interface/">Futon</a>テストスイートへのリンクを無効にし、Futonにビューリクエスト期間を追加した。更に、ユーザーに許可が無いボタンは無効にしている。またGitチェックアウトから直接ビルドするなら、<a target="_blank" href="http://lists.gnu.org/archive/html/autotools-announce/2008-09/msg00002.html">Autoconf v2.63</a> が必要である。公式情報によれば、Futonテストスイートがwebブラウザから走ると問題を起こすので、CLIから利用できるようにした。</p> 
 <p>CouchDB 1.3.0では、パスワードは、<a target="_blank" href="http://en.wikipedia.org/wiki/PBKDF2">PBKDF2</a> (パスワードベースのキー導出関数2)アルゴリズムを使って、設定可能ワークファクタによってハッシュされている。またutc_idアルゴリズムをサポートしている。データベース名は、改善されたC/C++コンパイラの検出機能を使って、書き換えている間にエンコードされる。また新たな要求に応じて、書き換えカウンタをリセットし、CouchDBのスクリプト内でプロセスが存在する前に、停止状態に戻る問題を修正した。</p> 
 <p>CouchDB 1.3.0は、WindowsとOS X用のビルド済パッケージを含み、マニュアルはFutonから直接ホストされる。Apacheはまた、インストールパッケージと一緒にPDF形式のマニュアルを提供している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
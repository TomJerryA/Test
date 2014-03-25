<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Espresso LogicがDBaaSのストアドプロシージャを呼び出せるRESTful APIを提供</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/espresso-logic-dbaas-rest-api"><em>原文(投稿日：2014/03/14)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://www.espressologic.com/">Espresso Logic</a>が同社のDBaaSサービス用のストアドプロシージャにRESTfulなエンドポイントを追加した。</p> 
  <p>Espresso Logicは企業向けにRESTfulなAPIを使ってDBaaSサービスを提供している。データベースのスキーマを分析し各テーブル向けのRESTエンドポイントを作成して、フィルタリングやソート、認証やページネーション、楽観的ロックを提供する。Espressoは近頃、データベースのストアドプロシージャのAPIを自動的に生成し、プロシージャをRESTのリソースとして公開する機能を発表した。呼び出しの戻り値はJSONで提供される。DBaaSとのやり取りは<a href="http://eval.espressologic.com/LogicDesigner/#/">Espresso Designer</a>(アカウントが必要)を経由して行われる。これはすべてのリソースに対してロールベースの安全なアクセスを提供する。データベースを使うには、開発者はSQLを使うのではなく、JavaScriptを使ってビジネスロジックを書く。</p> 
  <p>例えば、<code>get_employee</code>ストア度プロシージャを呼び出しには次のURLを<code>GET</code>する。</p> 
  <pre><a href="http://houston.d.espressologic.com/rest/abl/demo/v1/@procedures/get_employee">http://houston.d.espressologic.com/rest/abl/demo/v1/@procedures/get_employee</a></pre> 
  <p>出力は次の通り。</p> 
  <pre>
{<br />&nbsp; &quot;@metadata&quot;: {<br />&nbsp;&nbsp;&nbsp; &quot;href&quot;: &quot;<a href="http://houston.d.espressologic.com/rest/abl/demo/v1/@procedures/get_employee">http://houston.d.espressologic.com/rest/abl/demo/v1/@procedures/get_employee</a>&quot;<br />&nbsp; },<br />&nbsp; &quot;name&quot;: &quot;get_employee&quot;,<br />&nbsp; &quot;remarks&quot;: &quot;given an employee id and a number 'plus_one', adds one to the number and returns the employee info as well as picture, voice and icon&quot;,<br />&nbsp; &quot;args&quot;: [<br />&nbsp;&nbsp;&nbsp; {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;name&quot;: &quot;given_employee_id&quot;,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;type&quot;: &quot;BIGINT&quot;,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;direction&quot;: &quot;IN&quot;<br />&nbsp;&nbsp;&nbsp; },<br />&nbsp;&nbsp;&nbsp; {<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;name&quot;: &quot;plus_one&quot;,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;type&quot;: &quot;BIGINT&quot;,<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;direction&quot;: &quot;IN_OUT&quot;<br />&nbsp;&nbsp;&nbsp; }<br />&nbsp; ]<br />}</pre> 
  <p>同社のCEOであり共同創立者であるR. Paul Singh氏によれば、次のようなデータベースの構成も対応している。</p> 
  <blockquote> 
   <ul> 
    <li>私たちはユーザの領域でユーザのデータベースに接続します。こうするために、ユーザはリバースSSHトンネルを使います。</li> 
    <li>Amazon RDS(MySQL、SQL Server、Oracle)やAzure SQLなどさまざまなクラウドデータベースサービスに接続できます。</li> 
    <li>既存のデータベースから新しいデータベースを作りたいユーザのために、AWSのオプションとしてMySQLを提供している。近い将来にはもっと多くのオプションを追加する予定です。しかし、この機能は現在ベータ版です。</li> 
   </ul> 
  </blockquote> 
  <p>現時点では、EspressoのサービスはAWS上で動作しているが、同社によれば“近い未来に他のクラウドサービスも追加します。現在はMicrosoft Azureをサポートに対応するべく開発中“だ。オンプレミスで動作する企業向けのアプライアンスもある。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
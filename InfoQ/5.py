<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Tom Baeyens氏(jBPM，Alfresco Activitiの作者)，クラウド版BPMの新ベンチャを開始</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/baeyens-activiti;jsessionid=59630CEA3311EA7FCB33C658D77E10E4"><em>原文(投稿日：2013/03/13)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>JBoss <a target="_blank" href="http://www.jboss.org/jbpm/">jBPM</a> (Red Hatが買収) と <a target="_blank" href="http://www.activiti.org">Activiti</a> (Alfresco) のオリジナル作者であるTom Baeyens氏が，ビジネスプロセスを自動化するクラウドベースの新BPM (Business Process Management) ツールの <a target="_blank" href="http://www.effektif.com">Effektif</a> を発表した。新たなベンチャを進めるパートナーは，SaaSとオンプレミスのビジネスプロセスエディタを提供している <a target="_blank" href="http://www.signavio.com">Signavio</a> という，2009年に設立された新興企業だ。Effektifの開発促進と販売体制確立のためにSignavioは120万ユーロを投資している。これに合わせてEffektifは開発拠点をベルギーからドイツのベルリンへ移転し，Signavioの共同CEOであるTorben Schreiter氏が取締役に就任する。</p> 
 <p>Baeyens氏がInfoQに語ったところによれば，このプランの中核をなすのは &quot;BPMをクラウドに移行することにより，ビジネスプロセスの動的側面がより重要なものになる&quot; という発想だ。その結論としてシステムのワークフローは，ビジネスユーザ自身が定義および変更可能なものでなければならない。従来型のBPMNモデラ上にクラウドスケールの実行エンジンを構築しただけでは不十分だ，と氏は主張する。</p> 
 <p>Baeyens氏はEffektifを３つの概念的レイヤで考えている。第１のレイヤはブラウザベースのウィザードだ。ビジネスユーザがタスクやその委譲の定義，入力フォームの作成などを行うためのシンプルなメカニズムを提供する。作業の調整やフィードバックにはEメールを使用する。作成したプロセスをユーザが試行するためのサンドボックスも用意されている。&quot;私たちの狙いは，ビジネスユーザが５分未満で最初の簡単なプロセスを定義できるようにすることです&quot; とBaeyens氏は述べている。</p> 
 <p>第２のレイヤではSalesforceやGoogle Appsなど，他のクラウドベースのパッケージアプリケーションとの統合アダプタが提供されている。コーディングこそ必要ではないが，統合を定義するにはある程度の技術知識は必要だろう。この点はBaeyens氏も認めている。このレイヤでの作業はIT技術者が行うことになりそうだ。</p> 
 <p>最後の第３レイヤは，開発者がワークフローに付加するカスタムソフトウェアを記述する場所だ。ここで採用しているアプローチは <a target="_blank" href="http://aws.amazon.com/swf/">AmazonのSimple Workflow Service</a> のそれに近い。Effektifはシステムの各アクティビティ単位でタスクリストを保持している。開発者はRESTfulなAPIを通じてタスクリストから必要なタスクを参照し，処理結果をクラウドエンジンに返すようなコードを記述する。そこで返された結果がプロセスを起動するトリガになる，という機構だ。プログラムには任意の言語 – Bayens氏によれば &quot;PHP, Java, 他&quot; を使用することができる。同じ機構を使用して，ファイアウォール内にある企業システムとの統合も可能だ。</p> 
 <p>アーキテクチャ面に目を移すと，エンジンはJavaを使って開発され，<a target="_blank" href="http://www.bpmn.org/">BPMN(Business Process Model and Notation) 2.0</a> を採用している。Signavioの共同CEOであるGero Decker氏によると，製品のモデリングプロセスフローには同社のSignavio Process Editorが使われている。&quot;これには素晴らしい副産物があります。Signavioが現在すでに持っているプロセスモデルのインポート機能 (例:<a target="_blank" href="http://www.xpdl.org">XPDL</a>) が，Effektifでも利用できるのです。&quot;</p> 
 <p>RESTレイヤは <a target="_blank" href="http://restlet.org">Restlet</a> フレームワークを使って構築されている。JSONの処理には <a target="_blank" href="http://wiki.fasterxml.com/jacksonhome">Jackson</a> を，ストレージとしては <a target="_blank" href="http://www.mongodb.org">MongoDB</a> を使用する。フロントエンドのJavaScriptフレームワークについてはまだ未確定だ。</p> 
 <p>Effektifの最初のベータ版は夏頃になる見込みだ。製品の公開は今年の終わりを目標としている。価格については未定だが，アクティビティインスタンス単位の価格モデルをベースとしたものになりそうだ。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
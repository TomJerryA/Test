<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Rodney Viana氏の.NETデバッグ用WinDbgエクステンション</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/netext"><em>原文(投稿日：2013/11/08)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>.NETアプリケーションの実行が失敗したとき，多くの場合はメモリダンプが残るだけである。Visual Studioではメモリダンプを扱えないので，代わりに<a href="https://en.wikipedia.org/wiki/WinDbg">WinDbg</a>というツールを使わなければならない。このとき合わせて使用されるのが<a href="http://msdn.microsoft.com/en-us/library/bb190764(v=vs.110).aspx">SOS.dll</a>や<a href="http://blogs.msdn.com/b/tom/archive/2011/04/28/now-available-psscor4-debugger-extension-for-net-4-0.aspx">Psscor4.dll</a>といった，.NET固有の詳細情報を取得するエクステンションだ。これらはパワフルではあるが使用が難しいので，時には開発者自身がエクステンションを作ることもある。そのような開発者のひとり，<a href="http://blogs.msdn.com/b/rodneyviana/archive/2013/10/30/hardcore-debugging-for-net-developers-not-for-the-faint-of-heart.aspx">Rodney Viana</a>氏が<a href="http://netext.codeplex.com/">netext</a> 1.6.1をオープンソースプロジェクトとしてリリースした。</p> 
  <p>netextのユニークな部分は，SQLライクな文法を使ってヒープの内容を問合せできることだ。例えば，最近発生したWeb要求のエラー一覧を見たいとしよう。HttpRequestオブジェクトはキャッシュされているので，次のような指示を使ってエラー終了したクエリを探すことができる：</p> 
  <pre><p>!wfrom -type *.HttpContext |<br />where ( ($contains(_request._url.m_String, &quot;http:&quot;)) &amp;&amp; (_response._statuscode != 0n200) ) <br />select $addr(), _request._url.m_String, _response._statusCode</p></pre> 
  <p>サポートされるコマンドは次のものだ：</p> 
  <p>オブジェクトの詳細を表示するコマンド</p> 
  <ul> 
   <li>!wdo - その時点でのオブジェクトまたは配列を，GACまたはStackから表示する。</li> 
   <li>!wselect - その時点でのオブジェクトあるいは配列の全項目のフィールド(とレベルフィールド)を表示する。</li> 
   <li>!wfrom - ヒープオブジェクトのSQLライクな解析を実行する。比較，式評価，インデックス付きのフィルタリングなどの操作が可能だ。</li> 
  </ul> 
  <p>オブジェクトの列挙</p> 
  <ul> 
   <li>!windex – HttpContext型のオブジェクトというように，異なるフィルタに基づくオブジェクトのインデックス付けと表示を行う。</li> 
   <li>!wstack – 独自スタック上のオブジェクトをダンプする。</li> 
   <li>!wheap – インデックスを伴わないオブジェクトの一覧と，ヒープの限定的なサンプリング情報を表示する。</li> 
   <li>!wgchandles – GCルートハンドルをダンプする。</li> 
  </ul> 
  <p>特殊な機能</p> 
  <ul> 
   <li>!wdict – ディクショナリオブジェクトを表示する。</li> 
   <li>!whash – ハッシュテーブルオブジェクトを表示する。</li> 
   <li>!whttp – HttpContextオブジェクト一覧を表示する。</li> 
   <li>!wconfig – メモリ内の .configファイル行をすべて表示する。</li> 
   <li>!wservice – WCFサービスオブジェクト一覧を表示する。</li> 
   <li>!weval – 式リストを評価する。</li> 
   <li>!wclass – &quot;refrect&quot; されたクラス定義 (フィールド，プロパティ，メソッド) を表示する。</li> 
  </ul> 
  <p>さらにアグリゲーションや文字列， XML，配列，リフレクションを操作する<a href="http://netext.codeplex.com/#functions">関数</a>もサポートする。</p> 
  <p>NetextはGNU General Public License バージョン２を適用して公開されている。Rodney Viana氏はMicrosoftの社員だが，この開発は氏の個人的なプロジェクトとして見なされていて，Microsoftのサポートは受けていない。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
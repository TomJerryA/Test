<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>2.0リリースでクラウドへと向かうEclipse Code Recommender</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/10/eclipse-recommenders-20"><em>原文(投稿日：2013/10/31)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>本日のEclipseConでCodetrailsが<a href="http://www.codetrails.com/blog/code-recommenders-20-released">Code Recommenders 2.0のリリースを発表した</a>。Code Recommendersプロジェクトは，ドキュメントの不十分な，あるいは不慣れなAPIで作業する<a href="http://code-recommenders.blogspot.de/2010_03_01_archive.html">サポート開発者</a>たちの意見から生まれたものだ。Eclipse Junoリリーストレインの一部として公開されたCode Recommenders 1.0では，コードの重複パターン解析の結果を開発者に通知することで，この機能を実現していた。</p> 
  <p>最初のリリースには，コアJavaライブラリとさまざまなEclipseオープンソースライブラリに関する知識の集大成が組み込まれていた。この知識ベースによって例えば，現在のコンテキストにもっとも関連の深いメソッドを提示するような，インテリジェントなコード補完が可能になっている。</p> 
  <blockquote> 
   <code> </code> 
   <pre><code> swtTextWidget = new Text(container, SWT.NONE); swtTextWidget.&lt;control+space&gt; </code></pre> 
   <code> </code> 
   <div style="border:solid thin black">
    <code> </code> 
    <ul>
     <code> </code> 
     <li><code>setLayoutData(Object layoutData) : void - Control - 80%</code></li> 
     <code> </code> 
     <li><code>setText(String string) : void - Control - 53%</code></li> 
     <code> </code> 
     <li><code>addModifyListener(ModifyListener listener) : void - Text - 38%</code></li> 
     <code> </code> 
    </ul> 
    <code> </code>
   </div> 
   <code> </code> 
  </blockquote> 
  <p>サポート対象のAPI(上の例ではSWT)を参照するたびに，Code Recommendersは知識ベースを少しずつ，Eclipseサーバから自動的にダウンロードする。</p> 
  <p>Code Recommenders 1.0のコードベースはEclipseのUIコードと強く結び付いていたため，Eclipse IDE以外での利用は非常に難しくなっていた。この問題は今回の2.0リリースには当てはまらない。リコメンデーションエンジンはリファクタされ，Eclipse特有のUIコンポーネントから切り離されているからだ。インテグレーションの方法はまだEclipseのUIに近いようだが，ツール自体はヘッドレスモードでも動作するようになっている。アノテート付きのJavaDocドキュメントを生成することも可能だ。</p> 
  <blockquote> 
   <div style="border:thin solid black"> 
    <p><u>protected Control createDialogArea(Composite parent)</u></p> 
    <p>このダイアログの上部分(ボタンバーより上)を生成して，そのコンテントを返す。</p> 
    <p><b>関連項目:</b> <code> createDialogArea</code>をオーバーライドするサブクラスは，以下のメソッドもオーバーライドする場合が多い：</p> 
    <ul> 
     <li><code>configureShell(Shell):</code> <b>63%</b></li> 
     <li><code>okPressed():</code> <b>51%</b></li> 
    </ul> 
   </div> 
  </blockquote> 
  <p>&nbsp;</p> 
  <p>2.0で実現されたもうひとつのイノベーションは，コード補完を起動したメソッドの名称までも考慮した，コンテキスト対応の新たなリコメンダだ。例えばセッタやcreateメソッド内では，SWTの<code>Text</code>クラスの<code>dispose()</code>メソッドよりも<code>getText()</code>メソッドがコールされる可能性が高い。<code>dispose()</code>メソッドの中ならば，もっともコールされやすい<code>Text</code>のメソッドは<code>dispose()</code>だ。このように外側のメソッドコンテキストから最初の単語(lowerCamelCaseを使用して)をピックすることで，レコメンデーションの精度を向上させることができる。</p> 
  <p>スニペットの共有手段を提供するインキュベーティングプロジェクトの<a href="http://wiki.eclipse.org/Recommenders/Snipmatch">Snipmatch</a>によって，スニペットはひとつの中央場所で共有される。これは2.0リリースには含まれない機能だが，動作は比較的安定しているので，将来のリリースには取り込まれるだろう。</p> 
  <p>2.0リリースをベースに，<a href="https://www.eclipsecon.org/europe2013/eclipse-goes-crowd-code-recommenders-20-future-collaborating-teams">Codetrails Connectがクラウドサポートを追加している</a>。これによって，ライブラリ解析結果をプライベートサーバを使って他のチームメンバと共有したり，<a href="http://www.codetrails.com/connect">公開サーバ</a>を使ってコミュニティ全体と共有することが可能になる。後者の場合，どのコード補完イベント(ドロップダウンリストからコード補完が選択されたとき送信されるイベント)を送信するかは，ホワイトリストパッケージのリストをベースとして詳細に指定することができる。デフォルトリストには，コミュニティでイベントを共有する対象として，さまざまなオープンソースライブラリが挙げられている：</p> 
  <ul> 
   <li>android*</li> 
   <li>com.google.*</li> 
   <li>java.*</li> 
   <li>javafx.*</li> 
   <li>javax.*</li> 
   <li>org.apache.*</li> 
   <li>org.eclipse.*</li> 
   <li>org.jboss.*</li> 
   <li>org.w3c.*</li> 
   <li>org.xml.*</li> 
  </ul> 
  <p>最終的には<a href="http://www.codetrails.com/connect/">Codetrails Connect</a>プラグインの使用によって，プライベートあるいは内部のコードパスがコミュニティサーバに公開されないようにする必要がある。あるいはまた，Codetrailsでホストするプライベートサーバを立てて，すべてのコードをチームメンバが共有するようなことも当然可能だ。</p> 
  <p><a href="http://www.codetrails.com/ctrlflow">ControlFlow Miner</a>という独立ライブラリを使用することで，コンパイル済の既存コードベースを解析して，自分たちでサーバを運用しようという組織向けのリコメンデーションを提供することも可能だ。Code Trailsでも，プライベートサーバの使用を可能にする<a href="javascript:void(0);" www.codetrails.com="www.codetrails.com" connect="connect">いくつかのプランを</a>用意している。将来的には他の言語がCodetrails Connectプラグインでサポートされる可能性もある。</p> 
  <p>Code Recommenders 2.0は<a href="http://marketplace.eclipse.org/content/eclipse-code-recommenders">Eclipse Marketplace</a>および<a href="http://download.eclipse.org/recommenders/updates/stable/">アップデートサイト</a>からインストールできる。Codetrails ConnectあるいはControlFlowサービスに関する詳細は，<a href="http://codetrails.com">Codetrails</a>のWebサイトを参照してほしい。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
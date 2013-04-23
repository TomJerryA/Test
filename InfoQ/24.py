<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>IntelliJ IDEA 12.1がJavaFX 2.0を新たにサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/idea-121;jsessionid=004A3FB3E803A1273439721DC9D5DA29"><em>原文(投稿日：2013/04/16)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>JetBrainsがIntelliJ IDEA 12.1の提供を開始した。Javaクライアントプラットフォームの最新実装であるJavaFX 2.0のフルサポートを実現している。<a target="_blank" href="http://www.youtube.com/watch?v=omuW5M1_s2E&amp;feature=player_embedded">添付のビデオ</a> によれば，サポート範囲は &quot;FXMLマークアップ，カスタムCSS，コード補完，ナビゲーションと検索，リファクタリング，パッケージ用ツール，シーンビルダとの統合&quot; などだ。</p> 
 <p>Java 7のインストールと合わせて，&quot;hello world&quot; タイプのサンプルJavaFX アプリケーションを新規作成するテンプレートが提供される。作成されたサンプルにはレイアウトを記述した.fxmlファイル，コントローラを備えたハンドラ，main クラスが用意されているので，&quot;run&quot; をクリックするだけで動作を確認することができる。プロジェクトに関する機能としては，コード補完や &quot;クィックフィックス&quot; 候補の表示といった，期待されそうなサポートはすべて提供されている。</p> 
 <p>JavaFX用のグラフィカルなUIデザイナはJetBrain自身では提供せず，Oracleの <a target="_blank" href="http://www.oracle.com/technetwork/java/javafx/tools/index.html">Scene Builder</a> を組み込む方法を選択している。Scene Builderでシーンを開いて編集すると，その内容がIDEAに反映される仕組みだ。IDE内で直接シーンを開いて手作業で編集することも，もちろん可能だ。</p> 
 <p>JavaFXのパッケージ構築に関する機能もいくつか用意されているが，開発途中のような印象を与える部分がいくつかある。例えば，IDEのUIによるネイティブなパッケージング操作は，現時点ではサポートされていない。この部分はJavaFX Antタスクの使用に頼らなければならないのだ。このあたりの計画について確認すべくJetBrainsに連絡を取ったが，記事の発表時点では回答を得られていない。ただし <a target="_blank" href="http://blogs.jetbrains.com/idea/2013/03/packaging-javafx-2-applications-in-intellij-idea-121/#comments">こちらのブログ記事</a> によると，バージョン12.1.2での対処が予定されているようなので，JetBrainから返答があれば記事をアップデートしてお伝えしようと思う。</p> 
 <p>JavaFXサポートは無償版であるCommunity Editionにも提供されるが，JavaFX CSSサポートが含まれない点にも注意が必要だろう。この部分はUlitmateの限定機能であるCSSサポートに依存しているためだ。</p> 
 <p>JavaFX 2とは別に，Gradleサポートにも注目の追加オプションが２つある。</p> 
 <p>&nbsp;</p> 
 <p><img alt="" src="http://www.infoq.com/resource/news/2013/04/idea-121/ja/resources/1gradle.jpg;jsessionid=004A3FB3E803A1273439721DC9D5DA29" _href="img://1gradle.jpg" _p="true" /></p> 
 <p>&quot;Gradleラッパを使用する&quot; が選択された場合，IDEは，リンクされたGradleプロジェクトが <a target="_blank" href="http://www.gradle.org/docs/current/userguide/userguide_single.html#gradle_wrapper">ラッパ対応</a> であることを自動的に検出し，プロジェクトのリフレッシュとタスク実行にラッパを使用する。&quot;自動インポートを使用する&quot; オプションはGradleプロジェクトの更新時に，すべてのプロジェクト構造の変更を自動的にピックアップするように指示するものだ (例：build.gradleにライブラリが追加あるいは削除されたとき，IDEからも同時に追加あるいは削除される)。</p> 
 <p>他にも小さな改良が多数あるが，VMの各種言語に固有なものも数多く含まれている。Community，Ultimate両バージョンに共通する改善点は：</p> 
 <ul> 
  <li>Windowsのフルスクリーンモード</li> 
  <li>Groovy 2.1 サポート。新しいアノテーションやコンパイルのカスタマイズが含まれる。</li> 
  <li>Scalaサポートの改善 (文の補完と新コンパイラ)</li> 
 </ul> 
 <p>Ultimateバージョンでは，さらに次のような改善点がある。</p> 
 <ul> 
  <li>Spring Framework 3.2とPlay Framework 2.1のサポート</li> 
  <li>Adobe Gaming SDKサポート</li> 
  <li>CoffeeScript，Dart，TypeScript用のソースマップ経由のデバッガ</li> 
  <li><a target="_blank" href="http://sass-lang.com/">Sass</a> (&quot;Syntactically Awesome Stylesheets&quot;) のサポート改善 (カスタム関数定義，補完，リネームリファクタリング，入れ子形式のプロパティなど)</li> 
 </ul> 
 <p>そして最後に，AppleのMacBook Pro Retinaの所有者にとって間違いなく嬉しいのは，Darkulaテーマの高解像度ディスプレイ <a target="_blank" href="http://www.jetbrains.com/idea/features/darcula_retina.html">サポートが改善された</a> ことだろう。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>CamundaがAlfesco Activitiをフォーク</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Camunda-Forks-Activiti;jsessionid=BFE260CADDB5E6242117CFCC419D92F0"><em>原文(投稿日：2013/03/21)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>ベルリンを本拠とするBPM専門のソフトウェアコンサルタント会社である <a target="_blank" href="http://www.camunda.com">Camunda</a> が Alfesco の <a target="_blank" href="http://www.bpm-guide.de/2013/03/18/camunda-forks-activiti-and-launches-camunda-bpm/">Activiti</a> をフォークして，<a target="_blank" href="http://www.camunda.org/">camunda BPM</a> という新たな製品をローンチすると <a target="_blank" href="http://www.bpm-guide.de/2013/03/18/camunda-forks-activiti-and-launches-camunda-bpm/">発表した</a>。同社がこれまで扱っていた，Activiti ベースのBPM製品である camunda fox の後継となるプロダクトだ。</p> 
 <p>camunda BPM は４つのコンポーネントから構成される。</p> 
 <ol> 
  <li>BPMN 2.0 プロセスエンジン – Javaで実装されている。</li> 
  <li>Cockpit – システムの監視および管理用ツール。</li> 
  <li>Modeler – BPMN プロセスモデリング用の Eclipse プラグイン。</li> 
  <li>Cycle – ビジネスアナリストがBPMNツールで作成したBPMNダイアグラムと，エンジニアがModelerで編集したテクニカルで実行可能なBPMN 2.0 XMLファイルとの同期に使用する。</li> 
 </ol> 
 <p>camunda BPM の主要部分は <a target="_blank" href="http://www.apache.org/licenses/LICENSE-2.0">Apache ライセンス</a>，Eclipse Modeler ツールについては <a target="_blank" href="http://www.eclipse.org/legal/epl-v10.html">Eclipse Public Licence</a> で公開される。WebSphere と WebLogic とのインテグレーション，高負荷シナリオ用の Cockput モニタ用追加モジュールの２つも別途提供されるが，これらはオープンソースではない。</p> 
 <p>両製品で大きく異なる部分のひとつは，camunda BPM がアプリケーションサーバを幅広くサポートしている点だ。Tomcat以外にJBoss AS7 と EAP 6，Glass Fish 3.1，WebSphere 8，WebLogic 12cの上でも動作する。&quot;私たちにはプロセスエンジンの共有と組み込み，というコンセプトがあります。&quot; と，同社の創設者でマネージングディレクタのBernd R&uuml;cker氏は InfoQ に語っている。&quot;それを活用して，稼働するアプリケーションサーバを選びません。さまざまなサーバに対応するというのは，私たちにとって大して難しいことではないのです。&quot;</p> 
 <p>Activiti のプロジェクトリーダである Tijs Rademakers氏は自身の <a href="http://bpmn20inaction.blogspot.co.uk/2013/03/activiti-forked.html">ブログ</a> に&nbsp;&quot;アプリケーションサーバコンポーネントを追加していくという方法も，Activiti プロジェクトにとって相応しい作業でしょう&quot; と書いている。しかし我々とのインタビューで R&uuml;cker 氏は，フォークを行った動機として，技術的な問題と並んで両社の重視する部分の違いが大きかった，と説明している。</p> 
 <blockquote> 
  <p>Alfesco は Activiti を自社ECM (Enterprise Content Managenet) システムの組み込みエンジンとして開発しています。彼らのゴールは開発当初から，同システムの jBPM を置き換えることでした。私たちのシステムでは BPM + Java と呼んでいる部分です。</p> 
  <p>例えば私たちには Zalando というクライアントがあって，膨大な数のオーダ (と全体としてのプロセス数) を毎日発生させています。ECMシステムが処理する業務とは，要求されているものがまったく違うのです。その結果は多くの機能的な相違点に現れています – 例えば Alfesco ではシンプルなワークフローを手軽に設定できることが重要ですが，私たちの目標は BPMN 2.0 を完全にサポートすることにあります。このような違いはさまざまな軋轢を生じさせるものですから，プロジェクトを分離するのに十分な理由となります。</p> 
  <p>もうひとつの理由は，私たちがビジネスとITのアラインメントを重視している点です。 私たちはビジネスアナリストにもコミュニティに参加してほしいと思っています。Activiti のコミュニティで経験したことを繰り返したくないのです。</p> 
 </blockquote> 
 <p>Tijs Rademakers氏と話をしたとき，氏は &quot;プロジェクトをフォークする権利は誰にもある&quot; と言っていた。ただし条件がある。</p> 
 <blockquote> 
  <p>... オープンソースコミュニティに新たな価値を提供できるものでなければなりません。それが可能だと言える，正当な理由が必要なのです。</p> 
  <p>その点で私には，今回のフォークを完全に納得することができません。オープンソースBPMコミュニティに付加価値をもたらさないのではないのか，というのが私の意見です。それどころか，どちらのプロジェクトも同じ Activiti コードベースを使っているため，新機能はすべて重複して実装されることになります。それに camunda がオープンソース化したコンポーネントはすべて，Activiti プロジェクトにとっても同じように必要なものであるはずなのです。</p> 
  <p>統一したプロジェクトとして作業していくという選択が議論されることはありませんでした。事前に意見を交わす機会もなかったのです。ですからフォークという選択は，私たちにとって極めて不愉快な驚きでした。</p> 
 </blockquote> 
 <p>Activiti のオリジナル作者で，BPM をクラウド化する目的のために同じようにプロジェクトを離れた Tom Baeyens 氏についても，プロジェクトの将来に対して懸念を抱かざるを得ない存在のはずだ。しかし Rademakers 氏は，彼については心配していないと言う。</p> 
 <blockquote> 
  <p>ご存知のように Tom は，Joran [Barrez氏] と一緒に Activiti プロジェクトを立ち上げた人物です。BPM を完全にクラウド対応しようという彼の新プロジェクトの方向性には，非常に興味を持って見ていますし，ぜひ成功してほしいと思っています。Tom がプロジェクトを離れたことによる影響は，実際にはそれほど大きくありません。１年ほど前から，彼のプロジェクトへの関与は少なくなっていましたから。私たちは現在でも理想的なコミュニティとチームとして，Activiti の開発に携わっているのです。</p> 
  <p>将来について言えば，私は Activiti の将来はとても明るいと思っています。5.11 と 5.12 のリリースで見て頂いたように私たちは，堅牢な BPMN エンジンをベースとして，非常に多くの新機能 (新しいWebモデラ，操作の容易なプロセスエディタ，JavaScript ベースのプロセスダイアグラム，レポート機能など) を導入することに努力してきました。その結果はコミュニティ拡大や活発なフォーラム，コミュニティによる貢献という形で実を結びつつあります。ですから６月のリリース (5.13) に向けて私たちは，機能的に完成された REST API や JavaScript SDK，さらに簡単になった管理とセットアップ作業など，Activiti の向上を続けていくつもりです。コミュニティやパートナ，Alfesco のサポートする Activitiコア開発チームに恵まれた私たちは，BPM の世界で活動する上で理想的な環境にいると思っています。</p> 
 </blockquote> 
 <p>人気のあるプロジェクトをフォークすることが，リスクを伴う行為であることは間違いない。しかしR&uuml;cker氏は，挑戦に臆することはない，市場にはcamunda BPM の余地があると確信している，と話している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>IBMのNick O'Leary氏がNode-REDで「モノのインターネット」をデモ</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/ibm-node-red-qconlondon"><em>原文(投稿日：2014/05/26)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="https://twitter.com/knolleary">Nick O'Leary</a>氏は先回の<a href="http://qconlondon.com/">QCon London</a>で，<a href="http://en.wikipedia.org/wiki/Internet_of_Things">モノのインターネット(Internet of Things / IoT)</a>に注目したオープンソースプロジェクトの<a href="http://nodered.org/">Node-RED</a>を発表した。IBMの<a href="http://ibm.com/blogs/et">Emerging Technologyチーム</a>が開発したこのプロジェクトは，&quot;ハードウェアデバイス，API，オンラインサービスが画期的な方法で結合された&quot;仮想環境をブラウザ上で実現する。Raspberry Piのような低価格ハードウェアに加えて，開発者が&quot;配管工事に煩わされることなく本来の作業に集中できるようにする&quot;ため，クラウド上でも稼働するのが特徴だ。</p> 
  <p>最初にIoTのユースケースをいくつか紹介した後に，氏は，Node-REDの使いやすさと多能性をデモンストレーションしてみせた。その内容は，自身のWebブラウザ上で，&quot;#qconlondon&quot;というハッシュタグの付いたツイートを処理する小さなメッセージフローを作成して，ツイートの感情分析(sentiment analysis)をする，というものだ。ポジティブなツイートの数が，演台の前に設置されたLEDパネルにシリアルポート経由で表示されるとともに，WebSocketを通じてブラウザ上にも表示された。</p> 
  <p><a href="/resource/news/2014/06/ibm-node-red-qconlondon/ja/resources/Node-RED-WS-Tweet-Demo-QCon-London-2014.png" target="_blank"><img src="http://www.infoq.com/resource/news/2014/06/ibm-node-red-qconlondon/ja/resources/Node-RED-WS-Tweet-Demo-QCon-London-2014-small.jpg" _href="img://Node-RED-WS-Tweet-Demo-QCon-London-2014-small.jpg" _p="true" alt="" /></a></p> 
  <p>このサンプルが特定の問題の解法を示したに過ぎないことを強調しながらも，氏は，オープンデータとAPIの品質向上に寄与する点をメリットとして説明した上で，デバイスとプラットフォームの細分化がそれぞれの問題を難しくしている点を指摘した。すなわち，&quot;相互運用性は半分もなく，APIはすべてバラバラ，異なったプロトコルがたくさんあって，[...]&nbsp;見事なほどの混乱状態です。&quot; 結果的に開発者は，&quot;自分の目的を達成するためよりも，ソリューション同士のつなぎ合わせに時間を浪費&quot;しなければならない。</p> 
  <p>Node-REDの目標はこの状況を変えることにある。Node-REDの持つブラウザベースのエディタでは，使い勝手に優れた機能をカプセル化した，さまざまな種類の&quot;ノード&quot;を&quot;パレット&quot;から選択して&quot;フロー&quot;に接続し，それぞれの動作を設定することができる。作成したフローは，ボタンをクリックするだけで<a href="http://nodejs.org/">Node.js</a>ベースのランタイムに配信が可能だ。例えばTwitterノードは，OAuth認証フローの実行方法とTwitter REST APIの操作手順をカプセル化することで，実装の詳細をすべて開発者から隠ぺいする。</p> 
  <p>QConに参加した<a href="http://davidlaing.com/">David Laing</a>氏はプレゼンテーションの後，Node-REDを試してみるためにその次のセッションを飛ばすことにした。</p> 
  <blockquote>
   Node-REDは，&quot;ＡならばＢ&quot;的なワークフローの優れたオープンソースソリューションです。監視APIからデータを取り出して，ある条件が成立した場合に警告を発する処理ワークフローを，私は２時間以内で構築することができました。
  </blockquote> 
  <p>軽量なランタイムは通常スタンドアロンで動作するが，<a href="http://nodered.org/docs/embedding.html">他のNode.jsアプリへの組み込み</a>も可能だ。さらに先日，ヘッドレスモードでUIを使わずに実行できる機能も追加された。</p> 
  <p>提供されているノードのタイプは，幅広い機能をカバーする。それらが入出力や各機能の有無，特定の機能との統合などによって，次例のように分類されてパレットに表示される。</p> 
  <ul> 
   <li>ハードウェア – Rasperry Pi, BeagleBone Black, Arduino</li> 
   <li>ネットワーク – HTTP, TCP, UDP, MQTT, WebSocket</li> 
   <li>パーザ – CSV, JSON, XML</li> 
   <li>変換 – JavaScript関数, Mustacheテンプレート</li> 
   <li>ソーシャル – Twitter, Twillio, Email, IRC, RSS, XMPP</li> 
   <li>ストレージ – ファイルシステム, MongoDB, MySQL, PostgreSQL, Redis</li> 
   <li>分析 – 感情分析, 統計分析</li> 
  </ul> 
  <p>&quot;関数(Function)&quot;ノードは，<a href="http://nodered.org/docs/writing-functions.html">ユーザの定義したJavaScript</a>をサンドボックス内で実行することで，入力メッセージ(JavaScriptオブジェクト)を，場合によっては複数の出力に変換する。さらに&quot;投入(Inject)&quot;ノードでは，フローの手操作による起動や繰り返し起動，入力内容をエディタのデバッグパネルに表示するノードの&quot;デバッグ&quot;などが可能だ。</p> 
  <p>新しいノードタイプも簡単に作成できる。ノードはそれぞれ，サーバ側の動作を定義したJavaScriptファイルと，エディタ上のノードのインターフェースを定義するHTMLファイルで構成される。<a href="https://www.npmjs.org/">Node.jsパッケージリポジトリ</a>で公開されている何万というモジュールを選択して利用すれば，パレットノードの範囲を拡張して，新たな機能を追加することも可能だ。</p> 
  <p>Node-REDのユーザインターフェースには複数のワークスペースがあり，フローを並行して編集することができる。クリップボードや組み込みライブラリを対象として，フローのエクスポートやインポートにも対応する。シリアライズや転送を容易にするために，フローはJSONで表現される。Node-REDエディタに直接ドラッグ・アンド・ドロップすれば，JSON構造体を個別に登録することも可能だ。公開<a href="http://flows.nodered.org/">フローライブラリ</a>に登録して，他のユーザと情報を共有することもできる。公開されたフローはGitHubに，登録者のプライベートなGistとして保存される。</p> 
  <p>プロジェクトのソースコードとイシュートラックは<a href="https://github.com/node-red/node-red">GitHubで利用可能だ</a>。<a href="https://github.com/node-red/node-red-nodes">別のリポジトリ</a>には，拡張用のノードも公開されている。<a href="http://nodered.org/docs/">資料はメインサイトで</a>，進捗情報や最新状況は<a href="http://blog.nodered.org/">ブログ</a>や<a href="https://twitter.com/NodeRED">Twitter</a>を通じて，それぞれ提供される。コミュニティにより深く関わりたければ，活発な<a href="https://groups.google.com/forum/#!forum/node-red">Googleグループ</a>に参加するのがよいだろう。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
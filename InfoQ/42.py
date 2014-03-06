<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>NightwatchでEnd-to-Endテストを行う</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/nightwatch●"><em>原文(投稿日：2014/02/17)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://nightwatchjs.org/">Nightwatch</a>は、Node.js上で動く受け入れテスト用のフレームワークである。このツールは、Webアプリケーションのテストを自動化するために、<a href="http://docs.seleniumhq.org/docs/03_webdriver.jsp">Selenium WebDriver API</a>を使用している。また、Selenium Serverと相性が悪いJavaScriptやCSSセレクタを使ってEnd-to-Endテストを書くことができるよう、シンプルなシンタックスを用意している。</p> 
  <p>独立して動作し、モックやスタブを使用するBDDやユニットテストとは反対に、End-to-Endテストはできるかぎり本物のシステムのユーザに近い感覚をエミュレーションしようとする。Webアプリケーションの場合、それはブラウザの起動、ページの読み込み、JavaScriptの実行、DOM操作などを意味している。Nightwatchは<a href="http://nightwatchjs.org/guide#usage">シンタックスシュガーを用いて</a>、この目標を達成しようとしているのだ。</p> 
  <pre><p>this.demoTestGoogle = function (browser) {<br />&nbsp;&nbsp;&nbsp;browser<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.url(“http://www.google.com”)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.waitForElementVisible('body', 1000)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.setValue('input[type=text]', 'nightwatch')<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.waitForElementVisible('button[name=btnG]', 1000)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.click('button[name=btnG]')<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.pause(1000)<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.assert.containsText('#main', 'The Night Watch')<br />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;.end();<br />};</p></pre> 
  <p>自動テストを書くプロセスをシンプルにする他に、Nightwatchは開発においてシステムの完全な検証を行うため、<a href="http://nightwatchjs.org/guide#runner-options">継続的インテグレーションパイプラインと統合</a>することもできる。</p> 
  <p>現在の機能一覧は、NightwatchのWebサイトで確認することができる。</p> 
  <ul> 
   <li>シンプルながらも強力なシンタックスは、JavaScriptとCSSのセレクタのみで、テストを素早く記述できるようにする。その他のオブジェクトやクラスを初期化する必要はなく、テストのスペックを記述するだけで良いのである</li> 
   <li>同梱されているコマンドライン版のテストランナーは、グループ化したテストを一度に実行することも、単独で実行することもできる</li> 
   <li>Selenium Serverの自動管理（Seleniumが他のマシン上で実行している時は無効にできる）</li> 
   <li>継続的インテグレーションのサポート（JUnitのXMLフォーマットのレポーティングが組み込まれており、<a href="http://hudson-ci.org/">Hudson</a>や<a href="http://www.jetbrains.com/teamcity/">Teamcity</a>といったビルドシステムのビルドプロセスと統合することができる）</li> 
   <li>CSSセレクタもしくはXpathを用いて、ページ内のエレメントの走査や検証もしくはコマンドの実行を行う</li> 
   <li>アプリケーションに特有のコマンドを実装する必要がある場合、簡単に拡張できる</li> 
  </ul> 
  <p>最近のJavaScript界隈では、<a href="http://phantomjs.org/">PhantomJS</a>とともに受け入れテストを行う上で、Seleniumが最も人気なツールの1つとなっており、それぞれが独自のアプローチをとっている。それは、SeleniumがWebDriver APIと、PhantomJSのCUIのみのWebKitブラウザを使用するというものである。どちらもコミュニティからの強力なサポートがある、非常に成熟したツールである。これらのツールとNightwatchとの大きな違いは、主にシンタックスのシンプルさと継続的インテグレーションのサポートにある。SeleniumとPhantomJSは、コーディング量を増やすことにつながるより冗長なシンタックスを持ち、そしてNightwatchが行っているようなコマンドラインで簡単に設定できる継続的インテグレーションのサポート（JUnitのXMLフォーマットもしくはその他の標準的なアウトプット）を行っていない。</p> 
  <p>それでもなお、Nightwatchはより成熟したツールとなるべく、進化し続けている。Node.jsベースの受け入れテスト用フレームワークである<a href="https://github.com/admc/wd">WD.js</a>開発者のSebastien Vincent氏は、コールバックを管理するために選択した実装に関するいくつかの<a href="https://groups.google.com/forum/#!msg/appium-discuss/m8ypnn6lhLc/jDcugkzA3B8J">批判</a>をGoogleグループで行った。</p> 
  <blockquote> 
   <p>非同期呼び出しが関係している場合、キュー（待ち行列）によるメソッドチェーンは悪いデザインパターンです。何かややこしいことをしようとしたらすぐに、またはちょっとしたものを作るにしても、結局は手動でキューを停止させ、タスクを追加することになります（しかし、おそらくNightwatchはこの私の認識が間違っていることを証明してくれるでしょう）</p> 
  </blockquote> 
  <p>Vincent氏は、NightwatchとSelenium Server間の下位レイヤーの通信プロトコルの貧弱さについても指摘した。</p> 
  <blockquote> 
   <p>Nightwatchは、HTTPプロトコルについて見ただけでも、リトライやタイムアウトに対応していないことや、GETとDELETEメソッドに対してContent-LengthやContent-Typeを設定できないなどの問題があり、成熟には程遠いです。このことはsauce-connectやキューイングといった込み入ったケースにおいて、かなり早い段階で破綻を招くでしょう。</p> 
  </blockquote> 
  <p>こうした批判にも関わらず、このツールは<a href="https://github.com/trending?since=monthly">GitHubの今月（2月）もっとも活発なリポジトリ</a>として注目されており、また<a href="https://twitter.com/nightwatchjs">Twitterアカウント</a>はコミュニティおよび開発者とのやりとりから、フィードバックを受け付けている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
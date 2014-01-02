<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PayPal社がバックエンドをJavaからJavaScriptへ移行</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/paypal-java-javascript"><em>原文(投稿日：2013/11/29)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>PayPal社はJSPとJavaで書かれたレガシーコードを捨て、ブラウザからWebアプリケーションのバックエンドサーバまで、幅広くJavaScriptを採用することに決めた。</p> 
  <p>PayPal社の技術責任者であるJeff Harrell氏は、2つのブログ記事（『<a href="https://www.paypal-engineering.com/2013/06/17/set-my-ui-free-part-1-dust-javascript-templating-open-source-and-more/">Set My UI Free Part 1: Dust JavaScript Templating, Open Source and More</a>』、『<a href="https://www.paypal-engineering.com/2013/11/22/node-js-at-paypal/">Node.js at PayPal</a>』）において、Node.js採用の理由と、Webアプリケーション開発をJavaとJSPからJavaScriptとNode.jsに移行したことによる、いくつかの成果を示した。</p> 
  <p>Harrell氏によると、PayPal社のWebサイトには大量の技術的負債が山積しており、彼らは『技術的負債から脱却し、製品のアジリティ向上や革新を可能とする』ことを必要としていた。まず、Web技術者であるフロントエンドエンジニアと、Javaで開発しているバックエンドエンジニアとの間に深刻な隔たりがあった。UX担当者がWebページのたたき台を作成したい場合、それが動作するように、Javaプログラマにバックエンド側の処理を依頼する必要があった。このことは、彼らの『Lean UX』開発モデルにそぐわなかった。</p> 
  <blockquote> 
   <p>当時の私達のUIアプリケーションは、Javaと、柔軟性に欠けるプロプライエタリソリューションを利用したJSPをベースとしており、密結合かつ素早い変更が難しいものでした。私達のチームは、このアプリケーションに『Lean UX』開発モデルを適用することがふさわしいと思えませんでした。また、素早い変更に対応できなかったため、スクリプト言語でプロトタイプを構築し、それをユーザとテストし、そののち成果物に反映させました。</p> 
  </blockquote> 
  <p>PayPal社は『サーバ側の低レイヤーな技術から分離されており、アプリケーションの言語から独立しているUIを、徐々に改善していけるようなテンプレートエンジン』かつ、複数の環境で動くものを必要としていた。彼らは<a href="https://github.com/linkedin/dustjs">Dust.js</a>（LinkedIn社によって裏付けされたテンプレートフレームワーク）、そしてTwitter社の<a href="https://github.com/twitter/bootstrap">Bootstrap</a>と<a href="https://github.com/bower/bower">Bower</a>（Web向けパッケージマネージャ）に取り組むことに決めた。後ほど追加したものとしては<a href="http://lesscss.org/">LESS</a>、<a href="http://requirejs.org/">RequireJS</a>、<a href="http://backbonejs.org/">Backbone.js</a>、<a href="http://gruntjs.com/">Grunt</a>、そして<a href="http://visionmedia.github.io/mocha/">Mocha</a>がある。</p> 
  <p>Webページのいくつかは再設計されていたが、PayPal社は依然としてレガシー技術の資産を抱えていた。</p> 
  <blockquote> 
   <p>…私達にはレガシーなC++/XSLとJava/JSPの資産があり、そして私達は改善し続けるにつれて、それらのUIを置き去りにしたくありませんでした。JavaScriptテンプレートはこういった用途に最適です。私達は、C++の資産において、Dustをネイティブ並みのレンダリング性能にするために、V8を利用したライブラリを構築しました―これは驚くべき速さでした！Java側では、ビューの描画を行うために、Rhinoと連携したSpring ViewResolverを用いてDustを改善しました。</p> 
  </blockquote> 
  <p>その当時、彼らはまた、新しいWebページのプロトタイピングにNode.jsを使い始めた。Node.jsを『きわめて熟達している』と判断し、製品に適用してみることにしたのである。 彼らは<a href="https://github.com/paypal/kraken-js">Kraken.js</a>も開発したため、『規約レイヤー』を<a href="http://expressjs.com/">Express</a>（Node.jsベースのWebフレームワーク）の最上位に配置した（PayPal社は最近、Kraken.jsをオープンソース化している）。Harrel氏によると、Node.jsで開発すべき最初のアプリケーションは、PaypalのWebページ内で最もアクセスされるページのひとつである、アカウント概要ページだった。しかし、彼らはアプリケーションをより良くスケールできないことを恐れた。そのため、Node.jsが動かなかった場合にフォールバックできるよう、Javaアプリケーションと同じものを作ることに決めた。下記は、それぞれのアプリケーションが必要とした、開発リソースについてのいくつかの成果である。</p> 
  <table cellspacing="0" cellpadding="2" width="500" border="1" unselectable="on"> 
   <tbody> 
    <tr> 
     <td valign="top" width="166">&nbsp;</td> 
     <td valign="top" width="166"><strong>Java/Spring</strong></td> 
     <td valign="top" width="166"><strong>JavaScript/Node.js</strong></td> 
    </tr> 
    <tr> 
     <td valign="top" width="166">環境構築</td> 
     <td valign="top" width="166">0ヶ月</td> 
     <td valign="top" width="166">2ヶ月</td> 
    </tr> 
    <tr> 
     <td valign="top" width="166">開発</td> 
     <td valign="top" width="166">～5ヶ月</td> 
     <td valign="top" width="166">～3ヶ月</td> 
    </tr> 
    <tr> 
     <td valign="top" width="166">エンジニア</td> 
     <td valign="top" width="166">5人</td> 
     <td valign="top" width="166">2人</td> 
    </tr> 
    <tr> 
     <td valign="top" width="166">コードの行数</td> 
     <td valign="top" width="166">不明</td> 
     <td valign="top" width="166">元のコードの66%</td> 
    </tr> 
   </tbody> 
  </table> 
  <p>JavaScriptチームはインフラの初期セットアップに2ヶ月を要した。しかし、少ない時間と人数で彼らは同じ機能のアプリケーションを開発した。彼らは本番環境でテストスイートを実行し、Node.jsアプリケーションはJavaよりもパフォーマンスが向上していると結論づけた。その根拠として、</p> 
  <blockquote> 
   <p>Javaアプリケーションに対して、1秒間に倍のリクエストがありました。初回のパフォーマンス測定結果は、シングルコアのNode.jsアプリケーションと5コアのJavaアプリケーションとを比較したものだったため、この結果はかなり興味深いものでした。この差はさらに広がるものと私達は予想します。</p> 
  </blockquote> 
  <p>さらに</p> 
  <blockquote> 
   <p>同じページのレスポンスにかかる平均時間が、35%減少しました。この結果として、Webページは200ms早く表示されました―ユーザが何かしら確実に気づく程度に。</p> 
  </blockquote> 
  <p>と書かれている。結果として、Paypalは製品のベータ版でNode.jsアプリケーションを使い始めた。そして、今あるアプリケーションをNode.jsに置き換えながら、『ゆくゆくは、ユーザの目に触れるWebアプリケーションをすべてNode.jsで開発する』と決めた。</p> 
  <p>Harrell氏によると、JavaScriptをブラウザ側からサーバ側まで使用する利点の1つとして、『あらゆるレベルの技術において、理解し、ユーザのニーズに対応することができる』1つのチームが受け持つことにより、フロントとバックエンド開発間の隔たりをなくすことが挙げられるという。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
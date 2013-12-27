<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ビヘイビア駆動開発ツール、Jasmine 2.0がリリースされた</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/bdd-jasmine-2-released"><em>原文(投稿日：2013/12/22)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://en.wikipedia.org/wiki/JavaScript">JavaScript</a>の<a href="http://en.wikipedia.org/wiki/Behavior-driven_development">ビヘイビア駆動開発</a>テスティングフレームワーク、<a href="https://github.com/pivotal/jasmine">Jasmine</a>の最新バージョンがリリースされた。今回のリリースには、<a href="http://nodejs.org/">Node.js</a>サポートの改善と品質向上への取り組みが含まれている。バージョン2.0の変更点を以下に挙げる。</p> 
  <ul> 
   <li>NodeのテストをすべてJasmineの<a href="http://en.wikipedia.org/wiki/Continuous_integration">継続的インテグレーション</a>テストの一部に入れることで、Node.jsサポートの品質を強化した。インテグレーションテストには、Firefox、Chrome、Safari、Internet ExplorerといったWebブラウザに対するテストも含まれている。</li> 
   <li>Rubyへの依存がなくなり、Node.jsと<a href="http://gruntjs.com/">Grunt.js</a>に置き換えられた。これによってコード量は削減され、寄贈された機能を追加する前のコミュニティによる検証が簡単になるだろう。</li> 
   <li>自分自身をテストのためのJasmineを追加することで、Jasmineの品質向上に取り組んだ。</li> 
  </ul> 
  <p>以前のバージョンとの後方互換性を壊す変更もいくつか含まれている。</p> 
  <ul> 
   <li>非同期テストの構文が変わった。コールバック関数が提供される。</li> 
   <li>レポーターのインターフェイスが置き換えられた。これによってコールバックの使用方法が変わり、カスタム実装とJasmineの結合度が減少する。</li> 
   <li>等価チェックのためのコードが置き換えられた。振る舞いがこれまでと異なるおそれがある。</li> 
  </ul> 
  <p>こうした変更に加えて、多くの問題とバグも修正されている。そのうちの大部分は、より明確なコーディングスタイルを使った、コードにあるオブジェクトほぼ全てに対する<a href="https://github.com/pivotal/jasmine/blob/master/release_notes/20.md#massive-refactoring-and-better-testing">リファクタリング</a>によるものだ。これはテストの改善と、Jasmine拡張時にコアチームおよびコミュニティの開発が簡単になることを目的としている。<br /> また、2.0での変更を中心に、<a href="http://jasmine.github.io/2.0/introduction.html">Jasmineの紹介</a>もアップデートされた。</p> 
  <p>JasmineはJavaScriptコードのビヘイビア駆動開発テスティングフレームワークだ。他のJavaScriptフレームワークや<a href="http://en.wikipedia.org/wiki/Document_Object_Model">DOM (Document Object Model)</a>には依存していない。<br /> Jasmineユーザ向けの<a href="https://groups.google.com/forum/#!forum/jasmine-js">メーリングリスト</a>には800名以上が参加しており、これまで600ほどのトピックが語られている。今年の春には、Jasmineを使ったJavaScriptテスティングフレームワークに関する本も<a href="http://shop.oreilly.com/product/0636920028277.do">出版されている</a>。</p> 
  <p>Jasmineは<a href="http://pivotallabs.com/author/dwfrank/">Davis W. Frank</a>氏によって作られた。現在は3人の開発者によって<a href="https://github.com/pivotal/jasmine#maintainers">メンテナンスされ</a>、オープンソースプロダクトとしてMITライセンスで公開されている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Koa 0.2.0リリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/koa-0.2.0-release"><em>原文(投稿日：2014/01/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Node.jsベースのWebアプリケーションフレームワーク、<a href="http://koajs.com/">Koa</a> <a href="https://medium.com/code-adventures/a3a046a04836">version 0.2.0がリリースされた</a>。Koaは人気のあるMVCプラットフォーム、<a href="http://expressjs.com/">Express</a>の後継だが、新しいES6で導入された機能を多用している。プロジェクトリードの<a href="https://twitter.com/tjholowaychuk">TJ Holowaychuck</a>氏はKoaについて「私がConnect/Expressから学んだことを取り込んで、今度こそ「正しい」ことをするチャンス」だと語っている。</p> 
  <p>このリリースは &quot;short but sweet&quot; と呼ばれており、最初の0.1.0リリースからの設計選択を再確認し、今後のリリースとプロダクション利用のためにKoaのAPIを固める上で重要なリリースだ。</p> 
  <h2>0.2.0での変更</h2> 
  <p>このリリースで最大のアップデートは、実際のところ<a href="https://github.com/koajs/compose">koa-compose</a>モジュールに対するものだ。ミドルウェアがリクエストを操作する前後で、その内容を標準出力（stdout）にログ出力することにより、開発者はミドルウェアを流れるリクエストをデバッグすることができる。</p> 
  <p>より小さな変更点としては、ソケットをNodeレベルで処理したあとNodeサーバがクラッシュしないようソケットエラーをルーティングすること、<a href="http://expressjs.com/">Express</a>とKoaで共通の機能を両方のフレームワークが使えるようリファクタリングしてモジュール化したことが含まれる。ひとつの例は “accepts” モジュールだ。これは<a href="https://developer.mozilla.org/en-US/docs/HTTP/Content_negotiation">コンテンツネゴシエーション</a>をするもので、Accept HTTPヘッダの値に基づき、サーバがリクエストに対して異なるタイプのコンテンツで応答できるようにする。</p> 
  <h2>ジェネレータによる構築</h2> 
  <p>Koaは自身を「次世代Webフレームワーク」と呼んでおり、<a href="https://github.com/visionmedia/co">co</a>ライブラリを利用している。このライブラリは<a href="http://wiki.ecmascript.org/doku.php?id=harmony:specification_drafts">ECMAScript 6</a>言語仕様（&quot;Harmony&quot;として知られている）にあるジェネレータを使って、Nodeのノンブロッキング同期処理を生成する。HTTPリクエストで必要になる同様の「スタック処理」をするのに、これまでのNodeフレームワークはコールバックとPromiseを頼りにしていた。</p> 
  <p>ジェネレータは実際にはHarmonyイテレータを生成する「ファクトリ」だが、Koaはそれらを使って関数を同期オペレーションに変換する。Koa appはリクエストを複数のミドルウェアレイヤを通して渡すことができる。呼び出されるミドルウェア関数は、呼び出し元の処理を継続させるために、結果をyieldしなくてはならない。</p> 
  <pre>
var koa = require('koa');
var app = koa();

app.use(route.get('/', google));

function *people() {
 &nbsp;&nbsp;// “get” は非同期HTTP呼び出し
 &nbsp;&nbsp;var result = yield get('http://www.google.com');
 &nbsp;&nbsp;// この行は上のyieldが戻るまで実行されない
 &nbsp;&nbsp;this.body = result;

}</pre> 
  <h2>No Middleware</h2> 
  <p>Koaにはミドルウェアが含まれていない。これによってフットプリントを小さく維持できる。Holowaychuk氏はこう説明する。「もともとは、たくさんのミドルウェアを<a href="https://github.com/senchalabs/Connect">Connect</a>にバンドルしていました。エンドユーザのためだけでなく、自分たちのためでもありました。Nodeとそのエコシステム全体は急速に変化していたので、その方がメンテナンスしやすかったのです。それからはや数年、多くの人がミドルウェアをバンドルしたのは間違いだったと合意しています。」Holowaychuk氏はさらに続けて、このことが、Koaにはミドルウェアをバンドルしないが、便利にバンドルできる別のモジュールを提供することにつながったと言った。</p> 
  <p><a href="https://github.com/koajs/common">koa-common</a>モジュールは、Webアプリケーションに必要なミドルウェアの多くをバンドルしている。開発者は自分のKoaアプリケーションに、<a href="https://npmjs.org/">NPM</a>経由でこのミドルウェアすべてを追加することができる。</p> 
  <pre>
$ npm install koa-common</pre> 
  <h2>KoaとExpressの将来</h2> 
  <p>Holowaychuk氏によると、Koaは時折ある奇妙なフィーチャーリクエストがなければ完成状態にあると考えている。</p> 
  <p>“deif”というユーザは、Koaがリリースされたことで、Expressの将来について<a href="https://news.ycombinator.com/item?id=6933833">懸念を抱いている</a>。</p> 
  <blockquote> 
   <p>これについて、いくつか質問があります。</p> 
   <ol> 
    <li>FAQにはExpressのステータスについて政治的回答がなされていますが、私はもう、Expressはアクティブにメンテナンスされないと思っています。合っていますか？</li> 
    <li>Koaにフォーカスするなら、どうしてNodeフレームワークでビッグネームになっているExpressから名前を変えるのですか？</li> 
    <li>新しい開発者がExpressとKoaを見たとき、どちらにフォーカスしているかすぐにわかりますか？</li> 
   </ol> 
   <p>要するに、なぜExpress 3.0 (あるいは4.0)と呼ばなかったのか不思議に思っているのです。</p> 
  </blockquote> 
  <p>Holowaychuk氏は名前の変更についてこう説明した。</p> 
  <blockquote> 
   <p>ExpressからKoaへの移行は簡単ではありません。同じように見えるかもしれませんが、根本的にかなり違っています。そのため、私はそれをExpress 4.0と呼ぶのではなく、新しい名前を与えた方がよいと思いました。… 引き続きExpressをメンテナンスしている人たちもいますし、もし興味があるならチームに参加することも可能です。</p> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
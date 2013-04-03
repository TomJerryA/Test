<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Backbone.js 1.0リリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/backbone.js-1.0;jsessionid=A57DED25FAE2768A25D94DFE8F934A66"><em>原文(投稿日：2013/03/26)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>2年半の開発を経て、<a target="_blank" href="http://ashkenas.com/backbonejs-1.0/">Backbone.jsのバージョン1.0がリリースされた</a>。<a target="_blank" href="http://backbonejs.org/">Backbone.js</a>は人気のあるModel/ViewのJavaScriptライブラリで、<a target="_blank" href="http://www.usatoday.com">USA Today</a>、<a target="_blank" href="http://www.rdio.com/new">Rdio</a>、<a target="_blank" href="https://www.airbnb.com/wishlists/popular">Airbnb</a>を含む多くのWebアプリケーションで用いられている。</p> 
 <p>Backbone.jsはユーザーに3つのコアビルディングブロックを提供している。</p> 
 <ol> 
  <li><em>Model</em>は永続化可能なオブジェクトを表すために用いられる。Backbone.jsの同期機能を用いると、modelは自動的にリモートのデータソース（デフォルトではRESTfulなWebサービス）と同期する。同様に、modelのコレクションを管理したり、データソースと同期したりするための機能も提供されている。</li> 
  <li><em>View</em>はWebアプリケーションのUIを構築、維持するために用いられる。Viewはmodelが公開しているchangeイベントを待ち受けるようにする事ができ、modelを用いてUIを最新の状態に保つことが簡単にでき、またその逆を行うことも簡単にできる。</li> 
  <li><em>Router</em>はBackbone.jsアプリケーション内でのナビゲーションを提供する。典型的なBackbone.jsアプリケーションは単一ページのインターフェースであるが、一般的にはブックマーク可能なURLを持つことが望まれており、画面遷移にブラウザの戻るボタンを用いることも望まれている。Backone.jsの<em>router</em>はHTML5の新しい履歴APIを用いてこの機能を提供しており、その履歴APIがサポートされていない場合はURLハッシュにフォールバックする。</li> 
 </ol> 
 <p>&nbsp;</p> 
 <p>Backbone.js 1.0は0.9系に比べていくつかの変更が加えられている。変更にはコレクションのより効率的なバルク更新の方法、エンコードされたURLセグメントの自動デコード、イベントエミッタに対する新しい<tt>listenTo、stopListening</tt>メソッドが含まれる。デフォルトでは、modelのバリデーションはmodelが保存されるまで延期される。逆に、以前のリリースではバリデーションはプロパティを設定すると即座に実行されていた。これらの変更はいずれも基盤を破壊するようなものではないので、0.9からのアップグレードはほとんど問題はないとされている。</p> 
 <p>ここまでは長い道のりであったが、1.0はBackbone.jsの歩む道の最終地点ではない。 <a target="_blank" href="http://ashkenas.com/backbonejs-1.0/">アナウンスは新しいアイデアに対する明確な要求で締めくくられている。</a></p> 
 <blockquote>
  Backboneの中心にある欠くことのできない前提は、JavaScriptを用いてWebアプリケーションを構築する際に便利な最小限のデータ構造（Modelとコレクション）やユーザーインターフェース（ViewやURL）プリミティブを追求していこうという事です。我々はそう言った類の機能を探し続けていますし、もしあなたがそれを見つけたならば、ぜひ我々に教えて下さい。全体的で、あなたにとって全てを決めてくれるフレームワークが一般的で、サイトのlook &amp; feelやデフォルトの挙動を変更するために多くのライブラリを必要としているようなの現在のエコシステムにおいて、BackboneはWebアプリケーションのすべてのエクスペリエンスをデザインできる自由をあなたに与えるツールで居続けるべきなのです。
 </blockquote> 
 <p>&nbsp;</p> 
 <p>Backbone.js 1.0は単一のJavaScriptソースファイルとして<a target="_blank" href="http://backbonejs.org">ダウンロードする事ができる。</a>最小化され、gzip圧縮されたバージョンは6.3KBである。Backbone.jsはViewやRouterのようなDOMに依存する機能を利用する際、<a target="_blank" href="http://jquery.com">jQuery</a>や<a target="_blank" href="http://zeptojs.com">Zepto</a>同様に依存関係として<a target="_blank" href="http://underscorejs.org">underscore.js</a>を利用している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
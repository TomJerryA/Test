<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>レンダリングシステムを刷新したMeteor 0.8</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/04/meteor-08-blaze"><em>原文(投稿日：2014/04/08)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://www.meteor.com">Meteor</a>のバージョン0.8が公開された。“Meteorのレンダリングシステムが改善されている”という。</p> 
  <p>Meteorの次世代テンプレートエンジンであるBlazeは細かなDOMの更新が可能であり、jQueryと統合され、APIが単純になった。今回のリリースで2012年の<a href="https://www.meteor.com/blog/2012/08/31/introducing-spark-a-new-live-page-update-engine">バージョン0.4</a>導入されたページ更新エンジンであるSparkがBlazeに置き換わった。</p> 
  <p><a href="https://www.meteor.com/blog/2014/03/27/meteor-080-introducing-blaze">Meteorのブログ</a>でMatt Debergalis氏がBlazeについて“開発者フレンドリ”であり、設計上でもSparkより“いくつかの点”で優れている、と評している。</p> 
  <p>Blazeはふたつの部分でできている。ひとつは、テンプレートをJavaScriptのコードに変換するビルドタイムコンパイラだ。HandlebarsスタイルのコンパイラであるSpacebarsはHTMLのテンプレートを即時に更新されるDOMの要素に変換する。したがって、ユーザは普通のHTMLのテンプレートとヘルパを書けばいい。</p> 
  <blockquote> 
   <p>“ユーザがデータを変更したり、テンプレートが依存する新しいデータがネットワークから来たりしたとき、Blazeが自動的に画面を更新します”。“依存関係を宣言したり、更新を制御するコードを書いたりする必要”はない、とDebergalis氏は<a href="https://www.meteor.com/blog/2014/03/27/meteor-080-introducing-blaze">ブログに書いている</a>。</p> 
  </blockquote> 
  <p>Blazeのふたつ目の部分は“要素を描画したり、依存関係を追跡したり、変化に従って依存関係の更新を行う”ランタイムAPIだ。</p> 
  <p>SparkのAPIの<a href="https://github.com/meteor/meteor/wiki/Using-Blaze#replacements-for-advanced-spark-apis">置き換え</a>に伴い、Meteor.renderがなくなり、新しいパターンをカスタムブロックヘルパを定義するための新しいパターンが導入された。<a href="https://github.com/meteor/meteor/wiki/Using-Blaze#added-and-deprecated-apis">追加されたAPIと利用非推奨になったAPI</a>にはUI.bodyが含まれている。UI.bodyはBODY要素全体と対応するテンプレートだ。</p> 
  <p><a href="https://github.com/meteor/meteor/blob/devel/packages/spacebars/README.md">Spacebars</a>パーサーを使えば“以前はできなかった”処理ができる。例えば、</p> 
  <ul> 
   <li>HTMLのリアクティブな更新。テンプレートパーサはHTMLタグをパースし、細かい単位でリアクティブな更新ができる。DOMの要素を属性のレベルで更新できる。</li> 
   <li>プリコンパイル。Spacebarsコンパイラはシンプルな手続きがたのコードを生成する。生成されたコードは内部のMeteorインターフェースを呼び出す。このインターフェースは将来は、クライアントサイドのレンダリングでもサーバサイドのレンダリングでも利用される。テンプレートを解釈したりHTMLのアウトプットをパースするよりも効率的だ。</li> 
   <li>構文拡張。Handlebarsのシンタックスは極端に小さい。これは、厳選された拡張が追加されるのを見越しているからだ(現時点ではMeteorにない、現時点のHandlebarsの重要な機能を実装している。例えばオブジェクトをサポートし現在のインデックスやキーにアクセスできる#each。)</li> 
  </ul> 
  <p>Meteor 0.8ではHandlebars名前空間が非推奨になった。Handlebars.SafeStringはSpacebars.SafeStringに、Handlebars.registerHelperはUI.registerHelperになった。</p> 
  <p>Spacebarsを使うにはHTMLは“きちんと整形”されていなければならない。githubの<a href="https://github.com/meteor/meteor/wiki/Using-Blaze">Using Blaze</a>というページには、“SparkではHTMLのパースはHTMLの書き方に寛容なブラウザが行っていました。”と書いてある。</p> 
  <p>加えて、BlazeのHTMLパーサーは現時点ではHTMLの仕様を完全に満たしていない。リリースノートには&lt;p&gt;や&lt;li&gt;のような<a href="https://github.com/meteor/meteor/issues/1842">特定のタグ</a>は自動的に閉じない、と書いてある。</p> 
  <p>0.8のリリースはMeteorのコミュニティに大いに歓迎された。LinkedInのMeteor<a href="http://www.linkedin.com/groups?home=&amp;gid=4556383&amp;trk=anet_ug_hm&amp;goback=%2Egmr_4556383">グループ</a>では、ユーザであるUﾄ殷r Toprakdeviren氏が<a href="http://www.linkedin.com/groups/What-is-your-opinion-about-4556383.S.5855220594395619330?trk=groups_most_recent-0-b-ttl&amp;goback=%2Egmr_4556383">ディスカッション</a>を始めている。お題は“Meteor 0.8.0(Blaze、Spacebarsなど)についてどう思うか”</p> 
  <p>Ongo WorksのファウンダでありCTOであるAaron Singmaster-Judd氏は“素晴らしく良くできていて、Meteorのチームや新しいコードベースを活用したコミュニティの開発者たちはほんとうによくやったと思います“と答えている。</p> 
  <blockquote> 
   <p>“既存のパッケージを更新するのは大変かもしれません。ウェブ上の情報もかなりは無効になってしまいます。しかし、更新する価値はあります。”</p> 
  </blockquote> 
  <p>Hacker Newsでも今回のバージョンアップは好意的に受け止められている。elsherbini氏はjQuery統合について“とても素晴らしい!”と<a href="https://news.ycombinator.com/item?id=7484804">コメント</a>している。ほかのユーザもBlazeのリリースについて好意的に反応している。TylerE氏はコンパイラについて“とても興奮しています。jadeテンプレートを使うのも工夫は必要なさそうですね。これは少なくとも私にとっては大きなことです。”と<a href="https://news.ycombinator.com/item?id=7485394">コメント</a>している。</p> 
  <p>Debergalis氏によれば、テンプレートエンジンだけが0.8の新しい機能であり、Meteor 1.0リリースに向けての大きな1歩だ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
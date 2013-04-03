<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>JavaScriptでGitを実装するKickstarterプロジェクト、28時間で資金調達</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/git-in-javascript;jsessionid=806EFD9E289230875F28ABB47126B480"><em>原文(投稿日：2013/03/26)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>JavaScriptおよび<a target="_blank" href="http://nodejs.org">Node.js</a>コミュニティで有名な<a target="_blank" href="http://creationix.com/">Tim Caswell</a>氏が、JavaScriptで<a target="_blank" href="http://git-scm.com/">Git</a>を再実装しようと思いつき、Kickstarterで360名を超える出資者により<a target="_blank" href="http://www.kickstarter.com/projects/creationix/js-git">28時間で資金調達した</a>。このプロジェクトは、<a target="_blank" href="http://www.codinghorror.com/blog/2007/07/the-principle-of-least-power.html">Atwoodの法則</a>「JavaScriptで書けるものは、いずれJavaScriptで書かれる」の一例だ。</p> 
 <p>このプロジェクトについてもっと知るため、Tim氏に話を聞いた。</p> 
 <p><b>JSGitのアイデアはどこから生まれたのですか？</b></p> 
 <blockquote> 
  <p>私はいつも、自分が持っているデバイスをプログラムする新しい方法を探しています。最近、Microsoftのよい人から<a target="_blank" href="http://www.microsoft.com/Surface/en-US/surface-with-windows-rt/windows-rt">Surface RT</a>が送られてきました。前のプロジェクトで使った<a target="_blank" href="http://www.apple.com/ipad/">iPad</a>も2台ありますし、<a target="_blank" href="http://www.google.com/intl/en/chrome/devices/chromebook-pixel/">ChromeBook Pixel</a>を買ったところでした。いずれも興味深いデバイスなのですが、かなり不満がありました。鍵のかけられた環境で、そのデバイス上で開発するのには不向きなんです。だれも、あのAppleですら、鍵をかけていないプラットフォーム、それがブラウザのJavaScript環境です。あなたはコードを書いてブラウザで動かせます。ローカルストレージにもアクセスできますし、インターネットにデータをアップロード、ダウンロードすることもできます。</p> 
  <p>1年ほど<a target="_blank" href="http://c9.io">Cloud9</a>で仕事をして、ブラウザベースのIDEは実現可能だとわかりました。Cloud9がうまく解決していなかった唯一の問題、それがオフライン作業でした。自分のGitリポジトリを自分のデバイスにローカルにクローンし、海外へのフライト中（あるいは裏庭の向こうをぶらぶらしながら）オフライン作業し、その後インターネットにつながる環境に戻ったら、変更を自分のパブリックなGitリポジトリにプッシュする、そういうのがやりたかったんです。</p> 
  <p>JavaScriptはどこでも使えるプラットフォームです。そこでGitをポーティングしようと決めたんです。</p> 
 </blockquote> 
 <p><b>JSGitのユースケースをどう考えていますか？ 単なるブラウザベースのIDEやエディタですか、それとも、もっといろんな応用があるんですか？</b></p> 
 <blockquote>
  私の一番のユースケースはブラウザベースのプログラミング環境ですが、別の使い道に関心を持っている人がたくさんいます。たとえば、Node.jsのための完全にJavaScriptで書かれたGitクライアントとサーバなどです。Gitはいろんなデプロイメントシステムの共通コンポーネントなので、Git for Node.jsできめ細かくコントロールできれば、多くの人にとって非常に役立つでしょう。
 </blockquote> 
 <p><b>パフォーマンスはどう考えていますか？</b></p> 
 <blockquote>
  JavaScript自体はかなり高速です。最近、JavaScriptで非常に高速なハッシュ関数（MD5、SHA1、SHA256）を書いたんですが、私のデスクトップのブラウザで、1秒間に500,000 MD5ハッシュまで可能でした。大きなGitリポジトリの場合、高速なノートパソコン上でネイティブクライアントを使ったとしても、クローンには時間がかかるので、それがうまくやれるとは思っていません。でも、小さなリポジトリでは、かなり高速になると思っています。
 </blockquote> 
 <p><b>JavaScriptでスクラッチから全部再実装するのではなく、<a target="_blank" href="https://github.com/kripken/emscripten">Emscripten</a>のようなもので、既存のGitのC実装をクロスコンパイルするというアプローチを取らないのはなぜですか？ </b></p> 
 <blockquote>
  これも調べるつもりですが、初期調査の結果、2つのことが問題になると予想しています。1つ目は、Emscriptenはコードジェネレータだということです。これはかなり巨大なコードを生成します。コードの大部分を手動で微調整しない限り、結局は直接の移植になります。2つ目は、GitのCによる実装を見てみると、下位のファイルシステムやネットワーク呼び出しとの密結合がかなりあります。Gitのブラウザベースバージョンには、かなりのカスタマイズが必要になるでしょう。各種Webプラットフォームには独自のファイルストレージAPIがあるため、それぞれについてファイルシステム抽象化レイヤを書かなくてはなりません。
 </blockquote> 
 <p><b>Gitには、C、Javaなどの言語による実装がありますが、JavaScriptで実装するときの課題は具体的に何だと思いますか？</b></p> 
 <blockquote>
  JavaScriptでcrypto関係を実装した経験がかなりあるため、それは問題になるとは思っていません。でも、実装しなくてはならないコード量は問題でしょうね。まずは必要最小限なところに取り組んで、そこから時間を使い果たすまで成長させていくつもりです。
 </blockquote> 
 <p><b>なぜ今、このプロジェクトをやるんですか？ これを可能にする特別なHTML5技術があるのでしょうか？</b></p> 
 <blockquote>
  どちらかと言うとハードウェアですね。長時間のバッテリーとすばらしい画面を持つデバイスがどんどん増えていますが、開発環境としてはひどいものです。
 </blockquote> 
 <p><b>プロジェクトは1日ちょっとで資金調達できましたが、それでどんな機能が作れると思っていますか？</b></p> 
 <blockquote>
  <a target="_blank" href="http://www.kickstarter.com/projects/creationix/js-git/posts">Stretch Goals</a>で見積もったように、Gitの基本機能が作れると思っています。時間があれば、さまざまなプラットフォームとのインテグレーションもやりたいです。
 </blockquote> 
 <p><b>どうしてKickstarterを使ったんですか？</b></p> 
 <blockquote>
  よさそうに聞こえたんですよ。これまでやってきて、そしてKickstarterのルールを全部読んでみて、プロジェクトの理想には辛うじて合うかなと感じています。
 </blockquote> 
 <p><b>Kickstarterで資金調達しようとする（JavaScript）オープンソースプロジェクトは増えると思いますか？</b></p> 
 <blockquote>
  まだわかりませんね。これは1つの実験です。アイデアに何ヶ月も時間を費やす前に、アイデアをスクリーニングするという考え方は気に入っています。私は、結局はコミュニティの関心がほとんどないとわかるプロジェクトに、自分の自由時間を何百時間も費やして来ました。みんなが期待するクールなプロジェクトにフルタイムで取り組むという考え方は実に気に入っています。Kickstarterが長期的にうまくいくかはわかりませんが、もしうまくいかなくても、他の考え方を探し続けます。
 </blockquote> 
 <p>JSGitは、Kickstarterで資金調達に成功した最初のJavaScript関連プロジェクトではない。過去には<a target="_blank" href="http://www.kickstarter.com/projects/869786663/async-savascript-book?ref=live">非同期JavaScriptプログラミングに関する書籍</a>と<a target="_blank" href="http://www.kickstarter.com/projects/188988365/lets-code-test-driven-javascript?ref=live">テスト駆動JavaScriptのスクリーンキャスト</a>のプロジェクトがあった。だが、JSGitはJavaScriptライブラリを作る最初のKickstarterプロジェクトだ。</p> 
 <p><a target="_blank" href="http://www.kickstarter.com/projects/creationix/js-git">このプロジェクト</a>の支援募集は2013年3月30日までだ。期日が過ぎたら、Tim氏はすぐにプロジェクトに取り組む予定だ。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
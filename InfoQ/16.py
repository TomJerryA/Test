<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>JavascriptプラットフォームのFamo.usが初の公式アクセス版をローンチ</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/famous_launches_first_access"><em>原文(投稿日：2013/12/04)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://Famo.us">Famo.us Javascript platform</a>を開発したチームは2013年12月5日，同プラットフォームの能力をクライアント側に展開するための準備段階として，アプリケーションレイヤのコードを初めてプレビューリリースする予定である。JavaScriptのみで記述されているFamo.usは，現在まだアルファ版プレビューにも関わらず，70,000人を越える開発者の注目を集めている。プラグインを必要とせず，ブラウザ上でネイティブアプリのパフォーマンスを実現できる点がその魅力だ。</p> 
  <p>Famo.usは，ブラウザ本来のレンダリング機能との関連性を完全に断ち切っている。&quot;ユーザがおそらく見たいとも思わない，高度な数学や物理学を駆使して&quot;，ブラウザのレンダリングエンジンを完全に置き換えるように設計されているのだ。&quot;きっと目が回ってしまいますよ&quot; と語るのは，プロジェクトの創設者である<a href="https://twitter.com/stevenewcomb">Steve Newcomb</a>氏だ。ブラウザのレンダリングという壁を乗り越えるには，このような低レベルの工夫も必要なのだ。しかし開発者の98%が注目しているのはそこではないはずだ，とも氏は言う。&quot;この数年間は，jQueryを完全に置き換え可能なシンタックスシュガーの開発に費やしてきました。&quot; その結果として，Newcomb氏と同社は，現代的なブラウザのすべて -- Safari, Chrome, Firefox, IE10 -- で動作を保証するに至っている。</p> 
  <p>Famo.usチームが求めたのは，まさにこの普遍的な対応性，すなわち，デザイナからベテランのJavascript技術者まで，すべてのエクスペリエンスのレベルを満たす，jQueryの完全なリプレースなのだ。500万件を数える資金援助によって支えられて，完全無償のオープンソースプロダクトであるFamo.usには，４つの異なる操作レベルがある。&quot;一番簡単なレベルがデザイナです&quot; とNewcomb氏は言う。 &quot;デザイナでは，まったくコードを書く必要がありません。ウィジェットやテンプレートすべてにスライダが埋め込まれていますから，ユーザはただ，それを操作すればよいのです。スライダを変化させることで得られるバリエーションは無限大です。&quot; そのデザイナレイヤの下にはすべてのシンタックスシュガーがあり，ＵＩを構成するウィジェットとテンプレート，およびそれらを格納して拡張を続けるライブラリと結び付いている -- 開発されるアプリケーションの大多数はこのレイヤで，テンプレートとウィジェットを組み合わせて構成されるものになる，とFamo.usチームは考えている。３つめはウィジェットとテンプレートの下にある，プラットフォーム開発者がオリジナルなユーザエクスペリエンスを追求する部分だ。例えばプロプライエタリなUIを，初期のFamo.usに投資していたSamsungあたりが追求するかも知れない，とNewcomb氏は述べている。最後にFamo.usの内部深くにある数学的，物理学的エンジンは，Newcomb氏によれば，真のギークのためのものだ。</p> 
  <p>その構造の中には，Famo.usチームのある願望が潜んでいる -- 彼らはアプリケーション開発の新たなアプローチを提案している。jQueryベースのDOM解析処理から，コード開発者がアプリケーションの外観を操作して，彼らの提供する物理エンジンを活用するようなプラットフォームへの移行だ。HTML，webGL，キャンバスのレンダリングはFamo.usが行う。チームは12月5日を起点として，ウィジェットやテンプレート，アプリケーションのライブラリ拡張を週単位でロールアウトしていく計画だ。</p> 
  <p>Famo.usは <a href="http://meteor.com">Meteor</a>, <a href="http://firebase.com">Firebase</a>, <a href="leapmotion.com">LeapMotion</a>, <a href="http://http://backbonejs.org/">backbone js ライブラリ</a> との公式なパートナシップを発表した。コードは現在プライベートアルファ版で，2014年2月下旬に公式ベータ版のリリースが予定されている。リリース後は，プラットフォーム全体が<a href="http://www.mozilla.org/MPL/2.0/">Mozilla Public License MPL v2</a>の下で公開される予定だ。すべてのコードには自由にアクセス可能になるが，企業によるプロプライエタリなウィジェットやテンプレートの開発も認められる。ローンチを指揮するのは，Famo.usの開発担当副社長であり，<a href="https://developers.facebook.com/">Facebook Developer Platform</a>の創設や<a href="https://www.facebook.com/f8">F8カンファレンス</a>のローンチも行っているDave Fetterman氏である。</p> 
  <blockquote>
    &quot;本当の意味で堅牢なJavascript開発プラットフォームというのは，長く存在しませんでした。単なるウィジェットやプラグイン，ソリューションの一部に過ぎないようなプラットフォームは必要ではありません。人々がキャリアを賭けるに値するようなプラットフォームが必要なのです。そのようなものを，これまで長く求めてきました。&quot; とNewcomb氏は語る。
  </blockquote> 
  <p>それに向けてFamo,usチームは，３つのウィジェットと１つのアプリケーションを12月5日にリリースする。リリースでは<a href="http://codepen.io/">Codepen</a>をパートナに活用して，新しいウィジェットそれぞれ用の対話型エクスペリエンスが用意される予定だ。</p> 
  <h3><a href="http://bit.ly/1eJsK6a">Twitterアプリ</a></h3> 
  <p class="codepen" data-default-tab="result" data-user="befamous" data-slug-hash="ac53af08967073df60ceaf28c0c76007" data-theme-id="2352" data-height="350">&nbsp;</p> 
  <script async="" src="//www.codepen.io/assets/embed/ei.js"></script> 
  <p>&nbsp;</p> 
  <p>&nbsp;</p> 
  <h3><a href="http://bit.ly/18ivwv8">jQuery風のライトボックス・ウィジェット</a></h3> 
  <a href="http://bit.ly/18ivwv8"> <p class="codepen" data-default-tab="result" data-user="befamous" data-slug-hash="442915109539f48b92700c137c3fafe9" data-theme-id="2352" data-height="350">&nbsp;</p> <script async="" src="//www.codepen.io/assets/embed/ei.js"></script> <p>&nbsp;</p> <p>&nbsp;</p> </a> 
  <h3><a href="http://bit.ly/IHupPC">ボタンウィジェット</a></h3> 
  <p class="codepen" data-default-tab="result" data-user="befamous" data-slug-hash="c3147502f9f7f897a8197ed4b6dbcb5f" data-theme-id="2352" data-height="350">&nbsp;</p> 
  <script async="" src="//www.codepen.io/assets/embed/ei.js"></script> 
  <p>&nbsp;</p> 
  <p>&nbsp;</p> 
  <h3><a href="http://bit.ly/1bef9j9">1対多ウィジェット</a></h3> 
  <p class="codepen" data-default-tab="result" data-user="befamous" data-slug-hash="373819beb72b28945fa06e4346e20b54" data-theme-id="2352" data-height="350">&nbsp;</p> 
  <script async="" src="//www.codepen.io/assets/embed/ei.js"></script>
 </div> 
</div><br><br><br><br><br><br></body></html>
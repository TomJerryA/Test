<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ウェブスタイルは上手くいったか</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/web-style;jsessionid=856612D388D1A8108AB45FED13409457"><em>原文(投稿日：2013/03/24)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Jean-Jacques Dubray氏(JJ)が<a target="_blank" href="http://www.ebpml.org/blog2/index.php/2013/03/20/the-end-of-the-web">最近のブログ</a>で<a target="_blank" href="http://www.tbray.org/ongoing/When/200x/2006/04/17/SOA-or-not">Tim Bray氏がSOAの終焉を予言</a>してからほぼ7年経ったことに言及している。</p> 
 <blockquote>
  私はインタビューを受け、ポッドキャストで話しました。 [...] 両方とも私にはある疑問が浮かびました。“SOAについてどうするべきだと思うか”。不気味なことにこの問いを私に投げかけた人はいませんでした。そして私は答えを見つけました。“何もするな。‘SOA’はかつては何らかの意味を持っていたが、今は只のベンダの戯言だ。”
 </blockquote> 
 <p>TimTim Bray氏はSOAよりも<a target="_blank" href="http://www.tbray.org/ongoing/When/200x/2006/03/26/On-REST">ウェブスタイル</a>に未来がある、と宣言(予言)している。JJが説明するようにこの予言はその後、多く言及された。<a target="_blank" href="http://www.infoq.com/news/2009/01/is-soa-dead;jsessionid=3C3882C9D9DD4567D18E339670C63407;jsessionid=856612D388D1A8108AB45FED13409457">Anne-Thomas Manes氏など</a>の言及だ。結論のひとつはSOAプロジェクトの多くは衰退し、中止になった。JJは自身の経験を語っている。</p> 
 <blockquote>
  当時のマネージャが私にTim Brayの記事がIT部門で話題になっており、彼は自身のマネジメントでTimの宣言に対してどのように回答をしたらいいか解らないと言いました。そのとき、彼のチームは独自のESBを構築していました当時はまだXMLはほとんど知られていませんでした。絶えず上昇するトランザクション量(2007年初頭で1日10メガのリクエスト)がTim Brayの文章で危うくなったのです。
 </blockquote> 
 <p>JJは<a target="_blank" href="http://www.infoq.com/articles/rest-soap;jsessionid=3C3882C9D9DD4567D18E339670C63407;jsessionid=856612D388D1A8108AB45FED13409457">数年</a>に渡ってInfoQや他の媒体で<a target="_blank" href="http://www.infoq.com/news/2011/06/trouble-with-apis;jsessionid=3C3882C9D9DD4567D18E339670C63407;jsessionid=856612D388D1A8108AB45FED13409457">Webが見落としている</a><a target="_blank" href="http://www.infoq.com/news/2011/06/RestAPIs;jsessionid=3C3882C9D9DD4567D18E339670C63407;jsessionid=856612D388D1A8108AB45FED13409457">問題について</a><a target="_blank" href="http://www.infoq.com/articles/RESTSOAFuture/;jsessionid=3C3882C9D9DD4567D18E339670C63407;jsessionid=856612D388D1A8108AB45FED13409457">少なくない時間</a>を費やしている。最近では、ウェブスタイルを実装していると称する多くのサービスを見ている。</p> 
 <blockquote>
  9000のAPI[Programmable Webのディレクトリにある]の内、私の見積もりではTim Brayの
  <a target="_blank" href="http://en.wikipedia.org/wiki/Representational_state_transfer">ウェブスタイル</a>に従っているのは1%に満たないです。ほとんどのAPIはウェブスタイルではなく&quot;API&quot;スタイル、つまり、RPCのようなスタイルです。
 </blockquote> 
 <p>JJは自身が代表的なサンプルと考えるAPIをいくつか例示し、自身の考えを説明している。</p> 
 <blockquote> 
  <ul> 
   <li><span style="line-height: 19px; font-size: 13px"><strong>Ask Ziggy</strong> </span><a style="line-height: 19px; font-size: 13px" target="_blank" href="http://www.ask-ziggy.com/walkthrough.html#sample">&quot;アクション&quot;</a><span style="line-height: 19px; font-size: 13px"> (Play、NextSong、Previous Song、Shuffle...というような)を定義する機能を提供する</span></li> 
   <li><span style="line-height: 19px; font-size: 13px"><strong>WhatLanguage</strong> 同じURIにGET(リクエストの文字数が7500文字以下の場合)やPOSTをすることで与えられた文字列の言語を検出する<a target="_blank" href="http://www.whatlanguage.net/en/api/language_identification_documentation#detect_text">ことができる</a></span></li> 
   <li><span style="line-height: 19px; font-size: 13px"><strong>Do.com</strong> <a target="_blank" href="https://developers.do.com/docs/tasks">ウェブスタイルのAPI</a>を提供しているように見えるが、不十分。5種類のリソース(タスク、プロジェクト、ユーザ...)に対する単純なCRUD操作を提供する</span></li> 
   <li><span style="line-height: 19px; font-size: 13px"><strong>SkyBuffer</strong>も<a target="_blank" href="https://dev.skybuffer.com/version/1">ウェブスタイル</a>に従っているが、DO.comと同じようにエンティティに対するCRUDを提供する</span></li> 
   <li><span style="line-height: 19px; font-size: 13px"><strong>MaShape</strong>は&quot;Cloud APIハブ&quot;であり、APIの開発者にそのAPIの利用者のためのより良い方法を提供する。では<a target="_blank" href="https://www.mashape.com/docs/gettingstarted/overview">どのように実現しているのか</a>。&quot;<span>Mashape上でAPIを記述することでクライアントライブラリとドキュメントを自動生成する方法&quot;を提供する。数年のバッシングの後、開発者の間でクライアントコードの自動生成についての議論が始まったのだ。</span></span></li> 
  </ul> 
 </blockquote> 
 <p>&nbsp;JJの考えでは、Timやその他の人が推奨する純粋なウェブスタイルはAPIアプローチと競合関係にある。</p> 
 <blockquote>
  ウェブスタイルは&quot;統一インターフェース&quot;、ブックマークウェブスタイルは&quot;統一インターフェース&quot;、ブックマーク、
  <a target="_blank" href="http://www.infoq.com/articles/hypermedia-api-tutorial-part-one;jsessionid=3C3882C9D9DD4567D18E339670C63407;jsessionid=856612D388D1A8108AB45FED13409457">HATEAOS</a>ではなかったのか。標準IANA型を忘れてはいないか。このような議論は最近聞かなくなりました。URL内に動詞を埋め込む方法や複雑なクエリをポストすることを恥ずかしく思う人はいなくなりました。最も重要なのは
  <a target="_blank" href="http://docs.mongodb.org/manual/reference/javascript/">MongoDBが示したことです</a>。つまり、CRUDを行うためには4つの動詞と貧弱なURL構文では足りないということです。開発者と設計者はやけになって&quot;ウェブスタイル&quot;の周りをふらふらして、
  <a target="_blank" href="http://www.infoq.com/presentations/OpenStack-Extensions;jsessionid=3C3882C9D9DD4567D18E339670C63407;jsessionid=856612D388D1A8108AB45FED13409457">JSONに名前空間を付ける</a>というようなこともしています。
 </blockquote> 
 <p>このようなウェブスタイルのようなサービスを概観し、JJは価値を提供するのに失敗し、&quot;死んだ&quot;と結論を下している。さらに、ウェブそのものがほとんど死にかけていると宣言する。</p> 
 <blockquote>
  [...] 
  <a target="_blank" href="http://www.itwriting.com/blog/7249-native-apps-vs-html-5-no-consensus-over-how-to-choose.html">HTML5を使って価値あるものを作り出す方法がわからない、ネイティブアプリと競争しなければならない開発者</a>とウェブのビジネスモデルの中心にある&quot;製品&quot;に反映された素晴らしいアイディアに最終的に肝を冷やすことになるエンドユーザの間でウェブは死にかけています。&quot;ウェブよ永遠なれ&quot;というメッセージを携え、
  <a target="_blank" href="http://www.ebpml.org/blog2/index.php/2010/11/21/soon-the-web-will-die">Tim Berner-Leeは6ヶ月ごとにやってきますが</a>、
  <a target="_blank" href="http://www.bbc.co.uk/news/world-asia-21855051">セキュリティの大混乱</a>の後では、 大英帝国勲章の持ち主でももはやウェブを救えないように思えます。
 </blockquote> 
 <p>幸い、JJの記事は、過去とごまかされてきた&quot;技術的負債&quot;を陰鬱に振り返るだけで終わっていない。現在我々がどこにいるのか、そして、モバイルの新しい波についても言及している。JJはモバイルをこれまで見られなかった最大のパラダイムシフトになる可能性があると考えている。</p> 
 <blockquote>
  ほとんどの人は覚えていないでしょうが、ソフトウエアエンジニアリングは古い、とても古い&quot;ファイル処理&quot;というパラダイムの上に成り立っています。UFSがその頂点に位置しているのでしょう。ディスクトップのメタファとPCの主な利用パターンは&quot;ファイル処理&quot;に結びつけられたままです。モバイルにはファイルは関係ありません。モバイル端末は私たちの活動を逐一支援してくれます。少なくも、未来のオペレーティングシステムはアクティビティ中心になります。
 </blockquote> 
 <p>しかし、成功するためにはウェブの技術を置き去りにしなければならない、とJJは考えている。</p> 
 <blockquote>
  最高のユーザエクスペリエンスが勝ちます。それに対抗しようとする人は負けるでしょう。ウェブが興隆したのは、一時は優れたユーザエクスペリエンスを提供したからです。&quot;ウェブ&quot;だからという理由で興隆したのではありません。
 </blockquote> 
 <p>最後にJJは問題解決方法に対してもっと実用本位になり、過去から学ばなければならない、と主張する。</p> 
 <blockquote>
  さらにCRUDを突き詰めようとしてもRESTでない方法を切り捨てることはできません。MongoDB APIのように非常に優れた設計のAPIでさえそうです。また、オブジェクト指向は分散されたコンポーネント間の通信を表現するには不適切なパラダイムであることをしっかり理解する必要があります。すべてをステートレスなシングルトンのメソッド呼び出しで具現化することを辞めなければなりません。クラスのアノテーションはSOAが始め、私たちが終わらせなければならないセマンティック革命の推進力としては貧弱過ぎるのです。
 </blockquote> 
 <p>JJが示したこれらの変化を考慮すると、一体最終的なゴールは何なのだろう。JJは堅牢な合成プログラミングモデルを想定しているようだ。このモデルではモデルとビューが分離されながらも適切なつながりを持ち、アクティビティ/アクション/ライフサイクルのパラダイムに従う。残念ながらこのモデルについてJJは詳しく説明していないが、おそらくその意図は今後の関連する記事で説明されるだろう。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
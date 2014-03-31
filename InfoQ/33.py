<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>マイクロサービスとSOA</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/microservices-soa"><em>原文(投稿日：2014/03/23)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>ここ数年，小規模なサービススイートで構成されたアーキテクチャを表現することばとして&quot;マイクロサービス&quot;という用語が拡がっている。<a href="http://www.infoq.com/presentations/Micro-Services">QCon San Francisco 2012</a>でもThoughworksのJames Lewis氏が，このテーマでプレゼンテーションを行った。氏はMartin Fowler氏と共同で，同じテーマの<a href="http://martinfowler.com/articles/microservices.html">記事</a>も書いている。これに対して，マイクロサービスは一部の人々が考えるような新しい概念ではない，所詮はSOAの焼き直しに過ぎないという意見を持って，最近この<a href="http://service-architecture.blogspot.co.uk/2014/03/microservices-is-soa-for-those-who-know.html?utm_source=feedburner&amp;utm_medium=feed&amp;utm_campaign=Feed:+ServiceArchitecture+%28Service+Architecture+-+SOA%29">議論に加わった</a>のがSteve Jones氏だ。その中で氏は，Lewis氏とFowler氏の記事の分析を順に追いながら，両氏のマイクロサービスの定義を<a href="https://www.oasis-open.org/committees/download.php/19679/soa-rm-cs.pdf">OASIS SOA RM(Reference Model, 参照モデル)</a>と比較する，という作業を行っている。</p> 
  <p><strong>サービスによるコンポーネント化</strong>: OASIS SOA RMによると，</p> 
  <blockquote>
   SOA (Service Oriented Architecture) とは，さまざまなドメインの所有管理のもとに分散された機能を整理，活用するためのパラダイムである。
  </blockquote> 
  <p>Jones氏は次のように指摘する。</p> 
  <blockquote>
   OASISの定義は「要するにサービスとは何なのか」をうまく説明しています。 
   <ul> 
    <li><i>第３者のために処理を実行する能力</i></li> 
    <li><i>第３者に提供する処理の仕様</i></li> 
    <li><i>第３者に対する処理実行の提供</i></li> 
   </ul> SOAにおけるサービスとは，要求と機能を引き合わせるためのメカニズムなのです。
  </blockquote> 
  <p>続いて氏は，この件に関するLewis, Fowler両氏の発言を取り上げる。</p> 
  <blockquote>
   サービスとは，明示的なコンポーネントインターフェースを通じて通信するプロセス外コンポーネントです。
  </blockquote> 
  <p><strong>ビジネス機能中心の構成</strong>: Fowler氏が間違った思い込みをしている，マイクロサービスは新しくはない，と氏が考えるのはこの点だ。OASIS SOA RMは機能(Capability)について，次のように定義している。</p> 
  <blockquote>
   <i>サービス提供者がサービス利用者に対して提供できる現実的効果</i>
  </blockquote> 
  <p>機能(処理を行う実体)とサービス(体系的な構造)とは区別されなければならない，と氏は指摘する。</p> 
  <blockquote>
   私たちの10年にわたるSOAの試行錯誤，そしてOSASIS SOA RMに関わるすべての人々の多くの経験，そこから分かったのが，
   <i>フレームワークの体系化</i>とその動作との区別です。これが非常に重要だという理由は，サービス = 機能という考えでサービス開発に着手した結果，山のようなサービスを抱えることになる人々があまりに多いからです (まあ，そういう意味で言うなら，これがマイクロサービスということなのかも知れませんが)。
  </blockquote> 
  <p>Folwer氏の書いたことは間違いではないものの，大事なことを忘れている，と氏は考えている。</p> 
  <blockquote>
   新しい，ですか？ このようなアプローチに関するモデル，管理，チーム編成といった話題なら，私だって
   <a href="http://www.infoq.com/minibooks/enterprise-soa">本</a>を書いています。SOAの背景にある主原則についてならば，大勢の実践者グループによる
   <a href="http://www.soa-manifesto.org/">SOA憲章</a>(2009)もあります(個人的にはRMの方がよいと思っていますが)。ここでポイントなのは問題が２つあることです。ひとつはサービスと機能の混同，もうひとつは管理階層の重要性に関する認識の欠如です。
  </blockquote> 
  <p><strong>プロジェクトではなくプロダクト</strong>: Fowler, Lewis両氏の記事は，SOA RMの領域外としてこの話題を扱っている。しかし氏は，ここにも何ら新しいものはない，と言う。</p> 
  <blockquote>
   <a href="https://www.google.com/search?q=SOA+service+lifecycle&amp;oq=SOA+service+lifecycle&amp;aqs=chrome..69i57j69i60l5.9222j0j7&amp;sourceid=chrome&amp;espv=210&amp;es_sm=91&amp;ie=UTF-8">Googleでちょっと検索してみれば</a>，この分野にどれほど多くのものがあるのかすぐ分かるはずです。よいプロダクトもあれば，そうでもないものもありますが，いずれにしても目新しいものではありません。私は&quot;プロジェクトではなくプログラム&quot;という表現を使うようにしています。アーキテクトがプログラムのライフサイクル全般に対して&quot;責任を取る&quot;ことが必要だ，といつも言っているのです。繰り返しますが，彼らの主張が間違いだ，というのではありません。新しくはない，と言いたいのです。それが有効な手段であることは前から分かっていますが，コストという重大な問題があるのです。
  </blockquote> 
  <p><strong>賢いエンドポイントと愚かなパイプ</strong>: 氏はこの原則に全面的に同意するものの，これも新しいとは考えていない。またその表現も，次のように少し異なるものになっている。</p> 
  <blockquote>
   OASIS SOA RMには&quot;実行コンテキスト&quot;という概念があります。これはサービスがコールされたり，機能が実行されたりする一場面を表すことばです。何らかの動作を伴うエンドポイントがスマートであることに疑いはありません。&quot;
   <i>メカニズム</i>&quot;と表現されるのもそのためです。これに対して&quot;パイプ&quot;の方は，ダムであるにせよ，そうでないにせよ(火星に行ったRoverの&quot;パイプ&quot;はそれなりにスマートなようですが)，その存在自体
   <i>大した価値はありません</i>。これはSOAの重要な発見です。SOA RMにもそれは明記されています。実行コンテキストは必要な内部配線がすべて完成している場所ですが，機能へのアクセスを提供するのはあくまでサービスですし，価値を提供するのは機能なのです。
  </blockquote> 
  <p><strong>分散型ガバナンス</strong>: ここもまた，氏がFowler氏とLewis氏に同意できる場所である。ただし ...</p> 
  <blockquote>
   ガバナンスという面でSOAがマイクロサービス以上の存在であるというのは，間違ってはいないと思います。OASIS SOA RMで語られているSOAは，このような原則をすべてのIT資産に適用可能にするものです。特定の実装スタイルで実装されたものに限るわけではなく，ビジネススクールの教えるアプローチという意味において，すべてのIT資産を対象とするのです。
  </blockquote> 
  <p><strong>マイクロサービスとSOA</strong>: Lewis, Fowler両氏の記事は当初，SOAについては(十分には，あるいはまったく)言及していなかったようだ。Jones氏とのここ最近のやりとりの結果として，補足的な話題として付け足されたものであることが記事から見て取れる。しかしJones氏は，それを単に不十分なだけではなく，話題として無関係だと考える。</p> 
  <blockquote>
   [...] SOAの真の定義ではありません。REST主義者(RESTafarians)が自分たちの方法のすばらしさを説明する時に愛用していた，古い&quot;ビッグ&quot;ESBやWS-*的なものを展開したに過ぎないのです。両氏の記事はマイクロサービス形式を&quot;はっきり&quot;説明した上で，&quot;SOAには意味が多すぎる&quot;という理由から，SOAに対するマイクロサービスの優位性を主張しています。私が根本的に同意できないのはこの部分です。実装アプローチとしてのマイクロサービスの優位性を言いたいのならば，マイクロサービス以外のSOAが有効に動作するアプローチに対して，マイクロサービスがどう適合するかを説明することが必要だという点がそうですし，そもそも相応なサイズ(12人)のチームから個人単位にサービスの範囲を変更することが，サービスの&quot;マイクロ&quot;化なのだと言えるのでしょうか。
  </blockquote> 
  <p>結論として氏は，マイクロサービスには何の新規性もない，サービス指向デリバリ(Service Oriented Delivery)アプローチに過ぎないのだという，自身の意見を改めて述べている。アーキテクトや開発者はマイクロサービスよりも，定義が明確で実績も豊富なSOAをもっと活用した方がよいだろう。マイクロサービスに新しさを見出すよりも，&quot;今日&quot;のSOAを論じることが必要なのだ。氏は次のように述べている。</p> 
  <blockquote>
   その事実を裏付けるものとして，参考例とされているNetflixでも，脚注にもあるように，実際には&quot;小機能(fine-grained)SOA&quot;という用語を用いています。もうひとつの参考例(Amazon)でも
   <a href="http://www.infoq.com/news/Amazon-CTO-Werner-Vogels-on-SOA">SOAという表現</a>を使っているのです。
  </blockquote> 
  <p>読者の意見はどうだろう？ マイクロサービスは単なるSOAなのだろうか，それとも根本的に異なるのだろうか？</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
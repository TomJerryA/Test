<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Vaughn Vernon氏、リアクティブドメイン駆動設計について語る</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/vernon-reactive-ddd"><em>原文(投稿日：2013/11/19)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://en.wikipedia.org/wiki/Actor_model">アクターモデル</a>と<a href="http://en.wikipedia.org/wiki/Domain-driven_design">ドメイン駆動設計</a>（DDD）を組み合わせることで、<a href="http://en.wikipedia.org/wiki/Event-driven_architecture">イベント駆動</a>や<a href="http://alistair.cockburn.us/Hexagonal+architecture">ヘキサゴナル</a>アーキテクチャでよく見られるアーキテクチャオーバーヘッドを取り除けるかもしれない。<a href="http://dddcommunity.org/book/implementing-domain-driven-design-by-vaughn-vernon/">Implementing Domain-Driven Design</a>の著者である<a href="http://vaughnvernon.co/">Vaughn Vernon</a>氏が、<a href="http://www.scala-lang.org/">Scala</a>と<a href="http://akka.io/">Akka</a>（アクターモデルの実装）を使ったリアクティブDDDについて<a href="http://skillsmatter.com/podcast/design-architecture/reactive-ddd-with-scala-and-akka">説明した</a>。</p> 
  <p>「リアクティブ」という新たな用語が使われているが、実際のところまったく新しい概念というわけではない。多くの人はイベントやメッセージに反応することに馴染みがあるはずだ。でも、これは私に新たな変化をもたらしてくれた。Vaughn氏はこう言って、アクターモデルの基本特性を次のように定義した。</p> 
  <ul> 
   <li>ダイレクトな非同期メッセージング。アクターは別のアクターに直接かつ非同期にメッセージを送る。</li> 
   <li>ロックフリーの並行性。アクターはロックを扱わない。インフラストラクチャだけがロックを扱う。</li> 
   <li>何も共有しない。アクターは他のアクターの内部状態について何も知らない。</li> 
  </ul> 
  <p>Vaughn氏がDDDを使うモチベーションの1つは、ビジネスのコアとなる側面を、非常に明確なやり方でモデル化したいためだ。通常、イベント駆動アーキテクチャの場合、ドメインモデルで明確にし、ドメインイベントがモデルに表現力を加えるが、完全にはっきりするわけではない。というのも、ドメインイベントが発行されたとき、そのイベントに反応するコードの場所や、最終的にモデルに影響を及ぼすコードの場所を見つけるが困難だからだ。<br /> これに対し、アクターモデルは非常に明確だと彼は考えた。アクターがメッセージを他のアクターに送るとき、それはコード上に非常に明確に現われるためだ。</p> 
  <p>Vaughn氏の疑問は、DDDでアクターモデルを使うことで、どれだけのメリットがあるかだ。すべて以前と同じアーキテクチャで、アグリゲート間でメッセージを送るだけの話なのだろうか？ それに対する彼の答えは、ノーだ。彼はこれにより、イベント駆動やヘキサゴナルアーキテクチャでよく見られるアーキテクチャオーバーヘッドの多くを取り除けると考えている。適切なフレームワークを用いることで、アーキテクチャをただのコントローラとアグリゲートにすることができる。コントローラがアクターになる。これはメッセージをディスパッチしてモデルのアグリゲートとやりとりする方法を知っている。<br /> 彼はアクターモデルとDDDが使える場所に制限があるとは思っていない。それどころか、高いスケーラビリティ、高い可用性、低いレイテンシが必要とされる場所にも適用可能だと考えている。</p> 
  <p>AkkaはJVM用に作られているが、Vaughn氏はAkkaをC#およびF#に移植しようと、Akka.NET実装に取り組んでいる。</p> 
  <p>今年前半、Vaughn氏はアクターモデルとDDDの組み合わせについて<a href="http://www.infoq.com/jp/news/2013/06/actor-model-ddd">語った</a>。</p> 
  <p>2013年9月に<a href="http://www.reactivemanifesto.org/">Reactive Manifesto</a>が発表された。このコンセプトの背景にある基本アイデアが説明されている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Akka Toolkit 2.3 は Java 8 と Persistence をサポートする</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/akka-2-3-released"><em>原文(投稿日：2014/03/11)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>最新版の <a href="http://akka.io/">Akka</a> Toolkit には、内部状態を永続化するステートフル・アクターを可能にする Persistence が付属する。最近リリースされた<a href="http://akka.io/news/2014/03/05/akka-2.3.0-released.html">バージョン 2.3.0</a> は Java 8 のラムダ式サポートも備えられている。</p> 
  <p><a href="http://doc.akka.io/docs/akka/2.3.0/scala/persistence.html">Akka Persistence</a>では、現在の状態ではなく、アクターの状態の更新が永続化される。変更は履歴に追加され、アクターの内部状態は保存された変更をリプレイすることによって再構築可能である。Event Sourcingや少なくとも1回のメッセージ配信も保証されている。<br /> Java 8 やラムダ式を使うことにより、<a href="http://doc.akka.io/docs/akka/2.3.0/java/lambda-actors.html">アクター</a>と<a href="http://doc.akka.io/docs/akka/2.3.0/java/lambda-fsm.html">有限オートマトン</a> (<a href="http://en.wikipedia.org/wiki/Finite-state_machine">FSM</a>) の両方とも、匿名内部クラスを定義する必要性を排除し、ラムダ式を使って実装できるようになっている。<br /> Persitence モジュールとラムダ式サポートは<em>実験的機能</em>であると位置づけられており、双方ともユーザからのフィードバックに基づき API を拡張することを目論んでいる。</p> 
  <p><a href="http://akka.io/news/2014/03/05/akka-2.3.0-released.html">他に以下の拡張</a>を含む：</p> 
  <ul> 
   <li>クラスタ機能として、影響するノードが応答するようになると障害条件をクリアして、部分的な到達不能から再び正常動作に復帰できるようになった 。</li> 
   <li>Cluster Sharding は、アクターが一台のマシンを供給することによりリソースを消費した時に、いくつかのノードにステートフル・アクターを配布することができる。</li> 
   <li>Akka IO パッケージは、実験的機能でなくなったが、パイプラインインフラストラクチャは廃止された。</li> 
   <li><a href="http://en.wikipedia.org/wiki/OSGi">OSGi</a> サポートは akka-actor OSGi バンドルを作成するために再作業された。</li> 
  </ul> 
  <p><a href="http://doc.akka.io/docs/akka/2.3.0/intro/getting-started.html">Getting started</a> ガイドといっしょに<a href="http://akka.io/docs/">ドキュメント</a>は、フレームワークの変更点を反映して更新された 。Akka はより大きな<a href="http://typesafe.com/platform/getstarted">リアクティブ・プラットフォーム</a>のサンプルの一部でもある。<br /> 新しいリリースは、2.2.* からアップデートする際に<a href="http://doc.akka.io/docs/akka/snapshot/project/migration-guide-2.2.x-2.3.x.html">コードの修正</a>を必要とするいくつかの構造的な変更を含んでいる。より以前のバージョンからのアップグレードは、さらなるステップを必要とするかもしれない。</p> 
  <p>Akka Toolkit は<a href="http://en.wikipedia.org/wiki/Actor_model">アクターモデル</a>の実装であり、Java と Scala API が利用可能である。 この 2.3 リリースは、2014年後半に計画されたより大きな<a href="https://docs.google.com/document/d/18W9-fKs55wiFNjXL9q50PYOnR7-nnsImzJqHOPPbM4E/pub">マイルストーン</a>の最初のステップである。<br /> Akka は、Apache 2 ライセンスの元にライセンスされた、オープンソース製品である。</p> 
  <p><a href="http://www.informit.com/store/implementing-domain-driven-design-9780321834577">Implementing Domain-Driven Design</a>の著者である、<a href="http://vaughnvernon.co/">Vaughn Vernon</a>は昨年<a href="http://www.infoq.com/jp/news/2013/11/vernon-reactive-ddd">リアクティブドメイン駆動設計の中でのアクターモデル</a>について、より以前には<a href="http://www.infoq.com/jp/news/2013/06/actor-model-ddd">DDDとアクターモデルの基盤</a>について語っている。</p> 
  <p>3000人以上のメンバーが参加している Akka ユーザのための<a href="https://groups.google.com/forum/#!forum/akka-user">フォーラム</a>が利用可能である。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
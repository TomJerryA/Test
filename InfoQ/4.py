<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ORMツール Hibernare 4.3がリリース，JPA 2.1仕様を実装</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/hibernate-4-3-released"><em>原文(投稿日：2013/12/31)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Javaベースの<a href="http://en.wikipedia.org/wiki/Object-relational_mapping">オブジェクト-リレーショナルマッピング</a><a href="http://en.wikipedia.org/wiki/Object-relational_mapping">(ORM)フレームワークである</a><a href="http://hibernate.org/orm/">Hibernate ORM 4.3</a>の最終版が先日リリースされた。ストアドプロシージャのサポートとエンティティグラフを提供するとともに，2013年5月にリリースされた<a href="https://jcp.org/en/jsr/detail?id=338">JPA 2.1仕様</a> – JSR 338の実装として認定されている。</p> 
  <p>今回の<a href="http://in.relation.to/Bloggers/HibernateORM430FinalRelease">リリース</a>のおもな目的は，JPA2.1仕様に加えて，次のような新機能をサポートすることにある。</p> 
  <ul> 
   <li>プロバイダやデータベースベンダに依存しない，標準化されたストアドプロシージャと関数呼び出し処理のサポート。</li> 
   <li>タイプセーフな方法によるUPDATEおよびDELETEクエリの定義と実行が可能になった。</li> 
   <li>ライフサイクルイベントを個別のクラスに実装するためのエンティティリスナで，依存性注入のために<a href="https://www.jcp.org/en/jsr/detail?id=299">CDI</a>標準 (JSR-299) が使用可能になった。</li> 
   <li>AttibuteConvererによって，データベース内の表現と対応するオブジェクトの間で，基本データ値を変換できるようになった。</li> 
   <li>Entityグラフによって，エンティティとそのサブエレメントがロードされる方法を定義できるようになった。グラフのロードされる方法を動的に変更することも可能だ。</li> 
   <li>プロバイダに依存しない，標準化されたスキーマ生成方法のサポート。すべてのプロバイダが対応する，構成設定のベースラインも提供されている。</li> 
   <li>永続コンテキストと現在のトランザクションとの同期がSynchronizationTypeでコントロール可能になった。</li> 
   <li>@ConstructorResultアノテーションを使用することで，SQLクエリから返された引数値を用いたオブジェクト構築が可能になった。</li> 
  </ul> 
  <p>新しいJPA仕様に関連しないその他の重要な変更には，次のようなものがある。</p> 
  <ul> 
   <li><a href="http://en.wikipedia.org/wiki/OSGi">OSGi</a>環境のサポートが拡張された。Hibernate 5ではさらにサポートが向上する予定だ。</li> 
   <li>インラインのダーティチェックがサポートされた。Hibernate内での新たなバイトコード拡張のサポートに基づいて，状態の変化したエンティティを検出する。</li> 
  </ul> 
  <p>新バージョンに対応して<a href="http://hibernate.org/orm/documentation/">ドキュメント</a>もアップデートされている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>MongoDBがセキュリティの改善、テキスト検索、パフォーマンス向上を実現</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/mongodb-2-4;jsessionid=C2F15D8231EDBE007EF45A0361CF607F"><em>原文(投稿日：2013/03/29)へのリンク</em></a></p> 
<div class="clearer-space"></div> 
<div id="newsContent"> 
 <p><a href="http://www.mongodb.org/" target="_blank">MongoDB</a> 2.4は最近、テキスト検索、ハッシュベースのシャーディング、GeoJSONサポートによる優れた地理空間機能、そしていくつかのパフォーマンス改善とツーリング群の改善を行なって、リリースされた。我々は、またロードマップ上の次のリリースが何であるのかを10genと話した。</p> 
 <p>主な改善点のいくつかは以下のとおりである 。</p> 
 <ul> 
  <li><a href="http://docs.mongodb.org/manual/release-notes/2.4/#text-search" target="_blank">テキスト検索</a>は、ベータ機能として導入され、15の言語で語幹処理とトークン化をサポートしている。</li> 
  <li><a href="http://docs.mongodb.org/manual/release-notes/2.4/#new-hashed-index-and-sharding-with-a-hashed-shard-key" target="_blank">ハッシュベースのシャーディング</a>は、あらゆる自然なシャーディングキーに分散しているデータを簡単に予測できない場合のためである。</li> 
  <li><a href="http://docs.mongodb.org/manual/release-notes/2.4/#new-geospatial-indexes-with-geojson-and-improved-spherical-geometry" target="_blank">地理空間インデックス</a>は、GeoJSONサポートによる。</li> 
  <li>セキュリティの強化-新しい<a href="http://docs.mongodb.org/manual/release-notes/2.4/#new-modular-authentication-system-with-support-for-kerberos" target="_blank">モジュラー認証システム</a>、Kerberosとの統合、<a href="http://docs.mongodb.org/manual/release-notes/2.4/#role-based-access-control-and-new-privilege-documents" target="_blank">ロールベースのアクセス制御</a></li> 
  <li>いくつかのパフォーマンスの向上、カウントや集計などのいくつかの特定のシナリオでは著しい改善。</li> 
  <li>V8がMongoのシェルにおけるデフォルトのJavaScriptエンジンになった（SpiderMonkeyを置き換え）。これで、JavaScriptベースのアクションのパフォーマンスと同時実行性が改善される。</li> 
  <li>クラスタのステータス監視用の追加メトリクス</li> 
 </ul> 
 <p>10genは、また 2.4のリリースと一緒に<a href="http://www.10gen.com/products/mongodb-enterprise" target="_blank">MongoDBのエンタープライズ版</a>も導入した。</p> 
 <p>我々は、10genの製品マーケティングのディレクターである<a href="http://www.linkedin.com/in/kellystirman" target="_blank">Kelly Stirman</a>氏に連絡を取り、新機能と次に何が期待できるのかを聞いた。</p> 
 <p>氏は、コレクション・レベルのロックがMongoDBにとって意味をなさないかも知れない理由を説明した。</p> 
 <blockquote> 
  <p>2.2で、ロックによる改善は、ロック競合を減らすことにより、ライト時のスループットに本質的な便益を提供しています。David Mytton氏が<a href="http://blog.serverdensity.com/goodbye-global-lock-mongodb-2-0-vs-2-2/" target="_blank">この主題で良い記事を書き上げました</a>。</p> 
  <p>MongoDBの2.4は、2.0と2.2で提供した改善を超えて、ロックの粒度に関して何も追加していません。私たちは、2.6では、ドキュメントレベルのロックを検討しています。改善を生み出したロックは、充分本質的だったので、コレクション・レベルのロックは大きな改善を追加しないでしょう。なので、ドキュメントレベルのロックが、次のステップでしょう。</p> 
 </blockquote> 
 <p>新しいハッシュベースのシャーディングの代わりに範囲ベースのシャーディングをどのような場合に使用するのかについて。</p> 
 <blockquote> 
  <p>範囲ベースのシャーディングを使用する場合、もしシャードキーの範囲に基づいて、アプリケーションがデータを要求するなら、それらのクエリは、通常、一つのシャード、あるいは恐らく僅かな数のシャードである、適切なシャードにルーティングされます。ハッシュベースのシャーディングを使用したシステムでは同じクエリは、ずっと多くのシャード、おそらすべてシャードにリクエストをルーティングします。理想的には、クエリは単一のシャードまたはできるだけ少数のシャードにルーティングされます。すべてのクエリをすべてのシャーにルーティングするよりも、この方がずっと良くスケールするからです。だから、あなたがよく自分のデータとクエリを理解していれば、恐らく範囲ベースのシャーディングが最適なオプションです。</p> 
 </blockquote> 
 <p>MongoDB 2.4では、カウントは最高で20倍速くなり、Aggregationフレームワークは平均で３～５倍早くなります。氏の説明によると、改良されたカウントパフォーマンスは、MongoDBにおけるBツリーのトラバースへのいくつかの改善に依存している。カーディナリティが低いインデックスベースのカウントにおいて、最大の改善が見られます。アグリゲーションフレームワークの改善は、MongoDBの内部実装における多くの小さな変更が積み重なって大きな恩恵をもたらした結果なのだ。</p> 
 <p>エンタープライズフィーチャでは、何が次に入るのですか？</p> 
 <blockquote> 
  <p>MongoDBの2.4は、セキュリティおよび監視の領域で大きく前進しましたが、将来のリリースには、はるかに多くのものを計画しています。我々は、認証、認可、および監査の次元に沿ってセキュリティを考えます。MongoDBの今後のリリースでも、これらの領域に注力していきます。我々はMongoDBのを提供するツール群を強化していきます。 <a href="http://www.10gen.com/products/mongodb-monitoring-service" target="_blank">MongoDB監視サービス</a>（MMS）は、MongoDBのコミュニティで非常に人気を得ており、15,000人以上のユーザがおり、急速に成長しています。私たちは、MMSへの投資を引き続き行い、当社のエンタープライズサブスクリプションの一部として、クラウドベースのツールとオンプレムの製品の両方を無料で提供していきます。</p> 
 </blockquote> 
 <p>MongoDB 2.4の新しいフィーチャについてもっと知りたければ、<a href="http://docs.mongodb.org/manual/release-notes/2.4/" target="_blank">リリースノート</a>と<a href="http://docs.mongodb.org/manual/release-notes/2.4-overview/" target="_blank">概要</a>を読むといい。</p> 
 <p id="lastElm"></p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
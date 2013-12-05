<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>RESTを使ったエンタープライズ統合から学んだこと</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/rest-enterprise-integration"><em>原文(投稿日：2013/11/28)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>大規模なレガシー置き換えはIT業界における苦行だ。Thoughtworksの主任コンサルタントの<a href="http://brandonbyars.com/about/">Brandon Byars</a>氏はこう言って、大規模なレガシー置き換えプロジェクトで<a href="http://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_Web_Services">RESTful</a>統合を使った<a href="http://martinfowler.com/articles/enterpriseREST.html">経験について語った</a>。<br /> Brandon氏はこうしたプロジェクトの多くで、<a href="http://ja.wikipedia.org/wiki/REST">REST</a> over HTTPを使うのが魅力的な選択肢になると考えている。これは使いやすく、理解しやすく、巨大なフレームワークを必要としないためだ。アーキテクチャ上、RESTはスケーラブルであり、ドメインモデリングにフィットすることがわかっていると彼は考えている。しかし、RESTに関する議論は、ささいな詳細に陥りがちだ。プロジェクトの成功を確実にするため、彼がより重要だと考えているのは、そのデプロイメント戦略やテスト戦略としての側面だ。</p> 
  <p>Brandon氏の最初のアドバイスは、論理的な環境を使って、さまざまなチームや役割のニーズを満たすことだ。</p> 
  <blockquote>
   論理的な環境とは、ビジネスや開発ニーズを満たすのに必要とされる、適切に独立した、相互に関係のあるアプリケーション、サービス、基盤コンポーネントの集合です。
  </blockquote> 
  <p>そうして、彼はさまざまな環境に取り組んでメンテナンスしてきた経験から、役に立つことがわかったテクニックについて説明した。彼が反論しているものの1つは環境のバージョニングだ。これはシステムとの連携をかなり複雑にするおそれがあると彼は考えている。</p> 
  <p>Brandon氏の経験によると、アーキテクトがやってしまう最も高くつく間違いの1つは、データ境界がきちんと定義されていないことだ。よく見られるアンチパターンは、エンティティに関するすべての情報を単一のデータストアに格納して、必要に応じてエクスポートするという戦略だ。これは<a href="http://ja.wikipedia.org/wiki/マスターデータ管理">マスターデータ管理</a>(MDM)の表面的な誤解によって引き起こされていると彼は考えている。それに対して、彼の解決策は、<a href="http://ja.wikipedia.org/wiki/ドメイン駆動設計">ドメイン駆動設計</a>(DDD)の概念である<a href="http://en.wikipedia.org/wiki/Domain-driven_design#Bounded_context">境界づけられたコンテキスト</a>内に各チームの定義をラップし、その用語が使われるときはいつも同じものを意味するというものだ。</p> 
  <blockquote>
   各ビジネスユニットは、境界づけられたコンテキスト間の明確な翻訳を備えた共通のエンティティについて、異なるモデルを持っています。
  </blockquote> 
  <p>彼はまた、分散システムに取り組むときには、ハイレベルなフィーチャに関するユーザーストーリーをエピックにまとめ、そのエピックを使って進捗を計測することを推奨している。これにより進捗の錯覚を避けることができる。たいていのストーリーはチームが約束通りに行うことを示すことで完了となるが、わずかなストーリーが足らないためにフィーチャーはデモできなくなるためだ。</p> 
  <blockquote>
   プログラムレベルのメトリクスは、ベロシティを追跡する主要メトリックとしてエピックを保持します。チームのユーザーストーリー・ベロシティは進捗の錯覚をもたらすおそれがあります。
  </blockquote> 
  <p>Brandon氏は、RESTfulサービスを使った戦略を支持しており、それがよりシンプルな開発を促すと信じているが、RESTは決して銀の弾丸ではないことを強調して話を締め括った。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>APIのバージョニングコスト</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/api-versioning"><em>原文(投稿日：2013/12/01)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>コントラクトのバージョニングやAPI/サービスのバージョニングというのは、SOAベースのシステムにとって常に検討事項だ。<a href="http://www.infoq.com/jp/articles/contract-versioning-comp2">互換性にまつわるインパクト</a>のため、もしくは<a href="http://www.infoq.com/articles/Web-Service-Contracts">クライアント-サービスのガバナンス</a>のために、それはまだサイエンスというよりもアートに近いものだ。貴重な経験をもたらす例がたくさんある（たとえば、<a href="http://www.infoq.com/jp/news/2013/09/versioning-restful-services">REST周辺</a>は<a href="http://www.infoq.com/news/2010/06/rest-versioning">極めて人気がある</a>）。だが、Jean-Jacques Dubray氏の<a href="http://www.ebpml.org/blog2/index.php/2013/11/25/understanding-the-costs-of-versioning#">書いた記事</a>は、この領域に科学的客観性をもたらそうとしている。</p> 
  <blockquote>
   最近、API（あるいはWebサービス）のバージョニングコストを見積るよう頼まれました。私はこの見積りを共有することにしました。API/サービスのバージョニングにまつわるコストについて、多くの人がまだ理解していないと感じたためです。
  </blockquote> 
  <p>JJ氏によると、調べていくうちに、APIの構築コストは、その後のバージョニングに使われたアプローチに依存していることがわかった。</p> 
  <blockquote>
   理解すべき重要なポイントは、たとえAPI消費者に対するコストがあなたにとって小さく見えたとしても、それは純粋なコストではないということです。そこにはリスクがあります、混乱したプロジェクト計画、使えない予算。。。API変更を予期していない消費者にとって、変更は即座にビジネス価値を失うことにつながります。
  </blockquote> 
  <p>続いて、この記事では、APIのバージョニングを3つのアプローチに分類している。（それぞれについて、詳しくは元の記事を参照。JJ氏がいかにコストの測定方法を定義したのかも含まれている）</p> 
  <ul> 
   <li>ノット型「すべてのAPI消費者は1つのバージョンに結びつけられており、そのAPIが変わると、すべての消費者は変更する必要がある。これは基本的に、消費者およびエコシステム全体にわたって、大きな波紋を引き起こす。」</li> 
  </ul> 
  <p><img src="http://www.infoq.com/resource/news/2013/12/api-versioning/ja/resources/Screen Shot 2013-12-01 at 15.44.36.png" alt="" _href="img://Screen Shot 2013-12-01 at 15.44.36.png" _p="true" /></p> 
  <ul> 
   <li>ポイントツーポイント型「サービスのすべてのバージョンは稼動したまま残され、消費者は必要に応じて、自ら移行する必要がある。稼動しているバージョン数が増加するにつれ、メンテナンスコストも増加する。」</li> 
  </ul> 
  <p><img src="http://www.infoq.com/resource/news/2013/12/api-versioning/ja/resources/Screen Shot 2013-12-01 at 15.46.06.png" alt="" _href="img://Screen Shot 2013-12-01 at 15.46.06.png" _p="true" /></p> 
  <ul> 
   <li>互換性のあるバージョニング 「すべてのクライアントが同一の互換性のあるバージョンのAPI/サービスとやりとりする。」</li> 
  </ul> 
  <p><img src="http://www.infoq.com/resource/news/2013/12/api-versioning/ja/resources/1Screen Shot 2013-12-01 at 15.48.14.png" alt="" _href="img://1Screen Shot 2013-12-01 at 15.48.14.png" _p="true" /></p> 
  <p>これらの定義とJJ氏が述べる方程式を使って計算されたコストを前提とすると、相対的コストは以下のようにプロットできる（y軸はコストで、x軸はバージョン番号）。</p> 
  <p><img src="http://www.infoq.com/resource/news/2013/12/api-versioning/ja/resources/Screen Shot 2013-12-01 at 15.54.16.png" alt="" _href="img://Screen Shot 2013-12-01 at 15.54.16.png" _p="true" /></p> 
  <p>&nbsp;</p> 
  <p>JJ氏はこう語る。</p> 
  <blockquote>
   [...] APIを変えるとき、すべての顧客にアップグレードを強制して、1つのバージョンにするのは、エコシステムに対して非常に高くつきます。メンテナンスを必要とするバージョンを複数持っておく方がよりよいのですが、各バージョンをアップグレードし続けたり、代わりに古いバージョンを運用し続けようとするのは、かなりのコストです。互換性のあるバージョニング戦略が最も効率がよいように思えます。
  </blockquote> 
  <p>他の人はどう思うだろうか？ このAPIのバージョニングコスト計算は、JJたちが開発した環境以外に適用できるだろうか？ この相対的なコストの説明はあなたの経験と合っているだろうか？ 彼らがカバーしていないカテゴリはあるだろうか？</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
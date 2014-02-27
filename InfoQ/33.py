<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>クラウドホスト型アプリケーションのためのデザインパターン</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/cloud-design-patterns"><em>原文(投稿日：2014/02/11)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Microsoftの<a href="http://pnp.azurewebsites.net/en-us/">patterns &amp; practicesグループ</a>がクラウドホスト型アプリケーションの実装に適したソリューションとパターンを提案した<a href="http://msdn.microsoft.com/en-us/library/dn568099.aspx">ガイド</a>をリリースした。このガイドは各種パターンが解決する問題を、その利点と欠点とともに説明している。このグループは（たとえ例が<a href="http://www.windowsazure.com/">Windows Azure</a>を対象としていようとも）クラウドプラットフォームによらない分散システムのためのガイドを提供することを目的としている。</p> 
  <p>彼らは開発者コミュニティからのフィードバックを活用して、クラウドアプリケーションの開発で最もよく見られる領域をカバーした8つの問題カテゴリを定義した。</p> 
  <ul> 
   <li><a href="http://msdn.microsoft.com/en-us/library/dn600219.aspx">可用性 (Availability)</a></li> 
   <li><a href="http://msdn.microsoft.com/en-us/library/dn600216.aspx">データマネジメント (Data Management)</a></li> 
   <li><a href="http://msdn.microsoft.com/en-us/library/dn600217.aspx">設計と実装 (Design and Implementation)</a></li> 
   <li><a href="http://msdn.microsoft.com/en-us/library/dn600220.aspx">メッセージング (Messaging)</a></li> 
   <li><a href="http://msdn.microsoft.com/en-us/library/dn600218.aspx">マネジメントとモニタリング (Management and Monitoring)</a></li> 
   <li><a href="http://msdn.microsoft.com/en-us/library/dn600224.aspx">パフォーマンスとスケーラビリティ (Performance and Scalability)</a></li> 
   <li><a href="http://msdn.microsoft.com/en-us/library/dn600215.aspx">弾力性 (Resiliency)</a></li> 
   <li><a href="http://msdn.microsoft.com/en-us/library/dn600221.aspx">セキュリティ (Security)</a></li> 
  </ul> 
  <p>彼らは各カテゴリごとに指針を作って、開発者がよく遭遇する問題を解決する助けになるよう、共通のパターンをドキュメント化した。</p> 
  <p>このガイドには基礎知識と実践テクニックとして10の入門および指針のトピックが含まれており、それぞれアプリケーション開発の1面をカバーし、1つのカテゴリを対象としている。カバーしているトピックには、Asynchronous Messaging、Caching、Data Consistencyなどが含まれている。</p> 
  <p>また、彼らがクラウドホスト型アプリケーションで有用だと考える24のデザインパターンも含まれている。それぞれのパターンは1つ以上のカテゴリに属しており、たとえば、Compensating Transaction、Command and Query Responsibility Segregation (CQRS)、Pipes and Filtersといったパターンが含まれている。それぞれのパターンは、適用されるコンテキストと問題、パターンが提供するソリューション、パターンを適用する際の課題と考察を含んだ共通のフォーマットで説明されている。また、それぞれのパターンに対するAzureの例も提供されている。</p> 
  <p>説明したデザインパターンの使い方を実演するため、彼らは10のサンプルアプリケーションを作り、すべてのソースコードを<a href="http://www.microsoft.com/en-us/download/details.aspx?id=41673">ダウンロード</a>できるようにしている。サンプルには、サービスバスからメッセージを取得する消費者の競合に関するアプリケーションや、フィルタを使ってパイプラインをシミュレートするアプリケーションが含まれている。<br /> なお、彼らは、これらのサンプルは単純化されており、そのまま製品に使えるようには作られていないと強調している。</p> 
  <p>Windows AzureはMicrosoftが提供するクラウドプラットフォームだ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>MicrosoftとAWSがクラウド最適化サービスを無償提供</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/microsoft-metricshub-aws-advisor;jsessionid=4D360DBBA689B6EDC7FDB40D11C3704E"><em>原文(投稿日：2013/03/11)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>クラウドの利用を最適化するサービスの周囲の小さな産業は成長しているが、大規模なクラウド事業者も独自で最適化のサービスを提供し始めている。Microsoftは近頃、クラウドの性能を管理する企業を買収し、その会社の製品の無償提供を始めた。競合のAmazon Web Services (AWS)も“Trusted Advisor”プログラムの無償トライアルを積極的に推進している。</p> 
 <p>スタートアッププログラム<a target="_blank" href="http://www.microsoft.com/bizspark/accelerator/">The Microsoft Accelerator</a>の参加者である<a target="_blank" href="https://www.metricshub.com">MetricsHub</a>は、先週Microsoftに買収された。同社はクラウド環境の自動拡張や監視、性能問題の検知とアラート、Windows Azureのインボイスの解析などの<a target="_blank" href="https://www.metricshub.com/features?a=0&amp;sku=NoSKU">サービス</a>を提供する。<a target="_blank" href="http://techcrunch.com/2013/03/04/microsoft-acquires-cloud-performance-management-service-metricshub-makes-it-available-for-free-on-azure/">TechCrunchによれば買収された時点で、同社はたった374のユーザしか抱えていない</a>が、<a target="_blank" href="http://blog.metricshub.com/2013/03/04/future-of-metricshub/">MetricsHubのブログ</a>によれば、“無数のデータポイントを処理し、数千の自動アクションでクラウドアプリケーションのヘルスとコストの管理を支援します”。Microsoftはこの買収をブログで発表し、クラウド最適化の難しさとMetricsHubを買収した理由を説明した。</p> 
 <blockquote> 
  <p>拡張性や柔軟性などさまざまな理由でクラウドソリューションを利用せざるを得なくなっています。とりわけ最小限の投資で最大限の成果を上げようとしている企業にとってはそうでしょう。しかし、いつどのようにアプリケーションを拡張すればいいのか教えてくれる、すべてのデータポイントを監視し相関関係を探し、理解するのは難しいです。このようなデータポイントから本当の価値を引き出すには、アプリケーションがインテリジェンスを持って返答するように自動化する必要があります。ここがMetricsHubの技術が活かされる場面です。性能最適化を自動化する彼らの手法は顧客に負担をかけずに事態に対処できます。また、顧客が必要な分だけ支払いを行い、サービスの利用を最大化することを保証します。</p> 
 </blockquote> 
 <p>今回のプレリリースサービスはMicrosoftのすべての顧客が無償で利用できる。既存の顧客はこの無償プランに移行されるようだ。</p> 
 <p>AWSもクラウドを最適化するサービスを推進し、安全でコストパフォーマンスが良い環境を作成している。2012年に始まった<a target="_blank" href="https://aws.amazon.com/support/trustedadvisor/">AWS Trusted Advisor</a>プログラムはAWSサービスを監視し、性能改善や費用節約になる、すぐに出来るアクションを推薦する。このプログラムはプレミアムAWSサポートを利用している顧客に提供されるが、3月はAWSのすべての顧客に無償提供される。AWSチームは<a target="_blank" href="http://aws.typepad.com/aws/2013/03/aws-trusted-advisor-update-trial-new-features.html">この無償提供のトライアルについて</a>、このサービスの価値と成績を説明している。</p> 
 <blockquote> 
  <p>AWS Trusted AdvisorはAWSの多くの顧客によって利用されてきましたので、このサービスの推薦は信頼して役立てることができます。費用を節約したり、安全性を向上させたり、耐障害性を改善したり、全体の性能を向上させたりできます。これはクラウドベースのAPIで利用できるインフラでのみ可能なユニークで強力な利点です。</p> 
  <p>この推薦機能の価値を見るために最後の90日に注目してください。この期間、AWSの顧客はTrusted Advisorから135000の推薦を受け取り、年額1800万ドルを節約しました。</p> 
 </blockquote> 
 <p>Trusted Advisorの推薦機能は4つのカテゴリに分類される。コスト最適化、セキュリティ、フォールトトレランス、性能の4つだ。コスト最適化には“未活用のEC2インスタンス”(過去14日間で4日、CPU使用率10%以下のインスタンス)や“RDSがアイドル状態のDBインスタンス”(過去7日間でコネクションがないアクティブなデータベース)などが含まれる。セキュリティには7つの推薦があり、アクセス権限が弱いS3のバケットやアイデンティティとアクセス管理がサービスをまたいで利用されているかどうかを検出する。フォールトトレランスではVPNトンネルの冗長性、データベースのバックップ、複数の地域にまたがるデータベースや、地域をまたがるノードが不均等に分散している点などを検出する。性能ではCPUの平均利用率が90%を超えているサーバや過度のルール数を抱えるセキュリティグループなどを検出する。</p> 
 <p>MicrosoftとAWSの顧客にとってはこれらのサービスが無料で利用できるのは喜ばしいことだが、パートナーにとってはそれほどではない。Microsoftはパートナーの事業領域に侵入することで悪名高く、AWSも同じ道を辿りそうだ。<a target="_blank" href="https://cloudability.com/">Cloudability</a>、<a target="_blank" href="http://www.newvem.com/">Newvem</a>、<a target="_blank" href="http://www.cloudyn.com/">Cloudyn</a>、<a target="_blank" href="https://www.cloudvertical.com/">CloudVertical</a>などの会社は有償でAWSクラウドの監視と最適化を行うサービスを提供している。<a target="_blank" href="http://www.theregister.co.uk/2013/03/08/amazon_copies_partner_products/">The Registerの記事</a>はパートナーの不満と巨大で野心的なサービスプロバイダのアドインを構築している企業が抱える困難を指摘している。</p> 
 <blockquote> 
  <p>このAmazonのスポークスマンの発言の行間を読めば、Amazonはサービスの開発を続け、パートナーはAmazonによるコモディティ化の波から逃げるべく走り続けなければならないことがわかるだろう。</p> 
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
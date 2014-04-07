<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Googleのクラウド価格引き下げに対するAmazonの反応</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/aws-price-cut"><em>原文(投稿日：2014/03/29)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>GoogleはComputer Engine, Storage, BigQueryなど，同社の<a href="http://www.infoq.com/news/2014/03/google-cloud">クラウドサービスの価格を大幅に引き下げる</a>と発表した。しかし同社の価格的なアドバンテージはわずか24時間しか続かなかった。Amazonがその翌日，EC2, S3, RDS, ElasticCache, MapReduceといった<a href="http://aws.typepad.com/aws/2014/03/aws-price-reduction-42-ec2-s3-rds-elasticache-and-elastic-mapreduce.html">同社のサービスを大幅に切り下げた</a>ためだ。</p> 
  <p>次表はAWSの価格引き下げの概要をまとめたものだ。</p> 
  <table cellspacing="0" cellpadding="2" width="625" border="1" unselectable="on"> 
   <tbody> 
    <tr> 
     <td valign="top" width="131"><strong>サービス</strong></td> 
     <td valign="top" width="114"><strong>値下げ率 (%)</strong></td> 
     <td valign="top" width="358"><strong>コメント</strong></td> 
    </tr> 
    <tr> 
     <td valign="top" width="131">EC2 - オンデマンド</td> 
     <td valign="top" width="114">7-40</td> 
     <td valign="top" width="358">値下げ率はインスタンスタイプによって異なる。</td> 
    </tr> 
    <tr> 
     <td valign="top" width="131">EC2 - リザーブド</td> 
     <td valign="top" width="114">10-40</td> 
     <td valign="top" width="358">値下げ率はインスタンスタイプによって異なる。最大68%の値引きとなるボリュームディスカウトもある。</td> 
    </tr> 
    <tr> 
     <td valign="top" width="131">S3</td> 
     <td valign="top" width="114">36-65</td> 
     <td valign="top" width="358">平均51%</td> 
    </tr> 
    <tr> 
     <td valign="top" width="131">RDS</td> 
     <td valign="top" width="114">28</td> 
     <td valign="top" width="358">平均</td> 
    </tr> 
    <tr> 
     <td valign="top" width="131">ElasticCache</td> 
     <td valign="top" width="114">34</td> 
     <td valign="top" width="358">平均</td> 
    </tr> 
    <tr> 
     <td valign="top" width="131">MapReduce</td> 
     <td valign="top" width="114">27-61</td> 
     <td valign="top" width="358">hs1.8xlargeの価格で1000ドル/TB/年以下になる。</td> 
    </tr> 
   </tbody> 
  </table> 
  <p>Amazon CEOのJeff Bezos氏がWebサイトに掲載した顧客向けの価格引き下げ記事には，今回はAmazonが2008年以降に実施した値下げの42回目である，と記載されている。しかしその<a href="http://aws.typepad.com/aws/2014/03/aws-price-reduction-42-ec2-s3-rds-elasticache-and-elastic-mapreduce.html">ブログ記事</a>には何人かの読者が，彼らの&quot;費用削減を実現してくれた&quot;Googleに対する感謝のコメントを寄せている。</p> 
  <p><a href="http://www.rightscale.com/blog/cloud-cost-analysis/aws-responds-price-cuts-google-vs-aws-pricing-round-2">AWSの新価格をGoogleの価格と比較したRightScale</a>では，On Demandの標準インスタンス価格はまったく同じ，という結論に達している。しかしハイメモリとハイCPUのインスタンスにおいては，Googleの方がまだ，それぞれ33%および16%低価格である。ただしAWSのハイメモリインスタンスはメモリ容量が30%大きく，ハイCPUではメモリおよびSSD容量が倍であるので，実質的にはほとんど同じだ。</p> 
  <p>１年間のリザーブドインスタンスと長期利用割引(Sustained Use)を比較すると，AWSの標準およびハイメモリインスタンスの方がGoogleの100%-useよりも10～20%安価だが，ハイCPUについては高価(2～3%)だ。AWSの価格差が大きいのは3年間のリザーブドインスタンスで，Googleの長期利用割引よりも32～48%低価格である。しかしながらモデルの差も大きく，AWSが前払いであるのに対して，Googleの費用は年次計算になっている。RightScaleではクラウドユーザ向けに，価格的に優位な３つのシナリオを描いてみせている。</p> 
  <blockquote> 
   <ul> 
    <li>キャッシュが潤沢で利用方法を正確に予測できるクラウドユーザは，AWSのRIで費用を節約することができます。</li> 
    <li>クラウドのワークロードがまだ急激に増加中で，オンデマンドインスタンスとリザーブドインスタンスを併用するメリットを得たい多くのユーザにとって，もっともコスト効果の高い方法は，必要とするインスタンスの正確なタイプとRI利用の有効度によって異なります。</li> 
    <li>ワークロードに関する予測可能性が高くなく，主としてオンデマンドを利用するクラウドユーザは，Googleのサービスを使用することで費用を節約できるでしょう。</li> 
   </ul> 
  </blockquote> 
  <p>MicrosoftはAzureサービスの価格を部分的に引き下げた１年前に，&quot;計算やストレージ，帯域幅といった一般的サービスについては，<a href="http://blogs.msdn.com/b/windowsazure/archive/2013/04/16/the-power-of-and.aspx">価格をAmazonのWebサービスに合わせる</a>&quot; ことを約束している。我々はMicrosoftが価格を発表する今週まで今回の記事の発表を保留していたのだが，公開時点に至るまでレドモンドからは何の発表もない。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
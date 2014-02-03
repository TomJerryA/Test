<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PaaSに何が起きているのか？</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/paas-future"><em>原文(投稿日：2014/01/22)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>巨額の投資や長期の開発にもかかわらず，PaaSはいまだ多くのユーザを引き付けることに成功していない。この記事ではPaaSの現状とその将来について，何人かのアナリストによる意見を要約して紹介する。</p> 
  <p>PaaSは長い間，アプリケーション-サービス-ソフトウェア層とクラウドインフラストラクチャを結び付けるために必要な “接合剤” だと考えられてきた。<a href="http://cloudofdata.com/author/Paul/">Paul Miller</a>氏は &quot;<a href="http://cloudofdata.com/2013/12/is-paas-dying/">Is PaaS dying?</a>&quot; と題した記事の中で次のように書いている。</p> 
  <blockquote> 
   <p>プラットフォームの役割とは，明解で説得力があり，かつパワフルであることです。汎用のハードウェア上で動作するさまざまな安い仮想マシンよりも，重要で関心の高い，基本的なパーツであるべきです。プラットフォームこそがクラウドを支える原動力であり，クラウドが世界中のビジネスやビジネスモデルを変革し続けられる<em>理由</em>なのです。</p> 
  </blockquote> 
  <p>しかしMiller氏は，&quot;このような期待に対して，カテゴリとしてのPaaSはまったく応えられていない&quot; という。さらに最近では，<a href="http://gigaom.com/2013/12/03/so-do-you-really-need-a-paas/">PaaSは本当に必要なのか</a>，<a href="http://www.networkworld.com/news/2014/011314-paas-277660.html">PaaSは滅亡種なのではないか</a>，あるいは<a href="https://451research.com/report-short?entityId=79800">IaaSに吸収されるのではないか</a>，という声さえ聞かれる。事実，<a href="http://www.itworld.com/cloud-computing/400208/paas-winners-and-losers-so-far-might-surprise-you">先頃発表されたGartnerのApplication PaaS(aPaaS) Magic Quadrant</a>の論議の中ではNancy Gohring氏が，その驚くべきユーザ数について指摘している。Googleこそ約30,000のユーザを有しているものの，その他はSnapchatやKhan Academyといったビッグネームでさえも小規模なWebサイトに過ぎないのだ。実数は発表されていないが，&quot;GoogleがSalesforceよりランクが低い&quot; 事実からGohring氏は，Salesforceについても &quot;おそらくGoogleのApp Engineより多くのユーザ&quot; がいるのだろう，と考えている。しかし，よいニュースはそこまでだ。</p> 
  <blockquote> 
   <p>Gartnerの報告書でより興味を引くのは，ユーザ数の少ないベンダに関する部分です。その中にビッグネームがいくつも含まれているからです。例えばIBMのSCASサービスについて，Gartnerは，全世界のユーザ数を50未満と推定しています。SAPについても100ユーザ以下だとGartnerは言っています。OpenShiftを提供することで中心的な存在であるRed Hatでさえ，Gartnerによれば&quot;有償ユーザは少数&quot;なのです。</p> 
  </blockquote> 
  <p>新規参入組については，状況は少し明るくなる。&quot;ヨーロッパ市場にサービスを提供するドイツ企業であるCloudControlには400，Dockerには500の有償ユーザがあると発表されています。&quot;</p> 
  <p>7年を経過した (<a href="http://www.google.com/trends/explore#cat=0-5&amp;q=paas">Googleトレンドによると</a>，PaaSという単語が始めてWebに現れたのは2007年3月ということだ) 現在もPaaSには，IaaS (Amazon AWSを見よ) やSaaS (Salesforceを見よ) のような成熟は見られない。451 Researchグループは，先日公開した &quot;<a href="https://451research.com/report-short?entityId=79800">Is PaaS becoming just a feature of IaaS (PaaSはIaaSの一機能になってしまうのか)?</a>&quot; (記事の参照には登録が必要)と題する記事の中で，PaaSはIaaSに吸収されるのではないのか，という疑問を提示している。確かにGoogleもMicrosoftも，当初PaaSプロバイダとして出発したが，後に自社のサービス範囲をCPUやストレージなどのIaaS分野へと拡張している。</p> 
  <p>PaaSに何が起きているのだろう？ それはなぜ？ PaaSは生き残れるのだろうか？ Krishnan Subramanian氏は，PaaSがハイプ(誇大広告)のピークを過ぎて&quot;新たな成熟レベルに達した&quot; と考えている。不足する部分はまだ多いが，それでも2013年には重要な開発が行われた。大きく分けて２つの分野だ。</p> 
  <ul> 
   <li><strong>サービスオーケストレーションによるPaaS</strong> – &quot;Google App Engineのような初期プロバイダが提供するこの分野のPaaSでは，アプリケーションに必要なさまざまなサービスを組み合わせることで，プラットフォームが開発されています。&quot;</li> 
   <li><strong>コンテナオーケストレーションによるPaaS</strong> – &quot;高速で軽量なLinuxコンテナを使って，クラウドプロバイダ間でのユーザアプリケーション移植を容易にするもので，Dockerがまさにその例です。計算能力のみを抽象化する仮想マシンとは違って，コンテナでは，アプリケーションとアプリケーション環境全体をカプセル化することができます。&quot;</li> 
  </ul> 
  <p>Mike Kavis氏は<a href="http://www.virtualizationpractice.com/war-paas-24684/">PaaSの企業への導入が遅れている理由</a>として，氏が考える３つの原因について概説している。</p> 
  <ol> 
   <li><strong>不明確なマーケティングメッセージ</strong> – &quot;HerokuやGoogle, MicrosoftなどのパブリックPaaSプロバイダと，ApperendaやOpenShift, Pivotal, WSO2，その他多数のプライベートないしハイブリッドPaaSソリューションがあります。さらにモバイルやビッグデータ，ソーシャルといった特定分野にフォーカスした特定ドメイン用のPaaSソリューションも存在する，といった状況です。... AWSのElastic Beanstackなど，PaaS的なサービスを提供するIaaSプロバイダも少なくありません。事態をさらに混乱させているのが，GoogleやMicrosoftがIaaSとPaaSの両方を提供するようになったことです。PaaSであるMicrosoft Azureと，IaaSソリューションであるAWSを比較しようとしている人を見かけない日はありません。さらに悪いことに，いわゆる &quot;専門家&quot; さえ十分に理解できていないのです。&quot;</li> 
   <li><strong>成熟度の欠如</strong> – &quot;PaaSにとって難題なのは，SaaSとIaaSが多くのユーザの目から見て，どちらもすでに企業利用レベルに達していて，企業において多大な信頼を得ていることです (少なくともAWSはそうです)。PaaSは今，2008年当時のAWSと同じような，ニーズの大半が新興企業や中小企業からのものであった頃の状況にあります。大企業での印象的な成功例もありますが，数は多くありません。&quot;</li> 
   <li><strong>制限事項</strong> – &quot;これらのようなPaaSには，単に飛び乗ってコードをどんどん作り始めればよいのだ，という認識があります。それは事実かも知れませんが，正しく機能するコードを作るには，PaaSの限界を十分に理解した上で設計を行わなければなりません。例えばHerokuにはdynoというものがあります。インフラストラクチャとスタックをすべて保持する，仮想コンテナだと思えばよいでしょう。Herokuは適当と判断した場合，dynoをランダムにリサイクルします。その際に，エラーコードに対処するために与えられる時間は全部で10秒間です。... そう，まったく突然，プログラムにターゲットPaaSプラットフォームへの依存性が持ち込まれます。おそらくは予想していなかったロックインが形成されるのです。... ほとんどPaaSアーキテクチャにおいて，その制限を回避しようという試みは，それに必要な作業量と抽象化された多数のリソースを処理するコストのため，困難で高価，時には不可能でさえあります。大規模なアプリケーションはほとんどの場合，リソースの制限を受けるPaaS上よりも，IaaSソリューション上で提供した方が良好に動作するのです。&quot;</li> 
  </ol> 
  <p>Ben Kepes氏は<a href="http://www.forbes.com/sites/benkepes/2013/11/20/apprenda-scores-c-round-is-paas-finally-here/">Forbesへの寄稿</a>の中で，プレイヤの数があまりにも多過ぎる，PaaS市場はまだ固まっていない状態なのだ，と述べている。</p> 
  <blockquote> 
   <p>PaaSは奇妙な状況にあると言ってよいでしょう。Pivotal OneのCloud Foundryの持つ趣向にマインドシェアの大半が吸い寄せられて，その他のCloud Foundryベンダは差別化に頭を悩ませているように思えます。その中で<a href="http://www.google.com/finance?q=NYSE:RHT">RedHat</a>は，自身のPaaSである<a href="http://https//openshift.redhat.com/">OpenShift</a>によって，ある種の脱出速度に到達しようとしています。Heroku (現在はSalesforce.comの所有)や<a href="http://www.engineyard.com/">EngineYard</a>といった業界の重鎮も，PaaSの車輪を回すことを止めていません。さらにOpenStackに連なる企業が集合して独自のPaaSイニシアティブであるSolum発足を決定する，という事実に至っては，あなたも混乱するでしょうし，市場も困惑します。シアトル出身のモンスター，すなわちAWSとMicrosoftをそれに加えれば，世界中でPaaSの購入を実際に決定している半ダースほどのユーザ企業に対して，ほとんど１社に１つのベンダが存在しているようなものです。</p> 
  </blockquote> 
  <p>将来のことになると，意見はさまざまだ。</p> 
  <p>Brandon Butler氏 (<a href="http://www.networkworld.com/news/2014/011314-paas-277660.html?page=2">Is the PaaS market as we know it dying (私たちが知っているPssSは死に絶えるのか)?</a>) は，</p> 
  <blockquote> 
   <p>&quot;多くの人たちが，PaaSはDOA – 到着時死亡なのだ，と言っている&quot;，自身の独立事務所AVOAを持つCIO戦略アドバイザのTim Crawford氏は，このように述べています。氏も認めているように，IaaSやSaaSベンダの動きの方がはるかに活発なことを考慮すれば，スタンドアロンのホストプラットフォームとしてのPaaSが，企業の採用を獲得するための&quot;課題&quot;は少なくありません。</p> 
  </blockquote> 
  <p><a href="http://www.forbes.com/sites/benkepes/2013/11/20/apprenda-scores-c-round-is-paas-finally-here/">Kepes</a>氏: &quot;今こそPaaSは，市場においてファンタジー以上のものであることを，自ら証明しなければならないのです。&quot;</p> 
  <p><a href="http://www.virtualizationpractice.com/war-paas-24684/">Kavis</a>氏:&quot;PaaSは死んではいません – 実際それは生まれたばかりで，市場を奪い取る機会を待っているのです。問題なのは，現在はまだ多くの企業の投資対象には程遠い状態である，ということです。&quot;</p> 
  <p><a href="http://www.informationweek.com/cloud/platform-as-a-service/paas-is-dead-long-live-paas/d/d-id/1113444">Subramanian</a>氏: &quot;PaaSに対する早まった死亡宣告は，現在進められている開発に多くの価値を期待できたはずの，この業界を傷つける結果になるでしょう。&quot;</p> 
  <p>ハイプの時期を乗り越えた2014年にPaaSが成熟して，確固たる提案として十分な信頼性を備えることで企業に受け入れられ，成功への道へと進むことができるのか，今はまだ分からない。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
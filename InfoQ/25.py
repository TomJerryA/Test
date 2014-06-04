<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>FirefoxにHTML5 DRMを追加するというMozillaの計画にさまざまな反応があった</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/firefox-drm"><em>原文(投稿日：2014/05/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Mozillaは今週、FirefoxにMicrosoft, Google, Appleのそれぞれのブラウザーで実装しているDRMを追加したことを発表した。</p> 
  <p>Mozilla Foundationのexecutive chairwomanであるMitchell Baker氏は、彼女の&quot;DRMとユーザーにサービスを提供する課題&quot;という<a href="https://blog.mozilla.org/blog/2014/05/14/drm-and-the-challenge-of-serving-users/">記事</a>においてMozillaは、DRMを展開する新しいメカニズムを導入することについて、困難な立場にいると発表した。Encrypted Media Extensions (EME)仕様は、FlashやSilverlightのような従来のプラグインではなく、HTML5の&lt;video&gt;エレメントを使ってDRMコンテンツを再生する方法を定義する。Baker氏は、MozillaがDRMを嫌いにも関わらず、FirefoxがDRM制御されたコンテンツを見るためのメカニズムを提供する必要があると信じていると述べた。</p> 
  <p>彼の発表記事&quot;<a href="https://hacks.mozilla.org/2014/05/reconciling-mozillas-mission-and-w3c-eme/">MozillaのミッションとW3C EMEとの和解</a>&quot;へのコメントによるとMozilla CTOのAndreas Gal氏は、もしW3C EME仕様を実装しなければ、FirefoxユーザーはDRMで制限されたコンテンツを見るために他のブラウザーに切り替える必要があり、それによってWebブラウザーとしてのFirefoxに関する疑問を呼び起こすことになると言う。彼によると:</p> 
  <blockquote> 
   <p>MozillaはDRMで進行中の変更を無視することが難しくなってきました。Mozillaの哲学的に、コンテンツのオーナーが制限をかけることに反対している場合でも、Firefoxはコンテンツを楽しみたいと考えるユーザーを助ける必要があります。</p> 
   <p>これは、完全にオープンなWebという私たちのビジョンにおいて難しく不快なステップですが、これはまたDRMスペースを形成して、この議論で私たちのユーザーやその権利の擁護者になる機会も与えてくれます。GoogleとMicrosoftがリリースしている既存のW3C EMEシステムはオープンソースではなく、ユーザーへの透明性を欠いており、私たちが信じる2つの特性は、信頼できるWebを構築する上で不可欠です。</p> 
  </blockquote> 
  <p>オープンソースとDRM間の対立に直接対処して、Gal氏はMozillaはユーザーを中心としたオープンWebを信じ続けており、オンライン体験をユーザー自身が制御できるようにしていることを強調した。オープンWebの原則に&quot;反して&quot;DRM方式にする代わりに、Gal氏は&quot;電子透かしのようなコンテンツ配信を管理するためのよりモダンなアプローチ&quot;を長い間提唱しており、&quot;コンテンツ産業が、コンテンツのロックから特定のデバイスに移り、代替を提供することが好ましい&quot;言う。</p> 
  <p>Mozillaは、ユーザーがDRM制御コンテンツを見ることができる重要な機能を提供するためにAdobeを選択した。Baker氏は、この機能はすでにFlashが提供しており、Gal氏独自の保証を強化して、Mozillaは可能な限り個々のユーザーの利益を保護したいと話した。</p> 
  <p>提案されたメカニズムの機能はユーザーにDRM実装を有効にするかどうかを選択する機能を提供するだけでなく、Gal氏が&quot;オープンソースサンドボックス&quot;として参照するコンテンツ復号化モジュール (CDM:Content Decryption Module)をラップしたことにより、ユーザープライバシーを維持する。このようにMozillaは、CDMは暗号化されたデータの取り出しと結果を表示するだけのメカニズムではなく、サンドボックスでCDMがユーザーのハードドライブにアクセスできないようにすることを目指している。</p> 
  <p>Web界隈の反応は複雑な感情が交ざったものだった。 <a href="https://www.fsf.org">Free Software Foundation</a>のエグゼクティブ ディレクターJohn Sullivan氏は、MozillaとAdobeのパートナーシップを&quot;フリーソフトウェア活動とMozillaの基本理念に反する&quot;と<a href="http://www.fsf.org/news/fsf-condemns-partnership-between-mozilla-and-adobe-to-support-digital-restrictions-management">避難した</a></p> 
  <blockquote>
   Free Software Foundationは、Mozillaの発表に非常に失望しています。この決定は、ブラウザーマーケットシェアを失うことについて誤った不安を緩和するために重要な原則を損なっています。 
   <p>&nbsp;</p> 
   <p>私たちはMozillaがしぶしぶやっていることを認識しており、MicrosoftやAmazonから来たときよりも、Mozillaから来た言葉を信じています。同時にDRMを実装したほぼすべての人がそれをすることを余儀なくされたと言い、その説明責任を欠くことは、実践がそれ自身の維持することです。Mozillaの発表では、残念ながらそれが置かれ -- この点では -- 競合他社と同じカテゴリに入ります。</p> 
   <p>Mozillaの妥協は、ユーザーを集めるための表だった努力をすることなく、この仮定を&quot;選択を強要&quot;したことは重ねて残念です。彼らはこの決定を撤回するべきです。しかし、彼らがそれをするにしろ、しらないにしろ、彼らがそれをサポートすることに専念していることで、恒久的にDRMを排除するために彼らの豊富な資源の多くを費やすことで私たちに参加するように呼びかけています。</p> 
  </blockquote> 
  <p>元CEOのBrendan Eichは、<a href="http://openwall.info/">Openwall</a>の創設者Alexander Peslyak氏から<a href="https://twitter.com/solardiz/status/466664526516346881">Twitter</a>で&quot;あなたは状況を考えてMozillaのDRMの変更をサポートできますか？それはあなたがCEOやCTOだったとしても同じでしょうか？(みんなが推測する)&quot;と尋ねられた。</p> 
  <p>Eich氏は<a href="https://twitter.com/BrendanEich/status/466666103972696064">返信した</a>: &quot;私がMozillaにいたとき、私はこの最小最悪のEME計画をサポートした。&quot; そして、彼はまだ&quot;DRMなしのソリューション&quot;に取り組んでいた。 2013年にEich氏によって欠かれた<a href="https://brendaneich.com/2013/10/the-bridge-of-khazad-drm/">記事</a>では、Silverlightのような既存のプラグインをHTML5向けのCDMで置き換えることを直接提案していた。チームは市場シェアを失わない方法で、&quot;提案されたAPIの右側にMozillaとすべての私たちのユーザーを得るために働いていた&quot;とEich氏は言う。</p> 
  <p>FirefoxがW3Cに反発するためにやっているか、EMEコンテンツを許可することを拒否した場合、サポーターを失うか得るかコミュニティの怒りを買う議論は続いている。有名な<a href="http://craphound.com/msftdrm.txt">アンチDRM</a>のCory Doctorow氏は、&quot;Mozillaは、DRMからの害を最小限に抑えるために名誉の痛みを取っており&quot;、商用の対抗よりも高い標準のFirefoxのようなミッション駆動の非営利団体を保持するために&quot;不合理ではない&quot;と考えていると<a href="http://www.theguardian.com/technology/2014/may/14/firefox-closed-source-drm-video-browser-cory-doctorow">記事</a>でコメントした。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
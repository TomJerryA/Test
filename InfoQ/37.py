<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Connect 1.0とAtlassian VerifiedについてDave Meyer氏が語る</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/atlassian-connect-verified"><em>原文(投稿日：2014/03/27)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Atlassianが新しい製品<a href="http://blogs.atlassian.com/2014/03/introducing-atlassian-connect-1-0/">Atlassian Connect 1.0</a>を発表した。これはJIRA、Confluence、HipChatといった同社のアプリケーションのアドオンを開発するための製品であり、<a href="http://blogs.atlassian.com/2014/03/new-marketplace-atlassian-verified/">Atlassian Verified</a>という開発者向けの認定プログラムも提供する。</p> 
  <p>InfoQは<a href="https://www.atlassian.com">Atlassian</a>のプロダクトマーケティングスペシャリストであるDave Meyer氏に話を聞いた。</p> 
  <p><strong>InfoQ: Atlassian Connectについて教えてください。なぜこの製品が必要だったのでしょうか。</strong></p> 
  <blockquote> 
   <p>どんな開発者でも簡単にJIRAやConfluence OnDemand(SasS型の課題トラッキング、コラボレーションアプリケーション)のアドオンが作れるようにするために開発した製品がAtlassian Connectです。ホスト型のサービスが普及するに伴い、拡張性を確保するために開発プラットフォームを構築する必要が生まれました。Atlassian Connectを使うことで、JIRAやConfluenceのリッチなアドインは独立して動作し独立してスケールします。これによって全体のセキュリティや安定性が増します。</p> 
  </blockquote> 
  <p><strong>InfoQ: Atlassian Connectの機能を教えてください。どのように動作しますか。</strong></p> 
  <blockquote> 
   <p>Atlassian Connectを使えば、どのようなウェブアプリケーションでもJIRAやConfluenceのアドオンになり、エンドユーザにはシームレスな利用経験を提供できます。ウェブアプリケーションはアプリケーションを説明する記述子、必要なパーミッション、 そして利用する&quot;モジュール&quot;を提供します。モジュールはアプリケーション内でコンテンツをインサートしたい場所です。</p> 
   <p>ConnectのアドオンはREST APIやウェブホックのような標準的な技術を使ってAtlassianのアプリケーションと通信します。また、<a href="https://bitbucket.org/atlassian/atlassian-connect-express">node.js</a>や<a href="https://bitbucket.org/atlassian/atlassian-connect-play-java/overview">Play framework</a>のようなクライアントライブラリも提供して開発者が簡単に開発を始められるようにしています。</p> 
  </blockquote> 
  <p><strong>InfoQ: Atlassian Connect 1.0にさらなる機能を追加する計画はありますか。</strong></p> 
  <blockquote> 
   <p>はい。1.0のリリース後、私たちはAtlassian Connectが自分たちのサーバでJIRAやConfluenceを動かしている顧客でも利用できるようにしようとしています。また、JIRAやConfluenceの上で自分たちの製品を開発したいと思っている開発者も使えるようにしたいです。また、多くの機能改善も予定しています。JIRAやConfluenceやJIRS自体のREST APIも改善したいです。</p> 
  </blockquote> 
  <p><strong>InfoQ: Atlassian Connectはどの製品と連携できますか。</strong></p> 
  <blockquote> 
   <p>現時点では、JIRAとConfluence OnDemandです。HipChatのサポートは現在<a href="https://www.hipchat.com/docs/apiv2">ベータ</a>です。将来はBitbucket、Stash、Bambooのような開発ツールも含めてAtlassianのすべての製品と連携できるようにしたいです。</p> 
  </blockquote> 
  <p><strong>InfoQ: この製品の利点はなんでしょう。</strong></p> 
  <blockquote> 
   <p>Atlassian Connectを使えば、開発者は好きな技術を使ってJIRAとConfluence OnDemandのアドオンを開発できます。アドオンを開発しAtlassian Marketplaceで販売する開発者にとっては、新しいマーケットが開けることになります。さらに、JIRAとConfluence OnDemandのユーザはカスタムで開発したアドオンやAtlassian Marketplaceで購入したアドオンでインスタンスを拡張できます。<a href="https://marketplace.atlassian.com/plugins?marketingLabel=Built+with+Atlassian+Connect">15のサードパーティのアドオン</a>とともにリリースされました。現在、もっと多くのアドオンが開発中です。</p> 
  </blockquote> 
  <p><strong>InfoQ: この製品のエンドユーザは誰になるのでしょうか。</strong></p> 
  <blockquote> 
   <p>Atlassian Connectは開発者がアドオンを作るための方法です。開発者はアドオンを作り、シェアし、Atlassian Marketplaceで販売できます。さらに、顧客は独自のアドオンを作ることができます。</p> 
  </blockquote> 
  <p><strong>InfoQ: Atlassian Verifiedについて教えてください。</strong></p> 
  <blockquote> 
   <p>Atlassian VerifiedプログラムはAtlassianの顧客が簡単に優れたアドインを見つけることができるようにする方法です。Marketplaceでアドオンを販売する開発者向けの認定プログラムで、牽引力、信頼性、サポートを満たす開発者を認定します。</p> 
   <p>Atlassianの以下の基準を定義しています。</p> 
   <ul> 
    <li><b>牽引力</b> – Atlassianの顧客のクリティカルマスに使われるアドインを作ること。</li> 
    <li><b>信頼性</b> – 開発者のルールに基づいてアップグレードすること。Atlassian Verifiedな開発者はAtlassianアプリケーションがリリースしてから2週間以内に互換性を保ちます。</li> 
    <li><b>サポート</b> – 開発者は公開されたSLAに従うこと。サポートウェブサイトを開設し、1週間のうち5日、1日最低でも8時間利用できるようにすること。</li> 
   </ul> 
   <p>Atlassian Marketplaceの認定を受けた開発者のプロフィールにはチェックマークがつきます。これは認定プログラムの要件を満たしているということを示しています。</p> 
  </blockquote> 
  <p><strong>InfoQ: 認定を受ける手続きはどのようなものでしょうか。どのような開発者が適格ですか。</strong></p> 
  <blockquote> 
   <p>Atlassian Verifiedの認定を受ける開発者は上述の基準を満たす必要があります。Atlassian Marketplaceでアドインを販売する開発者ならどんな開発者でもベンダアカウントを使って認定プログラムに申し込むことができます。認定のすべての要件は<a href="https://developer.atlassian.com/display/MARKET/The+Atlassian+Verified+program">ここで確認できます</a>。</p> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
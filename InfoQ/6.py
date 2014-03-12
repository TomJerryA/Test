<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Anypoint for APIs:Uri Saridへのインタビュー</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/anypoint-api-sarid"><em>原文(投稿日：2014/02/25)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>MuleSoftが<a href="http://mulesoft.com/platform/api">Anypoint platform for APIs</a>の重大なアップデートをリリースした。このプラットフォームはAPIの設計とAPIの管理機能を提供する。InfoQはMuleSoftのCTOである、Uri Sarid氏にこのプラットフォームについて話を聞いた。</p> 
  <p>
   <bold>
    <strong>InfoQ: Anypoint platform for APIsの新しいリリースは3つのコンポーネントで構成されています。API Portal、API Manager、Mule Studioの3つです。Mule Studioはすでによく知られています。あとのふたつのコンポーネント、API PortalとAPI Managerについて簡単に教えてください。</strong>
   </bold></p> 
  <blockquote>
   <strong>US:</strong>Anypoint API Portalは利害関係者や開発者と協力してAPIを設計し、APIのモックを作り、ドキュメントを作り、コンソールとノートブックを使って実装前と後でAPIを確認できます。開発者コミュニティもあります。また、Anypoint API Managerとも完全に統合しており、誰がAPIにアクセスできるか、利用制限の設定、利用され方の分析など完全に管理できます。
   <br /> 
  </blockquote> 
  <p>
   <bold>
    <strong>InfoQ: あなたは&quot;</strong>
    <a href="http://blog.programmableweb.com/2014/01/09/the-emergence-of-api-first-development/"><strong>設計ファースト</strong></a>
    <strong>&quot;な方法を推進していますね。APIの規約が第一で実装はそれに次ぐという考えです。API開発者向けにあなたの考えるワークフローやライフサイクルについて教えてください。</strong>
   </bold></p> 
  <blockquote>
   <strong>US:</strong> 他のプロダクトデザインと同じです。注意深いクラフトマンシップとユーザエクスペリエンスに対する注意が必要です。この場合、開発者がユーザですね。このふたつを大切にすることで、プロダクトを公開したときに、不釣り合いなくらいの利益が得られます。つまり、APIを公開したときです。まず、
   <a href="http://raml.org/">RAML</a> (the RESTful API Modeling Language)を使ってドメインにとって適切なAPIとその代表的なユースケースを描き、素早くテストユーザに引き渡します。このラフで最初期のステージでさえ、API向けのライブコンソールがあり、ユーザがプロトタイピングできるモックの&quot;実装&quot;があります。また、素早くシナリオの動作確認をして知見を共有するためのノートブックも使えます。設計が重要なのは、成功しているAPIの周りにあるエコシステムは独自の勢いを持っており、APIの破壊的変更に抵抗するからです。利害関係者が納得するまで設計を繰り返した後、実装に入ります。しっかりとした実装が開発者を明るくし、望ましい結果を生み出すという確信を持って実装を行いのです。多くの場合、APIの実装は、既存の無数のオンプレミスとクラウドのシステムを接続することです。Mule StudioとAPIkitコンポーネントを使うことでRAMLの仕様を、この仕様を満たし、スケーラブルでメンテナンス可能なMuleの統合フローに簡単に変換します。出来上がったMuleアプリケーションはCloudHubやオンプレミス(またはプライベートクラウド)へ配置できます。また、Muleアプリが公開するAPIは自動的にAnypoint API Managerに結びつけられ、ポリシーが適用できるようになり、Anypoint API Portalでは、開発者がAPIを見つけ、利用できるようになります。
   <br /> 
  </blockquote> 
  <p>
   <bold>
    <strong>InfoQ: <a href="http://www.infoq.com/news/2013/05/mulesoft-new-api-platform-mason">APIKitの最初のリリース</a>では、ドキュメントフォーマットとしてSwaggerが使われていました。今はRAMLを使っていますね。なぜ変更したのですか。APIドキュメンテーションについて何か学んだことはありますか。</strong>
   </bold></p> 
  <blockquote>
   <strong>US:</strong> 私たちは他のAPI開発者がしているのと同じことをしていることに気付きました。Swaggerや類似のフォーマットはAPIのフォーマットのアウトプットとしては適切なのですが、APIの設計を表すのは得意ではないということです。誰もSwaggerを書き始めることから始めません。コードから生成されるのです。さらに言えば、記述も冗漫で、簡単に木を見て森を見ずになってしまいます。大量の記述があるので、少量のきれいで再利用可能なパターンを見つけたり、組み込んだりできません。RAMLを使ったのは、きれいで、表現力と効率性があるRESTfulなAPIを設計するための方法としてです。
   <br /> 
  </blockquote> 
  <p>
   <bold>
    <strong>InfoQ: サービスレジストリは何か変更しましたか。</strong>
   </bold></p> 
  <blockquote>
   <strong>US:</strong> サービスレジストリは引き続き重要です。レジストリはすべてのサービスが登録されます。RESTもSOAP、FTPのような呼び出されないサービスもです。私たちはAPIに特化した機能を追加しています。新しいポリシーやAnypoint API Portalとの統合、機能のカスタマーシステムとの統合などです。
   <br /> 
  </blockquote> 
  <p>
   <bold>
    <strong>InfoQ: API ManagerはMuleを使っていないAPIでも使えますか。MuleとMuleでないAPIにはプラットフォーム上で何らかの差異があるのでしょうか。</strong>
   </bold></p> 
  <blockquote>
   <strong>US: </strong>Muleを使っていないAPIでもAnypoint API Managerで管理できます。APIゲートウェイでプロキシするのです。管理側からの視点でも、ポータル側からの視点からでも、すべての機能は実装がMuleでされているのと同じように扱うことができます。
   <br /> 
  </blockquote> 
  <p>
   <bold>
    <strong>InfoQ: プロバイダとしてそして利用者として、APIに残された最大の難点とは何だと思いますか。</strong>
   </bold></p> 
  <blockquote>
   <strong>US: </strong>APIの黄金期のように思えますが、まだまだ成長の余地はあります。多くの企業はまだAPIについての動きを始めていません。APIの設計の重要性はちょうど今認識され始めたところです。ベストプラクティスはほとんどなく、道のりも遠いです。同じ組織の内部であっても一貫性のないAPIがあります。APIがある組織とない組織で巨大なギャップがあるのです。そしてこれは、APIの利用者が直接感じていることでもあります。たいていの利用者はAPIの利用で難儀しています。後付けで作られているように感じるのです。そして実際そのように作られているのです。
   <br /> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
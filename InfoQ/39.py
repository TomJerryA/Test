<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>RESTの代替は必要か</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/rest-alternatives"><em>原文(投稿日：2013/12/29)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>SoapUIの開発者であるOle Lensmar氏が最近、<a href="http://blog.programmableweb.com/2013/12/19/is-rest-losing-its-flair-rest-api-alternatives-2/">RESTは&quot;利点を失いつつあるのではないか&quot;</a>、RESTの代替が必要なのではないか、という問いを投げかけている。</p> 
  <blockquote>
   公開APIを構築するための有力な方式としてのRESTはほかのAPI技術を見劣りさせています。企業向けのシステムでは、ほかの方法(主にSOAP)も未だに使われていますが、RESTのアーリーアダプターはほかのAPI方式に対しては断固受け入れないスタンスを取り、RESTを採用してフォーマットにはJSONを使います。
  </blockquote> 
  <p>氏はSOAPやXML-RPCのようなほかの方式ではなくて、RESTが成功した理由を説明している。しかし、氏はRESTが利用しにくい領域も多くあり、そのような領域ではほかの方法が必要だと考えている。</p> 
  <ul> 
   <li>非同期API: &quot;従来のリクエスト/レスポンスではなく、データを非同期で押し出さなければならない場合、RESTfulな設計はうまく適用できません。さらに、基盤技術(WebSockets, MQTT, AMQP, Stomp, pubsubhubbub/WebHooksなど)はHTTPとはまったく異なるので、RESTの原則とは普通、相容れません。&quot;</li> 
   <li>オーケストレーションAPI: &quot;従来のREST APIが提供するリソースの粒度には利点はない。要求されたリソースをモバイルのダッシュボードや複雑なシングルページウェブアプリケーションから取得するには多くのAPIリクエストが必要。この場合、クライアントのロジック、帯域、サーバ処理にオーバヘッドが発生します。&quot;</li> 
   <li>SDK vs API: &quot;ほとんどのAPIの利用者はハイレベルな言語から利用します。したがって、各言語向けのクライアントライブラリを含む多くのAPIプロバイダが生まれます(Google、Facebookなど)。言語自体がRPC指向なので、SDKが提供するコードレベルのAPIも同様RPC指向になってしまいます。すると、おそらくは、最適化されたバイナリプロトコルを利用して、あるいは、RPCライクにHTTPリソースを使うことで(例えばJSON-RPC)、バックエンドのAPIも同様の動作をするように作ってしまいます。&quot;</li> 
   <li>バイナリプロトコル: &quot;[...] 例えばIoTデバイスやSDKからのリクエストに対応するために最適化されたメッセージ転送を行うため、バイナリプロトコルはより注目を集め、利用されるようになっています。&quot; Apache Thrift, Google Protocol Buffers, Apache Avroなどのプロトコルだ。&quot;上述した非同期APIのいくつかはバイナリフォーマットを利用しています。デバイスやサービスによって背負わされた帯域や処理の制限に対応するためです。&quot;</li> 
  </ul> 
  <p>氏はリアルタイムの要件のため、プロトコルとしてThriftを利用しているEvernoteを例示する。氏は、Daniel Jacobson氏の<a href="http://blog.programmableweb.com/2013/10/03/is-evernotes-restless-api-approach-a-model-for-other-api-designs/">EvernoteのRESTlessな設計</a>についての記事に言及している。</p> 
  <blockquote>
   [...] REST APIは不特定多数の開発者を相手にする場合は優れた方法だと思います。しかし、利用者が特定のユーザや市場、産業や技術だけに限定されている場合、もっと具体的な解決策を選択するのは合理的なやり方です。性能や使いやすさ、セキュリティの面で競合より優位に立てるかもしれません。
  </blockquote> 
  <p>氏は、とりわけAPIの設計では、ひとつの側面がすべてに適用できることはないということを認める。&quot;私たちのような情熱的な技術者にとって幸運なのは、新しいことを学び、それをすべての利害関係者にとって最適なかたちで利用することで、私たちの世界はよりしっかりする(すくなくとも私の世界は)ということです。私はこのような多様性のある環境を否定しません。大歓迎です。&quot;</p> 
  <p>コメント欄では氏に賛成するコメントもある一方、賛成しないコメントも多い。例えば、John Sheehan氏は、</p> 
  <blockquote>
   私はEvernoteはRESTを捨てたとは思いません。最初から使っていなかったのではないでしょうか。使っていなかったのにもしっかりとした理由があると思います。Webhooksはとても‘REST’っぽい(最低でも一般的な理解では)です。非同期についての解説であなたが挙げた一覧はほとんどの一般的な実装には適用できません。
  </blockquote> 
  <p>Darrel Miller氏はRESTと&quot;ポピュラーなREST&quot;の違いを示そうとしている。</p> 
  <blockquote>
   私がDaniel Jacobson氏のオーケストレーションレイヤから言えることは、長い間、私がRESTfulな(そしてハイパーメディア駆動)APIを構築する上で利用してきた方法にとても近い、ということです。人々が“ポピュラーなREST”の誇大広告はFieldingのRESTの特性を何も変えていないことに気付き始めているからです。
  </blockquote> 
  <p>多くのコメントがOle氏が真のRESTfulな原則とRESTfulと言われているが実際はそうでない実装を区別していない、と指摘している。あなたはどう思うか。すべての領域でRESTは利用できるのだろうか。あなたのおすすめを教えてください。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>HTTPを強化する</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/strengthen-http"><em>原文(投稿日：2014/01/05)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>以前、<a href="http://www.infoq.com/jp/news/2012/06/spdy-websockets">HTTPbis Working Group</a>で行われている<a href="http://www.infoq.com/jp/news/2012/12/http20-first-draft">HTTP 2.0</a>の策定作業についてレポートしたが、最近、Working Group議長のMark Nottingham氏がそのプロトコルのセキュリティ要件に関するグループの取り組みについて、<a href="http://www.mnot.net/blog/2014/01/04/strengthening_http_a_personal_view">個人的見解</a>を投稿した。</p> 
  <blockquote>
   最近、インターネットプロトコル界隈で一番ホットな話題のひとつは、
   <a href="http://www.theguardian.com/world/edward-snowden">Edward Snowden</a>氏によって世界に知れ渡ったpervasive monitoring攻撃に対して、Webのプロトコル、
   <a href="http://http2.github.io/">HTTP/2</a>の最新バージョンが暗号化使用について
   <em>何か</em>を要求したり、推奨したり、言及するかどうかです。
  </blockquote> 
  <p>Mark氏はこれまでの簡単な経緯について、特に、SPDYとセキュリティに関して次のように述べた。</p> 
  <blockquote>
   Mike (Belshe)氏とRoberto (Peon)氏がSPDYを我々のところへ持ってきたとき（「Snowden氏」がその名を知られるずっと前のこと）、すでにSPDYの実装は暗号化に
   <a href="http://en.wikipedia.org/wiki/Transport_Layer_Security">TLS</a>を使うことを必須としていました。これは実用的な理由（中間にいるものがそれを知っていないと、HTTPの新バージョンを導入するのは本当に難しい）と高尚な理由のためでした。
  </blockquote> 
  <p>セキュリティを必要としない場合のユースケースのため、また、それを必須とすることには異論があるため ...</p> 
  <blockquote>
   [...] 
   <a href="http://http2.github.io/http2-spec/">仕様</a>も
   <a href="http://datatracker.ietf.org/wg/httpbis/charter/">我々の憲章</a>も、暗号化および非暗号化コネクション上でHTTP/2を使えるという暗黙の了解という問題について何も言及しておらず、実装が何をサポートすべきかを決めていました。
  </blockquote> 
  <p>Snowden氏の登場と<a href="http://www.theguardian.com/world/2013/jul/31/nsa-top-secret-program-online-data">XKeyscore</a>の暴露により、IETFでは大きな方針転換があった。BerlinのWorking Groupミーティングでは<a href="http://www.ietf.org/proceedings/87/slides/slides-87-httpbis-3.pdf">臨時セッション</a>が開かれ、「もっと暗号化を使うことでHTTPのセキュリティを改善する」という強いコンセンサスが生まれた。IETFではその後もさらに議論が重ねられた。</p> 
  <blockquote>
   TLSをもっと使うこと（それにより、pervasive monitoringなどの攻撃に対して防御すること）が共通のゴールだということは非常にはっきりしていましたが、そのための手段はいろいろとあって、このゴールをどのように実現するのが最善か、何が適切なトレードオフなのかについて、多くの議論と反対が繰り返されました。
  </blockquote> 
  <p>Mark氏は、ChromeとFirefoxの開発者からは、TLSによって保護される場合に限りHTTP/2をサポートするという強力な支持があることを語った。彼の考えが前進するための最善の方法であることを説明するため、他のブラウザ開発者やセキュリティ専門家とも話した。</p> 
  <blockquote>
   [...] 通常のWebブラウジングのケースにおいて、ブラウザとの幅広い相互運用を求めるなら、HTTP/2サーバはTLSを使用する必要があります。— Mike氏とRoberto氏がSPDYでやったのと同じようにです。でも重要なことは、必ずしもプロトコル仕様自体がTLSの使用を要求する必要はないということです。
  </blockquote> 
  <p>Mark氏は自分の提案の背景、もっとセキュリティを必要としているグループもあれば、HTTP/2の使用すべてに暗号化を必須とするのはIETFにふさわしくないと考えている人たちもいることについて話を続ける。こうした状況では、IETFが決定に至るのは難しい。特に、こうした問題には、Mark氏の言葉で言うところの「政治」がつきものだ。</p> 
  <blockquote>
   政治的な判断というのは、政府を攻撃者と疑っているからではなく、HTTPがプロキシベンダー、ネットワークオペレータ、企業のファイアウォールなど、たくさんの既存のステークホルダで使われているプロトコルだからです。HTTP/2で暗号化を必須とするということは、これらのステークホルダの権利が奪われるということです。
  </blockquote> 
  <p>しかしながら、IETFとWorking GroupがHTTP/2プロトコルに柔軟性と明確さがあることを保証することで、さまざまな選択肢のメリット、デメリットについて必要な議論を促すことができると考えている。</p> 
  <blockquote>
   たとえば、現在のHTTPの設計では、暗号化を使うかどうかの判断は、完全にサーバ任せです。ユーザがやれるのは、URLが“HTTP”か“HTTPS”かを見て（あるいは鍵のアイコンを見て）、続行するかどうかを決めることだけです。もっと調和のとれたWebとは、クライアントもこの決定に入力を与えられることでしょう、サーバが暗号化をサポートするよう人参をぶらさげて — FirefoxとChromeがやっているように、暗号化されたときだけHTTP/2をサポートするなど。
  </blockquote> 
  <p>この場合、判断は標準ではなく、むしろブラウザベンダーによってなされることになる。次は何か？ 別のHTTPbis Working Groupミーティングが<a href="https://github.com/http2/wg_materials/blob/master/interim-14-01/arrangements.md">Zurich</a>で開かれ、Mark氏は<a href="https://github.com/http2/http2-spec/issues/314">重要な問題</a>を解決する提案を求めている。</p> 
  <blockquote>
   多くのブラウザ実装者は、「オープン」なインターネット上のトラフィックのため、HTTP/2 over TLSだけを実装すると意思表明しています。彼らはhttps:// URIのためだけにHTTP/2を実装することによって、それを実現することができます。新しいプロトコルを使いたいサイトは、http:// URIをリダイレクトする、できればそのアップグレードにHSTSを使う必要があります。これもまた、必ずしも要求として（つまり、MUSTやMUST NOTを使って）仕様化する必要はありません。こうしたブラウザで新しいプロトコルを使いたいサイトは、先ほどのパターンを実装することになるでしょう。ただし、相互運用を促進するため、ガイドラインや骨組みとなる要件が必要になるかもしれません。このissueは具体的な提案を集めるためです。
  </blockquote> 
  <p>つまり、HTTP/2標準がTLSを必須としなくても、ブラウザ実装がTLSを必須とするかもしれないということだ。だがMark氏が指摘するように、後からHTTP/2でTLSを必須にするブラウザ実装は、企業のプロキシがトラフィックなどを調べられるようにという圧力を感じるかもしれない。もしそうなったときには、標準の相互運用性を保った協調のとれたやり方で扱われることが重要だ。最後にMark氏は、決定はまだなされておらず、別の結果になる時間が残されていることを覚えておくよう述べている。そして、Working Groupは常にこの議論に関する<a href="http://lists.w3.org/Archives/Public/ietf-http-wg/">他人からの意見を聞くこと</a>に関心を持っている。最終的にIETF Working Groupでなされる決定は、今後多くの人に影響を与えることになるだろう。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
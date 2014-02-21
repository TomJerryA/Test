<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>WildFly 8についてJason Greene氏へのインタビュー</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/wildfly8-interview"><em>原文(投稿日：2014/02/12)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Red HatのJBoss部門はWildFly 8を発表した。WildFly 8は以前はJBoss Application Serverという名で知られていた製品であり、InfoQでも以前<a href="http://www.infoq.com/news/2014/02/wildfly8-launch">取り上げている</a>。InfoQはWildFlyのリードを努めた、Red HatのJBoss部門のJBoss EAP Platform ArchitectであるJason Greene氏にこの新しい製品について話を聞いた。WildFlyには新しいウェブサーバが含まれており(Undertow)、私たちはGreene氏にどうしてこの大きな決定を下したのか話を聞いた。</p> 
  <blockquote> 
   <p>この数年でウェブアプリケーションが劇的に進化し、ウェブサーバに対してこれまでにないくらい多くの要求を突きつけています。コンピューティングをするデバイスの増加によって、ウェブアプリケーションのクライアントは増加し、リッチなインターフェイスに対する欲求はより頻繁にデータ指向のトラフィックを増やしています。WebSocketのような2重通信はすでに一般的になっています。私たちは、0から設計された高性能なサーバが最適なソリューションだと感じていました。</p> 
   <p>現在のウェブアプリケーションのニーズを踏まえ、さらに、インフラ起因の問題にも対処したいと思っていました。このような問題は普通、代替のネイティブなサーバで解決するものです。例えば、Undertow WildFlyは効率的でノンブロッキングのリバースプロキシとしてApacheやNginxなしで動作します。</p> 
   <p>もうひとつはクラウド環境のポートの数を減らしたいという考えがありました。クラウドでは同じシステム上で数千のWildFlyが動作する可能性があります。Undertowを使えば、HTTP Upgradeを使ってHTTP上で動作するさまざまなプロトコルを多重化します。</p> 
   <p>また、Servletよりも開発者になじみやすい仕組みを構築することができます。依存関係がすくない軽量なメモリフットプリントを持ち、組み込み可能で、リアクティブなノンブロッキングスタイルと従来のブロッキングストリーム思考の方法の両方をサポートするAPIを使えます。</p> 
  </blockquote> 
  <p><strong>InfoQ</strong>: WildFly 8のログ監査機能について詳しく教えてください。</p> 
  <blockquote> 
   <p>WildFlyのログ監査はEAP 6.2に導入された機能のためです。RBACを有効にしている場合、AuditorロールかSuperUserロールだけが監査ログの構成を変更できます。管理モデルに対するどのような操作もログに記録されます。CLIのタブコンプレイションのような操作は多数の読み取り処理をするので、モデルの状態を変化させる処理だけをログ出力するようにできます。また、MBeanServerやコントローラーでJMXを使って管理モデルに処理がされたときもJMXアクセスのログを記録します。</p> 
   <p>また、ローカルのファイルやsyslogサーバへのログ出力もサポートしています。syslogサーバはローカルでもリモートでもかまいません。UDPやTCPプロトコルを使ってロギングできます。TLSもサポートされています。syslogのレコードを出力できるフォーマットはJSONだけですが、これは、コミュニティや顧客の要求に応じて簡単に出力フィールドを増やせるようにするためです。しかし、将来ほかの出力フォーマットを追加する可能性はあります。</p> 
   <p>ログに含まれているのは下記の情報です。<br /> -管理モデルを変更した操作<br /> -サーバ起動完了後に実施された処理<br /> -認証ユーザ名<br /> -処理が行われたインターフェイス。例えば、ウェブインターフェイス、JMXインターフェイス、ネイティブインターフェイスなど<br /> -呼び出し元のアドレス<br /> -処理が成功したかどうか<br /> -処理そのもの<br /> -ドメインモードの場合、処理を追跡するためのUUID。UUIDはドメインコントローラからホストコントローラ、そしてマネージドサーバへと受け継がれる。</p> 
   <p>次はレコードの例です。<br /> - - - - - - - - - - ----</p> 
   <pre>
  2014-01-23 10:30:16 - {
   &quot;type&quot; : &quot;core”,                      
   &quot;r/o&quot; : false,
   &quot;booting&quot; : false,
   &quot;version&quot; : &quot;8.0.0.Final-SNAPSHOT&quot;,
   &quot;user&quot; : &quot;$local&quot;,
   &quot;domainUUID&quot; : null,
   &quot;access&quot; : &quot;NATIVE&quot;,
   &quot;remote-address&quot; : &quot;127.0.0.1/127.0.0.1&quot;,
   &quot;success&quot; : true,
   &quot;ops&quot; : [{
       &quot;address&quot; : [{
           &quot;system-property&quot; : &quot;xxx&quot;
       }],
       &quot;operation&quot; : &quot;remove&quot;,
       &quot;operation-headers&quot; : {
           &quot;caller-type&quot; : &quot;user&quot;,
           &quot;access-mechanism&quot; : &quot;NATIVE&quot;
       }
   }]
}
</pre> 
  </blockquote> 
  <p><strong>InfoQ</strong>: パッチングシステムについて教えてください。実行中のシステムにパッチを当てることができるのでしょうか。</p> 
  <blockquote> 
   <p>パッチングの機能は第一にJBoss EAPのユーザのために作りました。しかし、私たちのオープンソースモデルの主要な方針は、企業向けに開発した主要な機能はすべて再活用するということです。したがって、この機能もJBoss EAP 6.2とWildFly 8の両方に搭載されています。新しい管理用の操作が含まれており、&quot;patch&quot;と呼ばれる新しいコマンドがCLIに追加されています。このコマンドを使うと、JBossのパッチをひとつのサーバに適用できます。リモートのサーバでもローカルのサーバでも適用できます。動いているシステムでも可能です。しかし、パッチを有効にするには再起動が必要です。パッチに問題があれば、ロールバックもできます。システムがすべてのパッチ履歴を保存しており、どの時点にも戻れるのです。内部がどうなっているか気になる方に説明すると、パッチインフラはWildFly内のモジュールクラス上に構築されており、パッチを適用するということはモジュールディレクトリを追加して、最初にインストールされたものを拡張したり置き換えたりすることなのです。</p> 
   <p>将来、この仕組みの上に新しい機能をリリースするつもりです。パッチを適用するのに使えるウィザードなどですね。</p> 
  </blockquote> 
  <p><strong>InfoQ</strong>: LDAPディレクトリはRBACのクレデンシャルを保持できますか。</p> 
  <blockquote> 
   <p>はい。私たちのLDAPサポートは柔軟でフィルタを調整して利用しているディレクトリプロバイダのスキーマにあわせられます。したがって、Active Directoryを含むどのようなLDAPサーバとも互換性があります。例えば、Active　Directoryならusername-フィルタをsAMAccountNameへ向ければいいのです。</p> 
  </blockquote> 
  <p><strong>InfoQ</strong>: ブランドの変更とは別に、JBoss EAPと比べてWildFlyのアプローチはどのような点が違いますか。EAPのほうがより保守的なのでしょうか。</p> 
  <blockquote> 
   <p>WildFlyは、頻繁に最新の技術を提供していくことにフォーカスしています。1年に一度はメジャーなリリースをするつもりですし、各リリースの間にもマイルストンを置くつもりです。WildFlyは開発者とユーザがともに助け合い、コードを共有していくというコミュニティサポートモデルを持っています。しかし、焦点と興味は常に今行われていることにあります。</p> 
   <p>EAPはもっと保守的です。7年から10年にわたってパッチでメンテナンスされているブランチに注力しています。これらのブランチに対する機能の更新はよりゆっくりと行われています(私たちは上位のツリーから古いリリースへ、互換性に注意しながら機能を移植しています)。EAPはサブスクリプションの一部として配布されること以上に多くの利点があります。ベンダ認定やコンプライアンス、広いナレッジベース、保証されたSLAなどです。</p> 
  </blockquote> 
  <p><strong>InfoQ</strong>: JBoss EAPのJava EE 7バージョンはいつ頃登場するのでしょうか。</p> 
  <blockquote> 
   <p>特定の日にちは言えませんが、次のメジャーリリースはJava EE 7をサポートする予定です。WildFly 8(と将来のWildFlyのリリース)も含まれます。</p> 
  </blockquote> 
  <p><strong>InfoQ</strong>: OracleがGlassFishの商用サポートをやめることはJBoss EAPにとってどの程度影響があると思いますか。</p> 
  <blockquote> 
   <p>どうなるか予想したいと思いませんが、GlassFishからWildFlyとEAPへ乗り換えることに対して次第に興味が高まっていることを感じています。アプリケーションサーバの選択にはさまざまな要因がありますが、私たちはオープンソースであることへのコミットメントとコミュニティが重要だと思っています。Red HatではこのふたつがDNAの一部なのです。すべてのコードをオープンソースにしています。</p> 
  </blockquote> 
  <p>さらに詳しい情報は、<a href="http://wildfly.org">WildFlyのウェブサイト</a>で確認できる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Red HatのJBossチームがWild Fly 8をローンチ - Java EE 7をフルサポート，組み込み可能な新Webサーバを装備</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/wildfly8-launch"><em>原文(投稿日：2014/02/12)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Red HatのJBoss部門は本日，<a href="http://wildfly.org">WildFly 8</a>の提供開始を<a href="http://wildfly.org/news/2014/02/11/WildFly8-Final-Released/">発表した</a>。これまではJBoss Application Server(JAS)という名称だったプロダクトだ。今回のリリースではJava EE7認定を取得し，Web ProfileとFull Profileの両方をサポートする。さらに，まったく新しいWebサーバであるUndertow，新たなセキュリティ機能，実行中のシステムを更新可能なパッチシステムを備えている。</p> 
  <p>UndertowはServlet 3.1コンテナであり，HTTP管理インターフェースのサーバでもある。新しいコンテナはHTTP/1.1 RFCの一部である<a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.42">HTTP Upgrade</a>をサポートしており，HTTP接続を他のプロトコルにアップグレードすることができる。そのもっとも一般的な用途は，Webソケット接続における，ブラウザなどクライアントによる全二重接続の確立だ。</p> 
  <p>HTTP Upgradeでは単一のHTTPポート上に複数のプロトコルを多重化することができるため，複数のポートを使用する必要がなくなり，ファイアウォールの設定が簡略化できる。WildFlyそれ自体，わずか２つのポートしか使用しない。JNDIとEJBコールはUndertowサブシステムの8080ポート上に，管理プロトコルはWeb管理ポート(9090)上に，それぞれ多重化されている。</p> 
  <p>一例として，接続確立後の最初のEJB要求は，通信の上では次のようなものになる。</p> 
  <pre>
GET / HTTP/1.1<br />Host: example.com<br />Upgrade: jboss-remoting<br />Connection: Upgrade<br />Sec-JbossRemoting-Key: dGhlIHNhbXBsZSBub25jZQ==</pre> 
  <p>これに対してUndertowは，アップグレード可能であることをクライアントに応答する。</p> 
  <pre>
HTTP/1.1 101 Switching Protocols<br />Upgrade: jboss-remoting<br />Connection: Upgrade<br />Sec-JbossRemoting-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=</pre> 
  <p>その後はWildFly EJBレイヤにソケットが渡されて，通常のEJB接続として動作する。</p> 
  <p>最初のHTTP要求にわずかなオーバーヘッドがあるものの，接続してしまえばパフォーマンスは完全に同等のはずだ。必要なポート数が確実に少なくなる分，全体として見ればメリットがあることを期待できる。Red Hat JBoss部門でJBoss EAPプラットフォームアーキテクトを務めるWildFlyリーダのJason Greene氏は，InfoQに次のように語っている。</p> 
  <blockquote> 
   <p>HTTP要求を処理する必要があるので，接続確立時にさらにオーバヘッドがいくらか発生しますが，Undertowの効率性によって非常に低く抑えられています。アップグレード要求後は，HTTPを使用しない場合と完全に同じ動作をしますので，その意味から見たパフォーマンスについてはまったく同じです。インパクトが極めて小さいので，私たちはこれをデフォルト設定にしました。 初期設定のWildFly 8はわずか２つのHTTPポートしか使用しません。ひとつは管理用，もうひとつはアプリケーション用です。その他のプロトコルはすべて，これらのポートを再利用しています。</p> 
  </blockquote> 
  <p>Undertowは組み込みモードでも使用可能なように設計されている。構築したサーバにHTTPハンドラを登録して，要求を非ブロック方式で処理するためのチェーン構成APIが用意されているのだ。<a href="http://undertow.io">undertow.io</a>Webサイトでの使用例を挙げる。</p> 
  <pre>
public class HelloWorldServer {

    public static void main(final String[] args) {
        Undertow server = Undertow.builder()
                .addListener(8080, &quot;localhost&quot;)
                .setHandler(new HttpHandler() {
                    @Override
                    public void handleRequest(final HttpServerExchange exchange) throws Exception {
                        exchange.getResponseHeaders().put(Headers.CONTENT_TYPE, &quot;text/plain&quot;);
                        exchange.getResponseSender().send(&quot;Hello World&quot;);
                    }
                }).build();
        server.start();
    }
}
</pre> 
  <p>Undertowでは，Servlet APIに基づいてコードを組み込むこともできる。これについては，いくつかの例が<a href="https://github.com/undertow-io/undertow/blob/master/examples/src/main/java/io/undertow/examples/servlet/ServletServer.java">GitHub</a>にある。</p> 
  <p>新しいWebサーバだけでなく，WildFly 8は監査ログやロールベースのセキュリティモデルの導入によって，セキュリティ面でも著しく向上している。</p> 
  <p>監査システムは，管理モデルに対するどのような操作であっても，ローカルファイルまたはサーバ上のログに確実に記録されるように設計されている。</p> 
  <p>WildFlyは２タイプのアクセス管理プロバイダを添付して提供される。&quot;シンプル&quot;タイプはAS 7と同等で完全にオール・オア・ナッシング形式のものだが，RBAC(Role Based Access Control)タイプは管理者それぞれに権限を設定可能だ(監視用ロール，更新ロール，といったように)。</p> 
  <p>WildFlyには７つのロールがあらかじめ定義されている。</p> 
  <ol> 
   <li><strong>モニタ</strong>: 最小限の権限を持つ。 コンフィギュレーションと現在のランタイム情報を参照できるが，機密性の高いリソースとデータ，監査ログおよび関連リソースにはアクセスできない。</li> 
   <li><strong>オペレータ</strong>: 監視ロールのすべての権限に加えて，実行状態の変更 – サーバのリロードあるいはシャットダウン，JMSデスティネーションの一時停止と再開が可能。ただし永続的なコンフィギュレーションを変更することはできない。</li> 
   <li><strong>メンテナ</strong>: オペレーターロールのすべての権限。 永続的なコンフィギュレーションの変更，すなわちアプリケーションのデプロイや，JMSデスティネーションの追加といった操作が可能。このロールでは，サーバとデプロイメントに関する，ほとんどすべてのコンフィギュレーションを変更することができる。ただし機密性の高い情報(パスワードなど)の参照や変更，監査情報の参照や変更を行うことはできない。</li> 
   <li><strong>デプロイヤ</strong>:&nbsp;メンテナとほとんど同じだが，対象がデプロイに関する修正に制限されている。その他の一般的な設定を変更することはできない。</li> 
   <li><strong>管理者</strong>:&nbsp;パスワードやセキュリティ関連の設定といった，機密性の高い情報の参照と変更が可能。ただし監査ログに関する操作はできない。</li> 
   <li><strong>監査人</strong>:&nbsp;モニタロールのすべての権限を持つ。基本的には読み取りのみのロールだが，監査ログシステムに関する設定は修正も可能。</li> 
   <li><strong>スーパーユーザ</strong>:&nbsp;AS 7のアドミニストレータと同じく，すべての権限を所有する。</li> 
  </ol> 
  <p>RBACデータはActive Directoryを含む，ほとんどすべてのLDAPサーバに保存することができる。</p> 
  <p>WildFlyには新しいパッチシステムも含まれている。これは当初，JBoss EAPのために開発されたもので，JBossの用意したパッチをリモートあるいはローカルで適用することができる。実行中のシステムに対するパッチ適用も可能だが，それを有効にするには再起動が必要になる。</p> 
  <p>最後に，WildFlyはおもにJava EEのサポートにフォーカスしているが，その他の言語や環境用にも使用することができる。例えば<a href="http://torquebox.org">TorqueBox</a>プロジェクトでは，サーバ上でRuby on Railsを稼働させることが可能だ。</p> 
  <p>詳細は<a href="http://wildfly.org">WildFlyのwebサイト</a>あるいは<a href="http://wildfly.org/news/2013/11/21/WildFly-8-Webinar/">webiner記録</a>で見ることができる。InfoQではJason Greene氏に<a href="http://www.infoq.com/jp/news/2014/02/wildfly8-interview">さらに広範な話題でのインタビュー</a>も行っている。そこではさまざまな話題と合わせて，新しい監査ログシステムであるUndertowの背景や，GlassFishの<a href="http://www.infoq.com/jp/news/2013/11/glassfish-commercial-dead/">商用サポートを廃止する</a>という，Oracleの決定が持つ影響についても取り上げている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
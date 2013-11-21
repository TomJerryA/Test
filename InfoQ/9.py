<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Apigee、Node.jsをサポートしVolosをオープンソース化</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/apigee-nodejs-volos"><em>原文(投稿日：2013/11/12)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Apigee EdgeがNode.jsをサポートし、API管理モジュールを含むプロジェクト、<a href="https://github.com/apigee/volos">Volos</a>をオープンソース化した。</p> 
  <p>Apigeeは最近、新規API、モバイルアプリケーション向けバックエンド、マッシュアップ、複合サービスの構築に使うことができる<a href="https://blog.apigee.com/detail/nodejs_extending_the_programmability_of_the_apigee_api_platform">Node.jsとNPMモジュールのサポートを追加した</a>。私たちはApigeeのチーフアーキテクトであるGreg Brail氏にインタビューし、開発者はNode.jsを使って、Apigeeプラットフォームで何ができるのか話を聞いた。</p> 
  <p><strong>InfoQ: Edgeプラットフォームに対してプログラミングするとき、JavaScript/Node.jsを使って何ができるのですか？</strong></p> 
  <blockquote> 
   <p><strong>GB: </strong>具体的に言うと、あなたはすぐにでも、Node.jsでWebアプリを書いて（標準の &quot;http&quot; と &quot;https&quot; モジュールを使って）、それをクラウドもしくは自分のデータセンタにあるApigee Edgeにデプロイできます。デプロイするアプリはNode.jsのフル環境にアクセスできます。NPMにホストされた大量のモジュールを使うこともできます。（私たちの環境はまだ互換性の欠けているところがあります。たとえば、CやC++ネイティブコードに依存するモジュールをサポートしていません）</p> 
   <p>既存のAPIプロキシと同様、スクリプトはEdge内で実行されるので、Edgeの各種デプロイメント機能をサポートしています。同じUIやAPIから異なる仮想環境に異なるバージョンをデプロイする機能や、地理的に複数のリージョンに自動的にデプロイする機能も含まれます。私たちはEdge経由でNode.jsプログラムに渡されるすべてのAPI呼び出しの分析結果を収集しており、トラフィック分析やカスタムデータによるカスタム分析も可能です。</p> 
   <p>さらには、Node.jsスクリプトを既存のポリシーライブラリと組合わせることもできます。たとえば、セキュリティポリシー（OAuthなど）、トラフィック管理（クォータやスパイク停止など）、セキュリティ脅威検出などです。</p> 
  </blockquote> 
  <p><strong>InfoQ: Objective-C、Java、.NET、Ruby、JavaScriptなど、たくさんのSDKもサポートしていますね。これらは、EdgeプラットフォームにNode.jsを使ってやれることと同じことをするのに使えるのですか？ 何か違いはあるのでしょうか？</strong></p> 
  <blockquote> 
   <p><strong>GB: </strong>Edgeプラットフォームには、独自の設定スキーマを使って定義されたAPIプロキシを実行できるランタイムが含まれていますが、そこにNode.jsを使って構築されたHTTPサーバを実行できるランタイムが含まれたということです。一方、SDKというのは、顧客が直接使えるようにEdgeが提供している各種APIのためのクライアントです。たとえば、SDKを使うことで、各種モバイルプラットフォーム向けアプリや、データストレージやプッシュ通知のようなバックエンドとしてEdgeを使うものが作れます。</p> 
   <p>これに対して、Edgeはサーバです。Node.js機能というのは、コードをサーバにデプロイする新しい手段です。サーバには最近のアプリにとって重要な機能を提供するために用意されたAPI一式も含まれます。SDKというのは、そうしたAPIにクライアントが簡単にアクセスするための手段なのです。</p> 
  </blockquote> 
  <p>また、Apigeeは<a href="https://github.com/apigee/volos">Volos</a>をオープンソース化した。これはNode.jsモジュール一式で、API OAuth 2.0認証、鍵の検証、クォータ管理、キャッシングをサポートする。Volosは独立して実行することもできるし、<a href="http://apigee.com/about/products/edge">Apigee Edge</a>とやりとりするようセットアップして、開発者、アプリ、APIの管理サポートを得ることもできる。また、VolosアプリをApigeeプラットフォームに直接デプロイすることもできる。</p> 
  <p>VolosとEdgeについて、Brail氏はこう語った。</p> 
  <blockquote> 
   <p>Volosが作られた理由の1つは、数々のEdgeの機能を活用することです。たとえば、VolosのOAuthとクォータモジュールはRedisデータベースに対してローカルに実行することもできますし、Edgeとやりとりすることもできます。そうすることでOAuth機能を使うということです。もちろん、VolosアプリをデプロイしてEdgeで動かせば、そうした機能を直接使うことができます。必ずしも二者択一ではないのです。</p> 
   <p>そうは言っても、Edgeは最新の管理機能をいろいろ備えています。開発者、アプリ、それらの集合の管理から、分散クォータやディープアナリティックスなど手の込んだものまで。</p> 
  </blockquote> 
  <p>Volosの今後について、Brail氏はApigeeのプランをこう付け加えた。</p> 
  <blockquote> 
   <p>私たちはVolosにさらなるモジュールを追加して、Node.jsにおけるプロダクション品質のAPI構築のための最高のツールセットにするつもりです。そして、もちろん、Edgeがそうしたアプリを動かすための最適な場になるよう、Edgeで実行するとEdgeプロダクトの全機能と有用性を活用できるようにしていきます。</p> 
  </blockquote> 
  <p>いろいろある中、Apigeeは新規あるいは既存のバックエンドやデータサービスと、クライアントとの間に介在するAPIの構築と管理をサポートしている。</p> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
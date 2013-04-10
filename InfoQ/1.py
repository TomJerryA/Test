<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Google+ Sign-In：連合アイデンティティ、認証、セマンティック アクティビティストリーム</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/google-plus-federated-identity;jsessionid=DC838EB3646E4698CDA4FA34E9E31F28"><em>原文(投稿日：2013/04/04)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://googleplusplatform.blogspot.com.au/2013/02/google-plus-sign-in.html">Google+ Sign-In</a>は、Google+ のソーシャルネットワークを拡張して、サードパーティのWebサイト、デスクトップアプリケーションやモバイルアプリケーションまで入り込み、さらにIDプロバイダとしてのGoogleの位置をTwitterやFacebookなど、他のもの並に強固する。2月26日に発表した新サービスでは、認証、認可、活動共有の機能を提供する。更にユーザー　エンゲージメント、溜まり場、Android アプリの自動ダウンロードをサポートする。</p> 
 <p>新しいサービスの議論は、Facebookとの <a target="_blank" href="http://www.theverge.com/2013/2/26/4030970/google-plus-sign-in-takes-on-facebook-connect-and-frictionless-sharing">予期される競争</a>が支配的だったが、技術的観点から、隠れている<a target="_blank" href="https://developers.google.com/+/">Google+ API</a>に目を向けるのは、いかに新しいフィーチャが動作し、使用するために配置されている標準のいくつかを理解するのに役立つ。</p> 
 <!-- <h3>Authentication and Authorization</h3> --> 
 <p>シンプルな[g+ | Sign In] <a target="_blank" href="https://developers.google.com/+/web/signin/">ボタン</a>は、サードパーティのWebページ、デスクトップやモバイルアプリケーションへの入り口を提供する。これは、ユーザーのGoogle+プロファイル用のアクセストークンを要求するアプリケーションを開始するプロセスを起動する。協調動作は、<a target="_blank" href="https://developers.google.com/+/web/signin/#using_the_client-side_flow">クライアント側のフロー</a>を介してウェブブラウザで行われるか、<a target="_blank" href="https://developers.google.com/+/web/signin/server-side-flow">サーバー側のフロー</a>を使ってバックエンドAPIの操作を介して行われる。ユーザーがまだGoogle+で認証されていない場合、認証は、サインインの一部として実行される。ユーザーはまた、サードパーティ製アプリケーションに与えたいアクセスのレベルを求められる。アクセスレベル、または<i>スコープ</i>は以下のことを含めることができる。</p> 
 <ul> 
  <li>userinfo.email: ユーザの電子メールアドレスのみを提供する</li> 
  <li>plus.me: ユーザーのGoogle+のプロファイル情報を提供する</li> 
  <li>plus.login: サークルにアクセスし、ユーザーのGoogle+アクティビティストリームへの活動を書き込む能力を与えることで、他のスコープを拡張する</li> 
 </ul> 
 <p>このアクセスの協調動作は、認証と認可の組合せで<a target="_blank" href="http://openid.net/connect/">OpenID Connect</a>ドラフト標準に従っており、これ自身が最近批准された<a target="_blank" href="http://www.rfc-editor.org/rfc/rfc6749.txt">OAuth 2</a>プロトコルにもとづいている。認証は、Googleの認証システム内で完全に処理され、サードパーティのアプリケーションを必要としない。OpenID Connectの層認証は、効果的にユーザーのGoogle+のプロファイルにアクセス権を付与することで、サードパーティのアプリケーションにユーザーを認証する。OpenID Connectは、OAuthの認証プロトコル上に認証を重ねており、ユーザーのGoogle+ プロファイルにアクセスを許すことで、効果的にユーザーをサードパーティ製のアプリに認証する。OpenIDファウンデーションの議長でOpenID Connectの共著者である<a target="_blank" href="http://openid.net/foundation/leadership/">Nat Sakimura</a>氏は、OpenID, OAuth、OpenID Connect間の違いといかにアプリケーションがGoogle+サインインのようなサービスを使ってアクセスを要求するユーザーの身元を確認しているかについて<a target="_blank" href="http://nat.sakimura.org/2011/05/15/dummys-guide-for-the-difference-between-oauth-authentication-and-openid/">素晴らしい説明</a>を提供している。</p> 
 <p>ユーザーは、アクセスを取り消すか、または共有設定を変更することがきる <a target="_blank" href="http://plus.google.com/apps">アプリ設定ページ</a>を使って、自分のアプリの権限を見直すことができる。</p> 
 <!-- <h3>Moments</h3> --> 
 <p>サードパーティ製アプリケーションは、Google+ API内でアプリケーション内アクティビティを管理するために、そのアクセストークンを使えるようになった。Googleは、これらのアクティビティを &quot;<a target="_blank" href="https://developers.google.com/+/api/latest/moments">Moments</a>&quot; として参照し、Google+ APIは、momentsを挿入、リスト、削除するための簡単なCRUDインターフェースを提供している。MomentsにはActivityTypeと呼ばれる、さまざまなタイプがある。すべてのアクティビティには、名前、説明、サムネイル、そして<i>itemtype</i>（これは、アクティビティの主題である）がある。Itemtypeは<a target="_blank" href="http://schema.org">schema.org</a> &quot;<a target="_blank" href="http://schema.org/Thing">Thing</a>&quot;のサブタイプでなければならない。例えば、<a target="_blank" href="http://schema.org/Book">Book</a>, <a target="_blank" href="http://schema.org/Place">Place</a> あるいは <a target="_blank" href="http://schema.org/Person">Person</a>。更に、項目は、関連項目用の<a target="_blank" href="http://schema.org">schema.org</a>マークアップを持つHTMLページへのURL参照を持たなければならない。こうして、Google+の統合は、構造化されたマークアップの&quot;セマンティックWeb&quot;の開発を促進し、これは、また <a target="_blank" href="http://googleblog.blogspot.com.au/2011/06/introducing-schemaorg-search-engines.html">検索エンジンに有用</a>である。アクティビティのリストは非常に包括的だ。</p> 
 <ul> 
  <li>AddActivityは、項目タイプ、名前、説明およびサムネイルを持つ一般的なアクティビティ</li> 
  <li>BuyActivityは、項目の購入を表す</li> 
  <li>CheckinActivityは、ある場所からチェックインしているユーザーを表し、アドレスと位置情報の追加属性を持つ</li> 
  <li>CommentActivityは、ユーザーがブログの記事、本や他の創造的な仕事にコメントする時に適切だ。</li> 
  <li>CreateActivityは、ユーザーが創造的な仕事を作成するときのため。</li> 
  <li>DiscoverActivityは、ユーザーが創造的な仕事を発見したときのため。</li> 
  <li>ListenActivityは、音楽の録音を聴くユーザーを表し、曲、アルバム、アーティストのメタデータ用の追加属性を提供する。</li> 
  <li>ReserveActivityは、レストランやホテルなどのローカルビジネスの予約を行っているユーザーを意味する。</li> 
  <li>ReviewActivityは、格付け情報を持つ項目のレビュー。</li> 
  <li>WantActivityは、例えば、アプリケーションの希望リストに項目を追加する場合、ユーザがアイテムを望んでいることを示す。</li> 
 </ul> 
 <p>Google+のアクティビティストリームへの、これらのmomentsの提示と配置は、すべてのユーザーの許可設定に基づいて、Google+のによって処理される。</p> 
 <p>この短いレビューは、Sign-Inによりローンチされた新しい Google+のフィーチャの表面を撫でたに過ぎないが、ソーシャルアクティビティストリームへのセマンティックマークアップの拡張と一緒に、新しい認証と認可の標準の面白い例を提供している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
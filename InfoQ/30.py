<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>エンタープライズシステムの新たなスタイル - SDA(Software-Defined Architecture)</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/sda"><em>原文(投稿日：2014/05/24)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>GartnerのVP兼フェローであるYefim V. Natis氏によると，最近上昇中の新たなエンタープライズアーキテクチャスタイルがあるという – それがSDA(Software-Defined Archtecture)だ。</p> 
  <p>氏は&quot;<a href="http://my.gartner.com/webinardetail/resId=2698619">Software-Defined Architecture: Application Design for Digital Business</a>&quot;(参照には登録が必要)と題したGartnerのウェビナ(Webinar)で，現在のITがソフトウェアアーキテクトに課している問題点を取り上げ，長期的に運用可能な，より優れたアプリケーション開発を支援する設計指針のいくつかを提示した。さまざまな話題が議論されたウェビナの中で，次図のように70年代のモノシリックな構造から始まるソフトウェアアーキテクチャの自然な発展形として，氏はこのSDAのアイデアを紹介したのだ(<a href="http://public.brighttalk.com/resource/core/36753/may_8_software_designed_arch_ynatis_54295.pdf">PDF</a>)。</p> 
  <blockquote> 
   <p><a href="/resource/news/2014/05/sda/en/resources/sda-1.png" target="_self"><img title="イメージ" border="0" alt="イメージ" src="http://www.infoq.com/resource/news/2014/05/sda/en/resources/sda-1.png" style="border-top:0px;border-right:0px;background-image:none;border-bottom:0px;padding-top:0px;padding-left:0px;border-left:0px;display:inline;padding-right:0px" _href="img://sda-1.png" _p="true" /></a></p> 
  </blockquote> 
  <p>SDAはSDN(Software-defined Networking)やSDS(Software-defined-Storage)など，クラウドコンピューティングとともに導入された仮想化技術の延長線上にある。しかしここでは，それをソフトウェアのスタック全体にまで拡張する。ソフトウェアの開発側から利用側まで，同一レベルの仮想化を導入するというのが基本的なアイデアだ。内部の実装依存部分はバウンダリによって隠ぺいされるので，ユーザに影響を与えることなく，実装の変更あるいは置き換えが可能になる。また，このプロセスの結果として，２セットのAPIが作り出される – 開発側で使用する内部APIと，上図にあるようなユーザ用の外部APIである。</p> 
  <p>内部APIは対象システムの構造を，標準化されたアーキテクチャ指針に従ってメンテナンス性の高いモジュールとして表現する。パフォーマンス上の理由から，内部APIではシステムに対する最適化が重視される。一方の外部APIは，さまざまな外部エンティティから内部APIを安全かつ容易に利用するためのもので，システムのシンプルなビューを提供するとともに，遠隔実行されるネットワーク呼び出しに対して最適化される。</p> 
  <p>SDAではまずサービスが開発される。ただしこのサービスは直接的には呼び出されず，ゲートウェイによってユーザから隔離される。下の図に示すように，両者の間には仮想的なバウンダリが設置されている。</p> 
  <blockquote> 
   <p><a href="/resource/news/2014/05/sda/en/resources/sda-2.png" target="_self"><img title="イメージ" border="0" alt="イメージ" src="http://www.infoq.com/resource/news/2014/05/sda/en/resources/sda-2.png" style="border-top:0px;border-right:0px;background-image:none;border-bottom:0px;padding-top:0px;padding-left:0px;border-left:0px;display:inline;padding-right:0px" _href="img://sda-2.png" _p="true" /></a></p> 
  </blockquote> 
  <p>SDAゲートウェイは内部実装を仮想化するためのもので，内部APIやプロトコル，使用されているモデルの変換などを担当する。APIのバージョン管理，セキュリティ，ルーティング，オーケストレーションなどの処理もここで行う。Natis氏によれば，このようなゲートウェイはすでに現在でも，いくつかの製品で部分的に実装されている。ApigeeとMasheryのAPIマネージャ，Layer 7あるいはVordelのAPIゲートウェイ，API管理を機能に含むタイプのESB(Enterprise Service Bus)，CastIronやBoomiのようなIPaas(Integration Platform-as-a-Service)などがその例だ。</p> 
  <p>さらに氏は，データセキュリティに関する処理を行うために，元データを処理可能なサービスをいくつか用意しておくことを推奨する。管理とセキュリティの機能を少数のAPIに集中させて，セキュリティホールとなり得る領域を狭くするためだ。</p> 
  <p>我々はSDAについてさらに詳しく知るため，Natis氏にインタビューした。</p> 
  <p><strong>InfoQ: SDAというものを今まで聞いたことがありませんでした。</strong><strong>以前から使われていた用語なのでしょうか，あなた方の造語なのですか？</strong></p> 
  <blockquote> 
   <p>[YN] はい，SDA(Software-Defined Architecture)はGartnerが導入したもので，これまでは使用されていませんでした。現在も発展中の新しい用語です。</p> 
  </blockquote> 
  <p><strong>InfoQ: SDAはモノシリックや２ティアなどに続く，ソフトウェアアーキテクチャの自然な進化の段階なのでしょうか？</strong></p> 
  <blockquote> 
   <p>[YN] そうですね，SDAとは仮想化SOA，あるいは管理されたSOAだと考えて頂いて差し支えありません。SOAインターフェース(API)の急激な拡大や，ユーザ定義型のAPIへの根強い要望に対応するものがSDAなのです。アプリケーションの仮想化，外部APIと内部APIの分離などによって，アプリケーションのコントロールを失うことなく，独自の外部APを自由に定義できるようになります。</p> 
  </blockquote> 
  <p><strong>InfoQ: SDAを使用するメリットは何でしょう？</strong></p> 
  <blockquote> 
   <p>[YN] アプリケーションあるいはアプリケーションサービスの仮想化が可能になることです。さらに，アプリケーションと外部との間に中間層(ゲートウェイ)が導入されるので，これを利用して外部サービスユーザとアプリケーション実装の間に付加価値を持たせることができます。管理機能，トラッキング，セキュリティ，課金処理，動作監視，最適化，ルーティング，統合，コンポジション，オーケストレーション，コンテキストインジェクションなど，さまざまな用途が考えられます。基本的なアプリケーションやデータにリスクを加えることなく，ユーザ独自のAPIを設計することができるのも，もうひとつのメリットでしょう。</p> 
  </blockquote> 
  <p><strong>InfoQ: SDAがどのような場面で使われるのか，いくつか例を挙げて頂けますか？</strong></p> 
  <blockquote> 
   <p>[YN] アプリケーションでのSDAは新たなコンセプトなので，本格的な実装例はあまり多くありません。NetflixのAPI管理などが適当な例でしょう。しかしインテグレーションブローカやAPI管理，APIゲートウェイの主要企業やSOAインターフェースマネージャでは，SDAの機能をある程度まで提供しています。アプリケーションサービスの管理で一貫性のある本格的なSDAの使用例が現れるのは，まだ数年先のことでしょう。技術的な問題もありますが，実行する組織の文化や規律による部分もそれに劣らず大きいのです。</p> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
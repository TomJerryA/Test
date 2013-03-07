<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>統合コンポーネントとしてGWTを加えた Vaadin 7 が登場</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/02/vaadin-7;jsessionid=D4F5680544D109DE080EF5F4DCEBDE9D"><em>原文(投稿日：2013/02/28)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://vaadin.com/">Vaadin</a>は，JavaベースWebアプリケーションフレームワークのバージョン７をリリースした。このVaadin 7プラットフォームは，同社としては2009年以来のメジャーアップデートになる。</p> 
 <p>Javaを使っているWebアプリ開発者の立場から見れば，Vaadin 7はWicketやJSF，あるいはGWT(Google Web Toolkit)などに相当するフレームワークのひとつだ。これらを比較してみれば，それぞれ類似点と相違点のあることに気付くだろう。Wicketとは特に共通点が多いが，VaadinがHTMLテンプレートの利用を必須としていないことが大きな相違点だ。JSFも同様で，サーバ側フレームワークであるという点は共通しているが，VaadinアプリケーションにはXML設定ファイルが必要なく，通常のJavaでプログラミング可能であるという違いもある。</p> 
 <p>Vaadinグループは５年以上にわたってGWT Steering Committeeのメンバを続けている。今回のVaadin 7では，コアコンポーネントとしてそのGWTを新たに採用した。2012年6月の <a target="_blank" href="https://vaadin.com/blog/-/blogs/gwt-built-in-vaadin-7">ブログ記事</a> で同社のLehtinen氏は，&quot;現在GWTを使ってアプリを開発しているのであれば，プロジェクトのJarファイルを置き換えるだけで，Vaadinに移行することができます&quot; と述べている。GWTの採用により，ユースケースにもよるが，従来のVaadinアプリケーションに対していくつかのメリットが生まれている。GWTアプリケーションの一般的なメリットとしては，オフラインでも動作する，サーバ側の状態管理を必要としないために多くの同時ユーザ(10,000以上)をサポート可能である，レイテンシが低い，などがある。ただしJava開発者とすれば，すべてがJavaで記述されていて，Javaサーバあるいはポータルで動作する従来型のVaadinベースUIの方が，開発上の苦労が少ないことは間違いないだろう。</p> 
 <p>Vaadin 7には，GWT以外にも <a target="_blank" href="https://vaadin.com/vaadin7">65の新機能</a> が実装されている。<a target="_blank" href="https://vaadin.com/faq">FAQ</a> ページには，Java EE標準に準拠して単一jarファイルとして実装されていること，標準的なデスクトップUIプログラムパターンを採用していること，などが紹介されている。さらには，40,000以上の活動的な登録メンバで構成されるオープンソースコミュニティのサポートとフィードバックも，今回のフレームワークの開発に活かされている。</p> 
 <p>InfoQではJoonas Lehtinen 氏 (Vaadin.comのCEO) にコンタクトを取り，Vaadin 7に関する詳細を聞いた。</p> 
 <p><strong>InfoQ: Vaadinの最新リリースで，フレームワークの利用者の立場から見てもっとも便利な機能を５つか６つ程度，挙げて頂けますか？</strong></p> 
 <blockquote>
  私が選びたいものは，https://vaadin.com/vaadin7 で紹介しているリストほとんど同じです。
  <br /> 
  <br /> それ以外のトップ５は次のものです。
  <br /> 
  <ol> 
   <li>GWT全体が組み込まれていること。これによって，すべてのパッケージがサポートされます。Googleの素晴らしいJava-to-JavaScriptコンパイラの能力を，アプリケーション内でも簡単に利用できるのです。</li> 
   <li>ウィジェットエクステンション。既存のウィジェット上に，独立したエクステンションとして機能を追加することができます。詳細は次のページを参照してください: https://vaadin.com/wiki/-/wiki/Main/Creating%20a%20component%20extension.</li> 
   <li>Saasコンパイラに，以前から要望のあったテーマのモジュール化が導入されました。</li> 
   <li>再設計されたレイアウトエンジン。すべてをJavaScript内で計算する代わりに，ブラウザネイティブなレイアウト計算を利用するようになっています。これによってリフロー数が大幅に減少するとともに，レイアウトの速度も向上しました。副次的な効果として，CSSもすべてサポートされています。</li> 
   <li>再設計されたウィンドウAPI。Vaadinアプリケーションを以前よりもWebアプリケーションらしくすると同時に，HTTPリクエストやWebページへのアクセスも簡単になりました。</li> 
  </ol> 
 </blockquote> 
 <p><strong>InfoQ: &quot;<a target="_blank" href="https://vaadin.com/gwt-report-2012-portlet/download/1871870899/Future-of-GWT-Report-2012.pdf">The Future of GWT Report 2012</a>&quot; と題されたレポートでは，SmartGWT，GXT，ErraiなどがGWTの拡張であるのに対して，VaadinはGWTを補完するものだ，とされています。</strong><strong>これについて詳しく説明してください。</strong></p> 
 <blockquote>
  GWTのプログラミングモデルには２つの抽象化レベルがあります。
  <br /> 
  <ol> 
   <li>Javaで記述されてJavaScriptにコンパイルされる UI。</li> 
   <li>ネイティブなJavaScript。SmartGWTやGXT，Erraiなどは基本的に，GWTの定義するプログラミングモデルに対して，新たな(本当にすばらしい)コンポーネントやヘルパを提供するものです。</li> 
  </ol> VaadinはGWTの提供するプログラミングモデル上に，サーバサイドJavaプログラミングモデルを加えます。この高レベルな抽象化によって，現代的Webアプリを実装するために必要なソフトウェア層の数が少なくなります。それが開発のスピードアップを実現するのです。GWTでは通常，UI層(ブラウザ)，RPCプラスUIサービス(サーバ)，ビジネスロジック(サーバ)の３つを構築する必要があります。しかしVaadinでは，サーバ上のUI・ビジネスロジック層だけでいいのです。このような本質的な削減によって，アプリケーションUIの開発に必要なコードサイズを半減できます。しかも柔軟性が必要な場合には，JavaあるいはJavaScriptでクライアント側UIを記述するための手段も提供しているのです。
 </blockquote> 
 <p><strong>InfoQ: GWTを使用している開発者からは，GWTに関する書籍の発行が極めて少ない以前の状態から，最近ではほとんどなくなっていることに対して不満の声が上がっています。</strong><strong>この状況を考えたとき，<a target="_blank" href="https://vaadin.com/book">Book of Vaadin</a> という書籍の重要性について，どのようにお考えでしょうか？</strong><strong>また，この本は現在プレビュー版ですが，今後どのような修正や拡張の予定があるのでしょう？</strong></p> 
 <blockquote>
  Book of Vaadinは，2007年から改訂が続けられています。 とても大変な仕事ですが，一流のマニュアルはどのようなフレームワークにおいても非常に重要な部分である，と私たちは考えています。機能が文書化されていなければ，誰も利用することなどできません。
  <br /> 
  <br /> Book of Vaadinの第１版は３月初頭には完成して，誰でも自由にダウンロード可能になる予定です。それ以降については，機能追加が実施されるごとに修正作業を続けていきたいと思っています。
 </blockquote> 
 <p><strong>InfoQ: Vaadin組み込み用にメンテナンスしているバージョンのGWTをVaadin開発チームが配布する場合，標準のGWTとの整合性を保つために，どのようなことを行う予定なのでしょうか？</strong></p> 
 <blockquote>
  私たちが手を加えているバージョンのGWTは，https://github.com/vaadin/gwtでソースを入手できます。
  <br /> 
  <br /> Vaadinフレームワーク全体のソースもhttps://github.com/vaadin/vaadinから入手可能です。
  <br /> 
  <br /> 私たちが現在配布しているのはVaadin Framework(GWT用ではない)のリリースのみですが，VaadinにはGWTが含まれていますから，これをGWTリリースの代替として使用することは可能です。フレームワークのクライアント側だけを使用しても問題ありません。
  <br /> 
  <br /> GWTとVaadinの関連性をアーキテクチャ的な視点で見たいのでしたら，https://vaadin.com/blog/-/blogs/vaadin-7-application-architectureを参照してください。
 </blockquote> 
 <p><strong>InfoQ: あなた方のWebサイトにある <a target="_blank" href="https://vaadin.com/faq">FAQ</a> には，&quot;Vaadinを使うべきではないのは (When should I not use Vaadin)?&quot; という章があります。</strong><strong>エンタープライズプロジェクトの規模は，Vaadin採用の判断に影響する部分があるのでしょうか？</strong></p> 
 <blockquote>
  そういう場合もあります - プロジェクトが大規模になるほど，Vaadin開発のメリットも大きいのです。逆にごく小規模なアプリケーションであれば，どのようなフレームワークでも，もちろんVaadinでも，簡単にできるはずです。
 </blockquote> 
 <p><strong>InfoQ: &quot;<a target="_blank" href="https://vaadin.com/who-is-using-vaadin">Vaadinを使っているのは(Who Is Using Vaadin)? </a>&quot; というページには，フィンランドで３４のショーケース(showcase)が提供中，とあります。</strong><strong>6つのショーケースを持つ米国が，一覧表ではその次にあります。</strong><strong>Vaddinのショーケースとは何でしょう？</strong><strong>170カ国の開発者がVaadinを使用しています。彼らの国々でVaadinのショーケースを増やすためには，何が必要なのでしょうか？</strong></p> 
 <blockquote>
  残念ながらこのショーケースマップは，非常に不完全なものです。&quot;Vaadinを使っているのは？&quot; リストを集めているときに私たちは，Vaadinの使用事例を見つけようとして，あちこち尋ねて回っていました。私たちの本社はフィンランドにあります。そのために，優れた採用事例がたくさん私たちの地元で集まった，という訳なのです。
  <br /> 
  <br /> できれば世界中から，このショーケースをリストアップしたいと思っています。 Vaadinで素晴らしいサイトを構築した人がいれば，ぜひ私たちに連絡をください。リストに掲載したいと思います。 
 </blockquote> 
 <p><strong>InfoQ: JVM以外のWebアプリケーションフレームワークで，Vaadinの競合相手となるものはありますか？</strong><strong>もしあれば，名前を教えてください。</strong></p> 
 <blockquote>
  当社はJVMを中心としていますが，こちらの世界でWebアプリを開発している人たちはみな，Webプラットフォームを使用しています。ですから，最大の競合相手はJavaScriptフレームワーク，ということになります。 異なるスキルを持ったフロントエンドとバックエンドのチームが別々にあったとしても，プロジェクトによってはうまくいくかも知れません。しかしエンタープライズ界でこのような２つのチームを持つことの過剰コストは，大部分のプロジェクトにとって不要なもののはずです。
 </blockquote> 
 <p><strong>InfoQ: Vaadinのコードベースにコントリビュートしたいというプロ開発者もいると思います。</strong><strong>このように隠れたコントリビュータを見つけ出すために，あなたのチームメンバたちは，どのようなプロセスを用いているのでしょう？</strong></p> 
 <blockquote>
  Vaadinプロジェクトへのコントリビューションのほとんどは，アドイン・コンポーネントの形で提供されています。このおかげで，Vaadinのコントリビュートの敷居は非常に低くなっています。Vaadinのディレクトリhttp://vaadin.com/directoryには，誰でもコントリビュートできるのです。
  <br /> 
  <br /> Vaadin Frameworkのコア部分にコントリビュートしたい場合には，まずは問題追跡システム http://dev.vaadin.com/wiki/SubmittingBug を通じてパッチを送ってください。コア開発チームの誰かがパッチを取得して評価，テストを実施した上で，当社内のGerritレビューシステムに送信します。それをコアチームの他のメンバが確認，評価するのです。このプロセスの中で，少なくとも部分的なパッチの書き換えは行われることになるでしょう。コントリビュータにはCA(Contribution Agreement)への署名も必要となります。
  <br /> 
  <br /> 将来的には社内Gerritシステムを公開したり，GitGubからのプル要求を受託するなどして，このプロセスをもっと簡略なものにしたいと思っています。
 </blockquote> 
 <p><strong>InfoQ: <a target="_blank" href="https://vaadin.com/blog/-/blogs/roadmap-for-the-next-74-days">ブログ記事</a> のロードマップからは，Vaadinフレームワークの開発プロセスを安定化しようという意図が感じられますが，</strong><strong>今後のプロセスは決定しているのでしょうか？</strong><strong>それはどのようなものでしょう？</strong></p> 
 <blockquote>
  私たちは先日，プロセスを一新しました - 理由のひとつは，Vaadin プロジェクトの遅れです。実際の開発を進めながら，並行してもっとカジュアルな研究プロジェクトにもトライしてみたいと思っています。そうすれば，ロードマップの見積もりも，もっとよいものになるでしょう。コアプロセスには，月毎のロードマップミーティングも含まれています。すべての製品に関する向こう３ヶ月のロードマップを，そこで決定します。内部プロセス全体としては，次のようになっています。
  <br /> 
  <br /> 
  <div style="text-align: center">
   &nbsp;
  </div> 
  <div style="text-align: center; font-weight: bold">
   <img alt="" src="http://www.infoq.com/resource/news/2013/03/vaadin-7/ja/resources/Vaadins_Development_and_Release_Process.jpg;jsessionid=D4F5680544D109DE080EF5F4DCEBDE9D" _href="img://Vaadins_Development_and_Release_Process.jpg" _p="true" />
  </div> 
  <div style="text-align: center; font-weight: bold">
   図：Vaadinの開発およびリリースプロセス
  </div> 
  <br /> 開発自体は、製品の機能に応じて，1～2週間という周期で行っています。世界に向けて公開できそうなものが完成に近づいた，と思えるような段階に達したとき，私たちは内部で開発レビューを行っています。そして可能であればアルファあるいはベータ版を公開して，開発プロセスの早いうちにフィードバックを収集するようにしているのです。
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
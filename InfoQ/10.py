<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Eclipse RAP 2.0リリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/02/eclipse-rap-2-released;jsessionid=328F64F91DC2A3D3D25B345FE9551868"><em>原文(投稿日：2013/02/28)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>6年の開発期間を経て、1月11日に<a target="_blank" href="http://eclipse.org/rap/">Eclipse RAP 2.0</a>がリリースされた。この期間にプロジェクトはEclipseに完全に統合され、Eclipse 4上で複数ユーザのインターフェースをサポートするようになった。</p> 
 <p>最初はInnoopractが開発し、今は<a target="_blank" href="http://eclipsesource.com/en/home/">EclipseSource</a>が開発をしている<b>Eclipse Rich Application Platform</b>はリッチなウェブアプリケーションを作るためのRCP、SWT、JFaceライブラリの再実装だった。ネイティブのグラフィックデバイスに描画する代わりに、SWTのRAP実装はJavaScriptを生成する。このJavaScriptが<a target="_blank" href="http://qooxdoo.org/">qooxdoo</a>ウェジェットライブラリを使って描画を行う。状態の更新はHTTPリクエストのポーリングを使ってサーバとクライアント間で同期される。Vaadinでも同じようなコンセプトが実装されている。Vaadinの場合はGWTを使ってサーバサイドモデル上にJavaScriptを提供する。このモデルはSWTから着想を得たVaadinのコンポーネントによって実装されている。</p> 
 <p>しかし、RCPのある種の限界はRAP 1.0では克服できなかった。例えば、Eclipse RCPは1人以上のユーザが使うことを想定して設計されていなかった。しかし、複数人が使うのはウェブアプリケーションの場合は普通のことだ。Eclipse 4の開発でこのような限界は克服され、RAPはどのようなクライアント実装からでも利用できるユニバーサルなAPIを提供できるようになった。</p> 
 <p>2.0のリリースに合わせて、Eclipse RAPは名前をRich Ajax Platformから<b>Remote Application Platform</b>へ変更した。リモートサーバに接続するどのようなクライアントでも利用できるプラットフォームになるということを反映した名前変更だ。このような取り組みは、バージョン1.5の時から始まっていた、とEclipse SourceのRalf Sternberg氏は<a target="_blank" href="http://eclipsesource.com/blogs/2013/02/01/rap-2-0-countdown-15/">RAP 2.0についてのブログ記事</a>で書いている。バージョン1.0の時は、サーバサイドコンポーネントはJavaScriptを使ってウェブブラウザと通信していたが、今はJSON APIを使っている。RAP 2.0のクライアントはJavaScriptに制限されない。<a target="_blank" href="http://developer.eclipsesource.com/tabris/">Tabris</a>のようなネイティブの実装にもなりうる。TabrisはiOSとAndroidのユーザインターフェースを提供する。</p> 
 <p>InfoQはEclipse RAPのプロジェクトリードである<b>Ralf Sternberg氏</b>にこのプロジェクトの次の計画について話を聞いた。</p> 
 <p><b>InfoQ</b>:2.0のリリース、おめでとうございます。RAP 1.0で抱えていた多くの問題がEclipse PlatformとRAPチームの協業によって解消されたのは素晴らしいことです。解決した問題のうち、一番大きかったのは何でしたか。また、協業はどうでしたか。</p> 
 <blockquote> 
  <p>ありがとうございます。1.0のころは、RAPはRCPアプリケーションをウェブブラウザで動かすことができるクールで先進的なプロジェクトでした。しかし、時がたち、プロジェクトは成熟し、Eclipseの世界に統合され、Eclipseコミュニティが抱えるサーバサイドアプリケーションの問題に気付くことになりました。</p> 
  <p>最も明白な課題は複数ユーザに対応することです。例えば、単一の文字列の翻訳を固定的に持つだけでは、異なる言語のユーザが同時にアプリケーションを使う場合に対応できません。RAPの複数ユーザの要求は、最終的にはEquinoxで複数のロケールをサポートし、JFaceのダイアログフレームワークにある種の調整を加えることになりました。</p> 
  <p>現在のEclipseプラットフォームを見ると、サーバサイドの要求が新しいEclipseプラットフォームであるE4に影響を与えるのは素晴らしいことだと思います。一般的にサーバサイドアプリケーションは疎結合、スレッドセーフ、高性能を要求します。技術が進むにつれて、このような特性が現在のすべてのアプリケーションの標準になると思います。</p> 
 </blockquote> 
 <p><b>InfoQ:</b>RAPを使うのに最適なプロジェクトはどのようなものでしょう。2.0ではどのような点が改善されましたか。</p> 
 <blockquote> 
  <p>現在、開発者は、アプリケーションがサポートしなければならないプラットフォームの増加に直面しています。5年前はディスクトップとブラウザがプラットフォームでしたが、今はモバイルとタブレットもあります。各プラットフォームはそれぞれ別の開発ツールと特別なノウハウを必要とします。これはひとつのソースのアプリケーションで複数のプラットフォームに対応するという私たちが取り組んだ課題とまったく同じです。</p> 
  <p>RAP 2.0では適切なプラットフォームに対してオープンなプロトコルでアクセスするためのクライアントコネクションを提供します。EclipseSourceでは、&quot;Tabris&quot;ブランドとしてiOSとAndroid向けのネイティブクライアントを提供します。この新しいプロトコルを使えば、誰もが他のプラットフォーム向けのRAPクライアントを開発できます。RAPは&quot;write once, run anywhere&quot;なプラットフォームを提供し続けます。</p> 
  <p>結果的に、RAPが最適なプロジェクトは将来のプラットフォームでコードの再利用をするという選択肢を持つ持続的な開発モデルを模索しているプロジェクトです。企業向けソフトウエア開発の世界ではこの要求は一般的です。</p> 
 </blockquote> 
 <p><b>InfoQ:</b>将来の計画はどうでしょうか。Vaadinが実現しているような技術を模索していますか。RAPをどのようなポジションに置きたいのでしょうか。</p> 
 <blockquote> 
  <p>もちろん、他のプロジェクトのサーバサイドUIの技術も追いかけています。単一ページのアプリケーション用のフレームワークにはとても印象的なものもあり、RAPのルックアンドフィールを改善するためのベンチマークとして使っています。RAPにはまだ改善の余地があり、私たちはユーザと共に一歩一歩改善しています。最新の例ではAllianz保険のために新しい動的ドロップダウンを実装しました。</p> 
  <p>近い将来、WebClientのための多くのカスタムウィジェットが登場すると思います。RAP 2.0はカスタムウィジェットやアドオンを簡単に開発できるクライアントサイドAPIを提供します。アドオンはどのようなJSライブラリも利用できます。RAPの内部には依存しません。拡張性は私たちにとって重要な資産です。今後も改善を継続していくつもりです。</p> 
  <p>しかし、RAPが他のフレームワークと違うのは、HTML5を超えている点です。私が知る限り、RAPはアプリケーションを一度開発すれば、すべてのプラットフォームで動作する唯一のクロスプラットフォームフレームワークです。ブラウザはひとつの選択肢です。また、ネイティブなウェジェットとネイティブなルックアンドフィール、ネイティブなナビゲーションコンセプトを提供するネイティブアプリは強力な選択肢のひとつです。</p> 
  <p>また、モジュール化されたアプリケーションの開発を支援するのもRAPの重要な特徴のひとつです。RAPはOSGi上で構築され、Eclipseプロジェクトとして、EMF、EclipseLink、Eclipse DatabindingのようなEclipseの技術とも自然に統合されます。JFaceを使えばUIとデータモデルを簡単に接続できます。私たちはこのようなモジュラリティが現在のアプリケーションにとって重要だと信じています。</p> 
 </blockquote> 
 <p><b>InfoQ:</b>プロジェクトを更新しようとしている開発者にアドバイスをお願いします。</p> 
 <blockquote> 
  <p>RAP 2.0は1.0とはバイナリレベルでの互換性はないということに注意してください。このメジャーリリースを機会にいくつかのAPIを整理しました。しかし、私たちはすぐにアップグレードすることをおすすめします。というのはRAP 2.0には重要な改善が含まれているからです。イベントハンドリングシステムやサーバプッシュシステムの改善です。何の問題もなくアップグレードを行っているプロジェクトをいくつか知っています。私たちのウェブページではアップグレードを支援するためのガイドを提供しています。</p> 
 </blockquote> 
 <p>RAP 2.0の<a target="_blank" href="http://eclipse.org/rap/noteworthy/2.0/">新しい点、注目すべき点</a>と<a target="_blank" href="http://eclipse.org/rap/noteworthy/2.0/migration-guide/">移行ガイド</a>が利用できる。移行を始める前に読むべきだろう。</p> 
 <p><i>Fabian Lange氏はEclipse Rich Ajax Platform 1.0の著者。</i></p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Neil Bartlett氏に聞く - OSGiとBndtools 2.0リリースについて</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Bndtools2;jsessionid=3A48DE420EF6256ABF109F62C07AB4D2"><em>原文(投稿日：2013/03/21)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Neil Barlett氏は卓越したOSGi専門家であり，現在はEclipseのOSGiプラグインとして有名なBndtoolsのメンテナでもある。その氏が先日，Bndtools 2.0のリリースを発表した。注目されるのは次のような機能だ。</p> 
 <ul> 
  <li>OSGi リリース５仕様のレゾルバとレポジトリをサポート</li> 
  <li>実行ディスクリプタを，スタンドアロンの実行可能ファイルとしてエクスポート可能</li> 
  <li>ベースライニング (不正バージョンのバンドルをビルドエラーとして通知)</li> 
  <li>コンシューマとプロバイダのアノテーション記述の導入により拡張されたセマンティックバージョニング</li> 
  <li>パッケージデコレーションのエクスポート</li> 
  <li>インクリメンタルビルダの改善</li> 
  <li>Apache ACEのサポート</li> 
  <li>多数のバグフィックスとパフォーマンス向上</li> 
 </ul> 
 <p>前回リリースされた1.1の公開が2012年３月だから，まさに待望のリリースだ。</p> 
 <p>InfoQではNeil Bartlett氏に，Bndtoolsを含むOSGi全般に関して話を聞いた。</p> 
 <p><b>OSGiに馴染みのない読者のために，OSGiとBndtoolsについて少し説明して頂けますか？</b></p> 
 <blockquote> 
  <p>OSGiはモジュラーアプリケーションを開発する手法のひとつです。明確に分離されて，依存性が明示的に管理されたモジュール (&quot;バンドル&quot;と呼ばれます) の開発が可能です。依存性を重視することによって，バンドルが現在の環境にインストール可能か，依存関係にあるバンドルの追加が必要か，他のモジュールに影響があるのか，といったことが明確になります。</p> 
  <p>Bndtoolsは，OSGiのバンドルとアプリケーションを開発するためのIDEです。Eclipseをベースとしていて，Eclipse Marketplaceからインストールすることができます。</p> 
 </blockquote> 
 <p><b>OSGiは，規模や種類に関わらず，すべてのJavaプロジェクトにとって重要なのでしょうか。それとも大規模プロジェクトか，あるいは小規模プロジェクトに適したものなのでしょうか？</b></p> 
 <blockquote> 
  <p>OSGi の意義はモジュール化にありますから，そのメリットはプロジェクト規模の大小に関わりません。大規模プロジェクトをモジュール化するメリットは明らかです - 複雑な構造を分解して，作業を管理可能な大きさに分割する操作をOSGiが支援してくれます。小規模なプロジェクトにもメリットがあります。例えば，ごく短いコードを書いたとしても，後にそれを別のプロジェクトで再利用したいこともあるでしょう。OSGiバンドルとして開発されていれば，再利用はずっと簡単になるのです。</p> 
  <p>そうは言っても，本当に小さなプロジェクトならば，モジュールにする必要もないでしょうね。&quot;Hello World&quot; にモジュール化アプローチを使っても，大したメリットはありませんから！</p> 
 </blockquote> 
 <p><b>OSGiには熱心な支持者こそいますが，大きな流れにはなっていないように思えます。</b><b>その理由はどこにあるのでしょう？</b></p> 
 <blockquote> 
  <p>そうですね，支持は急速に増えていますが，メインストリームになるまでに至っていないのは事実です。ソフトウェア開発プロセス全体の改善を目指しているという意味から言うと，OSGiは，実は相当に野心的な試みなのです。コードレポジトリからテスト，チーム構成に至るまで，すべての面に影響を与えることになります。ですから，そのメリットが認められるには時間が必要です。不確実な将来的利益のために必要な先行投資に対して，多くの企業が神経質になるのも無理はありません。それでも成功を収める企業が増えるに従って，この状況も変わってきています。</p> 
  <p>もうひとつの問題は技術的なものです。OSGiにはこれまでずっと，非常に粗末なツールサポートしかありませんでした。Bndtools – と，統合可能なツールのエコシステム – によって，この状況は好転し始めています。</p> 
 </blockquote> 
 <p><b>Androidが現在注目を集めていますが，OSGiはAndroid開発にも関与しているのでしょうか？</b></p> 
 <blockquote> 
  <p>はい，Androidアプリケーションも今後は大規模で複雑なものになっていくと思いますから，モジュール化を重視していかなければならないのは同じでしょう。AndroidプロジェクトにもOSGi導入の成功例はあります。ただしAndroidは，標準的なJavaとは – 微妙ですが，重要な部分で – かなり違いますから，当面は実験的な段階が続くと思います。</p> 
 </blockquote> 
 <p><b>BndtoolsはOSGiプロジェクトでどのように利用されるのでしょう？</b></p> 
 <blockquote> 
  <p>OSGiを使うのは難しいと一般に言われます。しかし本当に必要なのは，利用するコードに関する確実な情報を，明確に記述しておくことなのです。この種の情報のほとんどすべては，バンドルに収められたJavaクラスの中にあります ... ですから，それを引き出さなければなりません。Bndtoolsは開発プロセスのこの部分を担うものです。これによって開発者は，ソースに書いたことをもう一度書き下す必要がなくなり，自身のコードに専念できます。</p> 
  <p>さらにBndtoolsは，Eclipseのビルドシステムにも統合されています。つまりソースファイルを編集すればバンドルが直ちにビルドされて，実行可能な状態になるのです。その時点でOSGiランタイムが (デバッグやテストなどで) 起動されていれば，実行時にモジュールを動的に更新可能なOSGiのメリットを活かして，新しいバンドルがすぐに挿入されます。これによって非常に速いコード／実行／テストのワークフローが実現します。基本的にはコードを保存したとたんに，すでに実行されているのですから。</p> 
  <p>Bindtools 2.0では，OSGi リリース５の新しいレゾルバとレポジトリ仕様のサポートも追加されました。これによって，コア機能を提供する少数の &quot;トップレベル&quot; モジュールに注力したアプリケーション構成が可能になります – コアからの静的あるいは実行時依存性は，レゾルバがすべて面倒を見てくれるのです。ですから，クラスパスに必要なJARの長いリストを管理する必要はもうありません。</p> 
 </blockquote> 
 <p><b>Bndtoolsには，コラボレーションのためのツールはありますか？</b></p> 
 <blockquote> 
  <p>はい。開発者間のコラボレーションでは，共有するAPIの互換性の維持や，それを変更する必要が生じた場合の調整方法などが特に難しい部分です。これをうまく扱うためには，適切なバージョン戦略が重要になります。ところがほとんどの開発者は，制作物へのバージョン設定を手操作で，かなり適当に行っているのが実情です。BndToolsにはクラスパスを解析して，以前にリリースしたバージョンとの変更点を検出する機能があるので，バージョンの自動更新が可能になります。APIの利用者のために，互換性のあるバージョン範囲を検出する機能や，その範囲のインポートを自動生成する機能も備えています。</p> 
 </blockquote> 
 <p><b>Bndtoolsと競合するものはありますか？</b></p> 
 <blockquote> 
  <p>おそらくもっとも身近な競合相手はPDE (Plug-in Development Environment) でしょう。同じEclipseベースのIDEですが，アプローチがまったく違います。私はもちろんBndtoolsの方が優れていて，生産性も高いと思っています。私自身，Bndtoolsを開発するまではPDEを長い間使っていましたから，この結論には自信があります。</p> 
 </blockquote> 
 <p><b>Eclipseの使用は必須なのでしょうか，あるいはスタンドアロンでも利用可能ですか？</b><b>IntelliJやNetbeansなど，他のIDEもサポートしていますか？</b></p> 
 <blockquote> 
  <p>YesとNo，両方ですね。BndtoolsはPeter Kriens氏が開発したbndをベースにしています。bnd自体はコマンドラインやANT，Mavenなどからの利用を前提としたヘッドレスなツールですから，NetBeansやIDEA，さらに通常のテキストエディタを使っている開発者でも，bndさえ利用できればプロジェクトを使って作業することは可能です。</p> 
  <p>BndtoolsはEclipseの使用が必須です。他のIDEで直接使用することはできません。ただし他のIDEでも，bnd自体を使って独自のOSGiサポートを開発することは可能でしょう。Bndtoolsの便利な機能はほとんどがbndに由来しています。Bndtools自体はディスクリプタファイル用のしゃれたエディタ，ランチャ，Eclipseのビルドライフサイクルへのフックといったものを提供しているに過ぎません。</p> 
  <p>多くの人たちにOSGiを利用してほしいと思っていますから，他のIDEにもこのようなものを開発してほしいですね。Eclipseを好まない人たちに，無理強いするつもりはまったくありません。</p> 
 </blockquote> 
 <p>さらに詳しい情報を得るためのソースとして，<a target="_blank" href="http://bndtools.org/tutorial.html">Bndtool Tutorial</a> と並んでBartlett氏が推薦するのは，<a target="_blank" href="http://www.infoq.com/articles/java-application-architecture;jsessionid=CE3FC6104FFDA8C30D2BF21697A6FA8C;jsessionid=3A48DE420EF6256ABF109F62C07AB4D2">InfoQでも以前紹介した</a> Kirk Knoernschild氏の &quot;Java Application Architecture&quot; ，bndやBndtoolsなどのOSGiツーリングについて取り上げた Tim Ward，Holly Cummins両氏の共著 &quot;Enterprise OSGi in Action&quot; などの書籍だ。</p> 
 <p>InfoQでもこれまでに，モジュール化全般に関して議論した記事を，<a target="_blank" href="http://www.infoq.com/articles/modular-java-what-is-it;jsessionid=CE3FC6104FFDA8C30D2BF21697A6FA8C;jsessionid=3A48DE420EF6256ABF109F62C07AB4D2">Modular Java：それは何なのか？</a>，<a target="_blank" href="http://www.infoq.com/articles/modular-java-static-modularity;jsessionid=CE3FC6104FFDA8C30D2BF21697A6FA8C;jsessionid=3A48DE420EF6256ABF109F62C07AB4D2">Modular Java：静的なモジュール化</a>，<a target="_blank" href="http://www.infoq.com/articles/modular-java-dynamic-modularity;jsessionid=CE3FC6104FFDA8C30D2BF21697A6FA8C;jsessionid=3A48DE420EF6256ABF109F62C07AB4D2">Modular Java：動的なモジュール化</a>，<a target="_blank" href="http://www.infoq.com/articles/modular-java-declarative-modules;jsessionid=CE3FC6104FFDA8C30D2BF21697A6FA8C;jsessionid=3A48DE420EF6256ABF109F62C07AB4D2">Modular Java: Declarative Modularity</a> というシリーズで紹介している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
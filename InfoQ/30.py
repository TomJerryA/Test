<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>C++アプリケーションにOSGi APIを提供するC++ Micro Services</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/10/cpp-micro-services"><em>原文(投稿日：2013/10/29)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>EclipseCon Europeで今日，Sascha Zelzer氏が<a href="http://cppmicroservices.org">C++ MicroServices</a>というネイティブOSGiサービスレイヤを発表した。<a href="http://code.google.com/p/pojosr/">PojoSRプロジェクト</a>と同じように，相互接続サービスを組み込んだアプリケーション開発のためのサービスレイヤ提供が目的だ。C++ MicroServicesもPojoSRも，ライブコードをスワップアウト可能なOSGi機能を完全には実装していない。どちらも同じメモリプロセス，あるいはクラスローダ内で動作する。</p> 
  <p>バンドル(モジュール)の動的な停止と再起動を実現するマルチクラスローダモデルが，OSGiの長所のひとつであるとすれば，この<a href="http://www.osgi.org/blog/2011/04/osgi-lite.html">OSGi Lite</a>には用途があるのだろうか？ そう，PojoSRを始めとするネイティブアプローチ(別のOSGi Cランタイムである<a href="http://incubator.apache.org/celix/">Apache Celix</a>も含めて)の開発者たちは，協調型サービスという観点でのアプリケーション構築を可能にするという意味で，マイクロサービスプログラムモデルにもメリットが存在する，と考えているのだ。これにより，グローバルなサービスカタログに有効なサービス一覧を保持しておいて，それらのサービスを必要なコンポーネントがサービスレジストリに問い合わせて適切な実装を探し出す，という汎用的な依存注入メカニズムが実現可能になるからだ。</p> 
  <p>モジュールが“OSGi Lite” 仕様ではなかったとしても，サービスをレジストリから動的に停止(あるいは削除)することはできる。あるいは実行中のコード置換が実現できなくても，一定レベルの動的処理を実現することは可能だ。また一方で，Javaプログラムやライブラリの抱えている問題は，何もフラットなクラスパスだけに限ったものではない。つまり &quot;OSGi Lite&quot; パターンは，典型的なスパゲッティモデルをサービス構造へとリファクタリングしていく，その移行期間を作り出すためのものなのだ。</p> 
  <p>C++ MicroServicesプロジェクトでは，今年始めに<a href="http://blog.cppmicroservices.org/2013/07/19/cppmicroservices-1.0.0">バージョン 1.0.0をリリースしている</a>。使用方法を説明した詳細な<a href="http://cppmicroservices.org/doc_1_0/MicroServices_Tutorials.html">チュートリアル</a>と合わせて，<a href="https://github.com/saschazelzer/CppMicroServices/releases">GitHub</a>あるいは<a href="http://cppmicroservices.org/download.html">プロジェクトのダウンロードライブラリ</a>から入手可能だ。ライブラリでは &quot;<code>us::</code>&quot; というネームスペース(マイクロサービスの省略形)を使用する。<code>us::ModuleContext</code>(OSGiの<code>BundleContext</code>と同種)，<code>us::GetServiceReference</code>, <code>us::GetService</code>などの他，<code>Load</code>と<code>UnLoad</code>メソッドを備えて，モジュールの起動あるいは停止時の状態初期化を行う基本クラスである<code>us::ModuleActivator</code>や，サービスのインストールやアンインストールを追跡する<code>us::ServiceTracker</code>などが提供されている。</p> 
  <p>InfoQではZelzer氏に連絡を取り，最初にC++ Micro Servicesプロジェクトについて質問した：</p> 
  <blockquote> 
   <p><b>Zelzer</b>: 私は医療画像用の大規模なC++コードベースの開発に従事しています。たくさんの学生がアルゴリズムの開発に利用しています。このようなコードベースと開発者(トレーニングを受けたソフトウェア技術者はほとんどいません)を管理するには，モジュール性と再利用性が特に重要です。これはOSGiの得意とするところなのです。当初私たちは，完全なC++ OSGiライクのフレームワークを導入しようと試みましたが，いくつかの問題に突き当たってしまいました。中でも重大だったのは，純粋なOSGiアーキテクチャを適用するには既存のコードベースが複雑すぎたこと，保守的なC++開発者たちが別の複雑なフレームワークの導入に消極的であったこと，この２つです。いずれにしても，私たちがもっとも重視したのはサービスレイヤです - 実行時のコードのホットスワッピングや，モジュール層でのフレキシブルな依存解決メカニズムといったものは，私たちのユースケースにはありませんでした。それがCppMicroServicesプロジェクトを始めた理由です。</p> 
  </blockquote> 
  <p><b>InfoQ</b>: サービスの起動や終了はどのように扱われるのでしょう – モジュールはロードされたままなのでしょうか？</p> 
  <blockquote> 
   <p><b>Zelzer</b>: 通常，モジュールはアンロードされません(可能であったとしても)。モジュールはコンパイル時のリンク依存を解決するために，起動時に動的リンカによってロードされます。独自のプログラムを用意して，実行時に動的ロードやアンロードを行うことも可能です(ただしアンロードを行うことはほとんどありません)。参照不能になったサービスは，サービスリスナによって処理されなければなりません。アンロードされたモジュールのサービスを他のモジュールが使用し続けると，プログラムエラーが発生します。</p> 
  </blockquote> 
  <p><b>InfoQ</b>: 同じバージョンのコードを使用する場合でも，モジュールのロードとアンロードを動的に行うことができるのですか？</p> 
  <blockquote> 
   <p><b>Zelzer</b>: 可能ですが，これはプログラム次第です。OSが提供している機能(<code>dlopen()</code>, <code>LoadLibrary()</code>など)を使えば，実行時に共有ライブラリを動的ロードすることもできます。</p> 
  </blockquote> 
  <p><b>InfoQ</b>: バンドルのロードはどのように動作するのでしょう – JARのように，バンドルを表現可能な標準フォーマットがあるのでしょうか？</p> 
  <blockquote> 
   <p><b>Zelzer</b>: CppMicroServicesが優れているのは，処理を完全にOSにまかせている点です。ですからLinuxでは，バンドルのフォーマットは “ELF Shared Object”(staticも可能です)であり，Windowsならば，例えば “PE”(Portable Executive, .dllや.exeファイルのフォーマット)が使用されます。ローディングはOSの動的リンカが実行します。</p> 
  </blockquote> 
  <p><b>InfoQ</b>: CPP Micro Servicesがサポートしているプラットフォームは何ですか？</p> 
  <blockquote> 
   <p><b>Zelzer</b>: 標準的なC++ 98で記述されていますから，それに準拠したC++コンパイラのあるプラットフォームならば，コンパイルは可能なはずです。テストはLinux, Windows, MacOS上で，さまざまなバージョンのコンパイラを使って行っています。</p> 
  </blockquote> 
  <p><b>InfoQ</b>: OSGi NativeプロポーザルやApache Celixとはどのような関係なのでしょう？</p> 
  <blockquote> 
   <p><b>Zelzer</b>: 私自身はCppMicroServicesプロジェクトを，サービスレイヤのネイティブC++ APIに関するフィールドテストだと思っています。ここでの経験は，私の参加しているNative OSGi APIの仕様策定プロセスでも役に立つはずです。</p> 
  </blockquote> 
  <p><b>InfoQ</b>: 現時点ではどこで，どのような利用をされているのですか？</p> 
  <blockquote> 
   <p><b>Zelzer</b>: Medical Imaging Interaction Toolkit (<a href="http://www.mitk.org">MITK</a>) では広範に使用していますから，それを利用するプロジェクトでも間接的に使用されていることになります。商業的な例では<a href="http://www.mint-medical.de">Mint Medical</a>があります。医療画像の分野でC++ソリューションを提供している会社です。航空電子や組み込みシステム，あるいはセーフティ・クリティカルなソフトウェアプロジェクトなどからも関心を持たれているようです。</p> 
  </blockquote> 
  <p>ネイティブOSGiの領域への関心は高い。ネイティブライブラリにおけるOSGi API標準化への要件を議論する場として，<a href="https://www.osgi.org/bugzilla/show_bug.cgi?id=165">RFP(Request For Proposal)156</a> が存在する理由もそこにある。読者はネイティブコードでのOSGi APIの利用に興味をお持ちだろうか？</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
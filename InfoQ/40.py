<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>C++によるiOSとAndroidでのクロスプラットフォーム開発：Dropboxの教訓</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/dropbox-cpp-crossplatform-mobile"><em>原文(投稿日：2014/05/28)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Dropboxの開発者が、最近、アプリをiOSとAndroidの両方でそれぞれのプラットフォームごとにすべてを書き直すことなくサポートする方法についての講演をいくつか行っている。以下、そのアプローチをとることになった理由、それがもたらす恩恵、そのプロセスを通じて得られるいくつかのキーポイントについて再点検してみよう。</p> 
  <p>Dropboxの開発者として数ヶ月前に<a href="https://www.youtube.com/watch?v=S5rXCvu9-NM">Stephen Poletto氏とSean Beausoleil氏はFacebookの開発者の前で行った講演において</a>、iOSとAndroidで別々のコードベースを持つことはいくつかの欠点がある、と述べている:</p> 
  <ul> 
   <li>開発コストや維持コストが倍になる。</li> 
   <li>チームが複数回同じバグを書き、修正することになる。</li> 
   <li>バグは片方のプラットフォーム向けにのみ報告され、もう一方では気づかないままになりかねない。</li> 
   <li>アプリの挙動に、微妙かつ望まない違いが出る。</li> 
   <li>パフォーマンスの最適化が高コストになり、プラットフォーム特有のものになる。</li> 
  </ul> 
  <p>これらの課題を克服するためのDropboxの戦略の要は、データやネットワークロジックなどの非UIコードすべてに対して共通のC++クロスプラットフォームライブラリを構築したことだ。UIそのものはネイティブコードで作られており、それにより、アニメーション、デバイスセンサーなどのプラットフォームのサポートを完全に活用でき、完全な反応性を確保できるようにしている。</p> 
  <p>その2人の開発者はこのアプローチをボトムアップと表現している。これは、より抽象的な言語、たとえばHTML5やJavascriptを使うことを好むトップダウンアプローチに対する言い方である。このようなアプローチは多くの場合期待するパフォーマンスを提供することができない、とPoletto氏とBeausoleil氏は言う。</p> 
  <p>一方で、C++はiOSでうまくサポートされていて、容易に<a href="http://en.wikipedia.org/wiki/Objective-C#Objective-C.2B.2B">Objective-C++</a>コードと混ぜることが可能である。さらに、C++はAndroidアプリにおいても、iOSアプリほど簡単ではないにせよ、<a href="http://www.ntu.edu.sg/home/ehchua/programming/android/Android_NDK.html">Android Native Development Kit</a> （NDK）を通じて利用することが可能である。</p> 
  <p><a href="http://www.uikonf.com/">UIKonf 2014</a>において、Mailboxアプリの開発者Steven Kabbes氏は、Dropboxの開発者がGoogleのメタビルドシステム<a href="https://code.google.com/p/gyp/">gyp</a>を活用してNDKの複雑さにどのように対処しているかについて説明した。gypはでXcodeプロジェクト、AndroidやUnixのmakefile、Visual Studioプロジェクトを<a href="https://github.com/skabbes/mx3/blob/develop/mx3.gyp">JSONによる記述</a>から生成することができる。そして、Steven氏はDropboxで使われているクロスプラットフォームテクニックを紹介するための<a href="https://github.com/skabbes/mx3">GitHubプロジェクト</a>も公開した。</p> 
  <p><strong>C++レイヤーのデザイン</strong></p> 
  <p>DropboxのC++クロスプラットフォームレイヤーは次の要素を含むシンプルなアーキテクチャを持つ:</p> 
  <ul> 
   <li>SQLiteデータベース。&quot;真実の源&quot;としての役割を持つ。</li> 
   <li>同じスレッド内で動く同期サービス。DropboxサーバとローカルSQLiteデータベースの同期を保つことに責任を持つ。</li> 
   <li>オペレーションキュー。まだ実行されていない全てのユーザオペレーションを保持する。</li> 
   <li>オペレーションスレッド。キューからユーザーオペレーションを取り出し、Dropboxサーバに対してそれを実行することに責任を持つ。</li> 
  </ul> 
  <p>DropboxのC++クロスプラットフォームレイヤーの背後にある基本的な考え方は、このレイヤーとネイティブコードとの間に強力な境界をつくり出すことである。この意味することは、C++レイヤーとUIレイヤーはいかなるデータも共有されず、オブジェクトはレイヤーの境界を前後にまたぐ際にコピーされる、ということだ。このポリシーの主な利点は、並列処理を考える際に、この2つのレイヤーが独立していると考えられることであり、そのため特別なクロスレイヤーロッキングをまったく必要とせず、お互いを気にせずに並行処理を実施することができる。</p> 
  <p>DropboxのC++レイヤーの中心となるコンポーネントはSQLiteで作られたクエリーと永続化のフレームワークであり、それにより、Dropboxの開発者がiOSでCore Dataを使わなくて済むようにできる。このような決断はCore Dataそのものの問題によるものではない。実際、Core Dataは高速で強力である。Kabbes氏が言うには、この決断はもっぱらAndroid、iOS、Mac、そして将来的にはWindowsをサポートするという要求によるものである。このコンポーネントはCore Dataの機能を完全に代替することを目的としたものではなく、永続化とクエリーの機能に、Kabbes氏がキーコンポーネントと考えているUI反応性を保証する機能を付与して提供するだけのものである。その機能は<code>NSManagedObjectContextObjectsDidChangeNotification</code>によって提供されている機能と同様のC++通知メカニズムであり、変更の差分を前後に送ることのみを可能にする。この永続化コンポーネントのさらなる詳細は<a href="https://github.com/skabbes/uikonf_coredata_talk">GitHub上にあるKabbes氏のノート</a>や<a href="http://oleb.net/blog/2014/05/how-dropbox-uses-cplusplus-cross-platform-development/">Ole Begemann氏の投稿</a>の中に見ることができる。</p> 
  <p>C++クロスプラットフォームレイヤーを設計する際の難しい決断の1つが、片方のOSがネイティブに提供している機能をいつ再実装するか、そして、いつそのラッパーを書くか、ということだ。Poletto氏に従えば、C++でプラットフォーム全体を実装し直すことはできない。そのため、ネットワークアクセスやSSL証明書検証などの基本機能はC++レイヤーからプラットフォームに単純に呼び返される。Ole Begemann氏はスクラッチから再実装するという選択を行わなかった例をいくつか挙げている。それは例えば、<code>NSURLSession</code>によるバックグラウンドダウンロード、アプリのバックグラウンドの振る舞い、iCloudアクセスなどである。他に、プラットフォーム特有のAPIで提供されている機能が再実装されている例も紹介している。そのようなものとして、<code>NSUserDefaults</code>のケースがあり、これはDropboxのコードでは<a href="https://code.google.com/p/leveldb/">LevelDB</a>で置き換えられている。</p> 
  <p>iOSプラットフォームとAndroidプラットフォームの間で1つのコードベースを共有することによって、他にもいくつかの恩恵がもたらされている、とPoletto氏は言う。まず第一に、ほとんど自明のことだが、iOSチームとAndroidチームの間にコラボレーションが増えるということがある。バグは早期にキャッチされ、両方のプラットフォームで同時に修正される。パフォーマンス最適化も両方のプラットフォームで同時に行われる。最後に、DropboxはAndroidベータテストプログラムを&quot;iOSコード&quot;のテストに利用することができ、App Storeレビュープロセスを待つことなく即座に修正を配信することができるという利点がある。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>なぜGerritはBuckを選んだのか</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/10/gerrit-buck"><em>原文(投稿日：2013/10/31)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>今日EclipseConでShawn Pearce氏(<a href="https://gerrit.googlesource.com/gerrit/">Gerritプロジェクト</a>のメンテナ)が，<a href="https://www.eclipsecon.org/europe2013/improve-your-java-builds-buck">Improve your Java Builds with Buck</a>と題する講演を行った (<a href="http://gerrit-talks.commondatastorage.googleapis.com/buck-rant.html">スライド</a>, <a href="http://gerrit-talks.commondatastorage.googleapis.com/buck-intro.html">追加スライド</a>)。これらの資料は，Gerritプロジェクトが<a href="https://gerrit.googlesource.com/gerrit/+/fd6bb9f6a5aa4c2b8ae64ce2e42fd5efaa0459c9">MavenからBuckへとスイッチ</a>した結果，Gerrit 2.8以降のビルドでは最終的にBuckのみを使用するようになった，その理由を説明したものだ。</p> 
  <p>Buckは，Google社内で使用されているビルドシステムの 'blaze' を基本モデルとしたビルドシステムで，現在はFacebookに所属する元Google社員の手で開発された。Facebookでありながら，このビルドシステムはApacheライセンスのオープンソースとして<a href="https://github.com/facebook/buck#readme">GitHubで公開されている</a>。BuckはPythonベースだが，GerritではおもにJavaのコンパイルに使用している。</p> 
  <p>Buckの言語はDSLの一種で，基礎となるビルドファイルにはPythonを使用する。下記に示すのは，ファイルシステム上の別の場所に配置されたGuavaを参照する '<code>printy_lib</code>' というJavaライブラリの定義である：</p> 
  <blockquote> 
   <pre><code> java_library(   name = 'printy_lib',   srcs = glob(['src/main/java/**/*.java']),   deps = [':guava'], )  prebuilt_jar(   name = 'guava',   binary_jar = 'guava.jar', ) </code></pre> 
  </blockquote> 
  <p>Gerritプロジェクトでは，JAR参照をMaven Centralで解決してローカルシステムに取得する機能を追加した。取得するJARファイルの内容は，GAVによる識別とSHA1のチェックサムを使ってダウンロード時に検証される。 これらの拡張機能は現在のBuckでは使用できないが，将来的には寄贈される可能性もある。</p> 
  <blockquote> 
   <pre><code> include_defs('//lib/maven.defs')  maven_jar(   name = 'guava',   id = 'com.google.guava:guava:14.0',   sha1 = '67b7be4ee7ba48e4828a42d6d5069761186d4a53',   license = 'Apache2.0', ) </code></pre> 
  </blockquote> 
  <p>Mavenに対してBuckが持つ明確なメリットは，その処理速度だ。それを実現する重要なアドバンテージがいくつかある。モジュールをまたいだビルドの並列実行はそのひとつだ。Buckのビルドでは，デフォルト値としてCPU数&times;1.25のスレッドを使用している(MavenやMakeも並列ビルドは可能だが，モジュール単位での並列性に制限される)。<a href="http://gerrit-talks.commondatastorage.googleapis.com/buck-rant.html#12">Gerritの速度改善として示されている</a>のは次の値だ:</p> 
  <ul> 
   <li><b>クリーンビルド</b> <pre>
mvn package -Dmaven.{javadoc,test}.skip=true  ... 6分50秒
buck build :gerrit                            ... 2分 3秒
buck test --all                               ... 2分 5秒
</pre> </li> 
   <li><b>No-op インクリメンタル・リビルド</b> <pre>
mvn package -Dmaven.{javadoc,test}.skip=true  ... 4分44秒
buck build :gerrit                            ...     2秒
</pre> </li> 
   <li><b>buckdがバックグラウンドで実行されている場合はさらに高速に動作する</b> <pre>
~/buck/bin/buckd
time buck :gerrit                             ...    0.5秒
</pre> </li> 
  </ul> 
  <p>デフォルトでマルチスレッドがサポートされている以外にも，Buckはインクリメンタルビルドやコンパイル対象を変更されたクラスに限定するなどの方法で，コンパイル速度を向上している。更新されたソースファイルの検出には，ファイルシステムのタイムスタンプ(すべてのシステムで信頼性があるとは限らない)ではなく，最終コンパイル時をベースとしたSHAによる内容比較を用いている。ビルドファイルのハッシュ値も取得しているので，ビルド定義が変更された場合にはすべてのファイルが再コンパイルされる。</p> 
  <p>BuckにはJavaの依存関係に関する詳細な情報も組み込まれている。相互依存関係にあるクラスのビルド方法や，内部メソッドではなく公開されたAPIの変更時にのみ依存関係によるコンパイルを実施する処理などを実現する。</p> 
  <p>ローカルシステム上でビルド用のコンテントを共有するのと同様に，BuckをApache Cassandaストレージシステムに接続することで，複数の開発者によるライブラリ共有を許可することも可能だ。これは構築済，あるいは旧バージョン用のコンポーネントをダウンロード可能なリポジトリ機構として動作する。必要なコンポーネントが何かを解決する処理は，Buckビルドシステムが実行する。これによって問題の切り分けが簡単にできるようになると同時に，毎回ビルド処理を行うことなく，過去のビルドからの資産を解析することが可能になる。コンテンツはハッシュされているので，アップデートされていないバージョンや公開されていないバージョンも利用可能だ。</p> 
  <p>処理速度の向上は，より柔軟な開発作業を可能にする。ビルドが１秒以内に実行可能なため(Gerritデーモン実行時)，Gerritの開発ビルドでは開発モードで実行されていることを検出して，HTTP要求ごとにリビルドとリロードを起動するようなことが可能になる。これによって非常に短いターンアラウンドでのパッチ提供が可能になり，開発時にリビルドやデプロイのために数秒あるいは数分を待つ必要がなくなる。</p> 
  <p>Buckは開発中であるため，Gradleが提供しているコミュニティや資料に比べれば不足する部分もある。最後に，BuckはJavaで記述されているが，DSLとしてはPythonを使用する。また，テストはおもにMacとLinuxマシンで実施されている。これはつまり，現時点ではWindowsサポートの優先順位が低いことを意味する。</p> 
  <p>Buckに関する詳細な情報は，<a href="http://facebook.github.io/buck/">FaceBookのBuckを紹介したページ</a>を参照してほしい。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
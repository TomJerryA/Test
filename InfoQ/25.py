<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Parse、iOSとAndroid用の低レベルライブラリ集、Boltsを発表</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/parse-announces-bolts"><em>原文(投稿日：2014/02/10)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Parse（<a href="https://developers.facebook.com/blog/post/2013/04/25/welcoming-parse-to-facebook/">数ヶ月前にFacebookが買収</a>）がAndroidとiOS用の低レベルライブラリをまとめて、Boltsと名づけてオープンソース化した。Parseの発表によると、BoltsはParse/Facebookの共同成果であり、両社が独自に開発してきた小さな低レベルのユーティリティクラスを固めたものだ。</p> 
  <p><a href="https://github.com/BoltsFramework">GitHubで公開された</a>最初のBoltsコンポーネントはTasksで、<a href="http://www.promisejs.org/intro/">JavaScript Promiseモデル</a>にしたがった非同期操作を目的としている。</p> 
  <p>Promiseは<a href="http://www.promisejs.org/intro/">コールバックを使って非同期操作を処理するときによく見られる数々の問題</a>、特に複数のシリアルあるいはパラレルな非同期操作をやろうとすると、コールバック内で非同期操作をネストするせいですぐに面倒なことになるという問題を解決しようとしている。</p> 
  <p>この目的のために、Promiseは完了するかもしないかもしれない、最終的にエラーになるおそれもあるタスクの結果を表現するもので、非同期操作はその実行結果として即座にPromiseを返すことができる。Promiseはいつでもアクセスすることができ、非同期操作がまだ完了していなければブロックすることができる。</p> 
  <p>通常、Promiseには2つのコールバック、非同期タスクが完了したときに呼ばれるコールバックと失敗したときに呼ばれるコールバックを関連付ける。Promiseの独特なところは、コールバック自体がPromiseにカプセル化されていることだ。もとのPromiseで起こることに依存して、コールバックは将来のある時点で実行されるか、あるいはまったく実行されないことになる。</p> 
  <p><img src="http://www.infoq.com/resource/news/2014/02/parse-announces-bolts/en/resources/promise-chaining.png" alt="" _href="img://promise-chaining.png" _p="true" /></p> 
  <p>上の図にあるように（出典: <a href="http://www.slideshare.net/drprolix/promises-16473115">Promises, Luke Smith</a>）、この仕組みのおかげで、Promiseをつなげて非同期操作とそのコールバックを表現することができるので、一連の非同期操作は扱いやすくなる。</p> 
  <p>Promiseのもう1つの利点は、Promiseのチェーンをエラーが伝搬するところにある。Promiseはそれが満たされたか否かを知っており、エラーハンドラが見つかるまでエラー状態はPromiseのチェーンを伝播することになる。そのため、チェーンに含まれる非同期操作ごとにエラーハンドラを用意する必要はない。</p> 
  <p>Promisesの実装は<a href="http://www.infoq.com/articles/surviving-asynchronous-programming-in-javascript">JavaScript</a>、<a href="http://www.infoq.com/presentations/Asynchronous-Scala-Java">Scala</a>、<a href="http://dev.clojure.org/display/design/Promises">Clojure</a>など、多数の言語で利用できる。</p> 
  <p>Parseによると、Tasksには<a href="https://github.com/BoltsFramework/Bolts-Android">AndroidのAsyncTask</a>や<a href="https://github.com/BoltsFramework/Bolts-iOS">iOSのNSOperation</a>よりも、さまざまなメリットがあるという。</p> 
  <ul> 
   <li>複数のタスクを連続実行をしても、コールバックのみを使った場合に起こるネストされた「ピラミッド」コードにはならない。</li> 
   <li>Tasksは完全に構成可能であり、分岐、平行処理、複雑なエラーハンドリングが実行できる。</li> 
   <li>タスクベースのコードを実行される順番に並べることができ、ロジックをコールバック関数に散らばらせる必要がない。</li> 
  </ul> 
  <p>BoltsコンポーネントはParseやFacebookのサービスとはまったく関係がなく、利用するのにParseやFacebookの開発者アカウントは必要ない。</p> 
  <p>さらなるBoltsコンポーネントが発表されているが、Parseはまだ詳細をリリースしていない。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>LocalForageでアプリケーションのオフライン対応を行う</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/localforage-offline-data-web"><em>原文(投稿日：2014/02/26)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Mozilla財団が<a href="https://github.com/mozilla/localForage">localForage</a>をリリースした。localForgeは、Webアプリケーションのオフラインデータをシンプルに保存できるようにする、新しいJavaScriptライブラリである。</p> 
  <p>最近のブラウザの技術ではないにも関わらず、<a href="http://www.html5rocks.com/en/tutorials/offline/whats-offline/#toc-html5-offline-storage">選択肢の多さ</a>から、オフライン対応は常に統一感のない状態であった。このライブラリをユニークなものにしているのは、最新のクライアントサイド技術の特徴である非同期性とBlob対応という両方の長所を、シンプルなAPIとして組み合わせようとしている事である。このライブラリは、Webアプリケーションに強力なオフライン機能を提供する。そして、Webアプリケーションをモバイルのネイティブアプリケーションと同等の存在に近づけ、開発者の作業をより直感的にしている。</p> 
  <p>最初の選択肢のひとつであった<a href="http://www.w3schools.com/html/html5_webstorage.asp">localStorage</a>は、オフラインの保存領域に対するシンプルなデータアクセスを提供した。しかしながら、その遅さ、同期性やバイナリのBlobが扱えない（例えば、mp3ファイルのキャッシュができない）ことが<a href="http://calendar.perfplanet.com/2011/localstorage-read-performance/">ベンチマークテスト</a>によって示されている。それ以来、評判の良い他の2つの選択肢―<a href="https://developer.mozilla.org/en-US/docs/IndexedDB">IndexedDB</a>と<a href="http://html5doctor.com/introducing-web-sql-databases/">Web SQL</a>―が登場してきた。これらは非同期性を持ち、高速であり、そして多くのデータセットをサポートしている。これら２つの技術の難点は、APIの使用方法があまりシンプルではないということと、どちらも<a href="http://csimms.botonomy.com/2011/05/html5-storage-wars-localstorage-vs-indexeddb-vs-web-sql.html">すべてのメジャーなブラウザでサポートされているわけではない</a>ということである。</p> 
  <p>直近のlocalForgeのリリースは、統合された技術を用いてこれらの問題を打開しようとしている。すなわち非同期性と、とてもシンプルなlocalStorageのシンタックスを用いた、IndexedDBとWeb SQLのBlobサポートである。</p> 
  <pre><p>var settings = {color: 'black', font: 'Helvetica'};   <br />localForage.setItem('settings', settings, function(result) {   <br />&nbsp;&nbsp;console.log(result);   <br />});</p></pre> 
  <p>IndexedDBとWeb SQLのサポートを含めることにより、localStorage単体よりも多くのWebアプリケーションのデータ保存が可能となる。また、APIのノンブロッキングという性質は、get/setのコールにおいて、メインスレッドからの応答がなくならないようにする。そのため、Webアプリケーションをより高速化するのである。さらに、localForgeはコールバックと<a href="http://www.promisejs.org/">ES6 Promises</a>をサポートしており、開発者にとって最適な実装方法を選べるようにしている。</p> 
  <p>このライブラリはIndexedDB、Web SQLそしてlocalStorageのドライバの自動読み込みと管理を行うので、手動でドライバを扱う必要がない（Webアプリケーションを動かしているブラウザに関係なく、最適なドライバが選ばれる）。IndexedDBもWeb SQLも利用できない場合、localForageはlocalStorageを代わりに使用するため、少なくとも基本的なデータはオフラインに保存することができる（しかし、Blobのサポートはなく、パフォーマンスはより遅くなる）。</p> 
  <p>localForageはすべてのモダンブラウザをサポートしている。非同期のデータ保存はすべてのブラウザで利用可能であり、以下の一覧のカッコの中は 該当する localStorageのサポートバージョンである。</p> 
  <ul> 
   <li>Android Browser 2.1</li> 
   <li>BlackBerry 7</li> 
   <li>Chrome 23 （localStorageはChrome 4.0以降）</li> 
   <li>Chrome for Android 32</li> 
   <li>Firefox 10（localStorageはFirefox 3.5以降）</li> 
   <li>Firefox for Android 25</li> 
   <li>IE 10（localStorageはIE 8以降）</li> 
   <li>IE Mobile 10</li> 
   <li>Opera 15（localStorageはOpera 10.5以降）</li> 
   <li>Opera Mobile 11</li> 
   <li>PhoneGap/Apache Cordova 1.2.0</li> 
   <li>Safari 3.1</li> 
  </ul> 
 </div> 
</div><br><br><br><br><br><br></body></html>
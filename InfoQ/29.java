<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Going Offline with LocalForage</h3><p>The Mozilla Foundation has released <a href="https://github.com/mozilla/localForage">localForage</a>, a new JavaScript library that promises to simplify the process of storing offline data in web applications.</p>
<p>Although it's not a recent browser technology, offline support has always been too fragmented because of the <a href="http://www.html5rocks.com/en/tutorials/offline/whats-offline/#toc-html5-offline-storage">many choices available</a>. What makes this library unique is the fact that it tries to combine the best of both worlds: the features of some more recent technologies (asynchronism and blob support) with a simple API. This offers a powerful offline capability to web applications, making them closer to their mobile native counterparts and more intuitive for developers to work.</p>
<p>One of the first choices available was <a href="http://www.w3schools.com/html/html5_webstorage.asp">localStorage</a> which provided a simple data access for offline storage. However <a href="http://calendar.perfplanet.com/2011/localstorage-read-performance/">benchmark tests</a> have shown it to be slow, it's synchronous and it cannot handle binary blobs (for example, no mp3 files caching is possible). Since then, two other popular choices have emerged - <a href="https://developer.mozilla.org/en-US/docs/IndexedDB">IndexedDB</a> and <a href="http://html5doctor.com/introducing-web-sql-databases/">Web SQL</a> - which are asynchronous, fast, and support large data sets. The drawback of these two technologies is the fact their APIs aren't very simple to use and neither are <a href="http://csimms.botonomy.com/2011/05/html5-storage-wars-localstorage-vs-indexeddb-vs-web-sql.html">supported in all major browsers</a>.</p>
<p>The recently release of localForage tries to overcome these problems by unifying technologies – asynchronism and blob support from IndexedDB and Web SQL with the very simple localStorage syntax:</p>
<pre><p>var settings = {color: 'black', font: 'Helvetica'};   <br />localForage.setItem('settings', settings, function(result) {   <br />&nbsp;&nbsp;console.log(result);   <br />});</p></pre>
<p>The inclusion of IndexedDB and Web SQL support allows one to store more data for the web applications than localStorage alone would allow. The non-blocking nature of their APIs makes the web applications faster by not hanging the main thread on get/set calls. Additionally, localForage supports callbacks and <a href="http://www.promisejs.org/">ES6 Promises</a> leaving the choice of the best implementation to the developer.</p>
<p>The library automatically loads and manages the drivers for IndexedDB, Web SQL and localStorage so one don’t need to handle this manually (the best driver is chosen independently the browser where the application is running). When neither IndexedDB nor Web SQL are available, localForage falls back to localStorage so at least basic data can be stored offline (though with no blob support and much slower).</p>
<p>All modern browsers are supported by localForage. Asynchronous storage is available in all browsers, with their version that supports localStorage in parentheses:</p>
<ul> 
 <li>Android Browser 2.1</li> 
 <li>BlackBerry 7</li> 
 <li>Chrome 23 (Chrome 4.0 with localStorage)</li> 
 <li>Chrome for Android 32</li> 
 <li>Firefox 10 (Firefox 3.5 with localStorage)</li> 
 <li>Firefox for Android 25</li> 
 <li>IE 10 (IE 8 with localStorage)</li> 
 <li>IE Mobile 10</li> 
 <li>Opera 15 (Opera 10.5 with localStorage)</li> 
 <li>Opera Mobile 11</li> 
 <li>PhoneGap/Apache Cordova 1.2.0</li> 
 <li>Safari 3.1</li> 
</ul><br><br><br><br><br><br></body></html>
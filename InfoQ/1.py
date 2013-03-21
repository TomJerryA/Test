<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ネイティブのPHP4拡張モジュールをマネージド版で置き換え</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Phalanger-Managed;jsessionid=9591697275DA27229CB837F0F1421143"><em>原文(投稿日：2013/03/13)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://phalanger.codeplex.com/releases/view/103021">Phalanger</a>、.NET と Mono用のPHPランタイムは、重要なマイルストーンに達し、11の人気のあるPHP拡張機能を.NET同等版で置き換えた。これらの拡張機能は、以前、ネイティブのCあるいはC++で書かれており、 Phalangerは32ビットモードでしか走らない、という制限があった。</p> 
 <p><a target="_blank" href="http://www.php-compiler.net/blog/2013/phalanger-3-0-updates-for-march-2013">Phalanger 3.0に含まれるマネージドライブラリ</a>のリストが以下である。</p> 
 <ul> 
  <li>Class Library (PhpNetClasslibrary.dll)は、 Phalangerの基本部分で機能の基本セット（標準、コア、セッション、ctype、トークナイザ、日付、pcre、ereg、JSON、ハッシュ、SPL、フィルタ) を含む。</li> 
  <li>cURL（新規） - 最も一般的なタスクのために、Phalanger は、HTTP / HTTPSプロトコルをサポートし、cURL拡張モジュールが付属している。コミュニティは、必要に応じて自由にその機能を拡張できる。</li> 
  <li>GD2, exif とimage （新規）はよく知られたPHP拡張モジュールで、イメージの読み込み/操作ができる。</li> 
  <li>Iconv （新規）は、.NET Encoding上に構築された文字列変換用である。</li> 
  <li>MSSQLは Microsoft SQL拡張モジュールで、内部で SqlConnectionを使ってパフォーマンスを上げている。また最新の Microsoft SQLとの互換性が保証されている。</li> 
  <li>PDO（新規）は、PHPデータベース接続を抽象化している。PDOのサポートが追加され、SQLiteやMySQLのようないくつかのDBドライバを含んでいる。開発者は、自由に追加のDBドライバを使って、PDOサポートを拡張できる。</li> 
  <li>SoapClient （新規）は、.NET 組み込みの SOAPサポートを利用した PHP SOAPのマネージドによる再実装である。</li> 
  <li>SQLite（新規）は、Phalangerの別のDB拡張モジュールである。</li> 
  <li>Phalanger のMySQL拡張モジュールは、最新のマネージドOracle / .NETコネクタを利用している。これによって、標準の.NETのやり方で追加のオプションやセキュリティオプションを設定することができ、DBの操作がより速く、より安全になる。</li> 
  <li>XML（新規）拡張モジュールも Phalangerに含まれた。このあるべき拡張モジュールはutf8関数で共通に使われる。</li> 
  <li>XMLDOM拡張モジュールは、PHPのSimpleXML、DOM、XSL、libxml拡張機能をサポートしている。その機能セットはlibxml関数や改良されたHTMLパーシング関数によって拡張された。この拡張モジュールは、素晴らしいパフォーマンスとセキュリティを提供する.NETのXML組み込みサポートを利用している。</li> 
  <li>Zip（新規）拡張モジュールは、コミュニテイの貢献で追加された。とにかく、完成にはまだ幾つかの作業が必要である。</li> 
  <li>Zlib（新規）拡張モジュールは、主にそのgzip圧縮サポートのために、多くのPHPプロジェクトの本質的な部分である。 Phalangerに含まれた。</li> 
 </ul> 
 <p>これらのライブラリは、C#で実装されているので、理論的には、他の.NETベースの言語でもこれらのライブラリを使うことができる。そして<a target="_blank" href="http://phalanger.codeplex.com/">Apacheライセンスの元でリリースされている</a>ので、必要な部分のみを抽出することができる。</p> 
 <p>バイナリ数形式やboolval()のような追加のPHP 5.xフィーチャも含まれている。関数呼び出し配列の逆参照が動いているが、尚実験レベルである。</p> 
 <p>もし知らなければ、 Phalanger Tools for Visual Studioも最近アップデートされた。1月にリリースされ、インテリセンスの改善、領域の折り畳み、定義への移動、クラスビューとオブジェクトウィンドウのサポートが含まれている。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
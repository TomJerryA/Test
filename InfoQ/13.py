<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Casablancaの C++ SDKがオープンソースに</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/casablanca;jsessionid=E086FF70EDFA89E59BD968F98D9C5EC0"><em>原文(投稿日：2013/03/01)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p style="margin-bottom: 0in" lang="zxx">Microsoftの C++ REST SDK、コードネームが<a target="_blank" href="http://casablanca.codeplex.com/">Casablanca</a>、が Apacheライセンスのもとでオープンソースされた。「現代的な非同期のC++　API設計を使って、クラウドベースのクライアント－サーバー通信をネイティブコードでサポートするMicrosiftの成果」と、説明されている。高レベルな記述をせずに、この製品は、C++11を使って、Microsoftが望む、クライアント側のHTTPコードを書くための、より簡単な方法を提供する。</p> 
 <p style="margin-bottom: 0in" lang="zxx">&nbsp;</p> 
 <p style="margin-bottom: 0in" lang="zxx">Casablancaは、マルチプラットフォームであり、Windows 7と Windows 8と同様にLinuxをサポートしている。Microsoftの開発者である Artur Laksberg氏は、WinXPとVistaのサポートも開発中である、と述べている。もう一つ特筆すべきことは、非同期操作のサポートです。Microsoftの<a target="_blank" href="http://blogs.msdn.com/b/vcblog/archive/2013/02/26/the-c-rest-sdk-quot-casablanca-quot.aspx">発表</a> は、Casablanca の実際の動きを示すために、HTTPを介したファイルのアップロードやJSONオブジェクトの作成の例を幾つか提供している。</p> 
 <p>&nbsp;</p> 
 <p style="margin-bottom: 0in" lang="zxx">Windows とLinuxの両方のビルドは、以下のフィーチャをサポートしている。</p> 
 <blockquote> 
  <ul> 
   <li>HTTPクライアント経由でサーバーへの接続を生成し、リクエストを送り、応答を処理する機能。</li> 
   <li>Uniform Resource Identifiers (URI)の構築と使用をサポート。</li> 
   <li>JSONの値を構築、パース、シリアライズする。</li> 
   <li>Streams とStream Buffersを介してバイトを元にあるメディアへ/から非同期に書き/読みする。</li> 
  </ul> 
 </blockquote> 
 <p style="margin-bottom: 0in" lang="zxx">幾つかの異なる Streams とStream Buffersが使える：メモリーベースのプロデューサー－コンシューマ、ファイル、STLコンテナによるメモリーベースのストリーム、生ポインターストリーム、相互運用ストリーム。この最後のタイプのストリームによってできるようになるのは、「...Casablanca は、２セットのクラスを提供する。その１つは、 iostreamへの非同期のストリームインターフェースを与え、もう１つは、非同期ストリームへの iostreamインターフェースを与える。」</p> 
 <p style="margin-bottom: 0in" lang="zxx"><a target="_blank" href="http://casablanca.codeplex.com/wikipage?title=Linux Features&amp;referringTitle=Documentation">Linux httpクライアント</a>には、若干の制限があり、https、プロキシ、認証をまだサポートしていない。しかし、Microsoftは、これらのフィーチャは将来のリリースでサポートされる、と言っている。 CodePlexには、<a target="_blank" href="http://casablanca.codeplex.com/SourceControl/changeset/view/8737b35e9171#readme.txt">Casablancaのソースコード</a>があり、最新のスナップショットをオンラインで見ることもできるし、Gitで入手するか、Zipアーカイブをダウンロード出来る。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
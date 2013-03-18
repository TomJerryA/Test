<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Xamarinが iOS と Android向けのC#非同期を導入</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/async-xamarin;jsessionid=0BFEE16C2C2988D59D362249EB10FFB2"><em>原文(投稿日：2013/03/12)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Xamarinは、iOS and Android開発向けの非同期対応ライブラリのプレビューをリリースした。この成果は、Visual Studio 2012の一部として昨年リリースされた Microsoftの .NET 4.5に大きく基づいている。 Xamarinは、以前はAndroid用の MonoTouch と Monoとして知られていた開発プラットフォームの新名称である。</p> 
 <p><a target="_blank" href="http://www.infoq.com/news/2013/02/Xamarin-2;jsessionid=9BBAAF6D2685C01CBEEB8572A16ECCA0;jsessionid=0BFEE16C2C2988D59D362249EB10FFB2">Xamarin 2.0</a>イニシアチブの一環として、モバイルプラットフォームは、 Mono と .NETにあるクラスライブラリを採用している。以前、Android用の MonoTouch と Monoは、Silverlight/Moonlightベースのサブセットに制限されていた。<a target="_blank" href="http://blog.xamarin.com/brave-new-async-mobile-world/">Rodrigo Kumpera</a>氏は書いている。</p> 
 <blockquote> 
  <p>非同期処理がこのリリースの主要テーマだが、7000以上のコミットによる、Monoランタイムへの2年間の改善が詰め込んでいます。それらを Android, Mac、iOSのユーザーが使えるようになりました。</p> 
 </blockquote> 
 <p>このリリースは、またiOSバッチコンパイラーにも改善をもたらしている。他の殆どのプラットフォームと違い、iOSはJITコンパイルされたコードを許可しない。これは、動的に起動されるコードで特にジェネリックスが関与した場合に問題となる。</p> 
 <blockquote> 
  <p>iOS上で、我々は値型に対して「共有可能なコード」を生成できるようになりました。これはコード生成技術における真に革命的な革新です。実用上、これが意味すことは、以前「JITコンパイル方式を試しています」で、クラッシュしたコード全体が動くようになった、ということです。我々は、尚推論できる、高パフォーマンスで、微調整した汎用コードを提供します。例えば、メソッド Foo&lt;T&gt;(T x)–への直接呼び出しでは、以前は失敗した動的ケースで、使うことができる Foo&lt;T&gt;(T x) の値型共有バージョンを生成します。かつて夢だったものが現実になりました。</p> 
 </blockquote> 
 <p>現在、 Microsoftの .NET 独自の JITコンパイラには、この機能はない。1つのメソッドを全ての参照型で共有し、ジェネリックなメソッドは、それぞれ個別の値型で再コンパイルする必要がある。</p> 
 <p><a target="_blank" href="http://msdn.microsoft.com/en-us/library/dd799517.aspx">共変と反変</a>のサポートが.NET 4.0で導入されたが、Xamarin プラットフォームでも存在する。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
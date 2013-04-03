<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>WCF Data Services 5.4.0－Atomペイロードにクライアントフックとインスタンスアノテーション</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/wcf-data-services-5-4-0;jsessionid=7925EF0BCAD7D8BC56968F2CB32DE45C"><em>原文(投稿日：2013/03/27)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://blogs.msdn.com/b/astoriateam/archive/2013/03/26/wcf-data-services-5-4-0-prerelease.aspx">Microsoft</a> は、<a target="_blank" href="https://nuget.org/packages/Microsoft.Data.Services/5.4.0-rc1">WCF Data Services 5.4.0</a>のリリース候補（プレリリース）バージョンをリリースしたが、クライアントのデシリアライズ、シリアライズフック、<a target="_blank" href="http://www.odata.org/documentation/atom-format/">atomペイロード</a>のインスタンスアノテーション、インスタンスアノテーションのクライント消費、更にAtomとJSONフォーマット間の簡単化されたトランジションがサポートされている。<br /> <br /> クライアントのデシリアライズとシリアライズフックは、ワイヤータイプやプロパティ名を変更するような幾つもの様々なシナリオを可能にする拡張ポイントを提供する。 新リリースは、例えば Atomペイロードのインスタンスアノテーションをサポートする。これはODataフィードの拡張フィーチャであり、ODataのリクエストとレスポンスがフィード、単一のエンティティとプロパティを対象にしたアノテーションをつけることができるようになる。<br /> <br /> WCF Data Services 5.4.0は、クライアントにAPIを追加し、インスタンスアノテーションがそれらを使用できるようした。また Preferヘッダーを介して、クライアントが関係するのがどのインスタンスアノテーション化を示す機能を提供している。このおかげで、odata.includeアノテーション プレファレンスを重要視するODataサービスからのレスポンスを効率化できる。またAtomと<a target="_blank" href="http://www.json.org/">JSON</a>フォーマット間の変換を簡単にする新機能も含まれている。<br /> <br /> WCF Data Services 5.4.0は、以下のシナリオにおける問題の解決を提供する、幾つものバグ修正を行なっている。</p> 
 <ul> 
  <li>もし新しいJSONフォーマットが使われ、タイプリゾルバーが提供されない場合、複雑な値のコレクションを読み込むと失敗する時があった</li> 
  <li>ODataLibはIDと編集リンクにおけるリテラル値をエスケープできなかった</li> 
  <li>application/json;odata=nometadataにしてサービスドキュメントをリクエストすると失敗する</li> 
  <li>タイプリゾルバー無しで新しいJSONフォーマットを使うと、派生型で問題を起こす</li> 
  <li>クライアント上のLINKプロバイダは、複合キーを持つ派生型でキー式ではなく$filter を生成する</li> 
  <li>WCF DS クライアントで、大文字と小文字を区別する照合を必要とするヘッダーがある</li> 
  <li>新しいJSONフォーマットをリクエストすると、Atomフォーマットを使ったエラーになることがある</li> 
  <li>OData v1/v2 ペイロードのPATCHリクエストが405ではなく500エラーを返す</li> 
 </ul> 
 <p>最新リリースでは、また<a target="_blank" href="http://odata.codeplex.com/wikipage?title=ODataLib">ODataLib</a>のカレント項目を追跡するのが簡単になり、 EntityStateとETagを設定できないために、幾つかの操作でわざわざエンティティをデタッチし、そしてアタッチしなければならない問題が修正されている。プレリリースバージョンは、また.NET Framework 4.0, Silverlight 4.0が対象で、幾つかの言語に既にローカライズされている。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
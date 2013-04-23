<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>JSONバリデーションのまとめ</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/JSON-Validation;jsessionid=53384B83D1B1BA3FD97EAFB8D2E9C654"><em>原文(投稿日：2013/04/15)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>どんな “柔軟な” すなわち “拡張性のある” ファイルフォーマットを作っても、遅かれ早かれ開発者のグループがバリデーションに関して文句を言い始める。多くがこのことに対処できるが、それらは以下のように分類できる。</p> 
 <ul> 
  <li>データが正しくフォーマットされていると仮定する。</li> 
  <li>手動で間違った形式のデータを確認し、修正しようとする。</li> 
  <li>手動で間違った形式のデータを確認し、適切なら拒否する。</li> 
  <li>間違った形式のデータを自動的に確認する。</li> 
 </ul> 
 <p>この記事の目的は、これらのオプションを議論することではなく、自動バリデーションに利用できるツールキットをまとめることである。</p> 
 <p><b>JSON スキーマ</b></p> 
 <p><a target="_blank" href="http://json-schema.org/implementations.html">JSON スキーマ</a> は、17 の異なるプロジェクトでサポートされている、提案された標準だ。JavaScript、Java、Python、Ruby、Perl、PHP、.NET、ActionScript、C、Haskell、および Erlang で利用できる。その形式は、実際のデータにほとんど似ていないスキーマを持つ VeriJSON よりも複雑だ。それはまた、数の範囲チェック、リストの制限、リストに重複したエントリを防ぐ事が出来る機能を持ち、もっと包括的である。また、<a target="_blank" href="http://json-schema.org/example2.html">他のスキーマへの参照</a>をサポートし、大規模なスキーマを小さなコンポーネントに分解することができる。</p> 
 <p><b>Atdgen </b></p> 
 <p>Atdgen は、OCamlで JSON のシリアル化および逆シリアル化をサポートしている。JSON のスキーマは、atd ファイルとして知られているものを使用して作成される。これらのファイルは、OCaml クラスファイルを生成するコードジェネレーターとオブジェクト/JSON コンバーターをマッチさせることで走る。Atdgen では、バリデーションは、逆シリアル化プロセス中に発生します。</p> 
 <p>atdファイル中のバリデーションルールは、オープンエンドで、開発者は、どんなOCamlコードでもatdファイルに直接注入できる。セカンダリースキーマファイルへの参照がサポートされている。</p> 
 <p><a target="_blank" href="http://mjambon.com/atdgen">Atdgen</a> は、オープンソースライセンスのもとで入手できる。</p> 
 <p><b>DataContractJsonSerializer</b></p> 
 <p>WCFの DataContractSerializerに基づいた<a target="_blank" href="http://msdn.microsoft.com/en-us/library/system.runtime.serialization.json.datacontractjsonserializer.aspx">DataContractJsonSerializer</a>は、クラス定義とデータコントラクト属性を使って、どのようにJSONファイルをバリデートし、最終的に逆シリアライズするかを決める。これは基本的タスクに適しているが、パフォーマンス問題が発生する傾向にあり、辞書の作成が困難である。バリデーションは、基本的な構造にかなり制限されている。</p> 
 <p><b>Json.NET </b></p> 
 <p>James Newton-King氏が作ったJson.NETは、今日入手できる中で最も包括的なJSON シリアライザ/逆シリアライザである。 DataContractJsonSerializerのようにJson.NETは、クラスを使ってスキーマを定義できる。標準のWCFデータコントラクト属性、あるいは<a target="_blank" href="http://james.newtonking.com/projects/json/help/index.html?topic=html/SerializationAttributes.htm">JSON.NETのシリアライズ属性</a>を使うことができる。DataTable と nHibernate のエンティティを含む様々なタイプをサポートしている。今月に<a target="_blank" href="http://james.newtonking.com/archive/2013/04/07/json-net-5-0-release-1-net-4-5-biginteger-read-only-collections.aspx">JSON.NET 5.0</a>は、無制限サイズの整数(BigIntegerを介して)とIEnumerable コンストラクタを公開するリードオンリーのコレクションをサポートする。</p> 
 <p>JSON.NETはまた、JSON スキーマを介して、バリデーションをサポートする。</p> 
 <p><b>VeriJSON</b></p> 
 <p>VeriJSONは、パターンベースのマッチングを使用したObjective-C ライブラリである。パターン自身がJSONで書かれており、サポートされている型は “number”, “string”, “bool”, “url”である。文字列は、正規表現を使って制限できる。urlは、スキーマ（例えば、http, ftp)によって制限できる。配列やオブジェクトは、構造的に表せ、オプションのプロパティがサポートされている。</p> 
 <p><a target="_blank" href="https://bitbucket.org/dcutting/verijson">VeriJSON</a> は、オープンソースライセンスの下で入手できる。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
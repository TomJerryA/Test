<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PostgreSQLで頑強なデータベース設計</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/02/solid-database-design;jsessionid=4D6FD81A63BF494F50CE725E85F8A3ED"><em>原文(投稿日：2013/02/26)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Chris Travers 氏は、最近「頑強なデータベースの構築」と題する一連の記事を発表した。彼は、いかに幾つかの共通のOOP原則、例えば単一責務の原則、インターフェースの分離、依存性の逆転をいかに適用して、データモデルやデータベースのコードを改善するかに関する幾つかの考えを説明している。アイデアの幾つかは、どのようなリレーショナルデータベースにも部分的に適用出来るが、 記事は、PostgreSQLのようなデータベースにあるテーブルの継承のようなオブジェクト・リレーショナル機能を含んだシナリオを紹介している。</p> 
 <p align="justify"><a target="_blank" href="http://ledgersmbdev.blogspot.in/2013/01/building-solid-databases-single.html">単一責務と正規化</a>で、氏は、データモデルとクラスモデル間の類似性と微妙な違いを説明している。正規化は、通常、純粋なリレーショナル・データベースでSRPを満たすのに十分であるが、テーブル継承は、さらにデータベース内の他のフィールドに依存している一般的共起フィールドを管理するために使用できる。彼は例を提供している。</p> 
 <blockquote> 
  <p align="justify">合成が大きな違いをもたらす共通のケースは、ノートの管理においてである。人々は、データベースにあるあらゆる種類の他のデータにノートを付けたいと思うかもしれない。そうなら、ノートのテキストすなわち件名が互いに依存している、と言うことはできない。</p> 
  <p align="justify">典型的な純粋なリレーショナル　アプローチでは、多くの独立に管理されているノートのテーブルを持っているか、あらゆるもののためのメモを格納する単一のグローバルノートテーブルを持っているかのどちらかで、次に複数の結合テーブルを持ち、結合依存関係を追加する。</p> 
  <p align="justify">オブジェクト・リレーショナル・アプローチでは、複数のノートのテーブルを持つようになるが、それらが共通なノートのテーブルのテーブル構造を継承しているだろう。</p> 
 </blockquote> 
 <p align="justify"><a target="_blank" href="http://ledgersmbdev.blogspot.in/2013/01/building-solid-databases-openclosed.html">オープン・クローズ原則 </a>では、ゴールは、ベースバージョンが変更された時に、拡張性を壊さずに、システムを拡張可能に保つことだろう。再び、テーブルの継承がデータモデルの拡張ポイントを提供する柔軟な方法を提供することができる。ここでの例は、いかに pg_message_queue 0.2は、各データ型をサポートする別々のテーブを持ち、全てのテーブルは共通のテーブルから継承させることによって、様々なデータ型を扱うことができるかを示している。氏は、またセキュアなAPIがセキュリティコントロールのために、拡張性を維持しながら、修正に対してクローズドでいるかを示す、別の簡単な例を提供している。</p> 
 <p align="justify"><a target="_blank" href="http://en.wikipedia.org/wiki/Liskov_substitution_principle">Liskov の置換原則</a> は、通常、純粋にリレーショナルデータベースの問題ではないが、テーブルの継承を使うと、<a target="_blank" href="http://ledgersmbdev.blogspot.in/2013/02/building-solid-databases-liskov.html">前面に出てくる事がある</a> 。ここにある例は、 my_rectangleテーブルを継承している my_squareテーブルである。</p> 
 <div align="justify"> 
  <pre>
CREATE TABLE my_rectangle ( id serial primary key, height  numeric, width numeric );
CREATE TABLE my_square ( check (height = width) ) INHERITS  (my_rectangle);</pre> 
 </div> 
 <p align="justify">そして my_rectangleを更新する。</p> 
 <div align="justify"> 
  <pre>
UPDATE my_rectangle SET height = height * 2</pre> 
 </div> 
 <p align="justify">すると、それが squareテーブルに参照の問題を引き起こし、失敗する。これに対処する方法は、いっぺんに更新するのを避ける（行をイミュータブルにする）か、 トリガーを使って、そのような更新の度に、my_squareから行を削除し、 my_rectangleに挿入するかのどちらかである。</p> 
 <p align="justify"><a target="_blank" href="http://en.wikipedia.org/wiki/Interface_segregation_principle">インターフェースの分離</a>が <a target="_blank" href="http://ledgersmbdev.blogspot.in/2013/02/building-solid-databases-interface.html">データベースに適用されるとき</a>は、主にユーザー定義の関数あるいはストアドプロシージャを伴うだろう。氏は、これらを基礎となるデータへのインターフェースとして考えており、理想的な関数ないしストアドプロシージャが最小限の周辺ロジックを持つ１つの大きなクエリを持つことを提案している。5つ以上のクエリあるいは、多数のオプションのパラメータが複雑性を減らすべきことの示唆となり、それらは、複数の別々の関数かストアドプロシージャ（それぞれは1つの特定の目的を持つ）に分解することで対処すべきである。再び、この原則は単一責務の原則と一緒に適用される。</p> 
 <p align="justify"><a target="_blank" href="http://ledgersmbdev.blogspot.in/2013/02/building-solid-databases-dependency.html">依存性の逆転と堅牢なDBインターフェース</a>では、氏は、アプリケーションロジックとストアドプロシージャ間の緊密な結合がいかに、脆弱な抽象に導くことになり得るかを説明し、2,3の潜在的解決策を提案している。それらのあるものは、サービスロケーターパターンに似たものを使い、ビューあるいは関数を使い、<a target="_blank" href="http://www.postgresql.org/docs/9.1/static/xtypes.html">カスタムなデータ型</a>、トリガー、通知を使っている。ここでの主要な提案は、様々なオプションを検討し、データベース自身を適当なAPIを公開しているアプリケーションとして設計することである。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
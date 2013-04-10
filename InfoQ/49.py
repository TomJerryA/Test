<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Martin Fowler氏が21世紀のソフトウェアデザインについて講演</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/software-design-21st-century;jsessionid=8D827ACCDE25E4D182CBC1861FCA1B01"><em>原文(投稿日：2013/04/02)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>スキーマレスなデータ構造がよく理解されていない。NoSQLデータベースでこれらのデータ構造を使用する際に、その長所と短所を考慮することは、重要だ。最近の会社のイベントで<a target="_blank" href="http://martinfowler.com/">Martin Fowler</a>氏は,スキーマレスデータ構造とNoSQL＆一貫性について<a target="_blank" href="http://www.youtube.com/watch?v=8kotnF6hfd8">話をした</a>。</p> 
 <p><strong>スキーマレスデータ構造:</strong></p> 
 <p>スキーマレスであることは、しばしばNoSQLデータベースの大きな利点として考えられている。マーティンはこの領域が十分に理解されていないと信じており、スキーマレスなデータ構造を使用することの何が長所と短所あるかばかりでなく、スキーマレスの様々な面を説明している。</p> 
 <p>重要な点は、スキーマレス構造であっても尚スキーマを持っているということだ。データをクエリして情報を検索するためには、データを理解する必要があり、それは<a target="_blank" href="http://martinfowler.com/articles/schemaless/">暗黙のスキーマ</a>、データの定義が例えばコードの中にある。対照的に、正しいデータのみが受理されるリレーショナル・データベース内のスキーマは、<a target="_blank" href="http://martinfowler.com/articles/schemaless/">明示的なスキーマ </a>である。</p> 
 <p>氏は、この話の終わりに、ほとんどは、<em>&quot;Implicit Schema == Bad Thing&quot;</em> で、明示的なスキーマを使って、データがどんなものか、明確に定義する方が良い。確かにスキーマレスが役に立つ場合が少々あるが。しかし彼は、またスキーマは、固定したストレージスキーマである必要はなく、データアクセス層やXMLスキーマのようなもっと契約の形をとってもよい、と言った。</p> 
 <p><strong>NoSQLと一貫性:</strong></p> 
 <p>この講演で、氏はNoSQLデータベースにおける一貫性の2つの側面について論じた。</p> 
 <p>１つのデータベースで開発している時、論理的一貫性がデータの一貫性の維持を取り扱う。殆どのNoSQLデータベース（グラフは1つの例外である）に対して、集合 （ドメイン駆動デザインから来た概念で、オブジェクトのクラスタを同時に保存する）の使用は、矛盾を回避する明白なやり方である。</p> 
 <p>幾つかの場所に同じデータをコピーすることで、レプリケーションの一貫性を保つ、話している時に、氏は<a target="_blank" href="http://en.wikipedia.org/wiki/CAP_theorem">CAP 定理</a>を持ちだした。ネットワーク上でデータが既に複製されていれば、それは一貫性と可用性の間の選択であると単純化した。彼が強調したのは、これは技術的な問題ではなく、一貫性と可用性のどちらを優先させるか、というビジネス上の選択だ、ということである。</p> 
 <p>氏は、ソフトウェアデザインの価値と技術的負債を議論する話で講演を締めくくった。</p> 
 <p>&nbsp;</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
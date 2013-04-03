<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>調査: もっとも表現力に富んだ汎用プログラム言語は Clojure，CoffeeScript，Haskell</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Language-Expressiveness;jsessionid=37B5C24E3A36443B8F41718FDD0F0D5A"><em>原文(投稿日：2013/03/28)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>ある調査によると，表現力のもっとも高い汎用プログラム言語は Clojure と CoffeeScript，そして Haskell なのだという。その調査では LoC /コミットを表現力の測定単位として採用している。</p> 
 <p>RedMonk の常勤 PhD である Donnie Berkholz 氏は、さまざまなプログラム言語の <a target="_blank" href="http://redmonk.com/dberkholz/2013/03/25/programming-languages-ranked-by-expressiveness/">表現能力を定量化する調査を</a>，<a target="_blank" href="http://www.ohloh.net/">Ohlol</a> の提供するデータに基づいて実施している。Ohlol は、およそ 100 の言語で２０年に渡って記述されてきた、500,000以上のオープンソースプロジェクトの記録を収めたリポジトリだ。</p> 
 <p>Berkholz 氏が表現力の計測単位として採用したのは LoC/コミットという値だ。その理由として氏は， &quot;コミットは一般的に、ひとつのコンセプトを追加するために使用されるものだから&quot; と付け加えている。調査の結果には保守性や生産性、あるいは作成されたコードの可読性や製作に要した時間の長さなどは反映されていない。</p> 
 <p>次図は50以上の言語の表現能力について、昨年始めに公表された <a target="_blank" href="http://redmonk.com/sogrady/2013/02/28/language-rankings-1-13/">RedMonks の言語ランク</a> に基づいた色分けで示したものだ： 赤 - もっとも採用数の多い言語、青 - ２番目に多いもの、黒 - ３番目 (クリックで拡大)。</p> 
 <p class="image-wide"><a href="/resource/news/2013/03/Language-Expressiveness/en/resources/Expresiveness-1.png;jsessionid=D3E0F8D6E95B48BB1DB543642E183B94;jsessionid=37B5C24E3A36443B8F41718FDD0F0D5A"><img alt="" _p="true" _href="img://Expresiveness-1.png" src="http://www.infoq.com/resource/news/2013/04/Language-Expressiveness/ja/resources/Expresiveness-1.png;jsessionid=37B5C24E3A36443B8F41718FDD0F0D5A" /></a></p> 
 <p>調査では多数のプロジェクト／言語を対象としているため、各言語の LoC/コミット値は分散している。したがって各言語の値としては、それらの平均値を採用する。言語はそれぞれの中央値でランク付けされている – ボックス内の黒い線が対応するプロジェクトのLoC/コミットの50%，ボックスの上下の線が25%と75%，ヒゲ線が10%と90%をそれぞれ示す。</p> 
 <p>Berkholz氏の結論は次のようなものだ。</p> 
 <blockquote> 
  <p>３番目のグループに属する言語は全般的に表現力が非常に高い。</p> 
  <p>関数型言語には表現力の高い傾向がある。</p> 
  <p>ドメイン固有言語は全般的に表現力が非常に高い。</p> 
  <p>コンパイルと表現力の低さに相関関係はない。</p> 
  <p>CoffeeScript (#6) は JavaScript (#51) よりもはるかに高い表現力を示している。事実上，すべての言語の中での最高値である。</p> 
  <p>Lisp系言語では Clojure (#7) の値がもっとも高い。</p> 
  <p>Go (#24) は話題を集めている言語だが，表現性では目立ってはいない。... にも関わらず，第１グループのすべての言語に勝っているのは，それらの言語の経験しか持たない開発者がGoを使って，改善された部分を感じているのかも知れない。</p> 
 </blockquote> 
 <p>&quot;３番目のグループに属する言語の表現力が非常に高い&quot; という結論には，それならばなぜもっと採用数が増えないのか，という点が疑問に思われる。言語の持つ簡潔さが，平均的なプログラマの理解や利用を難しいものにしている，ということなのだろうか？それとも他の理由だろうか？</p> 
 <p>Berkholz氏はまた，ボックスの高さから求めた表現力の一貫性をベースとしたランク付けも行っている。その結果が次のグラフだ (クリックで拡大)。</p> 
 <p class="image-wide"><a href="/resource/news/2013/03/Language-Expressiveness/en/resources/Expresiveness-2.png;jsessionid=D3E0F8D6E95B48BB1DB543642E183B94;jsessionid=37B5C24E3A36443B8F41718FDD0F0D5A"><img alt="" _p="true" _href="img://Expresiveness-2.png" src="http://www.infoq.com/resource/news/2013/04/Language-Expressiveness/ja/resources/Expresiveness-2.png;jsessionid=37B5C24E3A36443B8F41718FDD0F0D5A" /></a></p> 
 <p class="image-wide">氏が出した結論は，</p> 
 <blockquote> 
  <p>第１グループの言語はここでも強い位置にいる。</p> 
  <p>第１グループの言語は表現力の高低に関わらず，高い一貫性を持っている傾向がある。</p> 
  <p>このことは，第１グループに属する言語の主要な特性が，生産性よりも予見可能性であることを示唆している。</p> 
  <p>第３グループの言語は，ここでは見劣りしている。</p> 
  <p>今回はJavaが，&quot;エンタープライズ&quot;言語 (C，C++，Java) で最高のパフォーマンスを示している。</p> 
  <p>一貫性においても CoffeeScript が変わらず No.1 であるが，４番目の Clojure と比較した IQR (interquartile range，,四分位範囲) の差異はわずか23LOC/コミットに過ぎない。</p> 
 </blockquote> 
 <p>表現力の一貫性の結果と RedMonk言語人気ランクの２つから Berkholz氏は，Clojure と CoffeeScript，そして Haskell がもっとも表現力の高い汎用言語である，と結論付けている。氏の調査の一部は，<a target="_blank" href="http://www.drmaciver.com/">David R. Maclver</a>氏が <a target="_blank" href="http://en.wikipedia.org/wiki/Law_of_the_instrument">Hammer Principle</a> を通じて2,576人のプログラマを対象に行った <a target="_blank" href="http://hammerprinciple.com/therighttool/statements/this-language-is-expressive">別の調査</a> によっても裏付けられている。Maclver氏によると，もっとも表現力のある言語は Haskell，Clojure と Scala である。逆に表現力の乏しい言語が C，PHP，TCL であり，こちらの調査には CoffeeScript が含まれない。</p> 
 <p>Berkholz氏による <a target="_blank" href="http://redmonk.com/dberkholz/2013/03/25/programming-languages-ranked-by-expressiveness/#comments">元の記事</a> と <a target="_blank" href="https://news.ycombinator.com/item?id=5438755">Hacker News</a>，<a target="_blank" href="https://twitter.com/search/realtime?q=http%3A%2F%2Fredmonk.com%2Fdberkholz%2F2013%2F03%2F25%2Fprogramming-languages-ranked-by-expressiveness%2F&amp;src=typd">Twitter</a> への投稿には多数のコメントが寄せられた。LoC/コミットは言語の実際の表現力を表していない，可読性や保守性も考慮すべきだ，DSLは含めるべきではない，などといった意見が多い。</p> 
 <p>表現力の定量化にLoC/コミットを用いた理由について Berkholz氏は，この調査は言語の可読性や保守性に関するものではない，&quot;レポジトリ上のコード状態に関する何らかの指標，使用されている開発プラクティス，(バグとLOCの相関性を根拠として) 発生が予想される潜在的なバグのレベル&quot; を扱うものなのだと主張し，<a target="_blank" href="http://redmonk.com/dberkholz/2013/03/26/what-does-expressiveness-via-loc-per-commit-measure-in-practice/">別の記事</a> でその詳細を説明している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
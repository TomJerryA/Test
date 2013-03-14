<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>アジャイルで開発速度を上げるには</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/agile-faster;jsessionid=A610B0A19D9A67009A1415D1E4DAE9B9"><em>原文(投稿日：2013/03/07)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>企業がソフトウェア開発へのアジャイル導入を望む理由として挙げられるのが，提供までの期間の短縮だ。<a target="_blank" href="http://www.infoq.com/news/2012/11/success-agile-projects;jsessionid=57257481F1FEDC936677687EBB9D7D6B;jsessionid=A610B0A19D9A67009A1415D1E4DAE9B9">InfoQの記事(evidence of success of agile projects)</a> で取り上げた Columbus Agile Productivity Benchmark Project など，アジャイルプロジェクトの開発短縮を示す調査結果も発表されている。開発速度を向上するためには，アジャイルをどのように使えばいいのだろうか？</p> 
 <p>Matthew Heusser氏の &quot;<a target="_blank" href="http://news.idg.no/cw/art.cfm?id=1FFBF5B6-0806-32B0-91FADBB886D47464">Who says agile development can't be faster?</a> &quot; と題したブログ記事には，氏が Agile Testing Days カンファレンスで行った議論の内容が公開されている。</p> 
 <blockquote> 
  <p>2012年11月にドイツのポツダムで開催されたAgile Testing Daysにおいて，&quot;Agile Testing: A Practical Guide&quot; 著者のLisa Crispin，Janet Gregory両氏は，&quot;アジャイルとは迅速さである&quot; というのは誤りだ，という大胆な主張をしました。</p> 
 </blockquote> 
 <p>カンファレンス後にJanet Gregory氏が，その発言の意味について氏に説明してくれた。</p> 
 <blockquote> 
  <p>アジャイルで重要なのは速さじゃない，と彼女は言いました。副産物としてそうなのかも知れないが，今この瞬間はそうではない，と言うのです。(...) アジャイルに移行することで，少なくとも一時的には遅くなるはず – それも，１週間や２週間ではなく，場合によっては１年や２年になるかも知れません。</p> 
 </blockquote> 
 <p>これに対して氏は，アジャイルを使えば速くなると考える理由をいくつか挙げて反論する。そのひとつとして説明しているのが，なすべきことを行って実行する価値のない要件を省くことが時間の節約につながる，と言う点であり，もうひとつが &quot;古い手法はどれも速くない&quot; という理由だ。</p> 
 <blockquote> 
  <p>(...) アジャイルを始めて１年でまだ成果を上げていないチームと，それができている従来手法のチームとを比較するのが，そもそも間違っています。１年では，従来手法のチームでも何の成果も上げられないでしょう。12個半の要件を片付けて，やりかけの仕事が残るくらいがせいぜいです。</p> 
 </blockquote> 
 <p>両氏の意見に同意できない理由を述べた上で氏は，アジャイルがチームを迅速にすると思う理由を説明して，このブログ記事を結論付けている。</p> 
 <blockquote> 
  <p>ひとつの疑問が残ります: アジャイルは速いのでしょうか？両氏はそれを大した問題ではない，と主張するかも知れません。短期的に純粋なスピードに注目することは作業のショートカットにつながり，長期的に見れば苦痛とパフォーマンス低下をもたらすことになる，と言うのです。しかし私は，無駄を取り除くことに注力して速度を向上し，プロセスを改善することは可能だと信じています。</p> 
 </blockquote> 
 <p>Chris Turner氏は <a target="_blank" href="http://skipoleschris.blogspot.nl/2012/07/making-agile-go-fast.html">Making agile go fast</a> と題するブログ記事で，アジャイルプロジェクトのパフォーマンスが上がらない理由について考察している。氏はそこで頻繁に見られる４つの原因を指摘し，それらに対処する方法を紹介する。</p> 
 <ul> 
  <li>不適切なメンバ – エンジニアとしての規律に従えない，あるいは物事を複雑にしようとするような人たちを，チームから除外すること。</li> 
  <li>プロセスの優先 – オープンなコミュニケーション，自己組織化，権限を持ったチームを確立すること。</li> 
  <li>誤った技術の適用 – チームに技術決定権を与えるとともに，デリバリの障害となる技術選択の破棄を許可すること。</li> 
  <li>複雑過ぎるアーキテクチャ – リファクタによってソフトウェアを可能な限りシンプルに保つこと。</li> 
 </ul> 
 <p>Neil Killick氏は自身のブログ記事 &quot;<a target="_blank" href="http://neilkillick.com/2012/10/24/sustainable-pace-the-fastest-way-to-deliver-software/">sustainable pace - the Fastest way to deliver software</a>&quot; で，アジャイルチームにスピードアップを求めるとソフトウェア開発が遅れるのはどのような場合か，ということを解説している。そこで取り上げているのは，２週間のSprintで平均10ストーリの作業能力を持ったアジャイルチームが，作業するストーリ数の拡大を求められる，という話だ。</p> 
 <blockquote> 
  <p>今このチームに対して，Sprint毎にただ１つのストーリをこなすように依頼したとします。(…) 断言はできないにせよ，その１ストーリは間違いなく実施される，と予想することは不自然ではないでしょう。それも極めて高い品質であることは，おそらく間違いありません。</p> 
  <p>(...) では，Sprint毎に処理するストーリの数を2つにしてみましょう。チームがその２ストーリを完了できることはまず間違いないのですが，確率としては，１ストーリを依頼したときに比べればわずかに小さくなっているはずです。つまり私たちは，予測可能性を少し失ったのです。</p> 
  <p>では次に，契約納期に向けて悪戦苦闘していて，”スピードアップ”を強いられているような状況を仮定してみましょう。そんな状態のチームに，予想処理数を10ストーリから12ストーリにするように依頼します (つまりキャパシティを越えた訳です)。それとも14にしましょうか？(...) チームの作業を &quot;もっと速く&quot; するように依頼する (もっとひどい場合は「言い渡す」)ことによって，ソフトウェア提供の予測性が下がるとともに，おそらくはその品質も低くなるのです。</p> 
 </blockquote> 
 <p>氏のアドバイスは，チームが一定のペースを守って仕事することを認める，というものだ。</p> 
 <blockquote> 
  <p>(...) チームに対して，彼らのキャパシティにおいて高品質のソフトウェアを提供できる，適切なバランスを見つけることを認めれば，成功のサイクルが完成するのです。</p> 
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
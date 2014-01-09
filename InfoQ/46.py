<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>振る舞い駆動開発(BDD) - コラボレーションによる価値創造</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/bdd-value-collaboration"><em>原文(投稿日：2013/12/30)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>ソフトウェアプロジェクトの目的は，ステークホルダに価値を提供することだ。プロジェクトを通じたステークホルダへの価値提供を中心とする<a href="http://en.wikipedia.org/wiki/Behavior-driven_development">BDD(Behavior-Driven Development，振る舞い駆動開発)</a>は，そのためにデザインされた – <a href="http://technologyconversations.wordpress.com/about/">Viktor Farcic</a>氏は，自身のBDDに対する見方をこのように説明する。<br /> ソフトウェア開発者としてウォーターフォールからアジャイルプロセスへの移行に取り組む同氏は，さらに次のように言う – BDDの原則のひとつに，要件は誰でも理解できる方法で記述されなければならない，というものがある。それと対照的に従来のウォーターフォールプロジェクトでは，ステークホルダに対すしての価値が不明であったり，忘れられていたりすることが多い。このようなプロジェクトに関わる人たちの多くは “自分の仕事” だけを気に掛けて，それを “壁越しに” 次の人に投げ渡しているのだ。</p> 
  <p>BDDにおいて要件を語る上で重要なのはストーリである。氏はストーリをナラティブ(Narrative，物語)と，それをフォローする１つ以上のシナリオ(Scenario)という，２つの要素で構成されるもだと説明している。ナラティブとは，人あるいは役割の面で語られた，短くてシンプルな機能説明である。すべての関係者(ビジネスアナリスト，開発者，テスタ他)の間で行うコミュニケーションのベースを提供する程度の内容で，文章による説明よりも会話での使用を前提とするものだ。その目標は，３つの質問 - 価値は何か，誰にとっての価値か，実際の機能は何か - に答えることにある。これらの質問に答えることでチームは，ステークホルダとの強力の下で，最善のソリューション定義に着手することができるのだ。<br /> 完了状態を定義し，開発したナラティブが期待を満たすことを確認する受け入れ基準となるシナリオを作成することで，ナラティブはさらに確固としたものになる。</p> 
  <p>しかしながら氏にとってのナラティブは，氏にとっては重要な違いのある，従来型の要件の特徴もいくつか持っている。時として極めて不正確になる書き言葉とは対照的なものとして，話し言葉による継続的なコミュニケーションに注目している点がそのひとつである。そしてもうひとつは，“本システムは ... します” というような形式の文章の羅列に終始しない機能記述が可能な点だ。機能の羅列は読み手に対して，システムの全体像やプロジェクトの目標の理解を難しくする。</p> 
  <p>最後に氏は，BDDから自動化への移行について説明する。BDDシナリオの実行は，<a href="http://jbehave.org/">JBehave</a>や<a href="http://cukes.info/">Cucumber</a>，<a href="http://specflow.org/">SpecFlow</a>，<a href="https://github.com/pivotal/jasmine">Jasmine</a>など，さまざまなフレームワークを使用して達成することができる。氏の提案によれば，BDDの実践は３つの段階で自動化することが可能だ。</p> 
  <ul> 
   <li>各ステップを正規化してライブラリを作成し，実際のコードからシナリオを分離する。これにより，非プログラマにも容易にストーリが記述できるようになる。</li> 
   <li>各ステップをより高度なビジネスレベルで結合して，アナリストや同様の立場からも理解しやすいものにする。</li> 
   <li>実施例の表を利用して，同一のシナリオをパラメータセットを変えながら何度も実行できるようにする。</li> 
  </ul> 
  <p>氏がまず最初のフェーズを実行するように奨める。そして最初のシナリオをサポートするに十分なステップが作られたならば，以降の２つのステップを続けていけばよい。</p> 
  <p>BDDは2006年頃，<a href="http://dannorth.net/introducing-bdd/">導入部</a>と<a href="http://dannorth.net/whats-in-a-story/">ストーリをBDDの視点から</a>記述した<a href="http://dannorth.net/about/">Dan North</a>氏によって開発された。<br /> <a href="http://en.wikipedia.org/wiki/Specification_by_example">例示による仕様記述</a>は，BDDと密接に関連した要件定義方法のひとつだ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
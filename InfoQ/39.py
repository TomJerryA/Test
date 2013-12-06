<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Kevin Behr氏に聞く，継続的改善の技術(Kung-Fu)</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/behr-continuous-improvement"><em>原文(投稿日：2013/11/17)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://www.devopsdays.org/events/2013-newyork/program/">先頃</a>ニューヨークで開催された<a href="http://www.devopsdays.org/">DevOps Days</a>で，<a href="http://en.wikipedia.org/wiki/The_Visible_Ops_Handbook">&quot;The Visible Ops Handbook&quot;</a>と<a href="http://itrevolution.com/books/phoenix-project-devops-book/">&quot;The Phoenix Project&quot;</a>の著者のひとりである<a href="http://www.kevinbehr.com/">Kevin Behr</a>氏は，Jesse Palmer氏とともに，常態的にオーバーワークにある運用チームに継続的改善の文化をいかに浸透させるか，というテーマで<a href="http://vimeo.com/album/2573383/video/77233580">講演</a>を行った。</p> 
  <p>両氏によると，この継続的改善のプロセスを通じて，チームの仕事の方法は劇的に変わった – 開発(Dev)と運用(Ops)が緊密な関係で作業し，不要な作業ややり直しは着実に減少しているというのだ。さらにこのプロセスは，チームが自分たちの仕事，つまりミッションの進むべき方向や一貫性のあるストーリを見失ったという結論に達したときにも，ブレークスルーを実現する上で重要な役割を果たしたという。</p> 
  <p>氏らはまず，現状の分析から始めた。この分析では<a href="http://en.wikipedia.org/wiki/Theory_of_constraints">TOC(theory of constraints, 制約理論)</a>や<a href="http://en.wikipedia.org/wiki/Cynefin">Cynefin</a>など，いくつかのフレームワークを指針として使用している。Cynefinは，複合系の進化的性質と内在する不確実性を論理的に検証するためのフレームワークだ。次に<a href="http://en.wikipedia.org/wiki/Current_reality_tree_(Theory_of_constraints)">CRT(current reality tree, 現状構造ツリー)</a>を使って，組織の問題を生み出す根源となっている最上位の問題を描き出した。</p> 
  <p>さらにMike Rother氏が著書 <a href="http://www.amazon.com/Toyota-Kata-Managing-Improvement-Adaptiveness/dp/0071635238">&quot;Toyota Kata&quot;</a> で推奨しているテクニックである <a href="http://www.lean.org/kata/">改善のカタ</a>を使った実験も，期間を短く制限して始めている。改善のカタとは，科学的手法を組織の日々の活動に適用することによって，問題やその根本原因を解決する方法である。今回使用された改善のカタは，毎日のスタンドアップミーティングで次の５つの質問に答える，いうものだ:</p> 
  <ul> 
   <li>目標条件は何か？</li> 
   <li>現在の状況はどうか？</li> 
   <li>目標条件を達成する上で，もっとも大きな障害は何か？</li> 
   <li>あなたは今日，どの障害を試すのか？</li> 
   <li>あなたの試みは何か，その結果はどうすれば確認できるのか？</li> 
  </ul> 
  <p>例えば，もっとも一般的な不満は <a href="http://c2.com/cgi/wiki?NotEnoughTime">&quot;十分な時間がない&quot;</a> というものだ。しかしチームは，それをもっと深く掘り下げることで，ひとつの結論に達した。それは皆がいつもその時点で，もっとも有効な手段を探しだそうとはしているが，全体的な視点が欠落している，というものだった。そこで彼らは<a href="http://en.wikipedia.org/wiki/Kanban_(development)">カンバン</a>を採用することにした。それによってチームは，バリューストリーム(value stream)の可視化やフロー管理，試行や進捗の状況を測定するためのステージ設定などが可能になった。</p> 
  <p>改善プロセスでは，&quot;技術的負債の返済&quot;や&quot;計画外作業の管理&quot;など，いくつかの目標条件を特定した。これらを達成する過程において，クリティカルな技術的負債プロジェクトの定義や，上位アクティビティを見失わないためのシンプルなプロジェクトプランの作成など，いくつかの実験が行われた。結果は具体的な形で現れた。<a href="http://en.wikipedia.org/wiki/Root_cause_analysis">根本原因の解析</a>にって<a href="http://www.urbandictionary.com/define.php?term=Groundhog%20Day%20Effect">マーモットの日(Groundhog Day)</a>効果が回避できたこともその一例だ。運用チームはさらに，デプロイメントプロセスの改善などといった，開発チームと共同で行う改善作業にも着手した。これが実現できたのは，何よりもチーム間にフィードバックループが形成されたからだ。</p> 
  <p>InfoQではKevinに，講演で取り上げた技術と実践について話を聞くことにした。</p> 
  <p><strong>講演で紹介した組織の改善事例では，改善のカタを利用したいう説明がありましたが，</strong><strong>これとような方法をいつも採用しているのでしょうか，あるいは今回の状況に合わせて改善のカタを選択したのですか？</strong></p> 
  <blockquote> 
   <p>形としてはさまざまですが，Mike Rother氏が著書 &quot;The Toyota Kata&quot; で説明したものと同じような改善のカタは頻繁に使用しています。私たちが使うのは，Opsflowと呼んでいる，より広範な形式のアプローチの中の一部としてです。組織学習の７つの面に合う，さまざまなメソッドやアセンブリを採用します。価値提供のサイクルとリードタイムを削減すると同時に，共適応的なイノベーション能力を開発し，潜在的才能を育成，発展させることが目標です。</p> 
  </blockquote> 
  <p><strong>目標条件は単なるゴール(Goal)やKPIではないという点について，詳しく説明して頂けますか？</strong><strong>ここで言う目標条件とは何なのでしょう？ </strong></p> 
  <blockquote> 
   <p>ゴールは遠すぎますので，その時々の作業判断による影響をほとんど見ることができません。課題(Challenge)はゴールよりも小さい達成の単位です (ゴールにほとんど近い課題もあり得ますが) 。ゴールよりもっと作業者に近くて小さなものが目標条件，すなわち作業者の隠喩的なワークステーションないしワークセンタにおける測定基準，あるいはその集合です。プロセスレベルでの測定基準(１日当たりのウィジェット開発のように)といったような，知的作業を測定する数値なのです。課題を達成するためには，デスクで何をしなければならないのか，目標条件の達成度を測るにはどうすればよいか。最初はそのようなことを広範囲に指導すればよいでしょう。習うより慣れる，ということですね。</p> 
  </blockquote> 
  <p><strong>目標条件を見つけ出すのには，どのような仕組みを使うのですか？</strong></p> 
  <blockquote> 
   <p>多くのテクニックを利用しています。もっとも有効なのは，組織のゴール/ミッション/戦略/計画/開拓といった，ミッション定義に対する管理的なアプローチですね。目標条件はすべて，管理の確立した領域内にあることが必要です - 目標条件の示す課題が，確実にゴールに近づくことのできるものであるように管理しなければならないのです。</p> 
  </blockquote> 
  <p><strong>ターゲットとする目標条件は，どのように決めているのでしょう？</strong></p> 
  <blockquote> 
   <p>現状構造ツリーや未来構造ツリー，移行ツリー，ゴールマッピングなど，Eli Golddatt氏の制約理論を基にした思考ツールを使っています。フューチャーバックワード(future backward)や儀礼的異議(ritual dissent)など，認知バイアスの回避と変更すべき根本条件の特定を支援するためにDavid Snowden氏のデザインしたメソッドやアセンブルも使っています。</p> 
  </blockquote> 
  <p><strong>継続的な学習あるいは継続的適応でもっとも難しいのは，その&quot;継続&quot;という部分だと思います。</strong><strong>勢いに乗って始めるのは簡単ですが，自然消滅することも少なくありません。</strong><strong>長期に渡って継続的な適用を維持するためのヒントやテクニックといったものはありますか？</strong></p> 
  <blockquote> 
   <p>ありますよ！ まずは形式を正確に，深く習得することです。科学的手法を学習して科学者の文化を確立し，育成することが重要なのです。その文化を守る姿勢を確立するためには，コーチングや第２コーチングなどのプログラムも必要になります。失敗を語り合い，成功を祝うために，振り返りを毎週実施してください。努力を継続する上で最大の障害は，課題が次から次へと現れるために，あたかもランニングマシンの上にいる(同じ場所にいるだけで，大きな変化が何もない)ように感じられる点でしょう。改善の失敗率は低いので，かえって落胆を感じてしまうかも知れません。チームが定期的に自らの成功と教訓を振り返れば，そこで得た達成感を使って，さらなる改良へのモチベーションを高めることができるでしょう。それが鍵なのです。</p> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
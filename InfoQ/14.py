<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>２つのDoDによる開発プロセスの改善</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/process-definition-done"><em>原文(投稿日：2014/03/11)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://www.roodmitek.nl/">Rood Mitek</a>の創設者で，<a href="https://www.rabobank.com/en/group/About_Rabobank_group/Profile/organisation/Rabobank_International.html">Rabobank International</a>のMicrosoft .NETコンサルタントでもあるChristian Vos氏が先日の<a href="http://www.scrumalliance.org/community/articles/2014/january/why-using-a-definition-of-done-in-an-agile-project">ブログ</a>で，成熟度と品質の面での向上のため，アジャイル用語としてのDoD(Definition of Done, 完了の定義)を理想と現状のバージョンに分離するように提案している。２つのバージョンが必要な理由として氏が挙げるのは，チームの能力と成熟度だ。</p> 
  <p>氏は2つのバージョンを次のように定義している。</p> 
  <blockquote> 
   <p>理想的なDoDとは，開発から製品の提供まで，インクリメントの完遂に必要なすべてのステップを定義するものです。それ以上の作業は必要ありません。 これに対して現状のDoDでは，１回のスプリントでチームが実行可能なステップを定義しています。</p> 
  </blockquote> 
  <p>そしてプロセスの透明性を向上するために，両方のバージョンのDoDを壁に掲示するよう提案している。チームとプロダクトオーナが，２つのDoDのギャップ解消を絶えず念頭に置きながら作業できるようにするためだ。</p> 
  <blockquote> 
   <p>２つのバージョンを壁に掲げることで，プロダクトオーナに対する透明性が生まれます。そこにはチームの現在の能力と，改善に向けてできることが示されています。チームは現状のDoDを一歩ずつ，理想的なDoDに向けて拡大すべく，絶えず努力することができます。このDoDの拡大こそが，品質と成熟度において向上するということに他なりません。</p> 
  </blockquote> 
  <p>氏は，製品レベルのコードの提供に必要なすべてのステップがDoDに含まれていないのは，チームの成熟度と能力の不足に原因がある，と述べている。スプリントが終了しても，さまざまな項目がいつも未完了のまま残っている。問題なのは，このような未完了の作業がスプリント毎に積み上げられた結果，多くのチームがリリースの準備作業として，これらを解決するための特別なスプリントを用意しなければならないことだ。</p> 
  <blockquote> 
   <p>この問題を解決するために多くのチームが，&quot;堅牢化スプリント&quot;あるいは&quot;リリース用スプリント&quot;と言われるものを導入しています。これらのスプリントは，例えば提供パッケージの作成や最終的なバグ解決，最終テストの実施などといった，ソフトウェアを製品レベルに仕上げるために使用されます。チームが完全なDoDを定義して適用すれば，未完了の作業はすべてスプリント内で実行されるようになりますから，リリーススプリントは必要ありません。</p> 
  </blockquote> 
  <p>優れたDoDが有効なのは次のようなポイントである，と氏は言う。</p> 
  <ul> 
   <li>フィードバックの獲得と，それによる製品や作業プロセスの改善</li> 
   <li>リリース計画の改善</li> 
   <li>バーンダウンチャート感覚の獲得</li> 
   <li>リスク遅延の最小限化</li> 
   <li>チームの質とアジリティの改善</li> 
   <li>ステークホルダに対する透明性の実現</li> 
  </ul> 
  <p><a href="http://www.net-a-porter.com/">Net-A-Porter</a>でアジャイルコーチを務めるDavid Lowe氏も，２バージョンのDoDを持つというアイデアに賛成だ。</p> 
  <blockquote> 
   <p>よくできたアイデアだと思います。少なくともチームがするべきと知っているものについては，これで受け入れられます。そこからどうやって理想型に進むかというのは，もちろん別の問題ですが。</p> 
  </blockquote> 
  <p>同じようなラインでは<a href="http://www.themotionstudio.nl/en/">The Motion Studio Multimedia Productions</a>を所有するWouter Tengeler氏が，ユーザストーリを別々に生成する，というアイデアを提案している。</p> 
  <blockquote> 
   <p>(技術的)負債を可視化するためには，現状のDoDと目標とするDoDとの違いを補完するようなストーリを追加するとよいでしょう。私ならばユーザマニュアル記述というストーリを追加してタスクを明らかにし，まだ実行すべきものが残っていることが誰でも分かるようにする，という方法を選ぶと思います。チームが成熟すれば，マニュアルの記述をDoDに書き込めるようになるでしょう。</p> 
  </blockquote> 
  <p><a href="https://www.atlassian.com/">Atlassian</a>のプロダクトマーケティングスペシャリストであるDave Meyer氏は，最近の<a href="https://blogs.atlassian.com/2013/10/8-steps-to-a-definition-of-done-in-jira/">ブログ</a>の中で，一定期間内のDoD管理にJiraを用いる方法について説明している。</p> 
  <blockquote> 
   <p>DoDは定期的な見直しが必要なライブドキュメントです。開発チームは改善に励むのと同じように，プラクティスも強化していくことが可能なのです。オプションを削除あるいは変更するよりも，単純に無効にしましょう。 無効にしたオプションはJIRA内に残りますが，イシューとして表示されなくなります。こうすることで，DoDの記録を経時的に保存することができるのです。</p> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
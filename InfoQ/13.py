<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Domino :Datascience-as-a-Service</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/domino-datascience-as-a-service"><em>原文(投稿日：2014/03/11)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>データサイエンス向けPlatform-as-a-Serviceである<a href="http://www.dominoup.com/">Domino</a>を使えば、PythonやRのような言語をクラウドで使ってデータ分析ができる。</p> 
  <p>Nick Elprin氏(Dominoの共同創業者)によれば、データサイエンティストはDominoを使ってインフラではなく分析に注力できる。</p> 
  <blockquote>
   データ量が増え、データ分析手法がより洗練されると、データ分析に必要なツールの使い勝手が悪くなり、データサイエンスの分野に取り組むのに不要な制限が生まれます。
  </blockquote> 
  <p>Dominoは3つの柱で成り立っている。</p> 
  <ol> 
   <li><em>クラウドに直接配置して実行</em>: 既存のコード(Python, R, Matlab, Julia, シェル)をEC2上で直接実行でき、負荷をかけず、リソースを使いすぎずに長時間実行できる。これを実現するための細かな調整はシステムが自動で実施してくれる。AMIの管理、マシンの起動と停止、マシンへの安全なデータ転送、分析結果の安全な取得などだ。</li> 
   <li><em>データサイエンスのバージョン管理</em>: Dominoの利用者はGitのようなツールは分析作業では使いにくいことを知っている。というのは、大規模なデータセットを扱えないし、入力と結果の間にリンクを作成できないからだ。Dominoはプロジェクト全体のスナップショットを自動的に取得する。現時点では40GBまで。スナッショットがあるので過去の作業を簡単に追跡できる。</li> 
   <li><em>コラボレーション</em>: Githubのプロジェクトのように、Dominoのプロジェクトは表示、編集、プロジェクトの実行ができる協力者を持つことができる。衝突を検知し、更新結果の通知を送信できる。チームの作業が進捗するたびに議論で利用できるノートブック機能もある。</li> 
  </ol> 
  <p><a href="http://inside-bigdata.com/2014/02/21/data-science-cloud-domino/">従量課金モデル</a>のDominoはフリーのアカウントもあり、月額サブスクリプションもある。InfoQがNick Elprin氏に取材したところ、まだ若いプラットフォームであるにもかからわらず、すでにあらゆる分野の<a href="http://bickson.blogspot.com/2014/03/domino-data-labs-run-data-analytics-in.html">データサイエンスの実践者</a>に使われている。学術の世界では数千の画像を分析する環境学者、<a href="https://www.kaggle.com/">Kaggleのコンテスト</a>に参加するデータサイエンスコンサルタント、マーケティング企業などだ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
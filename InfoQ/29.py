<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Canary Deploymentsを使って稼働中にテストする</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/canary-release-improve-quality;jsessionid=9A3E7C43F97413781779C86CBE329370"><em>原文(投稿日：2013/03/26)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Nolioが彼らの<a target="_blank" href="http://www.noliosoft.com/resources/videos/webinar/canary/show/1/">DevOpsのベストプラクティスに関するシリーズの最初のビデオ</a>で言っていることによれば、ユーザーの一部を新しい機能に目を向けさせたことで、企業は &quot;Canary Deployment&quot;を継続的デリバリの一部として使って、稼働中のソフトウェアをテストしている。&quot;Canary Deployment&quot;は一種の増分リリースで、ソフトウェアの新バージョンをその対応する稼働中のバージョンと並んでデプロイすることで実現される。ソフトウェア製品を並べて、複数のバージョンを走らせるには、ソフトウェアは、特にその構成と完璧な自動デプロイができるように設計されている必要がある。</p> 
 <p>&quot;Canary Deployment&quot;における技術的挑戦を克服したことで、デプロイプロセスのリスクを減らし、<a target="_blank" href="http://blogs.msdn.com/b/seliot/archive/2009/12/25/don-t-just-listen-to-your-users-watch-them-with-online-experiments.aspx">A/Bテスト</a>とプリエンプティブな<a target="_blank" href="http://highscalability.com/blog/2011/12/12/netflix-developing-deploying-and-supporting-software-accordi.html">パフォーマンステスト</a>できるようになる。A/Bテストにより、ほとんどのユーザーの使用感を変えることなく新しい機能をテストできる。同様に、パフォーマンステストは、全体としてユーザーベースにほとんど影響を与えない。</p> 
 <div>
  Nolioによれば、&quot;Canary Deployments&quot; は以下のステップから成る。
 </div> 
 <ol> 
  <li>ビルドによる成果物、テストスクリプト、設定ファイル、デプロイマニフェストを含んだデプロイ用の成果物を準備する。</li> 
  <li>ロードバランシングから&quot;Canary&quot; サーバーを除く。</li> 
  <li>&quot;Canary&quot; アプリケーションをアップグレードする（ドレインとデプロイ）。</li> 
  <li>アプリケーションの自動テスト。</li> 
  <li>ロードバランシングに&quot;Canary&quot; サーバーを戻す（接続性とサニティチェック）。</li> 
  <li>もし&quot;Canary&quot; テストがライブ使用で成功したら残りのサーバーをアップグレードする（失敗したらロールバックする）。</li> 
 </ol> 
 <div>
  Nolioのプレゼンテーションには、&quot;Canary Deployments&quot;の高レベルな統合を示す、
  <a target="_blank" href="http://www.noliosoft.com/product/zero-touch-deployment">彼らの製品の使い方の概要</a>が含まれている。彼らは、複数のプロセスで再利用できるアプリケーションモデルを使っているが、その使い方はデータから導ける。管理とレポーティングは、&quot;Canary Deployment&quot;に並行して行われる。
 </div> 
 <div>
  &nbsp;
 </div> 
 <p>&nbsp;</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
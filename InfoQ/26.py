<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Parse MBaaS の分析</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/analyzation_parse-MBaaS;jsessionid=FBA687AA86CDD8559D037869ABCCF4BF"><em>原文(投稿日：2013/03/22)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>MBaaS (Mobile Backend as a Service) が爆発的に成長しているのは，モバイルアプリケーション開発者たちがかなりの割合で <a target="_blank" href="http://blog.programmableweb.com/2012/11/29/mobile-backend-as-a-service-mbaas-give-me-liberty-or-give-me-convenience/">安易な解決策</a> を望んでいることの証明だ。すぐれたアプリを設計するには，それもひとつの方法に違いない。しかしMongoDBやCouch，Cassandra，MySQLなど複数の開発言語を積み上げて実用的で発展性に富んだバックエンドを構築するという，人の羨むようなスキルを習得するのは，それとはまったく別の話だ。</p> 
 <p>&nbsp;</p> 
 <p class="MsoNormal">MBaaS を提供する新興企業を取り上げる <a target="_blank" href="http://www.infoq.com/jp/news/2013/02/KinveyMBaaS;jsessionid=BF8640D98F42DDD73D5E3E9CAF29A314;jsessionid=FBA687AA86CDD8559D037869ABCCF4BF">シリーズ記事の第３弾</a> として，今回の記事では <a target="_blank" href="https://parse.com/">Parse という企業を動かしているもの</a> について検討する。<a target="_blank" href="http://gigaom.com/2011/08/08/parse/">2011年の始め</a>に <a target="_blank" href="http://ycombinator.com/">Y Combinator</a> の起業支援を受けて設立された Parse は，数を増し続ける競合企業たちと同じように，効率的なモバイルバックエンド構築に必要なモバイルアプリ開発者の時間と労力の削減を目的とする企業だ。</p> 
 <p class="MsoNormal">MBaaS を詳細に調べていくうちに，我々には彼らの FAQ や機能，あるいはサービスのメリットなどといったものが，どれも同じように見え始めていた。違うのはそれらの属性を実装する方法だ。個々のMBaaS プロバイダが持つユニークなコーディングスタイル，サーバ，プログラミングといったものが，最終的にまったく違う結果を生み出しているのだ。</p> 
 <p class="MsoNormal">Kii Cloud との <a target="_blank" href="http://www.infoq.com/news/2013/01/28;jsessionid=BF8640D98F42DDD73D5E3E9CAF29A314;jsessionid=FBA687AA86CDD8559D037869ABCCF4BF">以前のインタビュー</a> を例にしてみよう。同社と Parse のサービスには，UIの外観，ポイントやクリック操作のシンプルさなどの点で似た部分が少なくない。どちらも開発者に対して，すべての主要 <a target="_blank" href="https://parse.com/apps/quickstart">モバイルフォンプラットフォーム</a> 用アプリは当然のこと，非モバイル指向のプラットフォーム用アプリに対しても，MBaaS を簡単にプラグインするための機能を提供する。</p> 
 <p class="MsoNormal">まず大きく違うのが普及の範囲だ。Kii Cloud は戦略的パートナを通じて，アジアのモバイルユーザの中にいる数百万という潜在的ユーザに対してネットワークを提供する。Parse には <a target="_blank" href="https://www.parse.com/products">Kii の販売チャネルに相当するもの</a> はないようだが，同社のパートナたちが興味深い <a target="_blank" href="https://www.parse.com/customers/partners">付加機能</a> を数多く提供している。</p> 
 <p class="MsoNormal">どちらの MBaaS プロバイダも，それぞれ独自の変数を持っているようだ。例えば Parse では，検索を行うための <a target="_blank" href="http://blog.parse.com/">同社のメソッド</a> に準拠したデータモデルが必要になる： &quot;...文字列の正確なプレフィックスに合致しないストリング照会クエリでは，インデックスの使用はできません。この制限によって，このようなクエリは，アプリケーションの拡大にともなってタイムアウトエラーを発生する可能性が高くなります。&quot;</p> 
 <p class="MsoNormal">Parse は独立した初心者から巨大企業まで，すべての <a target="_blank" href="https://www.parse.com/plans">モバイルソフトウェア開発者</a> を対象とした３つの価格スキーマの下で，サービスを提供している。俗に言う &quot;靴ひも&quot; を買う程度の予算しかないのであれば，フリープランを利用する方法もある。このプランには１ヶ月あたり100万のリクエストとプッシュ，１ギガバイトのクラウドストレージが含まれている。</p> 
 <p class="MsoNormal">プッシュ技術に関して言えば，Parse では <a target="_blank" href="https://www.parse.com/products/push?mkt_tok=3RkMMJWWfF9wsRonu6TOZKXonjHpfsX57eUtUKWzlMI%2F0ER3fOvrPUfGjI4ATMdiI%2FqLAzICFpZo2FFIG%2FKGeQ%3D%3D#3">数多くのオプション</a> 機能を用意している。プッシュ通知の構成，スケジュール，分割，対象の設定や，詳細な分析を行うことが可能だ。</p> 
 <p class="MsoNormal">問題点を見つける作業は <a target="_blank" href="https://parse.com/questions/fetch-all-data-in-a-table-using-pfquery">コミュニティ</a> の役割だ。<span class="comhead"><a target="_blank" href="https://news.ycombinator.com/item?id=4701035">Hacker News</a> の <a target="_blank" href="https://news.ycombinator.com/user?id=jawngee">jawngee</a>氏によれば</span>，</p> 
 <blockquote>
  サブクラスがほとんど役に立たないというのは，どうかと思いますね。PFObject をサブクラス化することはできるのですが，PFQuery の機能のほとんどが利用できないのです。PFUser もサブクラス化したいものの代表ですが，あちらこちら手を入れないとまともに動きません。
 </blockquote> 
 <p><span style="line-height: 13px; font-size: 9pt">同じく <a target="_blank" href="https://news.ycombinator.com/user?id=bklimt">bklimt</a>氏は，</span></p> 
 <blockquote>
  PFObject のサブクラス化と包括的なオフラインソリューションは，どちらも機能リストの中で優先度が非常に高いもののひとつです。その２つを実現するために，時間を掛けて取り組んでいるところです。
 </blockquote> 
 <p>Parse ユーザの Huzell氏は，</p> 
 <blockquote>
  クエリで取得したすべてのオブジェクトを保持しておくには，どうすればよいのでしょう？
 </blockquote> 
 <p>という質問で，<a target="_blank" href="http://www.linkedin.com/in/33fosco">Parse のグル</a> を問い詰めることに成功した。</p> 
 <blockquote>
  多数の結果を取得する操作はサポートされていません – Fosco Marotto。
 </blockquote> 
 <p class="MsoNormal">コミュニティ全体でソリューションを見出せることも少なくない。少なくとも <a target="_blank" href="http://alexefish.com/post/29843064002/fetching-every-row-of-a-table-with-parse-and-pfquery">iOSに関しては</a>，Alex Fish氏がこの問題の解決に成功している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
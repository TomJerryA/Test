<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Spotifyはどうやってアジャイルをスケールアウトしたか: Henrik Kniberg氏へのインタビュー</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/scaling-agile-spotify-kniberg;jsessionid=5E6FF6EF2F2BFC635D900F206C72A32A"><em>原文(投稿日：2013/04/09)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>昨年11月、Spotifyは<a target="_blank" href="http://blog.crisp.se/2012/11/14/henrikkniberg/scaling-agile-at-spotify">Scaling Agile @ Spotify with Tribes, Squads, Chapters &amp; Guilds</a>と題したペーパーを発表した。私は最近、Henrik Kniberg氏にこのペーパーと現在の状況について質問する機会を得た。</p> 
 <p><strong>InfoQ:</strong>行っている業務がスケールしないことを示す最初の徴候は何だったのですか。どのような弱点があるのでしょう。</p> 
 <p><strong>Henrik Kniberg:</strong>求める生産性を手に入れられない状況で、会社内は総じてイライラしていました。例えば、 各チャプターのリードが直接の報告をしすぎるため、1対1のミーティングやアクティブなメンタリング、コーチングをする時間を見つける大変になったのです。</p> 
 <p><strong>InfoQ:</strong>アジャイルをスケールする方法や個々人の役割について最初に意思決定したのは誰ですか。</p> 
 <p><strong>Henrik Kniberg:&nbsp;</strong>Technology and Product部門の上級リーダーたちです。それから会社にフィードバックとインスピレーションをもらいました。一気に変えるのではなく、小さな改善を積み重ねるというやり方です。3年間かけて変化してきました。現在の私たちの働き方は自然に進化しています。</p> 
 <p><strong>InfoQ:</strong><strong>&nbsp;</strong>Scaled Agile FrameworkやDisciplined Agile Deliveryのような既存の手法とは反対の手法を採用したのはなぜですか。</p> 
 <p><strong>Henrik Kniberg:&nbsp;</strong>私たちはアジャイルとリーンの原則や基礎の熱心な支持者です。しかし、特定の方法に密着するということはありません。ただ単に自分たちの文化と環境に適した働き方を求めているのです。</p> 
 <p>自主性は私たちの原則のひとつです。私たちは、大きなアジャイルの枠組みで調整しなくても、自分たちで製品をビルドしリリースできる、独立したスクワッドを支援します。また、多くなプロジェクトも避けようとしています(可能な限り)。こうすることで複数のスクワッド間にまたがって調整をする必要を最小限にできるのです。</p> 
 <p><strong>InfoQ:</strong>3つの都市に30のスクワッドがあると言いましたね。スクワッドのメンバは同じ場所で働いているのですか、それともスクワッドのメンバが別々の都市にいることはありますか。</p> 
 <p><strong>Henrik Kniberg:&nbsp;</strong>ほとんどの場合、スクワッドとトライブは同じ場所で働いています。スクワッドのすべてのメンバは同じ部屋におり、トライブ内のすべてのスクワッドは同じオフィスの隣り合った部屋にいます。私たちは慎重にこの方法を進めました。特にプロダクトオーナがスクワッドと同じ場所、同じ部屋で働くように最新の注意を払いました。現在、メンバが同じ場所で働いていないスクワッドはひとつしかないはずです。</p> 
 <p><strong>InfoQ:</strong>&nbsp;このホワイトペーパーではツールは付箋とスプレッドシートを使っているのがわかります。Spotifyでは既存のアジャイルツールを使っていますか。使っていない場合はなぜ使っていないのか教えてください。</p> 
 <p><strong>Henrik Kniberg:&nbsp;</strong>定期的に実験しながら、複数のツールを組み合わせて使っています。現在、普通に使われているツールは壁に貼る付箋、Googleスプレッドシート、それにJIRAです。TrelloとLeanKit Kanbanも使っています。</p> 
 <p>知識の共有とベストプラクティスの普及を奨励していますが、どのようなツールを使って幸せかつ効率的に仕事をするのかは、スクワッドとトライブに任せています。プロジェクトが大きくなるのを避けるため、ツール選択の標準化は必要最低限にしています。</p> 
 <p><strong>InfoQ:</strong>ペーパーの2ページ目によれば製品のひとつひとつの部分をそれぞれの&quot;スクワッド&quot;が担当しているようですね。これはどのように管理しているのですか。製品全体の結合(やコードのオーナシップ)はどのように管理していますか。</p> 
 <p>&nbsp;</p> 
 <p><strong><img alt="" src="http://www.infoq.com/resource/news/2013/04/scaling-agile-spotify-kniberg/ja/resources/spotify_1.png;jsessionid=5E6FF6EF2F2BFC635D900F206C72A32A" _href="img://spotify_1.png" _p="true" /></strong></p> 
 <p><strong>Henrik Kniberg:&nbsp;</strong>組織の体制にとって技術アーキテクチャはとても重要です。組織の構造と技術アーキテクチャは調和していなければなりません。多くの企業は私たちの働き方をまねできないでしょう。アーキテクチャが許さないのです。</p> 
 <p>私たちは働き方を支援するアーキテクチャを実現するのに多くの投資をしてきました。その結果、しっかり結合したコンポーネントとアプリが独立して動き、進化するというアーキテクチャになりました。エコシステム全体の進化は強力な設計上のビジョンに導かれています。</p> 
 <p>上級プロダクトマネージャがスクワッド、プロダクトオーナ、デザイナとしっかりと協業して製品の設計の凝集度を保っています。こ調整作業はときに困難を極めます。これは私たちの課題のひとつです。デザイナは直接スクワッドと一緒に働きます。しかし、デザイナ　の作業時間の少なくとも20%は他のデザイナと製品全体のデザインの一貫性を保つために使われます。</p> 
 <p><strong>InfoQ:</strong>6ページ目の画像は多くの依存関係を示しています。UXは独立したチームが担当しているようですね。依存関係はどのように扱っているのですか。</p> 
 <p>&nbsp;</p> 
 <p><strong><img alt="" src="http://www.infoq.com/resource/news/2013/04/scaling-agile-spotify-kniberg/ja/resources/spotify_2.png;jsessionid=5E6FF6EF2F2BFC635D900F206C72A32A" _href="img://spotify_2.png" _p="true" /></strong></p> 
 <p><strong>Henrik Kniberg:&nbsp;</strong>依存関係の管理も私たちの課題のひとつです。依存関係が増えれば効率性が悪化します。</p> 
 <p>例えば、UXはほとんど分離されていました。しかし、依存関係の問題(上記の依存関係視覚化スプレッドシート参照)が生まれました。現在、デザインとUXはほとんどスクワッドに統合されています。これによって問題が少なくなりました。これが依存関係を低減するひとつの方法です。</p> 
 <p>依存関係を低減する方法は他にもあります。</p> 
 <ol style="margin-top: 0pt; margin-bottom: 0pt"> 
  <li> <p>依存関係をどこに置くかを決める。例えば、機能を担当するスクワッドとインフラを担当するスクワッドの間に意図的な依存関係を持ちます。この場合の依存関係は管理可能です。インフラのスクワッドの作業時間は予測可能だからです。依存関係を排除しようとするかわりに、管理できる依存関係にしようとしているのです。</p> </li> 
  <li> <p>準備できていないことを待たずに、自分で問題を解決する。オープンンソースモデルを採用しているので、スクワッドは他のスクワッドのコードを変更することができます。普通は会話とコードレビューを経て変更されます。</p> </li> 
  <li> <p>知識の共有。依存関係は知識の欠如から生まれることがあります。これは内部の技術的な会話で解決できます。他のスクワッドで“インターンシップ”を行い、学習します。</p> </li> 
  <li> <p>スクワッドを分割したり、合併したり、組み替えたりすることで依存関係の問題が解消される場合もあります。</p> </li> 
 </ol> 
 <p><strong>InfoQ:</strong>このホワイトペーパーが発表されてから重要な変化はありましたか。</p> 
 <p><strong style="font-family: Arial, Verdana, sans-serif; font-size: 12px">Henrik Kniberg: </strong>私たちは成長していますので、継続的に変化しています。</p> 
 <p>大きな一歩は自分たちの製品開発過程をより明確にしようとしていることです。<a style="text-decoration: none" target="_blank" href="http://blog.crisp.se/2013/01/13/henrikkniberg/how-spotify-builds-products"> How Spotify builds products</a>や Think It, Build It, Ship It, Tweak Itフレームワークを参照してください。また、リーンスタートアップの原則を適用しようとしています。たとえば、MVP(Minimum Viable Product)を素早くリリースすることや、計測可能な仮説を使って開発を進捗させようとしています。MVPを少人数のユーザにリリースしてユーザの実際の使い方を計測するという方法はかなり上手になりました。つまり、製品を開発しながら、実ユーザのフィードバックを受け、それを優先順位に反映させるということです。</p> 
 <p><strong>InfoQ:</strong>現時点での最大の問題は何ですか。</p> 
 <p><strong>Henrik Kniberg:&nbsp;</strong>現在の最大の問題は、</p> 
 <ul> 
  <li> <p>スクワッドの依存関係 - 依存関係を最小化する方法。必要な依存関係を最適化する方法。これは会社の成長し続ける限り、常に問題であり続けます。</p> </li> 
  <li> <p>組織上の注力点(スクワッドを同じ方法に向けて走らせる)とスクワッドの自主性(スクワッドが自ら進む方法を選ぶ)のバランスの取り方</p> </li> 
  <li> <p>デザインと開発をよりしっかりと結びつける方法</p> </li> 
  <li> <p>会社の成長に伴う、ボトルネックとなるオペレーションを排除する方法。スクワッドが継続的に配置し運用環境で実験できるようにする方法</p> </li> 
  <li> <p>多くのスクワッドを巻き込む“大きなプロジェクト”をどうやって調整するか</p> </li> 
  <li> <p>製品の設計の凝集度を保ちながら、多くの異なるスクワッドが独立して働く方法</p> </li> 
 </ul> 
 <p>&nbsp;</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
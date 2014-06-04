<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Facebook の決断：MVCはスケールしない。ならば Flux だ。</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/facebook-mvc-flux"><em>原文(投稿日：2014/05/15)へのリンク</em></a></p>
<p>この記事は、コミュニティと Jing Chen氏のFacebookでの反響にもとづいて アップデートされている（後ろの続報の項を参照）。</p>
<p>Facebookは、MVCパターンでは自分たちの要求の拡大に対応していくことで きないとの結論に達し、代わりに別のパターン Flux を使うことを決定した。</p>
<p>先日の<a href="https://www.facebook.com/f8">F8</a>でのセッション 「<a href="https://www.youtube.com/watch?v=nYkdrAPrdcw">ハッカー流の やり方：Facebookにおける、Webアプリ開発を再考する</a>」の中で、 Facebookの技術マネージャの Tom Occhino氏は、『十分に』巨大なコードベー スと大きな開発組織について説明し、さらに『MVCは、本当にあっというまに 複雑化してしまいます』と述べて、MVCはスケールしないと結論づけた。なにか新 しい機能を追加しようとするたびに、このシステムの複雑度は時々刻々と指 数関数的に増大し、そのコードは『壊れやすくて予測不能な』ものになって しまう。このことは、この種のコードベースに関わる開発者にとって新たに 深刻な問題を引き起こしている。なぜなら、なにか既存の機能を壊してしま わないかと彼らがコードに触れるのを恐れるからである。この結果、MVC は Facebookと決別することになったのである。</p>
<p>この問題への解決には『もっと予測可能な形でコードを構造化すること』が 求められる。これは、 <a href="http://facebook.github.io/react/docs/flux-overview.html">Flux</a> と <a href="http://facebook.github.io/react/index.html">React</a> を によって達成される。Fluxは、アプリケーション内のデータフローの単方向 化を促すシステム・アーキテクチャである。Occhio氏によれば、Reactは、 『予測可能』で『宣言的に』Web ユーザインターフェースを構築するための JavaScriptフレームワークであり、Facebook のWebアプリケーション開発を より高速化することを可能にするものである。</p>
<p>FacebookのソフトウェアエンジニアのJing Chen氏はさらに、MVCは小さなア プリケーションには適しているが、以下のスライドに示すようにモデルや関 連するビューが大量にシステムに加えられると複雑度が爆発してしまう、と 述べている。</p>
<blockquote> 
 <p><img src="http://www.infoq.com/resource/news/2014/05/facebook-mvc-flux/ja/resources/flux-react-mvc.png" alt="" _href="img://flux-react-mvc.png" _p="true" /></p> 
</blockquote>
<p>このようなアプリケーションは、モデルとビューの間に双方向のデータフロー が作られる可能性があるので、理解したりデバッグしたりするのが難しくな るのであり、Chen氏は、以下のような Flux による設計を代わりに提案して いる。</p>
<blockquote> 
 <p><img src="http://www.infoq.com/resource/news/2014/05/facebook-mvc-flux/ja/resources/flux-react.png" alt="" _href="img://flux-react.png" _p="true" /></p> 
</blockquote>
<p>この図の <em>Store</em> は、アプリケーションの全てのデータを含んでお り、<em>Dispatcher</em>は、先の図の <em>Controller</em> を置き換える もので、ある <em>Action</em> が起動された時にどうやっ て <em>Store</em> が更新されるべきかを決定するものである。 <em>Store</em>が変更された際には、 <em>View</em>も同時に更新され、それにともなって <em>Dispatcher</em> が処理すべき Action を発生させることもある。これにより、システムのコ ンポーネント間に単方向のデータフローしか生じないことが担保されている。 複数の <em>Store</em> や <em>View</em> をもつシステムも、ひとつだ け <em>Store</em> や <em>View</em> を持つシステムと同じと見なせる。な ぜなら、データは単一の方向にだけ流れ、別々の <em>Store</em> と <em>View</em> はお互いに直接影響しあうことがないためである。</p>
<p><a href="http://facebook.github.io/react/docs/flux-overview.html">Facebook</a> の、GitHub上の React のページには、Flux や <em>Dispatcher</em>、 <em>Store</em>についてのより詳しい解説がある。</p>
<blockquote> 
 <p>dispatcher は、Fluxアプリケーションの全てのデータフローを管理する 中央のハブです。これは、本質的には Store 内のコールバックの登録場所 です。各 Store は、それ自身を登録しコールバックを提供します。この Dispatcher が あるアクションに応答する際には、アプリケーション内の すべての Store はそこに登録されているコールバックによって、アクショ ンによって生じたデータを送信されるのです。</p> 
 <p>アプリケーションが成長するに従い、決まった順序で登録されたコールバッ クを実行することによって、Store間の依存関係を管理できるので Dispatcher はさらに不可欠なものになります。宣言にしたがって、Store は他の Store の更新が完了するまで待つことができます。そしてその後自 分自身を更新します。</p> 
 <p>Store は、アプリケーションの状態とロジックを含んでいます。Store の 役割は、古典的な MVC における Model の役割に少し似ていますが、しか し多数のオブジェクトの状態を管理していて、一個のオブジェクトのイン スタンスではないという点が異なっています。また、Backboneフレームワー クのコレクションと同じものでもありません。ORM形式のオブジェクトの集 合を管理するよりももっと単純に、Storeはそのアプリケーション内のある 特定の<strong>ドメイン</strong>について、アプリケーションの状態を管 理します。</p> 
</blockquote>
<p>重要なことは他のアクションが発火する以前に、データ層が自身が関係して いるビューの更新を完了させることである、と Chen氏は述べている。 <em>Dispatcher</em> は、直前の<em>アクション</em>の処理が未完了の間は、 次のアクションの処理を拒否することもできる。この設計方式は、他のビュー もいっしょに更新するといった副作用をもったアクションに対して特に有用で あり、コードはより明確で理解するのが容易になり、新米の開発者でもデバッ グが簡単にできるようになる。Flux は、Facebook の チャットのバグ（ニセの 新着メッセージ通知を行ってしまうバグ）を修正するのに役だった。</p>
<p><a href="http://facebook.github.io/react/docs/flux-todo-list.html">Flux TodoMVC チュートリアル</a>と、付属 の<a href="https://github.com/facebook/react/tree/master/examples/todomvc-flux"> ソースコード</a>は GitHubで公開されている。</p>
<p>Facebook は、彼らが適切だと思えばどんな設計方式を使うこともできるが、 疑問は残っている。MVCはスケールするのかしないのか？なにしろ、ここ以外に はスケールしているウェブサイトがたくさんあるのだから。</p>
<p><strong>続報</strong>。この記事を公開した後に、MVCに関するFacebookの 決定に関し て<a href="http://www.reddit.com/r/programming/comments/25nrb5/facebook_mvc_does_not_scale_use_flux_instead/"> 多くの開発者が Reddit でコメントを寄せた。</a>ここでいくつかそのコメ ントを紹介しよう。そもそも Facebook はMVCを誤用していたのだと考えてい る人もいるが、他の人々は Facebook は正しい判断を行っていると考えてい る。</p>
<blockquote> 
 <p><a href="http://www.reddit.com/r/programming/comments/25nrb5/facebook_mvc_does_not_scale_use_flux_instead/chj2fzc">giveupitscrazy 氏</a>：</p> 
 <p>これは、全く意味がないでしょうね。</p> 
 <p>まず１つには、彼らのMVCの構成には著しい欠陥があります。彼らは、コ ントローラが相互作用しているモデルに応じて分割するとか、なにか論理 的な分割理由があって、誰しもほぼ間違いなくコントローラを分割したく なるときでさえ、複数のモデルを操作するのにたった１つのコントローラ を使っています。</p> 
 <p>もちろん、彼らが説明しているような状況設定ならMVCは 動かないでしょうが、でもそれは そもそも本物の MVC ではないのです。</p> 
 <p>もし、彼らの Flux の構成図 と<a href="http://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/MVC-Process.svg/500px-MVC-Process.svg.png"> 本物のMVCの図</a>を比較したなら、web アプリにとってMVCをが本質的に 悪い事などなにもないということが明確に理解できるでしょう。</p> 
 <p><a href="http://www.reddit.com/r/programming/comments/25nrb5/facebook_mvc_does_not_scale_use_flux_instead/chj9zmj">balefrost 氏</a>：</p> 
 <p>そうですね・・・彼らの Flux の図はみんなが知ってる MVCの図に非常に よく似ています。</p> 
 <p>彼らは、実用的なMVCを再発明したのでしょう。そしてそれに新しい名前 をつけることにしたというわけです。あーあ！</p> 
 <p><a href="http://www.reddit.com/r/programming/comments/25nrb5/facebook_mvc_does_not_scale_use_flux_instead/chj3kmy">hackinthebochs氏</a>:</p> 
 <p>このアーキテクチャは、MVCを変形して少しばかりイベントベース風にし たもののようです。&quot;Store&quot;は、自分自身（そして、おそらく呼び出し順序 の依存性）を Dispatcher に登録し、その Dispatcher は、アクションを 処理して正しい呼び出し順序が達成されるように保証しています。これは、 正しい呼び出し順序を保証するという責任を、コントローラ から Dispatcherと Store に移動するものです。これは、振舞いを修正するため に必要な知識を減らしてしまうに違いないでしょう。</p> 
 <p><a href="http://www.reddit.com/r/programming/comments/25nrb5/facebook_mvc_does_not_scale_use_flux_instead/chj4f09">runvnc 氏</a>:</p> 
 <p>これを見て私が思ったことは、特別に深い理解というわけではないですが、 私はこれを理解したと思いますし、基本的なアイデアに賛成です。</p> 
</blockquote>
<p>Redditユーザの<a href="http://www.reddit.com/user/jingc09">jingc09 氏</a>は、コメント内容からしてたぶん Jing Chen氏だと思われるが、以 下のように、いくつか返信している。</p>
<blockquote> 
 <p><a href="http://www.reddit.com/r/programming/comments/25nrb5/facebook_mvc_does_not_scale_use_flux_instead/chjbo05">jingc09 氏</a>：たしかに、あれはトリッキーなスライドでした （１つのコント ローラが多数のモデルやビューと結びついていて、双方向のデータフロー がある）、この論争の原因の一部は、MVCが厳密には何であるのかについ ての十分なコンセンサスがなく、多くの人達が別々の意見を持っている ことにあります。本来私達が論じるべきテーマは双方向のデータフロー についてです。それは一方のデータ変更がもう一方にループバック可能 で、かつ連鎖的な効果を持っています。</p> 
</blockquote>
<p>事実を明確にするために、 『<a href="http://www.reddit.com/r/programming/comments/25nrb5/facebook_mvc_does_not_scale_use_flux_instead/chjbo05">Flux のDispatcherはMVCコントローラではない</a>』という記事も見てみよう。</p>
<blockquote> 
 <p>一つ私が明らかにしたい事は、Dispatcher が、Controller と同じ役目を果 たしているわけではないということです。Dispatcherにはビジネスロジッ クを持ちませんし、我々は同じ Dispatcher コードを複数のアプリケーショ ンで再利用しています。それは単にイベントを対応する登録先（たいてい はStoreです）に届けるための中央ハブに過ぎないのです。しかし、単方向 のデータフローを強制される場所であるため、Fluxアーキテクチャにおい てそれは重要なのです。・・・</p> 
</blockquote>
<p><a href="http://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller">Wikipedia の MVCコントローラに関する説明</a>のコメントでは以下のように述べら れている。</p>
<blockquote> 
 <p>コントローラは、モデルの状態を更新するために（たとえば、ドキュメン トの編集など）コマンドを送信することができます。またそれは、モデル に関係しているビューの表示を変化させるために（例えば、ドキュメント のスクロール）、ビューに対してもコマンドを送ることができます。</p> 
</blockquote>
<p><a href="http://www.reddit.com/r/programming/comments/25nrb5/facebook_mvc_does_not_scale_use_flux_instead/chjcifl">Chen 氏は述べている</a>。</p>
<blockquote> 
 <p>Dispatcherにはこんなことはできません。そのコマンドはどこか別のきっ かけ（ビューやサーバ応答、ライブ更新など）からスタートして、 Dispatcherに転送しなければならないのです。 <a href="https://github.com/facebook/react/blob/master/examples/todomvc-flux/js/dispatcher/Dispatcher.js">https://github.com/facebook/react/blob/master/examples/todomvc-flux/js/dispatcher/Dispatcher.js</a> を見ればこのことを理解する助けになるでしょう。</p> 
</blockquote>
<p>Redditでのコメントを見ていくと、MVCがどのようなものであり、どのよう に実装するべきななおかについて、少々混乱があるように思える。</p>
<p>Facebook の MVC に関する決定について、我々は以下の２つの見解を持っている。</p>
<p>１）最初のスライドは、モデルとビューが多すぎたので本当に衝撃的なもの に思えて、読者にこれは本当に実在しているものなのだろうかという戸惑いを 抱かせた。Facebook が Flux で解決した問題は、たかだか３つのビューを持つ チャットアプリだった。</p>
<p>２）彼らのMVCの例題では、なぜ双方向のデータフローによっ て <em>View</em> がデータフローを生じることになるのだろうか？ そしてな ぜ、このFluxの図では <em>View</em>が<em>Action</em>を発生させるのか？　<em>View</em>はいかな る物も発生させるべきではなかったはずだ。Facebook はMVCを誤用しているのではないか？</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Vagrantが開発環境向けコラボレーションツールをリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/vagrant-cloud"><em>原文(投稿日：2014/03/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>DevOpのツールを提供している<a href="http://www.vagrantup.com/" target="_blank">Vagrant</a>はバージョン1.5の重要な機能を発表した。公開イメージリポジトリと実行環境へのアクセスを共有する機能だ。Vagrant Cloudは完全な開発環境の発見と配信をシンプルにする。Vagrant Shareを使えば開発者は仮想環境へHTTPやSSHでアクセスする方法を他者に公開してコラボレーションできる。</p> 
  <p><a href="http://www.vagrantup.com/blog/vagrant-1-5-and-vagrant-cloud.html" target="_blank">最近のブログ記事</a>でVagrantチームはVagrant 1.5の機能を発表した。Vagrantは構成されたLinux仮想環境を作成し配布するのを単純化するツールだ。このツールのユーザは今までテンプレートとして利用するマシンを<a href="http://www.vagrantbox.es/" target="_blank">探しまわらなければ</a>ならなかった。これらのテンプレートは“ボックス”にパッケージングされている。ボックスはVagrantの基礎であり、<a href="http://docs.vagrantup.com/v2/virtualbox/index.html" target="_blank">VirtualBox</a>、AWS、<a href="http://docs.vagrantup.com/v2/vmware/index.html" target="_blank">VMware</a>、<a href="http://docs.vagrantup.com/v2/hyperv/index.html" target="_blank">Hyper-V</a>などのプロバイダで利用できる。<a href="https://vagrantcloud.com" target="_blank">Vagrant Cloud</a>が生まれたことで、開発者は公開、あるいは非公開のボックスにアクセスし<a href="https://vagrantcloud.com/help/boxes/lifecycle" target="_blank">バージョン</a>管理するための中心地を持つことができる。ほかの人が使うためのボックスをリリースすることも可能だ。</p> 
  <p>Vagrantのユーザは公開リポジトリでさまざまなボックスを公開し他のユーザが見つけられるようにできる。単純にVagrant Cloudで<a href="https://vagrantcloud.com/search?utf8=%E2%9C%93&amp;sort=&amp;provider=&amp;q=ubuntu" target="_blank">“Ubuntu”</a>という文字列で検索すると多くのボックスが見つかり、ユーザはホスティングプロバイダで検索結果をフィルタできる。ログインしたユーザはダウンロード数で結果をソートして最も人気のボックスを見つけられる。Vagrant CloudにはDocker、CoreOS、CentOS、Chef、Puppet、Salt、nginx、ElasticSearch、MySQL、Redisのためのボックスがある。</p> 
  <p>Vagrantは開発者同士の協力をソフトウエアの中核に据えようとしているようだ。新しいVagrant Shareを使えば、どこにいるどんな人でも実行中のボックスにアクセスできる。<a href="http://www.vagrantup.com/blog/feature-preview-vagrant-1-5-share.html" target="_blank">プレビューについてのブログ記事</a>で、Vagrantはこの機能について説明している。</p> 
  <blockquote> 
   <p>この機能を使えば、あなたのウェブサーバへのリンクを国中のあるいはオフィス内のチームメイトに共有できます。普通にウェブサイトにアクセスするのと同じように思えますが、これでチームメイトは実行中のVagrant環境に直接アクセスできるのです。チームメイトはあなたのした変更をリアルタイムですべて見れます。</p> 
   <p>Vagrant Shareを使えば、ウェブサーバに他人がアクセスできるようになるだけでなく、Vagrantの環境にローカルネットワークのマシンにアクセスするようにアクセスできます。</p> 
  </blockquote> 
  <p>開発者は<a href="http://docs.vagrantup.com/v2/share/index.html" target="_blank">3つのモードで</a>ボックスを共有できる。<a href="http://docs.vagrantup.com/v2/share/http.html" target="_blank">HTTP共有</a>モードを使うと誰でもVagrant環境へアクセスできるURLを生成する。NATやファイアウォールの背後でもアクセスできる。また、単なるウェブサーバへのアクセスだけではなく、開発者は<a href="http://docs.vagrantup.com/v2/share/ssh.html" target="_blank">SSH</a>を使った共有で外部の参加者がアクセスできるようにできる。Vagrantの示すユースケースにはトラブルシューティングの支援やペアプログラミングが取り上げられている。最後のモードは<a href="http://docs.vagrantup.com/v2/share/connect.html" target="_blank">General Sharing</a>モードだ。このモードでは開発者はVagrant環境の任意のポートやすべてのポートを外部に公開できる。セキュリティの懸念する向きに対して、Vagrantは<a href="http://docs.vagrantup.com/v2/share/security.html" target="_blank">セキュリティについての考慮点</a>と保護の仕組みを説明している。</p> 
  <p>次はどうなるだろう。Vagrantはより強力なVagrant Cloud、商用プラン、Windowsゲストのサポートを<a href="http://www.vagrantup.com/blog/vagrant-1-5-and-vagrant-cloud.html" target="_blank">約束</a>している。</p> 
  <blockquote> 
   <p>企業向けのサポート、APIアクセス、監査ログ、ボックス利用の統計値、Vagrant Shares上でのACL、カスタムドメインなど、新しい機能を予定しています。</p> 
   <p>Vagrant Cloudは現在、完全に無料です。最終的には課金する予定ですが、個人利用は無料のままになります。現在の計画では、商用利用と先進的な機能を考慮して価格を検討しています。</p> 
   <p>…</p> 
   <p>また、VagrantはWindowsゲストマシンを完全にサポートします。最低でもあとふたつのプロバイダを追加するつもりです。</p> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
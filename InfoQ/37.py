<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>VagrantがAmazon AWSとRackspaceをサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/vagrant-aws-rackspace;jsessionid=B7476C06B978541B0A06E4960507D413"><em>原文(投稿日：2013/03/08)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="http://www.hashicorp.com">HashiCorp</a> は，<a target="_blank" href="http://www.vagrantup.com/">Vagrant</a> のプロバイダとして <a target="_blank" href="http://aws.amazon.com">Amazon AWS</a> と <a target="_blank" href="http://www.rackspace.com">Rackspace</a> のサポートを加えることで新たな利用シナリオを実現する – 開発者のデスクトップ上に代えて，<a target="_blank" href="http://www.hashicorp.com/blog/preview-vagrant-aws.html">クラウド上で仮想マシン</a> が起動可能になるのだ。サポート対象プロバイダの追加によってVagrantは，開発～運用というワークフロー全体を極限までシンプルにする作業環境ツールというMitchell Hashimoto氏のビジョンに向けての新たな一歩を踏み出した，と氏は説明している。</p> 
 <p class="p1">3月12日にリリース予定のVagrant 1.1では，管理対象がECSインスタンス，Rackspaceクラウドサーバ，VirtualBoxあるいはVMware Fusion VMのいずれであるかに関わらず，開発用の作業環境構築や品質保証，さらに実行環境さえも，開発者は同じコマンドセットが使用できるようになる。</p> 
 <p class="p1">Rackspaceはクラウドサーバの実行に <a target="_blank" href="http://www.openstack.org">OpenStack</a> を使用している。したがってHashimoto氏が言うには，VagrantもOpenStackを90%はサポートしていることになる。氏はオープンソース開発者が後を引き継いで，欠けている部分を補ってくれればと考えている。</p> 
 <p class="p1">近く公開される Vagrant 1.1 では，目的とするプロバイダをコマンドライン引数として渡せるようになる予定だ。</p> 
 <pre class="p1">
$ vagrant up --provider aws</pre> 
 <p class="p1">上記のコマンドはデフォルトの <a target="_blank" href="https://www.virtualbox.org/">VirtualBox</a> の代わりに，新機能のAWSプロバイダを使用してECSインスタンスを起動する。</p> 
 <p class="p1">VagrantfileにもAWS用のパラメータが追加されていて，インスタンスを生成するリージョンの指定などが可能だ。</p> 
 <pre class="p1">
config.vm.provider :aws do |aws|
   aws.region = &quot;eu-west-1&quot;
end</pre> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
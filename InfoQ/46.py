<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Vagrant 1.6、Dockerコンテナのサポートを追加</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/vagrant-1-6-docker"><em>原文(投稿日：2014/05/26)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Vagrantの新バージョン1.6には、これまでサポートされてきたVirtualBoxやVMware、AWSといった仮想化およびクラウドプロバイダに加えて、<a href="http://www.vagrantup.com/blog/feature-preview-vagrant-1-6-docker-dev-environments.html">Dockerベースの開発環境</a>のサポートが含まれている。</p> 
  <p>この新リリースによって、Vagrantユーザはこれまで使ってきたのと同じ仮想マシン操作およびワークフローを、Dockerコンテナを使って実行することが可能になる。Dockerプロバイダは繰り返し新規コンテナを作成するのに役立つDockerfilesからのコンテナや<a href="https://index.docker.io/">Docker index</a>サポートしている。そこには事前ビルドされた多くのリポジトリが並び、公式のUbuntuやCentOS、Fedoraのベースイメージをはじめ、MySQL、Java、MongoDBといった環境も含まれている。このリリースにはDockerプロバイダ向けの2つの新しいコマンドも含まれている。<em>docker-logs</em>はコネクタログを表示し、<em>docker-run</em>はコンテナ内における任意のコマンド実行を可能にする。LinuxコンテナをネイティブでサポートしないOS XやWindowsといったプラットフォーム上では、追加のソフトウェアを用意する必要なしに、コンテナを実行するプロキシLinux VMを自動で管理してくれる。</p> 
  <p>Dockerが<a href="http://www.infoq.com/news/2014/05/docker_0_11">バージョン1.0に近づくにつれ</a>、Dockerコンテナをサポートするツールも増えてきている。ちょうど数週間前、Red HatはコンテナおよびDockerテクノロジによるベアメタルシステム、仮想マシン、プライベートおよびパブリッククラウドにわたる、最新のアプリケーションデリバリーおよびオーケストレーションのための新たなLinuxコンテナプロジェクトを<a href="http://www.redhat.com/about/news/press-archive/2014/4/linux-container-innovations">発表した</a>。Googleのインフラストラクチャ担当バイスプレジデントのEric Brewer氏は、Linuxコンテナについてこう語っている。</p> 
  <blockquote> 
   <p>Googleではプロダクションシステムをサポートするのに、Linuxアプリケーションコンテナをフル活用しています。コンテナはハイレベルなランタイムの分離とデプロイメントの柔軟性をもたらし、管理している分散アプリケーションの複雑さを減らし、全体の運用効率を高めています。</p> 
  </blockquote> 
  <p>Vagrant 1.6には以下のような注目すべき<a href="http://www.vagrantup.com/blog/vagrant-1-6.html">新機能</a>も追加されている。</p> 
  <ol> 
   <li> <p>Windowsゲスト: Vagrant 1.6では、Vagrant環境 (VirtualBox, Hyper-V, EC2など) 内での<a href="http://www.vagrantup.com/blog/feature-preview-vagrant-1-6-windows.html">Windows実行のサポートが追加</a>され、ソフトウェアのインストールおよび設定にPowerShellスクリプト、Chef、Puppetなどを使うことができる。Windowsゲストには、Linuxにおける<em>vagrant ssh</em>に相当する<em>vagrant rdp</em>が提供され、Windows環境における完全なリモートデスクトップ環境へのシングルコマンドアクセスを可能にする。Microsoft Open TechではHyper-V用にパッケージされたVagrant boxの形で<a href="http://vagrantbox.msopentech.com/">Windowsの評価コピーを提供している</a>。</p> </li> 
   <li> <p>グローバルステータスとコントロール: Vagrant 1.6では<a href="http://www.vagrantup.com/blog/feature-preview-vagrant-1-6-global-status.html">新しい<em>global-status</em>コマンド</a>が導入され、システム上に生成したすべてのVagrant環境のステータスを表示する。Vagrant環境ごとに割り当てられたユニークなIDを使うことで、グローバルコントロールはVagrantfileのあるディレクトリだけでなく、任意のディレクトリからのコントロールを可能にする。グローバルなIDを指定して、destroy, up, suspend,...といった任意のVagrantコマンドを使うことができる。</p> </li> 
  </ol> 
  <p>ほかにも、現在のVagrantバージョンだけでなく、そのバージョンが古いか教えてくれる新しい<em>version</em>コマンドや、これまでは最初の<em>vagrant up</em>で実行するだけだったのが、任意の<em>vagrant up</em>や<em>vagrant reload</em>コマンドで実行するようプロビジョナーを設定できる機能、といったものも含まれている。またVagrant 1.6からは、<em>vagrant up</em>後に表示されるpost-upメッセージをVagrantfilesに入れることができ、boxをLZMAで圧縮することもできる。これは多くの場合、サイズをずっと小さくする。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
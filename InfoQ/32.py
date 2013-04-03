<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Docker: 継続的ソフトウェアデプロイの自動化</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/Docker;jsessionid=05CCDFC61B7CDAE5AF8863C0EBE4CAD1"><em>原文(投稿日：2013/03/27)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>PaaS プロバイダの <a target="_blank" href="https://www.dotcloud.com/">dotCloud</a> が，自社プラットフォームの重要なコンポーネントである <a target="_blank" href="https://github.com/dotcloud/docker/">Docker</a> をオープンソースとして公開した。Docker は <a target="_blank" href="http://en.wikipedia.org/wiki/LXC">LXC(LinuX Container)</a> テクノロジの実装で，Unixプロセスを分離実行する軽量仮想化 (lightweight virtualization) ソリューションを実現した高レベル API を拡張機能として備えることにより，ソフトウェア展開の自動化に必要な，再現性を持ったセキュアな実行環境を提供する。</p> 
 <p>Dockerでは標準コンテナ(Standard Container)という概念を用いている。これはソフトウェアコンポーネントとその依存対象 – バイナリ，ライブラリ，定義ファイル，スクリプト，仮想環境，jarファイル，gemファイル，tarアーカイブファイルなど – をひとつにまとめたもので，<a target="_blank" href="http://en.wikipedia.org/wiki/Cgroups">cgroup</a> をサポートする x64-bit Linux カーネル上で稼働する。このコンテナによって維持される適切な動作環境をラップトップや分散インフラストラクチャ，クラウドなどに展開することが可能で，継続的デプロイ(Continuous Deployment)やWebデプロイ，データベースクラスタ，SOAなど広い用途に応用できる，と <a target="_blank" href="http://www.kavistechnology.com/blog/docker-is-open-source/">Mike Kavis氏がブログで説明している</a>。</p> 
 <blockquote> 
  <p>アプリケーション技術者である私に関係のある Docker のユースケースは，継続的デリバリのプロセス合理化への応用です。メインフレームの頃からクライアントサーバ，そしてクラウドの現在まで，私はさまざまな場所で仕事をしてきました。そのキャリアすべてにおいて，アプリケーションのテストを成功させるために動作環境を統一するという作業は，悪夢以外の何ものでもなかったのです。作業プロセスの優劣の問題ではありません。コードが開発からQA，さらに製品ステージへと移行する過程において，これらの環境が一環して同じであったことは一度としてありませんでした。結局は製品リリースでの品質が最終結果ということになるのです。&quot;テストでは動いていました&quot; というのは，&quot;いま小切手を送るところです&quot; というのと同じくらい，当てにならないフレーズでした。</p> 
  <p>継続的デリバリ (CD/Continuous Delivery) が実現すれば，コードととともにその<em>実行環境全体</em>も開発からQA，製品ステージへと引き継げるようになります。設定が問題だとか，システムが違うとか，弁解する必要はもはやありません。製品で動作しないものはテストでも動かないからです。Docker を使うことで，このような CD プロセスを自動化するスクリプトの記述が可能になります。新しい環境の構築が，セットアップや設定の問題に対処する必要なく，素早くできるようになりますから，マーケットへの製品展開も迅速になるでしょう。</p> 
 </blockquote> 
 <p>dotCloud の CEO である Solomon Hykes氏は <a target="_blank" href="http://www.youtube.com/watch?feature=player_embedded&amp;v=wW9CAH9nSLs">PyCon でデモを行ったとき</a>，Docker は再現性のある軽量仮想ソリューションである，なぜなら &quot;プロセスレベルで独立していて，自身のファイルシステムを所有している &quot; からだ，と説明していた。APIを使うことでシステム管理者は，コンテナ上で起動，停止，コピー，一時停止，コミット，標準ストリームへのアタッチ，ファイルシステム更新のリストなど，数多くの操作を実行することが可能になる。</p> 
 <p>Docker の <a target="_blank" href="https://github.com/dotcloud/docker/">主な機能</a> は次のようなものだ。</p> 
 <blockquote> 
  <ul> 
   <li> <p>ファイルシステムの分離： 各プロセスコンテナは完全に独立したルートファイルシステム上で動作する。</p> </li> 
   <li> <p>リソースの分離： CPUやメモリなどのシステムリソースは cgroup を使用して，各プロセスコンテナに別々に割り当てることができる。</p> </li> 
   <li> <p>ネットワークの分離： 各プロセスコンテナは自身のネームスペース内で動作し，自身の仮想インターフェースとIPアドレスを保持する。</p> </li> 
   <li> <p>コピー・オン・ライト： ルートファイルシステムはコピー・オン・ライトを使用して作成されている。これによってデプロイが極めて高速になるとともに，メモリおよびディスクの使用量も軽減される。</p> </li> 
   <li> <p>ロギング： 各プロセスコンテナの標準ストリーム(stdout/stderr/stdin) は収集され，リアルタイムあるいはバッチ取得のためにログされる。</p> </li> 
   <li> <p>更新管理： コンテナのファイルシステムの変更を新たなイメージにコミットして，別のコンテナを作成するために再利用することができる。テンプレートや手作業による設定の必要はない。</p> </li> 
   <li> <p>対話型シェル： Docker では仮想ttyをアロケートして，任意のコンテナの標準入力にアタッチすることができる。一時的な対話型シェルを実行するようなことも可能だ。</p> </li> 
  </ul> 
 </blockquote> 
 <p>現時点では，Docker は Ubuntu 12.04 および 12.10 でテストされている。ただし dotCloud によれば，Linux 2.6.24 以降であれば動作可能なはずだ。<a target="_blank" href="http://www.vagrantup.com/">Vagrant</a> を使用すれば，<a target="_blank" href="https://www.virtualbox.org/">VirtualBox</a> を通じて Windows や Mac OS X にもインストールすることができる。 Docker は Go で記述されていて，Linux の <a target="_blank" href="http://blog.dotcloud.com/kernel-secrets-from-the-paas-garage-part-24-c">cgroup</a> と <a target="_blank" href="http://blog.dotcloud.com/under-the-hood-linux-kernels-on-dotcloud-part">ネームスペース</a>，<a target="_blank" href="http://aufs.sourceforge.net/aufs.html">AUFS</a> – コピー・オン・ライト機能を持ったファイルシステム，<a target="_blank" href="http://lxc.sourceforge.net/">LXC</a> スクリプトなどを利用している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Docker, Inc: dotCloud、オールインワンのコンテナ技術に賭ける</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/10/dotcloud-renamed-docker"><em>原文(投稿日：2013/10/29)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>PaaSプロバイダのdotCloudが、自らの最新オープンソーステクノロジーに合わせて<a href="http://blog.docker.io/2013/10/dotcloud-is-becoming-docker-inc/">社名を変更した</a>。<a href="http://www.docker.com/" target="_blank">Docker, Inc</a>はスタンドアロンのPaaSプロダクトを提供し続けるが、社名と同じソフトウェアの成長と商業化にそのフォーカスを移すことになる。Dockerの急激な成長とプロダクトの向かう先について、CEOのBen Golub氏に話を聞いた。</p> 
  <p><a href="http://www.docker.io/" target="_blank">Docker</a>とは何か? これは開発者やシステム管理者が、Linux環境において自己充足のアプリケーションコンテナをデプロイするのを可能にするオープンソースエンジンだ。（悪く言う人がすぐに指摘するように）正直なところ新しいものではないが、DockerはLinuxユーザが今日にでも利用できるテクノロジーの上にできている。CEOのBen Golub氏は、目標は「ボックスを再発明すること」ではなく、他人の仕事を引き受け、コンテナを使いやすくし、標準的なツールに統合することだ、と語る。<a href="http://www.docker.io/" target="_blank">Docker.io</a>プロジェクトは2013年3月にリリースされて以来、<a href="http://www.businesswire.com/news/home/20131029005746/en/dotCloud-Docker">プレスリリース</a>にあるよう劇的に成長している。</p> 
  <blockquote> 
   <p>ローンチして7ヶ月、Dockerプロジェクトは開発者とDevOpsの両方のコミュニティの後押しで、急速に成長しているエコシステムに不可欠な要素になっています。</p> 
   <p>主なものを挙げると、</p> 
   <ul> 
    <li>140,000を超えるコンテナのダウンロード</li> 
    <li>GitHubにおける6,700を超えるスターと800を超えるフォーク</li> 
    <li>3か月で600を超えるGitHub Dockerfileの作成</li> 
    <li>Dockerパブリックリポジトリにおける何千ものコンテナ化されたアプリケーション</li> 
    <li>このオープンソースエンジン上に構築された150を超えるプロジェクト</li> 
    <li>世界30都市で50を超えるミートアップ</li> 
    <li>約200名のコントリビュータ、その92パーセントは社外の人</li> 
    <li>13,000を超えるオンラインのDockerトレーニング修了者</li> 
    <li>Dockerを利用していると公にしている<a href="http://api.yandex.com/cocaine/">Yandex</a>、<a href="http://www.rackspace.com/blog/how-mailgun-uses-docker-and-contributes-back/">Rackspace</a>、<a href="https://speakerdeck.com/teddziuba/docker-at-ebay">eBay</a>、<a href="http://www.youtube.com/watch?v=-Lj3jt_-3r0">CloudFlare</a>といった企業</li> 
    <li><a href="http://community.opscode.com/cookbooks/docker">Chef</a>、<a href="http://forge.puppetlabs.com/garethr/docker">Puppet</a>、Travis、<a href="https://github.com/georgebashi/jenkins-docker-plugin">Jenkins</a>など、非常に重要なエンタープライズプロジェクトとのインテグレーション</li> 
    <li><a href="http://coreos.com/">CoreOS</a>、<a href="http://deis.io/">Deis</a>、<a href="https://flynn.io/">Flynn</a>、<a href="https://orchardup.com/">Orchard</a>など、Docker上に専用ビジネスを立ち上げる企業の増加</li> 
   </ul> 
  </blockquote> 
  <p>Dockerの勢いに注目して、パートナーシップを競って結んでいるところもある。Red Hatは最近、Red Hat PaaSプラットフォーム、OpenShiftとのインテグレーションなど、複数の分野におけるDockerとの<a href="http://www.redhat.com/about/news/press-archive/2013/9/red-hat-and-dotcloud-collaborate-on-docker-to-bring-next-generation-linux-container-enhancements-to-openshift" target="_blank">「技術的コラボレーション」を発表</a>した。さらに、オープンソースIaaSプロジェクトのOpenStackは、最新リリースであるコードネーム “Havana”に<a href="http://blog.docker.io/2013/10/openstack-havana-docker/" target="_blank">Dockerを組み入れている</a>。</p> 
  <p>なぜDockerは伸びるのか? Golub氏は「コンテナ化は次世代コンピューティングを実現する最も重要な要素の1つ」であり、仮想マシンはそれにふさわしい単位ではないと考えている。人々はアプリケーションを使って仕事をしたいのであり、Dockerのような軽量コンテナがカプセル化とインターオペラビリティの絶妙な組み合わせをもたらすと信じている。Golub氏によると、Dockerにはまだ改良の余地がたくさんある。安定性とドキュメントの改善のほか、開発者はコンテナを組織化することで、複雑な分離システムを作成する方法を求めている。システム管理者は所定のホストにあるコンテナを特定し、そのパフォーマンスをモニタリングするための優れたツールを求めている。だが、最大のギャップは期待されているものだ。Dockerチームは今もなお、ユースケースを開拓し、人々がどのように使いたいのか学び続けている。</p> 
  <p>オープンソースに引き続きコミットすることを約束する一方、Docker, Incは明確な商業化計画を立てている。</p> 
  <blockquote> 
   <p>2014年の初めに、Docker, Inc.はDocker関連プロダクトを立ち上げます。これには開発者向け（Docker as a Service）と企業向け（プライベートレジストリ、オーケストレイション、モニタリングを含む）の管理サービスが含まれます。また、Docker, Inc.からのLevel IIIサポートが受けられるサービスプロバイダのパートナーネットワークを構築する計画も発表しました。</p> 
  </blockquote> 
  <p>dotCloud PaaSの将来は、少々怪しくなっている。Docker, IncはPaaSサービスを提供し続けると言っているが、会社のフォーカスは明確にDockerそのものにある。スタンドアロンのPaaSプロダクトはすぐれた顧客体験を提供するが、Golub氏は「あなたの一番の顧客があなたを大きくする」ことに気付いた。彼は、従来のPaaSサービスを通してであれ、Dockerのようなコンテナを通してであれ、開発者は間違いなくPaaSのような環境を必要としていると信じている。Dockerをリリースして、<em>これ</em>が会社として、コミュニティとして、彼らにより大きな影響を及ぼすチャンスをもたらすことがはっきりした。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
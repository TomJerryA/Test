<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Docker Indexがプライベートリポジトリとウェブフックを提供</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/docker-private-repositories"><em>原文(投稿日：2014/03/24)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="https://www.docker.io/">Docker</a>を提供する<a href="http://www.docker.com/">Docker Inc.</a>が新しいサービスを発表した。初の商用サービスである<a href="https://index.docker.io/help/docs/#repositories">プライベートリポジトリ</a>も含む。<a href="https://index.docker.io/">Docker index</a>はウェブフック、トリガ、<a href="https://index.docker.io/help/docs/#trustedbuilds">Trusted Builds</a>のためのリンク、メールによる通知を提供する。</p> 
  <p>Docker indexはDockerの<a href="https://docs.docker.io/en/latest/terms/image/#image-def">イメージ</a><a href="https://docs.docker.io/en/latest/terms/repository/#repository-def">リポジトリ</a>のための<a href="https://docs.docker.io/en/latest/terms/registry/">レジストリ</a>だ。リポジトリはプレビルドイメージを共有するための手段であり、毎回、全員が環境を再作成しなくてもよいようにする。雑な類推だが、Dockerにとってのリポジトリは、Vagrantにとっての<a href="http://docs.vagrantup.com/v2/boxes.html">ボックス</a>だ。プライベートリポジトリが利用できるようになることで、誰がリポジトリにプッシュやリポジトリからのプルができるのかを制御できる。また、イメージタグを使ってリポジトリを閲覧し、ファイルシステムの変更を見ることができる。</p> 
  <p>リポジトリへのプッシュからウェブフックを起動することもできる。ウェブフックのURLは下記のJSONペイロードを伴ったHTTPのPOSTリクエストを受けつける。</p> 
  <pre>
{
   &quot;push_data&quot;:{
      &quot;pushed_at&quot;:1385141110,
      &quot;images&quot;:[
         &quot;imagehash1&quot;,
         &quot;imagehash2&quot;,
         &quot;imagehash3&quot;
      ],
      &quot;pusher&quot;:&quot;username&quot;
   },
   &quot;repository&quot;:{
      &quot;status&quot;:&quot;Active&quot;,
      &quot;description&quot;:&quot;my docker repo that does cool things&quot;,
      &quot;is_trusted&quot;:false,
      &quot;full_description&quot;:&quot;This is my full description&quot;,
      &quot;repo_url&quot;:&quot;https://index.docker.io/u/username/reponame/&quot;,
      &quot;owner&quot;:&quot;username&quot;,
      &quot;is_official&quot;:false,
      &quot;is_private&quot;:false,
      &quot;name&quot;:&quot;reponame&quot;,
      &quot;namespace&quot;:&quot;username&quot;,
      &quot;star_count&quot;:1,
      &quot;comment_count&quot;:1,
      &quot;date_created&quot;:1370174400,
      &quot;dockerfile&quot;:&quot;my full dockerfile is listed here&quot;,
      &quot;repo_name&quot;:&quot;username/reponame&quot;
   }
}
</pre> 
  <p><a href="http://blog.docker.io/2013/11/introducing-trusted-builds/">Trusted Builds</a>はリポジトリとGitHubのアカウントをひも付け、GitHubリポジトリにポストコミットフックを追加する。このフックはDocker index内のイメージのビルドとアップデートを起動し、イメージと対応する<a href="https://docs.docker.io/en/latest/reference/builder/">Dockerfile</a>の関係をメンテナンスする。</p> 
  <p>Trusted Buildsはふたつの改善が行われた。リンクとトリガだ。リンクによってTrusted Buildのリポジトリが同期されるようになる。どのようなアップデートでもリンクされているTrusted Buildは他のTrusted Buildのアップデートを起動するのだ。トリガは単純なプロセスであり、リポジトリのビルドを起動する。GitHubには何もコミットしなくていい。</p> 
  <pre>
  $ curl --data &quot;build=true&quot; -X POST https://index.docker.io/u/samalba/docker-registry/trigger/b2562468-aea0-11e3-a39e-b6db5999dfec/
</pre> 
  <p>Docker indexのユーザがイベントが発生したことをメールで受け取れるようになった。Trusted Buildや他のユーザのコミットなどのイベントだ。</p> 
  <p>Docker indexの新しいサービスはDockerレジストリの選択肢を増やす。<a href="https://quay.io/">Quay.io</a>はすでに同じようなサービスを提供している。</p> 
  <p>プライベートリポジトリはDocker Incの初の<a href="https://index.docker.io/plans/">商用サービス</a>だ。彼らは支払いが必要なサービスを他にも構想している。同社の<a href="http://blog.docker.io/2014/03/introducing-private-repos-webhooks-and-more/">ブログ</a>によれば、</p> 
  <blockquote>
    Docker.io上のすべてのサービスは現在、無料です。これはDocker周辺のコミュニティを活発にし育てる上で重要なことです。したがってほとんどのサービスは引き続き無料で提供します。しかし、Benがすでに発表したように、Dockerに継続して投資していくには、オプションの商用サービスを提供する必要があります。プライベートリポジトリはその一環です。
  </blockquote> 
  <p>料金はリポジトリ数が5つで月額7ドル。最大５０リポジトリで月額50ドル。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
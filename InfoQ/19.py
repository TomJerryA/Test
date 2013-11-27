<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>"Luca, フォース(force)を使え" - Jenkins開発者が１ヶ月分のGitHubコミットを消失</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/use-the-force"><em>原文(投稿日：2013/11/12)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>昨日，<a href="https://groups.google.com/forum/#!topic/jenkinsci-dev/-myjRIPcVwU">Jenkinsプロジェクト</a>の開発者が誤って，JenkinsコードベースのGitリポジトリをストアしている<a href="https://github.com/jenkinsci/">GitHubレポジトリ</a>に<a href="https://groups.google.com/d/msg/jenkinsci-dev/-myjRIPcVwU/t4nkXONp8qgJ">強制的なプッシュ</a>を実行してしまい，数ヶ月間のコミットを紛失した。理解あるコミュニティによって問題はすぐに解決されたものの，この件は，GitHubの備えるオープン性 (<a href="https://github.com/jenkinsci">Jenkins CIの機構</a>と組み合わせれば，誰でも任意のリポジトリにコミットできる) が，問題を拡大する可能性のあることを浮き彫りにした。</p> 
  <p>Ｇｉｔの強制プッシュ(force push) – <code>git push -force</code>で実行する – は，サーバに指定したコンテントをプッシュして，リファレンス(ブランチあるいはタグ)の内容を置き換えるように指示するものだ。通常，Gitのリポジトリに許されているのは，<em>ファーストフォワード</em>プッシュに限定されている - すなわち，プッシュするリファレンスは，その先祖として現行のリファレンスを持っていなければならない。強制プッシュはこの制限を取り除いて，現行のコンテントを置き換えることができる。</p> 
  <p>Gitリポジトリの設定では，<a href="http://www.kernel.org/pub/software/scm/git/docs/git-config.html">git config</a>の値 &quot;<code>receive.denyNonFastForwards true</code>&quot; を使って，この動作の許可あるいは禁止を指定することができる。強制的な操作の防止にはこれを利用する。</p> 
  <p>強制的なプッシュが便利な場合もある。例えば <code>git filter-branch</code> のようなリファクタあるいはフィルタ操作が実行されると，コミットが現行ブランチの先祖ではなくなるため，通常の操作は不可能になる。別の利用ケースとして，ミラーリングが有効な場合に，２つのリポジトリの内容を同期させることで，エラーを発生させずに変更内容をパスすることができる。</p> 
  <p><a href="https://groups.google.com/d/msg/jenkinsci-dev/-myjRIPcVwU/t4nkXONp8qgJ">今回のケースで起きた</a>のは次のようなものだ - Gerritミラーリングプラグインをテスト中だったLucaは，Jenkinsリポジトリ用として，リポジトリセットをローカルにチェックアウトしていた。Gerritのミラーはこのローカルリポジトリからコンテントを取得するようにセットアップされていた。結果的にすべてのリポジトリが，彼の手元にあるチェックアウトからミラーするようになっていたのだ。不運なことに，そのレポジトリはしばらく更新されていなかったため，すべてのリポジトリを以前の状態にリセットすることになってしまった。</p> 
  <p>幸運なことに，現在はすべてのリポジトリが元に戻されている - Gitバージョン管理システム(あるいはどのDVCSでも)のメリットのひとつとして，任意のクローンからリポジトリを再生可能なことがあり，これを実行するのは簡単だった。GitHubのサポートも非常に効果的だった。コンテントを再取得するために，サーバ側のreflog (ブランチ内の変更を識別するために使用)を提供してくれたのだ。しかし，将来的にこの問題を緩和するためには，２つの重要な疑問に答を出さなければならない：</p> 
  <ul> 
   <li>ユーザが複数のリポジトリにコミットするのは妥当なことだろうか，あるいはレビュー/プルリクエストのように，管理されたチャネルを通じて変更を伝えるべきだろうか？</li> 
   <li>GitHubにおいて，<code>denyNonFastForwards</code>設定オプションを提供することは適切だろうか？</li> 
  </ul> 
  <p>GitHubの有力なライバルである<a href="http://bitbucket.org">BitBucket</a>では，<a href="https://bitbucket.org/site/master/issue/3338/git-allow-option-to-enable-disable-force">nonFastForwardsを無効にするオプション</a>を提供している。BitBuckerはAtlassianによって継続され，現在はDVCSのひとつであるMercurialの公式サイトとして使用されている。しかしながら，BitBucketが有名になったのはGitのホスティングソリューションとしてであり，そのGit管理ソリューションである<a href="https://www.atlassian.com/it/software/stash/overview">Atlassian Stash</a>はGitリポジトリに特化したものだ。</p> 
  <p>皮肉にもLucaは，Gerritをベースとするリポジトリを提供する<a href="http://gerritforge.com">GerritForge</a>という会社を持っている。先日著した <a href="http://www.infoq.com/articles/learning-gerrit-code-review"> Learning Gerrit Code Review</a> という本は，InfoQでもレビューしたばかりだ。JenkinsのリポジトリがGerritのようなレビューベースのツールを使っていれば，今回のことは起きなかったかも知れない。</p> 
  <p>GitHubがnonFastForwardsの設定機能を提供するまでの措置として，Jenkinsの開発者は，GitHubリポジトリへのプッシュを追跡して実行した変更とコミットのSHA値を記録する<a href="https://groups.google.com/forum/#!topic/jenkinsci-dev/dD-sumd81pU">ツールを作成した</a>。皮肉なことに彼らは，<code>rsync</code>を使ってリポジトリを複数の場所にバックアップすることを提案している。</p> 
  <p>強力な機能には大きな責任が伴う。GuiHubでforceオプションを使用するのはまさにそのケースだ。今後GitHubがこれを禁止するオプションを提供するかどうかに関わらず，バックアップされていない巨大な公開リポジトリをホストする場合には注意が必要だ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
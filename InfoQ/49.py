<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Git 2.0リリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/05/git-2-0"><em>原文(投稿日：2014/05/30)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Git 2.0がリリースされた。リリース候補版から1ヶ月程度でのリリースだ。ビットマップインデックスによる性能改善、センシブルデフォルトによる初心者の利便性向上などが特徴だ。既存ユーザにとっては、前のバージョンと同等の機能を維持する選択肢もある。</p> 
  <p>Gitのユーザは初期のリリースバージョンからこれらの機能に刺激を受けてきた。GitのメンテナであるJunio Hamano氏は次のように書いている(<a href="http://git-blame.blogspot.co.uk/2014/05/git-20.html">抜粋</a>)。</p> 
  <blockquote>
   ..新しいリリースには刺激的なものがない(というひともいるかもしれません)が、私たちはまさにそのような言葉を既存のユーザから聞きたいのです。近頃のリリースでは、2.0以前の新しいデフォルトをユーザが使えるようにするためのノブを追加してきました。そして、1.x系と2.0リリースとの間には操作上の違いがあることを警告してきました。これまでGitを使ってきたユーザはきっと現時点までに十分に準備できていると思います。そして、&quot;Git 2.0&quot;は&quot;デフォルトを放り投げる&quot;最終ステップとして設計されています。
  </blockquote> 
  <p>大きな改善点は以下の通り。</p> 
  <ul> 
   <li>pushがデフォルトで&quot;simple&quot;になる(&quot;matching&quot;ではなく)。カレントのブランチをリモートの同じ名前のブランチに追加する。</li> 
   <li>パスの指定無しで&quot;git add -u&quot;あるいは&quot;git add -A&quot;を実行した場合、サブディレクトリ内で実行した場合でもツリー全体を処理する。カレントディレクトリに対する追加を制限するにはピリオドを追加する(&quot;git add -u .&quot;あるいは&quot;git add -A .&quot;)必要がある。</li> 
   <li>&quot;git add &lt;path&gt;&quot;と&quot;git add -A &lt;path&gt;&quot;が同じ挙動になる。</li> 
  </ul> 
  <p>Felipe Contreras氏は<a href="http://felipec.wordpress.com/2014/05/29/git-v2-0-0/">後方互換性がない点</a>について詳しく説明している。</p> 
  <p>ほかにも改善点がある。</p> 
  <ul> 
   <li>&quot;-h&quot;(no header)と&quot;-c&quot;(count)オプションをつけると&quot;git grep&quot;がネイティブのgrepに似た挙動になる。</li> 
   <li>コミットを作成するコマンド、例えば、&quot;-pull&quot;や&quot;-rebase&quot;は&quot;--gpg-sign&quot;オプションを受け付ける(<a href="http://mikegerwitz.com/papers/git-horror-story">サインドコミットについてはこちらを参照</a>)。</li> 
   <li>&quot;pull.ff&quot;(ファーストフォワードのみ受け付け)、&quot;git reset&quot;のための&quot;-N&quot;オプション、&quot;commit.gpgsign&quot;(&quot;git commit&quot;を使ったときに常にサインする)などの新しいオプションの追加。</li> 
   <li>.gitignoreファイルの空白が警告され無視される(クオートされていれば無視されない)。</li> 
  </ul> 
  <p>性能改善と実装の改善もなされている。</p> 
  <ul> 
   <li><a href="http://www.eclipsecon.org/2013/sites/eclipsecon.org.2013/files/Scaling%20Up%20JGit%20-%20EclipseCon%202013.pdf">JGitのビットマップインデックス</a>が移植された。クローンやフェッチ処理でのカウントフェーズが劇的に改善する(インデックス用にいくらかのディスクスペースが必要)。</li> 
   <li>&quot;git log --cc&quot;による、複数のペアレントの差分表示が最適化された。</li> 
  </ul> 
  <p>詳細については<a href="http://article.gmane.org/gmane.comp.version-control.git/250341">リリースノート</a>で確認できる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
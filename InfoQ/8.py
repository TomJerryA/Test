<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Firefox 26がJavaをブロック</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/firefox-26-blocks-java"><em>原文(投稿日：2013/12/11)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>MozillaのFirefox 26は現在，セキュリティ上の懸念を理由に，デフォルトですべてのJavaプラグインをブロックしている。ただしユーザが希望すれば，プラグインを実行することが可能だ。</p> 
  <p>ブラウザに対するセキュリティの懸念から，<a href="http://www.infoq.com/jp/news/2011/10/mozilla-java">MozillaがブロックリストへのJavaの登録を検討した</a>のは2011年のことだ。しかしその時点では，何の決定も下されなかった。今年に入ってMozillaでは，使用するプラグインをユーザが選択できるようにするClick-to-Play(CtP)機能を開発し，そのテストを続けてきた。しかしプロセスは順調に進まず，Javaに依存するWebサイトやユーザに影響を与えている。</p> 
  <p>9月になってMozillaは，<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=914690">全バージョンのJavaバージョンをunsafeとマークすると決定</a>して，Firefox 24でそれを実行した。しかし，それによってアプリケーションやWebサイトが動作しなくなってしまったユーザのほとんどが，何が起こったのかを理解していなかった。彼らはCtPを使ってJavaを有効にできるということが分からなかったため，いくつかのプラグインを見ることができず，結果的にCtPは役に立たなかった。それどころか<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=914690#c65">CtPのUIが表示されないケースさえあったのだ</a>。少なくともいくつかの国では，多数のネットバンクユーザが影響を被っている:</p> 
  <blockquote> 
   <p><a href="https://bugzilla.mozilla.org/show_bug.cgi?id=914690#c40">Knud Berggreen</a>: Java Plugin 7 update 45をブロックしないでください！ 国中のログインがブロックされて，デンマーク国民すべてに影響します。</p> 
   <p><a href="https://bugzilla.mozilla.org/show_bug.cgi?id=914690#c91">etoxsg</a>: Javaプラグインをインストールしなくてもサービスを提供できるオンライン銀行は，ノルウェーには数えるほどしかありません。ノルウェー，スウェーデン，デンマークの全世帯の90%が，オンラインバンキングにJavaプラグインを必要としているのです。そうですから，Mozillaが事前の予告なくすべてのJavaをブロックすると決めたとき，私は友人や近所の人たちや家族を相手に，8件の訪問対応と15件の電話対応をしなければなりませんでした。</p> 
  </blockquote> 
  <p>その他のコミュニティの反応は:</p> 
  <blockquote> 
   <p><a href="https://bugzilla.mozilla.org/show_bug.cgi?id=914690#c33">Tomasz</a>: あからさまな言い方で申し訳ありません，でもユーザとして言いたい – FFがJavaをブロックするなんて，こんな超無責任な決定を一体誰がしたんですか！</p> 
   <p>おかげで私は，オンライン取引口座にログインできなくなってしまいました。銀行で使っているアプリが &quot;Javaバージョン1.5以降が必要です&quot; とメッセージボックスを表示するのです。セキュリティ問題どころではありません。単に動かないのです。</p> 
   <p><a href="https://bugzilla.mozilla.org/show_bug.cgi?id=914690#c30">ipatrol</a>: あなた方，頭がおかしくなったんじゃないですか？ Javaは動的コンテントを支える３大テクノロジのひとつなんですよ！ ハンマーを持ち出して些細なバグを叩き潰して，ちょっとしたUIの微調整って，落ち着き払って何を言ってるんですか？</p> 
  </blockquote> 
  <p>Java SEエンジニアリングマネージャの<a href="https://bugzilla.mozilla.org/show_bug.cgi?id=914690#c92">Roger</a>は，この問題についてこう述べている:</p> 
  <blockquote> 
   <p>FFがJava 7u45の脆弱性を指摘していることについて，非常に多くの人々がjava.comサイトに報告を寄せています。その対策はIEを使用することだ，と言う人もたくさんいます。関連用語の検索結果数は天井知らずです。今回の処置を実施したFFチームの，これがエンドユーザのソリューションとして意図したことだったのでしょうか。メッセージ表示に関する混乱と，Javaを実行可能にする方法のユーザビリティに問題があったのではないかと思います。今回の新たなブロックが，FFユーザの行動にどのような影響を与えているか，何か統計情報はありませんか？</p> 
  </blockquote> 
  <p>Mozillaは一旦はブロックを解除することにしたが，この措置はCtPが修正されるまでの一時的なものだった。10月末にMozillaは，再びセキュリティ上の問題を理由に，ベータ版の<a href="https://blog.mozilla.org/futurereleases/2013/10/31/click-to-play-plugins-ready-to-test-in-firefox-beta/">FirefoxでFlash以外のプラグインをブロックする</a>と発表した。</p> 
  <p>結果的に，今年末にリリースされたFirefox 26では，<a href="http://www.mozilla.org/en-US/firefox/26.0/releasenotes">すべてのWebサイトを対象としてJavaプラグインはデフォルトでブロックされている</a>。CtPユーザインターフェースがユーザに対して，必要な場合にJavaを有効にする方法を知らせるのに十分役立っているか，疑問の余地は残る。</p> 
  <p>ユーザのコンピュータ内のセキュリティホールに関しては，長い間，WindowsとFlashが非難の的になってきた。そして今では，Javaがその圧力を感じるようになっている。Oracleはこれまで，この問題にそれほど注意を払っていないようだった。しかしその考え方は改められたらしく，この10月には四半期に最低１回提供されるCritical Patch Updateとして，127件のセキュリティを修正するアップデートがリリースされた。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
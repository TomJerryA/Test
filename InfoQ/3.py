<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Ruby 2.1.0リリース，新しいGCを提供</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/ruby21"><em>原文(投稿日：2013/12/30)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p class="MsoNormal">Ruby 2.1の公式リリースが<a href="http://www.ruby-lang.org/en/news/2013/12/25/ruby-2-1-0-is-released/">公開された</a>。<a href="http://www.infoq.com/news/2013/09/ruby-2-1-gc-revamp">待望されていた</a>多数の改善の中にはガベージコレクタの大幅な変更も含まれ，将来的なパフォーマンスの向上を期待させている。
   <o:p></o:p></p> 
  <p class="MsoNormal">Ruby 2.1のガベージコレクタは世代別ガベージコレクションを実装したもので，RubyではこれをRGenGC(Restricted Generational Garbage Collection)と呼んでいる。これによって，従来のバージョンで使用されていた “マーク＆スイープ” 方式の実装は置き換えられることになる。2013年4月にRuby開発者のKoichi Sasada氏が行ったプレゼンテーションによると，Ruby開発者たちには，保護されたオブジェクトと安全でないオブジェクトを同一ヒープ上で扱うことのできるGCアルゴリズムを実装するという課題があった。
   <o:p></o:p></p> 
  <p class="MsoNormal">新しいGCを使用するために，既存のCエクステンションをすべて書き直すというのは現実的ではない。そのためRGenGCでは，実装の一部としてライトバリア(Write-Barrier)が使用されている。RubyConf 2013の<a href="http://www.atdot.net/~ko1/activities/rubyconf2013-ko1_pub.pdf">プレゼンテーション</a>でSasada氏が説明したように，RGenGCは A) 世代別GCをまったく実装しない(Ruby 2.0以前のように)，B) すべてのCエクステンションの書き換えが必要な世代別GCを実装する，という２つの選択肢のどちらでもない，第３の方法を提供しているのだ。
   <o:p></o:p></p> 
  <p class="MsoNormal">RGenGCはパフォーマンスの向上を達成しながら，同時に既存のエクステンションとの高い互換性を実現している。一般的なオブジェクトであるArrayやString, Hash, Object, Numericなどはいずれもライトバリアなので，RGenGCシステムのメリットを享受することが可能だ。内部および外部ライブラリに関する今後の開発によって，将来的にはさらなるパフォーマンスの向上も期待できる。
   <o:p></o:p></p> 
  <p class="MsoNormal">新しいガベージコレクションシステムだけが改善点ではない。RDoc 4.1.0やRubyGems 2.2.0，他にもいくつかのライブラリが更新されている。2.1の変更点に関する完全なリストは，プロジェクトのGitHubページにある<a href="https://github.com/ruby/ruby/blob/v2_1_0/NEWS">リリースノート</a>で確認できる。
   <o:p></o:p></p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
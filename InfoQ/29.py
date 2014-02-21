<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>GoogleのJavaコーディング規約</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/google-java-coding-standards"><em>原文(投稿日：2014/02/10)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Googleは、最近、<a href="http://google-styleguide.googlecode.com/svn/trunk/javaguide.html">Javaコーディング規約</a>の完全な定義を公開した。 この規約は強制力を持つ厳格なルールであり、Google全体で従うべきものだ。単なるフォーマットだけでなく、他の約束事やコーディング規約についても書かれている。</p> 
  <p>このドキュメントは、6つの主要な部分からなる。ソースファイル基礎、ソースファイル構成、フォーマット、ネーミング、プログラミングプラクティス、そして、Javadocだ。<i>ソースファイル基礎</i>は、ファイル名、ファイルエンコーディング、空白文字、特殊文字について、また、<i>ソースファイル構成</i>は、ライセンス情報、パッケージやインポート文、そして、クラスメソッドの順序付けについて書かれている。<i>フォーマット</i>は、大括弧やインデント、行の折り返し、空白、丸括弧、enum、配列、switch文、アノテーション、コメント、モディファイヤについて説明する。<i>ネーミング</i>は、パッケージ、クラス、メソッド、コンスタント、フィールド、ローカル変数、型変数などの識別子について説明し、キャメルケースを定義している。<i>プログラミングプラクティス</i>は、@Override、例外、スタティックメンバ、ファイナライザに関する章であり、<i>Javadoc</i>は、Javadocの書式設定方法やどのような場面で必要かについて書かれている。</p> 
  <p>ガイドに含まれているいくつかの項目をここで紹介する。</p> 
  <ul> 
   <li>ワイルドカードを使ったインポートは使わない。</li> 
   <li>オーバーロードは連続して現れる。</li> 
   <li>ボディが空や1行であっても、大括弧を使う。</li> 
   <li>インデントはスペース2つにする。</li> 
   <li>カラム制限は80か100文字。</li> 
   <li>C形式の配列宣言は使わない。</li> 
   <li>スイッチ文ではデフォルト文が必要。</li> 
   <li>Java言語仕様で推奨された順番で識別子が現れる。</li> 
   <li>コンスタントはCONSTANT_CASEを使う。コンスタントはすべてスタティックファイナルフィールドだが、すべてのスタティックファイナルフィールドがコンスタントの訳ではない。</li> 
  </ul> 
  <p>さらに詳細を知りたい場合は、<a href="http://google-styleguide.googlecode.com/svn/trunk/javaguide.html">Google Javaスタイル</a>を読もう。Oracleの公式な<a href="http://www.oracle.com/technetwork/java/javase/documentation/codeconvtoc-136057.html">Javaプログラミング言語のコード規約</a>がある。Googleには、C++やObjective-C、Python、Shell、HTML/CSS、JavaScript、Lispのような他の言語の<a href="https://code.google.com/p/google-styleguide/">スタイルガイド</a>もある。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
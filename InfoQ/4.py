<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Coverity 7.0がリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/coverity-7"><em>原文(投稿日：2014/01/24)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://www.coverity.com/why-coverity/#Developers">Coverity</a>がバージョン7.0をリリースした。21の新しく強力なC#に対する分析アルゴリズムが追加されており、C#のコードの欠陥検出の精度が向上している。さらに、リソースのリークや並列処理の問題、null参照なども修正されている。</p> 
  <p>この新しいリリースには<a href="https://www.owasp.org/index.php/Main_Page">Open Web Application Security Project</a> (OWASP)に対する新しいカバレッジが含まれている。また、Javaアプリケーションの脆弱性に対する追跡機能も強化されており、JavaとC/C++のコードに対する17の強化された分析が含まれている。これらの分析はクラッシュや不正確な処理、予測できない振る舞いを検出することができる。</p> 
  <p>Coverity 7は<a href="http://www.sonarqube.org/">SonarQube</a>統合を提供する。これは、開発者が単一のワークフローだけで Javaアプリケーションの幅広い欠点を確認し管理できる。さらに、新しいセキュリティ監査とコンプライアンスビューも提供される。</p> 
  <p>今回のリリースは<a href="http://www.eclipse.org/">Eclipse</a>とVisual Studioと統合されており、さらにAndroidとWindRiverで動作するデバイスの単体テスト分析も提供する。また、<a href="http://en.wikipedia.org/wiki/Objective-C">Objective-C</a>とC/C++の開発で広く使われているClangコンパイラもサポートする。</p> 
  <p>InfoQはCoverityのプロダクトマーケティング部門のシニアディレクターであるKristin Brennan氏に今回のリリースについて話を聞いた。</p> 
  <p><strong>InfoQ: CoverityとVisual Studio 2013で利用できるテストツールとはどのような違いがあるのでしょうか。</strong></p> 
  <blockquote>
   CoverityはVisual Studio 2013(以前は
   <a href="http://msdn.microsoft.com/en-us/library/bb429476(v=vs.80).aspx">FxCop</a>という名で知られた)のテストツールを補完します。というのは両者は異なるものを扱うからです。.NET frameworkの黎明期に一貫した標準的な書式のためのガイドラインが作られました。クラスのメンバの名前の付け方、名前空間はどうするべきか、クラスの間の関係はどうするかというようなことです。Visual Studioのツールはこれらのルールが違反されていないかに注目します。そして、Visual Studioのツールは進化していますので、バイトコードレベルでの問題も分析して検出するようになっています。しかし、バイトコードを分析して見つかる問題は全体の問題のごく一部です。
  </blockquote>
  <blockquote> 
   <p>Coverityはより狭い範囲でより深い分析を行います。Visual Studioのツールがバイトコードを分析してコードの一貫性を保持するために設計されているなら、Coverityはソースコードを分析し、致命的でインパクトが大きいバグを検出します。null参照や、リソースの問題、スレッドの問題です。</p> 
  </blockquote> 
  <p><strong>InfoQ: Coverityの目的とは何でしょうか。</strong></p> 
  <blockquote>
   Coverityは開発する組織がより良いソフトウエアを素早く開発できるように支援するため設立されました。Coverity Development Testing Platformは素早く効率的にコードのテストし、致命的な品質上、セキィリティ上の問題に対処するための静的解析を提供します。このプラットフォームは高品質でセキュアなソフトウエアを素早く提供できるようにすることで、ソフトウエア開発に競争力を提供します。
  </blockquote> 
  <p><strong>InfoQ: Coverityは開発者にどのような利点を提供しますか。</strong></p> 
  <blockquote>
    Coverityは開発者がより良いソフトウエアを素早く開発できるようにします。コードをテストし、致命的な影響力のある品質上、セキュリティ上の問題に対処できます。
  </blockquote> 
  <p><strong>InfoQ: Coverityを使ってテストできるアプリの種類を教えてください。</strong></p> 
  <blockquote>
   C/C++、Java、C#で書かれたどのような種類のアプリでもテストできます。
  </blockquote> 
  <p><strong>InfoQ: iOS、Android、Windows Phone 8はどうでしょうか?</strong></p> 
  <blockquote>
    iOS、Android、Windowsモバイルデバイス向けにC/C++をサポートします。
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>MySQLを“ウェブスケール”にするためにFacebook, Google, LinkedIn,Twitterが協力</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/04/webscalesql"><em>原文(投稿日：2014/04/04)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Facebook、Google、LinkedIn、Twitterは共同でリレーショナルデータベースを“ウェブスケール”にするため、<a href="http://webscalesql.org/">WebScaleSQL</a>を立ち上げた。これは、MySQL 5.6 Community Editionのブランチだ。</p> 
  <p>MySQLは上述の企業ですでにウェブスケールの規模で使われているが、“同じような課題に直面して”いた。そこで共同で“各社で別々のブランチをメンテナンスするのではなく、自分たちのニーズに適う共通の変更を開発、メンテナンスし、さらにカスタマイズをする”ことにした、とFacebookのソフトウエアエンジニアであるSteaphan Greene氏はInfoQのインタビューに答えた。このプロジェクトは“オープンであり、MySQLコミュニティの全員がに貢献でき、全員に利益があります”。</p> 
  <p>MariaDBではなくなぜMySQLなのか、という問いに対して、Greene氏は“MySQL-5.6が最適だという合意が生まれました。大規模な利用に耐えうる状態であり、MySQL-5.7で予定されている機能も私たちの行く末に適している”からだ、と答えた。</p> 
  <p>これがMySQL 5.6.17のブランチであり、フォークではないことに注意する必要がある。WebScaleSQLで導入される変更は“MySQLのコミュニティリリースが続く限り”トランクに反映される、と<a href="http://webscalesql.org/faq.html">プロジェクトのFAQ</a>には書いてある。</p> 
  <p>上述の4社は過去数ヶ月、MySQLについても協業してきた。自動化されたフレームワークを立ち上げ、コードベースに提案された変更を評価するための<a href="https://www.facebook.com/l.php?u=https%3A%2F%2Fgithub.com%2Fwebscalesql%2Fwebscalesql-5.6%2Fcommit%2F8b6adf69913226cab5cf8aaf45914e66b812692d&amp;h=yAQE0Aw1N&amp;s=1">ストレステストスイート</a>を開発した。コードの変更がサブミットされたとき、プロジェクトに参加している最低でもひとつの他の企業でも役に立つ場合にコードベースに取り込まれる。特定の企業にだけ便利なパッチは取り込まれない。</p> 
  <p>今まで、LinkedInは“テストフレームワークの変更、改善の提案や他のメンバの変更のレビュー”を行ってきた、と同社のマネージャのDavi Arnaut氏は言う。</p> 
  <p><a href="https://github.com/twitter/mysql/wiki/WebScaleSQL-and-Twitter-MySQL">Twitter</a>は<a href="https://github.com/webscalesql/webscalesql-5.6/commit/d086837b5487647b130ce471c45f8c9093e87855">MySQL 5.7からのバッファプール最適化のバックポート</a>や<a href="https://github.com/webscalesql/webscalesql-5.6/commit/5c030170c88b9d30165919e903eb6b5f54246b65">NUMAインターリーブポリシー</a>、多くの改善を行った。</p> 
  <p><a href="https://github.com/webscalesql/webscalesql-5.6/commits/webscalesql-5.6.16">すべてのプロジェクトのコミット</a>は<a href="https://github.com/webscalesql">GitHubのプロジェクトページ</a>で確認できる。</p> 
  <p>近い将来、Facebookは非同期クライアントを開発するつもりだ。このクライアントには、“テーブル、ユーザ、圧縮統計のプロダクションテストバージョン”が含まれている。</p> 
  <p>長期的には、WebScaleSQLはMySQLの直面している大規模な配置での問題に対処する計画だ。</p> 
  <p>WebScaleSQLはビルドは提供しない。ソースコードだけだ。これによって4社はそれぞれ、コードをダウンロードし、それぞれの企業固有のパッチ適用や最適化を行って、望ましいビルドを作成する。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
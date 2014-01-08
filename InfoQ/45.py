<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>DevDocs、リファレンスドキュメントのワンストップショップ</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/devdocs-api-documentation"><em>原文(投稿日：2013/12/30)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://devdocs.io">DevDocs</a>はソフトウェア開発者が共通に使えるよう、複数のリファレンスドキュメントを1つにまとめたWebサイトだ。1つにまとめた利点を活かして、検索インターフェイス、キーボードショートカット、共通のレイアウトや目次など、全API横断して使える機能を提供している。</p> 
  <p>DevDocのビジョンステートメントにはこう書かれている。</p> 
  <blockquote>
    DevDocsの目的は、読めて検索できるリファレンスドキュメントを、高速に簡単に楽しくすることです。このアプリの主たる目標は次の通りです。ブートおよびロード時間をできるだけ短くすること。品質、スピード、検索結果の順位を改善すること。キャッシュやその他パフォーマンス最適化を最大限利用すること。クリーンで読みやすいユーザインターフェイスを保つこと。完全なキーボードナビゲーションをサポートすること。すべてのドキュメントを通して一貫性のあるタイポグラフィおよびデザインにすることで、「コンテキストスイッチ」をなくすこと。特定カテゴリのコンテンツ（API/リファレンス）にフォーカスすること、そして多くの開発者にとって最低限有用なものだけをインデックス付けすることで、がらくたの山にしないこと。
  </blockquote> 
  <p>DevDocsは今のところ、主にWeb開発を対象としたドキュメントを提供している。標準（<a href="http://devdocs.io/html/">HTML</a>、<a href="http://devdocs.io/http/">HTTP</a>、<a href="http://devdocs.io/css/">CSS</a>など）、言語（<a href="http://devdocs.io/ruby/">Ruby</a>、<a href="http://devdocs.io/python/">Python</a>、<a href="http://devdocs.io/javascript/">JavaScript</a>など）、ライブラリ（<a href="http://devdocs.io/jquery/">jQuery</a>、<a href="http://devdocs.io/ember/">Ember</a>など）、プロダクト（<a href="http://devdocs.io/rails/">Ruby on Rails</a>、<a href="http://devdocs.io/postgresql/">PostgreSQL</a>、<a href="http://devdocs.io/redis/">Redis</a>、<a href="http://devdocs.io/git/">Git</a>など）。</p> 
  <p>DevDocsの作者、Thibaut Courouble氏はInfoQに対して、さらなるドキュメントの追加を進めているところだと語った。「私は現在、Linux manページに取り掛かったところで、Bash、C、C++、D3.js、Knockout.jsも短期的なToDoリストに入っています。」</p> 
  <p>DevDocsのHTMLホームページを見れば、DevDocsがどのようなものかがよくわかる。</p> 
  <p><img src="http://www.infoq.com/resource/news/2013/12/devdocs-api-documentation/en/resources/DevDocs_500.png" alt="" _href="img://DevDocs_500.png" _p="true" /></p> 
  <p>DevDocsで公開されているドキュメントはすべて<a href="https://github.com/Thibaut/devdocs#scraper">スクレイピング</a>したもので、即座に更新されるわけではない。Thibaut氏はこう言っている。「既存のドキュメントは頻繁に、通常は新しいバージョンがリリースされて数日以内に更新されます。リリースを見落していれば、ユーザがTrelloボードに更新をリクエストしてくれるとありがたいです」</p> 
  <p>DevDocsは<a href="https://github.com/Thibaut/devdocs">オープンソース化</a>されており、<a href="https://github.com/Thibaut/devdocs/blob/master/CONTRIBUTING.md">コントリビュータを歓迎している</a>。だれでもコントリビュート可能だが、新しいドキュメントをリクエストするための<a href="https://trello.com/b/6BmTulfx/devdocs-documentation">投票システム</a>も用意されている。Thibaut氏はこう説明する。</p> 
  <blockquote> 
   <p>新しいドキュメントをコントリビュートしてくれるのは大歓迎です。新しいドキュメントの追加と既存のドキュメントのメンテナンスに役立つ、柔軟なスクレイパー/ツールチェインを作るのには、たくさんの作業が必要になります。必要なことは、わずかな<a href="https://github.com/Thibaut/devdocs/blob/master/CONTRIBUTING.md#contributing-new-documentations">「品質ガイドライン」</a>とドキュメントのライセンスが変更バージョンの再配布を許可していることだけです（Microsoft、Apple、Oracleは禁じています）。</p> 
   <p>どのドキュメントに取り組むかの選択については、もちろん投票が大きな要因で、あとは個人的好み（もうやりたいものはほとんど追加してしまいましたが）とオリジナルのドキュメントがどう構成されているか（つまり、追加するのにどれくらい時間がかかるか）です。</p> 
  </blockquote> 
  <p>サイトの今後の計画については常にGitHubでトラックできるとThibaut氏は言う。</p> 
  <blockquote> 
   <p>計画については<a href="https://github.com/Thibaut/devdocs/issues?direction=desc&amp;labels=feature&amp;page=1&amp;sort=updated&amp;state=open">GitHub</a>に載せています。目下、スピードと使いやすさを最優先にしており、最適化とUIの調整についてアイデアがたくさんあります。</p> 
   <p>すぐに使えるオフライン可能なバージョン（今のところ、DevDocsをオフラインで使うにはコードをダウンロードする必要があります）と、スマートフォン/PhoneGapアプリ（現在のアプリはすでにモバイルに最適化されていますが、ネイティブアプリはオフラインで読むためのドキュメントをバンドルすることになるでしょう）を作りたいです。</p> 
   <p>さらに先には、IDEと密に連携することを考えています。すでに<a href="http://www.sublimetext.com/">Sublime Text</a>や<a href="http://brackets.io/">Brackets</a>用の<a href="http://devdocs.io/about#plugins">プラグイン</a>を作っている人もいます。</p> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
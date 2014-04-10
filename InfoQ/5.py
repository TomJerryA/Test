<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>New York Times Labがストリーム処理ツールを公開</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/04/nyt-streamtools"><em>原文(投稿日：2014/04/01)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>The New York Times R&amp;D Labが<a href="http://blog.nytlabs.com/2014/03/12/streamtools-a-graphical-tool-for-working-with-streams-of-data/">streamtoolsを発表</a>した。これはデータのストリームを処理するグラフィカルなツールで一般的な用途で使える。</p> 
  <p>NY Times Labでこのプロジェクトのリードを務める<a href="https://twitter.com/mikedewar">Mike Dewar氏</a>はこのツールの開発動機を次のように説明する。</p> 
  <blockquote>
   この20年間、私たちは表形式のデータを処理するツールに多大な投資をしてきました。Excel、MySQL、MATLAB、Hadoop、R、Python+Numpyなどです。これらのツールは終わりのないデータのストリームを上手く扱えず、私たちの創造性を殺いでしまいます。それでこのstreamtoolsを開発したのです。
  </blockquote> 
  <div>
   streamtoolsはブラウザで動作するGUIを提供し、ユーザは、データのストリームを閲覧し、変更し、分析できる。streamtoolsが定義する操作のボキャブラリは単純だ。データはコネクションを通じであるブロックから他のブロックへ流れる。ブロックを結びつけることでライブデータ処理システムが出来上がる。プログラミングや複雑なインフラも必要ない。
  </div> 
  <ul> 
   <li>ブロックは受け取ったメッセージに基づき、何らかの処理を行う。メッセージがブロックのタイプを定義する。</li> 
   <li>各ブロックは0以上のルールを持つ。このルールがブロックの挙動を決める。</li> 
   <li>各ブロックは名前付きルートを持つ。ルートはデータを受け取り、データを出力する。または、問い合わせに対して応答する。</li> 
   <li>ブロックはルートを経由してコネクションによって繋がる。</li> 
   <li>繋がったブロックの集まりをパターンと呼ぶ。パターンは実行中のstreamtoolsのインスタンスからエクスポート、インポートできる。フォーマットはJSON形式のドキュメント。</li> 
  </ul> 
  <div>
   streamtoolsは
   <a href="http://golang.org/">Go</a>で書かれている。Goは
   <a href="http://readwrite.com/2014/03/21/google-go-golang-programming-language-cloud-development">次第に人気を集めている</a>Googleのプログラミング言語だ。streamtoolsは
   <a href="https://github.com/nytlabs/streamtools/">GitHub</a>にホストされている。ライセンスはApache 2。Dewar氏は
   <a href="https://source.opennews.org/en-US/articles/introducing-streamtools/#comment-1282941834">Goに決めたことについて</a>次のように説明する。
  </div> 
  <blockquote>
   Goに決めたのは私たちがユーザに提示しようとした語彙をほぼそのまま使ってプログラミングができたからです。各ブロックはgoroutineになり、すべてのコネクションはチャンネルのペアになります。これはとても直接的な抽象化で、ユーザがシステムそのものを理解しやすくなると思います。また、新しいブロックを書くのも簡単です。コミュニティが便利だと思うブロックを簡単に作ってくれることを望んでいます。また、Goは安全で効率的にプログラミングできます。日々の仕事に使いやすいのです。
  </blockquote> 
  <div>
   NY Times LabのstreamtoolsチームはストリームベースのAPIがもっと流行し、ストリームを利用することで世界に対する理解の仕方が変わると考えている。
  </div> 
 </div> 
</div><br><br><br><br><br><br></body></html>
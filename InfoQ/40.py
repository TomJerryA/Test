<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Edge.jsは、Node.jsと.NETを結びつける</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/edgejs;jsessionid=F67E788EBE13D3F7FC25DD3D958173B2"><em>原文(投稿日：2013/03/22)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p style="margin-bottom: 0in" class="western">JavaScriptプロジェクト <a class="western" target="_blank" href="http://nodejs.org/">Node.js</a> は<a class="western" target="_blank" href="https://github.com/tjanczuk/edge">Edge.js</a>(以前は<a class="western" target="_blank" href="https://github.com/tjanczuk/owin">owin</a>と呼ばれていた)プロジェクトのおかげで.NETコードとひとつのプロセスで実行する機能を持つことになった。.NETとMonoを結びつける<a class="western" target="_blank" href="http://www.infoq.com/news/2012/05/frijters_IKVM;jsessionid=4BCB65B355443545F57293128CEFE48E;jsessionid=F67E788EBE13D3F7FC25DD3D958173B2">IKVMプロジェクト</a>と同様に、Edge.jsは.NETとNode.jsを組み合わせることで&quot;両方の世界で最高&quot;のアプローチを提案する。これにより、開発者はそれぞれのツールの長所を生かしてプロジェクトの効果を最大化することができる。</p> 
 <p style="margin-bottom: 0in" class="western">Tomasz Janczuk氏によって開発されたEdge.jsは、開発者がC/C++のような非CLR言語に頼ることなく、Node.jsを簡単に最大限に活用することができるように意図されている。Edge.jsのアプローチは、Node.jsのイベントループをブロックすることなく.NETのCPU境界の計算実行を含むいくつかのベネフィットを提供する。C/C++を使うことなくC#を使ってNode.jsを拡張することで、Windowsプラットフォーム固有の機能にアクセスすることができる。</p> 
 <p style="margin-bottom: 0in" class="western">node.jsとEdge.jsの間の接続はシームレスで双方向である: node.jsは、.NETメソッドを呼び出せ、.NETコードはNode.jsを呼び出すことができる。Edge.jsは、C#ソースを実行時にコンパイルするか、Edge.jsの開始前に事前コンパイルすることができる。</p> 
 <p style="margin-bottom: 0in" class="western">InfoQは、Janczuk氏とプロジェクトについて議論する機会に恵まれ、彼のEdge.jsに対する将来プランについて話すことができた:</p> 
 <p style="margin-bottom: 0in" class="western"><b><b>InfoQ: プロジェクトの同期は単純にC#とNode.jsを繋ぎたいという欲求だけですか？</b></b></p> 
 <blockquote> 
  <p style="margin-bottom: 0in" class="western"><b>Janczuk: </b>&quot;Edge.jsは、開発者にアプリケーション全体よりもより小さいスコープでの技術の選択肢を提供することを目指しているベストスイートです。Edge.jsは、すべてがnode.jsか.NETのどちらかで行われる前提に基づいているが、特定のものがどちらかよいもので行われます。これまでnode.jsと.NETの間は、開発者がアプリケーション全体のスコープで選択しました。Edge.jsでは、開発者は.NETとnode.jsを特定の技術が理にかなっているかどうかの観点で選択することができます。&quot;</p> 
 </blockquote> 
 <p>&nbsp;</p> 
 <p style="margin-bottom: 0in" class="western"><b>InfoQ: .NETの例はすべてC#であるように見えますが、Edge.jsはC#が必要なのですか？もしそうであれば、他の.NETプラットフォーム言語を広くサポートしますか？</b></p> 
 <blockquote> 
  <p style="margin-bottom: 0in" class="western"><b>Janczuk:</b> &quot;Edge.jsは、プリコンパイルされたCLRアセンブリか、node.jsアプリケーションに含まれる.NETソースコードのいずれかによって.NETコートとnode.jsアプリケーションを統合することができます。Edge.jsはFunc&lt;object,Task&lt;object&gt;&gt;デリゲートでプリコンパイルされたアセンブリを生成することで任意のCLR言語をサポートします。リテラル.NETコードがnode.jsアプリケーションに含まれている場合、edge.jsは現時点ではC#のみをサポートします。&quot;</p> 
  <br /> 
 </blockquote> 
 <p style="margin-bottom: 0in" class="western"><b>InfoQ: 今後6～12ヶ月のプロジェクトのゴールはなんですか？</b></p> 
 <blockquote> 
  <p style="margin-bottom: 0in" class="western"><b>Janczuk: </b>“Edge.jsは、.NETとnode.jsを間をインプロセスで相互運用可能な比較的少数のコンセプトを持つ小さなコンポーネントを維持する予定です。シナリオ固有の機能、例えばMS SQLにアクセスする、Windowsイベントログに書き込む、X.509証明書ストアにアクセスするなどは、edge.jsのスコープを広げるよりも、edge.jsに依存した新しいモジュールとして展開されることが期待されています。edge.jsに関するいくつかの特筆すべきプランは、Monoのサポートが含まれること、C#以外のCLR言語にコンパイルできること、.NETプロセスでnode.jsがホストできることがあげられます。”</p> 
  <br /> 
 </blockquote> 
 <p style="margin-bottom: 0in" class="western"><b>InfoQ: Microsoftでの専門職として考えると、このプロジェクトは独立したままでしょうか、それともMicrosoftツールの一部として公式になるのでしょうか？</b></p> 
 <blockquote> 
  <p style="margin-bottom: 0in" class="western"><b>Janczuk: </b>&quot;Microsoftは、オープンソース技術を採用した実績がありますが、現時点でedge.jsがMicrosoft製品の一部として採用される予定はありません。&quot;</p> 
 </blockquote> 
 <p>Edge.jsはApacheライセンスバージョン2でリリースされたオープンソースプロジェクトである。Janczuk氏は、プロジェクトのWebサイト上に、コードサンプルやより詳細な情報を含む<a class="western" target="_blank" href="http://tjanczuk.github.com/edge/#/">概要</a>を提供している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>AmazonがAppStream APIにHALメディアタイプを選択</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/amazon-hal-appstream"><em>原文(投稿日：2014/03/03)へのリンク</em></a></p>
<p>Amazonは，Amazon AppStreamプラットフォームにホストされたアプリケーションをプログラムから管理可能な新API，&quot;<a href="http://docs.aws.amazon.com/appstream/latest/developerguide/rest-api.html#rest-api-hal">ApStream API</a>&quot;をリリースした。このAPIの開発で同社が選択したのは<a href="http://tools.ietf.org/html/draft-kelly-json-hal-06">HALメディアタイプ</a>だ。HALは，マシン・ツー・マシンAPIを構築するメディアタイプのための，最小限のハイパーメディアである。Amazonは，一般公開されている製品の技術としてハイパーメディアを選択した最大の組織のひとつ，ということになる。</p>
<p>ハイパーメディアAPIはAPIの世界ではホットな話題だが，その支持者に対しては，現実での適用性に関する疑問が投げられることも多い。技術的な研究や議論が激増する一方で，ハイパーメディアAPIは現在のAPIエコシステムのごく一部を構成するに過ぎないのだ。SOA形式の製品開発をAmazonの開発チームに求めたのが，同社CEOのJeff Bezos氏であるというのはよく知られた話だ。その結果，数多くの内部APIと外部APIが作り出されることになった。最大ハイテク企業のひとつがHALを使ったハイパーメディアに賛成票を投じたことは，ハイパーメディア支持派を勇気づけるに違いない。</p>
<p>ハイパーメディアコミュニティが現在取り組む課題のひとつがドキュメント化だ。ハイパーメディアサービスのドキュメントとはメディアタイプの定義であって，それ以上のものはない，というのが従来の答だ。しかしこのアプローチは，既存のアーキテクチャスタイルとは大きく異なっている。このギャップを埋めるために，コミュニティは新たな戦略に取り組んでいる。</p>
<p>AppStream APIチームはAPIを，ヘッダ値，エラーコード，トップレベルリソース，リンク関係という，４つの大きなセクションの文書化を決定した。HTTPステータスコードとURLとパラメータの組み合わせに注目する，これまでのRESTfulサービスとは大きく異なる，従来のハイパーメディアのアプローチに極めて近い方法だ。HALユーザが仕様と用途について議論する場である<a href="https://groups.google.com/forum/#!msg/hal-discuss/3IyTn17m7Ps/AeBpQXadn8gJ">HAL-discussメーリングリスト</a>で，Andr&eacute;s Freyr&iacute;a Cede&ntilde;o氏は次のように発言している。</p>
<blockquote> 
 <p>ドキュメントに対する私の直感的な感想は，&quot;ハイパーメディアAPIが一般的なものならば，これで十分な資料だろう&quot;という線に沿ったものでした。しかし現在の状況を考えれば，開発者の作業の補助として十分なリソースであるとは言えません。</p> 
</blockquote>
<p>この傾向がどのように続いて，ハイパーメディアがAPIパターンとして確立されていくかは，今後明らかになるだろう。</p>
<p>HALは現在，メディアタイプとしてIETFで標準化作業が続けられている。Mike Kelly氏によって生み出されたHALは，XMLとJSONに対して一連の規則を提供することによって，リソースの相互リンクをシンプルかつ分かりやすく表現することを目標にしている。</p>
<p>次のHALレスポンスのサンプルはドラフトから抜粋したものだ。</p>
<pre>
{
     &quot;_links&quot;: {
       &quot;self&quot;: { &quot;href&quot;: &quot;/orders/523&quot; },
       &quot;warehouse&quot;: { &quot;href&quot;: &quot;/warehouse/56&quot; },
       &quot;invoice&quot;: { &quot;href&quot;: &quot;/invoices/873&quot; }
     },
     &quot;currency&quot;: &quot;USD&quot;,
     &quot;status&quot;: &quot;shipped&quot;,
     &quot;total&quot;: 10.20
   }
</pre>
<p>HALでは<small>
  <bold>
   _links
  </bold></small> と<small>
  <bold>
   _embedded
  </bold></small>というトップレベルの予約プロパティが２つ定義されているが，ここでは<small>
  <bold>
   _links
  </bold></small>を使用している。このオブジェクト中のリンク方法が，HALで標準化されたものだ。この例では架空の&quot;orders&quot;リソースへのリンクがあり，orderの格納されているwarehouseと，現在このorderに関連付けられている invoiceの両方にリンクしている。</p><br><br><br><br><br><br></body></html>
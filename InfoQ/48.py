<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>restyle.jsを使ったCSS処理</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/restylejs"><em>原文(投稿日：2014/02/17)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Andrea Giammarchi氏が開発している<a href="https://github.com/WebReflection/restyle">restyle.js</a>はJavaScriptベースのCSSプリプロセッサであり、サーバ(Node.js)でもブラウザでも動作する。 &quot;シンプルなCSSアプローチ&quot;と自称するこのツールはCSSのルールとプロパティのプレフィックス付きのバリエーションを生成し、DOMに挿入できる。</p> 
  <p>既存のCSSには機能的な不足はないものの、Andrea氏はサーバとクライアントの両方で動作する<a href="http://webreflection.blogspot.co.uk/2014/02/restylejs-simplified-css-approach.html">軽量なもの</a>がない、という。</p> 
  <blockquote> 
   <p>&quot;yet another CSS preprocessor&quot;を探しているなら、次のことを教えます。私が何人かの著名なCSS開発者やウェブ開発者に話を聞いたところ、そのようなスクリプトは存在しなかったです。&quot;なんで誰も作っていないんだろう&quot;、と思うでしょう。私の考えでは、誰かがすでに作っているものの、圧縮して0.8KBでサーバとIE6まで含んだクライアントと互換性のあるものがないんです。つまりrestyleのことです。</p> 
  </blockquote> 
  <p>このライブラリは、restyle()というメソッドを公開し、ふたつの引数をとる。ひとつはJavaScriptのオブジェクトでCSSやDOMスタイルの編集に似た文法を持つ。</p> 
  <pre>
 restyle({
    'body &gt; div.my-div': {
        backgroundColor: 'goldenrod',
        backgroundImage: 'url(mybg.png)'
    }
}); </pre> 
  <p>これによって、次のCSSが出来上がる。</p> 
  <pre>
 body &gt; div.my-div {
    background-color: goldenrod;
    background-url: url(mybg.png);
} </pre> 
  <p>異なる方法でJavaScriptオブジェクトを定義し、出力結果を得ることもできる。</p> 
  <pre>
 restyle({
    'body &gt; div.my-div': {
        background: {
            color: 'goldenrod',
            image: 'url(mybg.png)'
        }
    }
}); </pre> 
  <p>もちろん、特別なことはしていない。マークアップの記述の減量もわずかだ。しかし、restyle.jsは標準的なCSSでは冗漫になってしまうときにはrestyle.jsは効果的だ。例えば、ベンダプレフィックスを使うとき、ふたつ目の引数を使ってベンダプレフィックスを定義すればいい。例えば、</p> 
  <pre>
 restyle({
    '.my-div': {
        transition: 'background-color 500ms ease';
        backgroundColor: '#00f';
    }
}, ['moz', 'webkit']); </pre> 
  <p>出力結果は以下の通り。</p> 
  <pre>
 .my-div {
    -webkit-transition: background-color 500ms ease;
    -moz-transition: background-color 500ms ease;
    transition: background-color 500ms ease;
    background-color: #00f;
} </pre> 
  <p>これは、アニメーションのロールを記述とき、とても使いやすい。2、3のコードがベンダプレフィックスがついたCSSの属性に変換される。サーバでは、第2引数を省略すればプレフィックスなしになる。ブラウザで動作しているrestyle.jsでは、ブラウザの種類に関わらず、すべてのベンダプレフィックスを生成する。</p> 
  <p>restyle()関数は環境によって異なる結果を返す。Node.jsでは、結果のCSSを含む文字列を返す。ブラウザでは、CSSは自動的にDOMに挿入され即座に反映される。返却値は属性ノード(スタイルエレメント)、css(CSSを含む文字列)、remove()メソッドを含むオブジェクトを返す。removeメソッドは挿入したスタイルをDOMから削除する。</p> 
  <p>サンプルページは<a href="http://webreflection.github.io/restyle/">ここで確認できる</a>。実際にrestyle.jsを使って動作を確認できる。Andrea氏の記事への<a href="http://webreflection.blogspot.co.uk/2014/02/restylejs-simplified-css-approach.html#comments">コメント</a>が指摘するように、restyle.jsは<a href="https://github.com/krasimir/absurd">AbsurdJS</a>と同じアイディアでできている。大きさは10分の1だが、Arestyleは軽量で触ってみる価値はある。<a href="https://github.com/WebReflection/restyle/blob/master/README.md">readme</a>を読んでみるのもいいだろう。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
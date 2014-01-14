<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>モバイルアプリケーション向けA/Bテストを提供するSplitforce</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/splitforce-mobile-ab-testing"><em>原文(投稿日：2013/12/20)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>企業のIT戦略でモバイルアプリケーションがますます重要になるにつれて、アプリケーションをテストし分析することがより重要になってきた。ユニットテストを使ったテストなどコードの機能的なテストはすべてのソフトウエアプロジェクトで実施されているだろうが、ユーザの振る舞いを分析しコンバージョン率を最大化するのはモバイル分野ではまだ未開拓だ。</p> 
  <p><a href="http://www.splitforce.com">Splitforce</a>はモバイルアプリ向けにA/Bテストを提供する。アプリケーションの開発者はSplitforceを使うことで、アプリの機能やユーザエクスペリエンスを最適化できる。アプリストアに再提出することなく、ネイティブアプリのさまざまなバリエーションをテストでき、ユーザの行動を追跡し、分析できる。開発者はデータに基づいてデザインを決めることができる。Splitforceは現在、ネイティブのiOSアプリケーションと<a href="http://unity3d.com/">Unity</a>を使ったゲームをサポートしている。Splitforceによれば、Androidは2014年の第1四半期にサポートされる予定だ。</p> 
  <p>SplitforceのSDKとプラットフォームを使うことで、開発者は開発したモバイルアプリのユーザの端末での使われ方を変える実験をすることができる。アプリケーションにハードコーディングされているコンポーネントをSplitforceのサーバがウェブ経由でコントロールできる動的コンポーネントに置き換えることで、アプリケーションの新しいバリエーションを生み出したり、既存のアプリを変えたりできる。これらのバリエーションは次のカテゴリによって分析される。</p> 
  <ul> 
   <li><strong>レート:</strong> 購入やサインアップのような特定のゴールにどの程度の割合で到達しているのかを分析する。</li> 
   <li><strong>タイミング:</strong> アプリの特定の領域でユーザがどの程度時間を費やすか、またはユーザが製品を購入するまでにどの程度時間がかかるかを計測する。</li> 
   <li><strong>量:</strong> ゲームのあるレベルをクリアするなど、ユーザが特定のタスクを完了した回数を計測する。</li> 
  </ul> 
  <p>&nbsp;</p> 
  <p>文字列や数値、色、ブール値、カスタムのサブジェクトなどをベースに実験ができる。サインアップして実験を定義すると、Splitforceはコードスニペットを生成し、開発者はそれをアプリのソースコードに貼付ける。iOSアプリで異なる色のボタンをテストし、購入イベント発生数をカウントするのは次のコードだ。</p> 
  <blockquote> 
   <code> <pre>
[[SFManager currentManager] experimentNamed:@&quot;Experiment #1&quot; applyVariationBlock:^(SFVariation *variation) {
  // Configuration for 'Test Button Colors'
  UIColor *testSubject = [SFUtils colorFromHexString:variation.variationData[@&quot;Test Button Colors&quot;]];
  // set special button color  
} applyDefaultBlock:^(NSError *error) {
  if (error) NSLog(@&quot;Splitforce Error: %@&quot;, error);
  // set default button color
}];  
</pre> </code> 
  </blockquote> 
  <p>次のコードでは、ある目的が達成されたときSplitforceサーバに通知している。</p> 
  <blockquote> 
   <code> <pre>
SFVariation *variation = [SFManager.currentManager variationForExperimentNamed:@&quot;Experiment #1&quot;];

[variation goalResultNamed:@&quot;Item Purchased&quot;];
[variation variationEnded]; 
</pre> </code> 
  </blockquote> 
  <p>生成されたコードスニペットを挿入するだけで、あとはライブラリをインクルードしアプリケーションを起動するときにSplitforceを初期化すればいいだけだ。</p> 
  <p>&nbsp;</p> 
  <p>Splitforceの<a href="https://www.splitforce.com/pricing">サービスプラン</a>はテストできる日時のユーザ数に依存する。500人までは無料。5.000人まではエントリプランの月額299ドル。プロプランであれば、75.000人までテストでき月額2.499ドル。75.000人以上をテストしたい場合はエンタープライズプランが利用できる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
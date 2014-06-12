<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Xamarin.Formsで完全にネイティブなクロスプラットフォームUIを実現</h3><p><em><a target="_blank" href="http://www.infoq.com/news/2014/05/xamarin-forms">原文(投稿日：2014/05/29)へのリンク</a></em></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://xamarin.com">Xamarin</a>を使ってクロスプラットフォームのネイティブモバイルアプリケーションを書く場合、これまでは平均してコードの80％程度を共有できていた。しかし、UIコードに関わる残りの20％についてはプラットフォームごとに別々に書かなければならなかった。最新リリースである <a href="http://blog.xamarin.com/announcing-xamarin-3/">Xamarin 3.0</a> では <a href="http://developer.xamarin.com/guides/cross-platform/xamarin-forms/introduction-to-xamarin-forms/">Xamarin_Forms</a> というMVVMライブラリが導入された。これにより、単一のUIコードをC#で記述すれば、iOS上でもAndroid上でもWindows Phone上でもネイティブに実行させることができる。</p> 
  <p>Xamarin.Formsを使う場合、開発者は<em>ページ</em>（ContentPage、MasterDetailPage、NavigationPage、TabbedPage、CarouselPage）を作成する。コントロールは40以上のウィジェットやレイアウト（RelativeLayout、GridLayout、Button、TableView、ProgressBarなど）の一覧から選択できる。実行する際には、コントロールを格納したページは、動作するオペレーティングシステムにおいて対応する画面とコントロールを使用してレンダリングされる。例えば、主要な3つのモバイルプラットフォーム上でXamarin.Forms.DatePickerクラスをレンダリングすると下の写真のようになる。アプリケーションの見た目を完全にネイティブにできる。</p> 
  <p><a href="http://www.infoq.com/resource/news/2014/05/xamarin-forms/en/resources/xamarin-forms.png" target="_self"><img title="image" style="border-top: 0px; border-right: 0px; background-image: none; border-bottom: 0px; padding-top: 0px; padding-left: 0px; border-left: 0px; display: inline; padding-right: 0px" border="0" alt="image" src="http://www.infoq.com/resource/news/2014/05/xamarin-forms/en/resources/xamarin-forms.png" _href="img://xamarin-forms.png" _p="true" /></a></p> 
  <p>このライブラリが特定のネイティブ機能に対応していない場合は、開発者はXamarin.FormsのページにXamarin.iOSやXamarin.Androidで書かれたネイティブの画面を埋め込んだり混在させたりすることができる。また、カスタムのページやコントロールやレイアウトを定義することもできるし、Xamarin.Formsのコンポーネントのサブクラスを作り、動作をオーバーライドすることでカスタマイズすることもできる。</p> 
  <p>Xamarin.Formsで作成されたユーザインタフェースはXAMLとして保存されるため、ツールを使って編集することもできるし、手動で編集することもできる。本ライブラリはいくつものアニメーションやマップをサポートしている。たくさんの<a href="https://github.com/xamarin/xamarin-forms-samples">サンプル</a> がGitHubで公開されている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
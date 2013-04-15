<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Struts 1が寿命を迎える</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/struts1-eol;jsessionid=44287CF1B66584917DF96CBFBB6D45BD"><em>原文(投稿日：2013・04・07)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Apache財団の<a target="_blank" href="http://struts.apache.org/struts1eol-press.html">発表</a>によれば、JavaのMVCウェブフレームワークであるStruts 1が寿命を迎えた。ある意味では、この動きは単純に、Strutsチームがバージョン2の開発に注力しているという既成事実を公式に認めただけだ。Struts 1の最後のリリースは2008年のバージョン1.3.10だ。コードとドキュメントは今後も入手できるが、今後はセキュリティパッチやバグ修正は提供されない。<a target="_blank" href="http://struts.apache.org/struts1eol-announcement.html">FAQ</a>によれば、&quot;...既存のStruts 1にパッチを当てるか、他のウェブフレームワークに移行するかして、対処する必要があります&quot;。別の言い方をすれば、Struts 1で作られたアプリケーションやウェブサイトを新しいフレームワークに移行する差し迫った必要があり、新しいプロジェクトでStruts 1を使うのは推奨されない、ということだ。</p> 
 <p>Struts 1はCraig McClanahan氏が開発し、2000年にApache財団に寄贈された。一時はJavaのウェブアプリケーション開発のデファクトスタンダードになり、未だに運用環境で利用されている。</p> 
 <p>オープンソースフレームワークに特化したウェブアーキテクチャコンサルタントであるMatt Raible氏は“J2EEにとってStruts 1.xは'キラーアプリ'だったと思います”、と言う。</p> 
 <blockquote> 
  <p>2001年には、大抵の人々はServletとJSPに苦慮し、どのようにウェブアプリケーションを設計するかについて悩んでいました。チームが利用えきるフレームワークがなかったら、自分たちで開発していたでしょう。Javaはパターンが好きなので、Strutsは多くのパターンを使っていましたし、Strutsの呼び物でもありました。また、大部分がJavaで出来ており、Javaのスキルをウェブアプリケーションを開発するのに使えるのも多くの開発者を惹き付けた理由でした。多くの点で、GWTが現れたときにJavaの開発者が感じたことと似ていると思います。突然、JavaのスキルでWeb 2.0アプリケーションが作れるようになったのです。</p> 
  <p>&quot;Strutsを知っている開発者なら最高だよ&quot;と話していた採用担当者を覚えています。その当時は、ウェブ開発に関係のあるJavaのスキルはそれほど多くありませんでした。Strutsが唯一の技術だったのです。</p> 
  <p>2002年から2003年の間、私はフルスタックのフレームワークとしてAppFuseをStrutsを使って開発していました。そのときStrutsのファンになったのです。AppFuseはStrutsが必要とする多くの定型的なコードを排除し、さらにSpringとHibernateと統合しました。しかし、他の開発者からはWebWorkとSpring MVCのほうが優れていると言われ、この2つを使ってみると確かに良いフレームワークであると感じました。ActionFormsの代わりにPOJOが使えるのは素晴らしいと思いましたし、Strutsよりもはるかにテストしやすかったのです。</p> 
  <p>そしてその後、JVMのウェブ開発の世界は大きく進化しました。Ruby on Railsに着想を得た、GrailsやPlayのようなフレームワークが現れました。しかし、しっかりと構築されたスケーラブルなバックエンドがありフルスタックのフレームワークを欲しない組織はたくさんあります。純粋なウェブフレームワーク(JSF、Spring MVC、Struts 2、Tapestry 5、Wicket)の人気が衰えないのはこのためです。現在でも純粋なJavaフレームワークはより生産的になるように改良されています。JavaScriptのMVCフレームワークが盛んに使われるようになったものの、クライアントサイドのテンプレーティングの性能問題を発見した事業者(TwitterやAirbnbのような)が純粋なJavaフレームワークに新しい命を吹き込んでいるように思います。</p> 
 </blockquote> 
 <p>Struts 1はStruts 2に取って代わられた。Struts 2のリリースは2007年2月だったが、基になっていたのはWebWorkフレームワークだ。この2つのフレームワークの併合がどのように実現したかについてInfoQ <a target="_blank" href="http://www.infoq.com/minibooks/starting-struts2;jsessionid=1AAAC676EF6F9DC2AB08493D8206F1A2;jsessionid=44287CF1B66584917DF96CBFBB6D45BD">Struts2 eBook</a>の著者であるIan Roughley氏は次のように説明している。</p> 
 <blockquote> 
  <p>当初の計画では、既存のコードベースが役に立たない方向へStrutsを進化させる必要があったことからStruts Tiという製品を開発する予定でした。当時は、Patrick Lightbody氏が共通のフレームワークを作るために複数の異なるウェブフレームワークのリーダーに働きかけていました。この動きは勢いを失ってしまいましたが、WebWorkとStruts Tiの技術的な目標やコミッタの目標の共通点が見つかりました。それでプロジェクトを合併し、WebWorkをベース技術にしたのです。</p> 
 </blockquote> 
 <p>この結果、Struts 1に完全に互換性のあるフレームワークは存在しない。また、Struts 1を使っている大規模なアプリケーションのマイグレーションは複雑な作業になる。FAQには代替のフレームワークとしてStruts 2と同様に、Spring Web MVC、Grails、Stripesを推奨している。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Modern C++とVisual Studio</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/04/modern_cpp"><em>原文(投稿日：2014/04/05)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p class="MsoNormal">Herb Sutter氏は、MicrosoftのBuild conferenceにおいて<a href="http://channel9.msdn.com/Events/Build/2014/2-661">Modern C++</a>の現在のステータスについて講演した。C++の推進はMicrosoftにおける過去数年のルネッサンスのようなものであり、Sutter氏はこの増加に焦点を向けている。
   <o:p></o:p>
   <o:p>
    &nbsp;
   </o:p></p> 
  <p class="MsoNormal">&nbsp;</p> 
  <p class="MsoNormal"><b>今後のC++リリース
    <o:p></o:p></b></p> 
  <p class="MsoNormal">Sutter氏ははじめに、現時点でのISO C++標準の簡単な要約について説明した。今年2月にC++14の技術議論が完了し、標準化委員会は今年の後半に公式なISO標準になるように、この規格の承認に向けて投票を進めている。
   <o:p></o:p></p> 
  <p class="MsoNormal">(現在、設計中で議論中の)C++17標準がメジャーリリースであると見なされているのに対し、C++14リリースはマイナーリリースと見なされている。Microsoftの最新コンパイラープレビュー(CTP)は、昨年11月にリリースされた。Sutter氏による信頼度の高い情報によると、(まだ日付が発表されていない)次のCTPでは、次の機能が含まれていると予想されている:
   <o:p></o:p></p> 
  <blockquote> 
   <ul> 
    <li>ユーザー定義リテラル
     <o:p></o:p></li> 
    <li>C++14汎用ラムダキャプチャー
     <o:p></o:p></li> 
    <li>C++14 libs: std:: ユーザー定義リテラル
     <o:p></o:p></li> 
    <li>インライン名前空間
     <o:p></o:p>
     <o:p>
      &nbsp;
     </o:p></li> 
   </ul> 
  </blockquote> 
  <p class="MsoNormal">以下の機能は、このCTPにおいては中程度の確度(後のリリースで遅らせる可能性がある)である:
   <o:p></o:p></p> 
  <blockquote> 
   <ul> 
    <li>リテラル中のユニバーサルキャラクター名
     <o:p></o:p></li> 
    <li>noexcept (条件)
     <o:p></o:p></li> 
    <li>char16_t, char32_t, 属性
     <o:p></o:p></li> 
    <li>thread_local
     <o:p></o:p></li> 
    <li>無制限ユニオン
     <o:p></o:p></li> 
    <li>consexpr (コンストラクタ, リテラル型を除く)
     <o:p></o:p></li> 
    <li>constexpr (コンストラクタ, リテラル型を含む)
     <o:p></o:p></li> 
   </ul> 
  </blockquote> 
  <p class="MsoNormal">パラレルSTL(PPL, TBB, Amp, CUDA, Thrustの融合)は、来週<a href="https://parallelstl.codeplex.com/">CodePlex</a>にリリースされる予定である。Sutter氏は、過去2年は(<a href="http://channel9.msdn.com/Events/GoingNative/2013">GoingNative</a>)に置き換えられている、2014年9月7日-12日に予定されている<a href="http://www.cppcon.org/">CPPCon</a>というC++カンファレンスにスポンサードすることを発表した。</p> 
  <p class="MsoNormal">&nbsp;</p> 
  <p class="MsoNormal">
   <o:p></o:p></p> 
  <p class="MsoNormal"><b>Modern C++ユースケース
    <o:p></o:p></b></p> 
  <p class="MsoNormal">次のパートでは、今日のアプリケーション開発におけるmodern C++のユースケースについての議論に移った。Sutter氏の意見では、C++は以下のゴールや目標が必要な時に利用が必要である:
   <o:p></o:p></p> 
  <blockquote> 
   <ul> 
    <li>クロスプラットフォームの移植性と互換性
     <o:p></o:p></li> 
    <li>ハイパフォーマンスと完全なコントロール
     <o:p></o:p></li> 
    <li>ハードウェアやOSのリソースへの完全なアクセス
     <o:p></o:p></li> 
    <li>C++言語ハイライト: デフォルトで値型、デフォルトでの決定論、デフォルトでの連続性
     <o:p>
      &nbsp;
     </o:p></li> 
   </ul> 
  </blockquote> 
  <p class="MsoNormal">Sutter氏は、Modern C++はC++98--ではなく、Modern C++は、高速で柔軟なまま、よりクリーンで、より安全であると見ている。多くのケースで、コンパイラーから改善の警告や提案はあるものの、古いC++がサポートされないと言っているわけではない。
   <o:p></o:p></p> 
  <p class="MsoNormal">Modern C++が提供する機能のひとつに(開発者の視点で)単純化されたcode&gt;new-&gt; make_uniqueや<code>new-&gt;make_shared</code>を使った時のメモリ管理がある。deleteが不要で、自動的に例外処理セーフなライフタイム管理が可能だ。
   <o:p></o:p></p> 
  <p class="MsoNormal">別のエリアでは、値型の移動操作をより効率的に処理する方法だ。C++11では、オブジェクトのように型を移動するアイディアが追加されたこのアプローチをふまえ、削除しなくてはならないコピーを作るのではなく、所有権を持つようにした。改善されたmoveセマンティクスは、C++14機能を持つコンパイラーで再コンパイルすることで、レガシーコードを簡単にスピードアップさせることができる。
   <o:p></o:p></p> 
  <p class="MsoNormal">
   <o:p>
    &nbsp;
   </o:p></p> 
  <p class="MsoNormal"><b>より高速なコードを書く
    <o:p></o:p></b></p> 
  <p class="MsoNormal">連続した配列は、多くのオブジェクトを操作して、本当に隣接したアドレス順にアクセスしたいときに、重要だが忘れがちである。もし本気でパフォーマンスが重要なら、リストや配列リストだけでなく配列を使用する。
   <o:p></o:p></p> 
  <p class="MsoNormal">そのテーマに沿ってすすむと、Sutter氏はvectorで大量リストの挿入と削除によるベンチマークを提示した。事前に確保したリストは通常のリストよりも高速だが、Vectorよりもはるかに悪いままである。
   <o:p></o:p></p> 
  <p class="MsoNormal">Sutter氏の話しは非常に有益で有り、彼は魅力的なスピーカーのままである。完全な話しを見たい場合は、<a href="http://channel9.msdn.com/Events/Build/2014/2-661">Channel9</a>サイトを参照して欲しい。
   <o:p></o:p></p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
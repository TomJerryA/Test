<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Typemock Isolator++がアップデート，64bitをサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/typemock-isolator-plus-plus"><em>原文(投稿日：2014/02/19)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Typemockが<a href="http://www.typemock.com/isolatorpp-product-page">Isolator++</a>をリリースした。Windowsプラットフォーム用に記述された64bit C/C++コードのサポートに加えて，もともとテストを考慮していなかったようなレガシコードにも対応する。マクロを利用してテスト対象のメソッドの動作を変更することも可能だ。</p> 
  <p>C/C++用モックフレームワークのIsolator++は，メソッド呼び出しやパラメータのアサート，関数のモック生成，参照によって返される値のシミュレートなどの機能も提供する。<a href="http://smartbear.com/products/qa-tools/application-performance-profiling/">AQTime</a>, <a href="http://www.softwareverify.com/">Software Verify</a>, <a href="http://www.bullseye.com/">BullsEye</a>などのツールと統合可能であると同時に，<a href="http://sourceforge.net/apps/mediawiki/cppunit/index.php?title=Main_Page">CppUnit</a>, <a href="http://unittest-cpp.sourceforge.net/">UnitTest++</a>, Google Test Boostといったテスト実行フレームワークとの互換性も備えている。</p> 
  <p>最新リリースのメリットについて詳しく知るため，InfoQは，TypemockのプロダクトマネージャであるGil Zilberfeld氏に話を聞いた。<br /> <br /> <strong>64bitのサポートは，開発者にとってどのようなメリットがありますか？ 本当に意義はあるのでしょうか？</strong></p> 
  <blockquote>
   開発者の中には，64bit環境に限定して開発を行っている人もいます。64bitをサポートしなければ，彼らは32bit環境でテストを行わなければなりません。しかし32bit環境でのテストではシステムの&quot;真&quot;の動作とは違いますから，テスト結果が実際の条件を反映しているかどうか，信頼性に欠ける部分があります。Isolatorが64bitをサポートすることで，製品環境と同じ条件でテストを実行できるようになるのです。信頼性が向上すれば，テストが現実を表現しているのか，それとも限定的なものか，という余計な推測の入る余地はなくなりますから，すべてが64bitで正しく動作するという確信を持ちながら，コードのリファクタやテストを行うことができます。
  </blockquote> 
  <p><strong>Typemock Isolator++の機能について教えてください。</strong></p> 
  <blockquote>
   Typemock Isolator++は，Windows上のCおよびC++のための完全なモックフレームワークです。Visual Studio 2005以降を対象に，32bitと64bitをサポートします。インスタンスあるいはスタティック，グローバル，プライベートとパブリック，仮想と非仮想など，すべての関数コールをモックできます。特定のオブジェクトや型，いくつかのメソッドのみをダミーにして，その他は本物の実装を使用することも可能です。関数がコールされた回数をカウントして，それをアサートすることもできます。参照で返されるパラメータをシミュレートする機能もあります。テスト用にコードの修正したり，テストのために準備作業をしたりする必要はありません。
  </blockquote> 
  <p><strong>開発者の生産性は向上するのでしょうか？</strong></p> 
  <blockquote>
   Isolator++は&quot;テスト不能コード&quot;用にテストを記述できますから，アプリケーション全体をデバッグするよりも手早く，ユニットテストを使ってデバッグすることが可能です。テストの不可能なシナリオもテストできます(例えばコンピュータのクロックを変更する必要のあるシナリオでも，コード上で実行可能です)。テストのためにコードを変更すれば，機能を損なうことになりかねません。ユニットテストの生産性が向上することで，作業にじっくりと取り組む余裕が生まれるはずです。
  </blockquote> 
  <p><strong>C#やVB.NETはサポートしていますか？</strong></p> 
  <blockquote>
   いいえ，Isolator++はCとC++でのみ動作します。マネージドな.NET言語には，Isolator for .NETを用意しています。Isolator++ for .NETは単なる.NET用の&quot;すべてをモックする&quot;フレームワークではなく，SmartRunnerや視覚的なカバレッジ，テストコード補完やテストルールブックなどを備えています。
   <br type="_moz" /> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
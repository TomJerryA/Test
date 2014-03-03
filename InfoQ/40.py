<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>V8でバックグラウンドコンパイルの挑戦</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/chrome-v8-background-compilation"><em>原文(投稿日：2014/02/15)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>この記事にはChromeのJavaScriptエンジンV8に最近導入されたバックグラウンド コンパイルの詳細が含まれている。</p> 
  <p>Googleの最新ブラウザーは、Chrome Beta v. 33でありJavaScript V8エンジンに重要な変更が含まれている: 最適化されたコンパイル プロセスをバックグラウンド スレッドで処理して、メイン スレッドは応答し続けることで、パフォーマンスを向上させることができる。 Google EngineerのYang Guo氏によると<a href="http://blog.chromium.org/2014/02/compiling-in-background-for-smoother.html">V8のコンパイルには2種類</a>あるという:</p> 
  <blockquote> 
   <p>全体のコンパイル時間を短くするために、V8はJavaScriptのコンパイルを最初に実行される直前まで延期する。このコンパイル フェーズは高速だが、コードの最適化には焦点を当てておらず、すぐに完了する。V8では、<a href="http://blog.chromium.org/2010/12/new-crankshaft-for-v8.html">最適化コンパイラー</a> [Crankshaft]によって、非常に頻繁に二度目のコンパイルが実行される。二度目のコンパイル パスは、多くの高度な最適化技術を使用しているため、最初のパスよりも時間がかかるが、非常に高速なコードを生成する。</p> 
  </blockquote> 
  <p>最適化コンパイルを別スレッドで実行することで、アプリケーションの応答性がよくなるだけでなく、<a href="https://developers.google.com/octane/">Octane 2.0</a>ベンチマーク スイートの<a href="https://developers.google.com/octane/benchmark#mandreel">Mandreel</a>テストがNexus 5で27%高速化したとGuo氏は言う。</p> 
  <p>InfoQはChrome 33で(--js-flags=&quot;--concurrent-recompilation&quot;)と、非同期再コンパイルなし(--js-flags=&quot;--no-concurrent-recompilation&quot;)でテストを実施した。実行ごとにブラウザーを再起動して、テストを5回連続で実行した平均を考慮すると、Octane 2.0ベンチマークが以下のように改善されていることがわかった:</p> 
  <table cellspacing="0" cellpadding="2" width="316" border="1" unselectable="on"> 
   <tbody> 
    <tr> 
     <td valign="top" width="200"><strong>テスト</strong></td> 
     <td valign="top" width="114"><strong>改善</strong></td> 
    </tr> 
    <tr> 
     <td valign="top" width="200">Octane 2.0 (全17テスト)</td> 
     <td valign="top" width="114"> <p align="right">7.12%</p> </td> 
    </tr> 
    <tr> 
     <td valign="top" width="200">Mandreel</td> 
     <td valign="top" width="114"> <p align="right">18%</p> </td> 
    </tr> 
    <tr> 
     <td valign="top" width="200">Box2DWeb</td> 
     <td valign="top" width="114"> <p align="right">32%</p> </td> 
    </tr> 
    <tr> 
     <td valign="top" width="200">zlib</td> 
     <td valign="top" width="114"> <p align="right">11%</p> </td> 
    </tr> 
   </tbody> 
  </table> 
  <p>大きな改善は2Dや3Dの物理エンジンで見られ、Octaneスイート全体のベンチマークで7%の改善が見られた。</p> 
  <p>私たちは、最適化コンパイラーがなぜ<a href="http://www.infoq.com/jp/news/2010/12/Google-Chrome-OS/">Crankshaftがリリースされた2010年12月</a>に導入されなかったのかをGuo氏に尋ねた。彼がGoogleのために話しているわけではなく、また彼はその時点ではチームにいなかったが、Guo氏は改善は実際の必要性に基づいて実施されていると述べた:</p> 
  <blockquote> 
   <p>Crankshaftが設計された時点では、レイテンシーに大きな問題はありませんでした。JavaScriptコードはまだ、コンパイル時間が顕著になるサイズには至っていなかったため、低レイテンシーは問題でも、Crankshaftの設計目標でもありませんでした。私の考えでは、その時点で並列処理を導入することは、時期尚早であり、すぐにメリットがなく、駆け出しの最適化コンパイラーの設計を必要以上に複雑にすることになっていたでしょう。</p> 
   <p>ここ数年でこの状況は明らかに変化しました。<a href="https://code.google.com/p/octane-benchmark/source/browse/#svn%2Ftrunk">最新版のOctaneベンチマークスイート</a>を見ると、いくつかのサイズは1MB以上になっていることがわかります。これは、JavaScriptエンジンを限界まで使っている実世界を反映しています。Mandreelベンチマークは、最小化された4.8MBのコードで構成されています。比較のために<a href="http://computerhistory.org/atchm/adobe-photoshop-source-code/">Photoshop 1.0のソースコード</a>を展開すると4.4MBです。このコード量を処理すると時間がかかってしまい、特に問題となるケースとしては、アニメーションのレンダリングをした時には一瞬で完了することが期待されています。</p> 
  </blockquote> 
  <p>網羅的ではないにしても、Guo はV8でバックグラウンド コンパイルを実装するにあたって、なにが課題であったかについても語った:</p> 
  <blockquote> 
   <p>- すべてのコンピューター サイエンティストが言うように、マルチスレッドはとても難しいです。きちんとテストを網羅するのは難しいです。特定の動作に起因するバグを再現するのは、難しいかもしくは不可能です。アサーションによる不変値のガード、ファズテスト、そして最後にCanaryテストカバレッジによって、それが正しいという自信を持つことができました。<a href="https://code.google.com/p/data-race-test/wiki/ThreadSanitizer">ThreadSanitizerチーム</a>に拍手を送りたい。</p> 
   <p>- 実行を停止したコンパイルにおいては、コンパイルの前後で、そのすべてのオブジェクトを含む、JavaScriptヒープの状態が同じことを確認する。並列コンパイルでは、すでにこの前提は成立しない。これはいくつかの意味を持っている:</p> 
   <p style="margin-left: 40px;">- V8は、GCをキックするたびにオブジェクトが移動されるため、参照を更新する必要がある。これはコンパイル ジョブの実行中に頻繁に発生する可能性がある。コンパイル ジョブが保持するオブジェクトの参照が更新されない場合は、無効なメモリ アクセスになってしまう。</p> 
   <p style="margin-left: 40px;">- 実行中も並列コンパイルが継続している。これは、VMの状態とオブジェクトの中身、レイアウトが自由に変更できることを意味している。コンパイル ジョブの開始時の事実に基づく仮定は、終了時には意味がなくなっている可能性もある。最後に生成されたコードであっても有効ではない可能性もある。それを実行してしまうと、バグやクラッシュが発生する。これは正しく取り扱う必要がある。</p> 
   <p style="margin-left: 40px;">- 実際に、バックグラウンド スレッドはいつでもヒープにアクセスするため、競合状態になる可能性が非常に高い。私たちは、コンパイル ジョブの前に必要な情報をすべて集めることでこれを避けている。</p> 
   <p>- バックグラウンド スレッドでコンパイル ジョブをキックする正確な時間を見つけることは難しい: コードを最適化するために時間をかける価値があるかどうか、簡単にメリットを得ることができるかどうかを予見することはできない。それをケアするためにヒューリスティックな解決策を探すことはより困難である。多くの微調整が必要であったが、作業はまだ継続中である。</p> 
   <p>- 遅延解析のような相互接続状態を通じたソースコードのライフサイクルは、高速コンパイラーを使った初回コンパイルの後、最適化コンパイラーで最適し、(コンパイル時に後から停止すると仮定した場合)おそらく非最適化する、などすでに複雑である。並列コンパイルでは、2つの新しい状態がこのライフサイクルに追加された。これらすべてを追跡し続け、バグがなく、効率的であることを保証することは重要である。予想外の特殊なケースでは問題が発生することがある。</p> 
  </blockquote> 
  <p>Guo氏によると“V8はアクティブに開発されており、着実に改善されています”。<a href="https://www.dartlang.org/performance/">Dartによって維持されるライブ パフォーマンス チャート</a>では、2月のDeltaBlueベンチマークにおいてV8は、30%向上していることがわかる。11日の改善はコンパイラーの最適化によるもので、バックグラウンド コンパイルに関連する訳ではない。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
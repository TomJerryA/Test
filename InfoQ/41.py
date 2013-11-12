<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Google Espresso: Android UI のクラウド型高速自動化テスト</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/10/google-espresso-testing"><em>原文(投稿日：2013/10/24)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Google 製オープンソースの <a href="https://code.google.com/p/android-test-kit/wiki/Espresso">Espresso</a>は、Android の自動テストフレームワークであり、クラウド上の x86 マシンを使ってマルチスレッド環境でテストを実行することができ、UIテストに関する平行性の課題を解決する。</p> 
  <p>実際の Android 端末でテストを実施するのは、デバイスの数と種類の多さのため、非常に時間が掛かって高くつく作業である。一つの解決策は、エミュレータでテストを実行することである。エミュレータは複数のOSバージョン、画面サイズ、そしてメモリ制約を設定できる、コントロール可能な環境である。この方法はほとんどのコードバグをキャッチできるだろうが、残りのバグは人間のテスターが実際の端末でテストするまで見つからないだろう。</p> 
  <p>エミュレータの問題点は、その実行速度にある。ボトルネックは、ARM CPUエミュレータ上でAndroidを実行している点である。この課題を解決するため、Googleは x86ハードウェアで直接実行し、VMアクセラレーションを使うバージョンの Android を作成した。もう一つのボトルネックは、Android の起動時間であるが、それはOSのスナップショットを取得して実行することで対処されており、これにより目的のOSとアプリケーション設定を短時間で実行できる。この方法を用いることで、Googleは、8200万回の Android テストを今年の３月に実施した。</p> 
  <p>Nexus4 とエミュレータでのテストを較べると、後者はテストを完了するのに実際のデバイスの 65% の時間で済ませることができた。すなわち、良いエミュレータは自動化テストの問題を解決したように見える。しかし、そこにはまだ障害がまだ残っている。自動化テストは Android 上の計測用APIを用いるが、その API コールはUIスレッドとは別のスレッドで実行するので、自動化されたユーザインターフェイスのテストは、矛盾した信頼できないテスト結果という形で、やっかいな並行性の問題（スレッド競合）を引き起こしてしまうのだ。この問題に対する Google の解決策が <a href="https://code.google.com/p/android-test-kit/wiki/Espresso">Espresso</a> である。Espressoは UI テストをマルチスレッド環境で安全に実行させ、テストを書く際のおきまりの定型コードの大部分を不要にするテストフレームワークである。Espresso は携帯電話、TV、スマートグラス、車、等などの様々なモバイル機器で使うことができ、様々な画面サイズやメモリ容量、複数のAPIバージョンや異なるネットワーク環境を設定できる。Espresso の開発チームによれば、このソリューションは、Androidにおける<a href="https://www.youtube.com/watch?v=uHoB0KzQGRg#t=2385">バグの99%をキャッチすることができ</a>、実機を使った人間によるテストを必要とするのはごくわずかな残りのバグだけとなるので、総合的なテストの労力を削減することができる、とのことである。</p> 
  <p>例えば、あるビューが表示されないことの「表明」に対するテストは、Espressoを使うとこのようになる。</p> 
  <pre>
      onView(withId(R.id.bottom_left)).check(matches(not(isDisplayed())));</pre> 
  <p>他のテストのサンプルは、<a href="https://code.google.com/p/android-test-kit/wiki/EspressoSamples">ここで</a>見つけることができるだろう。</p> 
  <p>現在、Espressoはデベロッパ・プレビュー状態にあり、Google Code上で提供されているが、このフレームワークが熟成され十分に安定したら、Android SDKに含まれるようになるだろう。Espressoは、Google+やGoogle Maps, Google Drive などのGoogle製の30種類以上のアプリケーションのテストで用いられている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
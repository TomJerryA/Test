<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Greg Young氏，CEP(複合イベント処理)を語る</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/complex-event-processing"><em>原文(投稿日：2014/01/29)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>過去の記録データ全体にクエリを行うような，時間軸に対して実行しなければならない問題には，<a href="http://en.wikipedia.org/wiki/Complex_event_processing">Complex Event Processing</a>(CEP/複合イベント処理)が非常に有効だ – <a href="http://goodenoughsoftware.net/about/">Greg Young</a>氏は先日のプレゼンテーションで，このように提言した。<br /> 氏はイベント処理を，発生したある事象に関連するデータの経緯を解析し，そこから結論を導き出す方法だ，と説明している。ひとつの例は，異なった時間に発生した事象を関連付けしたい場合に用いられる，時間的相関の問合せだ。Twitterストリーム上で ，&quot;誕生日&quot; という単語を使ってから１分以内に &quot;プレゼント&quot; を使ったユーザを見つけ出す，あるいは臨床試験において，試験期間中の異なる時間にある特定の反応を示した患者を検索する，といった例が考えられる。</p> 
  <p>問合せの作成に氏が使用しているのは，イベントストリーム上で動作するクエリ言語で，JavaScriptで実装されている。JavaScriptでクエリを記述するため，Webブラウザを使用した記述やデバッグも可能だ。<br /> このクエリ言語は，<a href="http://geteventstore.com/docs/what-is-an-event-store.html">イベントソース(Event Source)</a> の概念に従って開発された<a href="http://en.wikipedia.org/wiki/NoSQL">NoSQL</a>である<a href="http://geteventstore.com/">Event Store</a> に含まれている。イベントソーシングでは，状態を直接的に表現する代わりに，ある特定の時間に発生した事実(fact)の連続として表現する。この方法でデータを保存することにより，現在の状態だけでなく，状態の変化がすべて保存されるため，情報が失われることがなくなる。</p> 
  <p>事実ないしイベントを保存することは，タイムマシンを作るようなもので，ある時間に立ち戻って過去の状態を見ることが可能になる。例えば，今日作成したレポート処理を実行して，１ヶ月前のレポートを発行することができるのだ。<br /> もうひとつのユースケースは，未来の方向に注目して，予測能力を評価するというものだ。1ヶ月前の時点で予測モデルを実行して今日の結果を予測し，実際の結果との比較を行うことでこれが可能になる。</p> 
  <p>Event Storeはオープンソースプロダクトで，修正版BSDライセンスで公開されている。最初のリリースは2012年9月だ。</p> 
  <p>Event Storeのリードアーキテクトを務めるGreg Young氏は，<a href="http://martinfowler.com/bliki/CQRS.html">CQRS</a> (Command Query Responsibility Segregation / コマンドクエリ責務分離) という造語で有名な独立系コンサルタントである。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
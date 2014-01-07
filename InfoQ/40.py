<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Twitterでの予測</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/twitter-forecasting"><em>原文(投稿日：2013/12/30)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://velocityconf.com/velocityeu2013">Velocity Conf London</a>でTwitterの<a href="http://velocityconf.com/velocityeu2013/public/schedule/speaker/150556">Arun Kejariwal氏</a>が<a href="http://www.slideshare.net/arunkejariwal/gimme-more-supporting-user-growth-in-a-performant-and-efficient-fashion">Twitterで使われている予測アルゴリズム</a>について話した。予測アルゴリズムはシステムリソースの予測とユーザ数やツイート数などビジネス上の指標の予測に使われている。Twitterのデータストリームのダイナミックさを考慮した場合、磨き直した<a href="http://en.wikipedia.org/wiki/Autoregressive_integrated_moving_average">ARIMAモデル</a>は一度予測エラーを検出して、異常値を排除できれば有効に働くということがわかった。</p> 
  <p class="MsoNormal"><span lang="EN-GB">Twitterでの予測の適用可能性の評価は、予測の正確さに加えて、モデルの季節性(例えば、1日の使われ方の循環パターンを調整する)とトレンド(例えば、大規模なスポーツイベントで利用が跳ねる)を扱う能力が重要だ。Twitterは全世界でユーザを増やしてきたため、十分な予測モデルが必要がなければトレンドをとらえることができないのだ。</span>
   <o:p></o:p></p> 
  <blockquote>
   ユーザが増えるにつれ、ツイートやお気に入り、写真などのビジネス上の指標を予測するのは上述のトレンドと季節性のために重要な事案になっています。線形回帰は役に立ちません。というのは、時系列上の季節性を捉えないからです。この限界を突破するため、一定の時系列でのトレンドと季節性を明確にモデル化し、しっかりとした予測を定期的に生み出すことができるARIMAモデルの利用を探ってきました。
   <br /> 
  </blockquote> 
  <p class="MsoNormal">しかし、むやみにARIMAモデルを使っても十分な予測はできない。ARIMAモデルは時系列を複数の短い期間に分割するからだ。ある普通ではない期間に季節性がなかったら、全体の季節性も消えてしまう。さらに、ある期間の境界のデータポイントが<a href="http://en.wikipedia.org/wiki/Outliers">異常値</a>の場合、全体の予測も歪んでしまう。最初の予測は分析する必要があり、データの中にはクリーニングしないとより正確で使える予測を生まないものもあるだろう。氏は、異常値を開発チームに伝え、コードの変更が必要かどうかを調査してもらっていると言う。</p> 
  <p class="MsoNormal"><img src="http://www.infoq.com/resource/news/2014/01/twitter-forecasting/ja/resources/ARIMA_based_forecast.png" alt="" _href="img://ARIMA_based_forecast.png" _p="true" /></p> 
  <p class="MsoNormal" align="center" style="text-align:center"><i><span lang="EN-GB">ARIMAによる予測。下降のスパイク(異常値)が初期にある</span></i><i><span lang="EN-GB">(Arun Kejariwal氏提供)</span></i></p> 
  <p class="MsoNormal" align="center" style="text-align:center"><i><span lang="EN-GB">
     <o:p></o:p></span></i></p> 
  <p class="MsoNormal"><img src="http://www.infoq.com/resource/news/2014/01/twitter-forecasting/ja/resources/1ARIMA_based_forecast_without_initial_spike.png" alt="" _href="img://1ARIMA_based_forecast_without_initial_spike.png" _p="true" /></p> 
  <p class="MsoNormal" align="center" style="text-align:center"><i><span lang="EN-GB">ARIMAによる予測。初期に</span></i>異常値がない<i><span lang="EN-GB">(Arun Kejariwal氏提供)
     <o:p></o:p></span></i></p> 
  <p class="MsoNormal"><span lang="EN-GB"><br /> ARIMAに加え、Twitterでは予測したいリソースに応じて、ほかのモデル(<a href="http://en.wikipedia.org/wiki/Holt-Winters">Holt-Winters</a>、<a href="http://en.wikipedia.org/wiki/Smoothing_spline">Spline</a>、<a href="http://en.wikipedia.org/wiki/Linear_regression">線形回帰</a>)も使っている。氏が言うには、</span></p> 
  <blockquote>
   私たちは多くの予測モデルを調査しています。どのモデルを使うかは文脈依存であり、モデル選択の問題(積極的に研究している分野です)に関わります。
   <br /> 
  </blockquote> 
  <blockquote>
   季節性がなければ、線形回帰が望ましいです。相対的には簡単に計算できますから。非線形なドレンドがあるなら、二次モデルが使えます。しかし、トレンドと季節性がある場合は、自明な選択肢はありません。
   <br /> 
  </blockquote> 
  <p class="MsoNormal"><span lang="EN-GB">氏によれば、Twitterの予測は通常、技術的な課題(例えば、インハウスシステムのキャパシティの更新)が原因で数週間先までに限られている。たまに、ビジネス上の指標に対して長い期間の予測をする場合がある(ユーザ数など)。近い将来、スケールの弾力性に対する予測も計画している。</span></p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
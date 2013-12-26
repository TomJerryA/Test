<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Gauntltによる継続的セキュリティテスト</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/velocity-eu-day1-gauntlt"><em>原文(投稿日：2013/11/30)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://gauntlt.org/">Gauntlt</a>コアチームのJames Wickett氏は<a href="http://www.slideshare.net/wickett/gauntlt-velocity-eu2013">Velocity Conf London</a>で，アプリケーションのセキュリティレベルに関するフィードバックの迅速化を目的とした，継続的インテグレーションサイクルへのセキュリティテスト統合についての<a href="http://velocityconf.com/velocityeu2013">解説</a>を行った。氏が強調したのは，継続的デリバリによるリリースデリバリ率の増加に伴う，定期的セキュリティチェックの重要性だ。リリース後のセキュリティチェックと長期的な外部監査では，氏によれば，もはや十分とは言えない。アプリケーションの安全を維持し，セキュリティ低下を防止するためには，運用(Ops)と開発(Dev)双方への継続的なフィードバックが必要なのだ。</p> 
  <p class="MsoNormal">
   <o:p></o:p></p> 
  <p class="MsoNormal"><span lang="EN-GB"><a href="http://github.com/GAUNTLT/GAUNTLT"><span lang="EN-US">Gauntlt</span></a></span>はこの考えを実践するために，<a href="http://en.wikipedia.org/wiki/Behavior-driven_development">ビヘイビア駆動開発</a>のツールとして評価の高い<a href="http://cukes.info/">Cucumber</a>と，一連のオープンソースのセキュリティテストツールをベースとした，セキュリティテスト自動化フレームワークを提供している。Gauntltは<a href="http://rubygems.org/gems/gauntlt">Ruby gem</a>として入手可能なので，継続的インテグレーションの<a href="http://www.infoq.com/articles/preparing-for-cd-in-the-enterprise">デリバリパイプライン</a>の一部として，Ruby環境でテストを実行することができる。次の例では，<a href="http://cukes.info/reports.html">Cucumberの場合</a>と同じようなHTMLテストを生成する:
   <o:p></o:p></p> 
  <p class="MsoNormal"><span courier="courier"><code>bundle exec gauntlt --format html &gt; out.html</code></span><span courier="courier">
    <o:p></o:p></span></p> 
  <p class="MsoNormal">Gauntltには，事前に定義された一連の”アタックアダプタ”と，それを使ったアタックをまとめたセットが同梱されている。アタックアダプタはアタックの各ステップを，種類別に実行可能なセキュリティツールにマッピングしたものだ:
   <o:p></o:p></p> 
  <ul> 
   <li><span lang="EN-GB"><a href="http://www.arachni-scanner.com/">Arachni</a> (<a href="http://en.wikipedia.org/wiki/Cross-site_scripting">XSS</a>のテスト)</span></li> 
   <li><span lang="EN-GB"><a href="https://github.com/mozilla/Garmr">Garmr</a>&nbsp;(ログインフロー内の新なたログインページや安全でない参照のテスト)</span></li> 
   <li><span lang="EN-GB"><a href="http://sqlmap.org/">SQLmap</a>&nbsp;(<a href="http://en.wikipedia.org/wiki/SQL_injection">SQLインジェクション</a>攻撃のテスト)</span></li> 
   <li><span lang="EN-GB"><a href="http://dirb.sourceforge.net/about.html">dirb</a>&nbsp;(Webオブジェクト設定のテスト)</span></li> 
   <li><span lang="EN-GB"><a href="https://github.com/iSECPartners/sslyze">SSlyze</a>&nbsp;(SSLサーバ設定のテスト)</span></li> 
   <li><span lang="EN-GB"><a href="http://nmap.org/">NMap</a>&nbsp;(想定外のオープンポートに関するテスト)</span></li> 
  </ul> 
  <p class="MsoNormal">現在のツールセットを拡張するのは，特殊な既定ステップを使ってバイナリコマンドラインの呼び出しを指示し，その実行後の出力をチェックする方法でのみ可能である。
   <o:p></o:p></p> 
  <p class="MsoNormal">
   <o:p>
    &nbsp;
   </o:p>Gauntltは内部的にCucumberを実行しているので，Gauntltのアタック定義ファイルはCucumberの機能ファイルに変換される。Cucumberの各シナリオが特定のアタックに対応する。例えば<code>port-check.attack</code>というアタックファイルでは，対象ホストに想定外のポートがオープンされていないことを確認するために<code>nmap</code>を使用するかも知れない:
   <o:p></o:p></p> 
  <blockquote> 
   <pre><code> <p class="MsoNormal"><span style="font-family:" courier="">Feature: nmap attacks for example.com 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;</span><span style="font-family:" courier="">&nbsp;&nbsp; Background: 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Given &quot;nmap&quot; is installed 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; And the following profile: 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | name &nbsp;&nbsp;&nbsp;&nbsp;| value &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | hostname | example.com |
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;</span><span style="font-family:" courier="">&nbsp;&nbsp; Scenario: Verify that there are no unexpected ports open 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; When I launch an &quot;nmap&quot; attack with: 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;&quot;&quot; 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nmap -F &lt;hostname&gt; 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;&quot;&quot; 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Then the output should not contain: 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;&quot;&quot; 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 25/tcp 
       <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;&quot;&quot;
       <o:p></o:p></span></p> </code></pre> 
  </blockquote> 
  <p class="MsoNormal">氏は &quot;<a href="http://www.infoq.com/news/2010/06/rugged-software-manifesto">頑丈なソフトウェアマニフェスト(Rugged Software Manifesto)</a>” に触発されて，アプリケーションのセキュリティテストに対する強い主張を持ったフレームワークとしてGauntltを作り上げた。<span lang="EN-GB">その最終的な目標は，開発(Dev)，運用(Ops)とセキュリティチームとのコミュニケーションの促進だ。 </span>セキュリティ的考慮と監視機能を<a href="http://en.wikipedia.org/wiki/DevOps">DevOps</a>に統合するというテーマでは，<a href="http://devopsweekly.com/">DevOps Weekly</a>創刊者の<a href="http://www.infoq.com/author/Gareth-Rushgrove">Gareth Rushgrove</a>氏も，<a href="http://vimeo.com/75665772">セキュリティ監視</a>に関する<a href="http://velocityconf.com/velocityeu2013/public/schedule/detail/33016">記事</a>の中で取り上げている。
   <o:p></o:p></p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
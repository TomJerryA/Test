<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Androidはクローズドソースモデルを目指しているのか？</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/android-closed-source-model"><em>原文(投稿日：2014/01/24)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/">Ars Technicaの興味深い分析</a>の中でRon Amadeo氏が，GoogleはAndroidを徐々にクローズソースモデルへとシフトしている，という主張をしている。Googleの戦略は，Androidを &quot;小さなホビーにも&quot; 使えるほど自由にカスタマイズ可能にする一方で，&quot;Googleの祝福を受けずにAndroidを使おうとする&quot; 試みを阻止しているというのだ。</p> 
  <p>Androidに関するGoogleの戦略は，初期の頃とは違ってきている，とAmadeo氏は言う。当初Googleが，完全にオープンなモバイルプラットフォームの提供を目指していたことは間違いない。実用的であるために必要なアプリとサービスをすべて備え，モバイル市場において完成した選択肢となることが目標だったのだ。当時のアプローチは，AOSP(Android Open Source Platform)に可能な限り多くのメーカを参加させる，というものだった。</p> 
  <p>第２段階としてAmadeo氏が続けるのは，Androidが支配的になった後の状況だ。この段階でGoogleは，検索や音楽，カレンダといった，AOSPのパーツの一部の開発に積極的ではなくなった。Ars Technicaの中では，オープンソースとしては開発停止状態となったこれらのアプリを，Googleが再びブランド化して拡張し，Play Storeでクローズドソースのアプリとして提供するようになった経緯が詳細に説明されている。&quot;オープンソースアプリを殺すことはできません。しかし，以降の開発をすべてクローズドソースモデルに移行することで，それをアバンダンウェア(破棄されたソフトウェア)化することは可能なのです。&quot; とAmadeo氏は言う。Ars Technicaの公開後に，<a href="http://www.unwiredview.com/2013/11/21/android-4-4-kitkat-ships-without-browser-app-oems-have-to-license-chrome-or-build-their-own/">Android 4.4からChromeが削除された</a>ことも注目に値する。</p> 
  <p>GoogleのAndroid戦略が目標とするもうひとつの柱は，OHA(Open Handset Alliance)によるメーカのロックインだ。OHAのメンバは &quot;その契約上，<a href="http://source.android.com/compatibility/overview.html">Googleの承認しないデバイス</a>の開発が禁止されている&quot; のである。これはすなわち，Androidの非互換フォークに基づいて携帯電話を開発しようとするOEMは，OHAの参加資格，つまり開発した製品上でGoogle Appsを利用する手段を失う，ということを意味する。Googleはこの契約義務を，Acerが<a href="http://en.wikipedia.org/wiki/Aliyun_OS">Aliyun OS</a>という，クラウドベースの中国製Androidフォークをベースとする携帯電話を出荷しようとした時に適用している。さらに有名なのは，Amadeo氏の言葉を借りるならば，Androidファミリに留まりたいと思う &quot;大手OEMには，Kindle FireをAmazon向けに生産することが許されていない&quot; ことだ。</p> 
  <p>戦略の第３の柱としてArs Technicaの記事が挙げているのは，Google mapsやプッシュ通知，位置情報，アプリ内課金，ゲームなどのプロプライエタリAPIによるサードパーティアプリのロックインだ。これらのAPIはAOSPに含まれないため，Googleの承認を受けないデバイスでは使用できない。Amadeo氏によれば，こういうことだ。</p> 
  <blockquote> 
   <p>Google Play Serviceに関するGoogleの戦略は，Googleが承認したデバイス上での開発を可能な限り容易にすることで – 同時に，承認されないデバイスでの開発をできる限り難しくすることで – ‘Android App エコシステム’を‘Google Play エコシステム’に置き換える，というものです。</p> 
  </blockquote> 
  <p>記事に対するコメントのいくつかには，次のような点が指摘されている。</p> 
  <ul> 
   <li>Googleの戦略 &quot;は，Androidのデフラグです [...] Googleがこれを行うのは，それが必要だからなのです。&quot; (<a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/?comments=1&amp;post=25517069">idealego</a>)</li> 
   <li>&quot;個々のユーザの観点で言えば，GoogleはAndroidデバイスに価値をもたらして，便利にしてくれているのです... &quot; (<a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/?comments=1&amp;post=25516865">batmanuel</a>), &quot;Googleがそれらを厳しく管理するのは，まったく正当なことです。&quot; (<a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/?comments=1&amp;post=25517107">karlsvec</a>)</li> 
   <li>&quot;これら付属ソフトがすべてクローズドソースになったとしても，基本であるAndroidがオープンソースであることに変わりありません。&quot; (<a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/?comments=1&amp;post=25517153">walkop</a>)</li> 
  </ul> 
  <p>その一方で，次のような点を強調するコメントもある。</p> 
  <ul> 
   <li>&quot;‘オープンソースAndroid’ というGoogleの PR自体がそもそも嘘です。&quot; (db<a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/?comments=1&amp;post=25517261">right</a>)</li> 
   <li>この戦略，特にOHA協定は，モバイル新興企業によるイノベーションを阻害しかねません。(<a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/?comments=1&amp;post=25517125">ChrisSD</a>)</li> 
  </ul> 
  <p>これを書いている時点で寄せられた<a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/?comments=1&amp;post=25516889#comment-25516889">コメントの大部分</a>が，Googleの戦略をMicrosoftの &quot;3E(Embrace, Extend, Extinguish/吸収，拡大，根絶)&quot; 戦略に擬えている。(<a href="http://arstechnica.com/gadgets/2013/10/googles-iron-grip-on-android-controlling-open-source-by-any-means-necessary/?comments=1&amp;post=25516889#comment-25516889">Paul Rodgers</a>)</p> 
  <p>議論はArs Technicaの外にも拡がっている。<a href="http://www.androidauthority.com/google-control-friday-debate-286504/">Android Authorityがホストするディベート</a>の中ではRobert Triggs氏が，Googleには &quot;プロプライエタリな製品やサービスが必要なのです。ソフトウェアをすべて，オープンソースコミュニティに解放することは不可能ですから。&quot; と述べている。またAdam Koueider氏は，GoogleのAndroidに対するコントロール範囲が拡大することは，最終的にユーザにもメリットがあると見ている。&quot;ひとつのパイを14の方向に，まったく別々に引っ張られなくですむ&quot; からだ。<a href="http://www.androidauthority.com/google-control-friday-debate-286504/#ViewPollResults">Android Authority Webサイトで実施された調査</a>によると，Googleによるコントロールの拡大はユーザにとってよいことだ，という意見が回答者の72%，結果的に悪くなる，という意見が13%だった。</p> 
  <p>Stijn Schuermans氏は<a href="http://www.visionmobile.com/blog/2013/11/the-naked-android/?1">'The Naked Android'</a>という記事の中で，プロプライエタリAPIに関するGoogleの戦略を整理している。</p> 
  <blockquote> 
   <p>Amazonや数え切れないほどのアジアの携帯電話メーカが，このオペレーティングシステムをフォークしています。さらに悪いことに，Google Playを独自のアプリストアで置き換えて既存のAndroidアプリを活用したり，Googleのサービス(Map)をサードパーティの代替サービス(NokiaのHERE)で代用したりすることが，いとも簡単にできてしまうのです。Androidのブランド自体，SamsungのGalaxyの影に隠れてしまって，もはや中核と呼べるものではありません。</p> 
  </blockquote> 
  <p>Googleが選択した対応策としてSchuermans氏が指摘しているのは，Androidを基本部分だけ残して分解し，手放せるようなものにした上で，プロプライエタリなGoogle Play ServiceやGoogle Appsと組み合わせる，というものだ。</p> 
  <p>この問題にはもうひとつ，OEMメーカに関する側面がある。彼らとGoogleとの関係，Androidへのコントロールを増大させるGoogleに対して彼らがどのような対応をするか，という点だ。</p> 
  <p>特許侵害訴訟に関する調査の一環として，The VergeのNilay Patel氏が，<a href="http://www.theverge.com/2011/05/12/google-android-skyhook-lawsuit-motorola-samsung/#2">OEMメーカに対するGoogleの慣習を報告</a>している。そこではGoogleが &quot;互換性を[OEMメーカに]やりたいことに従わせるためのクラブとして使用して&quot; いたと同時に，OEMメーカもそれを認識していた形跡がある，と指摘されている。さらにGoogleは，&quot;Andy Rubin氏自身がOEMからの要求を承認あるいは拒否するという方法で，Androidデバイスの開発において重要な役割を果たしていた&quot; とも述べられている。</p> 
  <p>Samsungがモバイルハンドセットの63%を販売し，最も成功したハンドセット10機種中5機種が同社のモデルである(<a href="http://www.localytics.com/blog/2013/fonblets-and-phablets-samsung-has-share-of-android-mobile-devices/">Localyticsデータ</a>)という現状においては，自身のソフトウェアをコントロールできていない点がSamsungにとって打破すべき限界となっていることや，Androidを乗り越えるために自社のTizen OSへの関与をますます深めていることは理解できる話だ，と<a href="http://www.firstpost.com/tech/why-samsung-is-planning-to-ditch-android-for-its-new-tizen-os-1225473.html">AP通信は伝えている</a>。</p> 
  <p>Parmy Olson氏も<a href="http://www.forbes.com/sites/parmyolson/2013/10/28/samsung-kicks-off-its-first-developers-conference-as-it-seeks-an-edge-in-software/">Forbesに向けた記事において</a>，Samsungが最近になって拡大する自社のプラットフォームに対する開発者コミュニティの関与を深めようと努力している点と，GoogleのAndroidに対するコントロールが拡大したことの関連性を立証している。その上で氏は，&quot;ユニークなソフトウェアサービスを通じて，いかにユーザのロイヤリティをつなぎ止めるかという点に，Androidの将来的な成長がかかっている&quot; と述べている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
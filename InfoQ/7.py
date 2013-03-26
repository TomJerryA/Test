<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>小から超大規模ウェブサイトまでのMySQL参照アーキテクチャ</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/MySQL-Reference-Architectures;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1"><em>原文(投稿日：2013/03/14)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Oracleが発表した<a target="_blank" href="http://www.mysql.com/why-mysql/white-papers/mysql-reference-architectures-for-scalable-web-infrastructure/">大規模な拡張性を備えたWebインフラストラクチャのためのMySQLリファレンスアーキテクチャ</a>、ホワイトペーパーには、データストレージにMySQLを使用してWebサイトのさまざまな種類とサイズ向けの推奨トポロジが概要されている。</p> 
 <p>このホワイトペーパーは、サイズと提供する4つの異なるタイプのサービスに対する可用性の要求に基づいた、MySQLを使うウェブサイトの作成用の4つのリファレンス・アーキテクチャを提案している。4つのサービスは、ユーザーとセッション管理、eコマース、アナリティクス（多構造化データ）、CMS（メタデータ）で、以下のテーブルに示す。&nbsp;</p> 
 <p class="image-wide"><img style="background-image: none; border-right-width: 0px; padding-left: 0px; padding-right: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px; padding-top: 0px" border="0" alt="" _p="true" _href="img://MySQL-1.png" src="http://www.infoq.com/resource/news/2013/03/MySQL-Reference-Architectures/ja/resources/MySQL-1.png;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1" /></p> 
 <p>これらのガイドラインは、基本的な推奨事項であり、使用される読み取り/書き込みのパターン、ロード・バランシング、キャッシングのメカニズムなどに基づいて調整される必要がある。</p> 
 <p><strong>小規模なWebリファレンスアーキテクチャ </strong></p> 
 <p>このリファレンス・アーキテクチャは、前に述べた4つのタイプのウェブサイトのすべての小規模な実装に使用することができる。MySQLレプリケーションは、バックアップや分析の目的でデータのコピーを作成するために使用することができる。</p> 
 <p><a href="$image[4].png;jsessionid=D37507DBDD46C3811D9D4D8BB358754C;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1"><img style="background-image: none; border-right-width: 0px; padding-left: 0px; padding-right: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px; padding-top: 0px" title="image" border="0" alt="image" _p="true" _href="img://MySQL-2.png" src="http://www.infoq.com/resource/news/2013/03/MySQL-Reference-Architectures/en/resources/MySQL-2.png;jsessionid=D37507DBDD46C3811D9D4D8BB358754C;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1" /></a></p> 
 <p><strong>中規模なWebリファレンスアーキテクチャ</strong></p> 
 <p>この場合、各MySQLインスタンスが、もしアプリケーション・サーバーの数がスケーラビリティの目的のために増加されている場合は、もっとスレーブ・インスタンスを追加し、最大8個のアプリケーション・サーバーを提供できることを考慮して、活動の異なるタイプごとに別々のインフラを使用することを薦めている。</p> 
 <p class="image-wide"><a target="_blank" href="/resource/news/2013/03/MySQL-Reference-Architectures/en/resources/MySQL-3.png;jsessionid=D37507DBDD46C3811D9D4D8BB358754C;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1"><img style="background-image: none; border-right-width: 0px; padding-left: 0px; padding-right: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px; padding-top: 0px" title="image" border="0" alt="image" _p="true" _href="img://MySQL-3.png" src="http://www.infoq.com/resource/news/2013/03/MySQL-Reference-Architectures/en/resources/MySQL-3.png;jsessionid=D37507DBDD46C3811D9D4D8BB358754C;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1" /></a></p> 
 <p>セミ非同期なレプリケーションと一緒に<a target="_blank" href="http://en.wikipedia.org/wiki/Linux-HA">Linux Heartbeat</a> がセッション管理とeコマースの高可用性目的の為に使われている。CMSサイトには、通常、読み取り操作でスケールアウトするために、より大きなニーズがあり、ホワイトペーパーでは、各スレーブは最大3000人の同時ユーザーを処理できることを考慮して、各MySQLマスタに20から30のスレーブを追加することを推奨している。CMSシステムは、SAN、または各サーバーに接続された分散型デバイス上にデータを格納することができる。</p> 
 <p>アプリケーションとMySQLサーバの負担の多くを緩和するために、セッション管理とCMSサイトの両方にメモリキャッシュを使用することが推奨されている。</p> 
 <p>分析目的のトポロジーは、もっと簡単で、3つのスレーブを持つマスターがジョブをこなす。</p> 
 <p><strong>大規模なWebリファレンスアーキテクチャ</strong></p> 
 <p>この参照アーキテクチャに対しては、ホワイトペーパーは、地理的に離れたクラスタ間で非同期レプリケーションを提供するMySQL地理的レプリケーションを使用して、異なるデータセンター間でのデータベースの複製を推奨している。</p> 
 <p class="image-wide"><a target="_blank" href="/resource/news/2013/03/MySQL-Reference-Architectures/en/resources/MySQL-4-XL.png;jsessionid=D37507DBDD46C3811D9D4D8BB358754C;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1"><img style="background-image: none; border-right-width: 0px; padding-left: 0px; padding-right: 0px; display: inline; border-top-width: 0px; border-bottom-width: 0px; border-left-width: 0px; padding-top: 0px" title="image" border="0" alt="image" width="640" height="375" _p="true" _href="img://MySQL-4-XL.png" src="http://www.infoq.com/resource/news/2013/03/MySQL-Reference-Architectures/en/resources/MySQL-4-XL.png;jsessionid=D37507DBDD46C3811D9D4D8BB358754C;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1" /></a></p> 
 <p>セッション管理とeコマースサイトでは、論文はクラスタを使用する必要があると言っている。 &quot;4xデータノードを使えば、各ページが8- 12のデータベース操作を生成する場合、1秒で6000セッション（ページヒット）をサポートすることが可能です &quot;。大規模CMSサイトは、単に必要に応じてスレーブを増やす中規模なものと同様の構成を使う。Data Refinery ユニットは、分析データをクリーンアップし、整理するために導入される。</p> 
 <p><strong>特大規模なWebリファレンスアーキテクチャ </strong></p> 
 <p>ホワイトペーパーは、ソーシャルなウェブサイトにも、MySQLは &quot;Google、FacebookやYouTubeなどウェブ上で最もトラフィックの多いトップ10サイトの内9社で配備されている”と言って使用を推奨している。ただしこれらのサイトが何にMySQLを使っているかは言っていない。しかし、LinkedInがMySQLの使用で成功しているのは、知られている。</p> 
 <p>ソーシャルなトポロジーは、専用アプリケーション・サーバー、メモリキャッシュ、データリファイナリーを含んだ中/大規模のウェブサイトが実装している概念を使用しているが、書き込み操作をスケールアウトできるようにシャードを導入している。MySQLクラスタは、ユーザー認証、検索、「検索に複数キーが使われる」時に適切なシャードに読み込みと書き込もを割り振るために使われている。</p> 
 <p class="image-wide"><a target="_blank" href="/resource/news/2013/03/MySQL-Reference-Architectures/en/resources/MySQL-5-XL.png;jsessionid=D37507DBDD46C3811D9D4D8BB358754C;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1"><img style="background-image: none; border-bottom: 0px; border-left: 0px; padding-left: 0px; padding-right: 0px; display: inline; border-top: 0px; border-right: 0px; padding-top: 0px" title="image" border="0" alt="image" width="640" height="405" _p="true" _href="img://MySQL-5-XL.png" src="http://www.infoq.com/resource/news/2013/03/MySQL-Reference-Architectures/en/resources/MySQL-5-XL.png;jsessionid=D37507DBDD46C3811D9D4D8BB358754C;jsessionid=12DD1EC39CD2AA2F58BCFB90146A38D1" /></a></p> 
 <p>MySQLマスタサーバとスレーブサーバの両方の推奨仕様は以下のとおり。</p> 
 <ul> 
  <li>8から16のx86-64ビットのCPUコア（MySQLバージョン5.5以上）</li> 
  <li>4から8までのx86 -64ビットCPUコア（MySQL 5.1とそれ以前のバージョン）</li> 
  <li>アクティブなデータよりも３から10倍以上のRAMが必要</li> 
  <li>Linux、Solaris、またはWindowsオペレーティングシステム</li> 
  <li>最低4倍のハードディスクドライブ。8から16のディスクがI / O集中型アプリケーションのパフォーマンスが向上する</li> 
  <li>バッテリバックアップされたキャッシュを搭載したハードウェアRAID</li> 
  <li>RAID 10は、推奨される。ワークロードは、読み取り集中型である場合、RAID 5が適しています</li> 
  <li>2倍のネットワーク・インタフェース・カードと冗長性を確保のために2倍の電源ユニット</li> 
 </ul> 
 <p>ホワイトペーパーは、またMySQLクラスタやデータストレージデバイスの推奨事項に加え、監視、バックアップ、クラスタ管理のためのソリューションを含んでいる。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
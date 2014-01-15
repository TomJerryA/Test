<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>FutureOpsと不変インフラストラクチャ，ビルトイン障害回復</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/futureops"><em>原文(投稿日：2013/12/31)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://www.vagrantup.com/">Vagrant</a>を開発したMitchell Hashimoto氏が先月の<a href="http://velocityconf.com/velocityeu2013">Velocity Conf London</a>で，“FutureOps” に対する自身のビジョンをテーマに，<a href="http://www.infoq.com/news/2013/08/immutable-servers">不変(Immutable)インフラストラクチャ</a>とビルトイン障害回復(Built-in Failure Recovery)の話題を交えながら講演を行った。</p> 
  <p><span lang="EN-GB">氏が披露したビジョンには，(コンフィギュレーション管理ツールによる)環境の再現性，(事前に構築された静的イメージを使用した)極限的な高速展開，(分散型オーケストレーションツールによる)サービスオーケストレーションなどの話題が包含されている。</span>このシナリオでは，新しいサーバの追加と障害の発生したサーバの置き換えとの間で，動作上の違いは何もない。
   <o:p></o:p></p> 
  <p class="MsoNormal">氏のビジョンが基本とするのは，<span lang="EN-GB">スタートアップ時に行われたマシン設定を一切変更しない</span>という，不変インフラストラクチャの発想だ。<span lang="EN-GB">起動以降の環境変更はすべて，古くなった不変マシンに代えて新たなマシンを配置することで対応することになる(複雑なデータベースサーバの更新や，CSS修正のような些細なアプリ修正は別として)。</span><span lang="EN-GB">今日のシステムの無数とも言える外部依存の存在を理由に，このアイデアを<a href="http://www.slideshare.net/MaheshKumar135/uncertain-infrastructure-2">夢物語だとする意見</a>も一部にはある。</span></p> 
  <p class="MsoNormal"><span lang="EN-GB">このような問題に氏が注目するようになったのは，<a href="http://puppetlabs.com/">Puppet</a>や<a href="http://www.getchef.com/">Chef</a>といった最近の構成管理ツールによる部分が大きい。</span><span lang="EN-GB">これらのツールでは，対象とするサーバが同じでも，パッケージやネットワーク可用性，あるいは (Chefの<a href="http://docs.opscode.com/essentials_cookbooks.html">クックブック</a>やPuppetの<a href="http://docs.puppetlabs.com/learning/manifests.html#manifests">マニフェスト</a>といった) 環境定義の変更に対する依存性のために，同一の結果を保証することが難しい。</span><span lang="EN-GB">予測可能性の鍵は，ソースコードからコンパイルされたソフトウェアバイナリと同じように，あらかじめビルドとテストを済ませたマシンイメージ(バイナリ)を使用することにある，と氏は言う。</span></p> 
  <p class="MsoNormal">氏によると，マシンイメージの利用はこれまで，そのメンテナンスの難しさから，あまりよい評価を得られていなかった。しかし現在の構成管理ツールを使えば，継続的インテグレーション方式でイメージを更新していく上で困難な部分は何もない。<a href="http://sysadvent.blogspot.pt/2013/12/day-14-what-is-packer.html">Packer</a>のような新しいツールでは，単一のテンプレートと環境定義のセットから複数の<a href="http://en.wikipedia.org/wiki/Hypervisor">ハイパーバイザ</a>(VirtualBoxやVMWareなど)に対応するイメージを構築することによって，作業はさらに簡素化されている。
   <o:p></o:p></p> 
  <p class="MsoNormal">しかしながら，サービスの検索やオーケストレーションタスク(ロードバランスの設定のような)に関しては，イメージの展開後に(配信プロセスそのものとは別に)必要な作業がまだ残っている。この分野のために氏が開発したもうひとつのツールが<a href="http://sysadvent.blogspot.pt/2013/12/day-13-controlling-cluster-of-servers.html">Serf</a>だ。 氏によれば，Serfは疎結合されたエージェントとゴシップ方式(Gossip-based)のメンバーシップ(新しいエージェントはシステムに参加するために，既存の１ノードにコンタクトしなければならない)によって，障害検出と回復をサポートするように設計されている。同様にエージェントが，障害が発生したノードを検出して，そのニュースを他のノードへ “ゴシップ” する場合もある。それによってノード交換の必要が判断されるのだ。
   <o:p></o:p></p> 
  <p class="MsoNormal">この方式の大きなメリットとして氏が挙げるのは，オーケストレーションの早さ，マシンイメージ生成時における構成管理プロセスの単純さ(Serfエージェントサービスだけを設定すれば，Serfがマシン起動時に自動的に立ち上がる)などの点だ。
   <o:p></o:p></p> 
  <p class="MsoNormal">氏はQ&amp;Aの間，Docker(アプリケーションコンテナ)やPacker(共通インフラストラクチャ)とSerf(サービスオーケストレーション)を同居させた場合でも問題がないことにも言及した。
   <o:p></o:p></p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
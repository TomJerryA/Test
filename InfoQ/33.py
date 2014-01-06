<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Xen Project，Mirage 0S 1.0をリリース</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/mirageos"><em>原文(投稿日：2013/12/23)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://blog.xen.org/index.php/2013/12/09/announcing-the-1-0-release-of-mirage-os/">Mirage OS</a>は &quot;クラウドオペレーティングシステム&quot; である。セキュリティ上の脆弱性回避と，単一目的の仮想アプライアンスの開発容易化による普及を目標とする。アプリケーションは関数型プログラム言語<a href="https://en.wikipedia.org/wiki/Ocaml">OCaml</a>で開発され，<a href="https://en.wikipedia.org/wiki/Xen">Xen</a> ハイパーバイザ上で直接動作するスタンドアロンの &quot;ユニカーネル&quot; にコンパイルされる。従来型のオペレーティングシステムを排除し，その構造を代替する言語ライブラリに置き換えることによって，従来よりコンパクトで高速に動作し，攻撃対象領域の少ないアプリケーションを実現する。開発したアプリケーションは，AmazonのEC2やRackspace Cloudのような，Xenベースのパブリッククラウドに直接デプロイすることも可能だ。</p> 
  <p>Mirage OSのアプローチはWebサーバやDNSサーバ，SDN (Software Defined Networking) などのインフラストラクチャソフトウェア開発者たちにアピールするかも知れない。コントリビュータであるケンブリッジ大学の <a href="http://anil.recoil.org/#!">Anil Madhavapeddy</a>氏は，次のようにコメントしている:</p> 
  <blockquote>
   Mirageは，OCamlに見られるような現代的モジュラプログラミング技術を用いて，特殊なインフラストラクチャアプリケーションを迅速に構築するという，私たちの夢を表現したものです。これまでに高レベル言語 (大部分はJavaとScala) で記述されたデータセンタツールは数多くありました。その底辺の部分に至るまで関数プログラミング技術を適用したならば，どのようなメリット(とデメリット！) があるのかを追求したいと思ったのです。
  </blockquote> 
  <p>システムは現在Xenハイパーバイザを対象としているが，Unixユーザ空間用のバイナリのビルドも可能だ。さらにプロジェクトには，FreeBSDカーネルモジュール用の試験的実装，NS3ネットワークシミュレータ，JavaScriptなどもある。Anil Madhavapeddy氏はさらに言う:</p> 
  <blockquote>
   VMWareやKVM, Hyper-Vといった他のハイパーバイザへの移植は，単純に適当なブートローダと仮想デバイスドライバを記述するだけの問題です。これはシステムプログラミングに足を踏み入れようという人にはうってつけのプロジェクトですので，私たちもメールリスト(mirageos-devel@lists.xenproject.org)を通じて，積極的に指導したいと思っています。
  </blockquote> 
  <p>Mirage OSが大きな可能性も持つ応用分野は，コンパクトでセキュアな &quot;ドメイン０&quot;，すなわちハイパーバイザの管理に使用される特別なドメインの提供だ。Anil Madhavapeddy氏は，これがMirage開発の背景となった大きな理由のひとつだとしている:</p> 
  <blockquote>
   XenServerディストリビューションではここ数年間，単一のモノシリックな &quot;ドメイン０&quot; の必要性を着実に排除しています。Mirageが提供するのは，そのパズルの最後のピース – これまでの管理ツールスタックを，標準的な分散システムプロトコルで相互に通信してコンセンサスを達成する，専門化したマイクロカーネルの集まりに転換するためのプログラミング環境なのです。これに伴って，セキュアなクラウドを構築する上で達成すべき水準は確実に高くなるでしょう。クラスタ内の仮想マシンに配置されたすてべのユーザデータのキーが，管理ツールスタックに保持されることになるからです。
  </blockquote> 
  <p>OCamlを選択した理由の質問に対して，同じくケンブリッジ大学のコントリビュータであるRichard Mortier氏は言う:</p> 
  <blockquote>
   理由はいくつかあります – 関数型言語としての実績，活発なコミュニティ，ランタイムへの移植が非常に効率的かつ比較的簡単，Xen管理スタックにOCamlで記述された部分がかなりある，強力なモジュールシステムによって効果的なモジュール化システムが実現可能，といったところでしょうか。
  </blockquote> 
  <p>TEE (Trusted Execution Environment) との関連性の有無についての質問には，Citrix XenServerシステムアーキテクトの<a href="http://dave.recoil.org/#!">David Scott</a>氏が次のような説明をしている:</p> 
  <blockquote>
   私にとってTE(Trusted Execution)には，(1) 意図したバイナリが実行中であることをどうやって確認するのか (2) 意図した動作をコードが行っていることをどうやって確認するのか，という２つの重要な側面があります。Measured Bootのようなテクニックは前者，つまり適切なバイナリの実行をチェックすることに注目しています。これに対してMirageは後者を，次のような方法で支援します。 
   <list> 
    <ul> 
     <li>必要なライブラリのみをリンクすることで，攻撃対象領域を最小化する。</li> 
     <li>コンフィギュレーションをどこか外部の(おそらくは変更可能な)ファイルシステムに置くのではなく，アプリケーションにリンクさせる。</li> 
     <li>メモリ破壊やバッファオーバーフロー攻撃といった類いの影響を受けないコード量を最大化する。</li> 
    </ul> 
   </list> 
  </blockquote> 
  <p>Mirage OSチームでは，組み込みアプリケーションや &quot;モノのインターネット(Internet of Things)&quot; といったユースケースも対象に含めている。Anil Madhavapeddy氏は，&quot;OCamlコンパイラ自体は，非常に小さなターゲット (<a href="http://www.algo-prog.info/ocaml_for_pic/web/">PIC18マイクロコントローラ</a>のような) にも容易に対応できる&quot;ものの，&quot;ビルドシステム関連で多くの作業が必要になる&quot; ことを指摘する。開発チームは先日の休暇を利用して，自分たちのWebページをMirage OSベースのサーバに移行した。その中には，バックエンドとしてRaspberry Piを使用したものもある。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>GlassFish Commercial Editionの提供が終了</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/glassfish-commercial-dead"><em>原文(投稿日：2013/11/07)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Oracleは先頃，<a href="https://blogs.oracle.com/theaquarium/entry/java_ee_and_glassfish_server">Java EEとGrassFish Servcerに関するロードマップの最新版</a>を発表した。2013年7月12日にリリースされたJava EE 7に合わせて，GlassFish Server Open Source Edition 4の提供が開始されたが，今週になってOracleは，Glass Fush 4の商用サポートバージョンを提供しないことを明言した。Java EE 7適合を実現したアプリケーションサーバとしてはTmaxSoftのJEUS 8があるが，リリースされるのは来年だ。したがってJava EE 7のリファレンス実装であるGlass Fish 4が，現時点では唯一のJava EE認証済アプリケーションサーバということになる。</p> 
  <p>OracleはGlassFish Server Open Source Editionについて，おもな目的がJava プラットフォーム Enterprise Editionの最新リリースを適用することであり，それは今後も変わることはない，と明言している。GlassFishの最新ロードマップは次のとおりだ。</p> 
  <ul> 
   <li>JavaOne 2013で発表されたように，GlassFish Server Open Source Edition 4.1のリリースが2014年に予定されている。</li> 
   <li>ソースのトランク(truck)は今後， GlassFish Server Open Source Edition 5に移行する。前回のリリースと同じステップを経由して，Java EE 8のリファレンス実装になる予定である。</li> 
   <li>Oracleは今後，商用サポート付きのGlassFishをリリースしない。GlassFish 4のCommercial Editionは提供されない予定である。</li> 
  </ul> 
  <p>既存のGlassFish 2および3のユーザに対するサポートは，Oracleの<a href="http://www.oracle.com/us/support/lifetime-support/index.html">ライフタイムサポートの方針</a>に従って継続される。GlassFish 2および3を新規購入したユーザには今後もサポートが行われるが，現行および将来のバージョンがサポートされない以上，これは強引な販売方法だろう。Java EE SDKには引き続きGlassFishがバンドルされるが，おもに開発者やコミュニティの要請によるものだ。コミュニティからのコントリビュートやバグ報告，およびGlassFishフォーラムへの参加は，今後も引き続き推奨される。</p> 
  <p>GlassFish 4に商用サポートを求めるユーザは，Oracle以外のサポートを探さなくてはならなくなる。OracleがJava 6のサポートを完了したとき，Red HatがOpenJDK 6を引き継いで，Java 6ユーザに対する事実上の拡張サポートを行った例がある。これを考えれば，Red HatがGlassFishのサポートを継続することもあり得るだろう。もうひとつの選択肢は，商用サポートのあるJava EEアプリケーションサーバに移行することだ。選択対象となりそうなJava EEサーバは多数存在する。Java EE認証を取得したアプリケーションサーバは，<a href="http://www.oracle.com/technetwork/java/javaee/overview/compatibility-jsp-136984.html">Java EE Compatibility</a>の一覧で確認することができる。その場合，アプリケーションが必要とするJava EEバージョンとプロファイルには注意しなくてはならない。商用サポートのあるオープンソース製品を引き続き使用したければ，まず思い浮かぶのはWildFlyとJBoss EAPだろう。この２つはコードベースは同じだが，ビルドの違うものだ。Oracleが推奨するのは，同社の商用サポート付きアプリケーションサーバであるWebLogicへの移行だ。必要な費用の詳細は，<a href="http://www.oracle.com/us/corporate/pricing/technology-price-list-070617.pdf">Oracle Technology Global Price List</a>で確認することができる。</p> 
  <p>Oracleは商用ライセンスでGlassFish Serverを使用しているユーザに，WebLogic Serverへの移行を開始するように勧めている。その理由は次のとおりだ。</p> 
  <ul> 
   <li>Java EE標準に従って開発されたアプリケーションは，GlassFish ServerにもOracle WebLogic Serverにもデプロイ可能である。</li> 
   <li>さらにGlassFish ServerとOracle WebLogic Serverには，実装依存のデプロイメントディスクリプタについても互換性がある。</li> 
   <li>GlassFish Server 3.xとOracle WebLogic Serverは相当量のコードを共有しているため，コンフィギュレーションや(拡張)機能に類似する点が多い。共有されるコードにはJPA, JAX-RS, WebSocket, CDI, Bean Validation, JSF, JAX-WS, JAXB, WS-ATなどが含まれる。</li> 
   <li>Oracle GlassFish Server 3.xとOracle WebLogic Server 12cは，いずれもOracle Access Manager, Oracle Coherence, Oracle Directory Server, Oracle Virtual Directory, Oracle Database, Oracle Enterprise Managerをサポートするとともに，その基盤であるOracle JDKのサポートも行うことができる立場にある。</li> 
  </ul> 
  <p>GlassFishからWebLogicへの置き換えであっても，アプリケーションサーバの変更であることに変わりはない。商用サポート版のGlassFishへの移行や，あるいはWildFlyからJBoss EAPへの移行に比べれば，詳細な計画や多くの労力が必要になる。開発作業についてはGlassFish上で継続して，その成果をWebLogicにデプロイして活用する方法も可能だ，とOracleは述べている。ただしこの方法ならば，JavaEE準拠のアプリケーションサーバ間のどれでも可能なことにも注意すべきだ。無償版のWebLogicサーバを開発用に直接使用する，という選択肢もあるだろう。</p> 
  <p>参考資料として，ソフトウェアアーキテクトのMarkus Eisele氏が &quot;<a href="http://blog.eisele.net/2013/11/rip-glassfish-thanks-for-all-fish.html">R.I.P. GlassFish - Thanks for all the fish</a>&quot; と題したブログ記事を書いている。GlashFishのサポートが完了したことについての，洞察力にあふれた解説資料だ。Oracleで製品マネージャの職にあるBruno Borges氏も &quot;<a href="https://blogs.oracle.com/brunoborges/entry/6_facts_about_glassfish_announcement">6 Facts About GlassFish Announcement</a>&quot; という記事を投稿して，今回の発表で想定される誤解について釈明している。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
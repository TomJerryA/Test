<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Oracleがjava EE 8計画について，さらにフィードバックを募集</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/ee8-survey-pt2"><em>原文(投稿日：2014/01/14)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>OracleはJava EE 8コミュニティサーベイの第２部をローンチした。クラウド，セキュリティ，ロギング，デプロイ，テスタビリティ，プルーニング，プロファイルといったトピックが対象だ。</p> 
  <p>&quot;過去５週間，第１部の調査に対するコミュニティの反応は，私たちにとって嬉しい驚きでした。&quot; David Delabassee氏はこのように<a href="https://blogs.oracle.com/theaquarium/entry/java_ee_8_community_survey">書いている</a>。&quot;貴重なフィードバックがたくさん寄せられてるのです！処理すべきデータが *たくさん* あるということは，まさに直面する価値のある課題ですね。&quot;</p> 
  <p>検討を要する重大な問題のひとつは，PaaSやSaaS, マルチテナンシなどのサポートを今の時点で標準化することは果たして妥当なのか，という点だ。この標準化は元々，Java EE 7の時に計画されていたのだが，後に見送られることになった作業だ。標準化を試みるにはあまりにも時期尚早だというのが，少なくともその理由のひとつだった。Linda DeMichiel氏は当時，次のように<a href="https://blogs.oracle.com/theaquarium/entry/java_ee_7_roadmap">書いている</a>。</p> 
  <blockquote> 
   <p>私たちは最善を尽くしていますが，開発予定のクラウドに関する部分の進行は捗々しくありません。理由のひとつはプロビジョニングやマルチテナンシ，柔軟性，クラウドへのアプリケーションのデプロイといった領域における完成度の不足です。保守的なアプローチを選択したことも原因のひとつです。作業に着手した時点で，私たちにはクラウド業界に関する経験が十分ありませんでした。そのような認識のもとで，すべてを &quot;正しく&quot; に行いたい，という意識が働いたのです。このような状況で，PaaS ベースのプログラミングとマルチテナンシの標準化サポートを確立して提供するには，Java EEのリリースを2014年の春 – 今から２年後まで，当初予定よりも１年ほど遅らせることになるでしょう。それでは遅すぎると思うのです。</p> 
  </blockquote> 
  <p>Oracleは現在，より多くのJavaコミュニティがこの問題に対して，再びチャレンジする価値を認めるかどうかに関心を持っている。</p> 
  <p>その他に検討中のアイデアとしては，ひとつのリクエストがシステム全体に与える影響をトレースするための標準APIというものがある。どのようなサービスを使っているのか，他にどのようなリクエストを起動しているのかを調べるためだ。さらにOracleでは，WebコンテナやJava EEコンテナの組み込みでサポートすることも検討している。セキュリティ面の提案としては，<a href="https://java.net/jira/browse/JAVAEE_SPEC-20">ロールマッピングのグループ</a>と<a href="https://java.net/jira/browse/JAVAEE_SPEC-29">EL式に対応した認証用アノテーション</a>の標準化，さらには<a href="https://java.net/jira/browse/JAVAEE_SPEC-28">簡易型セキュリティプロバイダの標準化</a>などがある。</p> 
  <p>Oracleはさらに，デプロイメントモデルの標準化に再度挑戦することも検討している。この問題に最初に取り組んだのがJava EE Aplication Deployment&nbsp;[JSR 88]だ。理屈の上では任意のJava EEアプリケーションを，同じツールを使って，任意のJava EE互換環境にデプロイ可能であるはずのものだ。しかしベンダによるサポートが十分ではなかったため，Java EE 6で廃止されることになった。</p> 
  <p>Java EE Management [JSR 77]もこれと同じように，管理ツールに対して，Java EE アプリケーションサーバに現在の状況やデプロイされているアプリケーションなどを問合せるためのAPIを提供する。これらのAPIを使えば，クロスベンダ形式で動作するサーバ管理ツールの構築が可能になる。システム管理者には，管理ツールやプロセスを変更ぜすにアプリケーションサーバを切り替えることや，あるいは異なるベンダのプラットフォーム実装で構成された複数のJava EEサーバによるネットワークを管理するための手段が提供されることになるだろう。JSR 88と同じように，このAPIもベンダのサポート不足に悩まされ，EE 7で一旦は放棄されたのだが，今回リストに復帰することになった。その他に破棄される可能性があるのは，EJB 2.xのリモートおよびローカルビュー (<em>EJBObject</em>, <em>EJBLocalObject</em>, <em>EJBHome</em>, <em>EJBLocalHome</em> といったインターフェース)とCORBAである。</p> 
  <p>今回の調査には28の質問項目がある。前回と同様それぞれの質問には，参加者が十分な技術情報の下で判断を下せるよう，関連する技術概念がバックグラウンドとして提供されている。調査については<a href="https://blogs.oracle.com/theaquarium/entry/java_ee_8_community_survey">こちら</a>で確認可能だ。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>JCACHEの仕様が完成</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/03/jcache-finalized"><em>原文(投稿日：2014/03/31)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Oracleは<a href="https://blogs.oracle.com/theaquarium/entry/jcache_is_final_i_repeat" target="_blank">今月</a>、<a href="https://jcp.org/en/jsr/detail?id=107" target="_blank">JCACHEの仕様</a>が完成したことを発表した。JSR-107は最古の仕様で、2001年の3月6日に起草された。13年に渡る進化と開発を経て、&quot;Java Temporary Caching API&quot;はJavaにキャッシュシステムとやり取りをする共通のAPIを提供する。</p> 
  <p>JCACHEが昨年のJava EE 7のリリースに含まれることに対してOracleに<a href="https://blogs.oracle.com/reza/entry/java_ee_7_survey_results" target="_blank">大きな関心</a>が寄せられていた。しかし、いくつかの&quot;致命的な納期&quot;を守れなかったことで<a href="https://blogs.oracle.com/theaquarium/entry/jcache_to_miss_java_ee" target="_blank">候補リストから外されてしまった</a>。Oracleが最近行った<a href="https://java.net/downloads/javaee-spec/JavaEE8_Community_Survey_Results.pdf" target="_blank">Java EE 8の調査</a>によれば、回答者の3分の2がJCACHEがJavaの次のEnterprise Editionに含まれることに関心を示している。今回の仕様完成の報を受け、Oracleはこのプロジェクトの<a href="https://github.com/jsr107/RI" target="_blank">参照実装</a>がJava EE 8を待つまでもなく、Java EE 6やJava EE 7のアプリケーションのドロップインとして使われいることを注記している。</p> 
  <p>JCACHEはキャッシュにアクセスするためのMapに似たAPIを提供する。また、キャッシュを永続化ディスクにスプールするためのAPI、名前付きキャッシュを検索するAPI、イベントリスナを登録するAPIを提供する。しかし、レプリケーションやトランザクションの仕様は提供しない。これらの機能を定義するのは<a href="https://jcp.org/en/jsr/detail?id=347" target="_blank">JSR-347 - JGRID</a>の一部はJCACHEはこのJGRIDの基盤となるコンポーネントのひとつだ。</p> 
  <p>InfoQはBen Cotton氏にJCACHEとJVMでのキャッシュ機構の将来について話を聞いた。氏はJSR-107とJSR-347の専門グループのメンバだ。</p> 
  <p>InfoQ: なぜJCACHEなのですか。</p> 
  <blockquote>
    JCACHEは、JDBCがJavaのRDBMSコミュニティに提供したものと同等のものを提供します。
   <br /> 
   <br /> JCACHEプログラマーがが透過的にデータを操作できるようにするための標準的なAPIをJavaに提供します。hibernateやJPA L2と連携するためのポイントも明確です。したがって、データのオペランドがデータベースのカラムであろうが、Map.Entryであろうが問題ありません。
  </blockquote> 
  <p>InfoQ: 今後の計画を教えてください。</p> 
  <blockquote>
    まず、トランザクションです。 
   <br /> 次にJGRID (JSR-347)との連携です。JCACHEは&quot;木&quot;であり、JGRIDは森です。
   <br /> そして、局所的なライブラリのデータオペランド(例えばPeterのOpenHFT SHM)との透過的なAPI連携ポイントです。
  </blockquote> 
  <p>オープソースの参照実装に加え、JSR-107の仕様は<a href="https://github.com/jsr107/jsr107spec" target="_blank">GitHubのページ</a>から自由に入手できる。課題やコメント履歴も閲覧できる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
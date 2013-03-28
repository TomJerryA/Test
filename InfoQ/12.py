<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Xtend 2.4 リリース - アクティブアノテーション，Androidサポートなどを新たに実装</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/xtend-24;jsessionid=C4A9062090E0A2B59ECD404B0E5610ED"><em>原文(投稿日：2013/03/20)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>Eclipse Foundationは先日，<a target="_blank" href="http://www.eclipse.org/xtend/">Xtend 2.4</a> のリリースを発表した。Xtendは静的型付けを持ったJava風プログラム言語である。記述されたコードはJavaにコンパイルされて，JVM (あるいはAndroidなどJVMライクなシステム) 上で動作する。</p> 
 <p>ScalaやKotlinといった他のJVMベースのコンパイル言語とは異なり，XtendはJavaコードに変換された後，標準的なJavaコンパイラでコンパイルされる。したがって生成されたコードに下位互換性の問題は存在しない。</p> 
 <p>さらにGroovyやJRuby/Jythonなどのインタプリタ言語とも異なり，静的型付けでありながら，シンプルなコード記述を可能にする型推測の機能を備えている。これによってリファクタリングや型に依存する補完機能がIDE上で実現されている。</p> 
 <p>InfoQでは昨年にも <a target="_blank" href="http://www.infoq.com/news/2012/06/xtend-release-10;jsessionid=AFA2C73BFBA4C2F3C048547092A3DCC2;jsessionid=C4A9062090E0A2B59ECD404B0E5610ED">1.0のリリース</a> を伝えているが，その後数多くの変更が行われている。今回リリースされた <a target="_blank" href="http://www.eclipse.org/xtend/release_notes_2_4_0.html">2.4の新機能</a> は，アクティブアノテーション，コレクションリテラル，Androidのサポート，リファクタリングの改善，ツーリングでのコンテントアシストなどだ。</p> 
 <p>InfoQはXtendのプロジェクトリーダであるSven Efftinge氏に連絡を取り，今回のリリースに関する詳細を聞くことにした。</p> 
 <p><b>InfoQ</b>: Xtend 2.4の新機能のひとつとして，アクティブアノテーションが追加されていますが，これがどのようなものなのか，どうやってボイラプレートコードを削減するのかを説明して頂けますか？</p> 
 <blockquote> 
  <p><b>Sven Efftinge</b>: 基本的にはアノテーションを記述することによって，その要素をどのようにJavaコード変換するのかをコンパイラに指示する，という方法です。典型的なユースケースはgetterとsetter，observer，visitorなど，一般的なデザインパターンの生成でしょう。ですが，他にもさまざまな使い道がありますから，アクティブアノテーションの開発や配布が手軽にできることを重視しています。</p> 
  <p>例として，JavaBeanパターンのプロパティを考えてみましょう。これにはget/setメソッドをペアで作る必要があります。いわゆる &quot;Javaコード肥大化&quot; に一役買うわけです。しかしXtendでは，フィールドがプロパティであると宣言するだけで，あとはXtendが処理してくれます。</p> 
  <pre>
@Property String name
</pre> 
  <p>これが次のようなJavaコードに変換されます。</p> 
  <pre>
private String name;
public String getName() {
  return this.name;
}
public void setName(String name) {
  this.name = name;
}
</pre> 
  <p>その他にも，<code>hashCode()</code> と <code>equals()</code> メソッドを自動生成する <code>@Data</code> や，<a target="_blank" href="http://www.eclipse.org/xtend/release_notes_2_4_0.html#active_annotations">リリースノート</a> でも紹介したように，データクラスに適用してプロパティ更新リスナのサポートを自動的に追加する <code>@Observable</code> などのアノテーションがあります。</p> 
  <p>この機能で一番クールなのは，IDEとコンパイラがコード変更を認識してくれることでしょう。タイピングやリンク時はもちろんのこと，ナビゲーションやコンテントアシストといった機能にも変更がオンザフライに反映されて，期待通りの動作をするのです。</p> 
  <p>コード生成機能はこうあるべきです。</p> 
 </blockquote> 
 <p><b>InfoQ</b>: もうひとつの新機能にリテラルコレクションがありますが，配列やセット，マップなどのリテラルはどのように記述するのでしょう？ネストは可能ですか？</p> 
 <blockquote> 
  <p><b>Sven Efftinge</b>: ハッシュに続けて中括弧かカギ括弧で記述します。リストの場合は，</p> 
  <pre>
val myList = #[1,2,3,4]
</pre> 
  <p>セットならば，次のように記述します。</p> 
  <pre>
val mySet = #{1,2,3}
</pre> 
  <p>マップはタプル演算子を使って生成します。</p> 
  <pre>
val mySet = #{1-&gt;&quot;one&quot;,2-&gt;&quot;two&quot; }
</pre> 
  <p>配列を記述すべき場所であれば，次のようにリストリテラルを配列リテラルとして使用することもできます。</p> 
  <pre>
val int[] myArray = #[1,2,3,4]
</pre> 
  <p>これらは通常の式ですので，ネストすることももちろん可能です。</p> 
 </blockquote> 
 <p><b>InfoQ</b>: リテラルコレクション型はミュータブル(mutable/可変)でしょうか，あるいはイミュータブル(immutable/不変)なのでしょうか？ミュータブルなコレクションをリテラルで初期化することは可能ですか？</p> 
 <blockquote> 
  <p><b>Sven Efftinge</b>: イミュータブルです。ミュータブルなインスタンスが必要な場合はファクトリメソッドを使用します。</p> 
  <pre>
val myArrayList = newArrayList(1,2,3,4)
</pre> 
  <p>既存のイミュータブルなリストからの生成も，もちろん可能です。</p> 
 </blockquote> 
 <p><b>InfoQ</b>: リテラルと言えば，エクステンションプロバイダとはどのようなものなのでしょう？エクステンションメソッドとはどう違うのでしょうか？</p> 
 <blockquote> 
  <p><b>Sven Efftinge</b>: エクステンションプロバイダは，プログラムのスコープ内でエクステンションメソッドを提供するオブジェクトです。例で説明するのが一番よいでしょう。<code>save(Entity)</code> というメソッドを持ったDAO(Data Access Object) を考えてみてください。</p> 
  <p>Javaでは次のような記述が必要です。</p> 
  <pre>
myDao.save(myEntity)
</pre> 
  <p>XtendならばDAOオブジェクトをエクステンションプロバイダにすることで，メソッドを最初のパラメータタイプのメンバメソッドとして使用できます。ですから次のように記述できるのです。</p> 
  <pre>
myEntity.save()
</pre> 
  <p>この機能は，C#のエクステンションメソッド (エクステンションとして使用できるのは静的メソッドに限られる) よりも大幅に拡張されています。 エクステンションプロバイダを使用することで，実装内容を簡単に入れ替えることができるのです。</p> 
 </blockquote> 
 <p><b>InfoQ</b>: JDK 8にはラムダ式をSAM(Single Access Method)型に変換するコンセプトがありますが，現在のXtendでJava 6やJava 7を使っても同じことが可能でしょうか？</p> 
 <blockquote> 
  <p><b>Sven Efftinfe</b> JDK8のラムダは，いわゆる関数インターフェースに変換されるだけのものですから，Xtendでも同じことが可能です。新しい機能は，SAM型とともに抽象クラスも使用可能になったことです。これは &quot;Functional Java&quot; などのフレームワークで多用されている方法です。</p> 
  <p>XtendならばJDK8を待たずとも，現行のJava 6やJava 7で同じことができますし，実際にはJava 5にも対応しています。</p> 
 </blockquote> 
 <p><b>InfoQ</b>: 下位互換性についてはどうでしょう？ Xtend 1.0でコンパイル可能だったプログラムは，今回のXtend 2.4でも使用できるのですか？</p> 
 <blockquote> 
  <p><b>Sven Efftinge</b>: バイナリ互換性がありますから，Xtend 1.0でコンパイルされたプログラムは，変更や再コンパイルをしなくてもXtend 2.4で動作します。</p> 
  <p>ソースレベルでも互換性を損なうような変更はありません。ただし，以前のバージョンでは警告されていなかった意味的エラーを強調するように，コンパイラのエラーメッセージなどは改良されています。</p> 
  <p>Xtendではコンパイル結果とソースの両方のレベルで，互換性を重視しているのです。</p> 
 </blockquote> 
 <p><b>InfoQ</b>: XtendのプロジェクトがAndroid用にコンパイル，インストールできるようになったのは，フレームワークとして大きな進歩だと思います。ところで，ScalaやKotlinを使ってAndroidアプリケーションをコンパイルすると，完成したパッケージが何メガバイトも大きくなります。Xtendでコンパイルしたアプリケーションは，Javaで直接コーディングした場合と比べて，平均的にどの程度のサイズ増加があるのでしょう？</p> 
 <blockquote> 
  <p><b>Sven Efftinge</b>: XtendはJavaのソースコードにコンパイルされて，それからJavaバイトコードにコンパイルされます。ですから，生成されたバイトコードはAndroidで確実に動作するものになります。さらにXtendでは，独自に巨大なライブラリを持つようなことをしていません。既存のJDKのクラスにエクステンションメソッドを追加するクラスがくつか(40K以下)と，1.3MというサイズのGoogle Guavaがあるだけです。</p> 
  <p>ですからXtendでは，非常に効率のよいAndroidアプリを開発することができるのです。</p> 
 </blockquote> 
 <p><b>InfoQ</b>: プログラム言語の成功指標のひとつに，IDEサポートが充実していることがあります。EclipseのXtendサポートはどの程度改良されているのでしょう？</p> 
 <blockquote> 
  <p><b>Sven Efftinge</b>: IDEにはフォーマッタや新しいクイックフィックス，新しいリファクタリング，コンテントアシストの大幅な改良など，さまざまな新機能があります。</p> 
  <p>コンパイラのパフォーマンスも大きく改善されました。 Xtendでは，IDEを使用した開発作業のワークフロー改善にも力を注いでいます。</p> 
  <p>他のJDMベース言語とは違って，XtendはJDTに対しても良好に動作します。JDTを置き換えたり，weavingを使用する必要はありません。さらに，プロジェクトのコンパイルには任意のバージョンのJavaコンパイラが使用可能です。プラグインとしてインストールされているバージョンに限定されません。</p> 
 </blockquote> 
 <p>Xtend 2.4の内容は 2.4リリースノート に記載されている。より詳細な情報については <a target="_blank" href="http://www.eclipse.org/xtend/">Xtend</a> のホームページを参照してほしい。</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
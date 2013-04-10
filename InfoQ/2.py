<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>GoogleとOperaがWebKitをフォーク，SamsungはFirefoxと共同でServoを推進</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/04/Google-Blink-Mozilla-Servo;jsessionid=E8D226605866F57D008378C1FE43754F"><em>原文(投稿日：2013/04/04)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>&nbsp;</p> 
 <p>２つの主要なブラウザ開発チームが先頃，パラレルアーキテクチャを目指すことを発表した。WebKit フォークの <a target="_blank" href="http://www.chromium.org/blink">Blink</a> を採用する Google と Opera，そして共同で <a target="_blank" href="https://github.com/mozilla/servo">Servo</a> をプッシュする Mozilla と Samsung だ。</p> 
 <p>６週間前に Opera は，独自のブラウザエンジンである Presto を放棄して <a target="_blank" href="http://www.infoq.com/jp/news/2013/02/Opera-WebKit-Presto;jsessionid=9E173F5EEFC7A3A414A50D2AF0E4780C;jsessionid=E8D226605866F57D008378C1FE43754F">WebKit を採用した</a>。多様性の減少による Web への影響を懸念する声もあったが，その心配はもはや必要ない。なぜなら Google が WebKit をフォークして <a target="_blank" href="http://www.chromium.org/blink">Blink</a> というブラウザエンジンコアを開発するからだ。Blink の開発は，その実装プラットフォームのひとつを提供することになる Chromium の開発と統合する形で行われる。<a target="_blank" href="http://www.brucelawson.co.uk/2013/hello-blink/">Opera も Google の Blink 開発に参加する</a> ことを，同社 Web エバンジェリストの Bruce Lawson 氏が発表している。</p> 
 <p>レンダリングエンジンとしては極めて大きな勢力であり，最も重要なエンジンになるチャンスもあったと思われる WebKit を，Google はなぜフォークするというのだろうか？ <a target="_blank" href="http://www.chromium.org/blink/developer-faq">Google の考え</a> はこうだ – &quot;開発者の生産性という面では，モノカルチャの方が望ましい。&quot; その一方で，長期的に見れば &quot;技術的停滞につながることは避けられない。&quot; つまり &quot;レンダリングエンジンの選択肢が多ければ，より多くの革新と，健全なWebエコシステムが実現できる&quot; はずだ。</p> 
 <p>WebKit のフォークに関して，Google はおもに２つの技術的理由があるという。</p> 
 <ul> 
  <li>Chrome は ”他の WebKit ベースのブラウザとは異なり，マルチプロセスアーキテクチャを採用している&quot;。そのため WebKit，Chrome ともに複雑さが増し，イノベーションに対して障害となっている。</li> 
  <li>Blink によって Google は，自分たちの望む方法でブラウザのパフォーマンスを改善することが可能になる。おもな方向性のひとつが並列処理である。</li> 
 </ul> 
 <p>要するに Google が望むのは，&quot;JavaScript において V8 が行ったのと同じことを，ネットワークやレンダリング，レイアウトでも実現します。V8 導入以前の JS を覚えているでしょうか。それと同じように，すべてのWebユーザ，すべてのブラウザに利益をもたらすような，健全なイノベーションを実現したいと思っています。&quot;</p> 
 <p>Google は自分たちの望む方向に進むための自由が欲しいのだろう。WebKit による開発上の制限を甘受するよりもむしろ，自分たちが多くのコントロールを所有している Chromium を強化する道を選んだのだ。開発者が Blink の <a target="_blank" href="http://dev.chromium.org/getting-involved/become-a-committer">コミッタ</a> あるいは <a target="_blank" href="http://dev.chromium.org/developers/owners-files">オーナ</a> になるためには，同社の定めるガイドラインに従う必要がある。</p> 
 <p>最初のステップは，WebKit から継承したコードの再構築だ。そのためには &quot;7つのビルドシステムと7,000以上のファイルを削除する必要があります。全体として，450万行以上に相当する量です。&quot; そして長期的には，次のようなイノベーションを Blink に導入したいと考えている。</p> 
 <ul> 
  <li><a target="_blank" href="http://www.chromium.org/developers/design-documents/oop-iframes">アウト・オブ・プロセス iFrame</a>。異なるページコンポーネントを別々のサンドボックスプロセスで実行可能にする。</li> 
  <li>より高速でシンプルなネットワーク処理。現在は &quot;変更不可能な古い Mac WebKit API の拘束によって&quot; 制限されている。</li> 
  <li>&quot;DOM (Document Object Model) をすべて JavaScript 内に&quot; 移動する。&quot;これにより，JavaScript のDOMアクセスが劇的に高速化する可能性があります。&quot;</li> 
 </ul> 
 <p>Google は他にも，次のような <a target="_blank" href="http://www.chromium.org/blink#new-features">改良の実施</a> を検討中だ。</p> 
 <blockquote> 
  <ul> 
   <li>マルチプロセスによる履歴アクセスのサポートを WebCore に追加 (現在は同じプロセスによる同期的な履歴アクセスを前提としている)</li> 
   <li>ウィジェットツリー (Mac WebKit1 の制約のひとつ) の削除</li> 
   <li>WebCore のモジュール分割</li> 
   <li>可能な部分については WebCore/プラットフォームではなく，サンドボックスプラットフォーム API を直接使用するようにコードを変更</li> 
   <li>２人のエンジニアが丸１日，フルタイムで稼働しなくても済むような，よりシンプルで厳格なツリーガーデニングシステムの確立</li> 
   <li>DOMをJSヒープへ移行する試み</li> 
   <li>マルチコアの活用拡大 (HTMLパーサ，スタイルエンジン，JavaScript パーサなど)</li> 
   <li>DOMのあいまいな部分の削除，あるいはパフォーマンス上のメリットや複雑性除去を目的とする，非後方互換の修正実施</li> 
   <li>Mac 版 Chrome で，現代的かつ高速な tcmalloc の全面的な採用</li> 
   <li>インクリメンタルおよびパラレルレイアウトの試行</li> 
   <li>JavaScript エンジンとして唯一サポートしている ScriptValue / ScriptState 抽象化の廃止によるメモリリークの修正</li> 
   <li>WebKitDL から WebIDL へのリプレースと，特別な JavaScript バインディングコードの削除</li> 
   <li>DOM3 イベント/[DOM] UI イベントの導入による WebCore の速度向上</li> 
  </ul> 
 </blockquote> 
 <p>新たなブラウザエンジンの登場は，Web 開発者たちに不安を抱かせている。彼らにとっては，自分たちのコードの正常動作を保証するブラウザがさらに増えることになるからだ。彼らの心配を解消するために Google は，Mozilla が Firefox で実装したものと同じような開発メカニズムを導入しようとしている。</p> 
 <blockquote> 
  <p>私たちの目標はイノベーションの促進と，互換性を備えたオープンなWebプラットフォームへの改善にあります。機能を際限なく追加して，他のブラウザとの互換性を損ねるようなことはありません。<a target="_blank" href="http://www.chromium.org/blink#new-features">新機能の追加</a> や <a target="_blank" href="http://www.chromium.org/blink#vendor-prefixes">ベンダプリフィックスの使用</a> には極めて開発者指向なポリシを導入すると同時に，<a target="_blank" href="http://www.chromium.org/blink#compatibility">リリースは必ず十分に安定したと認められた上で実施します</a>。</p> 
  <p>現在 Firefox は Gecko エンジンを使用しています。これは WebKit ベースではありませんが，２つのエンジンには非常に高い互換性があります。私たちも Mozilla と同じアプローチを適用することで，異なってはいても互換性を備えたオープンソースエンジンを実現したいと思っています。バグトラッキングと <a target="_blank" href="http://chromestatus.com/">実装状況</a> は今後も引き続きオープンにします。私たちの作業状況をいつでも見て，貢献して頂くことが可能です。</p> 
 </blockquote> 
 <p>特にベンダプレフィックスに関するポリシは重要だ。Google はそれらを新機能には使用しない意向のようなのだ。</p> 
 <blockquote> 
  <p>それに代わるものとして，試験的実装である DOM/CSS 機能を有効にする設定 (about:flag 内) を公開する予定です。<a target="_blank" href="https://plus.google.com/+GoogleChromeDevelopers/posts/ffDPaPAMkMZ">&quot;Experimental WebKit Features&quot; フラグ</a> で現在行っているのと同じように，その内容を見て，いろいろ試した上で，そのフィードバックを提供して頂ければと思います。これらの機能は，リリースが可能なまで安定したと見なされた時点で初めて，基本的には dev/canary チャンネルで提供されます。</p> 
  <p>旧来のベンダプレフィックス機能のために <code>-webkit-</code> プレフィックスも継続して使用します。これらのプレフィックスをすべて別のものに変更してしまうことは，開発者に不要な苦労をかけることになるからです。HTML5 と CSS3 の実際の使用頻度に関する調査も始めました。このようなデータが，プレフィックスのあるプロパティやAPIを，責任を持って廃止する方法の情報源となればと思っているのです。継承しているその他の非標準機能 (-webkit-box-reflect のような) については，標準化に向けて働きかけを行うか，あるいは廃止してしまうか，ケースバイケースで判断していきたいと思っています。</p> 
 </blockquote> 
 <p>Android を含むモバイル開発全般に関しては，Google は &quot;Webプラットフォーム全体が[新エンジンに]追随すると予想していますし，ある部分ではそれを期待しています。&quot;</p> 
 <p>Blink のもたらす副次的な影響のひとつとして，WebKit はおもに Apple の手中に残ることになる。Apple は他のブラウザと同じペースを保って，十分な速さで開発を進めることができるだろうか，注目したいところだ。</p> 
 <p>Google が Blink に関する発表を行う数時間前に Mozilla は，Samsung とのパートナーシップの下に <a target="_blank" href="https://github.com/mozilla/servo">Servo</a> の開発を推進すると <a target="_blank" href="http://blog.mozilla.org/blog/2013/04/03/mozilla-and-samsung-collaborate-on-next-generation-web-browser-engine/">発表した</a>。Servo は &quot;高速，マルチコア，異種混成という特徴を備えた明日のコンピュータアーキテクチャのメリットを活用する&quot; 試みとして，<a target="_blank" href="http://www.infoq.com/jp/news/2012/08/Interview-Rust;jsessionid=9E173F5EEFC7A3A414A50D2AF0E4780C;jsessionid=E8D226605866F57D008378C1FE43754F">Rust</a> 言語で開発された並列処理ブラウザプロジェクトである。Servo は，セキュリティメカニズムや大規模並列ハードウェアのサポートを含み，&quot;Web ブラウザを根本から再構築&quot; している。</p> 
 <p>その最初のステップでは Android/ARM 上での動作が実現される予定だ。現時点での Samsung のおもな貢献は，&quot;Rust 用の ARM バックエンドとしての役割と，Android 用のクロスコンパイルに必要なインフラの構築&quot; である。</p> 
 <p>今のところ Servo は，Mac OS X と Linux 64-bit で動作可能な，ブラウザエンジンのプロトタイプに過ぎない。今後はおそらく，使用している言語が成熟したものでないことによる影響を受けることになるだろう。同じ日に Mozilla は <a target="_blank" href="https://github.com/mozilla/rust/wiki/Doc-releases">Rust 0.6</a> を発表しているが，この言語が安定するには少なくともあと１年は必要だろう。それまでは &quot;Rust の最初のメジャーバージョン完成 – クリーンアップと拡張，ライブラリのドキュメント整備，ユーザエクスペリエンス改良のためのツール構築，パフォーマンス強化 – といった作業を急ぐ&quot; ことになる。</p> 
 <p>&nbsp;</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
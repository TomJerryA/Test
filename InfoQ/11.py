<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>アプリからクラウドへファイルをアップロードできるFilepicker</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/filepicker;jsessionid=E8AA61D8789F2BCDB111B714E036B2BA"><em>原文(投稿日：2013/03/20)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p><a target="_blank" href="https://www.filepicker.io/">Filepicker</a>はひとつのダイアログウィンドウを使って、Facebook、Dropbox、Instagram、Google Drive、Flickr、Skydrive、Evernote、Github、Picasa、Box、Alfresco、 Gmail、FTP、WebDAVからファイルをアップロードできる。アップロードされた画像は<a target="_blank" href="http://aws.amazon.com/s3/">Amazon Simple Storage Service (S3)</a>に保存され、アップロードが完了するとすぐにユニークなURLが生成される。</p> 
 <p>Filepickerはウェブ、<a target="_blank" href="http://www.apple.com/in/ios/">iOS</a>、<a target="_blank" href="http://www.android.com/">Android</a>、<a target="_blank" href="http://phonegap.com/">PhoneGap</a>をサポートし、画像をポストできる。画像はどのようなファイルタイプの画像がクラウドからアップロードされたかローカルデバイスからアップロードされたかにかかわらず正しいサイズになる。月5,000ファイルまでは無料で利用できる。メールとコミュニティによるサポートもある。<br /> <br /> InfoQは最高執行責任者であるFilepickerの<a target="_blank" href="https://twitter.com/ananddass">Anand Dass氏</a>に詳しい話を聞いた。<br /> <br /> <strong>InfoQ: Filepickerの本当の目的は何でしょう。</strong></p> 
 <blockquote>
  ウェブとモバイルのコンテンツの相互運用性は壊れています。Filepicker.ioの目的はこの問題を解決することです。例えば、モバイル生産性向上アプリを使って、メールアプリ内にあるPDFにアクセスしようとしたことはありますか。編集アプリでそのPDFを編集したら、自動的にDropbox、Google DriveへそのPDFが保存されたらどんなに楽でしょう。現在の携帯ではこのようなことは実現するのは難しいです。そしてこの例は問題の徴候のひとつに過ぎません。 
  <p>私たちの目的はコンテンツがどこにあれ、どんなデバイスを使っていても、どんなアプリを使っていても、コンテンツを取り出し、編集し、実行したいことをシームレスにできるようにするための、技術的基盤を構築することです。現在のバージョンはまだ限られたユースケースを満たす初期段階のサービスに過ぎません。</p> 
 </blockquote> 
 <p><strong>InfoQ: なぜFilepickerを開発したのですか。</strong></p> 
 <blockquote>
  ウェブとモバイルでの経験が壊れてしまっていることが原因です。どんなウェブサイトでもファイルや画像をアップロードする場合、私はまずFacebookかGoogle Driveからファイルをダウンロードしてローカルに保存し、そのファイルを対象のサイトにアップロードして、最後にディスクトップのコピーを削除します。 
  <p>現在のウェブアプリはユーザが扱いたいコンテンツはハードドライブにあるという前提を持っていますが、もはや正しくありません。携帯の場合はファイルをダウンロードする、アップロードするという考え方がありません。なので私も携帯ではアップロード、ダウンロードが上手くいかなかったのです。それでFilepicker.ioを作ろうと思い立ちました。</p> 
 </blockquote> 
 <p><strong>InfoQ: ユーザから見た場合、FilePickerを使う利点は何ですか。</strong></p> 
 <blockquote>
  これはエンドユーザ向けアプリケーションを開発しているモバイル、ウェブアプリケーション開発者のための製品です。なので、もし私たちが上手くやって開発者コミュニティをその気にさせたら、ユーザはコンテンツがどこにあるか、欲しくなったときどのように取得するかを気にしなくて済むようになります。
 </blockquote> 
 <p><strong>InfoQ: FilePickerはどのようなファイルをサポートしていますか。</strong></p> 
 <blockquote>
  カスタムのフォーマットを含めあらゆるフォーマットをサポートしています。文書、画像、音声、動画、フォトショップファイルをサポートします。モバイルアプリの勃興のおかげでファイルの概念が変わりつつあります。iOSのアプリは独自のデータコンテナを持っており、これらのデータはファイルの形式ではありません。近い将来、Filepicker.ioはファイル形式ではないコンテンツのデータ交換を実現するつもりです。
 </blockquote> 
 <p><strong>InfoQ: FilePickerとアプリを統合するのはどのくらい簡単ですか。</strong></p> 
 <blockquote>
  コード2行で済みます。
  <a target="_blank" href="http://developers.filepicker.io">JavaScriptライブラリ</a>を追加してタグを
  <em>&lt;input type=filepicker&gt;</em>に変更すれば完了です。単純なウェブアプリケーションなら10分で済みます。iOSとAndroidの場合はもう少しかかりますが、30分程度で統合が完了したという顧客のツイートがありました。
 </blockquote> 
 <p><strong>InfoQ:Filepickerはモバイルとタブレットデバイスをサポートしますか。</strong></p> 
 <blockquote>
  はい。iOS、Android、モバイルウェブ、PhoneGapをサポートします。私たちが受け取ったフィードバックの中で最も協力だったのは、モバイルユーザからのものでした。彼らは今、アプリケーションから直接クラウドのファイルを開いたり保存したりできています。これは他の方法では実現できないことです。 
  <p>プロダクト＆ユーザエクスペリエンス部門のトップであるLiyan Changが<a target="_blank" href="http://vimeo.com/45436417">Filepicker iOS</a>ライブラリの使い方の動画デモを作りました。</p> 
 </blockquote> 
 <p><strong>InfoQ: 無料版とプレミアムサービスの違いを教えてください。</strong></p> 
 <blockquote>
  月に扱えるファイル数だけです。月5000ファイルまでは無料です。もっと使いたい場合は有償版(月額99ドル)を使う必要があります。私たちはどんな開発者にも最高のエクスペリエンスを提供できると信じています。なので、これ以外の特徴でプランを別けることはしません。企業顧客向けにはスループット、SLA、使用可能時間の要件に応じてカスタマイズしたプランを提供します。
  <strong> </strong>
 </blockquote> 
 <p><strong>InfoQ:Windows Phone 8はサポートしますか。</strong></p> 
 <blockquote>
  はい。現在、Windows Phoneをサポートすべく鋭意開発中です。今年の後半くらいには何らかの発表ができると思います。
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
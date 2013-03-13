<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>期限切れのSSL証明書で AzureとTFSがダウン</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/03/feb22_azure_outage;jsessionid=DA5A16A9A6F4A4E31FBA87C7AF00F66D"><em>原文(投稿日：2013/03/05)へのリンク</em></a></p> 
<div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p style="margin-bottom: 0in" class="western"><span lang="en-US">Windows Azureストレージのユーザーは2月22日に長い動作不能を経験した。Team Foundation Service（TFS）は、バックエンド・ストレージを提供するのに、Azureに依存しており、その結果<a class="western" target="_blank" href="http://blogs.msdn.com/b/bharry/archive/2013/02/23/bad-day.aspx">9時間の動作停止</a>を経験した。 この停止は、HTTPSトラフィックを保護し、認証するために使用されている、<a class="western" target="_blank" href="http://en.wikipedia.org/wiki/SSL_certificate">SSL 証明書</a>の期限切れによるものだった。鍵証明書の有効期間が切れたので、影響を受けるサーバーとのHTTPSでの通信が失敗し始めた。HTTP通信は、いくつかのケースでは動作可能であったが、定義により、それは安全ではなく、平文での通信を許容できる顧客にのみ使えた。</span></p> 
 <p style="margin-bottom: 0in" class="western">公式には、停止は２月２２日の 12:29 PSTに始まり、HTTPSを使って、Windows Azure ストレージにアクセスしている全地域の顧客に影響した。世界中の全顧客が再び使えるようになったのは、２月２３日の 00:09 AM PSTだった。</p> 
 <p style="margin-bottom: 0in" class="western">Microsoftの Mike Neil氏、Windows Azureのジェネラルマネージャが故障の<a class="western" target="_blank" href="http://blogs.msdn.com/b/windowsazure/archive/2013/03/01/details-of-the-february-22nd-2013-windows-azure-storage-disruption.aspx">詳細</a> を提供した。AzureはSSLを使って、サービス全体のトラフィック、特に３つの主要なストレージタイプのブロブ、キュー、テーブル間のトラフィックを守っている。今回のケースで、停止が始まったのは、これらの領域の証明書が期限切れを起こし始めた時である。</p> 
 <blockquote> 
  <ul> 
   <li>*.blob.core.windows.net が２月２２日金曜日12:29:53 PM PST</li> 
   <li>*.queue.core.windows.net が２月２２日金曜日12:31:22 PM PST</li> 
   <li>*.table.core.windows.net が２月２２日金曜日12:32:52 PM PST</li> 
  </ul> 
 </blockquote> 
 <p style="margin-bottom: 0in" class="western">氏は更に、いかにAzureシステムで使用されているSSL証明書を監視し、更新する自動化されたプロセスが動作不能になったかを説明した。監視システムは、適切なスタッフに更新された証明書が必要であることを通知した。次にこれらは、通常のシステム更新で作成され、パッケージ化された。不幸にして、この更新には、時間に注意の要るコンポーネントが存在する、というラベルがされていなかったので、優先順位が低く、他の更新を優先させた。</p> 
 <p style="margin-bottom: 0in" class="western">新しい証明書が作成され、監視サービスで更新マークが付いていたので、これ以上のアップデートの通知は送信されなかった。したがって、新しい証明書は更新キューとマスタ証明書リポジトリで萎んでしまいが、本番Azure環境に行くことはなかった。</p> 
 <p style="margin-bottom: 0in" class="western">デプロイ用に修正パッチが作成され、22:45 PST までには、HTTPSサービスが大多数の顧客に回復し、完全なサービス回復宣言は、２月２３日 00:09 PSTだった。停止の結果、影響を受けた顧客は、２５％のサービスクレジット受け取る。自動証明書監視プロセスは、更新されたので、証明書はエンドポイントで監視され、失敗した/遅延したデプロイが見逃されることは、ないだろう。</p> 
 <p style="margin-bottom: 0in" class="western">Harryは、大規模のオンラインシステムを稼働させ、維持することは複雑である、と注意した。</p> 
 <blockquote> 
  <p style="margin-bottom: 0in" class="western">もちろん、大規模なミッションクリティカルなサービスを運営指定て、直ぐに学ぶことの１つが、あらゆるものが動いている、と仮定できないことです。この事で難しいのは、なんでも悪くなり得ることで、あなたが何に対して守るはずだったかは、結果論でしか明らかにならないことです。なのであらゆる可能性から守ろうとしなければなりません。</p> 
 </blockquote> 
 <p style="margin-bottom: 0in" class="western">Neilは、元のAzureシステムは単一点障害を患った、と見ている。</p> 
 <blockquote> 
  <p style="margin-bottom: 0in" class="western">「証明書の有効期限が顧客への直接的影響を引き起こしましたが、これらの証明書を維持そして監視する我々の手続きにおける瓦解が根本原因です。更に、証明書はどこでも同じであり、時間的にお互いに近かったので、それらはストレージシステムの単一点障害でした。」</p> 
 </blockquote> 
 <p style="margin-bottom: 0in" class="western">この機能停止に対するユーザーのコメントは、停止の深刻さと信頼出来るシステムの必要性を指摘した。ユーザー“trievangelist”は、停止している間、彼のとったNuGetの回避策について述べている。</p> 
 <blockquote> 
  <p style="margin-bottom: 0in" class="western"><i>trievangelist２月２３日午前６：４９#</i></p> 
  <p style="margin-bottom: 0in" class="western"><i>Brian,これを掲示してくれてありがとう。問題が起きたのは、我々がビルドプロセスの時で、これはNuGetを使い、問題が起き始めていた nuget.orgから nuget.exeの最新版をダウンロードすることに依存しています。ありがたいことに、我々は内部のNuGetギャラリーを使用していたので、私はnuget.exeのローカルバージョンを使用することで問題を回避することができました。 </i></p> 
 </blockquote> 
 <p style="margin-bottom: 0in" class="western">ユーザーの Keith Richardson氏はこの停止を使って、なぜ彼の会社がクラウドにシステムを移行するのに興味が無いかを説明した。</p> 
 <blockquote> 
  <p style="margin-bottom: 0in" class="western"><i>Keith Richardson ２月２３日午前８：４４#</i></p> 
  <p style="margin-bottom: 0in" class="western"><i>これは、我々がクラウドに移行しない、もう１つの理由です。あなた方には、６，７ヶ月おきに必ず、何らかの機能停止があるようです。もしこれが内部で起きたら、我々は誰か、あるいはベンダーを首にするでしょう。こんな言い方では足りません。誰かを「クビにする」。</i></p> 
 </blockquote> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
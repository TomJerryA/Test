<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>OpenAccess ORMがTelerik Data Accessに名称変更，改良UIとカラーのビジュアルデザイナを追加</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/02/telerik-data-access"><em>原文(投稿日：2014/02/18)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>OpenAccess ORMは先日，<a href="http://www.telerik.com/data-access">Telerik Data Access</a>と名称を変更した。リレーショナルのバックエンドを備えた，デザインタイムおよびランタイムインタラクションAPIである。2014年第１四半期のリリースには，アップグレードされたユーザインターフェースの他にウィザードが追加され，新しいロゴが与えられる予定だ。さらにビジュアルデザイナが緑色で表示されるようになり，Telerik.DataAccess.Core, Telerik.DataAccess.Fluent, Telerik.DataAccess.Fluent.SampleなどのNuGetパッケージが同梱される。</p> 
  <p>永続エンティティ定義を追加せずにデータ層を参照したいプロジェクトにはCoreパッケージが便利だろう。一方のFluentパッケージは，フルーエントマッピング(Fluent Mapping)のデータ層に適している。ただし従来のOpenAccessパッケージは廃止され，上記NuGetパッケージで置き換えられているので注意が必要だ。</p> 
  <p><a href="https://www.nuget.org/packages/Telerik.DataAccess.Core/">Telerik.DataAccess.Core</a> NuGetパッケージには，マッピング定義なしで永続的オブジェクトを使用するランタイムアセンブリが含まれている。パッケージマネージャを使うことでインストール可能だ。もうひとつのNuGetパッケージである<a href="https://www.nuget.org/packages/Telerik.DataAccess.Fluent/">Telerik.DataAccess.Fluent</a>は，コードファーストなフルーエントマッピングを使用したデータアクセスモデルの定義に利用できる。Telerik Data Access Enhancerツールがビルド実行中に生成したアセンブリリファレンスも含まれている。Telerik Data Accessのランタイムに必要な情報だ。</p> 
  <p><a href="https://www.nuget.org/packages/Telerik.DataAccess.Fluent.Sample/">Telerik.DataAccess.Fluent.Sample</a>パッケージには，Telerik DataAccessのフルーエントマッピングサポートの使用方法を確認するためのサンプルソリューションが含まれている。パッケージマネージャの&quot;Install-Package Telerik.DataAccess.Fluent.Sample&quot;というコマンドでインストールできる。</p> 
  <p>公式資料によれば，パッケージの切り替えによるAPIあるいはアセンブリ名称の変更はない。従ってOpenAccessContextやTelerik.OpenAccessアセンブリについても，従来と同じく利用することができる。</p> 
  <p>InfoQはTelerik Data AccessのチームリーダであるIvailo Ivanov氏にコンタクトを取り，最新の開発状況について詳細に聞いた。氏がくれた回答は次のようなものだ。</p> 
  <blockquote>
   この製品は当初，人気の高いNHibernateやEntity Frameworkの代替手段を提供するORMプロダクトとして設計されました。しかしながら年月を経て成熟すると同時に，それ以上のもの – データアクセスフレームワークに発展して，オブジェクト-リレーショナルマッピングはその一機能に過ぎなくなったのです。
   <br /> 
   <br /> 現在では低レベルのADO API，実行時に定義されたデータタイプを扱う機能，Webサービスの生成，バルク操作など，一般的なORM製品には見られない機能を数多く備えています。そこで私たちは，製品の成り立ちや目標をよりよく表すために，Telerik Data Accessに名称変更することを決定しました。
   <br /> 
   <br /> ブランド名を変えるにあたって，私たちが念頭に置いたことがひとつあります - マーケティング上の変更が，クライアントにコード変更を強いるようなことがあってはならない，という点です。そのために私たちは，互換性を損なうような変更の導入を回避しました – APIやアセンブリ名は変更されていません。唯一変更されたのは，NuGetにおける名称です。しかしそれについても，標準的なアップグレード手順が相違点を自動的に解決してくれているはずです。
  </blockquote> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
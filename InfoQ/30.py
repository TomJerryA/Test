<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>TypedMVVM - WinJS Windows StoreアプリをTypeScriptを使って開発</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/typedmvvm"><em>原文(投稿日：2013/12/10)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://typedmvvm.codeplex.com/">TypedMVVM</a>はDavide Zordan氏の開発した，WinJSや<a href="http://www.typescriptlang.org/">TypeScript</a>, <a href="http://en.wikipedia.org/wiki/Model_View_ViewModel">MVVM</a>を使用してWindows Storeアプリを記述するためのサンプルとライブラリのコレクションだ。<a href="http://msdn.microsoft.com/en-us/library/windows/apps/br229773.aspx">WinJS</a>で開発されたシンプルなWindows StoreナビゲーションアプリのMVVMパターンを通じて，関心事の分離を適用することにより，実世界のシナリオにおけるTypeScriptの使用を可能にする。</p> 
  <p>氏の説明によれば，すべての .jsソースファイルが，クラス/インターフェース実装を備えた新たなフォルダ構造のTypeScriptに変換されている。designDataがデザインタイムのデータの実装を提供してブレンダビリティ(Blendability, 混合性)を担保する一方で，ライブラリにはTypeScript定義やRelayCommand&lt;T&gt;やViewModelBaseといったTypedMVVMコアクラスが格納されている。パッケージにはサービスやビューモデル，ビューモデルファクトリ用のインターフェース，さらにビューモデルの具象クラスやビュー定義なども含まれる。</p> 
  <p>InfoQではMicrosoft MVPであるソフトウェアアーキテクト兼開発者の氏にコンタクトを取り，TypedMVVMについて詳しく聞いた。<br /> <br /> <strong>InfoQ: TypedMVVMを開発した背景について説明して頂けますか？</strong></p> 
  <blockquote>
   私は構造化された方法でコードを書くのが好きで，&quot;関心事の分離&quot; やオブジェクト指向，モジュール化，テスト容易性，拡張性といったベストプラクティスを受け入れたいと思っています。
   <br /> 
   <br /> TypeScriptは開発者に対して，プロフェッショナルなアプリケーションを開発する上で基本的なものだと私が考える機能を，数多く提供してくれます。特に，型のチェックと推論リファクタリング，インテリセンスの完全サポートといった機能は，複雑で大規模なアプリケーションを開発する場合には必須のものです。このような理由から私は，TypeScriptを使用して，MVVMデザインパターンをWinJSナビゲーションアプリに適用する方法を示すような，シンプルなクラスセットを開発しようと思いました。
  </blockquote> 
  <p><strong>InfoQ: TypedMVVMを使わずに開発されたWindows Storeアプリとは，どのような違いがあるのでしょう？</strong></p> 
  <blockquote>
   WinJSで開発された通常のWindows Storeアプリでは，コア言語としてJavaScriptを使用します。TypedMVVMでコア言語として使用するのはTypeScriptです。TypeScriptは静的型付け，インターフェース，クラス(ほんの数個ですが)を備えていますが，最終的にはプレーンなJavaScriptにコンパイルされます。その他には，ViewModelパターンを初めて使う開発者が，適切な構成とテスト性を備えたコードを記述できるようにするためのヘルパクラスがいくつか含まれています。
  </blockquote> 
  <p><strong>InfoQ: TypedMVVMを使用すると，どのようなタイプのアプリケーションが開発可能なのですか？</strong></p> 
  <blockquote>
   当面のターゲットは，WinJSフレームワークを使用したWindows Storeアプリです。
  </blockquote> 
  <p><strong>InfoQ: TypedMVVMを実装した実際のアプリケーションとして，何かご存じのものはありますか？</strong></p> 
  <blockquote>
   リリースされたばかりですので，現時点では，実際のプロジェクトに関する情報はありません。
   <br type="_moz" /> 
  </blockquote> 
  <p><strong>InfoQ: 今後のロードマップについて教えてください。</strong></p> 
  <blockquote>
   ロードマップはまだ作成中ですが，制御の逆転(inversion of control)や疎結合メッセージング，アプリケーション固有サービスといったものを考えています。これらは本当に有効なものになるでしょう。
   <br type="_moz" /> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
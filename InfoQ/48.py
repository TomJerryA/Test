<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>DevExpress ASP.NETグリッドコントロールがバッチ編集機能を導入</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/devpress-grid-batch-edit"><em>原文(投稿日：2013/12/18)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>DevExpress ASP.NETの最新リリースである13.2エディションに含まれているGridコントロール(<a href="http://demos.devexpress.com/ASPxGridViewDemos/Default.aspx">ASPxGridView</a>)では，ASP.NETおよびMVC開発者がクライアント上でグリッドデータをバッチ修正して，単一のリクエストとしてサーバに送信することが可能だ。エンドユーザは，マウスを使わずにキーボードだけでレコードを編集することができる。</p> 
  <p>ASPxGridViewコントロールがアップデートされて，レコードの変更をサーバに送信する前に，エンドユーザがプレビューできるようになった。さらに，編集されたセルの表示色を選択することも可能だ。</p> 
  <p>GridViewコントロールから<a href="http://demos.devexpress.com/ASPxGridViewDemos/GridEditing/BatchEditing.aspx">バッチ編集</a>ステージで実行されるアクションに関して，ユーザが有用な通知を受けることも可能になった。例えばセルの値を選択した後でカラムをソートしようとすると，次のようなメッセージが表示される。</p> 
  <p><img src="http://www.infoq.com/resource/news/2014/01/devpress-grid-batch-edit/ja/resources/Figure_1_GridView.png" alt="" _href="img://Figure_1_GridView.png" _p="true" /></p> 
  <p>バッチ編集機能を有効にするためには，ModeプロパティをBatchに設定する必要がある。それにより，インラインエディタでデータの編集が可能になる。編集されたセルは緑色で表示される。バッチ編集を有効にすると， “Save changes” リンクがクリックされるまで，すべての編集はクライアント側で保持される。“Cancel changes” リンクを選択することで，すべての変更をキャンセルすることも可能だ。</p> 
  <p>InfoQではDevExpressのソフトウェア開発者であるMehul Harry氏に，ASPxGridViewコントロールに関する詳細な情報を聞いた。</p> 
  <p><strong>InfoQ: GridViewのバッチ編集によるメリットを教えてください。</strong></p> 
  <blockquote>
    GridViewのBatchEditには次のような利点があります。 
   <ul> 
    <li>BatchEditでは，DevExpress ASPxGridViewのレコードをキーボード操作のみで編集することができます。マウスに手を伸ばす必要がありませんので，これは時間の節約になります。</li> 
    <li>編集や挿入が完了すれば，すべての編集を一度に確認することができます。</li> 
    <li>変更内容のキャンセルや保存がひとつの操作で可能です。</li> 
   </ul> 
  </blockquote> 
  <p><strong>InfoQ: バッチ編集機能はタッチ操作に対応していますか？</strong></p> 
  <blockquote>
   はい，DevExpress ASP.NETコントロールは
   <a href="https://www.devexpress.com/products/net/controls/touch.xml">タッチ</a>をサポートします。実際に私たちは，タッチデバイスとデスクトップブラウザのどちらにもマッチする
   <a href="https://community.devexpress.com/blogs/aspnet/archive/2013/11/13/asp-net-moderno-theme-what-39-s-new-in-13-2.aspx">テーマ</a>を用意しています。
  </blockquote> 
  <p><strong>InfoQ: バッチ編集が有効なシナリオをいくつか紹介して頂けますか？</strong></p> 
  <blockquote>
   バッチ編集は，複数の編集データを持っていて，それらの編集がすべて完了するまでデータベースへのアップロードやコミットを行いたくない，そういった要求を持つユーザに最適です。
   <br type="_moz" /> 
  </blockquote>
 </div> 
</div><br><br><br><br><br><br></body></html>
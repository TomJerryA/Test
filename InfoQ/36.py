<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ASP.NET Identity Preview 2.0でAccount Confirmation,Password Reset,Security Token Providerの機能をサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/12/asp-net-identity-preview-2"><em>原文(投稿日：2013/12/24)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="http://blogs.msdn.com/b/webdev/archive/2013/12/20/announcing-preview-of-microsoft-aspnet-identity-2-0-0-alpha1.aspx">Microsoft</a> は <a href="https://aspnetidentity.codeplex.com/">ASP.NET Identity Preview</a> をリリースし、バグフィックスに加えて Account Confirmation, Password Reset, Security Token Provider, UsersStore と RolesStore での IQueryable をサポートした。<br /> <br /> Account Confirmation 機能では、ユーザ情報をサイトに登録した後、SMTP や <a href="http://sendgrid.com/windowsazure.html">SendGrid</a> を利用してユーザにメールを送付し、リンクをクリックすることでアカウントをアクティブ化する機能を実現できる。また、Password Reset 機能を利用することで、パスワードを忘れた際に自身のパスワードを初期化するのが簡単になった。</p> 
  <p>Security Token Provider 機能を利用することで、パスワード変更時やFacebook, Google, Microsoft Account 等のソーシャルメディアのハンドルを削除した場合にトークンを再生成する方法を提供する。</p> 
  <p>開発コミュニティのフィードバックにより、Microsoft はユーザやロールのテーブルに対し、Primary Key(PK)を指定することが可能な拡張ポイントを提供した。更に、以前のバージョンではできなかった UserManager を介したユーザの削除が可能になる。最新のリリースでは、UserManagerFactory と DbContextFactory でもサポートする。</p> 
  <p>上記の機能に加え、Microsoft は IdentityUser クラスに Email と IsConfirmed 二つのプロパティを追加した。同プロパティを利用して、ASP.NET Identity 2.0 で生成したスキーマの変更結果を取得することができる。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
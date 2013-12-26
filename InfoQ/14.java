<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ASP.NET Identity Preview 2.0 Adds Account Confirmation, Password Reset and Security Token Provider</h3><p><a href="http://blogs.msdn.com/b/webdev/archive/2013/12/20/announcing-preview-of-microsoft-aspnet-identity-2-0-0-alpha1.aspx">Microsoft</a> has released <a href="https://aspnetidentity.codeplex.com/">ASP.NET Identity Preview</a> with support for account confirmation, password reset, security token provider, IQueryable on UsersStore and RolesStore in addition to bug fixes. <br /> <br /> The account confirmation feature works by sending an email via SMTP or third party services such as <a href="http://sendgrid.com/windowsazure.html">SendGrid</a> to users as soon as they register on the site and they will be required to activate the account by clicking on the link. On the other hand, password reset feature enables users to easily reset passwords if they forget their original password.</p>
<p>The security token provider provides a way to regenerate the token for the user in cases when the user changes password or any other security related information such as removing an associated social media handle such as Facebook, Google or Microsoft Account.</p>
<p>Based on the feedback from the developer community, Microsoft has provided an extensibility hook where you can specify what should be the primary key (PK) of your users and roles table. Moreover, it is also possible to delete a user through UserManager, which was not possible in the previous release. The latest release also provides support for UserManagerFactory and DbContextFactory middlewares.</p>
<p>In addition to the above features, Microsoft has added two new properties to the IdentityUser class such as Email and IsConfirmed, which results in a change of the schema created by the ASP.NET Identity system in 2.0.</p><br><br><br><br><br><br></body></html>
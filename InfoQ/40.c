<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ASP.NET MVC 5: Melhorias de autenticação com filtros</h3><p>O <a href="http://www.asp.net/mvc/tutorials/mvc-5/introduction/getting-started">ASP</a><a href="http://www.asp.net/mvc/tutorials/mvc-5/introduction/getting-started">.NET MVC 5</a> inclu&iacute;do no recente lan&ccedil;amento do <a href="http://www.microsoft.com/visualstudio/eng#2013-downloads">V</a><a href="http://www.microsoft.com/visualstudio/eng#2013-downloads">isual Studio 2013 Developer Preview</a>, permite que os desenvolvedores apliquem filtros de autentica&ccedil;&atilde;o capazes de autenticar usu&aacute;rios utilizando diversos controles de terceiros ou um controle de autentica&ccedil;&atilde;o customizado. Entretanto, estes filtros s&atilde;o aplicados antes das chamadas feitas aos filtros de autoriza&ccedil;&atilde;o.</p>
<p>Para gerar um filtro de autentica&ccedil;&atilde;o, &eacute; preciso criar um novo projeto C# ASP.NET, selecionando o tipo MVC na lista de projetos apresentados. Eric Vogel, Desenvolvedor de Software S&ecirc;nior da Kunz, Leigh &amp; Associates, investigou o uso dos filtros de autentica&ccedil;&atilde;o atrav&eacute;s de um filtro personalizado, que faz o redirecionamento dos usu&aacute;rios de volta &agrave; p&aacute;gina de login caso estes n&atilde;o sejam autenticados.</p>
<p>Vogel criou um diret&oacute;rio chamado CustomAttributes e uma nova classe chamada <strong>BasicAuthAttribute,</strong> que herda de ActionFilterAttribute e IAuthenticationFilter</p>
<pre>
public class BasicAuthAttribute: ActionFilterAttribute, IAuthenticationFilter
</pre>
<p>Embora o m&eacute;todo OnAuthentication() presente na interface <a href="http://stackoverflow.com/questions/15877029/iauthenticationfilter-interface-implementation-in-asp-net-mvc">I</a><a href="http://stackoverflow.com/questions/15877029/iauthenticationfilter-interface-implementation-in-asp-net-mvc">AuthenticationFilter</a> possa ser usado para executar qualquer autentica&ccedil;&atilde;o necess&aacute;ria, o m&eacute;todo OnAuthenticationChallenge() &eacute; usado para restringir o acesso baseado no papel do usu&aacute;rio autenticado.</p>
<p>O m&eacute;todo OnAuthenticationChallenge() recebe um argumento AuthenticationChallengeContext, e sua implementa&ccedil;&atilde;o se parece com a demonstrada logo a seguir:</p>
<pre>
public void OnAuthenticationChallenge(AuthenticationChallengeContext filterContext)
{
  var user = filterContext.HttpContext.User;
  if (user == null || !user.Identity.IsAuthenticated)
  {
    filterContext.Result = new HttpUnauthorizedResult();
  }
}
</pre>
<p>O c&oacute;digo completo est&aacute; dispon&iacute;vel no <a href="http://visualstudiomagazine.com/articles/2013/08/28/asp_net-authentication-filters.aspx">p</a><a href="http://visualstudiomagazine.com/articles/2013/08/28/asp_net-authentication-filters.aspx">ost</a> de Vogel em seu blog. A classe BasicAuthAttribute pode ser facilmente testada na classe HomeController, abrindo o arquivo e adicionando a seguinte linha de c&oacute;digo:</p>
<pre>
using VSMMvc5AuthFilterDemo.CustomAttributes;
</pre>
<p>Por fim, aplica-se o atributo customizado &agrave; classe HomeController, como mostrado a seguir:</p>
<pre>
[BasicAuthAttribute]
public class HomeController : Controller
</pre><br><br><br><br><br><br></body></html>
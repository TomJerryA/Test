<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Microsoft atualiza .NET Framework 4.5</h3><p>A Microsoft lan&ccedil;ou v&aacute;rias atualiza&ccedil;&otilde;es para o <a href="http://support.microsoft.com/kb/2750149">.NET Framework 4.5</a>, que corrigem problemas de compatibilidade, confiabilidade, estabilidade e desempenho, no <a href="http://msdn.microsoft.com/en-us/library/ms754130.aspx">Windows Presentation Foundation</a>, <a href="http://www.techopedia.com/definition/5225/common-language-runtime-clr">Common Language Runtime</a>, <a href="http://msdn.microsoft.com/en-us/library/dd30h2yb.aspx">Windows Forms</a>, <a href="http://www.w3schools.com/xml/">XML</a>, <a href="http://blogs.msdn.com/b/ncl/">Network Class Library</a>, <a href="http://www.w3schools.com/aspnet/default.asp">ASP.NET</a>, <a href="http://en.wikipedia.org/wiki/ADO.NET_Entity_Framework">Entity Framework</a>, <a href="http://msdn.microsoft.com/en-us/vstudio/jj684582.aspx">Windows Workflow Foundation</a> e <a href="http://msdn.microsoft.com/en-us/library/ms731082.aspx">Windows Communication Foundation</a>.</p> 
<p><strong>Windows Presentation Foundation</strong></p> 
<ul> 
 <li>Corrige o problema de recebimento no evento CanExecuteChanged ao implementar a interface ICommand;</li> 
 <li>Corrige o DataGrid ao definir o foco em uma c&eacute;lula na borda, e ao pressionar a tecla de seta que corresponde &agrave; coluna da borda;</li> 
 <li>Resolve um loop infinito e a exce&ccedil;&atilde;o System.OutOfMemoryException ao se tentar criar um painel personalizado que implementa a interface IScrollInfo;</li> 
 <li>Corrige a exce&ccedil;&atilde;o System.InvalidCastException quando chama o m&eacute;todo ScrollIntoView em um ListBox ou um DataGrid;</li> 
 <li>Corrige a exce&ccedil;&atilde;o System.NullReferenceException quando tenta implementar a interface INotifyDataErrorInfo em um objeto ou quando o seu objeto gera o evento ErrorsChanged.</li> 
</ul> 
<p><strong>Common Language Runtime (CLR)</strong></p> 
<ul> 
 <li>Resolve problemas de mau desempenho associados ao m&eacute;todo Array.Sort;</li> 
 <li>A atualiza&ccedil;&atilde;o resolve o erro &quot;Common Language Runtime detectou um programa inv&aacute;lido&quot; que se obtinha ap&oacute;s a atualiza&ccedil;&atilde;o do. NET Framework 4 para o 4.5.</li> 
 <li>H&aacute; corre&ccedil;&otilde;es de leitura de contadores de desempenho do ASP.NET ap&oacute;s a atualiza&ccedil;&atilde;o de uma vers&atilde;o anterior do. NET para o .NET 4.5.</li> 
 <li>Foi corrigido o retorno incorreto de valor ao utilizar o m&eacute;todo Type.IsAssignableFrom ap&oacute;s atualiza&ccedil;&atilde;o para o .NET Framework 4.5.</li> 
 <li>Corre&ccedil;&otilde;es de tratamento de exce&ccedil;&atilde;o na classe CryptoStream</li> 
 <li>Corrigida a exce&ccedil;&atilde;o System.Security.SecurityException quando controles de terceiros s&atilde;o utilizadas ap&oacute;s uma atualiza&ccedil;&atilde;o do framework .NET 4 para o .NET 4,5</li> 
</ul> 
<p><strong>Windows Forms</strong></p> 
<ul> 
 <li>Corre&ccedil;&otilde;es de intera&ccedil;&atilde;o de menus e o comportamento de janelas filhas e no posicionamento c&eacute;lula de controle TableLayoutPanel;</li> 
 <li>Corre&ccedil;&otilde;es no valor de retorno da cor (Color) ao usar propriedade System.Windows.Forms.FontDialog.Color.</li> 
</ul> 
<p><strong>XML</strong></p> 
<ul> 
 <li>Corre&ccedil;&otilde;es de exce&ccedil;&atilde;o ao tentar redefinir o namespace XML padr&atilde;o durante a <a href="http://www.w3schools.com/xsl/xsl_transformation.asp">transforma&ccedil;&atilde;o XSL</a>;</li> 
 <li>Corre&ccedil;&otilde;es de exce&ccedil;&atilde;o System.Reflection.TargetInvocationException quando a classe <a href="http://msdn.microsoft.com/en-us/library/system.xml.serialization.xmlserializer.aspx">XmlSerializer</a> &eacute; usada para serializar uma matriz de estruturas que implementa a interface <a href="http://msdn.microsoft.com/en-us/library/system.collections.ienumerable.aspx">IEnumerable</a>.</li> 
</ul> 
<p><strong>Network Class Library</strong></p> 
<ul> 
 <li>Corre&ccedil;&otilde;es de respostas fragmentadas quando as <a href="http://msdn.microsoft.com/en-in/library/windows/apps/hh452713.aspx">APIs ass&iacute;ncronas</a> s&atilde;o usadas;</li> 
 <li>Corrige exce&ccedil;&otilde;es n&atilde;o tratadas e posterior colis&atilde;o na <a href="http://www.symantec.com/connect/blogs/ssl-renegotiation-good-ddos-attacks-are-bad">renegocia&ccedil;&atilde;o de SSL</a> enquanto a aplica&ccedil;&atilde;o envia dados;</li> 
 <li>Corre&ccedil;&otilde;es de travamento de thread pools na classe <a href="http://msdn.microsoft.com/en-us/library/system.net.httpwebrequest.aspx">HttpWebRequest</a>;</li> 
 <li>Corrige a exce&ccedil;&atilde;o n&atilde;o tratada e posterior colis&atilde;o quando uma solicita&ccedil;&atilde;o HTTP &eacute; abortada e a autentica&ccedil;&atilde;o no proxy est&aacute; sendo negociada ao mesmo tempo.</li> 
</ul> 
<p><strong>ASP.NET</strong></p> 
<ul> 
 <li>Corrige a exibi&ccedil;&atilde;o de conte&uacute;do em Chin&ecirc;s Tradicional quando uma web application &eacute; acessada atrav&eacute;s da vers&atilde;o em Chin&ecirc;s Tradicional do Windows 8.</li> 
 <li>Corrige o valor dos contadores de desempenho do ASP.NET em um computador remoto quando o programa Perfmon.exe &eacute; utilizado em seu sistema local.</li> 
 <li>Corrige o erro de compila&ccedil;&atilde;o, como resultado da inser&ccedil;&atilde;o da tag &lt;thread&gt; em um controle de tabela HTML em uma p&aacute;gina ASP.NET usando o Visual Studio 2012.</li> 
 <li>Corrige o papel do valor do cookie quando a propriedade cachedRolesInCookie &eacute; definida como true.</li> 
 <li>Corrige o problema ocorrido quando o tipo de redirecionamento de p&aacute;gina AntiXssEncoder est&aacute; ligado na aplica&ccedil;&atilde;o, e pelo uso da propriedade NavigateUrl em HyperLinks nos controles de servidor web.</li> 
</ul> 
<p><strong>Entity Framework</strong></p> 
<ul> 
 <li>Corre&ccedil;&otilde;es de problemas de desempenho de redu&ccedil;&atilde;o devido &agrave; gera&ccedil;&atilde;o de instru&ccedil;&otilde;es SQL no Entity Framework quando usado com o <a href="http://www.microsoft.com/en-in/download/details.aspx?id=5783">SQL Server Compact 3.5</a> ou o <a href="http://www.microsoft.com/en-us/download/details.aspx?id=17876">SQL Server Compact 4.0</a>, ou ainda quando o aplicativo faz uso de <a href="http://msdn.microsoft.com/en-us/library/bb386964.aspx">LINQ to Entities</a> de consulta para executar v&aacute;rias declara&ccedil;&otilde;es <a href="http://www.w3schools.com/sql/sql_join_inner.asp">JOIN</a> sobre a entidade que define a obten&ccedil;&atilde;o de dados.</li> 
 <li>Melhora o desempenho da consulta quando voc&ecirc; tenta executar um aplicativo que consulta dados usando Entity Framework em um computador que tem o .NET Framework 4.5 instalado ou quando a consulta usa constructs de &quot;agrupar por vis&atilde;o&quot;.</li> 
</ul> 
<p><strong>Windows Workflow Foundation (WF)</strong></p> 
<ul> 
 <li>Corrige os arquivos de recursos embedding em quest&atilde;o no conjunto ao criar ou abrir um <a href="http://msdn.microsoft.com/en-us/library/bb483190%28v=vs.90%29.aspx">projeto existente no Visual Studio 2010</a>.</li> 
 <li>Corrige o problema de carregamento do deisign de fluxos de trabalho quando voc&ecirc; cria um projeto de <a href="http://msdn.microsoft.com/en-us/library/dd489397.aspx">Workflow console application</a> chamado WorkflowConsoleApplication1.</li> 
</ul> 
<p><strong>Windows Communication Foundation (WCF)</strong></p> 
<ul> 
 <li>Corrige a exce&ccedil;&atilde;o System.ServiceModel.ServiceActivationException quando voc&ecirc; tenta criar um projeto .NET 4.0 baseado em WCF em um computador que tem o .NET Framework 4.5 instalado, ou quando voc&ecirc; definir o valor da propriedade <a href="http://msdn.microsoft.com/en-us/library/system.servicemodel.servicehostingenvironment.aspnetcompatibilityenabled.aspx">aspNetCompatibilityEnabled</a> para true no arquivo <a href="http://en.wikipedia.org/wiki/Web.config">web.config</a>.</li> 
 <li>Corrige a exce&ccedil;&atilde;o System.Xml.XmlException quando API p&uacute;blica ByteStreamMessageEncoder.CreateMessage cria uma classe <a href="http://msdn.microsoft.com/en-us/library/system.xml.xmldictionaryreader.aspx">XmlDictionaryReader</a> que usa o padr&atilde;o da classe <a href="http://msdn.microsoft.com/en-us/library/system.xml.xmldictionaryreaderquotas.aspx">XmlDictionaryReaderQuotas</a> ao inv&eacute;s das quotas m&aacute;ximas definidas no XmlDictionaryReaderQuotas.Max.</li> 
 <li>Corrige a mensagem de erro ao tentar acessar a propriedade <a href="http://msdn.microsoft.com/en-us/library/system.web.httprequest.inputstream.aspx">HttpRequest.InputStream</a> em vez de uma opera&ccedil;&atilde;o de servi&ccedil;o.</li> 
 <li>Corrige o problema de tipos faltando quando voc&ecirc; tenta gerar <a href="http://www.codeproject.com/Articles/83223/Dynamically-Generate-a-WCF-Proxy">proxies WCF</a> para servi&ccedil;os ASMX usando um Add Service.</li> 
 <li>Utilit&aacute;rio de di&aacute;logo de refer&ecirc;ncia do .NET Framework 4.5 ou o <a href="http://msdn.microsoft.com/en-us/library/aa347733.aspx">Svcutil.exe</a>.</li> 
 <li>Corre&ccedil;&otilde;es do arquivo Reference.cs vazio quando voc&ecirc; tenta criar um projeto ASP.NET MVC4 com Web API no Visual Studio 2012, ou quando voc&ecirc; adiciona uma refer&ecirc;ncia de servi&ccedil;o WCF ao projeto.</li> 
</ul> 
<p>Segundo a Microsoft, n&atilde;o &eacute; preciso reiniciar o computador ap&oacute;s a instala&ccedil;&atilde;o dessa atualiza&ccedil;&atilde;o, se os arquivos afetados n&atilde;o estiverem sendo usados.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
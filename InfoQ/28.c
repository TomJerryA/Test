<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>LINQ para logs e rastreamentos</h3><p>A Microsoft Open Technologies, bra&ccedil;o da empresa que trabalha com tecnologias abertas, <a href="http://blogs.msdn.com/b/interoperability/archive/2014/01/06/new-release-tx-linq-to-logs-and-traces.aspx">anunciou recentemente</a> o lan&ccedil;amento do Tx, um projeto de c&oacute;digo aberto que pode ajudar a depura&ccedil;&atilde;o utilizando Logs e Traces, e construir sistemas para monitoramento de eventos e alerta em tempo real.</p>
<p>Algumas funcionalidades interessantes:</p>
<ul> 
 <li>Permite o uso de <a href="http://msdn.microsoft.com/en-us/library/bb397926.aspx">LINQ</a> em fontes de eventos do Windows;</li> 
 <li>Habilita o uso de <a href="http://msdn.microsoft.com/en-us/data/gg577609.aspx">Reactive Extensions</a> em fontes de eventos reais com suporte para sequ&ecirc;ncia de eventos multiplexados (uma &uacute;nica sequ&ecirc;ncia contendo eventos de diferentes tipos em ordem de ocorr&ecirc;ncia);</li> 
 <li>&Eacute; poss&iacute;vel fornecer consultas &uacute;nicas atrav&eacute;s de diferentes fontes, com a mesma API tanto para eventos em tempo real quanto para eventos hist&oacute;ricos;</li> 
 <li>Em logs hist&oacute;ricos, m&uacute;ltiplas consultas podem ser executadas em uma leitura - por exemplo, contar todos os eventos de &quot;Warning&quot;, comparar eventos &quot;Begin&quot; e &quot;End&quot; e calcular a dura&ccedil;&atilde;o m&eacute;dia de cada atividade.</li> 
</ul>
<p>Tamb&eacute;m &eacute; poss&iacute;vel usar o <a href="http://www.linqpad.net/">LINQPad</a> para analisar ou construir aplica&ccedil;&otilde;es .NET de monitoramento. No LINQPad, a experi&ecirc;ncia do Tx &eacute; como se todos os eventos estivessem em um banco de dados.</p>
<p>O lan&ccedil;amento fornece quatro pacotes diferentes para o NuGet:</p>
<ul> 
 <li><a href="http://www.nuget.org/packages/Tx.Core/">Tx.Core</a> - componentes comuns sem um formato de rastreamento especifico;</li> 
 <li><a href="http://www.nuget.org/packages/Tx.Windows/">Tx.Windows</a> - Suporte para o rastreamento de eventos (Event Tracing) no Windows, Event logs, e contradores de performance de arquivos e uma API de contador em tempo real, logs texto do IIS no formato W3C;</li> 
 <li><a href="http://www.nuget.org/packages/Tx.SqlServer/">Tx.SqlServer</a> - Eventos estendidos do SQL Server;</li> 
 <li><a href="http://www.nuget.org/packages/Tx.All/">Tx.All</a> - Um pacote de conveni&ecirc;ncia, com todos os listados acima.</li> 
</ul>
<p>Note que a Microsoft tamb&eacute;m aconselha <a href="http://tx.codeplex.com/SourceControl/latest#Doc/WhenToUse.md">quando n&atilde;o usar o Tx</a>:</p>
<ul> 
 <li>Quando n&atilde;o h&aacute; nenhum tipo de fornecimento de dados em tempo real envolvido e os dados j&aacute; est&atilde;o em mem&oacute;ria ou em um &uacute;nico arquivo de f&aacute;cil leitura, o guia &eacute; usar Linq-To-Objects ao inv&eacute;s do Tx;</li> 
 <li>Quando existe alimenta&ccedil;&atilde;o de dados em tempo real, mas cada fonte ou arquivo cont&eacute;m apenas um tipo de evento, use apenas as Reactive Extensions.</li> 
</ul>
<p>A ferramenta tem sido utilizada internamente na Microsoft, nas equipes do WCF e Service Bus e agora est&aacute; dispon&iacute;vel para todos os desenvolvedores .NET usarem em seus projetos. Para mais informa&ccedil;&otilde;es confira a <a href="http://tx.codeplex.com/documentation">documenta&ccedil;&atilde;o</a>.</p><br><br><br><br><br><br></body></html>
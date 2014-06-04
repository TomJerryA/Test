<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Gerencie as dívidas do seu software</h3><p>Existem diferentes tipos de d&iacute;vida de software. A&nbsp;<a href="http://www.google.com/url?q=http%3A%2F%2Fwww.infoq.com%2Ftechnicaldebt%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNEo7nP7hdOJreWXGvvVDAWBhQ8kCg">d&iacute;vida t&eacute;cnica</a> &eacute; a mais conhecida, mas n&atilde;o a &uacute;nica. Existem tamb&eacute;m as d&iacute;vidas de compet&ecirc;ncia e de qualidade. As d&iacute;vidas de software podem causar o aumento dos custos de manuten&ccedil;&atilde;o e tamb&eacute;m desencorajar desenvolvedores. Felizmente existem solu&ccedil;&otilde;es para gerenci&aacute;-las.</p>
<p>No post &quot;<a href="http://www.google.com/url?q=http%3A%2F%2Fwww.leanway.no%2Fcompetence-debt%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNG_wfiNUGsCBo8moGmO4AKZXf-CUw">O outro tipo de d&iacute;vida de software</a>&quot;, Niklas Bj&ouml;rnerstedt fala sobre a &quot;d&iacute;vida de compet&ecirc;ncia&quot;. Sua defini&ccedil;&atilde;o &eacute; a seguinte:</p>
<blockquote> 
 <p>A diferen&ccedil;a entre o que existe no seu c&oacute;digo e o quanto dele voc&ecirc; entende.</p> 
</blockquote>
<p>Para manter a manuten&ccedil;&atilde;o de software baixa, deve-se atentar tanto &agrave; d&iacute;vida t&eacute;cnica quanto &agrave; d&iacute;vida de compet&ecirc;ncia, conforme explica Niklas:</p>
<blockquote> 
 <p>Assim como a d&iacute;vida t&eacute;cnica, que cresce inevitavelmente com o tempo caso n&atilde;o seja enfrentado, a d&iacute;vida de compet&ecirc;ncia tamb&eacute;m segue a mesma regra. A maior diferen&ccedil;a entre elas &eacute; que, enquanto a d&iacute;vida&nbsp;t&eacute;cnica cresce conforme o c&oacute;digo sofre altera&ccedil;&otilde;es,&nbsp;a d&iacute;vida&nbsp;de compet&ecirc;ncia cresce mais r&aacute;pido se o c&oacute;digo n&atilde;o for alterado! A d&iacute;vidade compet&ecirc;ncia &eacute;, portanto, um problema que &eacute; mais agudo em sistemas maduros, que n&atilde;o est&atilde;o mais em desenvolvimento ativo.</p> 
</blockquote>
<p>Niklas prop&otilde;e duas t&eacute;cnicas cl&aacute;ssicas que podem ser usadas para reduzir essa d&iacute;vida: programa&ccedil;&atilde;o em pares e refatora&ccedil;&atilde;o de c&oacute;digo:</p>
<blockquote> 
 <p>Para mim, o valor real da programa&ccedil;&atilde;o em pares &eacute; a redu&ccedil;&atilde;o das d&iacute;vidas t&eacute;cnica e de compet&ecirc;ncia. Ao trabalhar em pares, as equipes ampliam as &aacute;reas da base de c&oacute;digo com as quais est&atilde;o familirializadas e aumentam a troca de experi&ecirc;ncias. De maneira similar, o valor da refatora&ccedil;&atilde;o n&atilde;o &eacute; apenas a redu&ccedil;&atilde;o da d&iacute;vida&nbsp;t&eacute;cnica. A refatora&ccedil;&atilde;o &eacute; uma &oacute;tima maneira de reduzir tamb&eacute;m&nbsp;a d&iacute;vida&nbsp;de compet&ecirc;ncia. S&oacute; se pode alterar um sistema se ele realmente for bem compreendido.</p> 
</blockquote>
<p>Quando a d&iacute;vida de compet&ecirc;ncia se acumula, o esfor&ccedil;o necess&aacute;rio para manter sistemas aumenta, at&eacute; chegar ao ponto em que as empresas come&ccedil;am a considerar a substitui&ccedil;&atilde;o do sistema:</p>
<blockquote> 
 <p>Pode-se alegar que um determinado sistema antigo &eacute; dif&iacute;cil de manter, quando na verdade o problema &eacute; que n&atilde;o se entende corretamente como o sistema funcionava. Sim, a d&iacute;vida&nbsp;t&eacute;cnica torna as coisas ainda piores, uma vez que c&oacute;digo confuso e a falta de testes automatizados tornam frustrante a tentativa de entender o sistema. O impulso por reescrever vem normalmente quando apenas poucos dos desenvolvedores originais ainda restam na equipe e a empresa n&atilde;o consegue encontrar novos desenvolvedores dispostos a aprender.</p> 
</blockquote>
<p>Mike Hustler escreveu um post sobre <a href="http://www.google.com/url?q=http%3A%2F%2Fwww.appneta.com%2Fblog%2Fagile-technical-debt%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNHR5617jAUZJGrnC1DqselL1b6_wA">a forma mais &aacute;gil de gerenciar a d&iacute;vida t&eacute;cnica</a>, no qual discute como equlibrar entre desenvolver novas funcionalidades em um produto e gerenciar a d&iacute;vida t&eacute;cnica. Ele explica como a abordagem de transferir produtos para times de manuten&ccedil;&atilde;o pode levar ao crescimento das d&iacute;vidas t&eacute;cnicas e de compet&ecirc;ncia:</p>
<blockquote> 
 <p>J&aacute; vi organiza&ccedil;&otilde;es criando times de manuten&ccedil;&atilde;o separados, os quais tinham metade do tamanho de um time que desenvolve novas funcionalidades. Em minha opini&atilde;o, essa &eacute; uma abordagem err&ocirc;nea (pelo menos comparado ao tamanho dos times que trabalhamos). (...) O comprometimento que surge de se sentir orgulho por ser dono de um produto &eacute; perdido quando algu&eacute;m fica respons&aacute;vel por solucionar os bugs criados por uma outra pessoa que, na verdade, pertence a um outro time.</p> 
 <p>Sem uma comunica&ccedil;&atilde;o s&oacute;lida, as raz&otilde;es que levam a optar por uma determinada abordagem ou solu&ccedil;&atilde;o s&atilde;o perdidas. O conhecimento do dom&iacute;nio n&atilde;o se torna presente, e a efici&ecirc;ncia em corrigir problemas &eacute; reduzida. Ainda pior, j&aacute; vi times de manuten&ccedil;&atilde;o com menos experi&ecirc;ncia que tiveram dificuldades para identificar a causa raiz de problemas, resultando em remendos onde um redesenho seria mais apropriado.</p> 
</blockquote>
<p>A d&iacute;vida t&eacute;cnica deprime os desenvolvedores e pode lev&aacute;-los a deixar o time, o que aumenta ainda mais a d&iacute;vida de compet&ecirc;ncia, conforme Cory House descreve em seu post &quot;<a href="http://www.google.com/url?q=http%3A%2F%2Fblog.pluralsight.com%2F7-reasons-clean-code-matters&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNG8i_fY3tcvfQVWx--j04Hz3rEmUw">Sete raz&otilde;es porque c&oacute;digo limpo &eacute; importante</a>&quot;:</p>
<blockquote> 
 <p>Escrever c&oacute;digo confuso e de maneira desleixada injeta d&iacute;vida t&eacute;cnica em nossos projetos. Enquanto&nbsp;d&iacute;vida t&eacute;cnica&nbsp;pode ser &uacute;til quando considerada cuidadosamente no seu contexto, a d&iacute;vida t&eacute;cnica&nbsp;excessiva &eacute; deprimente e afasta talentos das organiza&ccedil;&otilde;es. Quando coisas simples se tornam complexas, desenvolvedores ficam insatisfeitos e v&atilde;o trabalhar em outro lugar. Desenvolvedores obt&ecirc;m mais satisfa&ccedil;&atilde;o a partir da qualidade do seu trabalho do que da quantidade. A d&iacute;vida t&eacute;cnica diminui as chances de reuso e estabelece um n&iacute;vel baixo de qualidade para toda a base de c&oacute;digo.</p> 
</blockquote>
<p>David Hammerslag escreveu o post &quot;<a href="http://www.google.com/url?q=http%3A%2F%2Fwww.bigvisible.com%2F2013%2F10%2Fwant-predictability-avoid-quality-debt%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNFVSdkE3Q0xpVutNRNsyUwEor4BGA">Quer previsibilidade? Evite a d&iacute;vida de qualidade</a>&quot; onde ele discute os efeitos de encontrar defeitos no c&oacute;digo e n&atilde;o corrigi-los. A defini&ccedil;&atilde;o de David para o a d&iacute;vida de qualidade &eacute; a seguinte:</p>
<blockquote> 
 <p>A d&iacute;vida de qualidade &eacute; uma medida do esfor&ccedil;o necess&aacute;ria para corrigir os defeitos existentes em um software a qualquer momento.</p> 
</blockquote>
<p>David faz uma compara&ccedil;&atilde;o entre a d&iacute;vida de qualidade e a d&iacute;vida t&eacute;cnica:</p>
<blockquote> 
 <p>A d&iacute;vida t&eacute;cnica &eacute; uma medida da qualidade do design e do c&oacute;digo, os quais s&atilde;o a qualidade interna do software. A d&iacute;vida de qualidade &eacute; uma medida da qualidade externa do c&oacute;digo: as coisas que o usu&aacute;rio v&ecirc; e experimenta. Um usu&aacute;rio nunca enxerga (diretamente) a d&iacute;vida t&eacute;cnica.</p> 
 <p>Um programa pode ser completamente livre de d&iacute;vida de qualidade mas, em contrapartida, pode possuir uma enorme d&iacute;vida t&eacute;cnica. Esse mesmo programa pode implementar corretamente todas as funcionalidades requeridas e executar sem nenhuma falha. Ainda assim sua d&iacute;vida t&eacute;cnica pode ser enorme, contendo todas as m&aacute;s pr&aacute;ticas de design e implementa&ccedil;&atilde;o que se possa imaginar. De maneira inversa, o c&oacute;digo mais bem projetado e elegante pode produzir resultados errados ou n&atilde;o conter todas as funcionalidades esperadas.</p> 
</blockquote>
<p>A d&iacute;vida de qualidade n&atilde;o deve ser ignorada, conforme David explica:</p>
<blockquote> 
 <p>A d&iacute;vida de qualidade &eacute; como uma d&iacute;vida financeira: quanto mais tempo se demora com ela, mais dif&iacute;cil torna-se para liquid&aacute;-la. No pior caso, um projeto adia os testes at&eacute; que o desenvolvimento esteja completo. &Eacute; fato que, quanto mais tempo um defeito permanece no c&oacute;digo, mais dif&iacute;cil ser&aacute; corrigi-lo. Se v&aacute;rios defeitos persistem (sejam eles conhecidos ou n&atilde;o), o efeito &eacute; agravado ainda mais, pois esses defeitos tendem a mascarar uns aos outros.</p> 
</blockquote>
<p>David sugere diversas pr&aacute;ticas &aacute;geis que podem ser usadas para gerenciar defeitos e manter baixa a d&iacute;vida de qualidade:</p>
<blockquote> 
 <ul class="c3 lst-kix_hx3i005hb41p-0 start"> 
  <li>Defini&ccedil;&atilde;o de pronto (Done)</li> 
  <li>BDD e testes de aceita&ccedil;&atilde;o automatizados</li> 
  <li>Integra&ccedil;&atilde;o cont&iacute;nua</li> 
  <li>Testes automatizados</li> 
  <li>N&atilde;o tolerar &quot;janelas quebradas&quot; (toler&acirc;ncia zero).</li> 
 </ul> 
</blockquote>
<p>&nbsp;</p><br><br><br><br><br><br></body></html>
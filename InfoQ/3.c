<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PayPal muda de Java para JavaScript</h3><p>O PayPal decidiu usar JavaScript de ponta-a-ponta, do browser at&eacute; o servidor de backend para aplica&ccedil;&otilde;es web, descontinuando o c&oacute;digo legado escrito em JSP/Java.</p>
<p>Jeff Harrell, diretor de engenharia do PayPal, explicou em alguns posts no seu blog (<a href="https://www.paypal-engineering.com/2013/06/17/set-my-ui-free-part-1-dust-javascript-templating-open-source-and-more/">Set My UI Free Part 1: Dust JavaScript Templating, Open Source and More</a>, <a href="https://www.paypal-engineering.com/2013/11/22/node-js-at-paypal/">Node.js at PayPal</a>), o motivo por tr&aacute;s dessa decis&atilde;o e algumas das conclus&otilde;es que resultaram da mudan&ccedil;a de seu desenvolvimento web de JSP/Java para uma solu&ccedil;&atilde;o totalmente JavaScript/Node.js.</p>
<p>Segundo Harrell, os sites do PayPal acumularam um grande n&uacute;mero de d&iacute;vidas t&eacute;cnicas, e a ideia era ter &quot;uma pilha tecnol&oacute;gica livre delas de modo a possibilitar uma maior agilidade e inova&ccedil;&atilde;o em seus produtos&quot;. Inicialmente, existia uma grande cisma entre os engenheiros de frontend, que trabalhavam com tecnologias web e os engenheiros de backend, que trabalhavam com Java. Quando algu&eacute;m de UX queria desenhar algumas p&aacute;ginas, era necess&aacute;rio pedir para os desenvolvedores Java fazer configura&ccedil;&otilde;es no backend. Isso n&atilde;o se encaixava com o modelo adotado de Lean UX:</p>
<blockquote> 
 <p>Na &eacute;poca, nossas aplica&ccedil;&otilde;es de interface de usu&aacute;rio eram baseadas em uma solu&ccedil;&atilde;o Java e JSP propriet&aacute;ria r&iacute;gida, fortemente acoplada de dif&iacute;cil manuten&ccedil;&atilde;o e aprendizado. Nossas equipes al&eacute;m de n&atilde;o considerarem essa situa&ccedil;&atilde;o aderente ao nosso modelo de desenvolvimento Lean UX, tamb&eacute;m n&atilde;o conseguiam mover-se rapidamente internamente de forma que passaram a construir seus prot&oacute;tipos em uma linguagem de script, test&aacute;-los com os usu&aacute;rios, e depois portar o c&oacute;digo para a nossa pilha de produ&ccedil;&atilde;o.</p> 
</blockquote>
<p>Havia o desejo de uma &quot;solu&ccedil;&atilde;o de template desacoplada da tecnologia utilizada no lado servidor e que permitisse a evolu&ccedil;&atilde;o das interfaces de usu&aacute;rio, independentemente da linguagem da aplica&ccedil;&atilde;o&quot;, isso deveria funcionar em m&uacute;ltiplos ambientes.</p>
<p>A decis&atilde;o foi utilizar o <a href="http://akdubya.github.io/dustjs/">Dust.js</a> - um framework apoiado pelo LinkedIn - somado ao Bootstrap do Twitter e Bower, um gerenciador web de pacotes. As partes adicionadas posteriormente foram LESS, RequireJS, Backbone.js, Grunt e Mocha.</p>
<p>Algumas das p&aacute;ginas do PayPal foram redesenhadas, mas ainda mantiveram um pouco da pilha legada:</p>
<blockquote> 
 <p>… temos como legado c&oacute;digos C++/XSL e Java/JSP, e n&atilde;o quer&iacute;amos deixar essas interfaces de usu&aacute;rio para tr&aacute;s, &agrave; medida que segu&iacute;amos adiante. Templates JavaScript s&atilde;o ideais para isso. Sobre a pilha C++, constru&iacute;mos uma biblioteca que utilizou V8 para fazer uso de renderizadores Dust nativamente - o resultado em termos de velocidade foi excelente. No lado Java, integramos o Dust usando um Spring ViewResolver acoplado ao Rhine para renderizar a camada de visualiza&ccedil;&atilde;o.</p> 
</blockquote>
<p>Naquela &eacute;poca, tamb&eacute;m passaram a utilizar o Node.js para prototipar novas p&aacute;ginas, concluindo que era &quot;extremamente proficiente&quot; e decidiram experimentar isso em produ&ccedil;&atilde;o. Para isso, constru&iacute;ram o <a href="https://github.com/paypal/kraken-js">Kraken.js</a>, uma &quot;camada&quot; sobre o Express, que por sua vez &eacute; um framework web baseado em Node.js. (PayPal recentemente tornou o Kraken.js como c&oacute;digo-aberto). A primeira aplica&ccedil;&atilde;o a ser feita em Node.js foi a p&aacute;gina de vis&atilde;o geral da conta, que era uma das p&aacute;ginas mais acessadas do PayPal, segundo Harrell. Mas gra&ccedil;as ao temor de que o app n&atilde;o escalasse bem, decidiram criar uma aplica&ccedil;&atilde;o Java equivalente como seguran&ccedil;a para o caso da aplica&ccedil;&atilde;o Node.js n&atilde;o funcionar. A seguir, est&atilde;o algumas conclus&otilde;es referentes ao esfor&ccedil;o de desenvolvimento dispendido para ambas aplica&ccedil;&otilde;es:</p>
<p>&nbsp;</p>
<table border="1" cellpadding="7" cellspacing="5"> 
 <tbody> 
  <tr> 
   <td width="220px"> 
    <div align="center">
     &nbsp;
    </div> </td> 
   <td align="right" width="220px"> <p align="center"><strong>Java/Spring</strong></p> </td> 
   <td align="right" width="220px"> <p align="center"><strong>JavaScript/Node.js</strong></p> </td> 
  </tr> 
  <tr> 
   <td> <p align="center">Configura&ccedil;&atilde;o inicial</p> </td> 
   <td align="right"> <p align="center">0</p> </td> 
   <td align="right"> <p align="center">2 meses</p> </td> 
  </tr> 
  <tr> 
   <td> <p align="center">Desenvolvimento</p> </td> 
   <td align="right"> <p align="center">aprox. 5 meses</p> </td> 
   <td align="right"> <p align="center">aprox. 3 meses</p> </td> 
  </tr> 
  <tr> 
   <td> <p align="center">Engenheiros</p> </td> 
   <td align="right"> <p align="center">5</p> </td> 
   <td align="right"> <p align="center">2</p> </td> 
  </tr> 
  <tr> 
   <td> <p align="center">Linhas de c&oacute;digo</p> </td> 
   <td> <p align="center">n&atilde;o especificado</p> </td> 
   <td> <p align="center">66% n&atilde;o especificado</p> </td> 
  </tr> 
 </tbody> 
</table>
<p>A equipe JavaScript precisou de dois meses para a configura&ccedil;&atilde;o inicial da infraestrutura, mas criou - com menos pessoas - uma aplica&ccedil;&atilde;o com a mesma funcionalidade e em menos tempo. Executando a su&iacute;te de testes em hardware de produ&ccedil;&atilde;o, concluiu que o aplicativo Node.js estava com desempenho melhor que o anterior em Java, servindo:</p>
<blockquote> 
 <p>o dobro de requisi&ccedil;&otilde;es por segundo em rela&ccedil;&atilde;o &agrave; aplica&ccedil;&atilde;o Java. Isso &eacute; ainda mais interessante, devido aos nossos resultados inicias de performance estarem utilizando apenas um n&uacute;cleo para a aplica&ccedil;&atilde;o Node.js, contra cinco da aplica&ccedil;&atilde;o Java. Temos expectativa que essa essa diferen&ccedil;a possa ser ainda maior.</p> 
</blockquote>
<p>e resultando</p>
<blockquote> 
 <p>um decr&eacute;scimo de 35% no tempo m&eacute;dio de resposta para a mesma p&aacute;gina. Isso resultou em p&aacute;ginas sendo servidas 200ms mais r&aacute;pido - algo que os usu&aacute;rios certamente perceber&atilde;o.</p> 
</blockquote>
<p>Como resultado, o PayPal come&ccedil;ou a utilizar em produ&ccedil;&atilde;o a aplica&ccedil;&atilde;o Node.js beta, tendo decidido que &quot;daqui em diante todas as nossas aplica&ccedil;&otilde;es web para o cliente ser&atilde;o feitas em Node.js,&quot; enquanto algumas das existentes est&atilde;o sendo portadas para Node.js.</p>
<p>Um dos benef&iacute;cios de utilizar JavaScript do browser at&eacute; o servidor &eacute;, de acordo com Harrell, a elimina&ccedil;&atilde;o da separa&ccedil;&atilde;o do desenvolvimento front e backend, por ter uma &uacute;nica equipe &quot;que nos permite entender e reagir &agrave;s necessidades dos nossos usu&aacute;rios em qualquer n&iacute;vel da pilha tecnol&oacute;gica.&quot;</p><br><br><br><br><br><br></body></html>
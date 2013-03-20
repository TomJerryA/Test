<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Stripe abre código do Abba, um framework para testes A/B</h3><p>A <a href="https://stripe.com/">Stripe</a> abriu os fontes de seu framework de JavaScript para <a href="http://en.wikipedia.org/wiki/A/B_testing">testes A/B</a> chamado <a href="https://github.com/maccman/abba">Abba</a>. Com ele, para criar um teste para uma aplica&ccedil;&atilde;o web, basta que o trecho de c&oacute;digo seguinte seja inserido na p&aacute;gina principal:</p> 
<pre>
&lt;script&gt;
  Abba('test name')
    .control('Test A', function(){ /* ... */ })
    .variant('Test B', function(){ /* ... */ })
    .start();
&lt;/script&gt;
</pre> 
<p>Este trecho de c&oacute;digo define um teste de controle chamado Test A, para o qual todos os resultados ser&atilde;o relatados, e uma outra varia&ccedil;&atilde;o de nome Test B. &Eacute; poss&iacute;vel criar diversas varia&ccedil;&otilde;es de um teste. Para cada teste, uma rotina de tratamento &eacute; especificada, sendo chamada pelo framework quando necess&aacute;rio.</p> 
<p>Quando o teste &eacute; iniciado, o Abba faz, aleatoriamente, chamada para os controladores associados com os diferentes testes. Esta a&ccedil;&atilde;o normalmente resulta na exibi&ccedil;&atilde;o de p&aacute;ginas diferentes para os usu&aacute;rios de um site. O framework armazena e rastreia as a&ccedil;&otilde;es de cada usu&aacute;rio durante o teste, at&eacute; sua conclus&atilde;o. Se configurado adequadamente, o Abba &eacute; capaz de garantir que um usu&aacute;rio acesse a mesma p&aacute;gina que acessou anteriormente quando voltar a visitar o site.</p> 
<p>Os dados s&atilde;o armazenados em um banco de dados MongoDB e podem ser visualizados em formato de um gr&aacute;fico de visitas di&aacute;rias e taxas de convers&atilde;o (visitantes que completaram o teste) para um certo per&iacute;odo de tempo. Valores para diferentes varia&ccedil;&otilde;es s&atilde;o ponderados e uma <a href="http://en.wikipedia.org/wiki/Standard_score">pontua&ccedil;&atilde;o padr&atilde;o</a> &eacute; computada para avaliar a exatid&atilde;o do teste. Os resultados inclusive podem ser filtrados por data e/ou tipo de navegador.</p> 
<p>O Abba pode executar tanto localmente como em um servidor dedicado, com explica&ccedil;&otilde;es fornecidas para execut&aacute;-lo sobre o Heroku. O framework requer o Ruby 1.9.3 e o MongoDB.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Os custos para versionamento de uma API</h3><p>O versionamento de contrato e o versionamento de API/Servi&ccedil;os sempre foram motivos de preocupa&ccedil;&atilde;o em sistemas baseados em SOA. Seja devido ao <a href="http://www.infoq.com/articles/contract-versioning-comp2">impacto que existe sobre a modularidade</a>, ou a <a href="http://www.infoq.com/articles/Web-Service-Contracts">governan&ccedil;a cliente-servi&ccedil;o</a>. Neste cen&aacute;rio, versionamento ainda &eacute; uma esp&eacute;cie de arte mais do que uma ci&ecirc;ncia. H&aacute; muitos exemplos de grupos publicando o benef&iacute;cio de suas experi&ecirc;ncias (por exemplo, o <a href="http://www.infoq.com/news/2013/09/versioning-restful-services">REST</a> &eacute; <a href="http://www.infoq.com/news/2010/06/rest-versioning">extremamente popular</a>). Entretanto, Jean-Jacques Dubray <a href="http://www.ebpml.org/blog2/index.php/2013/11/25/understanding-the-costs-of-versioning#">escreveu um artigo</a> recentemente que tenta injetar algum objetivo cient&iacute;fico nesse dom&iacute;nio de problema.</p>
<blockquote> 
 <p>Pediram-me recentemente para criar uma estimativa dos custos de versionamento de APIs (ou WebServices). Gostaria de compartilhar essa estimativa porque sinto que muitas pessoas continuam n&atilde;o entendendo o custo e as implica&ccedil;&otilde;es ao se versionar uma API/Servi&ccedil;o.</p> 
</blockquote>
<p>De acordo com Jean-Jacques Dubray, durante o trabalho, foi descoberto que o custo de constru&ccedil;&atilde;o de APIs dependia da abordagem a ser utilizada posteriormente para o versionamento dessas APIs.</p>
<blockquote> 
 <p>A parte mais importante a entender &eacute;, mesmo que o custo para os consumidores pare&ccedil;a pequeno para voc&ecirc;, n&atilde;o se trata de apenas um custo puro, isso &eacute; risco, interrup&ccedil;&atilde;o em planos de projetos, or&ccedil;amentos indispon&iacute;veis… com mudan&ccedil;as que n&atilde;o tem valor de neg&oacute;cio imediato para um cliente real que n&atilde;o espera nenhuma mudan&ccedil;a na API.</p> 
</blockquote>
<p>O artigo ent&atilde;o passa a classificar tr&ecirc;s diferentes abordagens para o controle de vers&atilde;o de uma API (veja o artigo completo para se aprofundar em cada assunto, incluindo como o autor define uma maneira para mensurar custos):</p>
<ul class="c9 lst-kix_kjfzp0xgf3x2-0 start"> 
 <li><strong>O N&oacute;</strong> - &quot;Todos os consumidores est&atilde;o vinculados a uma &uacute;nica vers&atilde;o da API, quando a API muda, todos consumidores tem que mudar, basicamente criando um massivo efeito em cascata em todo o conjunto de consumidores / ecossistemas.&quot;</li> 
</ul>
<p><img src="http://www.infoq.com/resource/news/2013/12/api-versioning/pt/resources/imagem01.png" alt="" _href="img://imagem01.png" _p="true" /></p>
<ul class="c9 lst-kix_y84b0f6573lh-0 start"> 
 <li><strong>Ponto a Ponto</strong> - &quot;Cada vers&atilde;o do servi&ccedil;o &eacute; deixada em execu&ccedil;&atilde;o e em produ&ccedil;&atilde;o e os consumidores s&atilde;o obrigados a mudar por conta pr&oacute;pria, quando eles desejarem. O custo de manuten&ccedil;&atilde;o aumenta conforme o n&uacute;mero de vers&otilde;es em produ&ccedil;&atilde;o aumenta.&quot;</li> 
</ul>
<p><img src="http://www.infoq.com/resource/news/2013/12/api-versioning/pt/resources/imagem 2.png" alt="" _href="img://imagem 2.png" _p="true" /></p>
<ul class="c9 lst-kix_oq8ggrruul9t-0 start"> 
 <li><strong>Versionamento Compat&iacute;vel</strong> - &quot;Todos clientes conversam com a mesma vers&atilde;o de API/Servi&ccedil;o compat&iacute;vel.&quot;</li> 
</ul>
<p><img src="http://www.infoq.com/resource/news/2013/12/api-versioning/pt/resources/imagem 3.png" alt="" _href="img://imagem 3.png" _p="true" /></p>
<p>Dadas essas defini&ccedil;&otilde;es e os custos associados computados utilizando as equa&ccedil;&otilde;es que Jean-Jacques Dubray descreve, &eacute; poss&iacute;vel tra&ccedil;ar os custos relativos como mostrado abaixo (o eixo y &eacute; o custo, o eixo x &eacute; o n&uacute;mero da vers&atilde;o):</p>
<p><img src="http://www.infoq.com/resource/news/2013/12/api-versioning/pt/resources/imagem 4.png" alt="" _href="img://imagem 4.png" _p="true" /></p>
<p>Sobre os custos relativos, o autor escreveu que:</p>
<blockquote> 
 <p>[...] uma &uacute;nica vers&atilde;o for&ccedil;ando cada consumidor a migrar quando a API muda &eacute; o custo mais caro para o ecossistema. A multiplicidade de vers&otilde;es que precisam ser mantidas &eacute; melhor, mas ainda muito caro quando voc&ecirc; tenta manter atualizada cada vers&atilde;o, ou alternativamente, funcionando em vers&otilde;es mais antigas. A estrat&eacute;gia de vers&atilde;o compat&iacute;vel parece oferecer a melhor efici&ecirc;ncia.</p> 
</blockquote>
<p>Ent&atilde;o o que os outros acham dessa abordagem? &Eacute; esta a maneira que Jean-Jacques Dubray e sua equipe calculam o custo de versionar APIs aplicados al&eacute;m dos ambientes no qual eles foram desenvolvidos? A explica&ccedil;&atilde;o relativa dos custos faz sentido dado sua pr&oacute;pria experi&ecirc;ncia? Existem outras categorias que Jean-Jacques Dubray e sua equipe n&atilde;o cobriram?</p><br><br><br><br><br><br></body></html>
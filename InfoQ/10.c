<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>50 dicas para aplicações web mais rápidas no Windows</h3><p>O gerente de projetos do Internet Explorer <a href="http://www.google.com/url?q=http%3A%2F%2Fchannel9.msdn.com%2FEvents%2FSpeakers%2Fjatinder-mann&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNEk6Lw8oaKlBiaGxqq6va0muePeSA">Jatinder Mann</a> da Microsoft apresentou uma a palestra <a href="http://www.google.com/url?q=http%3A%2F%2Fchannel9.msdn.com%2FEvents%2FBuild%2F2012%2F3-132%3Fformat%3Dhtml5&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNH7ZSgMWCKYBHZHm7mijZkC9mXYFg">50 truques de performance para fazer suas aplica&ccedil;&otilde;es HTML 5 e sites mais r&aacute;pidos</a>, no evento BUILD, fornecendo dezenas de dicas para criar aplica&ccedil;&otilde;es web mais r&aacute;pidas. Os conselhos dados por Jatinder Mann foram organizados em volta de seis princ&iacute;pios fundamentais.</p> 
<p><strong>1. Responder rapidamente a requisi&ccedil;&otilde;es de rede</strong></p> 
<ul> 
 <li>Evite redirecionamentos. 63% dos mil sites mais acessados utilizam redirecionamentos. A performance desses sites poderiam melhorar em 10% caso esse recurso n&atilde;o fosse utilizado.</li> 
 <li>Evite utilizar a tag de <a href="http://www.google.com/url?q=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMeta_refresh&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNEUHafMZ_Pb3ykX5EDNE03Yrf5gjQ">meta-refresh</a>. 14% das URLs do mundo utilizam essa tag.</li> 
 <li>Reduza o tempo de resposta do servidor utilizando CDNs (redes de distribui&ccedil;&atilde;o de conte&uacute;do) localizadas o mais pr&oacute;ximo poss&iacute;vel dos usu&aacute;rios.</li> 
 <li>Maximize o uso de conex&otilde;es paralelas no navegador, efetuando o download de recursos a partir de diferentes dom&iacute;nios.</li> 
 <li>Reutilize conex&otilde;es. N&atilde;o feche uma conex&atilde;o ao responder uma requisi&ccedil;&atilde;o.</li> 
 <li>Garanta que dados servidos por parceiros n&atilde;o estejam causando lentid&atilde;o no carregamento das p&aacute;ginas.</li> 
 <li>Entenda o tempo de cada um dos componentes de rede - Redirect, Cache, DNS, Request, Response etc. Utilize a <a href="http://www.google.com/url?q=http%3A%2F%2Fmsdn.microsoft.com%2Fen-us%2Flibrary%2Fie%2Fhh673552(v%3Dvs.85).aspx&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNF93RzSWFAqo6hfczo9vk-TgNrpMA">API de tempo de navega&ccedil;&atilde;o</a> no Internet Explorer 9 e 10 para medir o tempo gasto pelo navegador em cada opera&ccedil;&atilde;o.</li> 
</ul> 
<p><strong>2. Minimizar o tamanho dos downloads.</strong> Minimize a quantidade de dados que precisa ser baixado quando a p&aacute;gina &eacute; carregada. O tamanho m&eacute;dio de download de um site &eacute; de 777KB dos quais 474KB s&atilde;o imagens, 128 KB s&atilde;o scripts e 84KB s&atilde;o arquivos Flash.</p> 
<ul> 
 <li>Fa&ccedil;a requisi&ccedil;&otilde;es de conte&uacute;do compactado (gzip).</li> 
 <li>Mantenha recursos localmente em pacotes, como o <a href="http://www.google.com/url?q=http%3A%2F%2Fmsdn.microsoft.com%2Fen-us%2Flibrary%2Fwindows%2Fapps%2Fhh694557.aspx&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNGQCKMFg-gIAJe5qxlirmvUtBoD3w">Package Resource Index</a> gerado por aplicativos da Windows Store. Dessa forma os recursos sempre estar&atilde;o dispon&iacute;veis quando necess&aacute;rio.</li> 
 <li>Efetue o cache de recursos din&acirc;micos utilizando o recurso de cache do HTML5 (HTML5 App Cache). Esse cache efetua o download dos recursos apenas uma vez, evitando m&uacute;ltiplas requisi&ccedil;&otilde;es de rede. O cache tamb&eacute;m efetua um novo download dos recursos automaticamente quando a vers&atilde;o do aplicativo &eacute; alterada.</li> 
 <li>Sempre que poss&iacute;vel, forne&ccedil;a conte&uacute;do que possa ser posto em cache, utilizando o campo &quot;Expires&quot; nas respostas.</li> 
 <li>Utilize requisi&ccedil;&otilde;es condicionais configurando o campo <a href="http://www.google.com/url?q=http%3A%2F%2Fwww.w3.org%2FProtocols%2Frfc2616%2Frfc2616-sec14.html&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNGH6cWhVOVootz02-X0U6wgo7eFQw">If-Modified-Since</a> na requisi&ccedil;&atilde;o.</li> 
 <li>Efetue o cache de requisi&ccedil;&atilde;o de dados - HTTP, XML, JSON, etc - porque cerca de 95-96% das requisi&ccedil;&otilde;es n&atilde;o se alteram ao longo de um dia. Embora esta seja uma boa ideia, menos de 1% dos sites efetuam cache de respostas de requisi&ccedil;&otilde;es.</li> 
 <li>Padronize a varia&ccedil;&atilde;o de mai&uacute;sculas e min&uacute;sculas no nome dos arquivos do site. Apesar de o servidor reconhecer a diferen&ccedil;a entre Icon.jpg e icon.jpg, esses arquivos s&atilde;o recursos diferentes para a plataforma web, gerando diferentes requisi&ccedil;&otilde;es de rede.</li> 
</ul> 
<p><strong>3. Estruture o HTML de maneira eficiente.</strong> Para o Internet Explorer utilize as &uacute;ltimas vers&otilde;es do HTML, pois s&atilde;o as mais r&aacute;pidas. Vers&otilde;es anteriores (Internet Explorer 6 ao 9) s&atilde;o reconhecidas pelo Internet Explorer 10, mas n&atilde;o s&atilde;o t&atilde;o r&aacute;pidas como a mais recente.</p> 
<ul> 
 <li>Utilize o campo do cabe&ccedil;alho http &quot;X-UA-Compatible: IE=EmulateIE7&quot; o inv&eacute;s da tag HTML &lt;meta http-equiv=&quot;X-UA-Compatible&quot; content=&quot;IE=EmulateIE7&quot;&gt;, para for&ccedil;ar o IE a executar em modo legado, o que pode ser necess&aacute;rio para algumas aplica&ccedil;&otilde;es web de neg&oacute;cios. &Eacute; mais r&aacute;pido.</li> 
 <li>Arquivos de estilos devem ser vinculados no topo da p&aacute;gina dentro da tag &lt;head&gt; e depois da tag &lt;title&gt; para proporcionar renderiza&ccedil;&atilde;o mais suave.</li> 
 <li>Arquivos de estilos nunca devem ser vinculados no rodap&eacute; da p&aacute;gina. A p&aacute;gina pode piscar enquanto estiver carregando nesses casos.</li> 
 <li>Evite utilizar &quot;@import&quot; para heran&ccedil;a de estilos porque isso bloqueia a cria&ccedil;&atilde;o das estruturas de dados do CSS e a renderiza&ccedil;&atilde;o das p&aacute;ginas.</li> 
 <li>Evite utilizar estilos CSS diretamente na p&aacute;gina e em tags HTML porque isso for&ccedil;a o navegador a fazer uma mudan&ccedil;a de contexto, na interpreta&ccedil;&atilde;o de HTML e CSS durante o carregamento da p&aacute;gina.</li> 
 <li>Vincule somente arquivos de estilos que realmente sejam necess&aacute;rios, para evitar o download e a interpreta&ccedil;&atilde;o de recursos que n&atilde;o ser&atilde;o usados.</li> 
 <li>Vincule arquivos JavaScript no rodap&eacute; da p&aacute;gina. Isso garante que imagens, CSS e outros recursos j&aacute; foram carregados; ent&atilde;o os scripts podem executar sem ter que esperar que outros recursos sejam carregados. Isso tamb&eacute;m evita a mudan&ccedil;a de contexto.</li> 
 <li>N&atilde;o vincule recursos JavaScript no topo da p&aacute;gina. Utilize o atributo &quot;defer&quot; se algum script precisar ser carregado no in&iacute;cio da p&aacute;gina.</li> 
 <li>Evite utilizar JavaScript diretamente na p&aacute;gina para evitar mudan&ccedil;as de contexto.</li> 
 <li>Utilize o atributo &quot;async&quot; para carregar c&oacute;digos JavaScript. Isso faz com que todo o carregamento e execu&ccedil;&atilde;o do script seja feito de maneira ass&iacute;ncrona.</li> 
 <li>Evite c&oacute;digo duplicado. 52% das p&aacute;ginas web do mundo inteiro cont&ecirc;m 100 ou mais linhas de c&oacute;digo duplicadas, por exemplo vinculando o mesmo arquivo JavaScript duas vezes.</li> 
 <li>Padronize a utiliza&ccedil;&atilde;o de um framework JavaScript, seja ele jQuery, Dojo, Prototype etc. Dessa maneira o navegador n&atilde;o ter&aacute; que carregar m&uacute;ltiplos frameworks para fornecer as mesmas funcionalidades.</li> 
 <li>N&atilde;o carregue scripts - como do Facebook, Twitter ou outros - s&oacute; para &quot;estar na moda&quot;. Eles competem por recursos.</li> 
</ul> 
<p><strong>4. Otimizar o uso de m&iacute;dias.</strong> Imagens s&atilde;o os recursos mais utilizados, sendo que em m&eacute;dia um website efetua download de 58 imagens.</p> 
<ul> 
 <li>Evite efetuar o download de muitas imagens, mantendo o n&uacute;mero m&aacute;ximo entre 20 e 30, devido ao tempo de carregamento da p&aacute;gina.</li> 
 <li>Utilize <a href="http://www.w3schools.com/css/css_image_sprites.asp">sprites</a> para combinar diversas imagens em uma &uacute;nica imagem. Essa t&eacute;cnica reduz o n&uacute;mero de conex&otilde;es de rede, o n&uacute;mero de bytes trafegados e o n&uacute;mero de ciclos de GPU.</li> 
 <li>Crie sprites manualmente, pois ferramentas podem deixar grandes espa&ccedil;os em branco, gerando maiores tempos de download e mais ciclos de GPU.</li> 
 <li>Utilize imagens do tipo PNG, que oferecem a melhor rela&ccedil;&atilde;o entre tamanho do download, tempo de codifica&ccedil;&atilde;o, compatibilidade e taxa de compress&atilde;o. Imagens JPEG podem ser utilizadas para fotografias.</li> 
 <li>Utilize a resolu&ccedil;&atilde;o de imagens nativas para evitar que o download e consumo de CPU desnecess&aacute;rios, aumentando a escalabilidade.</li> 
 <li>Sempre que poss&iacute;vel substitua imagens por gradientes do CSS3.</li> 
 <li>Sempre que poss&iacute;vel substitua imagens por bordas arredondadas do CSS3.</li> 
 <li>Utilize transforma&ccedil;&otilde;es do CSS3 para criar movimentos, rota&ccedil;&otilde;es ou inclina&ccedil;&otilde;es.</li> 
 <li>Utilize <a href="http://www.google.com/url?q=http%3A%2F%2Fen.wikipedia.org%2Fwiki%2FData_URI_scheme&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNEcq3M_6lBncTAs2_K7N3JNUweDyA">Data URI</a> para pequenas imagens sozinha. Esse recurso elimina a necessidade de um download adicional para a imagem.</li> 
 <li>Evite a utiliza&ccedil;&atilde;o de arquivos SVG complexos, pois eles exigem downloads mais demorados e processamento adicional.</li> 
 <li>Especifique uma &quot;imagem de capa&quot; quando utilizar v&iacute;deos com HTML5. Dessa maneira, o navegador n&atilde;o ter&aacute; que baixar todo o v&iacute;deo para descobrir a imagem inicial.</li> 
 <li>Utilize HTML5 ao inv&eacute;s de Flash, Silverlight ou Quicktime. O HTML5 &eacute; mais r&aacute;pido e o ambiente de execu&ccedil;&atilde;o de plug-in consome recursos do sistema.</li> 
 <li>Efetue download de m&iacute;dias ricas proativamente, de maneira ass&iacute;ncrona, e mantenha as m&iacute;dias no cache da aplica&ccedil;&atilde;o.</li> 
</ul> 
<p><strong>5. Escreva c&oacute;digo JavaScript de alto desempenho</strong></p> 
<ul> 
 <li>Utilize inteiros ao executar opera&ccedil;&otilde;es matem&aacute;ticas em JavaScript, sempre que poss&iacute;vel. Opera&ccedil;&otilde;es de ponto flutuante demoram muito mais tempo para executar do que as equivalentes utilizando inteiros. Converta pontos flutuantes para inteiros utilizando os m&eacute;todos Math.floor e Math.ceil, especialmente para opera&ccedil;&otilde;es computacionalmente intensas.</li> 
 <li>Minifique c&oacute;digo JavaScript para reduzir o tamanho dos downloads e obter melhor performance em tempo de execu&ccedil;&atilde;o.</li> 
 <li>Inicialize o c&oacute;digo JavaScript sob demanda. Carregue o c&oacute;digo JavaScript dinamicamente quando for necess&aacute;rio.</li> 
 <li>Minimize intera&ccedil;&otilde;es com o DOM, efetuando cache de vari&aacute;veis como document, body, etc.</li> 
 <li>Utilize c&oacute;digo de manipula&ccedil;&atilde;o do DOM interno, como element.firstChild ou node.nextSbiling. A performance desse c&oacute;digo &eacute; melhor do que uma biblioteca de terceiros pode proporcionar.</li> 
 <li>Utilize querySelectorAll para acessar uma grande quantidade de elementos do DOM.</li> 
 <li>Utilize a propriedade .innerHTML para construir p&aacute;ginas dinamicamemte.</li> 
 <li>Execute altera&ccedil;&otilde;es no HTML de maneira agrupada, sempre que poss&iacute;vel</li> 
 <li>Mantenha o DOM pequeno e bem organizado, com o m&aacute;ximo de 1.000 elementos.</li> 
 <li>O JSON &eacute; mais r&aacute;pido que XML.</li> 
 <li>Utilize os m&eacute;todos nativos do navegador para trabalhar com JSON.</li> 
 <li>N&atilde;o exagere no uso de express&otilde;es regulares.</li> 
</ul> 
<p><strong>6. Entenda o que a sua aplica&ccedil;&atilde;o est&aacute; fazendo</strong></p> 
<ul> 
 <li>Entenda os temporizadores (timers) do JavaScript: setTimeout e clearInterval. N&atilde;o deixe esses timers serem executados ao menos que sejam realmente necess&aacute;rios. Tamb&eacute;m os combine para obter melhores resultados.</li> 
 <li>Alinhe os temporizadores &agrave; tela de exibi&ccedil;&atilde;o em 16.7 milisegundos, se o monitor atualizar a 60 Hz.</li> 
 <li>Utilize o requestAnimationFrame para anima&ccedil;&otilde;es, quando for trabalhar com gr&aacute;ficos no IE 10/Chrome/Firefox. Esse recurso faz uso de callbacks para desenhar a tela, eliminando a necessidade de um timer.</li> 
 <li>Utilize a API de visibilidade (document.hidden, Visibilityhange) para determinar o estado de visibilidade da aplica&ccedil;&atilde;o, e controle o fluxo de atividades, quando a p&aacute;gina n&atilde;o estiver vis&iacute;vel. Essa estrat&eacute;gia economiza CPU e bateria.</li> 
</ul> 
<p>Jatinder Mann recomenda, ainda, a utiliza&ccedil;&atilde;o da ferramenta <a href="http://www.google.com/url?q=http%3A%2F%2Fmsdn.microsoft.com%2Fen-us%2Fperformance%2Fcc825801.aspx&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNH4VUVdczDNscVRaqD7_GIimqdeuA">Windows Performance Tools</a> para medir a performance de p&aacute;ginas no Internet Explorer e otimiz&aacute;-las para menor consumo de CPU e aumentar o paralelismo.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
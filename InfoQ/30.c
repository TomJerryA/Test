<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>MongoDB 2.4: busca textual, sharding e mais</h3><p>O time de desenvolvimento do MongoDB <a href="http://docs.mongodb.org/manual/release-notes/2.4/">anunciou</a> a vers&atilde;o 2.4 de seu banco de dados NoSQL, agora com a fun&ccedil;&atilde;o de busca textual, uma das funcionalidades mais esperadas para o projeto. A funcionalidade, ainda em beta, inclui o tratamento de &iacute;ndices de texto, diferencia&ccedil;&atilde;o de mai&uacute;sculas e min&uacute;sculas e omiss&atilde;o de palavras comuns de um idioma (<a href="http://searchenginewatch.com/article/2049138/What-Are-Stop-Words">stop words</a>).</p> 
<p>Outra caracter&iacute;stica importante lan&ccedil;ada nesta vers&atilde;o &eacute; a utiliza&ccedil;&atilde;o de &iacute;ndices hash e sharding. O <a href="http://docs.mongodb.org/manual/core/sharded-cluster-internals/">sharding</a> baseado em hashes permite que os dados e a carga da CPU sejam distribu&iacute;dos entre os n&oacute;s do banco de dados de forma simplificada. Os desenvolvedores do MongoDB recomendam a utiliza&ccedil;&atilde;o dessas funcionalidades para os casos de documentos acessados ​​aleatoriamente ou padr&otilde;es de acesso imprevis&iacute;veis.</p> 
<p>A nova vers&atilde;o inclui tamb&eacute;m:</p> 
<ul> 
 <li>Novos &iacute;ndices Geoespaciais com suporte para <a href="http://geojson.org/geojson-spec.html">GeoJSON</a> e <a href="http://docs.mongodb.org/manual/reference/operator/nearSphere/">geometria esf&eacute;rica</a>;</li> 
 <li>A implementa&ccedil;&atilde;o de um novo sistema de autentica&ccedil;&atilde;o modular;</li> 
 <li>Um sistema de controle de acesso baseado em pap&eacute;is (roles) e a capacidade de ter documentos do tipo &quot;apenas usu&aacute;rios com privil&eacute;gio podem acessar&quot;;</li> 
 <li>Aumento do processamento JavaScript do MongoDB no mapReduce com a substitui&ccedil;&atilde;o da antiga engine SpiderMonkey para o JavaScript V8;</li> 
 <li>Suporte a matrizes de tamanho fixo em documentos;</li> 
 <li>Otimiza&ccedil;&atilde;o do desempenho de contagem no mecanismo de execu&ccedil;&atilde;o al&eacute;m da adi&ccedil;&atilde;o de um analisador de tamanho de conjunto de trabalho com o objetivo de tornar mais f&aacute;cil a medi&ccedil;&atilde;o dos recursos utilizados.</li> 
</ul> 
<p>Para mais detalhes sobre estas e outras mudan&ccedil;as no MongoDB 2.4, consulte as <a href="http://docs.mongodb.org/manual/release-notes/2.4/">notas de lan&ccedil;amento</a>, que incluem detalhes sobre como atualizar para a vers&atilde;o 2.4 a partir de vers&otilde;es anteriores. Usu&aacute;rios Mac OS X devem observar que apenas a partir da vers&atilde;o 10.6 (Snow Leopard), a nova vers&atilde;o do MongoDB &eacute; suportada.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Pesquisadores expõem vulnerabilidades do SSL</h3><p>Pesquisadores da Universidade do Texas em Austin e da Universidade Stanford <a href="http://www.cs.utexas.edu/~shmat/shmat_ccs12.pdf">publicaram os resultados de uma pesquisa</a> que exp&otilde;e vulnerabilidades cr&iacute;ticas no uso de bibliotecas SSL em aplica&ccedil;&otilde;es &quot;n&atilde;o-browser&quot;, antes consideradas altamente seguras. Esses softwares s&atilde;o usados em servi&ccedil;os cr&iacute;ticos banc&aacute;rios e SDKs para com&eacute;rcio eletr&ocirc;nico, al&eacute;m de softwares menos cr&iacute;ticos como armazenamento na nuvem e mensageria. A pesquisa coloca a culpa nos pobres testes de adversidades, bibliotecas de SSL inseguras, uso programa&ccedil;&atilde;o insegura das bibliotecas SSL, complexidade na resolu&ccedil;&atilde;o de problemas escondidos profundamente na pilha de erros e na pr&aacute;tica de desabilitar a valida&ccedil;&atilde;o dos certificados pelos desenvolvedores.</p> 
<p>A amea&ccedil;a modelo usada pelo time &eacute; um ataque do tipo <a href="http://pt.wikipedia.org/wiki/Ataque_man-in-the-middle">man-in-the-middle</a>. O ataque simulado usou tr&ecirc;s certificados: (1) um auto-assinado com os mesmos nomes usados pelo servidor ao qual o cliente desejava se conectar, (2) um certificado auto-assinado com um nome incorreto; e (3) e um certificado v&aacute;lido emitido por uma autoridade confi&aacute;vel para um dom&iacute;nio chamado AllYourSSLAreBelongTo.us. Os ataques man-in-the-middle focaram na cadeia de verifica&ccedil;&atilde;o de confian&ccedil;a e do nome do servidor mas n&atilde;o testaram a revoga&ccedil;&atilde;o do certificado e as extens&otilde;es X.509. O c&oacute;digo para o modelo de simula&ccedil;&atilde;o do ataque pode ser <a href="https://cs.utexas.edu/~georgiev/publications/ccs2012/MITM.zip">baixado aqui</a>.</p> 
<p>A pesquisa mostra detalhes relevantes para desenvolvedores que utilizam bibliotecas SSL: OpenSSL e JSSE e bibliotecas de transporte de dados: Apache HttpClient, Weberknecht, cURL, o m&eacute;todo fsocketopen do PHP, a t&eacute;cnica de cURL binding e certas bibliotecas do Python: urllib, urllib2 e httplib. A maioria das bibliotecas SSL executam verifica&ccedil;&atilde;o de certificados, mas deixam para o cliente algumas op&ccedil;&otilde;es abertas quanto &agrave; verifica&ccedil;&atilde;o do nome do servidor, que em geral &eacute; ignorada pela maioria dos desenvolvedores. Por exemplo, na API de baixo n&iacute;vel do JSSE, a classe SLSocketFactory automaticamente desliga a verifica&ccedil;&atilde;o do nome do servidor se o campo algoritmo for nulo. Maioria dos clientes n&atilde;o implementam seus pr&oacute;prios esquemas de verifica&ccedil;&atilde;o do nome do servidor incluindo o Apache HttpClient, o que traz riscos de seguran&ccedil;a. O seguinte trecho de c&oacute;digo elucida esse fato:</p> 
<pre>
private void checkTrusted(X509Certificate[] chain, String authType, Socket socket, boolean isClient)
throws CertificateException {
    ...
    String identityAlg = sslSocket.getSSLParameters().
    getEndpointIdentificationAlgorithm();
    if (identityAlg != null &amp;&amp; identityAlg.length != 0)
      {
      String hostname = session.getPeerHost();
      checkIdentity(hostname, chain[0], identityAlg);
      }
}
</pre> 
<p>Tais vulnerabilidades infiltram-se em qualquer aplica&ccedil;&atilde;o n&atilde;o-browser usando essas bibliotecas. Para uma recomenda&ccedil;&atilde;o espec&iacute;fica da correta implementa&ccedil;&atilde;o de clientes usando SSL e de biblioteca de transporte de dados vejam a <a href="https://docs.google.com/document/pub?id=1roBIeSJsYq3Ntpf6N0PIeeAAvu4ddn7mGo6Qb7aL7ew">FAQ fornecida pelos autores da pesquisa</a>.</p> 
<p>Metade da pesquisa discute os resultados de ataques simulados contra APIs de clientes de nuvem (AWS EC2, e ferramentas de API ELB), Apps (Chase mobile banking, Rackspace IOS, Groupon, TextSecure), SDKs (Amazon Flexible Payments Service, PayPal Payments Standards), middleware de Web Services (Apache Axis, Axis2, CodeHaus XFire e Pusher) e an&uacute;ncios mobile (AdMob). A pesquisa conclui com as seguintes recomenda&ccedil;&otilde;es aos desenvolvedores de aplica&ccedil;&otilde;es:</p> 
<blockquote> 
 <p>FA&Ccedil;AM <a href="http://pt.wikipedia.org/wiki/Fuzzing">Fuzzing</a> (blackbox, se necess&aacute;rio) e testes de adversidade para ver como a aplica&ccedil;&atilde;o se comporta quando apresentada a um certificado SSL anormal. Mesmo quando as vulnerabilidades s&atilde;o sutis, os sintomas geralmente n&atilde;o s&atilde;o. Em v&aacute;rios dos nossos casos de estudo, ficou &oacute;bvio que o software em quest&atilde;o nunca tinha sido testado com qualquer outro certificado que n&atilde;o do servidor desejado. Quando apresentados a um certificado emitido para AllYourSSLAreBelongTo.us ao inv&eacute;s do certificado esperado da Amazon, PayPal ou Chase, esses servidores estabeleceram conex&otilde;es SSL e entregaram seus segredos. Essas vulnerabilidades deveriam ter sido observadas durante os testes.</p> 
 <p>N&Atilde;O modifique o c&oacute;digo da aplica&ccedil;&atilde;o ou desabilite a valida&ccedil;&atilde;o do certificado para testar com certificados auto-assinados e/ou n&atilde;o confi&aacute;veis. Encontramos, nos nossos casos de estudo, muitos desenvolvedores que esqueceram de reverter essas modifica&ccedil;&otilde;es, mesmo em vers&otilde;es para produ&ccedil;&atilde;o. Em vez disso, crie uma keystore tempor&aacute;ria contendo uma chave publica de um CA n&atilde;o confi&aacute;vel. Enquanto testa sua aplica&ccedil;&atilde;o com seu certificado auto-assinado ou n&atilde;o confi&aacute;vel, use essa keystore como sua keystore confi&aacute;vel.</p> 
 <p>N&Atilde;O dependa dos padr&otilde;es da biblioteca para configurar uma conex&atilde;o SSL de maneira segura. Configura&ccedil;&otilde;es padr&atilde;o podem e devem mudar entre as bibliotecas diferentes ou mesmo entre vers&otilde;es diferentes da mesma biblioteca; por exemplo, a cURL antes da vers&atilde;o 7.10 n&atilde;o validava os certificados por padr&atilde;o, mas a partir da vers&atilde;o 7.10 e superior essa a&ccedil;&atilde;o &eacute; realizada. Sempre explicite o conjunto de op&ccedil;&otilde;es necess&aacute;rias para estabelecimento de uma conex&atilde;o segura.</p> 
</blockquote> 
<p>E para os desenvolvedores de bibliotecas SSL:</p> 
<blockquote> 
 <p>FA&Ccedil;AM bibliotecas SSL mais expl&iacute;citas quanto &agrave; sem&acirc;ntica de suas APIs. Em muitos casos &eacute; &oacute;bvio que os desenvolvedores de aplica&ccedil;&otilde;es n&atilde;o entenderam o significado de v&aacute;rias op&ccedil;&otilde;es e par&acirc;metros. Por exemplo, as bibliotecas de PHP para a Amazon Flexible Payments Services e a PayPal Payments Standard tentam habilitar a valida&ccedil;&atilde;o do nome do servidor no cURL, mas acidentalmente sobrescrevem o valor padr&atilde;o correto e o desabilitam (Se&ccedil;&otilde;es 7.1 e 7.2). Isso mostra que mesmo valores padr&atilde;o seguros podem ser insuficientes. O Lynx tenta verificar certificados auto-assinados, mas confunde o significado do retorno da valida&ccedil;&atilde;o da fun&ccedil;&atilde;o de verifica&ccedil;&atilde;o de certifica&ccedil;&atilde;o do GnuTLS, e o teste nunca &eacute; executado (Se&ccedil;&atilde;o 7.4).</p> 
 <p>N&Atilde;O delegue a responsabilidade pelo gerenciamento das conex&otilde;es SSL &agrave;s aplica&ccedil;&otilde;es. As bibliotecas SSL existentes exp&otilde;em muitas op&ccedil;&otilde;es para aplica&ccedil;&otilde;es de alto n&iacute;vel. Isso &eacute; muito perigoso. Os desenvolvedores de aplica&ccedil;&otilde;es podem n&atilde;o perceber que devem escolher explicitamente certas op&ccedil;&otilde;es para habilitar a valida&ccedil;&atilde;o dos certificados. Ao mesmo tempo, as bibliotecas devem utilizar op&ccedil;&otilde;es padr&atilde;o seguras tanto quanto for poss&iacute;vel. Al&eacute;m disso, n&atilde;o devem pular funcionalidades importantes como verifica&ccedil;&atilde;o do nome do servidor como faz o JSSE quando o campo algoritmo &eacute; nulo ou uma string vazia. Ao contr&aacute;rio, devem disparar uma Runtime Exception ou informar a aplica&ccedil;&atilde;o de alguma outra forma.</p> 
 <p>FA&Ccedil;AM um desenho claro e consistente da interface de relato de erros. Bibliotecas como OpenSSL e GnuTLS relatam alguns erros via retorno de valores de fun&ccedil;&atilde;o, enquanto outros erros da mesma fun&ccedil;&atilde;o s&atilde;o relatados por uma flag passada como argumento. Interfaces inconsistentes confundem os desenvolvedores, que ent&atilde;o erroneamente omitem algumas checagem de erros nas suas aplica&ccedil;&otilde;es.</p> 
</blockquote> 
<p>Algumas empresas e organiza&ccedil;&otilde;es est&atilde;o trabalhando nas falhas apontadas na pesquisa e est&atilde;o relatando os resultados de volta aos pesquisadores, que os est&atilde;o publicando na FAQ. Para o benef&iacute;cio dos desenvolvedores que lidam com SSL, a ISec Partners tinha <a href="https://www.isecpartners.com/blog/2012/10/14/the-lurking-menace-of-broken-tls-validation.html">liberado</a> tr&ecirc;s ferramentas que testam as vulnerabilidades expostas na pesquisa.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
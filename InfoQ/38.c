<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>WildFly 8: suporte total ao Java EE 7 e novo Web Server embarcado</h3><p>A divis&atilde;o JBoss da Red Hat <a href="http://wildfly.org/news/2014/02/11/WildFly8-Final-Released/">anunciou</a> a disponibilidade do <a href="http://wildfly.org">WildFly 8</a>, antes conhecido como JBoss Application Server. Esta vers&atilde;o est&aacute; certificada para o Java EE7, suportando ambos Web e Full profiles. O WildFly tamb&eacute;m ganhou um novo servidor web completo chamado Undertow, novos recursos de seguran&ccedil;a, e um sistema de corre&ccedil;&atilde;o para atualiza&ccedil;&otilde;es com o sistema em funcionamento.</p>
<p>O Undertow &eacute; um container Servlet 3.1 e um servidor para a interface de administra&ccedil;&atilde;o HTTP. O novo container inclui suporte para o <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.42">HTTP Upgrade</a> − Parte do HTTP /1.1 RFC, que permite uma conex&atilde;o HTTP para ser atualizado para outro protocolo. O uso mais comum &eacute; para iniciar uma conex&atilde;o web socket que permite que navegadores e outros clientes iniciem uma comunica&ccedil;&atilde;o full duplex.</p>
<p>Como o HTTP Upgrade permite multiplexar v&aacute;rios protocolos em uma &uacute;nica porta HTTP, elimina-se a necessidade de m&uacute;ltiplas portas e simplifica a configura&ccedil;&atilde;o de firewall. O WildFly usa somente duas portas: as chamadas JNDI e EJB s&atilde;o multiplexadas sobre a porta 8080 do subsistema Undertow, e o gerenciamento &eacute; multiplexado sobre a porta de gerenciamento web (9090).</p>
<p>O exemplo a seguir apresenta como &eacute; uma requisi&ccedil;&atilde;o inicial do EJB, uma vez que a conex&atilde;o &eacute; estabelecida:</p>
<pre>
GET / HTTP/1.1
Host: example.com
Upgrade: jboss-remoting
Connection: Upgrade
Sec-JbossRemoting-Key: dGhlIHNhbXBsZSBub25jZQ==
</pre>
<p>O Undertow, ent&atilde;o responde ao cliente dizendo que o upgrade &eacute; permitido e completou:</p>
<pre>
HTTP/1.1 101 Switching Protocols
Upgrade: jboss-remoting
Connection: Upgrade
Sec-JbossRemoting-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
</pre>
<p>Depois que o socket &eacute; passado para a camada EJB do WildFly seu funcionamento &eacute; como o de uma conex&atilde;o normal EJB.</p>
<p>Existe uma pequena sobrecarga de desempenho para processar a requisi&ccedil;&atilde;o HTTP inicial, mas uma vez feita, o desempenho deve ser exatamente o mesmo, e uma vez que o n&uacute;mero de portas necess&aacute;rias atualmente &eacute; menor o efeito global esperado &eacute; ben&eacute;fico. Jason Greene, l&iacute;der do WildFly e arquiteto da plataforma JBoss EAP na divis&atilde;o JBoss da Red Hat disse ao InfoQ.com:</p>
<blockquote> 
 <p>H&aacute; uma sobrecarga adicional na conex&atilde;o uma vez que precisamos processar uma requisi&ccedil;&atilde;o HTTP. No entanto, a efici&ecirc;ncia que o Undertow mant&eacute;m est&aacute; muito baixa. Ap&oacute;s a requisi&ccedil;&atilde;o de upgrade ter sido executada o socket se comporta exatamente como no cen&aacute;rio n&atilde;o HTTP, assim as sem&acirc;nticas de desempenho s&atilde;o exatamente as mesmas a partir desse ponto. Uma vez que o impacto &eacute; t&atilde;o baixo, deixamos est&aacute; configura&ccedil;&atilde;o por padr&atilde;o. De forma inovadora, o WildFly 8 s&oacute; possui 2 portas HTTP, uma para o gerenciamento e uma para uso da aplica&ccedil;&atilde;o. Todos os outros protocolos reutilizam essas portas.</p> 
</blockquote>
<p>O Undertow tamb&eacute;m foi concebido para ser usado de modo embarcado. Existe uma API que pode ser usada para construir o servidor e registrar um manipulador HTTP, que processa as requisi&ccedil;&otilde;es de uma forma sem bloqueio. A seguir temos um exemplo do site <a href="http://undertow.io">undertow.io</a>:</p>
<pre>
public class HelloWorldServer {
    public static void main(final String[] args) {
        Undertow server = Undertow.builder()
                .addListener(8080, &quot;localhost&quot;)
                .setHandler(new HttpHandler() {
                    @Override
                    public void handleRequest(final HttpServerExchange exchange) throws Exception {
                        exchange.getResponseHeaders().put(Headers.CONTENT_TYPE, &quot;text/plain&quot;);
                        exchange.getResponseSender().send(&quot;Hello World&quot;);
                    }
                }).build();
        server.start();
    }
}
</pre>
<p>O Undertow tamb&eacute;m permite inserir o c&oacute;digo com base na API Servlet e existem alguns exemplos no <a href="https://github.com/undertow-io/undertow/blob/master/examples/src/main/java/io/undertow/examples/servlet/ServletServer.java">GitHub</a>.</p>
<p>Assim como o novo servidor web, o WildFly 8 tem melhorias de seguran&ccedil;a consider&aacute;veis​​, com a adi&ccedil;&atilde;o de log de auditoria e regra baseada no modelo de seguran&ccedil;a.</p>
<p>O sistema de auditoria foi concebido para assegurar que qualquer opera&ccedil;&atilde;o contra o modelo de gerenciamento fique gravado no log que pode ser escrito no arquivo local ou no servidor.</p>
<p>O WildFly vem com dois provedores de controle de acesso − o &quot;simples&quot; que &eacute; equivalente ao encontrado no AS 7, sendo tudo ou nada; embora o modelo <a href="http://pt.wikipedia.org/wiki/Role-based_access_control">Permiss&otilde;es com Base no Controle de Acesso (Role Based Access Control - RBAC)</a> permite que diferentes administradores tenham diferentes permiss&otilde;es (por exemplo, uma permiss&atilde;o de monitoramento versus permiss&atilde;o de atualiza&ccedil;&atilde;o).</p>
<p>O WildFly vem com sete permiss&otilde;es pr&eacute;-definidas RBAC:</p>
<ol start="1"> 
 <li><strong>Monitor</strong>: Tem a menor quantidade de permiss&otilde;es. Pode ler as configura&ccedil;&otilde;es e o estado atual de execu&ccedil;&atilde;o, n&atilde;o pode ler os recursos ou informa&ccedil;&otilde;es confidenciais, e n&atilde;o pode ler o log de auditoria e recursos relacionados.</li> 
 <li><strong>Operator</strong>: Tem todas as permiss&otilde;es que o perfil monitor tem. Adicionalmente pode modificar o estado em tempo de execu&ccedil;&atilde;o − recarregar ou desligar o servidor, pausar/retomar uma fila JMS. Um operator n&atilde;o pode modificar configura&ccedil;&otilde;es persistentes.</li> 
 <li><strong>Maintainer</strong>: Tem todas as permiss&otilde;es do operador. Pode modificar as configura&ccedil;&otilde;es persistentes para implantar uma aplica&ccedil;&atilde;o, adicionar um destino JMS e assim por diante. O maintainer pode editar quase todas as configura&ccedil;&otilde;es associadas com o servidor e suas implanta&ccedil;&otilde;es. Entretanto, o maintainer n&atilde;o pode ler ou modificar informa&ccedil;&otilde;es sens&iacute;veis (como senhas), e n&atilde;o pode ler ou modificar informa&ccedil;&otilde;es de auditoria.</li> 
 <li><strong>Deployer</strong>: O mesmo que o maitainer, mas tamb&eacute;m &eacute; limitado apenas a altera&ccedil;&otilde;es relacionadas &agrave; implanta&ccedil;&atilde;o. Um deployer n&atilde;o pode alterar configura&ccedil;&otilde;es gerais do servidor.</li> 
 <li><strong>Administrator</strong>: Pode visualizar e modificar informa&ccedil;&otilde;es sensitivas como senhas, configura&ccedil;&otilde;es de seguran&ccedil;a do dom&iacute;nio. Entretanto, n&atilde;o pode fazer nada com o log de auditoria.</li> 
 <li><strong>Auditor</strong>: Tem todas as permiss&otilde;es do monitor. Essencialmente um perfil apenas de leitura, mas pode visualizar e modificar as configura&ccedil;&otilde;es relacionadas ao sistema de log de auditoria.</li> 
 <li><strong>SuperUser</strong>: Equivalente ao administrador no AS 7 e tem todas as permiss&otilde;es.</li> 
</ol>
<p>O dados RBCA podem ser armazenados em praticamente qualquer servidor LDAP, incluindo o Active Directory.</p>
<p>WildFly tamb&eacute;m inclui um novo sistema aplica&ccedil;&atilde;o de corre&ccedil;&otilde;es originalmente desenvolvidas para o JBoss EAP. O sistema permite implantar uma corre&ccedil;&atilde;o do JBoss remotamente ou localmente. A publica&ccedil;&atilde;o realizada no ambiente de execu&ccedil;&atilde;o armazena o patch, mas &eacute; necess&aacute;rio reiniciar a aplica&ccedil;&atilde;o para surtir efeito.</p>
<p>Finalmente, enquanto WildFly est&aacute; focado inicialmente no suporte ao Java EE, o mesmo pode ser usado para outras linguagens e ambientes. Por exemplo, o projeto <a href="http://torquebox.org">TorqueBox</a> permite que projetos Ruby on Rails possam ser executados no servidor.</p>
<p>&Eacute; poss&iacute;vel encontrar mais informa&ccedil;&otilde;es no <a href="http://wildfly.org">site do WildFly</a> e tamb&eacute;m nesta <a href="http://wildfly.org/news/2013/11/21/WildFly-8-Webinar/">grava&ccedil;&atilde;o webinar</a>. O InfoQ tamb&eacute;m tem uma <a href="http://www.infoq.com/news/2014/02/wildfly8-interview">entrevista mais extensiva</a> com Jason Greene, na qual entre outras coisas, discutimos alguns dos antecedentes de Undertow, o novo sistema de log de auditoria e o impacto da decis&atilde;o da Oracle em <a href="http://www.infoq.com/news/2013/11/glassfish-commercial-dead/">acabar com o suporte comercial</a> para o GlassFish.</p><br><br><br><br><br><br></body></html>
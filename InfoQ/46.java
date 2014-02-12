<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Red Hat's JBoss Team Launch WildFly 8 with full Java EE 7 Support and a New Embeddable Web Server</h3><p>Red Hat's JBoss division has today <a href="http://wildfly.org/news/2014/02/11/WildFly8-Final-Released/">announced</a> the availability of <a href="http://wildfly.org">WildFly 8</a>, the product formerly know as JBoss Application Server. This release is Java EE7 certified, supporting both the Web and the Full profiles. WildFly also gains a completely new web server called Undertow, new security features, and a patching system for updates to the running system.</p>
<p>Undertow is a Servlet 3.1 container. It is also the server for the HTTP management interface. The new product includes support for <a href="http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.42">HTTP Upgrade</a> - Part of the HTTP/1.1 RFC - which allows an HTTP connection to be upgraded to another protocol. The most common use is to initiate a web socket connection which allows browsers and other clients to initiate a full duplex connection.</p>
<p>Since HTTP Upgrade allows you to multiplex several protocols over a single HTTP port, it removes the need for multiple ports and makes firewall configuration simpler. WildFly itself uses only two ports:&nbsp;JNDI&nbsp;and EJB calls are multiplexed over the undertow subsystem port 8080, and management is multiplexed over the web management port (9090).</p>
<p>As an example, this is what an initial EJB request looks like on the wire once the connection is established:</p>
<pre>
GET / HTTP/1.1<br />Host: example.com<br />Upgrade: jboss-remoting<br />Connection: Upgrade<br />Sec-JbossRemoting-Key: dGhlIHNhbXBsZSBub25jZQ==</pre>
<p>Undertow then replies to the client saying the upgrade is allowed and completed:</p>
<pre>
HTTP/1.1 101 Switching Protocols<br />Upgrade: jboss-remoting<br />Connection: Upgrade<br />Sec-JbossRemoting-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=</pre>
<p>After that the socket is passed off to the WildFly EJB layer and it behaves as a normal EJB connection.</p>
<p>There is a small performance overhead to process this initial HTTP request, but once that is done the performance should be exactly the same, and since the number of ports you need is actually smaller the overall effect is expected to be beneficial. Jason Greene, WildFly Lead / JBoss EAP Platform Architect at Red Hat's JBoss division told InfoQ</p>
<blockquote> 
 <p>There is some additional overhead in establishment since you need to process an HTTP request. However, Undertow's efficiency keeps this very low. After the upgrade request has been fulfilled the socket behaves exactly as it would in a non-HTTP setting, so the performance semantics are exactly the same from that point on. Since the impact is so low, we have made this the default setting. Out of the box, WildFly 8 only has 2 HTTP ports, one for management, and one for application usage. All other protocols reuse these ports.</p> 
</blockquote>
<p>Undertow is also designed to be used in embedded mode. There is a chained builder API that you can use to construct the server and register an HTTP handler, which processes requests in a non-blocking fashion. Here's an example from the <a href="http://undertow.io">undertow.io</a> website</p>
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
<p>Undertow also allows you to embed code based on the Servlet API, and there are some examples in <a href="https://github.com/undertow-io/undertow/blob/master/examples/src/main/java/io/undertow/examples/servlet/ServletServer.java">GitHub</a>.</p>
<p>As well as the new web server, WildFly 8 has considerable security improvements with the addition of both audit logging and a role based security model.</p>
<p>The audit system is designed to ensure that any operation against the management model gets recorded in the log which can be written either to a local file or a server.</p>
<p>WildFly ships with two access control providers - the &quot;simple&quot; one is equivalent to that provided in AS 7 and is very much all or nothing, whilst the Role Based Access Control model (RBAC) one allows different administrators to have different permissions (for example a monitoring role vs. an update role).</p>
<p>WildFly ships with 7 pre-defined RBAC roles:</p>
<ol> 
 <li><strong>Monitor</strong>: Has fewest permissions. Can read configuration and current runtime state, cannot read sensitive resources or data, and cannot read the audit log and related resources.</li> 
 <li><strong>Operator</strong>: Has all the permissions of the monitor role. Additionally, can modify the runtime state - reload or shutdown a server, pause/resume a JMS destination. An operator cannot modify persistent configuration.</li> 
 <li><strong>Maintainer</strong>: All the permissions of the operator role. Can modify persistent configuration so can deploy an application, add a JMS destination and so on. The maintainer role can edit almost all configuration associated with the server and its deployments. However, the maintainer cannot read or modify sensitive information (like passwords), and cannot read or modify audit information.</li> 
 <li><strong>Deployer</strong>: Much the same as the maintainer, but is also limited to just deployment related changes. A deployer cannot alter general server configuration.</li> 
 <li><strong>Administrator</strong>: Can see and modify sensitive information such as passwords, security domain settings. However, cannot do anything with the audit log.</li> 
 <li><strong>Auditor</strong>: Has all the permissions of the monitor role. Essentially a read-only role but can view and modify settings related to the audit logging system.</li> 
 <li><strong>SuperUser</strong>: Equivalent to AS 7 administrator, and has full permissions.</li> 
</ol>
<p>RBAC data can be stored in pretty much any LDAP server including Active Directory.</p>
<p>WildFly also includes a new patching system originally developed for JBoss EAP. The system allows you to deploy a JBoss produced patch either remotely or locally. Deploying against a running system stages the patch but a restart is required for it to take effect.</p>
<p>Finally, whilst WildFly is primarily focussed on supporting Java EE it can be used for other languages and environments. For example the <a href="http://torquebox.org">TorqueBox</a> project allows Ruby on Rails to be run on the server.</p>
<p>You can find out more from the <a href="http://wildfly.org">WildFly website</a>&nbsp;and via this <a href="http://wildfly.org/news/2013/11/21/WildFly-8-Webinar/">webinar recording</a>. InfoQ also has a more <a href="http://www.infoq.com/news/2014/02/wildfly8-interview">extensive interview</a> with Jason Greene where, amongst other things, we discuss some of the background to Undertow, the new audit logging system, and the impact of Oracle's decision <a href="http://www.infoq.com/news/2013/11/glassfish-commercial-dead/"> to kill off commercial support</a> for GlassFish.</p><br><br><br><br><br><br></body></html>
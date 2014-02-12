<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Interview with WildFly Lead Jason Greene on WildFly 8</h3><p>Red Hat's JBoss division has today announced the availability of WildFly 8, the product formerly know as JBoss Application Server, as we <a href="http://www.infoq.com/news/2014/02/wildfly8-launch">reported elsewhere</a>. InfoQ spoke to Jason Greene, WildFly Lead / JBoss EAP Platform Architect at Red Hat's JBoss division to find out more about the new product. Since WildFly includes a brand new web server (Undertow), a major undertaking, we started by asking Greene what had led to that decision.</p>
<blockquote> 
 <p>Well as you know web applications have evolved dramatically over these last few years, and they are placing greater demands than ever on web servers. Due to the growth of computing devices, web applications are seeing dramatically more clients, and the desire for rich interfaces has led to more frequent and more data-oriented traffic. Full duplex communication using technologies like WebSockets is already a common practice. We felt the best solution was a high-performance server designed from the ground up to meet these challenges.</p> 
 <p>In addition to meeting the needs of modern applications, we also wanted to address the infrastructure oriented problems typically solved using alternative native web servers. As an example, with Undertow WildFly can now function as an efficient non-blocking reverse proxy without the need for Apache or Nginx.</p> 
 <p>Another factor was the desire to reduce the number of ports in a cloud environment where hundreds or even thousands of WildFly instances can be running on the same system. Undertow gave us the ability to multiplex the various protocols we support over HTTP using HTTP Upgrade.</p> 
 <p>Finally, it gave us an opportunity to build something very developer friendly that goes beyond the capabilities of the Servlet spec. The resulting project is tiny with very few dependencies, it has a lightweight memory footprint, is embeddable, and has an easy to use API that supports both the reactive non-blocking style and the more traditional blocking stream oriented method of web development.</p> 
</blockquote>
<p><strong>InfoQ</strong>: Can you tell me more about the audit logging features in WildFly 8?</p>
<blockquote> 
 <p>Audit logging in WildFly is the upstream work for the feature introduced in EAP 6.2. If running with RBAC enabled, only the Auditor or SuperUser roles can change the audit log configuration. Any operation against our management model gets recorded in the log. Since things like tab-completion in the CLI perform a lot of read operations, you can configure it so that only operations that actually modify the state of the model get logged. Also, we audit log all JMX access, either in the MBeanServer itself or in the core controller in the case of invocations on our JMX facade to the core management model.</p> 
 <p>We support logging to a local file or to a syslog server. The syslog server may be either local or remote, and we support logging over both the UDP and TCP protocols. TLS (tested against rsyslog) is also supported, with optional client certificate authentication. Syslog records are currently output in JSON format only, in order to easily be able to add more logged fields in response to our community and customer needs. However, it is written in such a way that adding other output formats will be possible in the future.</p> 
 <p>Information that we log includes:<br /> -Whether the operation modified the management model<br /> -Whether the operation happened once the server was fully booted<br /> -The authenticated username<br /> -The interface the operation came in through, i.e. if it came from the web interface, the JMX interface or the native interface<br /> -The address of the caller<br /> -Whether the operation succeeded<br /> -The operations themselves<br /> -In domain mode there is an UUID that can be used to track an operation as it makes its way from the Domain Controller to the Host Controllers and then to the managed servers.</p> 
 <p>Example Record<br /> - - - - - - - - - - ----</p> 
 <pre>
  2014-01-23 10:30:16 - {
   &quot;type&quot; : &quot;core”,                      
   &quot;r/o&quot; : false,
   &quot;booting&quot; : false,
   &quot;version&quot; : &quot;8.0.0.Final-SNAPSHOT&quot;,
   &quot;user&quot; : &quot;$local&quot;,
   &quot;domainUUID&quot; : null,
   &quot;access&quot; : &quot;NATIVE&quot;,
   &quot;remote-address&quot; : &quot;127.0.0.1/127.0.0.1&quot;,
   &quot;success&quot; : true,
   &quot;ops&quot; : [{
       &quot;address&quot; : [{
           &quot;system-property&quot; : &quot;xxx&quot;
       }],
       &quot;operation&quot; : &quot;remove&quot;,
       &quot;operation-headers&quot; : {
           &quot;caller-type&quot; : &quot;user&quot;,
           &quot;access-mechanism&quot; : &quot;NATIVE&quot;
       }
   }]
}
</pre> 
</blockquote>
<p><strong>InfoQ</strong>: Can you tell me more about the patching system? Does it allow me to patch a running system?</p>
<blockquote> 
 <p>The patching feature was something we developed primarily for JBoss EAP users, but a key element of our open source model is that all major features we develop for our enterprise offering, we bring upstream. So the feature is included both in JBoss EAP 6.2 and WildFly 8. The capability includes a set of new management operations and a new command in our CLI called &quot;patch&quot;. Using this command you can apply a JBoss produced patch to a single server instance either remotely or locally. You can run it against a running system, however it only stages the patch. A restart is required for the changes to take effect. You can also rollback the patch if it has problems, and the system can store the whole patch history if you like, which allows you to go back to any point in time. For those curious about the internals, the patch infrastructure builds on the modular class loading in WildFly, and essentially adds additional module directories which extend or replace those shipped with the initial install.</p> 
 <p>We plan to build on this capability in future releases, including adding some nice Wizards in the UI to apply patches.</p> 
</blockquote>
<p><strong>InfoQ</strong>: What LDAP directories are supported for storing RBAC credentials? Is Active Directory among them?</p>
<blockquote> 
 <p>Yes. Our LDAP support is pretty flexible and allows you to adjust the filters to match the schema of your directory provider. So it's essentially compatible with any LDAP server including Active Directory. As an example, with Active Directory you would likely set the username-filter to point to sAMAccountName.</p> 
</blockquote>
<p><strong>InfoQ</strong>: Aside from the branding change, how does the approach taken for WildFly differ from that taken for JBoss EAP? Is EAP more conservative?</p>
<blockquote> 
 <p>WildFly's focus is more on delivering the latest technology at frequent intervals. We aim to have a major release at least once per year, and provide frequent milestones between them. WildFly has a community support model where developers and users help each other on the forums and share code. However the focus and interest is usually always on what's current.</p> 
 <p>EAP on the other hand is more conservative and focuses on long running branches which are maintained with patches for 7-10 years. Feature updates on those branches are more gradual, and easier to consume. (We backport features from our upstream trees into older releases with a focus on preserving compatibility.) EAP has a number of other benefits beyond the distribution as part of the subscription, including vendor certification and compliance, an extensive knowledge base, and guaranteed SLAs.</p> 
</blockquote>
<p><strong>InfoQ</strong>: How soon can we expect to see a Java EE 7 version of JBoss EAP?</p>
<blockquote> 
 <p>I can't release any specific dates at this time, but I can say that the next major release of EAP7 is intending to provide Java EE 7 support. It will also include the capabilities of WildFly 8 (and future WildFly releases), since ultimately EAP is derived from WildFly.</p> 
</blockquote>
<p><strong>InfoQ</strong>: How much impact do you think Oracle's decision to kill off commercial support for GlassFish will have on the uptake of JBoss EAP?</p>
<blockquote> 
 <p>I don't want to speculate on what will ultimately happen, but I can say we have noticed increased interest in converting from GlassFish to WildFly and EAP. While there are many factors that go into choosing an application server, we understand that commitment to open source and the community is an important one. At Red Hat that has always been part of our DNA. Every line of code we write is 100% open source.</p> 
</blockquote>
<p>You can find out more from the <a href="http://wildfly.org">WildFly website</a>.</p><br><br><br><br><br><br></body></html>
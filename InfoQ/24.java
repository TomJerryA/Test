<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>RESTful Web Services Framework Jersey 2.5 Released</h3><p>The RESTful Web Services Framework <a href="https://jersey.java.net/download.html">Jersey 2.5</a> was recently released, bringing support for the latest version of <a href="http://www.eclipse.org/jetty/">Jetty</a> web server, an upgrade of the Apache Connector and numerous defects corrected.</p>
<p><a href="https://jersey.java.net/release-notes/2.5.html"> Changes</a> in the Java-based Jersey framework include:</p>
<ul> 
 <li>Support for version 9 of the Jetty web server and servlet container. This includes both a Jersey Server container based on a Jetty HTTP and Servlet container, and a Jersey Client connector supporting synchronous as well as asynchronous client invocation using the Jetty Fluent Client API.</li> 
 <li>The Apache Connector now uses the <a href="http://hc.apache.org/httpcomponents-client-4.3.x/index.html">Apache HttpClient 4.3</a>, which itself is a major refactoring with several <a href="http://www.apache.org/dist/httpcomponents/httpclient/RELEASE_NOTES-4.3.x.txt">new features and improvements</a>.</li> 
 <li>Over 60 bug fixes, including multi value http headers not correctly read and component registration through package scanning missing components.</li> 
</ul>
<p>Changes in earlier releases, after the major <a href="http://www.infoq.com/news/2013/06/Jersey_2_0_released">2.0 release</a> in June, include:</p>
<ul> 
 <li>Support for <a href="http://en.wikipedia.org/wiki/OAuth">OAuth1</a> acting as a consumer or a service provider and <a href="http://oauth.net/2/">OAuth2</a> acting as a consumer only.</li> 
 <li>Ability for a client to configure or override connection properties on a per-request basis.</li> 
 <li>Support for https when using <a href="https://grizzly.java.net/">Grizzly</a> or Apache Connector.</li> 
 <li>Support for <a href="http://projects.spring.io/spring-framework/">Spring 3</a>, enabling injection of Spring managed beans into Jersey managed resource classes as well as allowing for JAX-RS resource classes to be managed by Spring instead of Jersey.</li> 
 <li>Including the 2.5 release, 30 improvements have been made and more than 160 bugs fixed.</li> 
</ul>
<p><a href="https://jersey.java.net/documentation/latest/">Documentation</a> has been upgraded for the new release including <a href="https://jersey.java.net/documentation/latest/migration.html">issues when migrating</a> from earlier 2.* releases to 2.5.</p>
<p>Jersey 2.5 is a reference implementation of the <a href="https://jax-rs-spec.java.net/nonav/2.0/apidocs/index.html">JAX-RS 2.0 API Specification</a>, (<a href="http://jcp.org/en/jsr/detail?id=339">JSR 339</a>), released in May 2013, and a member of the <a href="https://glassfish.java.net/">GlassFish</a>&nbsp;application server project. It is <a href="https://jersey.java.net/license.html">dual licensed</a> under 2 OSI approved licenses.</p><br><br><br><br><br><br></body></html>
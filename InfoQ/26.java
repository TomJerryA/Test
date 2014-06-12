<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Spring Cloud 1.0 - Cloud Platform Abstraction</h3><p> Pivotal has recently released <a href="http://projects.spring.io/spring-cloud/">Spring Cloud 1.0</a>, an open-source library that provides a simple way to develop JVM-based applications for the cloud. Applications can connect to various cloud services and discover information about the cloud environment at runtime. Spring Cloud can be used with both Spring and non-Spring based applications. Spring Cloud 1.0 has support Cloud Foundry and Heroku, and can be extended to support other cloud platforms. </p>
<p> Spring Cloud introduces the concepts of a Cloud Connector and a Service Connector. A Cloud Connector is an interface that a cloud provider implements to allow the rest of the library to work with a cloud platform. Spring Cloud 1.0 comes with a Cloud Foundry Cloud Connector and a Heroku Cloud Connector. A Service Connector is an object that represents a connection to a service. Spring Cloud 1.0 comes with a Service Connector for javax.sql.DataSource and Spring Data projects. Custom Cloud Connectors and Service Connectors can be written to support other cloud platforms and services, packaged as JAR files and simply added to the classpath. </p>
<p> To use Spring Cloud with a Spring application, you will need to add the <em>spring-cloud-spring-service-connector</em> dependency. Here's the Maven dependency snippet. </p>
<pre>
	&lt;dependency&gt;
		&lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
		&lt;artifactId&gt;spring-cloud-spring-service-connector&lt;/artifactId&gt;
		&lt;version&gt;1.0.0.RELEASE&lt;/version&gt;
	&lt;/dependency&gt;
</pre>
<p> To use Spring Cloud with a non-Spring application, you will need to add the <em>spring-cloud-core</em> dependency instead. </p>
<pre>
	&lt;dependency&gt;
		&lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
		&lt;artifactId&gt;spring-cloud-core&lt;/artifactId&gt;
		&lt;version&gt;1.0.0.RELEASE&lt;/version&gt;
	&lt;/dependency&gt;
</pre>
<p> If you want the ability to deploy to both Cloud Foundry and Heroku, add the following dependencies. </p>
<pre>
	&lt;dependency&gt;
		&lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
		&lt;artifactId&gt;spring-cloud-cloudfoundry-connector&lt;/artifactId&gt;
		&lt;version&gt;1.0.0.RELEASE&lt;/version&gt;
	&lt;/dependency&gt;
	&lt;dependency&gt;
		&lt;groupId&gt;org.springframework.cloud&lt;/groupId&gt;
		&lt;artifactId&gt;spring-cloud-heroku-connector&lt;/artifactId&gt;
		&lt;version&gt;1.0.0.RELEASE&lt;/version&gt;
	&lt;/dependency&gt;
</pre>
<p> Here's an example of getting a DataSource service and an ApplicationInstanceInfo. ApplicationInstanceInfo provides information about the instance, and is cloud platform specific. </p>
<pre>
	// MyController.java
	@Controller
	public class MyController {
		@Autowired(required = false) DataSource dataSource;
		
		@Autowired ApplicationInstanceInfo instanceInfo;
		
		...
	}
</pre>
<pre>
	// CloudConfig.java
	@Configuration
	@ServiceScan
	@Profile(&quot;cloud&quot;)
	public class CloudConfig extends AbstractCloudConfig {
		@Bean
		public ApplicationInstanceInfo applicationInfo() {
			return cloud().getApplicationInstanceInfo();
		}
	}
</pre>
<p> The <em>@Profile(&quot;cloud&quot;)</em> annotation is used since we only want this configuration loaded in a cloud environment. The <em>@ServiceScan</em> annotation scans for all services and creates a bean for autowiring. <em>@ServiceScan</em> is similar to <em>@ComponentScan</em>, but instead of looking for components and beans, it looks for bound services. </p>
<p> For a quick walkthrough on how to deploy to Cloud Foundry or Heroku, read the <a href="http://spring.io/blog/2014/06/03/introducing-spring-cloud">Introducing Spring Cloud</a> blog post. This blog post uses a Spring Boot sample application. Non-Spring based applications should go over the <a href="https://github.com/spring-projects/spring-cloud/blob/master/spring-cloud-core/README.md">Spring Cloud Core README</a> usage notes. </p><br><br><br><br><br><br></body></html>
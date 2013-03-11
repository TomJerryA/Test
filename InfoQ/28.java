<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Jelastic 1.9 with FTP, NGINX caching, Apache TomEE and MariaDB 10</h3><p><a href="http://jelastic.com/press-releases/jelastic-launches-new-version-1-9">Jelastic</a>, a Platform-as-a Service Java and PHP cloud server hosting platform has released version 1.9 with support for FTP/FTPS and <a href="http://wiki.nginx.org/Main">NGINX</a> caching. The latest release provides support for <a href="http://tomee.apache.org/apache-tomee.html">Apache TomEE</a>, the enterprise edition of Apache Tomcat and <a href="http://blog.mariadb.org/tag/mariadb-10/">MariaDB 10</a> that enables developers to take advantage of multi-source replication, dynamic columns and <a href="http://blog.mariadb.org/mariadb-galera-cluster-5-5-29-stable-ga-released/">MariaDB Galera Cluster</a>.</p> 
<p>Jelastic 1.9 includes an advanced reporting dashboard that enables hosting providers to analyze all aspects of their <a href="http://searchcloudcomputing.techtarget.com/definition/Platform-as-a-Service-PaaS">PaaS</a> business and customer behaviour including conversion process, churn rate, activity rate, feature popularity and revenue per customer. It also provides a new log management system that enables hosting providers to effectively support their Jelastic customers using a new browser based user interface.</p> 
<p>Jelastic 1.9 enables hosting providers to build templates from RPMs and activates secure SSL (HTTPS) for database administration web pages. It also includes Jelastic Cluster Admin (JCA) features such as smart live migration, dashboard customization, funding history, tariffs management and system monitoring.</p> 
<p>Jelastic framework has been developed in such a way that server resources for Java and PHP applications are allocated depending upon the usage.</p> 
<p>In an exclusive interview to InfoQ, Dmitry Sotnikov, Chief Operating Officer shared additional information about Jelastic 1.9<br /> <br /> <strong>InfoQ: What is the real meaning of PaaS?</strong></p> 
<blockquote>
  Platform-as-a-Service (PaaS) is automated hosting that takes IT management burden away from you. In regular hosting or infrastructure-as-a-service you basically get a server or a virtual machine. There is still a lot of administrative work that needs to be done from that moment to having your application running: set up the servers, set up the databases, set up load-balancing, set up clustering if high availability is required, make sure that all configuration changes and application and library versions are consistent across all servers, and so on. And this has to be done again and again each time your application changes, more servers need to be added and so on.
 <br /> &nbsp;
 <br /> With PaaS, all of that is automated by the platform. You can just concentrate on your amazing application and let the platform handle all the server management and scaling.
 <br /> 
 <br /> In addition, you get many more features that developers and production IT people appreciate, including: 
 <ul> 
  <li>Ability to build applications in the cloud directly from source code repositories</li> 
  <li>Support for application development lifecycle with ability to clone environments (including all data!) and swap them (for example, Production and Staging)</li> 
  <li>Teamwork support with roles and permissions</li> 
  <li>Integration with popular developer tools</li> 
  <li>Remote debugging</li> 
  <li>Integration with popular 3rd-party services for monitoring, log management, and much more</li> 
 </ul> 
</blockquote> 
<p><strong>InfoQ: Can you share with us how Jelastic is different from normal shared hosting?</strong></p> 
<blockquote>
  With Jelastic you get more than a slice of a web server. You log into Jelastic dashboard, and with a few clicks of a mouse create a whole environment that has application servers, load balancers, databases, Memcached, and so on. Then you simply upload your application or specify connection information for your GIT or SVN code repository - and Jelastic gets your application running and automatically scaling in the cloud.
 <br /> 
 <br /> So unlike shared hosting, you get the power to easily scale your application to many servers, and the flexibility of fully managing the servers: changing configuration files, uploading application libraries, and so on. 
</blockquote> 
<p><strong>InfoQ: How many sites I can host with Jelastic?</strong></p> 
<blockquote>
  There is no limit - Jelastic gives you a self-service dashboard in which you define how many servers you need, how you want to use them, and whether and how you want Jelastic to scale them. 
</blockquote> 
<p><strong> InfoQ: Does Jelastic provide support for .NET Framework?</strong></p> 
<blockquote>
  At the moment, Jelastic provides full support for PHP and Java applications, including all JVM-based languages such as Closure, Groovy, Scala, Jruby and Jython.
 <br type="_moz" /> 
</blockquote> 
<p><strong>InfoQ: How much it will cost to host a site?</strong></p> 
<blockquote>
  Jelastic has hourly billing and automated scaling (including vertical scaling - ability to add memory and processing power on the fly) - hence you are actually only paying for what you use, and do not have to overpay for something you do not need. The costs start at mere 2 cents/hour and learning your actual price for your actual application is easy: just sign up for a 
 <a href="http://jelastic.com">free trial</a>, run your application, and you will see your &quot;virtual bill&quot; that you do not need to pay - but that will tell you exact costs with no guessing required.
 <br type="_moz" /> 
</blockquote> 
<p><strong>InfoQ: Is it possible to install WordPress and other PHP based blogging apps?</strong></p> 
<blockquote>
  Jelastic can host and scale any PHP or Java application. In addition to that, some of our 
 <a href="http://www.servint.net/jelastic.php">hosting partners</a> are using Jelastic to provide one-click deployment of popular applications such as Wordpress, Joomla, Drupal, Magnolia, Liferay and so on. 
</blockquote> 
<p><strong>InfoQ: Is Jelastic capable of handling two lakh visitors per day?</strong></p> 
<blockquote>
  Jelastic is 
 <a href="http://jelastic.com/customers">hosting applications</a> that serve hundreds of thousands of users and millions of webrequest a day.
 <br type="_moz" /> 
</blockquote> 
<p><strong>InfoQ: Does Jelastic provide support for all major browsers including Internet Explorer?</strong></p> 
<blockquote>
  Applications within Jelastic can support whatever browsers the creators of these applications choose to support.&nbsp; 
</blockquote> 
<p><strong>InfoQ: Does Jelastic include any apps to notify downtimes?</strong></p> 
<blockquote>
  Jelastic provides basic built-in monitoring and allows you to integrate with any external monitoring solutions. 
</blockquote> 
<p><strong>InfoQ: Is it possible to create POP3 mail boxes with Jelastic?</strong></p> 
<blockquote>
  Jelastic is application hosting - not mailbox hosting service. However, if your application requires the ability to send email, you can either add a mail server (such as Sendmail) or use external mailboxes (such as Google Apps) or SendGrid. 
</blockquote> 
<p><strong>InfoQ: Is there any similarity between Jelastic and Windows Azure?</strong></p> 
<blockquote>
  Both are platforms-as-a-service. Azure is primarily targeting ASP.NET applications with some support for non-Microsoft systems, and is only available from Microsoft. Jelastic is the platform-as-a-service for Java and PHP applications and is available from hosting providers around the Globe including US, Brazil, UK, Germany, Sweden, Finland, Russia and Japan.
 <br type="_moz" /> 
</blockquote> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
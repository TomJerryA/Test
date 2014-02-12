<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Design Patterns for Cloud-Hosted Applications</h3><p>The <a href="http://pnp.azurewebsites.net/en-us/">patterns &amp; practices group</a> at Microsoft recently released a <a href="http://msdn.microsoft.com/en-us/library/dn568099.aspx">guide</a> with suggested solutions and patterns suitable when implementing cloud-hosted applications. The guide discusses the problems different patterns address together with benefits and possible downsides. The ambition from the group has been to provide guidance for distributed systems irrespective of cloud platform even though the examples given are targeting <a href="http://www.windowsazure.com/">Windows Azure</a>.</p>
<p>Using feedback from the developer community, the group has identified eight categories of problems they believe cover the most common areas in cloud application development:</p>
<ul> 
 <li><a href="http://msdn.microsoft.com/en-us/library/dn600219.aspx">Availability</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/dn600216.aspx">Data Management</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/dn600217.aspx">Design and Implementation</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/dn600220.aspx">Messaging</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/dn600218.aspx">Management and Monitoring</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/dn600224.aspx">Performance and Scalability</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/dn600215.aspx">Resiliency</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/dn600221.aspx">Security</a></li> 
</ul>
<p>For each of these categories, the group have created guidance and documented common patterns to help developers in solving problems they regularly encounter.</p>
<p>The guide contains ten primer and guidance topics providing basic knowledge and good practice techniques, each covering one aspect of application development and targeting one of the categories. Topics covered include Asynchronous Messaging, Caching and Data Consistency.</p>
<p>Also included are 24 design patterns that the group have found useful in cloud-hosted applications, each pattern belonging to one or more of the categories described. Examples of patterns included are Compensating Transaction, Command and Query Responsibility Segregation (CQRS) and Pipes and Filters. Each pattern is described in a common format with the context and problem where the pattern applies, the solution given by the pattern together with issues and considerations for applying the pattern. An example for the Azure is also provided for each pattern.</p>
<p>To demonstrate the usage of the design patterns described the group has created ten sample applications with all source code available for <a href="http://www.microsoft.com/en-us/download/details.aspx?id=41673">download</a>. The samples include one application concerning competing consumers retrieving messages from a service bus and one using filters simulating a pipeline.<br /> The P &amp; P group emphasizes that the examples are simplified and not designed for production usage.</p>
<p>Windows Azure is the cloud platform provided by Microsoft.</p><br><br><br><br><br><br></body></html>
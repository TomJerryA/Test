<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Patterns and Anti-Patterns for Scalable and Available Cloud Architectures</h3><p>More than anything else, architectural choices matter when designing a system with high scalability and availability. Using Azure customers as an example, Microsoft talks about the patterns and anti-patterns they see with their Azure customers and how it affects the four facets of system architecture:</p>
<ul> 
 <li>Scalability: Can I add capacity to handle increased demand?</li> 
 <li>Availability: Will my application endure transient and enduring faults?</li> 
 <li>Manageability: Do I have ways to understand the health and performance of the live system?</li> 
 <li>Feasibility: Can I build and maintain the system with my time and cost budget?</li> 
</ul>
<p><b>Scalability</b></p>
<p>Scalability comes from two aspects: capacity and density. Capacity involves adding extra hardware, which may be trivial (adding extra web servers behind a load balancer) or very difficult (adding a second database server). Density refers to how efficient you can use the capacity you already have. Traditional performance tuning can significantly increase density.</p>
<p><b>Sidebar: Lighting Money on Fire</b></p>
<p>A common theme during the presentation is “lighting money on fire”. By this Mark Simms means doing something that is inefficient for no reason. Examples include using NATs instead of proper load balancers or XML as an internal data exchange format.</p>
<p><b>Metered Resources</b></p>
<p>Metered resources are something that need to be carefully monitored. An example of a metered resource is a database connection. As a limited resource, misusing it can dramatically reduce density.</p>
<p>To make this more concrete, consider Azure SQL. The standard version only allows 180 connections per database. The default connection pool in ADO.NET is 100. So if you have two web servers connected to an Azure SQL database, and those web servers leak connections, you can easily exceed the cap.</p>
<p>Other examples of metered resources include authentication servers and third party web services. These are sometimes called “hidden resources” because developers often overlook them when planning their architecture.</p>
<p><b>Load Leveling through Queues</b></p>
<p>Spikes in uploads can be problematic, especially on systems that are tuned read-heavy workloads. One way to mitigate this is by trading latency for availability through the use of queues.</p>
<p>Under this scheme new data isn’t synchronously stored in the database. Instead they are placed in a queue which a background process monitors. This background process can smooth out the workload so that the database is used consistently instead of being hammered at some times and idle at others.</p>
<p>Another advantage of using queues is that work can be batched. Generally speaking it is much faster to load information into a database in batches rather than one record at a time.</p>
<p>Finally, this adds a decoupling point. The background process or database could be down entirely without affecting the front-end application’s ability to accept new data.</p>
<p><b>Improving Message Queue Availability</b></p>
<p>If too many messages are received at one time, secondary message queues can be used to store the excess. In order to do this you need to design the application to support multiple queues, even if you intend to only deploy it with one queue to start.</p>
<p>When messages that exceed the size that the application is designed to handle, one technique to avoid data loss is to write the message to blob storage. The logical message in the queue is then modified to store a pointer to the blob entry instead of the original payload.</p>
<p><b>Web Server Availability</b></p>
<p>In order to keep the web server available, all downstream calls must be asynchronous and bounded. The bounds must be in terms of both time outs and concurrent requests. The latter is often overlooked. A somewhat embarrassing example of this is Visual Studio Online’s two hour outage. The root cause of this outage was too many concurrent requests to an external authentication server that had temporarily gone down.</p>
<p><b>Authentication Services</b></p>
<p>This leads us to our next topic, authentication services. When an authentication server goes down it can completely take down an otherwise stable application. For this reason Microsoft highly recommends the use of a federated authentication server.</p>
<p><b>Bad Data Logging</b></p>
<p>Most developers understand the need to validate data, but they don’t know what to do when that validation fails. Merely discarding the data and throwing an error isn’t enough. The bad data should be logged in its raw form so that developers can figure out why the bad request was made.</p>
<p>Most bad requests come from version mismatches. This happens when the user has an older, or newer, version of the client than the server is capable of handling.</p>
<p><b>Anti-Pattern: Configuration</b></p>
<p>When Microsoft’s Azure team review client code they still see hard-coded connection strings and other configuration data. This can be a real problem with the configuration needs to be changed in a hurry to point to different hardware.</p>
<p><b>Anti-Pattern: Assumed Database Reliability</b></p>
<p>For the last generation of developers, database connectivity was a given. Database and internal network failures almost never happen. So it common for developers to not check for exceptions. Or if they do, they don’t handle them correctly and data is lost.</p>
<p><b>Anti-Pattern: SQL Injection</b></p>
<p>Yes, it is still very common problem. In some cases the very first web request they examine has an obvious SQL Injection vulnerability.</p>
<p><b>Anti-Pattern: Logging to the Failed Resource</b></p>
<p>The logging infrastructure needs to be isolated from the rest of the application stack. If logs are written to the same database as the production data, losing one database necessarily means the other is lost as well.</p>
<p><b>Anti-Pattern: Rethrowing Exceptions</b></p>
<p>There are two common anti-patterns in this area. The first is rethrowing exceptions with “throw ex;” instead of “throw;”, causing the stack trace to be lost. The second is rethrowing the exception when there isn’t a higher level handler to catch it. This of course causes the whole application to crash in .NET 2.0 and later.</p>
<p>To see the whole video check out <a href="http://channel9.msdn.com/Events/Build/2014/3-633">Building Big: Lessons Learned from Azure Customers</a> on Channel 9.</p><br><br><br><br><br><br></body></html>
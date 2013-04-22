<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Database Lifecycle Management Guidance Updated by Microsoft</h3><p>Microsoft has updated the <a href="http://msdn.microsoft.com/en-us/library/jj907294.aspx">database lifecycle management</a> curated guidance page in the MSDN library, which provides relevant resources for SQL Server Data Tools, SQL Server Management Studio and Windows Azure SQL Database. The page features SQL Server database lifecycle management diagram to identify the applications and actions that apply to your database scenarios.</p> 
<p><a href="/resource/news/2013/04/database-lifecycle-management/en/resources/Figure_1_Original.gif;jsessionid=748EEDFE057214140AEB9DC5384E0DD8" target="_blank"><img src="http://www.infoq.com/resource/news/2013/04/database-lifecycle-management/en/resources/4Figure_1.png;jsessionid=748EEDFE057214140AEB9DC5384E0DD8" alt="" _href="img://4Figure_1.png" _p="true" /></a></p> 
<p>For instance, if you need to know more about Windows Azure SQL database backup and restore then you just need to navigate to backup and restore task located under Windows Azure SQL Database section and you will be able to view a detailed tutorial of the task with source codes, screenshots and external references.</p> 
<p>&quot;The subject matter is curated for students and others new to the industry. I hope it helps them,&quot; says <a href="http://www.linkedin.com/pub/louis-berner/19/214/829">Louis Berner</a> who works as a Technical Writer/Software Engineer with SQL Server User Education.</p> 
<p>As of the time of this writing, following topics are covered in the database lifecycle management guidance page.</p> 
<p><strong>SQL Server Data Tools</strong></p> 
<ul> 
 <li><a href="http://msdn.microsoft.com/en-us/data/tools.aspx">Microsoft SQL Server Data Tools (SSDT)</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/data/hh297028">Get Started with SQL Server Data Tools</a> - Video</li> 
 <li><a href="http://channel9.msdn.com/Events/TechEd/Europe/2012/DBI311">Microsoft SQL Server Data Tools: Database Development from Zero to Sixty</a> - Video</li> 
 <li><a href="http://msdn.microsoft.com/en-us/data/aa937699">Data Development Technical Documentation</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/hh550080(VS.103).aspx">Data Portability</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/windowsazure/ee621784.aspx">Tools and Utilities Support (Windows Azure SQL Database)</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/windowsazure/ff394102.aspx">Guidelines and Limitations (Windows Azure SQL Database)</a></li> 
 <li><a href="http:// http://blogs.msdn.com/b/ssdt/">SQL Server Data Tools Team Blog</a></li> 
</ul> 
<p><strong>SQL Server Management Studio</strong></p> 
<ul> 
 <li><a href="http://www.windowsazure.com/en-us/manage/services/sql-databases/how-to-manage-a-sqldb/">Managing Windows Azure SQL Database Using SQL Server Management Studio</a></li> 
 <li><a href="http://technet.microsoft.com/en-us/library/ms187048.aspx">Backup and Restore of SQL Server Databases</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/windowsazure/ee730904.aspx">Migrating Databases to Windows Azure SQL Database</a></li> 
 <li><a href="http://channel9.msdn.com/Events/TechEd/Europe/2012/FDN01">The New World of Data: SQL Server and Hybrid IT</a> - Video</li> 
 <li><a href="http://go.microsoft.com/fwlink/?LinkId=274959">Get Started with SQL Data Sync</a></li> 
 <li><a href="http://blogs.technet.com/b/dataplatforminsider/">SQL Server Team Blog</a></li> 
</ul> 
<p><strong>Windows Azure SQL Database</strong></p> 
<ul> 
 <li><a href="http://www.windowsazure.com/en-us/manage/services/sql-databases/getting-started-w-sql-databases/">Get Started with Windows Azure SQL Database</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/windowsazure/ff394114.aspx">Monitor Windows Azure SQL Database Using Dynamic Management Views </a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/windowsazure/jj650016.aspx">Windows Azure SQL Database Backup and Restore</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/library/windowsazure/hh335292.aspx">How to: Import and Export a Database (Windows Azure SQL Database)</a></li> 
 <li><a href="http://www.microsoft.com/en-us/download/details.aspx?id=8396">Windows Azure Training Kit - November 2012</a></li> 
 <li><a href="http://windowsazure-trainingkit.github.com/index.htm">Windows Azure Training Kit - GitHub</a></li> 
 <li><a href="http://www.windowsazure.com/en-us/pricing/free-trial/">Windows Azure 90-day Free Trial</a></li> 
 <li><a href="http://social.technet.microsoft.com/wiki/contents/articles/1541.windows-azure-sql-database-connection-management.aspx">Windows Azure SQL Database Connection Management</a></li> 
 <li><a href="http://social.technet.microsoft.com/wiki/contents/articles/1719.windows-azure-sql-database-connectivity-troubleshooting-guide.aspx">Windows Azure SQL Database Connectivity Troubleshooting Guide</a></li> 
 <li><a href="http://social.msdn.microsoft.com/Forums/en-US/ssdsgetstarted/threads">Windows Azure SQL Database Community Forum</a></li> 
 <li><a href="http://blogs.msdn.com/b/windowsazure/">Windows Azure Team Blog</a></li> 
 <li><a href="http://www.windowsazure.com/en-us/support/service-dashboard/">Windows Azure Service Dashboard</a></li> 
 <li><a href="http://stackoverflow.com/questions/tagged/azure%20sql-azure">Stackoverflow for Windows Azure SQL Database</a></li> 
</ul> 
<p>In an interview to InfoQ, Louis explained the purpose behind the creation of a curated page for database lifecycle management.</p> 
<p><strong>InfoQ: Do you think the flowchat diagram will really assist developers to code quickly and without any frustration?</strong></p> 
<blockquote>
  The diagram provides a holistic view of SSDT, SSMS, Azure, and a hybrid architecture in terms of the actions that connect them. For example, you can publish from SSDT to Azure; you can import to SSDT from a local instance of SQL Server; and you can export a .bacpac file from SQL Database on Azure to a local disk.
 <br /> 
 <br /> It is the &quot;publish,&quot; &quot;import,&quot; and &quot;export&quot; actions - along with the other operations in the visual - that tie together the Microsoft applications in the diagram. The visual presentation is not intended to assist developers to code quickly or without frustration, but rather to connect the dots for customers and provide a visual sense of cohesion between the applications that contribute to the database lifecycle. 
</blockquote> 
<p><strong>InfoQ: From your point of view, who will benefit from the resources provided on the DLM page?</strong></p> 
<blockquote>
  The DLM topic is the result of work I am doing with Microsoft Customer Support Services (CSS). CSS Support Engineers have data that indicate barriers to adoption of the Azure platform because customers are confused about: 
 <ul> 
  <li>How to get started with SQL Server Data Tools</li> 
  <li>How to get existing data migrated to the Azure platform - i.e., data portability options</li> 
  <li>How to compare and sync data</li> 
  <li>How to backup to the Cloud or how to use Import/Export features</li> 
  <li>How to do backup and restore operations from the Cloud in order to satisfy their SLA requirements</li> 
 </ul> 
 <p>You can see from the list of topics that they are mostly 100-level and 200-level concepts. So the initial release of the DLM topic - published end-Jan-2013 - addresses adoption of the Azure platform, data portability, getting up-and-running, and basic developer tasks. Future DLM topic updates will include more advanced subjects like:</p> 
 <ul> 
  <li>Federations</li> 
  <li>Performance - latency, throttling, wait statistics</li> 
  <li>Error reference</li> 
  <li>PowerShell scripting</li> 
  <li>Monitoring</li> 
  <li>Permissions and roles</li> 
 </ul> 
 <p>I continue to consume CSS data to ensure that I address customer top tasks. The new topics listed above are from the latest cut of CSS customer data.</p> 
</blockquote> 
<p><strong>InfoQ: Do you have any plan to update DLM topic page frequently?</strong></p> 
<blockquote>
  The plan is to update the topic each quarter. The next update should be ready to publish in May/June 2013. 
 <p>I am developing a workflow to analyze customer data, build a backlog of topics, review the backlog with project stakeholders, publish updates to the topic, and validate that the topic is meeting customer needs.</p> 
 <p>It is a method of content curation, as nearly all of the content listed in the DLM topic already exists somewhere on the Web. I am collecting the best-of-breed content, tutorials, video, and community assets in a single repository, and customers seem to like my approach.</p> 
</blockquote> 
<p><strong>InfoQ: Do you have any estimate regarding how many developers really benefited from the DLM resource page?</strong></p> 
<blockquote>
  Since Jan-2013, the topic has &gt; 3,000 page views on MSDN, excellent customer ratings, and verbatim comments like &quot;Awesome&quot; and &quot;Very helpful&quot;&nbsp; It may not meet everyone's needs, but for the target audience:&nbsp; new to Azure, new to SQL Server, frustrated with getting started, looking for the best documentation and video available - I have begun to build a following. 
</blockquote> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
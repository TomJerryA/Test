<p>Microsoft has announced the availability of <a href="http://blogs.msdn.com/b/adonet/archive/2013/02/27/ef6-alpha-3-available-on-nuget.aspx">Entity Framework 6 Alpha 3</a> with support for code first mapping to insert, update, delete stored procedures with the help of fluent API, connection resiliency, pull request from iceclow, UnaiZorrilla and new DbContext API scenarios that enables you to manage your own transactions. <br /> <br /> According to Microsoft, three stored procedures should be created in format such as &lt;type_name&gt;_Insert, &lt;type_name&gt;_Update and &lt;type_name&gt;_Delete. Moreover, the parameter names correspond to the property names and insert and update stored procedures should include a parameter for every property except for those marked as identity or computed and the delete stored procedure should have a parameter for the key value of the entity.</p> 
<p>Let us take a look at the following code snippet<br /> <br /> <code> public class Blog <br /> { <br /> &nbsp; public int BlogId { get; set; } <br /> &nbsp; public string Name { get; set; } <br /> &nbsp; public string Url { get; set; } <br /> } </code></p> 
<p>The insert stored procedure corresponding to the above code should look like as shown below<br /> <br /> <code> CREATE PROCEDURE [dbo].[Blog_Insert] <br /> &nbsp; @Name varchar(max), <br /> &nbsp; @Url varchar(max) <br /> AS <br /> &nbsp; INSERT INTO [dbo].[Blogs] ([Name], [Url])<br /> &nbsp; VALUES (@Name, @Url)<br /> <br /> &nbsp; SELECT SCOPE_IDENTITY() AS BlogId </code></p> 
<p>The update and delete procedures will be ab shown below<br /> <br /> <code> CREATE PROCEDURE [dbo].[Blog_Update] <br /> &nbsp; @BlogId int, <br /> &nbsp; @Name varchar(max), <br /> &nbsp; @Url varchar(max) <br /> AS <br /> &nbsp; UPDATE [dbo].[Blogs]&nbsp;&nbsp; SET [Name] = @Name, [Url] = @Url&nbsp;&nbsp;&nbsp; <br /> &nbsp; WHERE BlogId = @BlogId; </code><br /> <br /> <br /> <code> CREATE PROCEDURE [dbo].[Blog_Delete] <br /> &nbsp; @BlogId int <br /> AS <br /> &nbsp; DELETE FROM [dbo].[Blogs]<br /> &nbsp; WHERE BlogId = @BlogId </code></p> 
<p>The official <a href="http://entityframework.codeplex.com/wikipage?title=Code%20First%20Insert%2fUpdate%2fDelete%20Stored%20Procedure%20Mapping">documentation</a> examines all the possible scenarios in detail. <br /> <br /> Entity Framework 6 Alpha 3 includes <a href="http://entityframework.codeplex.com/wikipage?title=Connection%20Resiliency%20Spec">connection resiliency</a> that enables automatic recovery from transient connection failures. It is implemented using IExecutionStrategy interface which in turn make use of IRetriableExceptionDetector and IRetryDelayStrategy interfaces.</p> 
<p>According to official sources, Entity Framework will ship with four execution strategies such as NonRetryingExecutionStrategy, DefaultSqlExecutionStrategy, ExecutionStrategy and SqlAzureExecutionStrategy.<br /> <br /> Entity Framework 6 Alpha 3 provides an ability to pull request from <a href="http://www.codeplex.com/site/users/view/iceclow">iceclow</a> that allows you to create custom migrations operations and process them in a custom migrations SQL generator. <a href="http://romiller.com/2013/02/27/ef6-writing-your-own-code-first-migration-operations/">Rowan Miller</a>, Program Manager, ADO.NET Entity Framework, Microsoft has examined the implementation of iceclow with relevant code samples. <br /> <br /> The Alpha 3 also enables you to pull request from <a href="http://www.codeplex.com/site/users/view/UnaiZorrilla">UnaiZorrilla</a> which provides a pluggable pluralization and singularization service including the ability to manage your own transactions with the help of DbContext.Database.UseTransaction and DbContext.Database.BeginTransaction APIs.</p> 
<p id="lastElm"></p>
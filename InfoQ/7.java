<p>In <a href="http://www.nuget.org/packages/microsoft.aspnet.webapi.odata">ASP.NET Web API OData</a>, it is possible to enable <a href="http://www.odata.org/">OData</a> query syntax for a particular action with the help of <a href="http://blogs.msdn.com/b/webdev/archive/2013/02/06/protect-your-queryable-api-with-validation-feature-in-asp-net-web-api-odata.aspx">Queryable API</a> as shown below<br /> <br /> <code> [Queryable]&nbsp;&nbsp;&nbsp; <br /> public IQueryable&lt;WorkItem&gt; Get(int projectId) </code><br /> <br /> However, if you expose the queryable action outside your organization, you should protect the service by adding a layer of protection with the help of query validation. Hongmei Ge, Program Manager, Microsoft recently examined the various scenarios where you can infuse validation in Queryable API.<br /> <br /> The first scenario as pointed out by Hongmei is to only allow queries that contains $top and $skip using a property called AllowedQueryOptions as shown below<br /> <br /> <code>[Queryable(AllowedQueryOptions = AllowedQueryOptions.Skip | AllowedQueryOptions.Top)]<br /> public IQueryable&lt;WorkItem&gt; Get(int projectId) </code></p> 
<p>It is possible to limit the value for $top and $skip to 100 and 200 using MaxTop and MaxSkip property<br /> <br /> <code>[Queryable(MaxTop = 100)]<br /> public IQueryable&lt;WorkItem&gt; Get(int projectId) </code><br /> <br /> <code>[Queryable(MaxSkip = 200)]<br /> public IQueryable&lt;WorkItem&gt; Get(int projectId) </code><br /> <br /> With the help of AllowedOrderbyProperties, you can order the results by Id propery because the order by arbitrary properties could be slow<br /> <br /> <code> [Queryable(AllowedOrderByProperties = &quot;Id&quot;)]<br /> public IQueryable&lt;WorkItem&gt; Get(int projectId) </code><br /> <br /> If your clients use equal comparison inside the $filter, then you should validate it using AllowedLogicalOperators<br /> <br /> <code>[Queryable(AllowedLogicalOperators = AllowedLogicalOperators.Equal)]<br /> public IQueryable&lt;WorkItem&gt; Get(int projectId) </code><br /> <br /> It is possible to turn off arithmetic operations in $filter by setting the value of AllowedArithmeticOperators to None<br /> <br /> <code>[Queryable(AllowedArithmeticOperators = AllowedArithmeticOperators.None)]<br /> public IQueryable&lt;WorkItem&gt; Get(int projectId) </code><br /> <br /> You can limit the usage of function in $filter using AllowedFunctions property<br /> <br /> <code>[Queryable(AllowedFunctions = AllowedFunctions.StartsWith)]<br /> public IQueryable&lt;WorkItem&gt; Get(int projectId) </code><br /> <br /> The above code implies that only StartsWith function can be used in $filter.<br /> <br /> Hongmei aslo demostrates query validation in advanced scenarios such as customizing default validation logic for $skip, $top, $orderby, $filter and the usage of ODataQueryOptions to validate the query.</p> 
<p id="lastElm"></p>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>A first look at Opserver, Stack Exchange's monitoring solution</h3><p><a href="https://github.com/opserver/opserver">Opserver</a> is an open source monitoring solution, released by <a href="http://www.stackexchange.com/">Stack Exchange</a>, of <a href="http://www.stackoverflow.com/">Stack Overflow</a>'s fame. Unusually in the monitoring tool's space, is is built on top of the .Net Framework.</p>
<p>Opserver aims to provide a quick overall view of each monitored system's health, but allowing the user to deep dive using a drill-down approach. As <a href="http://nickcraver.com">Nick Craver</a>, one of Opserver's creator told InfoQ:</p>
<blockquote>
 We believe a monitoring system should show you systems at a high level, present what’s wrong, and allow you to drill in for more detail.
</blockquote>
<p>Opserver is organized around web dashboards, each one specialized on a given system. Opserver currently supports <a href="http://www.microsoft.com/sql">SQL Server</a>, <a href="http://www.elasticsearch.org/">ElasticSearch</a>, <a href="http://haproxy.1wt.eu/">HAProxy</a>, <a href="https://github.com/NickCraver/StackExchange.Exceptional">StackExchange.Exceptional</a> and <a href="http://redis.io/">Redis</a>. It also uses <a href="http://www.solarwinds.com/network-performance-monitor.aspx">SolarWinds' Orion</a>, a commercial tool, to provide infrastructure and network monitoring. An Opserver installation does not require using all these systems, as they can be configured on an opt-in basis.</p>
<p>Taking SQL Server as an example, Opserver provides high-level information on CPU and memory consumption or the overall health of databases:</p>
<p>(Click on the image to enlarge it)</p>
<p><a _href="resource://OpServer_SQLServer_Dashboard_full.png" href="/resource/news/2013/12/first_look_at_opserver/en/resources/OpServer_SQLServer_Dashboard_full.png"><img alt="Opserver's SQL Server Dashobard" _href="img://OpServer_SQLServer_Dashboard.png" _p="true" src="http://www.infoq.com/resource/news/2013/12/first_look_at_opserver/en/resources/OpServer_SQLServer_Dashboard.png" /></a></p>
<p>Below the 10,000 feet view, Opserver provides additional data. For instance, it provides a list of the top queries, sorted by multiple criteria (total duration, average CPU consumption). For each query, it provides more detailed information, including its query execution plan (a detailed breakdown of the steps taken to execute the query).</p>
<p>(Click on the image to enlarge it)</p>
<p><a _href="resource://OpServer_SQLServer_TopQueries_full.png" href="/resource/news/2013/12/first_look_at_opserver/en/resources/OpServer_SQLServer_TopQueries_full.png"><img alt="Opserver's SQL Server Top Queries" _href="img://OpServer_SQLServer_TopQueries.png" _p="true" src="http://www.infoq.com/resource/news/2013/12/first_look_at_opserver/en/resources/OpServer_SQLServer_TopQueries.png" /></a></p>
<p>There are a few steps to take in order to setup Opserver. Besides github's Opserver <a href="https://github.com/opserver/opserver">readme</a> file, <a href="http://dannysorensen.azurewebsites.net/2013/11/using-stack-exchanges-opserver-step-1-will-it-build/">some</a> <a href="http://patpack.blogspot.pt/2013/10/setting-up-stackexchanges-opserver.html">users</a> have described their setup experiences. In a nutshell, the code must be cloned from github, compiled and published on an IIS server. There is also the need to perform some configurations, of which there are two types: security settings and system's settings. Opserver provides examples for each settings definition, based on the ones used on Stack Exchange itself. These examples can be found at &lt;site root&gt;\Config.</p>
<p>The SecuritySettings.config file is the place where items such as the authentication methods are defined:</p>
<pre>
&lt;?xml version=&quot;1.0&quot; encoding=&quot;utf-8&quot;?&gt;
&lt;SecuritySettings provider=&quot;AD&quot;&gt;
    &lt;!-- Optional, these networks can see the 
	overview dashboard without authentication --&gt;
    &lt;InternalNetworks&gt;
        &lt;Network name=&quot;SE Internal&quot; cidr=&quot;10.0.0.0/8&quot; /&gt;
    &lt;/InternalNetworks&gt;
&lt;/SecuritySettings&gt;

&lt;!-- 
Example of global access for everyone:
&lt;SecuritySettings provider=&quot;alladmin&quot; /&gt;
--&gt;</pre>
<p>There is one configuration file per system. The currently supported format is JSON. Here's an example of a SQL Server configuration:</p>
<pre>
{
    &quot;defaultConnectionString&quot;: &quot;Data Source=$ServerName$;Initial Catalog=master;Integrated Security=SSPI;&quot;,
    &quot;clusters&quot;: [ // clusters are only available for SQL Server 2012
        {
        	&quot;name&quot;: &quot;NY-SQLCL04&quot;,
        	&quot;refreshIntervalSeconds&quot;: 20,
        	&quot;nodes&quot;: [
        		{ &quot;name&quot;: &quot;NY-SQL03&quot; }
        	]
        }
    ],
    &quot;instances&quot;: [
        { // This instance cannot use the defaultConnectionString, 
	 // so it has to specify its own.
            &quot;name&quot;: &quot;NY-DB05&quot;,
            &quot;connectionString&quot;: &quot;Data Source=NY-DB05;Initial Catalog=bob;Integrated Security=SSPI;&quot;, 
        },
        // The server name on defaultConnectionString gets replaced by &quot;name&quot;
        { &quot;name&quot;: &quot;NY-DESQL01&quot; }     ]
}</pre>
<p>If Opserver does not cover a given scenario, there are some extensibility points to augment the tool with additional dashboards and configuration options. There are plans to make this process easier and more powerful in the future:</p>
<blockquote> 
 <p>The biggest upcoming change as time allows is putting in a plugin model.&nbsp; People will be able to add tabs, views, pollers etc. that others can use.&nbsp; For example you could put a MongoDB monitoring tab up top with any level of detail you want inside.</p> 
</blockquote>
<p>The team also has other goals in the tool's roadmap:</p>
<blockquote> 
 <p>It’ll also integrate heavily with our monitoring solution, keeping data history and not just real-time data.&nbsp;</p> 
 <p>I plan on including functionality for other third-party tools in the base install to enhance Opserver if you’re using them.&nbsp; For example, <a href="http://sqlblog.com/blogs/adam_machanic/archive/2011/04/30/twenty-nine-days-of-activity-monitoring-a-month-of-activity-monitoring-part-30-of-30.aspx">sp_WhoIsActive</a> is already integrated, things like <a href="http://www.brentozar.com/blitz/">sp_Blitz</a>,<a href="http://www.brentozar.com/askbrent/">sp_AskBrent</a>, and larger products like <a href="http://www.sqlsentry.com/">SQL Sentry</a> will be tied in.&nbsp; They’ll absolutely not be required, just add views and details if they’re there...since the information they provide will then be available.&nbsp;</p> 
 <p>Opserver also exposes almost all the data it has via JSON in a REST-feeling way. I plan to make all data available this way so the UI is totally optional.&nbsp; This allows whomever to write scripts against routes returning JSON to use in other ways, it really opens up many use cases.</p> 
</blockquote>
<p>InfoQ asked why Stack Exchange decided to build its own monitoring tool. Nick told us that it grew organically:</p>
<blockquote> 
 <p>It started out as a central exception log viewer from our StackExchange.Exceptional database, a central log location for all our applications. From there as a spare time project I started adding aspects of monitoring that didn’t exist, or didn’t exist correctly already (e.g.: an <a href="https://connect.microsoft.com/SQLServer/feedback/details/779206/sql-server-2012-alwayson-availability-groups-dashboard-stops-updating-after-thread-exhaustion#details">issue</a> with SQL Server 2012's AlwaysOn monitoring).</p> From there I started adding SQL features for things we like to keep an eye on because I wanted a single place to view all our systems. After that, I started adding all the systems we use at Stack Exchange...the goal shifted from filling the gaps in existing monitoring to having a single pane of glass view of our infrastructure. 
</blockquote>
<p>&nbsp;</p><br><br><br><br><br><br></body></html>
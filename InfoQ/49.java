<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>LINQ To Logs And Traces</h3><p>Microsoft Open Technologies recently <a href="http://blogs.msdn.com/b/interoperability/archive/2014/01/06/new-release-tx-linq-to-logs-and-traces.aspx">announced</a> the release of <a href="http://tx.codeplex.com/">Tx</a>, an open source project that can help debugging using Logs/Traces, and building of real-time monitoring and alerting systems.</p>
<p>Some interesting features&nbsp;–</p>
<ul> 
 <li>Allows use of <a href="http://msdn.microsoft.com/en-us/library/bb397926.aspx">LINQ</a> on raw event sources</li> 
 <li>Enables use of <a href="http://msdn.microsoft.com/en-us/data/gg577609.aspx">Reactive Extensions</a> on real event sources with support for multiplexed event sequences (single sequence containing events of different types in order of occurence).</li> 
 <li>Possible to provide single query across multiple sources, with same API for both real-time and past history</li> 
 <li>On historical log/trace files, multiple queries can be performed in one read&nbsp;– for e.g. count all “Warning” events, match “Begin and “End” events and calculate average duration of each activity</li> 
</ul>
<p>You can either use <a href="http://www.linqpad.net/">LINQPad</a> for one-off analysis or build .NET applications for building monitoring applications. In LINQPad, the experience of Tx is as if all the events were in a database.&nbsp;</p>
<p>The release provides 4 different NuGet packages:</p>
<ul> 
 <li><a href="http://www.nuget.org/packages/Tx.Core/">Tx.Core</a>&nbsp;– common components not specific to a particular tracing format</li> 
 <li><a href="http://www.nuget.org/packages/Tx.Windows/">Tx.Windows</a>&nbsp;– Support for Event Tracing For Windows, Event logs, Performance counters from files and real-time counter API, IIS Text logs in W3C format</li> 
 <li><a href="http://www.nuget.org/packages/Tx.SqlServer/">Tx.SqlServer</a>&nbsp;– SQL Server extended events</li> 
 <li><a href="http://www.nuget.org/packages/Tx.All/">Tx.All</a>&nbsp;– A convenience package with all of the above</li> 
</ul>
<p>Note that Microsoft also advises <a href="http://tx.codeplex.com/SourceControl/latest#Doc/WhenToUse.md">when not to use Tx</a>&nbsp;as well&nbsp;-</p>
<ul> 
 <li>When there are no real-time feeds involved and data is already in memory or in a <a href="http://tx.codeplex.com/SourceControl/latest#Source/Tx.Windows/IIS/W3CEnumerable.cs">single file that is easy to parse</a>, the guidance is to use LINQ-To-Objects instead of Tx.</li> 
 <li>When there are real-time feeds but each feed/file contains only a single type of events, use only Reactive Extensions</li> 
</ul>
<p>The tool has been in use internally at Microsoft in the WCF and Service Bus teams and is now open for all .NET developers to use for their own projects. You can have a look at <a href="http://tx.codeplex.com/documentation">the documentation</a> to get started.&nbsp;</p><br><br><br><br><br><br></body></html>
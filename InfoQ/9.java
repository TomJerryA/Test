<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Highlights from Build 2014’s Second Keynote</h3><p>Today felt like a day of housekeeping. Mostly it was about promoting products from preview/beta to production status. There were some big revelations around opening sourcing Roslyn the formation of the .NET Foundation, but even these were just doing what the community has been asking for all along.</p>
<p>The day 2 keynote opened with Microsoft’s Scott Guthre crowing about Azure’s adoption rate. Currently Azure is hosting 250K active websites and over a million SQL databases. The video game Titanfall used a pool of 100,000 virtual machines on day 1. In order to ensure a consistent experience they are literally allocating a VM from the pool for each game.</p>
<p><b>Virtual Machines</b></p>
<p>Visual Studio Integration: you can now create, destroy, and manage VMs from within Visual Studio. You can even enable remote debugging in a virtual machine directly from the IDE.</p>
<p>VM images can now capture storage devices, reducing the amount of effort needed to setup a cloned instanced.</p>
<p>The server management tool <a href="https://puppetlabs.com/">Puppet</a> now is deeply integrated into Azure. Once you have a Puppet Master setup you can provision new VMs with Puppet Agent or Chef simply by specifying the name of the puppet server.</p>
<p>Auto-scaling virtual machines has also reached general availability, though details of this capability were not discussed. This feature was <a href="http://weblogs.asp.net/scottgu/archive/2013/06/27/windows-azure-general-availability-release-of-web-sites-mobile-services-new-autoscale-alerts-support-no-credit-card-needed-for-msdn-subscribers.aspx">announced as a preview</a> last year.</p>
<p><b>Azure Website Service</b></p>
<p>In addition to .NET, PHP, Python, and Node.js, Microsoft is now offering Java support for the Azure Website Service.</p>
<p>Auto-scaling works with Azure Websites as well, allowing web servers to be dynamically added or removed as the load changes.</p>
<p>Queue driven background tasks known as <a href="http://curah.microsoft.com/52143/using-the-webjobs-feature-of-windows-azure-web-sites">WebJobs</a> can be run in the context of the Azure Website. In the past background tasks had to be run on a separate VM, which can significantly increase costs if the tasks are usually idle.</p>
<p>Every Azure Website instance will now include a free SSL certificate.</p>
<p><b>PowerShell for Visual Studio and Azure</b></p>
<p>When new ASP.NET projects are created you can provision Azure VMs at the same time. If you do so, PowerShell based deployment scripts are created at the same time.</p>
<p>And by the way, PowerShell editing is now supported by Visual Studio.</p>
<p><b>Live Editing HTML and CSS using Browser Link</b></p>
<p>Most browsers allow you to edit CSS and HTML directly in the browser. With Visual Studio 2013 you could already hook your browser (IE, Chrome, etc.) to the IDE using <a href="http://www.asp.net/visual-studio/overview/2013/using-browser-link">Browser Link</a>. With this update you can make changes to HTML or CSS in the browser and have those changes automatically reflected in the source code. Essentially the browser becomes your code editor.</p>
<p><b>Static Analysis for JavaScript</b></p>
<p>The static analysis tool <a href="http://www.jshint.com/">JSHint</a> is now integrated into Visual Studio.</p>
<p><b>Azure for Mobile</b></p>
<p>Azure’s Mobile Services now support Active Directory using OAuth tokens. These tokens can then be used to access <a href="http://msdn.microsoft.com/en-us/library/office/dn605892(v=office.15).aspx">Office 365 APIs</a> in addition to the application’s custom backend.</p>
<p>In the demo they showed using a mobile device to fill in a form which was then stored as a word document in SharePoint using the mobile user’s account information.</p>
<p>Xamarin was also highlighted as part of this demo to illustrate iOS support.</p>
<p>Again remote debugging was a key feature.</p>
<p><b>Azure SQL</b></p>
<p>Databases can now grow to 500GB with a 99.95% a SLA.</p>
<p>Self-service backups are available for up to 31 days on all accounts. Administrators can choose to rollback to any point in time within that window.</p>
<p>Active Geo Replication keeps replicated servers hot so that you can fail over in the event of an outage.</p>
<p><b>HDInsight </b></p>
<p><a href="http://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html">YARN</a> and <a href="http://hive.apache.org/">Hive Query</a> are now supported in <a href="http://azure.microsoft.com/en-us/services/hdinsight/">HDInsight</a>.</p>
<p><b>Roslyn – The .NET Compile Platform</b></p>
<p>The new language services will be available in the next version of Visual Studio, but you can try it out now with an end-user preview of Roslyn.</p>
<p>The entire Roslyn project is being open sourced, including the VB and C# compilers. During the keynote Microsoft demonstrated changing the compiler to add a new language feature to C#.</p>
<p>Even more amazing is that the VS refactoring tools automatically honor the new syntax.</p>
<p><b>C# 6.0</b></p>
<p>Static using statements are supported so you no longer have to prefix static functions such as Max with the class name. This is feature already seen in Visual Basic and Java.</p>
<p><b>Xamarin</b></p>
<p>Xamarin has started supporting Roslyn with the option to choose alternate compilers in their IDE. Currently Roslyn is only active during compilation but they intend to add syntax highlighting and other features.</p>
<p><b>.NET Foundation</b></p>
<p>The .NET Foundation is a new organization for governing the various open source offerings for .NET from Microsoft, Xamarin, and others.</p>
<p><b>New Azure Portal</b></p>
<p>A new portal for Azure has been created. The primary selling point is easier to understand billing metrics. Directly from the home page you can see how much Azure is costing you on a service by service basis.</p>
<p><a href="http://appinsights.com/">AppInsights</a> is being integrated into the Azure portal. This product is used to collect data about how an application is being used in terms of features, duration, etc. It also includes performance and error metrics.</p>
<p>Team Foundation Server and web-based code editors are available. This allows you to modify an application and redeploy it from any web browser.</p>
<p>Resource groups can be created to logically associate web sites with the database and other resources that it needs. These resource groups can be turned into JSON-based templates that not only create the individual services but also cross links them with the appropriate connection strings.</p>
<p><b>Visual Studio Online</b></p>
<p><a href="http://www.visualstudio.com/en-us/products/visual-studio-online-overview-vs.aspx">Visual Studio Online</a> has finally left the beta phase (only a year late) and has reached general availability.</p>
<p><b>Moving Old VB 6 and .NET Applications Forward</b></p>
<p>The next block features WebMap2. This product takes legacy WinForms applications and converts it into an HTML based application. It does this by splitting the .NET code into views and controllers. It then converts the views into HTML while the bulk of the code lives in server-side controllers.</p>
<p><a href="http://mobilize.net/home-0/">Mobilize.NET</a> also has a product for converting legacy VB 6 applications into WinForms application. This can be used as-is or as a stepping stone into web-based technologies.</p>
<p><b>.NET Micro Framework</b></p>
<p>The <a href="http://www.netmf.com/">.NET Micro Framework</a> is finally being updated to support generics and modern versions of Visual Studio.</p>
<p><b>AppStudio: Concert Websites into Mobile Applications</b></p>
<p>The new AppStudio tool can convert websites into mobile applications. By default this is just a wrapper around the website, but you can enable caching for off-line use by modifying a configuration file. This is available for “both windows and non-windows” devices including Android.</p>
<p><b>Universal Apps and Xamarin</b></p>
<p>Microsoft briefly demonstrated a Windows Universal app recompiled with Xamarin. Unfortunately they didn’t go into details so we don’t know how much can be shared. Presumably it is still just business logic, not Common XAML.</p>
<p>More details on Azure, Roslyn, and the .NET Foundation will be available throughout the week.</p><br><br><br><br><br><br></body></html>
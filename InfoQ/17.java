<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ZeroTurnaround has Announced the Availability of LiveRebel 2.6</h3><p>ZeroTurnaround has announced the availability of LiveRebel 2.6, its software release automation tool.</p> 
<p>Version 2.6 adds the following features:</p> 
<ul> 
 <li>Support for applications built using Java, PHP, Python, PERL and Ruby.</li> 
 <li>Database updates and version control, giving operations teams the ability to update or rollback database changes along with associated applications.</li> 
 <li>Multiplatform updates, enabling teams to release applications built using multiple platforms and databases across many unlike environments.</li> 
 <li>Property management that allows deploying a single release onto several, unlike environments by applying specific configurations for each one behind the scenes.</li> 
 <li>Monitors the health of the application and the server it runs on in real-time.</li> 
</ul> 
<p>InfoQ has interviewed Krishnan Badrinarayanan ZeroTurnaround Product Marketing Manager for LiveRebel.</p> 
<p><b>I see you position LiveRebel as a test and release tool, but you are not a continuous integration tool. What does LiveRebel add to the test and release equation?</b></p> 
<blockquote> 
 <p>When you think about releasing apps, CI tools can be thought of as scripting on steroids. You can do anything with them, but you have to code and maintain it all. They do not have knowledge about your environment, configuration, database or anything else. They just trigger and execute tasks one after another and log success or failure.</p> 
 <p>LiveRebel approaches this differently. It knows everything about your environment - which servers are running, and which apps and versions are deployed. It manages and versions properties specific to environments. It understands and versions database and environment changes.</p> 
 <p>A typical use case: An agile development team releases updates every few days. The QA team picks each release up, and using LiveRebel automatically deploys it - code, DB, conf - onto their test environments. Once deployed, LiveRebel automatically calls test scripts. Once passed, the Operations team deploys the app onto the staging environment. LiveRebel automatically calls smoke tests. Finally, the operations team deploys the app onto the production environment with no downtime. If any deployment were to fail, LiveRebel automatically rolls back changes.</p> 
 <p>In the end LiveRebel releases apps - code, DB and config, all in-sync, across physical, virtual or cloud environments. Deployments are versioned, automated, fully reversible and testable. The result: teams better manage and expedite releases predictably, without compromising quality or disrupting user experience.</p> 
</blockquote> 
<p><b>Is a CI tool actually required or can LiveRebel perform CI functions as well?</b></p> 
<blockquote> 
 <p>They occupy different niches. LiveRebel doesn't do builds, it comes after the builds were done. LiveRebel is a release automation tool that also integrates with popular CI tools. For example, if the development team were to package a release by hand, they can use the LiveRebel command center to upload it, and then deploy it onto various environments, quickly and safely.</p> 
 <p>However, if the team were to use a CI tool like Jenkins, Hudson or Bamboo, they can install the LiveRebel plugin and create deployment tasks that would hand off deployment to LiveRebel. LiveRebel would then deploy the release - code, DB and conf, all together - onto selected environments with no downtime and in a failsafe manner.</p> 
</blockquote> 
<p><b> </b></p> 
<p><b>Can you talk about property management?</b><b> </b></p> 
<blockquote> 
 <p>When you release apps through testing, staging, production, or onto customer or external environments, you encounter differences in environment properties, environment variables and configuration. Often this is solved by packaging a separate release for each environment. This means that your releases are subtly different between environments and cannot be tested completely. Others have found a way to externalize these environment specific properties using home-grown scripts and tools.</p> 
 <p>With LiveRebel, release engineers can specify property sets that apply for each environment. LiveRebel then deploys the same package to all chosen environments and applies their respective property sets. It will even alert you if you are missing some properties.</p> 
 <p>This means that you can run the same release process through testing, staging and production and be sure it's tested before getting to users.</p> 
</blockquote> 
<p><b>What about the monitoring capabilities?</b></p> 
<blockquote> 
 <p>LiveRebel provides basic application and server monitoring by placing a beacon beside each app or server. The beacons pulsate based on the number of requests they receive, and turns from green to red based on their health. On mouse-over, the beacon provides a pop up with key stats on response throughput. It's not a replacement for a full-blown Application Performance Monitor, but it provides the key metrics to monitor the server and application health.</p> 
</blockquote> 
<p><b> </b></p> 
<p><b>Do you support the usual build tools, Ant, Maven, Gradle?</b><b> </b></p> 
<blockquote> 
 <p>Yes. LiveRebel offers a fully featured command line interface and REST API. So, with a couple lines of scripting, engineers can integrate LiveRebel with build tools.</p> 
</blockquote> 
<p><b>Do you integrate with Hudson, Bamboo, and TeamCity, and the various source control systems?</b></p> 
<blockquote> 
 <p>LiveRebel has ready-made plugins for Hudson, Jenkins and Bamboo. A plugin in for TeamCity is in the works. The plugins can be installed from each of their plugins menu and set up to communicate with LiveRebel securely. Once set up, you can automatically deploy releasable artifacts right from the CI tool via LiveRebel into selected environments with no downtime. All deployments are failsafe, which means if a failure were to occur, LiveRebel automatically rolls back any changes before users are impacted. Any source control system will do. For managing app configuration LiveRebel uses GIT.</p> 
</blockquote> 
<p><b>This seems like a completely different tool than sister product JRebel. Is there any kind of synergy?</b></p> 
<blockquote> 
 <p>Absolutely. It's a part of our mission to help software eat the world faster! We help software teams make the process of developing and delivering apps more pleasant and productive.</p> 
</blockquote> 
<p><b>What operating systems, Windows, Unix, Linux?</b></p> 
<blockquote> 
 <p>All of the above and the MacOS X. <a href="http://zeroturnaround.com/software/liverebel/what-we-support/#headline">Here is a complete list</a> of what we support.</p> 
</blockquote> 
<p><b> </b></p> 
<p><b>Your website says this is free. What is your pricing model?</b><b> </b></p> 
<blockquote> 
 <p>LiveRebel is free for up to 2 managed servers. Which means you can deploy apps on up to two servers that host apps for free. Database servers do not count towards this quota. Any additional managed servers can be acquired at $420 per year.</p> 
</blockquote> 
<p><b> </b></p> 
<p>Badrinarayanan told InfoQ that the next steps in product development will focus on increasing platform coverage and improving release management support. More information on LiveRebel is available <a href="http://www.liverebel.com">here</a>.</p> 
<p>&nbsp;</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
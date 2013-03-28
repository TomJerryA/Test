<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Use Canary Deployments to Test in Production</h3><p>Companies use &quot;Canary Deployments&quot; to test software in production by routing a subset of users to new functionality as part of continuous delivery according to Nolio in their <a href="http://www.noliosoft.com/resources/videos/webinar/canary/show/1/">1st video in a series about DevOps Best Practices</a>. A &quot;Canary Deployment&quot; is a type of incremental release performed by deploying a new version of software side by side with its production version counterpart. Running multiple versions of a software product side by side requires the software to be specifically designed for that configuration and flawless deployment automation.</p> 
<p>Overcoming the technical challenges involved in &quot;Canary Deployments&quot; will reduce the risk in the deployment process, allow for <a href="http://blogs.msdn.com/b/seliot/archive/2009/12/25/don-t-just-listen-to-your-users-watch-them-with-online-experiments.aspx">A/B testing</a> and pre-emptive&nbsp;<a href="http://highscalability.com/blog/2011/12/12/netflix-developing-deploying-and-supporting-software-accordi.html">performance testing</a>. A/B testing allows for new features to be tested without changing the user experience for the majority of users. The performance testing likewise would have a negligible affect on the user base as a whole.</p> 
<div>
 According to Nolio &quot;Canary Deployments&quot; consist of the following steps:
</div> 
<ol> 
 <li>Stage artifacts for deployments, including: build artifacts, test scripts, config files, and deployment manifests.</li> 
 <li>Remove &quot;Canary&quot; servers from load balancing.</li> 
 <li>Upgrade &quot;Canary&quot; application (drain and deploy).</li> 
 <li>Automated testing of application.</li> 
 <li>Restore &quot;Canary&quot; servers to load balancing (connectivity and sanity checks).</li> 
 <li>Upgrade the rest of the servers if the &quot;Canary&quot; testing with live usage is successful. (Otherwise rollback)</li> 
</ol> 
<div>
 Nolio includes in the presentation an 
 <a href="http://www.noliosoft.com/product/zero-touch-deployment">overview of using their product</a> for high level orchestration of &quot;Canary Deployments&quot;. They use an application model that can be reused in multiple processes by driving the usage of it from data. Administration and reporting are done adjacent to the &quot;Canary Deployment&quot;.
</div> 
<div>
 &nbsp;
</div> 
<p>&nbsp;</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
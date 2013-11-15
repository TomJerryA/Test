<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Apcera Continuum</h3><p>Cloud startup Apcera is making its Continuum product more visible with the launch of a new <a href="http://apcera.com/">website</a> on 14 Nov.</p>
<p>Continuum will be taking on Pivotal’s Cloud Foundry open source PaaS, which Apcera founder Derek Collison helped to create. Whilst Pivotal has enabled integration with existing enterprise infrastructure from VMware with the recent release of its commercial <a href="http://www.infoq.com/news/2013/11/pivotal-cf">Pivotal CF</a>, Apcera are focussing on a more holistic policy based approach. In an introductory blog post ‘<a href="http://apcera.com/blog/why-were-here/">why we’re here</a>’ Collison writes :</p>
<blockquote>
 For enterprise IT to out-innovate its competitors, it needs to put policy front and center, successfully blend delivery models (IaaS, PaaS, SaaS) in one platform, and enable semantic awareness of communications. 
 <div>
  &nbsp;
 </div> 
 <div>
  Today, PaaS is still a first-generation cloud-computing model, framed around making developers’ lives easier. What PaaS doesn’t do is address critical enterprise needs such as governance, policy, compliance, authentication, identity, security, auditing, etc. The more we see people using PaaS, the more we understand its limitations. There has never been a single, fully enterprise-grade platform that makes all delivery models work together in compliance while accelerating both Dev and Ops. Up until now, it wasn’t clear how that could happen.
 </div> 
</blockquote>
<p>Apcera have chosen not to go down an open source route to market, though they have open sourced some components such as <a href="https://groups.google.com/forum/#!topic/natsio/amSefF3TbDI">gnatsd</a> ‘a high performance NATS server’, which is used within Continuum for messaging. Collison has promised to open source more of the product over time, but explains why Continuum isn’t fully open source:</p>
<blockquote>
 Ecosystem engagement is a delicate balance. In my previous efforts from within Google to VMware, there were different tools to try to achieve this goal. A common one that has become table stakes is to open source the tool, software or platform. This does drive growth, but I will argue it does not, in itself, solve the ecosystem engagement and nurturing that is required long term. 
 <div>
  &nbsp;
 </div> For instance, if a system is open source, but is not purposely built to be programmable, extensible, and composeable from the inside out, different members of the ecosystem will drive the platform in different ways, leading to an implicit forking problem, where your version has diverged quickly from the lead member, and presents ever-increasing costs to merging back to the main branch. This can be seen in many popular IaaS and PaaS solutions on the market today that are driving ecosystem engagement primarily through open source. 
</blockquote>
<p>Some of the capabilities that Apcera are demoing for Continuum look a lot like <a href="http://www.infoq.com/news/2013/10/dotcloud-renamed-docker">Docker’s</a> approach to lightweight virtualization. Collison explains what’s actually going on under the hood:</p>
<blockquote>
 Within Continuum, everything to us is just a job, a workload that our platform runs, manages, monitors, and allows users to update, report on and govern. There is no difference in our mind and within our platform between an OS, a legacy app, or a web or mobile application using a modern framework. 
 <div>
  &nbsp;
 </div> These things all need isolation in order to achieve many of the goals mentioned above. In that regard, we at Apcera always speak in terms of Isolation Contexts. Isolation Contexts are always isolated, insulated, and autonomous. We believe they are many ways to achieve this, from full-on virtualization with a hypervisor, to lighter-weight primitives like Linux containers, or Solaris Zones, and even micro-task virtualization that’s driven directly by hardware CPUs as popularized by companies like Bromium. 
 <div>
  &nbsp;
 </div> We implemented our first version using the underlying primitives to Linux containers, and there will be many more. Heterogeneous and hybrid are the norm, and one size does not fit all. Lost in our definition could be autonomous, but this one is very important to us. What we mean by autonomous is that every job within the system can only communicate with endpoints that are allowed and defined by policy. This policy reaches from physical access to the networking layer, to addressing, discovery and semantic awareness of communication protocols as mentioned above. Again, this is an extremely powerful pattern. Some have called this Application SDN. We believe we are the first to have really taken this problem head on. And of course, as a modern platform, this is all transparent to the user, and as things change, move, and restart, Continuum handles all of the undifferentiated heavy lifting for you, while supplying secure audit logs for every state transition within the system. With policy built into the core of the architecture, customers gain visibility, insight and compliance from day one.
</blockquote>
<p>Apcera have been an early and vocal adopter of the <a href="http://www.infoq.com/presentations/Go-Google">Go</a> programming language, which is used extensively throughout the platform. Meanwhile Cloud Foundry have been migrating components such as their router, logging system, health manager and <a href="http://blog.cloudfoundry.com/2013/11/09/announcing-cloud-foundry-cf-v6/">CLI</a> over to Go to take advantage of its suitability for highly concurrent applications.</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Designing SOA Systems with ServiceMatrix</h3><p>The <a href="http://particular.net/service-platform">Particular Service Platform</a> has four headline components: ServiceMatrix, ServiceInsight, ServicePulse, and the well-respected NServiceBus. Over the next few weeks, we’ll be looking at each in turn starting with ServiceMatrix, their SOA design tool.</p>
<p><a href="http://docs.particular.net/servicematrix/getting-started-with-servicematrix-2.0">Service Matrix</a> can be thought of as a <a href="http://en.wikipedia.org/wiki/Computer-aided_software_engineering">CASE tool</a> for SOA architectures. You start by using a visual designer to create endpoints and messages. The end points can be based on ASP.NET MVC or <a href="http://docs.particular.net/nservicebus/the-nservicebus-host">NServiceBus Hosts</a>.</p>
<p>&nbsp;<img alt="" _p="true" src="http://docs.particular.net/servicematrix/images/servicematrix-sales-undeployed.png" /></p>
<p>We spoke with Udi Dahan, CEO of Particular Software, about how he sees the product,</p>
<blockquote> 
 <p>You can think about ServiceMatrix as a force multiplier for team leads and architects.</p> 
 <p>By having a graphical representation of endpoints, messages, processing logic, and the routing between them, this makes it much easier to make sure everyone on the team knows how their piece of the system works with everything else and for the leads to know that the team haven’t drifted away from the original design.</p> 
 <p>ServiceMatrix also automates a lot of the repetitive steps of creating new endpoints, making it much easier for teams to consistently follow best practices, all the while keeping all of that in extensible T4 templates that architects can tweak.</p> 
</blockquote>
<p>InfoQ: Visual tools such as BizTalk tend to have a bad reputation for making anything that is non-trivial significantly more difficult. How does ServiceMatrix avoid that problem?</p>
<blockquote> 
 <p>I think the way that we avoid falling into many of the issues that other visual tools (like BizTalk) run into is that the platform is based on NServiceBus – a purely code-centric development framework and runtime. For years we’ve been honing and improving on NServiceBus so that developers have the most friction-free coding experience.</p> 
 <p>In doing that, we uncovered certain areas that were better handled visually – like the routing of messages between endpoints. Other things we found was that when people wanted to choose a common error or audit queue for their system, they had to either manually make sure to set that up for every new endpoint they created or to build some infrastructure to get that set by default. These were opportunities for us to provide global settings in ServiceMatrix which would then be automatically applied.</p> 
 <p>In some cases, what we found when working on ServiceMatrix was that by making certain improvements to NServiceBus, the UI in ServiceMatrix could be simplified even further.</p> 
 <p>In short, by taking a platform perspective (rather than just a Visual/code-generation perspective) we’re hoping to strike the right balance between doing as little as possible and as much as necessary, eventually reaching that elusive state – “not when there is nothing more to add, but when there is nothing left to take away”.</p> 
</blockquote>
<p><a href="http://docs.particular.net/servicematrix/customizing-extending">ServiceMatrix stays code-centric by&nbsp;using code generation and partial classes</a>. Here is a typical example of a service method created by ServiceMatrix.</p>
<pre>
namespace OnlineSales.Sales
{
    public partial class SubmitOrderHandler : IHandleMessages&lt;SubmitOrder&gt;
    {
        public void Handle(SubmitOrder message)
        {
            // Handle message on partial class
            this.HandleImplementation(message);
        }
        partial void HandleImplementation(SubmitOrder message);
        public IBus Bus { get; set; }
    }
}</pre>
<p>This code would be managed by ServiceMatrix itself; the developer is responsible for implementing the partial method HandleImplementation. Dependency injection is important part of this pattern. In order to support outgoing messages, a reference to the service bus is exposed via the Bus property.</p>
<p>By default message handlers are stateless. If you want something more sophisticated with support for long running operations then you need to look into <a href="http://docs.particular.net/nservicebus/sagas-in-nservicebus">NServiceBus Sagas</a>.</p>
<blockquote> 
 <p>Any process that involves multiple network calls (or messages sent and received) has an interim state. That state may be kept in memory, persisted to disk, or stored in a distributed cache; it may be as simple as 'Response 1 received, pending response 2', but the state exists.</p> 
 <p>By default, NServiceBus stores your sagas in RavenDB. The schema-less nature of document databases makes them a perfect fit for saga storage where each saga instance is persisted as a single document. There is also support for relational databases using NHibernate . NHibernate support is located in the NServiceBus.NHibernate assembly. You can, as always, swap out these technologies, by implementing the IPersistSagas interface.</p> 
</blockquote>
<p>When ServiceMatrix generates a handler for a saga, it injects a Data property for handling saga related information as well as methods such as MarkAsComplete to manipulate lifecycle.</p>
<p><a href="http://particular.net/licensing">ServiceMatrix is licensed</a> as part of the Particular Service Platform. Pricing is dependent on the deployment model and either the number of nodes or developers.</p><br><br><br><br><br><br></body></html>
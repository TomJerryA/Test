<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Applying Use Cases in Agile: Use Case 2.0, Slicing and Laminating</h3><p>To incrementally develop and deliver products using agile software development, requirements are gathered and organized into a product backlog. A requirement technique that is used in agile software development is use cases. Some techniques to apply use cases for managing product requirements in agile are use case 2.0, slicing and laminating.</p>
<p>Shobha Rangasamy Somasundaram and Amol Sharma wrote a blog post about <a href="http://www.infosysblogs.com/infosys-labs/2013/10/can_formal_requirement_methods.html">can formal requirement methods work for agile</a> in which they compare the usage of requirements between waterfall and agile software development:</p>
<blockquote> 
 <p>In traditional software development or waterfall process, the following methods are used during the requirements phase - brain storming, questionnaire, modeling, prototyping, observation, focus group, survey, reverse engineering, interview, document analysis, workshop for joint application development (JAD) - collaboration &amp; domain model creation. In waterfall, requirements are sourced from the client, the BA and the product owner, wherein, they interact and prepare the final requirements document. Once the requirements are finalized, they are conveyed to the development team.</p> 
</blockquote>
<blockquote> 
 <p>(…) requirements in agile are no longer committed to the beginning of the project or limited to a few individuals, but are a perpetual driver for the entire software development lifecycle. Agile does not prescribe any one way to document the requirements, the focus is instead on &quot;just enough&quot; documentation. Details are discovered and unfold slowly only when they are required. The monolithic dedicated &quot;requirements stage&quot; is broken and dispersed, that it now becomes omnipresent, with the same traditional analysis methods, performed throughout the lifecycle.</p> 
</blockquote>
<p>In their blog post Shobha and Amol provide a detailed description on how to combine roadmaps, use cases and user stories to manage the product requirements.</p>
<p>Andy Hayward explored different requirement techniques in a series of blog post. In <a href="http://whyarerequirementssohard.wordpress.com/2013/10/16/when-to-use-user-stories-use-cases-and-ieee-830-part-2-use-cases/">when to use user stories, use cases and IEEE 830 – Part 2: Use cases</a> he mentions several use case formats:</p>
<blockquote> 
 <p>Use cases can be written in a highly formal format to describe the process extremely precisely, or in a simple paragraph format, what Alistair Cockburn described as a “Use Case Brief”, which is slightly more detailed than a User Story, and there are many variations in between. This gives the analyst a broad range of options to fit her use cases to the project need. Unfortunately, most organizations enforce a standard template for use cases which limits this flexibility.</p> 
</blockquote>
<p>Breaking down use cases into smaller parts can be difficult as Andy explains:</p>
<blockquote> 
 <p>The problem with use cases is that they usually encapsulate a lot of requirements into one large chunk of information. This makes it hard for development teams to estimate the use case’s complexity and plan their work, and hard for the business to provide a meaningful estimation of value or priority. It’s possible to break each use case down into a list of ‘scenarios’ that describe each possible path through the steps, but if you’re doing that much additional work you might as well write “The system shall” in front of each scenario.</p> 
</blockquote>
<p>The webpage <a href="http://www.ivarjacobson.com/Software_Use_Case_Essentials/">use case 2.0 essentials practice</a> provides an overview (based on the <a href="http://www.ivarjacobson.com/Use_Case2.0_ebook/">Use-Case 2.0 ebook</a>) of how to capture requirements with use case slicing:</p>
<blockquote> 
 <ul> 
  <li>Describe exactly what a software system must do</li> 
  <li>Group parts of the requirements together for broad-brush scope management</li> 
  <li>Slice the requirements to create well-formed product backlog items and drive iterative development</li> 
  <li>Change the priority of what the customer wants at any time</li> 
  <li>Produce a simple visual model, and meaningful requirements, that are understandable to developers and customers alike</li> 
  <li>Realize the benefits of iterative and backlog-driven management practices such as Scrum, and the IJI Iterative Essentials</li> 
  <li>Capture their requirements just-in-time, and in just enough detail, to support their business goals.</li> 
 </ul> 
</blockquote>
<p>You can do use case slicing in agile to incrementally develop and deliver products:</p>
<blockquote> 
 <p>The Use-Case 2.0 Essentials practice starts by finding actors and use cases, and selecting and prioritizing the parts (slices) of the use cases to be developed. It continues by detailing the use-cases slices and more importantly their tests, and then implementing software to meet the tests. It concludes by executing the tests, tracking progress in terms of verified, working software and feeding back the results in order to handle change and better support the team.</p> 
</blockquote>
<p>Building a product starts with a skinny system as <a href="http://www.infoq.com/author/Ivar-Jacobson">Ivar Jacobson</a> described in his blog post <a href="http://blog.ivarjacobson.com/architecture/">architecture</a>:</p>
<blockquote> 
 <p>[A skinny system] has all significant paths through the use cases (or scenarios); it has all significant subsystems, components, classes, nodes. Usually this skinny system only includes 5-15% of the final code, but enough to demonstrate that the significant elements work. And most important, we know that this skinny system can grow to become the complete system.</p> 
</blockquote>
<p>In the blog post <a href="http://blog.xebia.com/2012/07/12/improving-user-stories-with-usecases/">improving user stories with use cases</a> Richard Schaaf described how use case 2.0 can help to manage the product requirements with use cases. According to Richard, the problems that organizations have with user stories have to do with process that is used to define them:</p>
<blockquote> 
 <p>The issue here is (..) that it is really hard to write User Stories in such a way that they really help and are useful in the long term. What we need is not a replacement for User Stories, but a better way to come up with them.</p> 
</blockquote>
<blockquote> 
 <p>Quite often, the Product Backlog degenerates over time and this leads to real problems for the teams. If you want to have a really successful Agile organisation, you really need to focus on the process of User Story generation.</p> 
</blockquote>
<p>He suggests using use case slices to define your user stories:&nbsp;</p>
<blockquote> 
 <p>A use-case slice is a collection of front-to-back flows through a use case, including the associated test cases that is of clear value to the customer. A front-to-back flow is called a use-case story.</p> 
</blockquote>
<p>Richard explains how you can break down a use case into use case stories, and use them to define use case slices which can be the user stories that we need for our product backlog:</p>
<blockquote> 
 <p>If you did your use-case modelling right, each of these use-case stories has a certain value. A use-case slice is then simply a selection (one of more) of these use-case stories, plus a number of test cases that should be met.</p> 
 <p>A use-case slice defined in this way meets all the criteria for being a User Story. After all, we know who it is for (the initiating actor), what is requested (the use-case stories and test cases) and the value (derived from the way the use case was constructed). Thus a use-case slice <strong>is</strong> a User Story and can be used as an item on the Product Backlog.</p> 
</blockquote>
<p>Some of the advantages of using use case slices according to Richard are:</p>
<blockquote> 
 <p>By putting the use cases in a central position, the focus is always on the entire system.</p> 
 <p>The level of detail is a discussion item early on, so we end up with just enough detail, just in time.</p> 
 <p>The definition of a use-case slice ensures that each User Story is a front-to-back Story that actually focuses on value.</p> 
</blockquote>
<p><a href="http://www.infoq.com/author/Alistair-Cockburn">Alistair Cockburn</a>&nbsp;wrote&nbsp;<a href="http://alistair.cockburn.us/Laminating+not+slicing">laminating not slicing</a>&nbsp;where he describes a metaphor which he calls “laminating”:</p>
<blockquote> 
 <p>However, the language is backwards, we are not starting with an elephant, and deconstructing it into slices. We are starting from nothing and constructing the elephant. Having a pile of elephant slices does not produce an elephant. What we want to discuss is the sequence of laminations that produce the best-semblance of an elephant in the least time.</p> 
</blockquote>
<p>Laminating starts with a <a href="http://alistair.cockburn.us/Walking+skeleton">walking skeleton</a>:</p>
<blockquote> 
 <p>A walking skeleton is a tiny implementation of the system that performs a small end-to-end function. It need not use the final architecture, but it should link together the main architectural components. The architecture and the functionality can then evolve in parallel.</p> 
</blockquote>
<p>How can a walking skeleton of a software product or system look? Alistair provides some examples:</p>
<blockquote> 
 <p>What constitutes a walking skeleton varies with the system being designed. For a client-server system, it would be a single screen-to-database-and-back capability. For a multi-tier or multi-platform system, it is a working connection between the tiers or platforms. For a compiler, it consists of compilation of the simplest element of the language, possibly just a single token. For a business process, it is walking through a single and simple business transaction (as Jeff Patton describes in the technique Essential Interaction Design, later in this chapter).</p> 
</blockquote>
<p>From the walking skeleton you start to laminate outwards as Alistair described in <a href="http://alistair.cockburn.us/The+A-B+work+split%2c+feature+thinning+and+fractal+walking+skeletons">the A-B work split, feature thinning and fractal walking skeletons</a>:</p>
<blockquote> 
 <p>I put part of the feature F on the steeply rising part of the curve, and said, “Just do enough of the feature to be sure you can do the rest of the feature without trouble (that’s the A part). Now defer the rest of the feature F (the B part) to the tail of the curve. You know you can grab for B at any time.</p> 
</blockquote>
<p>Alistair provides several strategies on how you can do the A-B work split to determine and prioritize thin features that you can use to develop your product incrementally:</p>
<blockquote> 
 <ul> 
  <li><a href="http://alistair.cockburn.us/The+A-B+work+split">The A-B work split</a> says to implement just enough of a feature to be sure you can grab the rest of it at any time.</li> 
  <li>Jeff Patton’s <a href="http://alistair.cockburn.us/Feature+thinning">Feature thinning</a>&nbsp;does something different — he implements enough of the feature to argue that it really works, just isn’t very glossly (like having ordinary brakes on a car, but not anti-lock brakes).</li> 
  <li>The <a href="http://alistair.cockburn.us/Walking+Skeleton">Walking Skeleton</a>&nbsp;strategy says to get the barely minimal (sub-minimal?) functionality running to establish connections between the parts. Jeff recently expanded that to having a mini – walking skeleton for each story (<a href="http://agileproductdesign.com/blog/the_new_backlog.html).">http://agileproductdesign.com/blog/the_new_backlog.html).</a> Gery Derbier wrote me with the phrase recursive or fractal walking skeletons to describe this, a nice phrase. He says they use them on his project and they like them a lot. I would think so —- It’s vaguely related to the A-B work split and hence has risk reduction characteristics. I’m not sure if Jeff has feature thinning in mind with his mini (fractal) walking skeletons, but I think they’re possibly slightly different from each other.</li> 
 </ul> 
</blockquote>
<p>How do you manage your product requirements with use cases: Use Case 2.0, slicing, laminating, or in another way?</p><br><br><br><br><br><br></body></html>
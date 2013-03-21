<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Should You Create User Stories for Technical Debt?</h3><p>Agile teams sometimes struggle with the planning of pure technical tasks, like tasks that have to do with technical debt. Such tasks&nbsp;have no direct value for the user of a system, but have to be done to deliver working software. Should&nbsp;you create user stories to handle such technical tasks and technical debt, or not?</p> 
<p>In the blog post <a href="http://www.industriallogic.com/blog/as-a-developer-is-not-a-user-story/">&quot;As a Developer…” Is Not a User Story</a>, Bill Wake talks about user stories that he encountered which do not have value for the customer. As an example he mentions the user story &quot;As a developer, I want to configure Jenkins so that we have continuous integration&quot;. Bill explains why he thinks we shouldn't call them user stories:</p> 
<blockquote> 
 <p>My argument is not that those activities are not good or important things to do (they are for this team), but that thinking of them as user stories misleads the team and its customers. Writing something in the <i>form</i> of a user story when it's not about <i>users</i> of the system misses the point.</p> 
</blockquote> 
<p>His opinion is that we should call them tasks in stead of user stories. Applying lean thinking, he considers them to be waste:&nbsp;&nbsp;&nbsp;</p> 
<blockquote> 
 <p>From that perspective [of lean thinking], many of the activities teams do can be regarded as a type of waste, but we don't know how to develop software effectively without doing them. Lean teams talk about this kind of waste as &quot;Non-Value-Added But Necessary&quot;: work we do because we have to.</p> 
</blockquote> 
<p>Bill suggests to be critical on user stories where the role is somebody from development, in stead of an actual user of the software. Try to reframe such a user stories as functional behavior or quality characteristic and rephrase it, if that isn't possible then consider it to be a task. Task are there for the development team to track, but should not be put on the backlog as user stories since they&nbsp;are not delivering value:</p> 
<blockquote> 
 <p>(…) recognize that your team will sometimes just have tasks. You may decide to track tasks internally, but don't treat them or track them as direct progress on the developed system.</p> 
</blockquote> 
<p>Mattias Marschall provides a solution on how to handle technical tasks in a backlog, in the blog post <a href="http://www.agileweboperations.com/how-to-translate-business-value-of-things-that-are-technically-important">how to translate “business value” of things that are technically important</a>. He starts by explaining how he sees the relationship between user stories and technical tasks:</p> 
<blockquote> 
 <p>User Stories should describe what a user wants the system to do. Purely technical tasks should usually be implemented as part of a User Story.</p> 
</blockquote> 
<p>But what about&nbsp;technical tasks which are not&nbsp;directly related to a specific user story? Mattias suggest&nbsp;to put them on the product backlog:</p> 
<blockquote> 
 <p>To be able to put technical tasks into the product backlog for prioritization, just create a User Story for each of them. But, isn’t that cheating? Not if you can answer these two questions:</p> 
 <ol> 
  <li>Who benefits from the result?</li> 
  <li>Why is this task necessary?</li> 
 </ol> 
</blockquote> 
<p>With his solution you can have all the technical tasks covered by user stories in the backlog, either as a part of a user story for a customer, or with a user story specifically for the technical tasks:</p> 
<blockquote> 
 <p>If you’re able to formulate your technical tasks as a kind of User Story, your stake holders will be able to understand the necessity of them and will be able to prioritize them along with other User Stories.</p> 
</blockquote> 
<p>Bastian Buch explains in his blog post <a href="http://www.codovation.com/2012/06/effective-steps-to-reduce-technical-debt-an-agile-approach/">effective steps to reduce technical debt: an agile approach</a> that developers and product owner can have a different opinion on technical tasks that are related to technical debt:</p> 
<blockquote> 
 <p>Developers know about technical debt and are aware that it is important to face this problem.</p> 
 <p>Product Owner often doesn’t understand the need and benefits of reducing technical debt and don’t consider or allow technical projects / stories in their backlog and release plan.</p> 
</blockquote> 
<p>He suggests that the&nbsp;product owner should take responsibility for reducing technical debt. Team members should discuss technical debt with the product owner, and work together&nbsp;to give&nbsp;it the right priority on the product backlog:</p> 
<blockquote> 
 <p>The team should remember the product owner that he is part of the team: his pain is the pain of the team and other way round. He is not the customer, payer or employer of the team but more a SME (subject matter expert) and manager / analyst of product requirements from different stakeholders.</p> 
</blockquote> 
<blockquote> 
 <p>As a team give your product owner the guarantee that growth of the product will stay the most important part – but not just in a short team (Performance) but also in a long term (Health) manner.</p> 
</blockquote> 
<p>Bastian&nbsp;proposes that we should collect the technical problems into user stories, estimate&nbsp;the effort needed to solve it and&nbsp;the benefits that solving would bring. He calls the benefits “payment”, as solving the problem reduces the technical debt:</p> 
<blockquote> 
 <p>(…) we created stories marked as “TechnicalDebtItems” in JIRA for each task we defined. For bringing those items into a prioritized order and for drawing the right conclusions, we created a chart to visualize how the efforts relate to the payment and vise versa.</p> 
</blockquote> 
<p>Making things visible helps the product owner and the team to collaboratively reduce technical debt.</p> 
<blockquote> 
 <p>[With] the visualization of the debt and the finding of a possible repayment plan (…) the team now can focus on the most important steps. An important side effect: This overview is also a great tool for working with the product owner and other stakeholders because it gives him a good transparency regarding technical debt.</p> 
</blockquote> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
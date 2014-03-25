<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Managing your Software Debt</h3><p>Software debt exists in different ways. <a href="http://www.infoq.com/technicaldebt/">Technical debt</a>&nbsp;is widely known, some other forms are competence debt and quality debt. Software debt can cause product maintenance costs to increase and can depress developers. Several solutions exist to manage software debt.</p>
<p>In the blog post&nbsp;<a href="http://www.leanway.no/competence-debt/">the other kind of software debt</a> Niklas Bj&ouml;rnerstedt talks about “competence debt”. He defines it as:</p>
<blockquote> 
 <p>The gap between what is in your codebase and how much of it you understand.</p> 
</blockquote>
<p>To keep software maintenance low you should pay attention to both technical debt and competence debt, as Niklas explains:&nbsp;</p>
<blockquote> 
 <p>Just as technical debt inexorably grows with time unless you fight it, competence debt also grows with time. The biggest difference between the two types of debt is that while technical debt grows faster the more you change a codebase, competence debt grows faster if you stop changing it! Competence debt is therefore a problem that is most acute in mature systems where active development has ended.</p> 
</blockquote>
<p>Niklas&nbsp;proposes two techniques that can be used to reduce your debt: programming in pairs and code refactoring:&nbsp;</p>
<blockquote> 
 <p>For me, the real value of pair programming is in reducing both technical debt and competence debt. By pairing, team members broaden the areas of the codebase they are familiar with and increase overlap. In a similar manner, the value of refactoring is not just the reduction of technical debt. Refactoring is a great way of reducing competence debt too. It is only when you can change a system that you truly understand it.</p> 
</blockquote>
<p>When competence debt is accrued&nbsp;the effort needed to maintain systems increases, up to a point where organizations start to consider replacing the system:</p>
<blockquote> 
 <p>People would claim that the old system was impossible to maintain when the real problem was that they did not understand how it worked. Yes, technical debt made things worse since the confusing code and lack of automated tests made it frustrating to understand the system. The impulse to rewrite typically comes when too few of the original developers are left and the business is unable to find new developers that are able or willing to learn.</p> 
</blockquote>
<p>Mike Hustler wrote a blog post about&nbsp;<a href="http://www.appneta.com/blog/agile-technical-debt/">the most agile way to manage technical debt</a>&nbsp;where he discusses how to balance&nbsp;between developing product capabilities and managing technical debt.&nbsp;He explains&nbsp;how handing products over to a&nbsp;maintenance team can lead to increasing technical and competence debt:</p>
<blockquote> 
 <p>I have seen organizations build a separate maintenance team that is, for example, half the size of the new-feature team. In my opinion, this is the wrong approach (at least for the size of teams we work with). (…) The follow through which comes from the pride of ownership is lost because someone else is dealing with the bugs created by a different person, in fact a different team. Without solid communication, the backstory of why a certain initial approach was taken is lost. The domain knowledge is not present and thus the efficiency in fixing the issue is reduced. Even worse, I’ve seen maintenance teams of less experienced developers have trouble identifying the root cause of issues, resulting in band-aid fixes where rework would be preferred.</p> 
</blockquote>
<p>Technical debt depresses&nbsp;developers and can make them&nbsp;decide to leave which increase competence debt as Cory House&nbsp;described in his blog post&nbsp;<a href="http://blog.pluralsight.com/7-reasons-clean-code-matters">7 reasons clean code matters</a>:</p>
<blockquote> 
 <p>Writing sloppy or confusing code injects technical debt into our projects. And while technical debt can be useful when carefully considered in context, excessive technical debt is depressing and drives talent away from the organization. When the easy things become hard, developers start voting with their feet and go elsewhere. Developers derive more job satisfaction out of the quality of their work than the quantity. Technical debt decreases the chance of reuse and sets a low bar for quality throughout the rest of the code base.</p> 
</blockquote>
<p>David Hammerslag wrote&nbsp;the blog post&nbsp;<a href="http://www.bigvisible.com/2013/10/want-predictability-avoid-quality-debt/">want predictability? Avoid quality debt</a>&nbsp;where he&nbsp;discusses the effects of leaving defects that have been found in the code unsolved. His definition of quality debt is:</p>
<blockquote> 
 <p>Quality Debt is a measure of the effort needed to fix the defects existent in a software product at any given point in time.</p> 
</blockquote>
<p>He compares quality debt with technical debt:&nbsp;</p>
<blockquote> 
 <p>Technical debt is a measure of the quality of the design and the code, which is the internal quality of the software. Quality debt is a measure of the external quality of the code, the things that the user sees and experiences. A user never (directly) sees technical debt.</p> 
 <p>A program could be completely quality debt free and have a huge technical debt. It could correctly implement all the required and expected functionality and run flawlessly. Yet its technical debt could be enormous, exhibiting every poor software design and implementation you can imagine. On the other hand, the best designed, most sublimely elegant code could still produce wrong results or be missing functionality.</p> 
</blockquote>
<p>&nbsp;Quality debt shouldn’t be ignored as David explains:</p>
<blockquote> 
 <p>Quality Debt is much like a financial debt: the older it gets the harder it is pay down. In the worst case a project puts off testing until the development is done. It is well established that the longer a defect ages the harder it is to fix. If many defects persist (either known or unknown) the effect is exacerbated as the defects mask each other, and fixes involve the same code.</p> 
</blockquote>
<p>&nbsp;David suggests several agile practices that can be used to manage defects and keep your quality debt low:</p>
<blockquote> 
 <ul> 
  <li>Definition of Done.</li> 
  <li>BDD / Automated Acceptance Testing.</li> 
  <li>Continuous Integration.</li> 
  <li>Automated Testing.</li> 
  <li>Don’t tolerate “broken windows”.</li> 
 </ul> 
</blockquote><br><br><br><br><br><br></body></html>
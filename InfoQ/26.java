<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Leveraging DDD in Core-Business Applications Using Entity Framework</h3><p><a href="http://en.wikipedia.org/wiki/Domain-driven_design"> Domain-Driven Design</a>, DDD, is all about the domain, not about persistence, <a href="http://thedatafarm.com/blog/">Julie Lerman</a>&nbsp;recently explained in a <a href="http://vimeo.com/78893724">presentation</a> at &Oslash;redev, a developer conference in Sweden.<br /> Julie, a <a href="http://mvp.microsoft.com/en-us/mvp/Julie Lerman-8987">Microsoft MVP</a> since 2003, working as a consultant on the .NET platform, has been focusing on database programming for 25 years, later years using <a href="http://msdn.microsoft.com/en-us/data/aa937723">Entity Framework</a>, (EF), but is now inspired by DDD with its focus on the domain.<br /> Her experience is that a lot of people working with DDD ignore persistence; the database becomes an afterthought at the end of development. But still, in the long run you have to get data into a database and even if Julie focuses on the domain she early on want to make sure that when the time comes to add persistence it will work.</p>
<p><a href="http://en.wikipedia.org/wiki/Domain-driven_design#Bounded_context">Bounded context</a> is for Julie one of the most important concepts in DDD. Instead of thinking about everything in an application at the same time, entities, behaviour, etc., bounded context helps her thinking about the problem in a more structured way, in subsystems. When working in customer service she can ignore interactions with other subsystems, e.g. marketing. There may be a need for an identity or a small piece of information from another context but for the most part this is bounding things within a contextual domain. This means she can focus on a smaller amount of entities at a time when thinking about persistence.<br /> When working with the same entity, e.g. a customer, in different contexts she redefines the customer entity in each context although they are all still persisted into the same Customer table. A potential extension she sees is to completely separate the contexts by using different tables, or even databases.</p>
<p><a href="http://en.wikipedia.org/wiki/Value_object">Value Objects</a> has been a confusing concept for Julie. She has heard five different explanations from DDD experts, they have all been correct and they have all enriched her view. Now, a value object for Julie is an immutable object without an identity that functions as a complex type persisted over several columns in a database.</p>
<p>Normally Julie uses the domain model also as a data model but in some very complex domains she has found a need for a separate persistence model, one scenario for this is when working with legacy databases.</p>
<p>Earlier this year Julie wrote <a href="http://www.infoq.com/news/2013/10/data-driven-to-ddd">three articles</a> about her lessons learnt moving from data-driven development into using DDD.</p><br><br><br><br><br><br></body></html>
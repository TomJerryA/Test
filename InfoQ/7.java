<p>Developers can apply the Bounded Context concept from <a href="http://en.wikipedia.org/wiki/Domain-driven_design">Domain Driven Design</a> (DDD) to divide a large model into smaller models using the Database Context (DbContext class) in <a href="http://msdn.microsoft.com/en-us/data/aa937723">Entity Framework</a> (EF), <a href="http://thedatafarm.com/blog/">Julie Lerman</a> recently <a href="http://msdn.microsoft.com/en-us/magazine/jj883952.aspx">explained</a> in MSDN Magazine.</p> 
<p>Moving from a single model comprising many classes in one context to smaller models has benefits, according to Julie, a <a href="http://mvp.microsoft.com/profiles/Lerman">Microsoft MVP</a> since 2003, working as a consultant and mentor on the .NET platform. Bounded Context creates smaller, more cohesive models with boundaries between models. Julie's article builds on this but notes that Bounded Context within DDD is a larger concept than using EF DbContext, and she therefore calls her implementation �Constrained� or �Focused� DbContexts.<br /> &nbsp;<br /> By separating classes for different contexts, e.g. separating classes for customer care from classes for orders and shipping, and putting these classes into separate DbContexts, Julie splits a large context, containing all classes in an application into smaller and more focused contexts. This retains the same large underlying data model and database tables.<br /> &nbsp;<br /> When not all attributes of a class are needed within a context, a smaller, more focused class can be created that covers parts of the original classes and indirectly of the underlying database tables. This is done by using views into the database. A restriction on these classes is that they cannot be used for inserts into the database if there are non-nullable columns not under the control of the class. The DbContext will throw an exception in response to such an insert.<br /> &nbsp;<br /> Setting up the database with automatic creation of all tables, �Code First�, requires extra work with a separate �&uuml;ber-model� and a DbContext containing all classes. This complete context is then used for initialising the database.<br /> &nbsp;<br /> <a href="http://www.infoq.com/author/Eric-Evans;jsessionid=F9243E2866BAC5BF2A12B9B4FCA715A3">Eric Evans</a>, author of the original <a href="http://domaindrivendesign.org/books/evans_2003">DDD</a> book, reacted positively in a <a href="https://twitter.com/ericevans0/status/259096298198794240">tweet</a> but others have some <a href="http://stackoverflow.com/questions/13067650/bounded-dbcontexts-in-entity-framework-architecture">concerns</a> about applying a Bounded Context in this way and offer alternatives. One reaction is that this violates the concept, citing the DDD community <a href="http://dddcommunity.org/uncategorized/bounded-context/">definition</a>:</p> 
<p>�Explicitly define the context within which a model applies. Explicitly set boundaries in terms of team organization, usage within specific parts of the application, and physical manifestations such as code bases and database schemas. Keep the model strictly consistent within these bounds, but don't be distracted or confused by issues outside.�<br /> &nbsp;<br /> Entity Framework is Microsoft's <a href="http://en.wikipedia.org/wiki/Object-relational_mapping">object-relational mapper</a> for the .NET platform.<br /> &nbsp;</p> 
<p id="lastElm"></p>
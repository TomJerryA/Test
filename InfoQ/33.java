<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ORM Tool Hibernate 4.3 Released, Implementing JPA 2.1 Specification</h3><p>The final version of <a href="http://hibernate.org/orm/">Hibernate ORM 4.3</a>, a Java-based <a href="http://en.wikipedia.org/wiki/Object-relational_mapping">Object-Relational Mapping</a>, ORM, framework, was recently released, bringing support for stored procedures and entity graphs. Hibernate 4.3 is a certified implementation of the <a href="https://jcp.org/en/jsr/detail?id=338">JPA 2.1 Specification</a>, JSR 338, released in May 2013.</p>
<p>Main focus for this <a href="http://in.relation.to/Bloggers/HibernateORM430FinalRelease">release</a> has been on support for the JPA 2.1 specification and the new features defined which include:</p>
<ul> 
 <li>Standardized support for working with stored procedure and function calls, across both providers and database vendors.</li> 
 <li>Definition and execution of UPDATE and DELETE queries can now be made in a type-safe way.</li> 
 <li>Entity listeners, for implementing lifecycle events in separate classes, may now use the <a href="https://www.jcp.org/en/jsr/detail?id=299">CDI</a> standard, (JSR-299), for injection of dependencies.</li> 
 <li>AttributeConverters, which enable conversions of basic values between the representation in the database and in the corresponding objects.</li> 
 <li>Entity Graphs for defining how an entity and its sub-elements are loaded. How a graph is loaded may also be changed dynamically.</li> 
 <li>A standardized way of how schema generation is performed across providers together with a baseline of configuration settings all providers understand.</li> 
 <li>Synchronization of persistence context with the current transaction can now be controlled via SynchronizationType.</li> 
 <li>An object can now be constructed using argument values returned from a SQL query by using the @ConstructorResult annotation.</li> 
</ul>
<p>Other significant changes, not related to the new JPA specification, include:</p>
<ul> 
 <li>Increased support for <a href="http://en.wikipedia.org/wiki/OSGi">OSGi</a> environments. The plan is to further improve the support in Hibernate 5.</li> 
 <li>Support for inline dirty checking, finding which entities state has changed, based on new bytecode enhancement support within Hibernate.</li> 
</ul>
<p><a href="http://hibernate.org/orm/documentation/"> Documentation</a> has been updated to correspond with the new version.</p><br><br><br><br><br><br></body></html>
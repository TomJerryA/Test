<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Functional Relational Mapping Library Slick 2.0 Released</h3><p>The latest version of <a href="http://slick.typesafe.com/">Slick</a>, a <a href="https://typesafe.com/blog/slick-20-ga-functional-relational-mapping-made-easy">Functional-Relational Mapping</a>, FRM, library for <a href="http://en.wikipedia.org/wiki/Scala_(programming_language)">Scala</a>, comes with reverse-engineering of database schemas and new driver architecture to allow support for non-SQL databases. Changes in the recently released version 2.0 include:</p>
<ul> 
 <li>A code generator that reverse-engineers a database schema, generating all code required.</li> 
 <li>New driver architecture to enable support for non-SQL, non-JDBC databases.</li> 
 <li>Removal of the flat tuples restriction in table definitions, allowing usage of any type valid as a Query return type.</li> 
 <li>Support of heterogeneous lists for records of arbitrary size in addition to Scala tuples.</li> 
 <li>A new model for pre-compiled queries has replaced the old QueryTemplate abstraction.</li> 
 <li>Besides querying, pre-compiled queries can now also be used for update and delete operations.</li> 
 <li>Soft inserts as the default, removing the need for separate projections for inserts. The old behaviour is still supported.</li> 
 <li>New and more verbose syntax table definitions in the Lifted Embedding standard API to avoid pitfalls in earlier versions.</li> 
 <li>Support for server-side Option conversions.</li> 
 <li>An experimental feature which allows for Query scheduling, allowing usage of tables from multiple databases in a single query.</li> 
 <li>A new Activator template aiming at simplifying getting started with Slick.</li> 
</ul>
<p>In addition to these updates, more than 200 changes are included in the new release. The team have also updated the <a href="http://slick.typesafe.com/doc/2.0.0/">documentation</a>, including a new <a href="http://typesafe.com/activator/template/hello-slick">getting started guide</a>. This release is not backward compatible, a <a href="http://slick.typesafe.com/doc/2.0.0/migration.html">guide for migration</a> describes the changes from 1.0.</p>
<p>Slick is a relational database access library for the functional language Scala; corresponding to an <a href="http://en.wikipedia.org/wiki/Object-relational_mapping">Object-Relational Mapper</a>, ORM, for object-oriented languages, e.g. Hibernate.<br /> A <a href="https://groups.google.com/forum/#!forum/scalaquery">mailing list</a> for Slick users is available with more than 700 members.</p>
<p>Slick is an open source product with a BSD-style <a href="https://github.com/slick/slick/blob/master/LICENSE.txt">license</a>. <a href="http://slick.typesafe.com/doc/2.0.0/introduction.html#supported-database-systems">Supported database systems</a> include H2, MySQL and PostgreSQL. Drivers for Oracle, IBM DB2, and Microsoft SQL Server are available through a <a href="http://slick.typesafe.com/doc/2.0.0/extensions.html">closed-source extension</a>.</p><br><br><br><br><br><br></body></html>
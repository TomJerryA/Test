<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>A Proposal for a Database URI Standard</h3><p>David Wheeler has proposed a <a href="https://github.com/theory/uri-db">standard URI format for database connections</a>. This proposal would allow applications built on different technologies to share the same connection string. That would be beneficial for a wide variety of tools including report builders, automated build and deploy tools, and ORMs. The proposal uses db as its schema, which is then followed by the database engine name. This is where it first differs than current practice. Rather than specifying a specific driver, it leaves that decision to the application.</p>
<p>This is critical for a cross-platform URI standard. Sharing connection strings between JDBC, OleDB, and ODBC can be difficult because they often require different driver names to connect to the same database engine. Even within one API there may be multiple drivers available.</p>
<p>Following the engine name is a set of standardized parameters: username, password, host, port, and dbname. Again unlike current practices, these would always appear in the same order.</p>
<ul> 
 <li>db:engine://[username[:password]@]host[:port][/dbname][?params]</li> 
 <li>db:engine:[dbname][?params]</li> 
</ul>
<p>Any database specific parameters when follow a “?” much like query parameters in a HTTP request. These would use the standard key-value format.</p>
<p>Finally is an optional fragment, indicated by a “#” mark, for denoting a specific table or view.</p>
<p><img alt="" src="http://www.infoq.com/resource/news/2013/12/DB-URI-Standard/en/resources/Image1.png" _href="img://Image1.png" _p="true" /></p>
<p>The format is inspired by a number of formats that use the engine://authority/dbname convention.</p>
<ul> 
 <li><a href="http://www.postgresql.org/docs/9.3/static/libpq-connect.html#LIBPQ-CONNSTRING">PostgreSQL libpq URIs</a></li> 
 <li><a href="http://docs.sqlalchemy.org/en/rel_0_9/core/engines.html#database-urls">SQLAlchemy URLs</a></li> 
 <li><a href="http://docs.stackato.com/3.0/user/services/data-services.html#database-url">Stackato database URLs</a></li> 
 <li><a href="https://github.com/kennethreitz/dj-database-url">Django database URLs</a></li> 
 <li><a href="https://github.com/glenngillen/rails-database-url">Rails database URLs</a></li> 
</ul>
<p>There are some objections to the use of a “db:” prefix. Peter Eisentraut writes,</p>
<blockquote> 
 <p>I don't think the db: prefix is necessary. Firstly, I think having two scheme prefixes is not allowed under the syntax rules of RFC 3986. Secondly, it's not useful. A hypothetical software that can use these URIs will be able to tell what to do by the scheme itself.</p> 
 <p>URL generally identify a protocol for accessing a resource, not what the nature of the resource is. For example, a git repository can be accessed via several different URL schemes. There is no single git: URL system, let alone a scm:git: or something. Also, a browser might be able to access a file via several different protocols such as http: and ftp:. There is no single textfile: or video: URL scheme. Heck, that file might even be a database, so I'd expect something like SQLite to accept a typical http: URL as its database URL.</p> 
 <p>I don't think there is much to standardize, except asking that implementors try to faithfully adhere to RFC 3986.</p> 
</blockquote>
<p>Counter-arguments can be made. For example, without a common prefix you would have to register a separate prefix in the operating system for each and every database engine an application can connect to. This scheme would allow the application to prompt the user when a previously unknown database is encountered instead of simply failing. It would be akin to having a separate prefix for each file type instead of just using http/https and letting the browser decide what to do.</p>
<p>David Wheeler mentions other issues that need to be considered in his <a href="http://theory.so/rfc/2013/11/26/toward-a-database-uri-standard/">announcement</a>.</p>
<blockquote> 
 <p>First, the requirement that the authority part must include a host address prevents the specification of a URI with a username that can be used to connect to a Unix socket. PostgreSQL and MySQL, among others provide authenticated socket connections. While <a href="http://www.ietf.org/rfc/rfc3986.txt">RFC 3986</a> requires the host name, its predecessor, <a href="http://www.ietf.org/rfc/rfc3986.txt">RFC 2396</a>, does not. Furthermore, as a precedent, neither do <a href="http://en.wikipedia.org/wiki/File_URI_scheme#Examples">file URIs</a>. So I’m thinking of allowing something like this to connect to a PostgreSQL database</p> 
 <p>db:pg://postgres:secr3t@/</p> 
 <p>In short, it makes sense to allow the user information without a host name.</p> 
 <p>The second issue is the disallowing of relative file names in the path part following an authority part. The problem here is that most database engines don’t use paths for database names, so a leading slash makes no sense. For example, in db:pg:localhost/foo, the PostgreSQL database name is foo, not /foo. Yet in db:firebird:localhost/foo, the Firebird database name is a path, /foo. So each engine implementation must know whether or not the path part is a file name.</p> 
 <p>But some databases may in fact allow a path to be specified for a local connection, and a name for a remote connection. Informix appears to support such variation. So how is one to know whether the path is a file path or a named database? The two variants cannot be distinguished.</p> 
 <p>RFC 2396 is quite explicit that the path part must be absolute when following an authority part. But RFC 3986 forbids the double slash only when there is no authority part. Therefore, I think it might be best to require a second slash for absolute paths. Engines that use a simple name or relative path can have it just after the slash, while an absolute path could use a second slash:</p> 
 <ul> 
  <li>Absolute: db:firebird://localhost//tmp/test.gdb</li> 
  <li>Relative: db:firebird://localhost/db/test.gdb</li> 
  <li>Name: db:postgresql://localhost/template1</li> 
 </ul> 
</blockquote><br><br><br><br><br><br></body></html>
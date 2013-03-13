<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Replacing Native PHP4 Extensions with Managed Extensions</h3><p><a href="http://phalanger.codeplex.com/releases/view/103021">Phalanger</a>, the PHP runtime for .NET and Mono, has reached a significant milestone with the eleven popular PHP extensions being replaced with .NET equivalents. Previously these extensions, written in native C or C++, were limiting Phalanger to only running in 32-bit mode.</p> 
<p>Here is the list of <a href="http://www.php-compiler.net/blog/2013/phalanger-3-0-updates-for-march-2013">managed libraries include in Phalanger 3.0</a>:</p> 
<ul> 
 <li>Class Library (PhpNetClasslibrary.dll) is basic part of Phalanger containing basic set of functionality (standard,Core,session,ctype,tokenizer,date,pcre,ereg,json,hash,SPL,filter).</li> 
 <li>cURL (new) – for most common tasks, Phalanger now comes with cURL extension suporting HTTP/HTTPS protocols. Community is now free to extends its functionality as they need.</li> 
 <li>GD2, exif and image (new) are well known PHP extensions allowing to read/manipulate with images.</li> 
 <li>Iconv (new) for string encoding conversions built on .NET Encoding.</li> 
 <li>MSSQL is Microsoft SQL extension using SqlConnection internally to increase performance. It also ensures compatibility with latest Microsoft SQL servers.</li> 
 <li>PDO (new) is an abstraction over PHP database connections. Support for PDO was added, containing several DB drivers like SQLite or MySQL. Developers are free to extend PDO support with additional DB drivers now.</li> 
 <li>SoapClient (new) is managed reimplementation of PHP SOAP taking advantage of .NET built-in SOAP support.</li> 
 <li>SQLite (new) is another DB extension for Phalanger.</li> 
 <li>MySQL extension for Phalanger takes advantage of latest managed Oracle/.NET connector. This makes DB operations faster and safer, allowing to configure additional options and security options in standard .NET-way.</li> 
 <li>XML (new) extension is now contained in Phalanger too. Must-have extensions commonly used for its utf8 functions.</li> 
 <li>XMLDom extension contains support for PHP SimpleXML, dom, xsl and libxml extensions. Its feature set was extended by libxml functions and improved HTML parsing functions. The extension takes advantage of .NET XML built-in support which offers great performance and security.</li> 
 <li>Zip (new) extension was added thanks to community contributions. Anyway still needs some work to be finished.</li> 
 <li>Zlib (new) extension is essential part of many PHP projects, mainly because of its gzip compression support. A part of Phalanger now.</li> 
</ul> 
<p>Since these libraries are implemented in C# you could, in theory, use these libraries with other .NET based languages as well. And since it is <a href="http://phalanger.codeplex.com/">released under the Apache License</a>, you can extract just the parts you need.</p> 
<p>Additional PHP 5.x features are also included such as Binary number format and boolval(). Function call array dereference is working, but still experimental.</p> 
<p>In case you missed it, Phalanger Tools for Visual Studio was also updated recently. Released back in January, we saw IntelliSense improvements, region collapsing, go to definition, and support for the Class View and Object Browser.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>WCF Data Services 5.4.0 - Client Hooks and Instance Annotations on Atom Payloads</h3><p><a href="http://blogs.msdn.com/b/astoriateam/archive/2013/03/26/wcf-data-services-5-4-0-prerelease.aspx">Microsoft</a> has released a release candidate (prerelease) version of <a href="https://nuget.org/packages/Microsoft.Data.Services/5.4.0-rc1">WCF Data Services 5.4.0</a> with client deserialization and serialization hooks, instance annotations on <a href="http://www.odata.org/documentation/atom-format">atom payloads</a>, client consumption of instance annotations in addition to simplified transition between Atom and JSON formats. <br /> <br /> The client deserialization and serialization hooks provide extensibility points that enable a number of different scenarios such as modifying wire types and property names. The new release also provides support for instance annotations on Atom payloads, which is an extensibility feature in OData feeds that allow OData requests and responses to be marked up with annotations that target feeds, single entities and properties.<br /> <br /> WCF Data Services 5.4.0 has added APIs to the client to enable instance annotations to consume them, that provides an ability to indicate which instance annotations the client cares about via the Prefer header thus streamlining the responses from OData services that honor the odata.include-annotations preference. It also includes a new feature which <br /> simplifies the transition between the Atom and <a href="http://www.json.org/">JSON</a> format.<br /> <br /> WCF Data Services 5.4.0 includes several bug fixes which provide solution for the issues under the following scenarios</p> 
<ul> 
 <li>Reading a collection of complex values would fail if the new JSON format was used and a type resolver was not provided</li> 
 <li>ODataLib was not escaping literal values in IDs and edit links</li> 
 <li>Requesting the service document with application/json;odata=nometadata would fail</li> 
 <li>Using the new JSON format without a type resolver would create issues with derived types</li> 
 <li>LINQ provider on the client would produce $filter instead of a key expression for derived types with composite keys</li> 
 <li>Some headers required a case-sensitive match on the WCF DS client</li> 
 <li>A request for the new JSON format could result in an error that used the Atom format</li> 
 <li>PATCH requests for OData v1/v2 payloads would return a 500 error rather than 405</li> 
</ul> 
<p>The latest build also make it easier to track the current item in <a href="http://odata.codeplex.com/wikipage?title=ODataLib">ODataLib</a> and fixes an issue where the inability to set EntityState and ETag values forced people to detach and attach entities for some operations. The prerelease version also targets .NET Framework&nbsp; 4.0, Silverlight 4.0 and has been localized for several languages.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
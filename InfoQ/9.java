<p lang="zxx" style="margin-bottom: 0in">Microsoft's C++ REST SDK, codenamed <a href="http://casablanca.codeplex.com/">Casablanca</a> has been open sourced under the Apache license. It is described as a &quot;a Microsoft effort to support cloud-based client-server communication in native code using a modern asynchronous C++ API design.&quot; Breaking through the highlevel description, this offering uses C++11 to provide what Microsoft hopes is an easier way to write client-side HTTP code.</p> 
<p lang="zxx" style="margin-bottom: 0in"> </p>
<p lang="zxx" style="margin-bottom: 0in">Casablanca is multi-platform, supporting Linux as well as Windows 7 and Windows 8. Microsoft developer Artur Laksberg states that support WinXP for and Vista is being developed. Another highlight is its support for asynchronous operations. Microsoft's <a href="http://blogs.msdn.com/b/vcblog/archive/2013/02/26/the-c-rest-sdk-quot-casablanca-quot.aspx">announcement</a> provides some examples of a file upload via HTTP and creating a JSON object to demonstrate Casablanca in action.</p> 
<p></p> 
<p lang="zxx" style="margin-bottom: 0in">Both the Windows and Linux builds support the following feaures:</p> 
<blockquote> 
 <ul> 
  <li>Ability to create a connection to a server via a HTTP Client, send requests and handle response.</li> 
  <li>Support for construction and use of Uniform Resource Identifiers (URI).</li> 
  <li>Constructing, parsing and serializing JSON values.</li> 
  <li>Asynchronously reading/writing bytes to/from an underlying medium via Streams and Stream Buffers.</li> 
 </ul> 
</blockquote> 
<p lang="zxx" style="margin-bottom: 0in">There are several different Streams and Stream Buffers available: a memory based producer-consumer, files, a memory based stream backed by a STL container, raw pointer streams, and interop streams. This last type of stream allows for &quot;...Casablanca [to provide] two sets of classes, one to give an async stream interface to an iostream, one to give an iostream interface to an async stream.&quot;</p> 
<p lang="zxx" style="margin-bottom: 0in">The <a href="http://casablanca.codeplex.com/wikipage?title=Linux Features&amp;referringTitle=Documentation">Linux http client</a> is somewhat limited in that it does not yet support https, proxies, or authentication, but Microsoft states these features will be part of a future release. CodePlex houses <a href="http://casablanca.codeplex.com/SourceControl/changeset/view/8737b35e9171#readme.txt">Casablanca's source code</a> where it may be viewed online, obtained via Git, or downloaded as a Zip archive with the latest snapshot.</p> 
<p id="lastElm"></p>
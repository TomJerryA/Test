<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Tabris 1.0: Cross-platform Mobile Development in Java</h3><p>After three years in development, <a href="http://www.eclipsesource.com">EclipseSource</a> has released <a href="http://developer.eclipsesource.com/tabris/">Tabris 1.0</a>, a cross-platform Java mobile development framework for iOS and Android. Tabris is targeted at enterprises, and unlike other mobile solutions out there it uses a different approach:</p> 
<ul> 
 <li>Most of the programming is done in Java</li> 
 <li>The business logic including the binary representation of the client UI runs on the server side on <a href="http://eclipse.org/rap/">Eclipse RAP</a>.</li> 
 <li>A very thin client application runs on the mobile device</li> 
 <li>The server communicates with the client in JSON format, sending data and commands for creating the visual UI</li> 
 <li>The client generates the interface using native components</li> 
 <li>The client is written in Objective-C for iOS and Java for Android</li> 
</ul> 
<p>Tabris comes with a <a href="http://eclipsesource.com/blogs/2013/02/19/inside-the-tabris-ui/">UI Toolkit</a> built on top of Java SWT API. The toolkit adds two main widgets: <em>Page</em> and <em>Action</em>. <em>Page</em> contains the basic content of an application while <em>Action</em> is for taking user’s commands. <em>Page</em> is shown in red and <em>Action</em> is shown in green in the following snapshot of a demo Tabris application:</p> 
<p class="image-wide"><a href="$image[4].png;jsessionid=C0B17176B6F8FBDBEF0E6F3BB0DB474E"><img title="image" style="border-left-width: 0px; border-right-width: 0px; background-image: none; border-bottom-width: 0px; padding-top: 0px; padding-left: 0px; display: inline; padding-right: 0px; border-top-width: 0px" border="0" alt="image" src="http://www.infoq.com/resource/news/2013/04/Tabris-mobile-Java/en/resources/Tabris-1.png;jsessionid=C0B17176B6F8FBDBEF0E6F3BB0DB474E" _href="img://Tabris-1.png" _p="true" /></a></p> 
<p><em>Pages</em> can be chained and navigated, while <em>Actions</em> can be global –for the entire application-, or local – for the current page-.</p> 
<p>After processing a component, the server side of the application sends a JSON snippet to the client as the following one used to create a button:</p> 
<p><a href="$image[9].png;jsessionid=C0B17176B6F8FBDBEF0E6F3BB0DB474E"><img title="image" style="border-top: 0px; border-right: 0px; background-image: none; border-bottom: 0px; padding-top: 0px; padding-left: 0px; border-left: 0px; display: inline; padding-right: 0px" border="0" alt="image" src="http://www.infoq.com/resource/news/2013/04/Tabris-mobile-Java/en/resources/Tabris-2.png;jsessionid=C0B17176B6F8FBDBEF0E6F3BB0DB474E" _href="img://Tabris-2.png" _p="true" /></a></p> 
<p>The client app will render the button using iOS or Android native components.</p> 
<p>InfoQ has talked to <a href="http://eclipsesource.com/blogs/author/hstaudacher/">Holger Staudacher</a>, Team Lead for Tabris-server at EclipseSource, to find out more about the framework. According to Staudacher, Tabris is targeted at enterprises and requires a permanent network connection to the server:</p> 
<blockquote> 
 <p>Tabris is for On-Site mobility applications. This means it works best in a controlled environment. With controlled I mean a fixed network connection and so on. We have customers e.g. like a hospital where all devices are connected to the same network. Such applications are usually developed by the enterprise.</p> 
 <p>Tabris does not work offline. A mobile UI is basically a session. So, if the user's device loses connection the session becomes invalid. There is error handling which can be done on the mobile clients. We have implemented standard error handling for retrying sending the http request and so on. But this can be extended by the app developer with native extensions.</p> 
</blockquote> 
<p>When asked if Tabris would make sense for developing applications for the general public, Staudacher said that theoretically it could be done but it is not best fit for that purpose:</p> 
<blockquote> 
 <p>To general public means you will create a heavy load on the server. We are using standard Java EE technology there. So, if you have such a heavy load standard Java EE clustering mechanisms can be used. It's not yet tested with millions of users. But from a technical point of view it should be doable ;)</p> 
</blockquote> 
<p>Tabris <a href="http://developer.eclipsesource.com/tabris/docs/supported-api/">supports many SWT components</a> and adds support for several native sensors such as camera and geolocation.</p> 
<p>Currently, tablets are supported but such an application shows only one page at a time. Support for multiple pages is to be added in the future. Also, Tabris can be extended to other mobile platforms, and Windows will be probably supported if the framework gets traction.</p> 
<p>In the near future, the Tabris team intends to add the following functionality:</p> 
<ul> 
 <li>Address book support</li> 
 <li>Device orientation support</li> 
 <li>Client Scripting support for handling client events</li> 
 <li><a href="http://x-callback-url.com/">XCallbackUrl</a> support</li> 
</ul> 
<p>According to an <a href="http://developer.eclipsesource.com/tabris/docs/faq/">FAQ</a>, applications created with Tabris can be deployed through the App Store “as long you comply with the App Store rules”. A <a href="https://play.google.com/store/apps/details?id=com.eclipsesource.tabris.android.demos">demo application</a> for Android can be found on Google Play.</p> 
<p>Tabris is not open sourced but enterprise licensees can get access to the source code. More details can be found on <a href="http://eclipsesource.com/en/products/tabris/pricing/">EclipseSource’s pricing page</a>.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
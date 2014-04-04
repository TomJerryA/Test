<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Changes to the Silverlight Runtime for Windows Phone</h3><p>Until now we’ve been focusing on Common XAML, but now our attention turns to Silverlight for Windows Phone. Though Common XAML (i.e. Universal Apps) is meant to eventually replace it, the Silverlight framework is still a viable option for Windows Phone developers.</p>
<p><b>Landscape</b></p>
<p>Moving forward innovations and investments will be primarily directed at XAML first. They will then try to make those same features in Silverlight.</p>
<p>Roughly 90% of the Silverlight APIs are available in XAML. The intent is to move all of the remaining features into XAML in the future. Some of the more notable APIs are the Lockscreen, Lenses, VOIP, Camera, and Clipboard.</p>
<p><b>Upgrading to Windows Phone 8.1</b></p>
<p>Migrating apps from Silverlight for WP 8.0 to 8.1 is a simple process. You merely have to right-click on project and select upgrade from the menu. Since there will be a period of time when some Windows Phone 8 devices haven’t been upgraded, Microsoft recommends keeping both a WP8 and WP8.1 app in the store. (The stores still supports 7.1 as well.)</p>
<p><b>Modern Context</b></p>
<p>Silverlight 8.1 apps run in something called a “Modern Context”. In real terms this means that Silverlight 8.1 needs both a WMAppManifest and an appxManifest. Without the later you won’t be able to access newer XAML based features.</p>
<p>Silverlight 8.1 is not 100% compatible with Silverlight 8.0. For example, Array.Sort no longer uses a stable sort, which could cause problems for some applications.</p>
<p>Another concern is Fast App Resume. In Silverlight 8.0 this was an optional feature that you could turn on. Inside the Modern Context it is the only option.</p>
<p>XAML apps do not terminate when you press the Back button. Silverlight 8.1 apps will terminate by default, just like Silverlight 8.0, but you can disable it.</p>
<p>Background audio doesn’t currently work in Silverlight 8.1. It is hoped that it will be fixed in a future update.</p>
<p>Note that Silverlight 8.0 apps do not run in the modern context. This means that Silverlight 8.0 apps are 100% compatible with Windows Phone 8.1.</p>
<p><b>New APIs</b></p>
<p>Aside from what was mentioned above, all of the Silverlight 8.0 APIs are available in Silverlight 8.1. Most of the XAML APIs are exposed. A notable exception is anything dealing with Modern Resource Technology isn’t being exposed to Silverlight.</p>
<ul> 
 <li>Silverlight apps can now access the SD Card.</li> 
 <li>The Share contract can exchange binary data now. Previously it only supported text and HTML.</li> 
 <li>Silverlight applications can be Picker Providers. This allows integration with services such as Drop Box.</li> 
 <li>GeoFencing is supported.</li> 
 <li>WinRT style Background Tasks are supported in Silverlight apps.</li> 
 <li>Appointments and Calendar support has been enhanced to allow editing and deleting appointments.</li> 
 <li>Email with attachments is now supported.</li> 
 <li>Web Authentication makes using OAuth easier to use.</li> 
 <li>Accessibility support is better than before, but still limited. Unlike XAML there are no pre-defined styles but the app can at least query for accessibility settings.</li> 
 <li>Data Roaming allows phone and store apps to be associated with each other. This means user information such as settings, high scores, and save files can roam between Windows 8 and Windows Phone. This feature requires that you reserve an app name.</li> 
</ul>
<p><b>Name Reservation</b></p>
<p>When creating a new XAML or Silverlight 8.1 app, a name needs to be reserved from the Windows Store just like you would with a new WInRT app.</p>
<p>Because of the possibility of name collisions, existing Silverlight 8.0 apps do not need a matching name reservation when being upgraded to Silverlight 8.1.</p>
<p><b>Which Framework to Use</b></p>
<ul> 
 <li>New Apps: Silverlight 8.x or XAML</li> 
 <li>Existing Windows Store App: XAML</li> 
 <li>Lock Screen App: Silverlight 8.x</li> 
 <li>Camera Based App, VOIP: Silverlight 8.x</li> 
 <li>Music App: Silverlight 8.0 or XAML</li> 
 <li>Existing Silverlight Phone Apps: Silverlight 8.x or XAML</li> 
</ul>
<p>For more information see the <a href="http://channel9.msdn.com/Events/Build/2014/2-517">What’s New with Windows Phone Silverlight Apps</a> video on Channel 9.</p><br><br><br><br><br><br></body></html>
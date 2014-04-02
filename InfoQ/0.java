<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Microsoft Opens Windows to the Universal App: One App for All Platforms</h3><p class="MsoNormal" style="margin-bottom: 0.0001pt;">Today at the opening day of Microsoft’s Build developer conference the company formally announced Universal Windows apps.&nbsp; These apps will run across the Windows family of devices:&nbsp; phone, tablet, and desktop PC.&nbsp; The upcoming release of Windows Phone 8.1 will align that platform with the existing Windows 8.1 platform that exists for desktops and tablets.&nbsp; This change means that developers can write a single app that will run unmodified on all of these platforms.&nbsp; Developers will retain the ability to customize the app behavior and appearance for each environment if they desire.
 <o:p></o:p></p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">
 <o:p>
  &nbsp;
 </o:p></p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">During the keynote, Microsoft Director <a href="http://blogs.windows.com/windows/b/buildingapps/archive/2014/04/02/extending-platform-commonality-through-universal-windows-apps.aspx">Kevin Gallo</a> demonstrated this new binary by taking an existing Windows 8.1 app in Visual Studio and then added Windows Phone 8.1 compatibility in a straightforward manner.&nbsp; Under the existing solution, nodes appear in Visual Studio’s Solution Explorer for the original Windows 8.1 target and the newly added Windows Phone 8.1 target.&nbsp; A third node exists for code common to both platforms.&nbsp; Developers can control which portions of the code are stored in this common code, and which is stored in a platform specific manner.&nbsp; One advantage of this approach is that app logic can be stored in the common area to be shared by both platforms, while still allowing developers to add device specific functionality—be it keyboards and mice or the presence of GPS information on phones.
 <o:p></o:p></p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">
 <o:p>
  &nbsp;
 </o:p></p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">Under the hood, universal apps are running on the Windows Runtime, which was originally introduced with Windows 8. &nbsp;NuGet packages installed for a particular platform are by default associated with that platform, but developers have the option to reuse it for the newly added targets.&nbsp; For an example, Gallo demonstrated how JSON.NET was part of the Windows 8.1 app, and then easily added to the Windows Phone 8.1 target when that target was added to the solution.
 <o:p></o:p></p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">
 <o:p>
  &nbsp;
 </o:p></p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">&nbsp;</p>
<p class="MsoNormal" style="margin-bottom: 0.0001pt;">InfoQ is covering the Build 2014 Conference first hand and will continue to provide updates on this and all news that emerges—stay tuned.
 <o:p></o:p></p><br><br><br><br><br><br></body></html>
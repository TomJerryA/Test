<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Features of the New Windows Phone App Model</h3><p class="MsoNormal" style="margin-bottom:0in;margin-bottom:.0001pt">At Build 2014 Andrew Clinick gave a presentation titled, <a href="http://channel9.msdn.com/Events/Build/2014/2-509">“The New Windows Phone App Model”</a>, in which he described the new features of this model that is coming with Windows Phone 8.1.&nbsp;<br /> &nbsp;</p>
<p class="MsoNormal" style="margin-bottom:0in;margin-bottom:.0001pt">The first of these features is the ability to process push notifications before a <a href="http://msdn.microsoft.com/en-us/library/windowsphone/develop/jj662938(v=vs.105).aspx">toast update</a> appears.&nbsp; Previously a user would see an update appear and theny would want to immediately tap the update to act on it.&nbsp; This posed a performance problem as the app may itself be processing the event that generated the update, causing a lag between the user’s tap and the app’s response.&nbsp; Now an app may process the event, perform any updates it needs, and then generate the toast update.&nbsp; Then when the user acts on the toast the app is ready for their participation with little or no lag.
 <o:p></o:p></p>
<p class="MsoNormal" style="margin-bottom:0in;margin-bottom:.0001pt">
 <o:p>
  &nbsp;
 </o:p></p>
<p class="MsoNormal" style="margin-bottom:0in;margin-bottom:.0001pt">Developers looking for an easier way to demo their apps can benefit from the new ability to display their phone’s screen on an external display via USB.&nbsp; Newer Lumia handsets can also use a MiraCast adapter to reproduce their display as well.
 <o:p></o:p></p>
<p class="MsoNormal" style="margin-bottom:0in;margin-bottom:.0001pt">
 <o:p>
  &nbsp;
 </o:p></p>
<p class="MsoNormal" style="margin-bottom:0in;margin-bottom:.0001pt">OneDrive is taking an expanded role with Windows Phone.&nbsp; If a user customizes their phone’s start screen tile layout, that layout and associated metadata is backed up to OneDrive daily.&nbsp; This preserves the user’s experience in the event their phone is lost or damaged.&nbsp; A user’s app data is also backed up to OneDrive and each app can use 100 kilobytes for free.&nbsp; This storage does not impact the user’s personal quota on OneDrive and is not visible to them.&nbsp; (If you want to show your app’s data, the OneDrive SDK should be used.)
 <o:p></o:p></p>
<p class="MsoNormal" style="margin-bottom:0in;margin-bottom:.0001pt">
 <o:p>
  &nbsp;
 </o:p></p>
<p class="MsoNormal" style="margin-bottom:0in;margin-bottom:.0001pt">Working with the <a href="http://www.infoq.com/news/2014/04/universal_win_apps">universal Windows apps</a>&nbsp;platform, developers can send notifications to all instances of the app on a user’s devices or just specific ones.&nbsp; So for example a game may want to alert the user that it is their turn to play whether they are currently using their Windows Phone or 8.1 desktop. &nbsp;However, at present these notices don’t sync, so there is no way for your phone to tell your PC that you acknowledged the notice (so each notice would have to be closed separately.)
 <o:p></o:p></p><br><br><br><br><br><br></body></html>
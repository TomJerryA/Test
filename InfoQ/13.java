<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PhoneGap 2.5 Enables Application Cache and InAppBrowser Geolocation</h3><p><a href="http://phonegap.com/blog/2013/02/28/pg-250-released/">PhoneGap 2.5</a> has been released which enables application cache and geolocation in the <a href="http://wiki.apache.org/cordova/InAppBrowser">InAppBrowser</a> including fix for a null pointer exception which occurs when the user click the back button while the app is launched. Moreover, the release also includes a new configuration parameter named disallowOverscroll which enables you to remove blue glow when you try to scroll past the top/bottom of the screen.</p> 
<p>PhoneGap 2.5 has been updated in such a way that config.xml document should make use of &lt;widget&gt; instead of &lt;cordova&gt; including the addition of pluginInitialize method to <a href="http://docs.phonegap.com/en/2.2.0/guide_plugin-development_ios_index.md.html">CDVPlugin</a>. Moreover, the latest version removes <a href="https://github.com/apache/incubator-cordova-ios/blob/master/CordovaLib/Classes/CDVViewController.m">CDVViewController</a> from <a href="https://github.com/apache/incubator-cordova-ios/blob/master/CordovaLib/Classes/CDVCapture.m">CDVCapture</a>, <a href="https://github.com/hollyschinsky/PGPushNotificationSample/blob/master/platforms/ios/CordovaLib/Classes/CDVSound.m">CDVSound</a> and CDVLocation and adds whitelist method to CommandDelegate.</p> 
<p>PhoneGap 2.5 enables you to implement useSplashScreen without using a setting and distinguish top-level from sub-frame navigations. The latest release provides an ability to make use of a custom script for www/ copying and correct MIME-type for asset-library responses. It also provides a fix for <a href="http://mail-archives.apache.org/mod_mbox/cordova-commits/201302.mbox/%3C20130220221628.A371882D71F@tyr.zones.apache.org%3E">CB-571</a> media updates.</p> 
<p>PhoneGap 2.5 also enables you to run <a href="http://uncrustify.sourceforge.net/">uncrustify</a> on CDVPlugin and enables you to automatically add a notification so that plugins will know when page loads occurs including the ability to add body property to FileTransferError object.</p> 
<p>It also adds NATIVE_URI to FileTransfer.upload, copyTo, moveTo, getMetadata, readAsDataURL and getFileMetadata methods including addition of <a href="https://developer.apple.com/library/mac/#documentation/Cocoa/Reference/Foundation/Classes/NSURLCache_Class/Reference/Reference.html">NSURLCache</a> to app template. The latest release provides a fix for CDVViewController user agent lock and includes updates for Windows Phone 7, <a href="http://www.bada.com/">Bada</a>, BadaWac, <a href="http://en.wikipedia.org/wiki/WebOS">WebOS</a>, Tizen, QT, <a href="http://phonegap.com/2012/03/21/introducing-cordova-js/">CordovaJS</a> and <a href="https://github.com/apache/cordova-cli">Cordova CLI</a>.</p> 
<p>PhoneGap 2.5 provides support for AppCache and adds NATIVE_URI to the quick-return logic including fix for a geolocation database error. It ships with updates for <a href="http://www.windowsphone.com/en-in/how-to/wp8/start/whats-new-in-windows-phone">Windows Phone 8</a> which checks app resources if iso file does not exist and also added html+js mime type. Moreover, it detect instances where item is a resource and use a stream instead of iso-store.</p> 
<p id="lastElm"></p></body></html>
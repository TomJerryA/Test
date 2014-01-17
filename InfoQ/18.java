<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Apps Have to be iOS 7 Compatible by February 1st</h3><p>Apple recently <a href="https://developer.apple.com/news/">announced</a> that iOS applications have to be iOS 7 compatible by February, 1st. To submit new applications or application updates to the iTunes Store, developers have to build their applications with XCode 5 and apps have to be optimized for iOS7. Compatibility with iOS 7 includes changing the UI according to the current <a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/MobileHIG/index.html#//apple_ref/doc/uid/TP40006556">iOS Human Interface Guidelines</a> and the <a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/TransitionGuide/index.html#//apple_ref/doc/uid/TP40013174">iOS 7 UI Transition Guide</a>, as well as adopting the new version of the iOS API.</p>
<h3>User Interface Changes</h3>
<p>The user interface for iOS 7 focuses on clear presentation of content. Developers should avoid graphical elements like skeuomorphism, shadows or borders and use the whole screen to present data to the user. User interface elements have to be nondominant and should not distract to user from the content that is presented. Besides leading to a clearer presentation of content, controls of the new iOS interface design also use less screen space now, so more content can be presented. Apple also advices developers to use auto-layout features as much as possible instead of programatically positioning UI elements.</p>
<p>Handling text with UILabels, UITextFields and UITextViews is now based on <a href="https://developer.apple.com/library/ios/documentation/StringsTextFonts/Conceptual/TextAndWebiPhoneOS/CustomTextProcessing/CustomTextProcessing.html">TextKit</a>. TextKit brings features like kerning, hyphenation or embedded pictures to text elements. Developers can use different styles of text instead of using point or pixel sized fonts. iOS text styles are similar to text styles in HTML and include values like &quot;headline&quot; or &quot;body&quot;. The actual rendering size is calculated by iOS and might depend on zoom settings applied by the user.</p>
<p>Furthermore, iOS 7 also offers new design elements and techniques to UI designers:</p>
<ul> 
 <li>Translucency: Developers can now chose to make views translucent. In contrast to opaque views, they can give the user an idea of the content underneath. According to the iOS User Interface Guidelines, this is especially useful for temporary overlaying views like slide-in menus or settings panels.</li> 
 <li>Depth: The User Interface Guidelines also encourage designers to use depth and layering as a way to express the relation between objects presented to the user. To give the impression of depth, iOS provides a pseudo 3D effect in the user interface. When panning or tilting the device, users are able to look beneath objects that are floating above the content.</li> 
</ul>
<p>&nbsp;</p>
<h3>iOS API Enhancements</h3>
<p>iOS 7 comes with three new <a href="https://developer.apple.com/library/ios/releasenotes/General/WhatsNewIniOS/Articles/iOS7.html#//apple_ref/doc/uid/TP40013162-SW10">multitasking modes</a> to keep the state of an application up to date: The &quot;fetch&quot; mode lets apps periodically check for data updates. Developers can define a minimum update interval for applications and iOS will launch the app in the background and call a delegate method to receive new data. Based on situations like good network connection, iOS might even decide to launch an application before its update interval is elapsed. The mode &quot;remote-notification&quot; uses push-notifications to trigger application updates. Until iOS 7, users received a notification, launched an application and had to wait until the app then updated its content. Now, applications receive the notification, update their state in background and notify the user after the update has completed.</p>
<p><a href="https://developer.apple.com/library/ios/documentation/MapKit/Reference/MapKit_Framework_Reference/_index.html#//apple_ref/doc/uid/TP40008210">MapKit</a> offers advanced overlay handling. Developers can now define different levels to add overlays to a map. Besides, the class MKOverlayView is now deprecated and should be replaced by the new class MKOverlayRenderer. MKDirections lets apps ask for routing information without having to switch to the maps application. With the use of MKMapSnapshotter it is possible to create and display a UIImage of a map region based on parameters like coordinates, altitude or pitch.</p>
<p>Applications can communicate with each other using Airdrop or Peer-to-Peer Connectivity. Both APIs are based on the discovery of nearby devices without having internet connectivity. Apps can register for specific file types and can receive them via Airdrop. iOS will launch the application and call a delegate method when a new file is received. With the help of Peer-to-Peer Connectivity, services can be published and discovered between nearby devices. After establishing a session, devices can exchange arbitrary messages and data.</p>
<p>In case a device does not support iOS 7, it is still possible to provide updates and let users <a href="http://www.infoq.com/news/2013/09/previous-version-ios-apps">download earlier versions</a> of an application from the app store.</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Introducing Common XAML UI</h3><p>A constant complaint amongst .NET developers is the myriad of different XAML-based UIs. The problems started with Silverlight, which had a similar but different set of controls than WPF. Silverlight for Windows Phone added a third set, and XAML for WinRT a fourth.</p>
<p>In today’s Build Keynote we heard that Microsoft is finally starting the reconciliation process with the introduction of Common XAML UI. Based on XAML for WinRT, this UI framework will allow the same UI code to be shared on phones, tablets, desktop computers, and eventually Xbox One.</p>
<p>A cornerstone of the Common UI is a new project type called “shared projects”. This is a new concept for Visual Studio and works very differently than portable class libraries. A shared project cannot be independently compiled into a DLL or EXE. Instead it is merged at build time into one or more traditional project types. The traditional projects are informally referred to as “project heads”.</p>
<p>Core primitives such as panels, buttons, and text boxes/buttons will have the same behavior on Windows and Windows phone. Higher level primitives such as Hub, AppBar/CommandBar, date/time pickers, ListView, flyouts, and media will have the same API on both platforms but will behave differently. The Ads SDK will also have a common API signature between the platforms, but again the behaviors will differ.</p>
<p>It should be noted that some features will silently fail. For example, if you have too many buttons in the CommandBar then Windows Phone will only render the first few.</p>
<p>While many of the controls are scalable to different screen sizes, there will be times when you need to tailor the behavior for some devices. One way to accomplish this is through the use of platform specific custom controls. Shared controls can reference these platform specific custom controls so long as a control with the correct name exists in each project head.</p>
<p>Another option for improving code reuse is the use of conditional compilation and #if def in the code-behind. In this sense it is like the classic approach of sharing source code files between projects using soft links.</p>
<p>Resource files, the same that are used for localization, offer a third way to tailor the user experience. The cited example is how command bar buttons are expected to be in lower case on phones and title cased on the desktop.</p>
<p>While most of the APIs are now shared, there are some UI aspects that are not available on all platforms. The most significant ones are:</p>
<p>Windows Only APIs</p>
<ul> 
 <li>SearchBox</li> 
 <li>Settings Flyout</li> 
</ul>
<p>Windows Phone Only APIs</p>
<ul> 
 <li>Pivot</li> 
 <li>AutoSuggestBox</li> 
 <li>ContentDialog</li> 
 <li>Maps</li> 
 <li>System Chrome</li> 
 <li>Progress area, in-call UI</li> 
</ul>
<p>The Windows and Windows Phone back button do behave differently, so some custom work around them may be needed. Platform specific code will also be necessary for file pickers, share, and settings.</p>
<p>Common XAML and Universal Apps are available in all versions Visual Studio 2013 Update 2.</p><br><br><br><br><br><br></body></html>
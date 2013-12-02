<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Visual Commander Professional v1.3 Introduces 99 Commands, 50 Extensions and C# Syntax Highlighting</h3><p><a href="http://vlasovstudio.com/visual-commander/professional_edition.html">Visual Commander Professional v1.3</a> has been released with the ability to create 99 commands and 50 extensions either by pressing the Add button in the Commands window or by import. It introduces syntax highlightingand also integrates Visual Studio text editor to enable developers to edit code and added recording for Edit.FindNextSelected, Edit.FindPreviousSelected, Edit.FindNext and Edit.FindPrevious commands.</p>
<p>Visual Commander v1.3 provides an ability to select default language for new commands and extensions by selecting the macro language. It also provides fixes for ReflectionTypeLoadException, which occurs when multiple versions of Visual Studio are installed on the same machine in addition to a fix for FileNotFoundException that throws when custom assemblies are referenced with the full path. The recent release includes improved storage processing to preserver CR in code and several enhancements in exception handling.</p>
<p>The extension enables developers to automate repetitive tasks in Visual Studio 2013/2012/2010 either by creating new commands and extensions in C#, VB or by reusing existing Visual Studio macros from previous versions. It also provides an ability to record and playback keyboard commands for the Visual Studio text editor.</p>
<p>With the help of Visual Commander, Record Macro (Ctrl+Shift+R) and Run Macro (Ctrl+Shift+P) commands can be reassigned by manually assigning them in Visual Studio keyboard options for the VCmd.RecordMacro and VCmd.RunMacro commands. Moreover, the extension stores all the settings including commands, extensions and the temporary macro in &quot;%APPDATA%\Sergey Vlasov\Visual Commander\1.0\snippets.vcmd&quot;.</p>
<p>&quot;There is no API for Visual Commander at the moment. You can assign shortcuts to the commands and add them to the toolbar using standard Visual Studio interface,&quot; said <a href="http://vlasovstudio.com/about.html">Sergey Vlasov</a>, Lead Developer, Visual Commander.<br /> <br /> InfoQ had a chat with Sergey to know more about his Visual Studio extension.</p>
<p><strong>InfoQ - Can you share with us the real purpose behing the creation of Visual Commander?</strong></p>
<blockquote>
  The main goal for Visual Commander was to give developers the ability to run existing macro commands in Visual Studio 2012/2013. Visual Studio supported macro commands since Visual Studio 6, lots of custom commands were created to improve productivity and removal of this feature in Visual Studio 2012 left many developers empty handed. Also no other 3rd party tool have this functionality at this moment. 
</blockquote>
<p><strong>InfoQ - Does Visual Commander improve developer productivity?</strong></p>
<blockquote>
  Absolutely. For common tasks you can create a command sequence to edit code, change Visual Studio options or modify your solution and then invoke it with a single mouse click or a keyboard shortcut. 
</blockquote>
<p><strong>InfoQ - Can you share any case study where the product has been tested successfully?</strong></p>
<blockquote> 
 <a href="http://visualstudio.uservoice.com/forums/121579-visual-studio/suggestions/2650757-bring-back-macros">Jeff Relf</a> posted his experience using Visual Commander Professional to the &quot;Bring back Macros&quot; thread on VS uservoice. The Visual Commander page on 
 <a href="http://visualstudiogallery.msdn.microsoft.com/deda8ac1-75e6-4068-89ab-b607cee38f2d">Visual Studio Gallery</a> lists 3 reviews and Q&amp;A. 
</blockquote>
<p><strong>InfoQ - Can you disclose the future roadmap of Visual Commander?</strong></p>
<blockquote>
  I plan to improve Visual Commander integration with Visual Studio and make it easier to use: 
 <ol> 
  <li>Add the ability to reorder and sort Visual Commander commands in the VCmd menu.</li> 
  <li>Add custom command names for keyboard binding to Visual Studio keyboard options.</li> 
  <li>Add explicit menu command to save recorder macro as a command.</li> 
  <li>I'd like to find a way to enable intellisense for command editing, but currently hitting limitations of Visual Studio extensibility.</li> 
 </ol> 
</blockquote><br><br><br><br><br><br></body></html>
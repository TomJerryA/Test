<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Bringing Visual Studio's CodeLens Into Focus</h3><p class="Standard">One of the most popular features shipping with Visual Studio 2013 Ultimate is CodeLens.&nbsp; <a href="http://msdn.microsoft.com/en-us/library/dn269218.aspx">CodeLens</a> provides meta-information about the source you are working with while you edit it.&nbsp; When used in conjunction with Team Foundation Server (TFS), several useful stats are provided on the fly:&nbsp; unit test results, change history, and work item history.&nbsp; To this functionality the forthcoming Update 2 to VS2013 will add a new ability called Incoming Changes.
 <o:p></o:p>
 <o:p>
  &nbsp;
 </o:p></p>
<p class="Standard">Incoming Changes is intended to make working with multiple branches on TFS easier.&nbsp; Another field is added to the CodeLens status (helpfully labeled “incoming change”) which when clicked (or accessed via hotkey ALT+6) will produce a tool tip with several new pieces of information:&nbsp; the name of the branch a change occurred on, which changeset it is accessed on, the author, and a datestamp.
 <o:p></o:p></p>
<p class="Standard">Why is this helpful?&nbsp; Well it provides insight as to changes that are happening in the source tree while are working on your section.&nbsp; Perhaps their work has no bearing on yours, but if it does negative collisions can be avoided.&nbsp; Code diffs can also be performed to compare the upcoming change with the contents of the file in your editor.
 <o:p></o:p></p>
<p class="Standard">The level of detail is configurable, so if you are interested in the full change history of intermediate branch merges you can enable them to be shown.&nbsp; (The default is to hide them.)&nbsp; The overall CodeLens feature itself is also configurable under the Options menu.&nbsp; Incoming Changes and the other indicators CodeLens offers can be individually enabled/disabled as desired.
 <o:p></o:p></p>
<p class="Standard">For a complete illustrated walkthrough, Microsoft’s Mathew Aniyan has <a href="http://blogs.msdn.com/b/visualstudioalm/archive/2014/03/03/new-codelens-indicator-incoming-changes.aspx">provided</a> an article describing Incoming Changes in detail.&nbsp; To try out the feature for yourself, you will need Team Foundation Server 2013 Update 2 RC and Visual Studio 2013 Ultimate with Update 2 CTP2 applied.&nbsp; 
 <o:p></o:p></p>
<p class="Standard">
 <o:p>
  &nbsp;
 </o:p></p>
<p class="Standard">
 <o:p>
  &nbsp;
 </o:p></p><br><br><br><br><br><br></body></html>
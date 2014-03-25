<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Using Sigma for Drawing Graphs</h3><p>The team behind <a href="http://sigmajs.org/">Sigma</a>, a JavaScript library dedicated to drawing graphs in Web applications, released a new <a href="https://github.com/jacomyal/sigma.js/blob/master/CHANGELOG.md">version</a> of this tool.</p>
<p>What this library provides is a way for developers to create graphs while making networks manipulation on webpages smooth and faster for the user. Although the current version mainly represents bug fixes, the previous one - released in the beginning of this year – was totally developed from scratch with a fully new architecture.</p>
<p>For a current list of features, the Sigma’s webpage states the following:</p>
<ul> 
 <li>Custom rendering - You can use the <a href="http://www.w3schools.com/html/html5_canvas.asp">Canvas</a> or <a href="http://www.khronos.org/webgl/">WebGL</a> built-in renderers, or even write your own. The built-in renderers also provide many ways to customize the rendering.</li> 
 <li>Interactivity oriented - You can catch when the users clicks or rolls the mouse over a node. You can catch when the user drags the graph or zoom in, and always know the position of the graph relatively to the screen.</li> 
 <li>Powerful graph model - Sigma is just a rendering engine, but you might want to do more, like running your own graph algorithms. For that, Sigma's graph model is customizable, and you can add your own custom indexes on the data.</li> 
 <li>Extendable - It is easy to develop plugins or simple snippets to augment Sigma's features. Some are already available in the main repository to read some popular graph file formats or to run complex layout algorithms.</li> 
 <li>Compatibility - Sigma runs on all modern browsers that support Canvas but works faster on browser with WebGL support.</li> 
</ul>
<p>This library was featured on last month GitHub’s <a href="https://github.com/trending">most trending repositories</a> and InfoQ got in touch with Alexis Jacomy, lead developer of Sigma, to know a little more about this project:</p>
<p><strong>InfoQ: What is the motivation behind Sigma?</strong></p>
<blockquote> 
 <p>I started developing graph drawing Web tools in Flash some years ago to help <a href="https://gephi.org/">Gephi</a> users display interactively their graphs on web pages. Sigma was initially just the first HTML5 step and it is now kind of successful, which keeps me motivated on it.</p> 
</blockquote>
<p><strong>InfoQ: </strong><strong>The new version of Sigma has been under a heavy refactoring. What were you trying to accomplish?</strong></p>
<blockquote> 
 <p>Original Sigma's source code was very strict and not tested at all. This refactoring was for me the occasion to fix these issues, with a more consistent API and unit tests. In addition, everything in Sigma is now overridable, to allow implement almost any feature as a plugin.</p> 
</blockquote>
<p><strong>InfoQ: There are other libraries that make graph drawing possible in JavaScript (Processing.js, jit.js, D3.js). What do you think makes this tool unique?</strong></p>
<blockquote> 
 <p>Sigma is a library dedicated to graph drawing. It aims to simplify basic use cases, but also to allow integration for much more complex applications:</p> 
 <ul> 
  <li>It provides without effort multitouch support, smooth zooming and deals with window resizing, to cite a few of the built-in features.</li> 
  <li>It provides some more complex features implemented as plugins.</li> 
  <li>Its API and events system ease interacting with the graph.</li> 
 </ul> 
</blockquote>
<p><strong>InfoQ: </strong><b>Do you know any project that currently uses Sigma?</b></p>
<blockquote> 
 <p>I have heard about some people currently integrating the new version of Sigma, but nothing in production yet:</p> 
 <p>From Sciences-Po m&eacute;dialab (my current employer, who financed the development of the latest version):</p> 
 <ul> 
  <li><a href="http://tools.medialab.sciences-po.fr/iwanthue/">http://tools.medialab.sciences-po.fr/iwanthue/</a></li> 
  <li><a href="https://github.com/medialab/Hypertext-Corpus-Initiative">https://github.com/medialab/Hypertext-Corpus-Initiative</a></li> 
  <li><a href="https://github.com/medialab/sciencescape">https://github.com/medialab/sciencescape</a></li> 
 </ul> 
 <p>From Oxford Internet Institute:</p> 
 <ul> 
  <li><a href="https://marketplace.gephi.org/plugin/sigmajs-exporter/">https://marketplace.gephi.org/plugin/sigmajs-exporter/</a> - which has a lot to do with Sigma's success</li> 
  <li><a href="https://apps.facebook.com/namegendev/">https://apps.facebook.com/namegendev/</a></li> 
  <li><a href="http://collegeconnect.us">http://collegeconnect.us</a></li> 
 </ul> 
 <p>From other people:</p> 
 <ul> 
  <li><a href="http://moviegalaxies.com/">http://moviegalaxies.com/</a></li> 
  <li><a href="http://linkurio.us/">http://linkurio.us/</a></li> 
  <li><a href="http://app.algopol.fr/">http://app.algopol.fr/</a></li> 
 </ul> 
</blockquote>
<p><b>InfoQ: What are future plans for this project?</b></p>
<p>My plans are essentially to keep maintaining it, and try to get some more people getting involved into the core developments. Also, there are still some features I did not find the time to implement yet, like an SVG renderer or a web workers based layout algorithm.</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>CoffeeScript 1.7 Released: Adds Chaining Without Parenthesis, Multiline Strings and More</h3><p>Jeremy Ashkenas has released <a href="https://gist.github.com/aseemk/8637896">version 1.7 of CoffeeScript</a>, and with it introduced some highly anticipated changes to the popular JavaScript transpiler.</p>
<p>Version 1.7 includes one of the most popular requests for the language; support for chaining without parenthesis. Prior to the 1.7 releases, if a developer wanted to chain functions, they had to use parenthesis, which are not required for functions in CoffeeScript.</p>
<pre><p>// prior to 1.7 - parenthesis required to chain<br />$('#element').addClass('active').css({ left: 5 });</p>
<p>// as of 1.7 - no parenthesis<br />$ '#element'<br />.addClass 'active'<br />.css { left: 5 }</p></pre>
<p>This release also introduces proper support for multiline strings. In previous versions of CoffeeScript, herestrings (or string literals) while intended to preserve new lines and whitespace, would ignore the `\` operator which is meant to designate that two strings should be preserved on the same line. As of 1.7, this is fixed, allowing the developer to cleanly format multiline strings in CoffeeScript.</p>
<pre><p>console.log '''The quick brown fox jumped over the \<br />lazy dog'''</p>
<p>// prior to 1.7 outputs<br />The quick brown fox jumped \nover the lazy dog</p>
<p>// as of 1.7 now outputs<br />The quick brown fox jumped over the lazy dog</p></pre>
<p>Expansion has also been added to array destructuring, which had previously been the <a href="https://github.com/jashkenas/coffee-script/pull/3268">longest open issue</a> on the CoffeScript repo.</p>
<pre><p># get the last item in the animals array<br />animals = [ 'cat', 'dog', 'hippopotamus' ]</p>
<p># prior to 1.7<br />hippo = animals[animal.length - 1]</p>
<p># as of 1.7<br />[..., hippo] = animals</p>
<p># ...both of which transpile to...<br />hippo = animals[animals.length - 1];</p></pre>
<p>New convenient mathematical operators are present as well in the addition. There is the new power operator, floor division, and a modulo operator (returns the remainder of a division operation).</p>
<pre><p># power<br />2 ** 2<br /># transpiles to...<br />Math.pow(2, 2);</p>
<p># floor division<br />2 // 3<br />#transpiles to...<br />Math.floor(2 / 3)</p>
<p># modulo<br />2 %% 3<br />#transpiles to...<br />var __modulo = function(a, b) { return (a % b + +b) % b; };<br />__modulo(2, 1);</p></pre>
<p>Other enhancements include bringing CoffeeScript in line with Node.js so that its require statement doesn't automatically run every file in a directory, but behaves like Node and only runs the index.coffee file.</p>
<p>The majority of the work on the 1.7 release (and in fact most of CoffeeScript for the past few years) is done by members of the community. &quot;There are over 100 developers who have contributed to and had patches merged into CoffeeScript&quot; said Jeremy. &quot;Whatever adoption CoffeeScript has enjoyed has happened because the idea appeals to JavaScript programmers.&quot; In regards to work on the 1.7 release, Jeremy sent <a href="https://twitter.com/jashkenas/status/428243869487362048">special thanks</a> to <a href="https://github.com/xixixao">Michael Srb</a> for his contributions.</p>
<p>CoffeeScript has indeed enjoyed immense popularity, peaking at one point as the <a href="http://en.wikipedia.org/wiki/CoffeeScript">10<sup>th</sup> most popular project on GitHub</a>. It's also seen support in frameworks such as Ruby on Rails (since version 3.1), and is supported in Microsoft's Visual Studio via the <a href="http://vswebessentials.com/">Web Essentials plugin</a>. Additionally JavaScript creator <a href="http://en.wikipedia.org/wiki/Brendan_Eich">Brenden Eich</a> has expressed how CoffeeScript influenced his thoughts on <a href="https://brendaneich.com/tag/javascript-ecmascript-harmony-coffeescript/">the future of JavaScript</a>.</p>
<p>GitHub user <a href="https://gist.github.com/stefanpenner">stefanpenner</a> noted that in CoffeeScript “…ES6 import export would be killer…”</p>
<p>Jeremy does address ES6 features in CoffeeScript saying,</p>
<blockquote> 
 <p>CoffeeScript is mostly finished — has been quite stable for a couple of years now — but will continue to grow in small ways in the future. Some examples are: support for new JavaScript features as they land, further improved source map support, more polish for the literate programming style and more streamlining for the internals of the compiler.</p> 
</blockquote>
<p>At one point there, was a <a href="https://www.kickstarter.com/projects/michaelficarra/make-a-better-coffeescript-compiler">Kickstarter project</a> to re-write the CoffeeScript compiler. The project has since been successfully funded and is dubbed <a href="http://github.com/michaelficarra/CoffeeScriptRedux">CoffeeScriptRedux</a>. Jeremy sees the creation of new compilers as a benefit for CoffeeScript saying, &quot; The more compilers that successfully target a given language — the healthier that language is. It's to CoffeeScript's benefit to have multiple independent compilers.&quot;</p>
<p>The 1.7 release is available immediately via <a href="https://github.com/jashkenas/coffee-script">GitHub</a>, or the <a href="http://coffeescript.org/">official CoffeeScript site</a>.</p><br><br><br><br><br><br></body></html>
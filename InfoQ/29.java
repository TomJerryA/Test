<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>A Merge Tool that Understands Functions</h3><p>Codice Software, maker of <a href="http://plasticscm.com/">Plastic SCM</a>, has released a preview of a semantic merge tool. This tool parses your code, allowing for a more accurate merge than the line-by-line comparisons most tools use. We interviewed Pablo Santos Luaces, Principal Software Engineer of Codice Software.</p> 
<p><b>InfoQ</b>: What first inspired you and your company to look into semantic merges?</p> 
<blockquote> 
 <p><b>Pablo</b>: It is actually a long story that started long ago.</p> 
 <p>We truly believe that &quot;with great branching comes great merging&quot; :) and since we strongly believe in &quot;branch per task&quot; (http://codicesoftware.blogspot.com/2010/08/branch-per-task-workflow-explained.html) which implies coming up with tons of branches, we always thought we'd need a much better merge mechanism.</p> 
 <p>DVCS is rocking the development world but we're still using merge algorithms based on text, basically the same &quot;merge engines&quot; we used 15 years ago.</p> 
 <p>So we started thinking on &quot;semantic merge&quot; but of course it is far from easy. So we first came with &quot;Xdiff and Xmerge&quot; http://plasticscm.com/features/xmerge.aspx as a way to empower our current &quot;text-based&quot; diff and merge algorithms. We though they were great, but we wanted to come up with something better. Semantic was always the goal.</p> 
 <p>Then we worked hard in better ways to merge files and directories in order to have better &quot;refactoring support&quot; and we added this to the core of Plastic SCM: http://plasticscm.com/mergemachine/index.html.</p> 
 <p>And when all the bits and pieces were there (back in mid 2012) we jumped to Semantic Merge: let's forget about the old text-based ways of merging files and let's parse the source code and deal with namespaces, classes, methods and so on instead of lines of text.</p> 
 <p>And that's how we started the whole thing.</p> 
 <p>The inspiration was: forget everything you know about current merge technology, as a developer: how would you expect merges to behave? How should they really work? The answer was: &quot;merge should understand the code&quot;, and this is how all started.</p> 
</blockquote> 
<p><b>InfoQ</b>: Could you talk a little bit more your &quot;branch per merge&quot; philosophy?</p> 
<blockquote> 
 <p><b>Pablo</b>: Branch per task is a well-known branching pattern and is based on the following idea: for each task in your issue tracker you'll create a branch to work on it.</p> 
 <p>So yes, every single change or new feature will have an entry on the issue tracker (whether it is a new task, a bug, a performance issue, anything) and then it will have a branch.</p> 
 <p>Advantages:</p> 
 <p>* In pure mainline (trunk) development (everyone working on a single branch) the version control is perceived as just a &quot;delivery mechanism&quot; by the developer. A pain. That's all.<br /> * But using your own branch (whether you're working centralized or distributed) you don't use the version control just as a delivery mechanism, now it is a productivity tool: you checkin as often as you need (a checkin is not a delivery, just your own checkpoint), you can check differences on your own code... and so on.<br /> * The main issue with traditional CI is &quot;breaking the build&quot;, it is a reactive way of working: you first break the build, then it has to be fixed. This is a consequence of the &quot;mainline&quot; way of working: you checkin and the code hits the mainline. Using branch per task you're shielded from that.<br /> * It is not true that more branching leads to more merging: working in parallel is what leads to merging, but you can change a file in parallel with me even if we're on the same branch... then one of the two will have to merge.<br /> * You tend to better isolate tasks, which are more independent from each other than what we tend to think. So branch per task enables more flexible release cycles, more controlled ones too.<br /> * Creating stable baselines during the merge phase (which can happen once a day, branch per task doesn't mean you've to merge once a month... not at all!) is also very natural with branch per task.</p> 
 <p>You can find the entire explanation here: <a href="http://www.plasticscm.com/infocenter/quick-start/intro-task-driven-development.aspx">http://www.plasticscm.com/infocenter/quick-start/intro-task-driven-development.aspx</a></p> 
</blockquote> 
<p><b>InfoQ</b>: Why did you choose C# as your first language to support?</p> 
<blockquote> 
 <p><b>Pablo</b>: There are several reasons for that, I'll describe them in no particular order:</p> 
 <p>1) We're a .NET shop at heart! :-) We develop C# code on a daily basis, so eating our own dog's food seemed like a good thing to do :-)</p> 
 <p>2) C# is one of the top languages in number of users: go to StackOverflow and you'll find out C# is the most popular tag! http://stackoverflow.com/tags. Go to the TIOBE Index and C# is in the top 5 http://www.tiobe.com/index.php/content/paperinfo/tpci/index.html. According to PYPL https://sites.google.com/site/pydatalog/pypl/PyPL-PopularitY-of-Programming-Language C# is number 3 and raising... So, definitely is a very extended language.</p> 
 <p>3) C# (and Java) are very good to start with a concept like semantic merge because they're easier to deal with (from the tech point of view) than C++, so at the very beginning we were able to focus more on the semantic merge technology itself and less on the languages.</p> 
 <p>So, these are the main reasons.</p> 
</blockquote> 
<p><b>InfoQ</b>: What other languages/file formats are you planning on supporting in the future?</p> 
<blockquote> 
 <p><b>Pablo</b>: Our goal is to release support for VB.NET, then Java and then jump to C and C++. After that we'll be running a <a href="http://plasticscm.uservoice.com/forums/196398-mergebegins">survey</a> among our early adopters to learn what they need.</p> 
</blockquote> 
<p><b>InfoQ</b>: Most merge tools &quot;see&quot; files in terms of lines. What does your product see? Just functions? Statements and blocks? Expressions within a statement?</p> 
<blockquote> 
 <p><b>Pablo</b>: What semanticmerge sees is a the source file in a tree format: namespaces, then class(es), methods inside... Basically the structure. The semantic doesn't see &quot;the code inside the methods&quot;, so it stops at method, property or field level. The merge of the bodies of methods or properties is run in a text-based way. It doesn't &quot;semantically&quot; merge &quot;if statements&quot;, for instance. Not yet at least ;-).</p> 
 <p>Of course, it is able to reduce the 3-way merge to a method-based 3-way merge: it finds the &quot;ancestor&quot; of the method and the two contributors and hence greatly simplifies life to the text-based merge tool used to deal with method bodies.</p> 
</blockquote> 
<p><b>InfoQ</b>: Occasionally a developer will run a &quot;clean-up&quot; tool across a file, sorting methods from properties and alphabetizing everything. Needless to say, a line-based merge tool doesn't handle this very well. Would this be a scenario that your too supports?</p> 
<blockquote> 
 <p><b>Pablo</b>: This is exactly my favorite case!! Yes, semantic merge is able to deal with this case cleanly. In fact it is NOT affected by the location of the elements, it *does know* a method is the same method regardless of the position :-). So yes, this is a great feature because basically we empower refactoring: nothing will prevent you know from having your files as clean as readable as possible.</p> 
</blockquote> 
<p>You can apply for the closed beta at <a href="http://www.plasticscm.com/sm/index.html">http://www.plasticscm.com/sm/index.html</a>.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
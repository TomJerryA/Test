<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Git Gets Better Defaults, Faster</h3><p>Git 2.0 is finally released, almost a month after the first release candidate was available. This comes with performance improvements such as introduction of bit-map indexes, as well as sensible defaults, especially helping first-time users. For existing users, there are also options to keep functionality similar to previous versions, reducing impact to their workflows.</p>
<p>Git users were being primed from earlier releases for some of these features. Junio Hamano, maintainer of Git, says (<a href="http://git-blame.blogspot.co.uk/2014/05/git-20.html">excerpt</a>) -</p>
<blockquote>
 ..(Some may even say) that the new release does not offer anything exciting—and that is exactly what we want to hear from existing users. In recent releases for the past year or so, we have added knobs to allow users to enable these new defaults before 2.0 happens, and added warnings to let users know when they perform an operation whose outcome will be different between 1.x series and 2.0 release. The existing users are hopefully very well prepared by now, and &quot;Git 2.0&quot; is designed to be the final &quot;flipping the default&quot; step.
</blockquote>
<p>Some of the major improved defaults are -</p>
<ul> 
 <li>push defaults to &quot;simple&quot; semantics (instead of &quot;matching&quot;) - which pushes only the current branch to a branch in the remote with the same name</li> 
 <li>&quot;git add -u&quot; and &quot;git add -A&quot;, when run without path, operate on the entire tree even if run inside a subdirectory. You need to add an extra period (&quot;git add -u .&quot; or &quot;git add -A .&quot;) to limit the add to current directory.</li> 
 <li>&quot;git add &lt;path&gt;&quot; will not ignore removals, and in effect be same as &quot;git add -A &lt;path&gt;&quot;</li> 
</ul>
<p>Felipe Contreras <a href="http://felipec.wordpress.com/2014/05/29/git-v2-0-0/">explains these backward-incompatible differences</a> in a bit more detail.</p>
<p>There are also several other improvements. Some of them are -</p>
<ul> 
 <li>&quot;git grep&quot; behaves in a way similar to native grep when &quot;-h&quot; (no header) and &quot;-c&quot; (count) options are given</li> 
 <li>Many commands that create commits, such as &quot;-pull&quot; and &quot;-rebase&quot; take &quot;--gpg-sign&quot; option on the command line (read more about <a href="http://mikegerwitz.com/papers/git-horror-story">Signed commits</a>)</li> 
 <li>Several new options such as &quot;pull.ff&quot; (accept only fast-forward), &quot;-N&quot; option for &quot;git reset&quot;, &quot;commit.gpgsign&quot; (always sign when using &quot;git commit&quot;)</li> 
 <li>Trailing whitespaces in .gitignore files are warned and ignored (unless they are quoted)</li> 
</ul>
<p>Several performance and implementation improvements, such as -</p>
<ul> 
 <li><a href="http://www.eclipsecon.org/2013/sites/eclipsecon.org.2013/files/Scaling%20Up%20JGit%20-%20EclipseCon%202013.pdf">bitmap-index feature from JGit</a> has been ported, which if used, significantly improves the counting phase of the clone and fetch operations (at the cost of extra disk space used by indexes)</li> 
 <li>The way &quot;git log --cc&quot; shows a combined diff against multiple parents has been optimized</li> 
</ul>
<p>You can learn more about all the changes as well as all the fixes in the <a href="http://article.gmane.org/gmane.comp.version-control.git/250341">release notes</a>.&nbsp;</p><br><br><br><br><br><br></body></html>
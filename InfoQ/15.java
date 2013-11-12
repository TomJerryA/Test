<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Use the Force, Luca</h3><p>Yesterday, a developer on the <a href="https://groups.google.com/forum/#!topic/jenkinsci-dev/-myjRIPcVwU">Jenkins project</a> accidentally triggered a <a href="https://groups.google.com/d/msg/jenkinsci-dev/-myjRIPcVwU/t4nkXONp8qgJ">force push</a> on the <a href="https://github.com/jenkinsci/">GitHub repositories</a> that store the Git repositories for the Jenkins codebase, wiping out several months of commits. The community were very understanding and the problem was quickly resolved, but it does highlight an area where GitHub's openness (coupled with the <a href="https://github.com/jenkinsci">Jenkins CI organisation</a>'s openness to allow anyone to commit to any repository) can magnify problems when they occur.</p>
<p>A Git forced push, run with <code>git push --force</code>, tells the server to replace the content of the references (branches/tags) being pushed with the content given. Normally, a Git repository will only allow <em>fast forward</em> pushes; that is, where the pushed reference has the current reference as an ancestor. A force push removes that restriction, allowing the content to replace what was there before.</p>
<p>Configurations in Git repositories can be configured to allow or deny this with the <a href="http://www.kernel.org/pub/software/scm/git/docs/git-config.html">git config</a> value <code>receive.denyNonFastForwards false</code>. This prevents such forces from occurring.</p>
<p>There are cases where enabling force is useful; for example, if a refactoring or a filtering operation such as <code>git filter-branch</code> is executed, then the commits will not be ancestors of the current branch and so won't work. Another use-case is when mirroring is enabled, to synchronise the content of two repositories, where you want the changes to go through without erroring.</p>
<p>That's what <a href="https://groups.google.com/d/msg/jenkinsci-dev/-myjRIPcVwU/t4nkXONp8qgJ">happened in this case</a> – Luca was testing the Gerrit mirroring plugin, and had a set of repositories for the Jenkins repository checked out locally. The Gerrit mirror was set up to take content from this local repository, and resulted in all of the repositories being mirrored from his local checkouts. Unfortunately, since the repositories hadn't been updated in a while the net effect was to reset the repositories to a prior state.</p>
<p>Fortunately all the repositories have been restored at this point – one of the advantages of the Git version control system (or any DVCS) is that you can repopulate a repository from any of its clones, and it was easy enough to do this. But it does ask two particular questions of how to mitigate this in future:</p>
<ul> 
 <li>Does it make sense to have users committing against multiple repositories, or should changes come in through a managed channel such as a review/pull request?</li> 
 <li>Does it make sense for GitHub to offer the configuration option to <code>denyNonFastForwards</code>?</li> 
</ul>
<p>GitHub's main competitor, <a href="http://bitbucket.org">BitBucket</a>, does provide <a href="https://bitbucket.org/site/master/issue/3338/git-allow-option-to-enable-disable-force">an option to disable nonFastForwards</a>. BitBucket was taken over by Atlassian and used to be the canonical location of the also-ran DVCS, Mercurial. However, BitBucket's growth has been in Git hosting solutions, and their Git management solution <a href="https://www.atlassian.com/it/software/stash/overview">Atlassian Stash</a>, is focussed solely on Git repositories.</p>
<p>Ironically, Luca has a company providing Gerrit based repositories called <a href="http://gerritforge.com">GerritForge</a> and has recently authored a book on <a href="http://www.infoq.com/articles/learning-gerrit-code-review">Learning Gerrit Code Review</a>, recently reviewed by InfoQ. Perhaps if the Jenkins repositories were using a review-based tool such as Gerrit this may not have happened.</p>
<p>Until such time as GitHub offer the configuration for nonFastForwards, the Jenkins developers are <a href="https://groups.google.com/forum/#!topic/jenkinsci-dev/dD-sumd81pU">writing a tool</a> to track pushes to the GitHub repository and recording the changes that are made, along with the SHAs of the commits. Ironically they propose using <code>rsync</code> to back them up to multiple locations.</p>
<p>With great power, comes great responsibility, and GitHub's use of the force certainly has that opportunity. Whether GitHub will provide an option to prevent this in the future or not, it's worth being aware if you host large enterprise repositories that aren't backed up.</p><br><br><br><br><br><br></body></html>
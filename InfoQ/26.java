<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>New Gem Creates Test Boilerplate for Chef Cookbooks</h3><p><a href="https://github.com/paulczar/meez">Meez</a>, written by <a href="https://twitter.com/pczarkowski">Paul Czarkowski</a> of Rackspace is a command line tool for creating new cookbooks with all the boilerplate necessary to start practicing TDD on your infrastructure. <a href="http://sysadvent.blogspot.co.uk/2013/12/day-11-lazy-sysadmins-guide-to-test.html">Originally a skeleton cookbook</a>, meez has since evolved into a more flexible tool that allows you to start out with some of the metadata pre-filled in.</p>
<p><a href="https://github.com/paulczar/meez#about">According to the author</a> the name is slang for <i>mise en place</i> (putting in place), a French expression used in the kitchen that refers to the act of separating and arranging all the ingredients that will be used for the dish being cooked. As with other tools built around Chef, it uses food analogies to describe its purpose: a cookbook created with meez comes with many common tools in place to assess the quality of the code, helping solve the problem of how to get started testing infrastructure code. Without using it, the user would have to include each tool individually, and in many cases create directory structures and boilerplate manually before writing actual test code, which can be a tiring exercise of digging around the web for documentation and example code. By making all this tooling readily accessible it encourages best practices towards writing better code. It also takes away one point of failure to check when things go wrong. After all, the structure was created following known working patterns.</p>
<p>These are the tools included by meez in a cookbook:</p>
<ul> 
 <li><a href="http://berkshelf.com/">Berkshelf</a> to manage cookbook dependencies</li> 
 <li><a href="http://batsov.com/rubocop/">RuboCop</a> to check code style</li> 
 <li><a href="http://acrmp.github.io/foodcritic/">Foodcritic</a> to lint cookbook code</li> 
 <li><a href="https://github.com/sethvargo/chefspec">ChefSpec</a> for unit testing</li> 
 <li><a href="http://serverspec.org/index.html">Serverspec</a> for acceptance testing</li> 
 <li><a href="https://github.com/test-kitchen/test-kitchen">Test Kitchen</a> to run tests across multiple platforms</li> 
 <li><a href="https://github.com/customink/strainer">Strainer</a> which provides a single command to run all tests in isolation</li> 
</ul>
<p>The only required argument is the cookbook name, but optional arguments for cookbook license, author’s name and e-mail can be provided and will perform text substitution in the metadata file and others, a handy addition to the cookbook creation process.</p>
<p>It is also possible to run meez on top of existing cookbooks where the user wants to add tests. When doing so, the tool carefully asks what to do with each conflict as they arise. For instance, when run against the official apache2 cookbook, it stops execution before changing the existing Berksfile:</p>
<pre><p>* Initializing Cookbook<br />** Creating cookbook apache2<br />** Creating README for cookbook: apache2<br />** Creating CHANGELOG for cookbook: apache2<br />** Creating metadata for cookbook: apache2<br />&nbsp;&nbsp;Rewriting metadata.rb<br />&nbsp;&nbsp;Rewriting recipes/default.rb<br />* Initializing Berkshelf<br />&nbsp;&nbsp;conflict apache2/Berksfile<br />Overwrite /home/user/chef-repo/cookbooks/apache2/Berksfile? (enter &quot;h&quot; for help) [Ynaqdh]</p></pre>
<p>The same happens for all conflicting files in the cookbook.</p>
<p>Last month <a href="http://community.opscode.com/chat/openstack-chef/2014-01-22">on the #openstack-chef freenode channel</a>, the author said it is not possible to customize the template, meaning that for the moment any special requirements, such as integration with other tools or using a different template for the metadata.rb file, a special file that serves as a high-level description of the cookbook, have to be added after the fact. That is not different from what happens when using more common tools such as Berkshelf or <a href="http://docs.opscode.com/knife.html">knife</a>, to create a cookbook. He also mentioned plans to add a <a href="http://rake.rubyforge.org">Rake</a> task and integration with <a href="https://travis-ci.org">Travis CI</a>.</p>
<p>James Wickett, proponent of <a href="http://ruggeddevops.org">Rugged DevOps</a>, a flag under which he encourages the union of the InfoSec and DevOps communities advocating for both agile and more secure software deliveries, <a href="http://theagileadmin.com/2014/01/20/clean-up-your-cookbook-mess-with-meez/">describes his experience</a> with the gem:</p>
<blockquote> 
 <p>Once you tell meez to create a cookbook for you, it sets up all the different frameworks and gets you ready to start actually writing your recipes and working on your cookbook. No more remembering how to setup all the testing tools and frameworks. Sweet!</p> 
</blockquote>
<p>The gem's <a href="https://github.com/paulczar/meez/blob/master/README.md">README file on GitHub</a> is the main source of information about its usage.</p><br><br><br><br><br><br></body></html>
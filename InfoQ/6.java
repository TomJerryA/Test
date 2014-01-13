<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Chef Sugar Aims to Enhance Chef's Recipes Authoring Experience</h3><p><a href="https://github.com/sethvargo/chef-sugar">Chef Sugar</a> is an extension to <a href="http://www.getchef.com/">Chef</a> that offers DSL methods to make more readable recipes. <a href="https://sethvargo.com/">Seth Vargo</a>, Chef Sugar's author, <a href="https://sethvargo.com/spice-up-your-recipes-with-chef-sugar/">wrote about his motivations</a> for creating Chef Sugar, highlighting them with examples. InfoQ interviewed Seth to know more about his views on syntactic sugar and the benefits of a plug-in architecture in the context of Chef.</p>
<p>Chef Sugar provides DSL methods in <a href="http://code.sethvargo.com/chef-sugar/">several areas</a>, such as cloud (e.g.: <code>cloud?</code>, <code>ec2?</code>) or platform (e.g.: <code>ubuntu?</code>, <code>centos?</code>). There are <a href="https://github.com/sethvargo/chef-sugar/issues">ongoing discussions</a> to add additional helper methods. In his article, Seth shows an example that contrasts a recipe with and without the use of Chef Sugar. This recipe:</p>
<pre>
include_recipe 'cookbook::_windows_setup' if platform_family?('windows')  
include_recipe 'cookbook::_ec2_setup' if node['ec2'] || node['eucalyptus']

package 'foo' do  
  action :nothing
end.run_action(:install)

execute 'untar package' do  
  if node['kernel']['machine'] == 'x86_64'
    command 'ARCH_FLAGS=x64 make'
  else
    command 'ARCH_FLAGS=i386 make'
  end
  not_if do
    ::File.exists?('/bin/tool') &amp;&amp;
    ::File.executable?('/bin/tool') &amp;&amp;
    shell_out!('/bin/tool --version').stdout.strip == node['tool']['version']
  end
end

credentials = Chef::EncryptedDataBagItem.load('accounts', 'passwords') 
</pre>
<p>can be transformed into this recipe:</p>
<pre>
include_recipe 'cookbook::_windows_setup' if windows?  
include_recipe 'cookbook::_ec2_setup' if ec2? || eucalyptus?

compile_time do  
  package 'apache2'
end

execute 'untar package' do  
  if _64_bit?
    command 'ARCH_FLAGS=x64 make'
  else
    command 'ARCH_FLAGS=i386 make'
  end
  not_if { installed_at_version?('/bin/tool', node['tool']['version']) }
end

credentials = encrypted_data_bag_item('accounts', 'passwords')	
</pre>
<p>Chef Sugar was intentionally written to be accessible within a recipe, but also as a <a href="http://docs.opscode.com/essentials_cookbook_libraries.html">Chef library</a>, the concept that allows arbitrary Ruby code to be included in a cookbook. The only significant difference is that when used as a library, Chef Sugar's methods take a <a href="http://docs.opscode.com/essentials_node_object.html">node object</a> as a parameter:</p>
<pre>
# cookbook/libraries/default.rb
def only_on_windows(&amp;block)  
  yield if Chef::Sugar::PlatformFamily.windows?(@node)
end 
</pre>
<p>InfoQ: Syntactic sugar is sometimes viewed as something superfluous and less important. Since you created a project called Chef Sugar you clearly don't think that's always the case. When do you think a bit of sugar is good and when do you think it's a bit too much?</p>
<blockquote> 
 <p>I think syntactic sugar is one of the top reasons why Ruby (and Rails) became such a hit among developers. For example, ActiveSupport adds sugar to Ruby's Integer class that permits method calls like <code>5.days.ago</code>. Sugar is incredibly useful in reducing complexity and repetition. Many cookbooks share common idioms or patterns - like checking if a piece of software is installed at a particular version. When I saw this type of pattern appearing, I knew it was time to slap on some sugar.</p> 
 <p>Conversely, I did not (and do not) actively seek areas to &quot;sugarize&quot;. I think this is an often-made mistake. In my opinion, a sugar has gone too far when there are more than two logic branches or components. For example, one could easily write a sugar that wraps a bunch of logic and resources, but this is better served as a library or LWRP. Sugars should be easily testable and maintainable, and novice developers should be able to dissect the method that defines the syntactic sugar.</p> 
</blockquote>
<p>InfoQ: Do you believe that, in general, this kind of features should be available in the core of an application or is it better to have them as &quot;add-ons&quot;? Why?</p>
<blockquote> 
 <p>I am a firm believer in the plugin-architecture pattern. I easily could have added Chef Sugar to core Chef, but I made the conscious decision to keep it isolated. Just like a developer should not be forced to use ActiveSupport, a Chef developer should not be forced to use Chef Sugar.</p> 
 <p>From a maintainability standpoint, having Chef Sugar as a separate gem allows me to work and iterate independently of the Chef release cycle. Ruby itself is consuming this kind of plugin-pattern, migrating core Ruby classes to gems with individual maintainers. Rubinius 2.0 is entirely composed of gems. Just like there are advantages of having a distributed system instead of one monolithic application, those same advantages are present when using a plugin-based &quot;add-on&quot; rather than bundling the component in the core framework. This pattern is also present in tools like Vagrant Knife (the CLI for Chef) or Rubygems.</p> 
 <p>There is, however, a happy medium in which the plugin is locked and bundled at a particular version in the core (as a dependency), but continues to live outside of the framework as an isolated resource. Users may choose to update to the latest version of the plugin at any time, or wait to upgrade the entire software package. Ruby 2.0 follows this pattern. Try uninstalling bigdecimal and you will get this error:</p> 
 <pre>
ERROR:  While executing gem ... (Gem::InstallError)
    gem &quot;bigdecimal&quot; cannot be uninstalled because it is a default gem
</pre> 
 <p>But Ruby developers can choose to upgrade to a newer version of bigdecimal at any time.</p> 
 <p>The last thing to consider (which is often overlooked), is the licensing implications. In the case of Chef Sugar, both Chef and Chef Sugar are licensed under the Apache 2.0 license, so it is not a concern. Sometimes it is not possible to bundle a plugin in a core application because it would disallow reselling, patenting, etc.</p> 
</blockquote>
<p>InfoQ: Is there any remaining area of Chef that could benefit with additional Chef Sugar methods?</p>
<blockquote> 
 <p>As I said earlier, I do not actively seek areas to &quot;sugarize&quot;. When I first released Chef Sugar, there was immense popularity. Within 20 minutes, a community member added FreeBSD platform support. The project then lived for two months without any maintenance (it just &quot;worked&quot;). About a month ago, someone added support for Cloudstack.</p> 
 <p>I tend to pride myself on quickly acknowledging and merging pull requests, so I always encourage people to submit them. I am also not afraid to say no when I think a patch exceeds the goals of the project. If a community member sees an area that can be &quot;sugarized&quot;, I am happy to take a look!</p> 
</blockquote>
<p>InfoQ: What are the most important areas in Chef that could benefit with more community involvement?</p>
<blockquote> 
 <p>All of Chef's issues are tracked on <a href="https://tickets.opscode.com">Chef Software's ticketing system</a>. Most of the issues are triaged and ordered by priority. For new community members, issues tagged &quot;trivial&quot; or &quot;minor&quot; probably involve minimal changes and are a great way to dive into the Chef core. And lastly, never underestimate the power of typographical or grammatical fixes. As Chef is gaining increasing popularity, users of non-English backgrounds should be able to consume the documentation too.</p> 
 <p>Additionally, there is an open GitHub project for <a href="https://github.com/opscode/chef-rfc">Chef RFCs</a>. These are proposals from the community for high-level features or changes in the Chef roadmap. The Pull Requests in that repository significantly benefit from community involvement (even if it is just a simple :+1:).</p> 
 <p>Aside from the Chef core software project, it was announced at the Chef Community summit last November some important changes to the <a href="https://tickets.opscode.com/browse/COOK">COOK project</a> (the community cookbooks that Chef maintains). Chef is in the process of sharing responsibility for <a href="http://community.opscode.com/cookbooks">community cookbooks</a> with Chef community members.</p> 
</blockquote>
<p>&nbsp;</p><br><br><br><br><br><br></body></html>
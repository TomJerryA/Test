<p class="p1"><a href="http://www.hashicorp.com">HashiCorp's</a> latest addition to support <a href="http://aws.amazon.com">Amazon AWS</a> as provider for <a href="http://www.vagrantup.com/">Vagrant</a> Virtual Machines (VM) is in a new league: for the first time it will be possible to spin up <a href="http://www.hashicorp.com/blog/preview-vagrant-aws.html">Virtual Machines in the cloud</a> instead of the developer's desktop.</p> 
<p class="p1">With supporting Amazon AWS developers will be able to use the very same set of commands to manage EC2 instances. No matter whether the local developer box is not powerful enough to run the required environment or developers want to spin up staging or even production environments - everything will be possible with Vagrant 1.1. This is a major step to further simplify managing various environments for developers. It has the potential to further streamline the collaboration between development and operations - it can help strengthen a <a href="http://www.infoq.com/devops;jsessionid=2D98C560E5732322670C49775374820D">DevOps culture</a> in an organization.</p> 
<p class="p1">The upcoming Vagrant 1.1 will enable developers to pass the desired provider as a command line argument:</p> 
<pre class="p1">
$ vagrant up --provider aws</pre> 
<p class="p1">Instead of using the default <a href="https://www.virtualbox.org/">VirtualBox</a> the above command will use the new AWS provider and instantiate an EC2 instance instead. Destroying the Vagrant managed instance happens with <em>vagrant destroy</em> as one would expect.</p> 
<p class="p1">The Vagrantfile will support defining additional parameters for AWS like the region in which the instance(s) should be created:</p> 
<pre class="p1">
config.vm.provider :aws do |aws|
&nbsp;&nbsp; aws.region = &quot;eu-west-1&quot;
end</pre> 
<p id="lastElm"></p>
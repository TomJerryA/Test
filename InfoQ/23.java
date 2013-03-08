<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Vagrant Support for Amazon AWS and Rackspace</h3><p><a href="http://www.hashicorp.com">HashiCorp's</a>&nbsp;latest addition to support&nbsp;<a href="http://aws.amazon.com">Amazon AWS</a>&nbsp;and&nbsp;<a href="http://www.rackspace.com">Rackspace</a>&nbsp;as providers for&nbsp;<a href="http://www.vagrantup.com/">Vagrant</a>&nbsp;enables new usage scenarios: it will be possible to spin up&nbsp;<a href="http://www.hashicorp.com/blog/preview-vagrant-aws.html">Virtual Machines in the cloud</a>&nbsp;instead of the developer's desktop. The new providers are one more step towards Mitchell Hashimoto's vision of making Vagrant&nbsp;<em>the</em>&nbsp;work environment tool to make the entire workflow of dev =&gt; prod as simple as possible, as he explained to InfoQ.</p> 
<p class="p1">With Vagrant 1.1, scheduled to be released on March 12, developers will be able to use one set of commands - no matter whether they want to manage EC2 instances, Rackspace cloud servers, VirtualBox or VMware Fusion VMs, to create new work environments for development, quality assurance or even production.</p> 
<p class="p1">As Rackspace uses <a href="http://www.openstack.org">OpenStack</a> to run its cloud servers, Vagrant is 90% there to support OpenStack as well, according to Hashimoto. He hopes that Open Source developers take over and add the missing pieces.</p> 
<p class="p1">The upcoming Vagrant 1.1 will enable developers to pass the desired provider as a command line argument:</p> 
<pre class="p1">
$ vagrant up --provider aws</pre> 
<p class="p1">Instead of defaulting to&nbsp;<a href="https://www.virtualbox.org/">VirtualBox</a>, the above command will use the new AWS provider and instantiate an EC2 instance instead.&nbsp;</p> 
<p class="p1">The Vagrantfile will support defining additional parameters for AWS like the region in which the instance(s) should be created:</p> 
<pre class="p1">
config.vm.provider :aws do |aws|
&nbsp;&nbsp; aws.region = &quot;eu-west-1&quot;
end</pre> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
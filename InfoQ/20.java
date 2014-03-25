<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Vagrant Launches Collaboration Tools for Development Environments</h3><p>DevOps tool provider <a href="http://www.vagrantup.com/" target="_blank">Vagrant</a> announced significant new features in their 1.5 release, including a public image repository and the ability to share access to running environments. The Vagrant Cloud is meant to simplify the discovery and distribution of complete development environments. Vagrant Share lets developers collaborate with others by exposing HTTP or SSH access to these virtual environments.</p>
<p>In a <a href="http://www.vagrantup.com/blog/vagrant-1-5-and-vagrant-cloud.html" target="_blank">recent blog post</a>, the Vagrant team announced a batch of features in Vagrant 1.5. Up until now, users of Vagrant – a tool that simplifies the creation and distribution of configured Linux virtual machines – had to <a href="http://www.vagrantbox.es/" target="_blank">hunt around</a> for machine templates to use. These templates, packaged up into “boxes”, form the foundation of Vagrant and work across a range of providers including <a href="http://docs.vagrantup.com/v2/virtualbox/index.html" target="_blank">VirtualBox</a>, AWS, <a href="http://docs.vagrantup.com/v2/vmware/index.html" target="_blank">VMware</a>, and now, <a href="http://docs.vagrantup.com/v2/hyperv/index.html" target="_blank">Hyper-V</a>. With the launch of the <a href="https://vagrantcloud.com" target="_blank">Vagrant Cloud</a>, developers have a centralized location to access public or private boxes, <a href="https://vagrantcloud.com/help/boxes/lifecycle" target="_blank">version</a> their boxes, and release boxes for others to use.</p>
<p>Vagrant and its users are populating the public repository with a wide variety of ready-to-use boxes for others to discover. A simple Vagrant Cloud <a href="https://vagrantcloud.com/search?utf8=%E2%9C%93&amp;sort=&amp;provider=&amp;q=ubuntu" target="_blank">search for “Ubuntu”</a> returns many boxes and lets the user filter results by hosting provider. Logged-in users can also sort results by download count to find the most popular boxes. The Vagrant Cloud contains boxes for Docker, CoreOS, CentOS, Chef, Puppet, Salt, nginx, ElasticSearch, MySQL, Redis, and more.</p>
<p>Vagrant seems to be making developer collaboration a key part of their software. The new Vagrant Share gives any person in any location live access to a running box. In <a href="http://www.vagrantup.com/blog/feature-preview-vagrant-1-5-share.html" target="_blank">a blog post about this preview feature</a>, Vagrant explained what this feature is all about.</p>
<blockquote> 
 <p>This feature lets you share a link to your web server to a teammate across the country, or just across the office. It'll feel like they're accessing a normal website, but actually they'll be talking directly to your running Vagrant environment. They'll be able to see any changes you make, as you make them, in real time.</p> 
 <p>With Vagrant Share, others can not only access your web server, they can access your Vagrant environment like it was any other machine on a local network. They can have access to any and every port.</p> 
</blockquote>
<p>There are <a href="http://docs.vagrantup.com/v2/share/index.html" target="_blank">three modes of sharing</a> that developers can apply to their box. The <a href="http://docs.vagrantup.com/v2/share/http.html" target="_blank">HTTP sharing</a> option produces a URL that anyone can use to access a Vagrant environment, even if either party is behind a NAT device or firewall. For more than just web server access, developers can <a href="http://docs.vagrantup.com/v2/share/ssh.html" target="_blank">open up SSH</a> to outside participants. Vagrant pointed out example use cases for this, including troubleshooting assistance or pair programming. The final sharing mode is called <a href="http://docs.vagrantup.com/v2/share/connect.html" target="_blank">General Sharing</a>. This lets a developer expose any or all ports of a Vagrant environment to outside participants. For those concerned about the security implications of these sharing features, Vagrant <a href="http://docs.vagrantup.com/v2/share/security.html" target="_blank">described some security considerations</a> and mechanisms for protection.</p>
<p>What’s next? Vagrant <a href="http://www.vagrantup.com/blog/vagrant-1-5-and-vagrant-cloud.html" target="_blank">promises</a> a more robust Vagrant Cloud, a commercialization plan, and support for Windows guests.</p>
<blockquote> 
 <p>Coming very soon to Vagrant Cloud: support for organizations, API access, audit logs and statistics for box usage, ACLs on Vagrant Shares, custom domains, and more.</p> 
 <p>Vagrant Cloud is completely free for now. While we'll eventually charge for some access to it, most personal usage will likely remain free. Our current plans for pricing revolve around commercial use and advanced features.</p> 
 <p>…</p> 
 <p>Vagrant will also have full support for Windows-based guest machines, finally. And we're planning on adding at least two providers to core, if not more.</p> 
</blockquote><br><br><br><br><br><br></body></html>
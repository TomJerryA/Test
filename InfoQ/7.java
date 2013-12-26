<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Xen Project Releases 1.0 of Mirage OS</h3><p><a href="http://blog.xen.org/index.php/2013/12/09/announcing-the-1-0-release-of-mirage-os/">Mirage OS</a> is a ‘cloud operating system’ that seeks to avoid security vulnerabilities and bloat by facilitating the creation of single purpose virtual appliances. Applications are developed in the <a href="https://en.wikipedia.org/wiki/Ocaml">OCaml</a> functional programming language and compiled into standalone ‘unikernels’ that run directly on the <a href="https://en.wikipedia.org/wiki/Xen">Xen</a> hypervisor. By removing the traditional operating system, and replacing it with language libraries that replicate operating system constructs, Mirage offers the promise of smaller, faster applications with a reduced attack surface area. Applications can be deployed directly into Xen based public clouds such as Amazon’s EC2 and Rackspace Cloud.</p>
<p>The Mirage OS approach is likely to appeal most to creators of infrastructure software such as web servers, DNS servers and software defined networking (SDN). University of Cambridge contributor <a href="http://anil.recoil.org/#!">Anil Madhavapeddy</a> comments:</p>
<blockquote>
 Mirage represents our dream to be able to rapidly build specialised infrastructure applications using modern, modular programming techniques such as those found in OCaml. We've seen a lot of datacenter tools being written in high-level languages (most often Java and Scala), and we wanted to explore the benefits (and drawbacks!) of bringing functional programming techniques down to the bare metal.
</blockquote>
<p>At present the system targets the Xen hypervisor, and can also build Unix user space binaries. The project also has experimental ports to FreeBSD kernel modules, the NS3 network simulator and JavaScript. Anil Madhavapeddy adds:</p>
<blockquote>
 Porting it to run on other hypervisors such as VMWare, KVM and Hyper-V is simply a matter of writing an appropriate bootloader and virtual device drivers. This is an excellent project for someone who wants to get their feet wet with systems programming, and we'd be happy to mentor them on our mailing list (mirageos-devel@lists.xenproject.org).
</blockquote>
<p>A significant potential application area for Mirage OS is to provide a smaller and more secure ‘domain 0’, the special domain used for the management of a hypervisor. Anil Madhavapeddy states that this has been one of the primary drivers behind Mirage development:</p>
<blockquote>
 The XenServer distribution has been steadily eliminating the requirement for a single monolithic &quot;domain 0&quot; for some years now, and Mirage provides the final piece of the puzzle: a programming environment to convert the management toolstack into a set of specialised microkernels that communicate and achieve consensus with each other using standard distributed systems protocols. This will really raise the bar for building more secure clouds, since the management toolstack holds the keys to all the customer data held within the virtual machines in a cluster.
</blockquote>
<p>On the question of why OCaml was chosen University of Cambridge contributor Richard Mortier says:</p>
<blockquote>
 Several reasons: tried and tested functional language; active community; very efficient and relatively simple to port runtime; large parts of the Xen management stack were already written in OCaml; the powerful module system makes it possible to really effectively modularise the system.
</blockquote>
<p>When asked about potential tie ins to trusted execution environments Citrix XenServer systems architect <a href="http://dave.recoil.org/#!">David Scott</a> explains:</p>
<blockquote>
 For me, there are two important aspects to trusted execution: (i) how do you check that you're running the binary you thought you were running; and (ii) how do you know the code is doing what you think it should be doing. Techniques such as measured boot focus on the first of these: checking you're running the right binary. Mirage helps with the second by: 
 <list> 
  <ul> 
   <li>Minimising the attack surface by only linking in the libraries you need.</li> 
   <li>Allowing your configuration to be linked into your app, rather than stored somewhere external on a (possibly mutable) filesystem.</li> 
   <li>Maximising the amount of code which is immune to certain kinds of memory corruption and buffer overflow attacks.</li> 
  </ul> 
 </list> 
</blockquote>
<p>The Mirage OS team are also targeting embedded applications and Internet of Things (IoT) use cases. Anil Madhavapeddy points out that ‘the OCaml compiler itself is easy to retarget to tiny targets (even a <a href="http://www.algo-prog.info/ocaml_for_pic/web/">PIC18 microcontroller</a>)’, but ‘the bulk of the effort is around the build systems’. The development team are moving their personal web pages to Mirage OS based servers over the holidays, with one of them using as Raspberry Pi as the back end.</p><br><br><br><br><br><br></body></html>
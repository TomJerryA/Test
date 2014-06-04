<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>PowerShell Desired State Configuration Takes on Linux</h3><p>Microsoft continues to invest in <a href="http://technet.microsoft.com/en-us/library/bb978526.aspx">PowerShell</a>, its command-line shell and associated scripting language. <a href="http://technet.microsoft.com/en-us/library/dn249912.aspx">PowerShell Desired State Configuration</a> (DSC) can now <a href="http://blogs.msdn.com/b/powershell/archive/2014/05/19/announcing-windows-powershell-desired-state-configuration-for-linux.aspx">manage Linux boxes</a>.</p>
<p>PowerShell DSC for Linux was <a href="http://channel9.msdn.com/Events/TechEd/NorthAmerica/2014/DCIM-B417#fbid=?hashlink=fbid">announced</a> at the last <a href="http://northamerica.msteched.com/">TechEd North America</a>. DSC for Linux's first resource providers are the basic building blocks for infrastructure management, following the same path that DSC for Windows treaded. As <a href="http://blogs.msdn.com/b/powershell/archive/2014/05/19/announcing-windows-powershell-desired-state-configuration-for-linux.aspx">reported</a> by the PowerShell team's blog, they are:</p>
<blockquote> 
 <ul> 
  <li>nxFile – manage files and directory state</li> 
  <li>nxScript – runs script blocks on target nodes</li> 
  <li>nxUser – manages Linux users</li> 
  <li>nxGroup – manages Linux groups</li> 
  <li>nxService – manages Linux services (System-V, Upstart, SystemD)</li> 
 </ul> 
</blockquote>
<p>DSC for Linux uses the <a href="https://collaboration.opengroup.org/omi/">Open Management Infrastructure</a> (OMI), open-sourced by Microsoft in 2012, as a <a href="http://en.wikipedia.org/wiki/Common_Information_Model_(computing">Common Information Model</a> (CIM) server. Microsoft is positioning PowerShell DSC as a platform on which tool vendors build their products, so it's not in direct competition with tools like Puppet or Chef. Indeed, several tool vendors are working with Microsoft to support PowerShell DSC, as <a href="http://channel9.msdn.com/events/TechEd/NorthAmerica/2014/DCIM-B324#fbid=">demonstrated</a> (check around minute 51) by Julian C. Dunn, from Chef. Julian shows Chef's cookbooks using Powershell DSC resources, directly embedded in Chef's DSL.</p>
<p><img src="http://www.infoq.com/resource/news/2014/05/powershell-dsc-takes-on-linux/en/resources/DSC.png" alt="PowerShell DSC Architecture" _href="img://DSC.png" _p="true" /></p>
<p style="text-align:center"><em>PowerShell DSC Architecture (Credits: Hemant Mahawar and Narayanan Lakshmaman)</em></p>
<p><a href="http://social.technet.microsoft.com/profile/Kris%20Bash">Kris Bash</a>, Senior Program Manager in the Microsoft Open Source Technology Center, wrote a <a href="http://blogs.technet.com/b/privatecloud/archive/2014/05/19/powershell-dsc-for-linux-step-by-step.aspx">step-by-step guide</a> on how to build, install and use DSC for Linux on a CentOS 6 system, although Kris stated that it should also work on Debian/Ubuntu.</p>
<p>Although DSC for Windows supports both <a href="http://www.infoq.com/news/2013/12/powershell-dsc-push-and-pull">pull and push modes</a>, DSC for Linux's current release only supports the simpler push mode. PowerShell DSC is available as a <a href="http://blogs.msdn.com/b/sqlphp/archive/2010/06/14/what-is-a-community-technology-preview-ctp.aspx">Community Technology Preview</a> (CTP) and is <a href="https://github.com/MSFTOSSMgmt/WPSDSCLinux/releases">hosted</a> on GitHub.</p>
<p>InfoQ spoke with Kris to know more about this initiative.</p>
<p><strong>InfoQ: What Linux distributions are supported by PowerShell DSC for Linux?</strong></p>
<blockquote> 
 <p>When DSC for Linux reaches general availability, we will support Red Hat Enterprise Linux, SUSE Linux Enterprise Server, CentOS, Ubuntu Server, Oracle Linux and Debian – the same enterprise distros supported for running with Hyper-V and managing with System Center. We will continue to release the source as we add features, so that DSC can be modified and built to support other operating systems.</p> 
</blockquote>
<p><strong>InfoQ: Do you intend to release additional resources in the same fashion that you've been doing with Windows? Can you shed a light on what resources are in the pipeline?</strong></p>
<blockquote> 
 <p>Yes, we do have plans to release additional resources. Firstly, we will complete the base set of “built-in” resources, and then move on to other common configuration scenarios, with Linux networking configuration being a likely target. We are also working on guidance for resource development for Linux so that others can build and share their own custom resources.</p> 
</blockquote>
<p><strong>InfoQ: Why did you choose to host DSC For Linux on GitHub?</strong></p>
<blockquote> 
 <p>We believe that GitHub is familiar to most Linux administrators, and we have a history of releasing Linux-oriented features on GitHub, such as the Windows Azure Linux Agent and Beanspy (for monitoring of JEE application servers).</p> 
</blockquote>
<p><strong>I</strong><strong>nfoQ: Do you plan to accept contributions?</strong></p>
<blockquote> 
 <p>We are currently evaluating this topic. In the meantime, we would ask that early adopters report any issues or requests as Issues on the GitHub repo.</p> 
</blockquote><br><br><br><br><br><br></body></html>
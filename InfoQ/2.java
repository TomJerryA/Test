<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Microsoft to Stop Honoring SHA1 Certificates for SSL and Code Signing</h3><p>The US National Institute of Standards and Technology has recommended that SHA1 no longer be trusted past January of 2014. But with 98% of certificates issued world-wide being based on that standard an immediate change is no feasible. So <a href="http://blogs.technet.com/b/pki/archive/2013/11/12/sha1-deprecation-policy.aspx">Microsoft is giving websites until January first of 2017 to replace their SSL certificates with a more secure version</a>.</p>
<p>Application vendors that need to sign their code are also affected. They only have until January first of 2016 to acquire new code signing certificates. “SHA1 code signing certificates that are time stamped before 1 January 2016 will be accepted until such time when Microsoft decides SHA1 is vulnerable to pre-image attack.”</p>
<p>These polices are subject to review in the middle of 2015. Two key factors that may affect Microsoft’s timelines are:</p>
<blockquote> 
 <p>whether SHA1 is still considered resistant to pre-image attacks by the security community, and</p> 
 <p>whether a significant portion of the ecosystem is not capable of switching to SHA2. Third party legacy systems and embedded devices that cannot be upgraded to SHA2 may be particularly susceptible. We will continue to gather data on this portion of the ecosystem.</p> 
</blockquote>
<p>As currently written the SHA1 Deprecation Policy will apply to Windows Vista, Windows Server 2008, and later operating systems. Those still running Windows XP will need at least Service Pack 3 in order to use SHA2. Windows Server 2003 Service Pack 2 also supports SHA2.</p><br><br><br><br><br><br></body></html>
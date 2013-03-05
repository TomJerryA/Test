<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Expired SSL Certificates Break Azure and TFS</h3><p class="western" style="margin-bottom: 0in"><span lang="en-US">Users of Windows Azure storage experienced a lengthy outage on February 22. &nbsp;T</span><span lang="en-US">eam Foundation Service (TFS) relies on Azure to provide backend storage, and so as a result also &nbsp;experienced</span><span lang="en-US"> a</span><span lang="en-US"> <a class="western" href="http://blogs.msdn.com/b/bharry/archive/2013/02/23/bad-day.aspx">nine hour outage</a>. &nbsp;</span>The outage was due to the expiration of <a class="western" href="http://en.wikipedia.org/wiki/SSL_certificate">SSL certificates</a> used to secure and authenticate HTTPS traffic.&nbsp;As key certificates expired, communication across HTTPS with the affected servers began to fail. HTTP communication remained operational in some cases, however it is by definition insecure and of use only to those customers who could tolerate communicating in plaintext.</p> 
<p class="western" style="margin-bottom: 0in">Officially the outage began at 12:29 PST on February 22 and affected customers across all regions that were accessing Windows Azure storage using HTTPS. &nbsp;Availability was restored worldwide for all customers by 00:09 AM PST on February 23, 2013.</p> 
<p class="western" style="margin-bottom: 0in;">Microsoft's Mike Neil, general manager of Windows Azure provided <a class="western" href="http://blogs.msdn.com/b/windowsazure/archive/2013/03/01/details-of-the-february-22nd-2013-windows-azure-storage-disruption.aspx">details</a> of the failure. Azure uses SSL to secure traffic for throughout the service, in particular between the 3 major storage types: blobs, queues, and tables. In this case, the outage began when the certificates for these areas began to expire:</p> 
<blockquote> 
 <ul> 
  <li>*.blob.core.windows.net Friday, February 22, 2013 12:29:53 PM PST</li> 
  <li>*.queue.core.windows.net Friday, February 22, 2013 12:31:22 PM PST</li> 
  <li>*.table.core.windows.net Friday, February 22, 2013 12:32:52 PM PST</li> 
 </ul> 
</blockquote> 
<p class="western" style="margin-bottom: 0in;">Neil went on to describe how the automated process of monitoring and updating the SSL certificates in use by the Azure system broke down. The monitoring system notified the appropriate staff that updated certificates were needed-- these were then created and packaged in a routine system update. Unfortunately this update was not labeled as containing time-sensitive components, so it was deprioritized in favor of other updates.</p> 
<p class="western" style="margin-bottom: 0in;">Since new certificates were created and marked updated in the monitoring service, no further update notices were sent. Thus the new certificates languished in the update queue and master certificate repository, but never made it to the production Azure environment.</p> 
<p class="western" style="margin-bottom: 0in;">A corrective patch was created for deployment that restored HTTPS service to a majority of customers by 22:45 PST, with full service restoration declared February 23<sup>rd</sup> at 00:09 PST. As a result of the outage affected customers will receive 25% service credit. The automated certificate monitoring process has been updated so that certificates are monitored at the end points so that a failed/delayed deployment would not be overlooked.</p> 
<p class="western" style="margin-bottom: 0in">Harry noted that running and maintaining large online systems is complex:</p> 
<blockquote> 
 <p class="western" style="margin-bottom: 0in">Of course, one of the things you quickly learn when operating a large scale mission critical service is that you can’t assume anything is going to work... The hard thing about this is that anything can go wrong and it’s only obvious in hindsight what you should have been protecting against – so you have to try to protect against every possibility.</p> 
</blockquote> 
<p class="western" style="margin-bottom: 0in;">Neil observed that original Azure system suffered from a single point of failure:</p> 
<blockquote> 
 <p class="western" style="margin-bottom: 0in">“While the expiration of the certificates caused the direct impact to customers, a breakdown in our procedures for maintaining and monitoring these certificates was the root cause. Additionally, since the certificates were the same across regions and were temporally close to each other, they were a single point of failure for the storage system.”</p> 
</blockquote> 
<p class="western" style="margin-bottom: 0in;">Users commenting on the outage noted the seriousness of the outage and the need for reliable systems. User “trievangelist” noted his workaround for NuGet during the outage:</p> 
<blockquote> 
 <p class="western" style="margin-bottom: 0in"><i>trievangelist 23 Feb 2013 6:49 AM #</i></p> 
 <p class="western" style="margin-bottom: 0in"><i>Thank you for posting this, Brian. We were impacted when our build processes, which use NuGet and rely on downloading the latest version of nuget.exe from nuget.org began failing. Thankfully we are using an internal NuGet gallery and I was able to work around the problem by using a local version of nuget.exe.</i></p> 
</blockquote> 
<p class="western" style="margin-bottom: 0in;">User Keith Richardson used the outage to explain why his firm is not interested in migrating systems to the cloud:</p> 
<blockquote> 
 <p class="western" style="margin-bottom: 0in;"><i>Keith Richardson 25 Feb 2013 8:44 AM #</i></p> 
 <p class="western" style="margin-bottom: 0in"><i>This is yet another reason we won't move to the cloud. Every 6-7 months you guys seem to have an outage of some sort or another...if this was internal we would fire someone/a vendor. I can't stress this enough. We would FIRE someone.</i></p> 
</blockquote> 
<p id="lastElm"></p></body></html>
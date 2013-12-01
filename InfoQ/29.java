<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>The Costs of Versioning an API</h3><p>Contract versioning and API/Service versioning has always been a consideration for SOA based systems. Whether because of the <a href="http://www.infoq.com/articles/contract-versioning-comp2">impact it has on composability</a>, or <a href="http://www.infoq.com/articles/Web-Service-Contracts">client-service governance</a>, it is still something of an art rather than a science. There are many examples of groups giving the benefit of their experiences (e.g., <a href="http://www.infoq.com/news/2013/09/versioning-restful-services">around REST</a> is <a href="http://www.infoq.com/news/2010/06/rest-versioning">extremely popular</a>). However, recently Jean-Jacques Dubray has <a href="http://www.ebpml.org/blog2/index.php/2013/11/25/understanding-the-costs-of-versioning#">written an article</a> which attempts to inject some scientific objectivity into this problem domain.</p>
<blockquote>
 I have been asked recently to create an estimate of the costs of versioning APIs (or Web Services). I wanted to share this estimate because I feel a lot of pe
 <span style="font-size: 13px; line-height: 19px;">ople still don't understand the cost implications of API/Service versioning. </span>
</blockquote>
<p>According to JJ, during the work they found that the cost of building APIs was dependent upon the approach used subsequently to version them.</p>
<blockquote>
 The key point that [you need] to understand is that even if the cost to your consumers may look small to you, it is not just a pure cost, it is risks, disrupted project plans, unavailable budgets... with changes that often have no immediate business value to an existing consumer who was not expecting any change to API.
</blockquote>
<p>The article then goes on to classify three different approaches to API versioning (see the full article for a more in depth discussion of each, including how JJ defines a way to measure cost):</p>
<ul> 
 <li>The Knot. &quot;All API consumers are tied to a single version of the API, when that API changes, all consumers have to change, in essence creating a massive ripple effect across the entire set of consumers / ecosystem.&quot;</li> 
</ul>
<p><img _p="true" _href="img://Screen Shot 2013-12-01 at 15.44.36.png" src="http://www.infoq.com/resource/news/2013/12/api-versioning/en/resources/Screen Shot 2013-12-01 at 15.44.36.png" alt="" /></p>
<ul> 
 <li>Point-to-Point. &quot;Every service version is left running in production and consumers are required to migrate on their own, when they need to. The maintenance costs increase as the number of version in production increases.&quot;</li> 
</ul>
<p><img _p="true" _href="img://Screen Shot 2013-12-01 at 15.46.06.png" src="http://www.infoq.com/resource/news/2013/12/api-versioning/en/resources/Screen Shot 2013-12-01 at 15.46.06.png" alt="" /></p>
<ul> 
 <li>Compatible Versioning. &quot;<span>All clients talk to the same compatible API/Service version.&quot;</span></li> 
</ul>
<p><img _p="true" _href="img://1Screen Shot 2013-12-01 at 15.48.14.png" src="http://www.infoq.com/resource/news/2013/12/api-versioning/en/resources/1Screen Shot 2013-12-01 at 15.48.14.png" alt="" /></p>
<p>Given these definitions and associated costs computed using the equations JJ describes, it is possible to plot the relative costs as shown below (y axis is cost, x axis is the number of services):</p>
<p><img _p="true" _href="img://Screen Shot 2013-12-01 at 15.54.16.png" src="http://www.infoq.com/resource/news/2013/12/api-versioning/en/resources/Screen Shot 2013-12-01 at 15.54.16.png" alt="" /></p>
<p>&nbsp;</p>
<p>As JJ says:</p>
<blockquote>
 [...] a single version forcing every consumer to upgrade when the API changes is the most expensive to the ecosystem. A multiplicity of versions that need to be maintained is better, but still quite costly when you try to keep upgrading each version or alternatively operating older versions. A compatible versioning strategy seem to offer the best efficiency.
</blockquote>
<p>So what do others think? Is this way of calculating the cost of versioning APIs applicable beyond the environments in which it was developed by JJ and team? Does the relative cost explanation make sense given your own experiences? Are there other categories which JJ and team don't cover?</p><br><br><br><br><br><br></body></html>
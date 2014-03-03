<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Amazon Chooses HAL Media Type for AppStream API</h3><p>Amazon has released a new API, the <a href="http://docs.aws.amazon.com/appstream/latest/developerguide/rest-api.html#rest-api-hal">AppStream API</a>, which allows you to programmatically manage applications hosted on the Amazon AppStream platform. For this API, they chose to build it with <a href="http://tools.ietf.org/html/draft-kelly-json-hal-06">the HAL media type</a>. HAL is a minimalistic hypermedia enabled media type for building machine-to-machine APIs. Amazon is one of the largest organizations to choose hypermedia as a technique for a public-facing product.</p>
<p>While hypermedia APIs are a hot topic in the API space, advocates are often asked about its real-world applicability. While there has been an explosion of research and debate on the technique, hypermedia APIs make up a small fraction of the current API ecosystem. Amazon's CEO, Jeff Bezos, famously required his teams to build products in an SOA style, leading to a large number of internal and external APIs. This vote of confidence in hypermedia via HAL from one of tech's biggest companies should hearten hypermedia enthusiasts.</p>
<p>One question that the hypermedia community is currently grappling with is documentation. The traditional answer to documenting hypermedia services consists of providing a media type definition and nothing more. This approach is significantly different than other architectural styles, and so the community has been working on other strategies to assist bridging this gap.</p>
<p>The AppStream API team chose to document the API in four major sections: header values, error codes, top-level resources, and link relations. This is very different from more traditional RESTful services, which focus on combinations of HTTP status codes, URLs, and parameters. This approach is very close to the traditional hypermedia approach. <a href="https://groups.google.com/forum/#!msg/hal-discuss/3IyTn17m7Ps/AeBpQXadn8gJ">On the HAL-discuss mailing list</a>, a place for HAL users to talk about the specification and its uses, Andr&eacute;s Freyr&iacute;a Cede&ntilde;o said this:</p>
<blockquote> 
 <p>My gut reaction to the docs were along the lines of &quot;this would be sufficient documentation if hypermedia APIs were the norm&quot;. Given the current state of art though, I don't think there are enough ancillary resources for developers to work with.</p> 
</blockquote>
<p>We'll see how this trend continues as hypermedia becomes a more established API pattern.</p>
<p>HAL is a media type currently undergoing standardization by the IETF. Originally authored by Mike Kelly, HAL is focused on providing a simple, easy to understand set of conventions to XML and JSON for resources to link to one another.</p>
<p>Here's a sample HAL response, from the draft:</p>
<pre>
{
     &quot;_links&quot;: {
       &quot;self&quot;: { &quot;href&quot;: &quot;/orders/523&quot; },
       &quot;warehouse&quot;: { &quot;href&quot;: &quot;/warehouse/56&quot; },
       &quot;invoice&quot;: { &quot;href&quot;: &quot;/invoices/873&quot; }
     },
     &quot;currency&quot;: &quot;USD&quot;,
     &quot;status&quot;: &quot;shipped&quot;,
     &quot;total&quot;: 10.20
   }
</pre>
<p>HAL defines two reserved top-level properties, </p>
<pre>_links</pre>
<pre>_embedded</pre>
<pre>_links</pre>
<p></p><br><br><br><br><br><br></body></html>
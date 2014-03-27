<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ASP.NET Web API Gets OData v4.0 Support, WCF Will Not</h3><p>ASP.NET Web API 2.2 for OData v4.0 are now available as nightly builds. The team also <a href="http://blogs.msdn.com/b/odatateam/archive/2014/03/21/odata-6-1-and-odata-client-6-1-are-now-shipped.aspx">released OData core libraries version 6.1 on nuget</a> with several bug fixes and new features, especially increased support for OData v4 spec. However, the MS team suggested that WCF will not get OData v4 specific features.</p>
<p>OData v4.0 and OData JSON Format v4.0 <a href="http://blogs.msdn.com/b/interoperability/archive/2014/03/17/odata-v4-0-and-odata-json-format-v4-0-approved-as-oasis-standards.aspx">were recently adopted as an OASIS standard</a>. You can read&nbsp;<a href="http://docs.oasis-open.org/odata/new-in-odata/v4.0/new-in-odata-v4.0.html">what is new in OData v4.0</a>.</p>
<p>Following are the improvements in both ASP.NET Web API 2.2 and the OData core libraries -</p>
<ul> 
 <li>Protocol and format changes from V3 to V4</li> 
 <li>OData attribute routing</li> 
 <li>Support for defining functions in OData model and binding them to controller actions</li> 
 <li>Model aliasing - allowing different names for types or properties of OData models and CLR Types</li> 
 <li>Ability to define which properties of the model can be filtered, sorted, expanded or navigated across</li> 
 <li>Support for ETags</li> 
 <li><a href="http://aspnetwebstack.codeplex.com/workitem/1584">Support for Enums</a></li> 
 <li>Support for $format query string option so client can specify the format</li> 
 <li><a href="http://blogs.msdn.com/b/odatateam/archive/2014/03/05/use-singleton-to-define-your-special-entity.aspx">Singleton support</a></li> 
 <li><a href="http://blogs.msdn.com/b/odatateam/archive/2014/03/13/containment-is-coming-with-odata-v4.aspx">Containment support</a></li> 
</ul>
<p>Known limitations -</p>
<ul> 
 <li>There are many OData v4 featuers that are still not supported - the main focus of the release was feature parity with earlier release along with few new features</li> 
 <li>OData core libraries are capable of serializing the OData v4 Atom format but this is not officially supported since Atom specification is not at CS2 stage yet.</li> 
</ul>
<p>On the client side, there is a new package that supports only OData v4.0 - if your client needs to consume both V1-3 and V4 services, then you'll have to use both the new and the old packages in your application.</p>
<p>A somewhat controversial decision is to reduce investments in making WCF a stack for building OData services. This is what the OData Services team had to say -</p>
<blockquote> 
 <p>..we do plan to reduce investment in WCF Data Services as a stack for creating OData services. To mitigate the inconvenience this may cause, we are working on cleaning up the code and making it compatible with OData v4, and will then release that stack as open source. We do not plan to put any significant investment into adding v4-specific features to the WCF DS stack.</p> 
</blockquote>
<p>The community, however, wants WCF to support OData 4.0. <a href="http://blogs.msdn.com/b/odatateam/archive/2014/03/21/odata-core-libraries-now-support-odata-v4.aspx#10510961">Says Adam</a> -</p>
<blockquote> 
 <p>As our business tier is written in WCF DS, I feel that we have been thrown under the bus on this decision. We have invested so much effort in working around the weaknesses of WCF DS (prop change tracking, performance, containment, hackish T4 support for client proxies, terrible EF6 alpha quality provider, etc) and have been happily awaiting your new v4 release only to find out at this stage that you are abandoning it. Switching to Web API at this point seems like we pay the price for every decision you make. We are a Gold MS Partner.</p> 
</blockquote>
<p>Others have <a href="http://blogs.msdn.com/b/odatateam/archive/2014/03/21/odata-6-1-and-odata-client-6-1-are-now-shipped.aspx#10510500">also</a> <a href="http://blogs.msdn.com/b/odatateam/archive/2014/03/21/odata-6-1-and-odata-client-6-1-are-now-shipped.aspx#10510761">requested</a> that for OData v4.0 support in WCF. We can only wait and watch whether Microsoft changes it's decision on this.</p>
<p>You can get started with <a href="http://blogs.msdn.com/b/webdev/archive/2014/03/13/getting-started-with-asp-net-web-api-2-2-for-odata-v4-0.aspx">writing an OData v4.0 service</a> and use the <a href="http://blogs.msdn.com/b/odatateam/archive/2014/03/11/how-to-use-odata-client-code-generator-to-generate-client-side-proxy-class.aspx">OData Client Code Generator</a> to generate client-side proxy classes.</p><br><br><br><br><br><br></body></html>
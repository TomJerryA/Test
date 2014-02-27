<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Anypoint for APIs: An Interview with Uri Sarid</h3><p>MuleSoft recently released a significant upgrade to their <a href="http://mulesoft.com/platform/api">Anypoint platform for APIs</a> which brings together API design, collaboration and API management features. InfoQ interviewed MuleSoft CTO, Uri Sarid to find out more about the platform.</p>
<p>
 <bold>
  <strong>InfoQ: The new release of Anypoint platform for APIs comprises three components: API Portal, API Manager and Mule Studio. Mule Studio is already well known, can you give us a brief overview of the two new components - API Portal and API Manager?</strong>
 </bold></p>
<blockquote>
 <strong>US:</strong> The Anypoint API Portal is where you can design APIs in collaboration with your stakeholders and future app developers, mock them, document them, explore them before or after implementation with the console and the notebook and fully engage with your developer community. It's tightly integrated with the Anypoint API Manager, which gives you complete control over who can access your APIs, place limits on their usage, and measure and analyze how they're being used.
 <br /> 
</blockquote>
<p>
 <bold>
  <strong>InfoQ: You're promoting a &quot;</strong>
  <a href="http://blog.programmableweb.com/2014/01/09/the-emergence-of-api-first-development/"><strong>Design First</strong></a>
  <strong>&quot; methodology whereby the API contract is the primary artifact and then the implementation follows. Can you describe the type of workflow or lifecycle that you envisage for API developers?</strong>
 </bold></p>
<blockquote>
 <strong>US:</strong> It's like any other product design, where careful craftsmanship and attention to the user experience — in this case, the developer users — yields disproportionately high benefits once the product is launched — in this case, the API being published. So you roughly sketch out the API appropriate for the domain and the primary use cases using 
 <a href="http://raml.org/">RAML</a> (the RESTful API Modeling Language), and quickly put it in the hands of some test users. Even in this rough, early phase, there's a live console for the API, and a mocked &quot;implementation&quot; of the service the users can prototype with (e.g. with prototype mobile apps), as well as a live scripting notebook that lets them quickly work out usage scenarios and share their findings. The design is important because the ecosystem that develops around a successful API carries its own momentum, which resists breaking changes to the API. With the API design iterated on until it's accepted by stakeholders, it's time to implement — with confidence now that a faithful implementation will yield delighted developers and the desired benefits. In many cases, the implementation of the API is an exercise in connecting to and from a myriad of existing on-premise and in-cloud systems; Mule Studio and its APIkit components make quick work of turning a RAML spec into a set of Mule integration flows that realize the spec, scalable and maintainably. The resulting Mule application can be deployed in CloudHub or on premise (or a private cloud), while the API it exposes is automatically bound to the Anypoint API Manager, where policies can be applied to it, and to the Anypoint API Portal, where it can be discovered and consumed by app developers.
 <br /> 
</blockquote>
<p>
 <bold>
  <strong>InfoQ: The <a href="http://www.infoq.com/news/2013/05/mulesoft-new-api-platform-mason">first release of APIKit</a> used Swagger as its document format. You've now moved to RAML. Can you tell us what motivated that change? Are there any lessons learned in terms of API documentation?</strong>
 </bold></p>
<blockquote>
 <strong>US:</strong> Simply put, we realized ourselves what numerous others in the API space have realized: that Swagger and similar formats may be suitable as the *output* format of an API, something that expresses it after it exists, but they're not good for designing APIs. Nobody starts by writing down Swagger; they generate it from code, so the API is really designed via its implementation, which is a bit upside down. Moreover, it's quite a verbose description, which can easily lead to losing the forest in the trees: you get reams and reams of description, so you cannot see, and certainly cannot build in, a few clean patterns that can explicitly be reused throughout the API. With RAML, we aimed for a way of designing and expressing RESTful APIs that were as clean, expressive and efficient as REST itself. So far, so good.
 <br /> 
</blockquote>
<p>
 <bold>
  <strong>InfoQ: Are there any changes to Service Registry?</strong>
 </bold></p>
<blockquote>
 <strong>US:</strong> The service registry continues to be a great place to, well, keep a registry of all your services, whether REST or SOAP or even things that many wouldn't even call APIs such as FTP locations. But we're adding many API-specific features to it, such as new policies, integration with the Anypoint API Portal and more integration with existing customer systems.
 <br /> 
</blockquote>
<p>
 <bold>
  <strong>InfoQ: Does API Manager work with APIs that haven't been implemented using Mule? Are there any differences in the way that Mule and non-Mule APIs interact with the platform?</strong>
 </bold></p>
<blockquote>
 <strong>US: </strong>You can use Anypoint API Manager to control APIs that aren't implemented with Mule by proxying them through the API gateway. From a management perspective, or even a portal perspective, all the capabilities are available for these APIs as they would be if the implementation itself was in Mule.
 <br /> 
</blockquote>
<p>
 <bold>
  <strong>InfoQ: What do you see as the biggest remaining challenge with APIs - either for providers or consumers?</strong>
 </bold></p>
<blockquote>
 <strong>US: </strong>Though this certainly feels like the golden age of APIs, there's tremendous room for growth too: many enterprises still have not rolled out broad API initiatives. API design is just now being recognized as a critical discipline, best practices are few and far between, and there's very little consistency across APIs, even within the same organization. There's a huge gap between the API have's and have-not's. And that's felt directly by API consumers, who more often than not struggle with APIs that seem like an afterthought — because they were.
 <br /> 
</blockquote><br><br><br><br><br><br></body></html>
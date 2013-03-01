<p><a href="http://vaadin.com/">Vaadin</a> has released version 7 of its Java-based web application framework. The Vaadin 7 platform is the framework's first major update since 2009.</p> 
<p>Java web application developers may find Vaadin 7 comparable with other frameworks like Wicket, JSF and Google Web Toolkit (GWT) and notice similarities and differences among them. In many ways Vaadin is similar to Wicket - the main difference is that Vaadin does not require the use of HTML templates. Likewise, the similarity between JSF and Vaadin is that they both are server-side frameworks; however Vaadin applications are programmed in plain Java requiring no XML configurations.</p> 
<p>The Vaadin group has been a member of the GWT Steering Committee for over five years, and Vaadin 7 now includes GWT as its core component. In his June 2012 <a href="https://vaadin.com/blog/-/blogs/gwt-built-in-vaadin-7">blog post</a>, Lehtinen suggests that &quot;Anyone who is building their apps using GWT today can move to Vaadin by simply replacing the jars in the project&quot;. Using GWT had some advantages over a traditional Vaadin application, depending on the use case. GWT applications can be made to work off-line, can support larger number of concurrent users (10,000+) where server-side state is not required, and have lower latency. However a traditional Vaadin-based UI running on a Java server or portal is almost certainly easier for a Java developer to build since it can be completely coded in Java.</p> 
<p>The Vaadin development team has implemented <a href="https://vaadin.com/vaadin7">65 new features</a> in addition to the inclusion of GWT. The framework's <a href="https://vaadin.com/faq">FAQ</a> page mentions that Vaadin 7 is a single jar-file implementation following Java EE standards and it uses typical desktop UI programming patterns. The framework also leverages the support and feedback provided by the open source community consisting of over 40,000 active registered members.</p> 
<p>InfoQ communicated with Joonas Lehtinen (CEO, Vaadin.com) to find out more about Vaadin 7.</p> 
<p><strong> InfoQ: Can you list five or six of the most useful features in the latest release of Vaadin from the view of new adopters of the framework? </strong></p> 
<blockquote>
  My top picks list is pretty much the list at: https://vaadin.com/vaadin7 
 <br /> 
 <br /> Out of those, my top-five ones are: 
 <br /> 
 <ol> 
  <li>Full copy of GWT built-in. This allows us to support the whole package and make it easier to leverage the power of Google's brilliant Java-to-JavaScript compiler in your applications.</li> 
  <li>Widget extensions allow adding functionality on top of existing widgets as independent extensions. For more info on this, see https://vaadin.com/wiki/-/wiki/Main/Creating%20a%20component%20extension.</li> 
  <li>Sass compiler introduces long needed modularization of themes.</li> 
  <li>Redesigned layout engine that uses browsers native layout calculations instead of calculating everything in JavaScript. This radically decreases the number of reflows and makes layouts much faster. As a side benefit, we now support all of CSS.</li> 
  <li>Redesigned window API that makes Vaadin applications feel more like web applications and simplifies access to the http request and web page.</li> 
 </ol> 
</blockquote> 
<p><strong> InfoQ: The report &quot;<a href="https://vaadin.com/gwt-report-2012-portlet/download/1871870899/Future-of-GWT-Report-2012.pdf">The Future of GWT Report 2012</a>&quot; says that SmartGWT, GXT and Errai extend GWT while Vaadin complements it. Can you tell us more on that? </strong></p> 
<blockquote>
  The GWT programming model has two levels of abstraction: 
 <br /> 
 <ol> 
  <li>UI written in Java and compiled to JavaScript, and</li> 
  <li>Native JavaScript. SmartGWT, GXT and Errai essentially just provide more (really nice) components and helpers within the programming model defined by GWT.</li> 
 </ol> Vaadin adds a server-side Java programming model on top of the programming model provided by GWT. This higher level abstraction speeds up development by decreasing the number software layers required to implement a modern web application. In GWT, one needs to build the UI layer (in browser), RPC plus UI services (in server) and the business logic (in server). In Vaadin, only server-side UI and business logic layers are required. This essentially cuts the code size needed for developing an application UI by half. Vaadin still provides access to writing client-side UI in both Java and JavaScript, if more flexibility is needed. 
</blockquote> 
<p><strong> InfoQ: Developers using GWT complain that they have very few to almost no GWT books published recently. Given that background, how do you explain the importance of having the <a href="https://vaadin.com/book">Book of Vaadin</a>? And what are your plans to maintain or enhance its current Preview Edition? </strong></p> 
<blockquote>
  We have been maintaining the Book of Vaadin since 2007. This has been a huge task, but we feel that top notch documentation is a very important part of any framework - if a feature is not documented, it is not useful for anyone. 
 <br /> 
 <br /> The first full edition of the Book of Vaadin should be ready by early March as a free download for everyone. After that we'll continue to maintain it every time we add new features to the framework. 
</blockquote> 
<p><strong> InfoQ: If the Vaadin development team is distributing a version of GWT which they are maintaining for Vaadin, how are they planning to keep this in-line with standard GWT? </strong></p> 
<blockquote>
  The sources for the GWT version that we maintain are available at https://github.com/vaadin/gwt. 
 <br /> 
 <br /> All of Vaadin framework is also available at https://github.com/vaadin/vaadin. 
 <br /> 
 <br /> We only distribute releases for the Vaadin Framework (not for GWT), but since Vaadin includes GWT, it can be used as a drop-in replacement for GWT distribution - even if only client-side features of the framework would be used. 
 <br /> 
 <br /> If you want to take a peek into GWT and Vaadin relationship from an architecture point of view, see https://vaadin.com/blog/-/blogs/vaadin-7-application-architecture. 
</blockquote> 
<p><strong> InfoQ: The <a href="https://vaadin.com/faq">FAQ</a> section on your web site includes a paragraph on “When should I not use Vaadin?” How does the size of an enterprise project influence the decision on adopting Vaadin? </strong></p> 
<blockquote>
  Sometimes it does: Larger the project, more the benefits for the Vaadin developers. Building a very small application should be easy with almost any framework - including Vaadin. 
</blockquote> 
<p><strong> InfoQ: The page &quot;<a href="https://vaadin.com/who-is-using-vaadin">Who Is Using Vaadin</a>&quot; shows Finland hosting 34 showcases. USA that hosts six showcases is the next one on the list. What is a Vaadin showcase? Developers in 170 countries use Vaadin, so what will it take to increase the number of Vaadin showcases hosted in those countries? </strong></p> 
<blockquote>
  Unfortunately our showcase map is very incomplete. When we started collecting the &quot;who is using Vaadin&quot; list, we just asked around to find about cases using Vaadin. Our headquarters are in Finland, so we heard of quite a few nice showcases from our local networks. 
 <br /> 
 <br /> We would love to list showcases from all around the world. Anyone who has built something nice with Vaadin is encouraged to contact us for including them in our listing. 
</blockquote> 
<p><strong> InfoQ: Do any non-JVM web application frameworks present competition to Vaadin? If yes, can you name them? </strong></p> 
<blockquote>
  While we are very JVM centric, everyone building a web app in this space is also using the web platform. Thus the most competition is from JavaScript frameworks. While having separate front-end and back-end teams with different skills could be ok for some projects, the extra cost of this split should be unnecessary for the most projects in the enterprise space. 
</blockquote> 
<p><strong> InfoQ: A professional developer may want to contribute to the Vaadin's codebase. What process do your team members follow for qualifying a potential contributor? </strong></p> 
<blockquote>
  Most of the contributions to the Vaadin project come in the form of add-on components. This sets the bar low - anyone can contribute to the Vaadin directory at http://vaadin.com/directory. 
 <br /> 
 <br /> When one wants to contribute to the core Vaadin Framework, they should submit their patch though the issue tracking system: http://dev.vaadin.com/wiki/SubmittingBug. One of the core development team members then picks up the patch, evaluates and tests it, and then submits it to our internal Gerrit review system where it is read and evaluated by at least one other developer from our core team. At the minimum, the patch often gets partially re-written during the process. All contributors are also required to sign a contribution agreement. 
 <br /> 
 <br /> We are looking forward to making this process simpler by making our Gerrit system public and starting to accept pull requests from GitHub in the future. 
</blockquote> 
<p><strong> InfoQ: We learn from your roadmap <a href="https://vaadin.com/blog/-/blogs/roadmap-for-the-next-74-days">blog post</a> that the Vaadin framework intends to follow a steady development process. Is the future process formalized? What does it look like? </strong></p> 
<blockquote>
  We renewed our process recently - partly because of the delays in the Vaadin 7 project. We try to do more informal research projects on the side while continuing with the actual development. We hope that this allows us to make better estimates for the roadmap. The core process includes a monthly roadmap meeting where we set roadmaps for all products for the next three months. This internal process as a whole looks like below: 
 <br /> 
 <br /> 
 <div style="text-align: center;">
  <img src="/resource/news/2013/02/vaadin-7/en/resources/Vaadins_Development_and_Release_Process.jpg;jsessionid=C072A8D6D496F296C51DC46230B942C3" border="0" alt="Vaadin's Development and Release Process" _href="img://Vaadins_Development_and_Release_Process.jpg" _p="true" />
 </div> 
 <div style="text-align: center; font-weight: bold;">
  Figure: Vaadin's Development and Release Process
 </div> 
 <br /> The development itself follows one or two weeks-long cycles, depending on the product feature. When we are getting closer to having something we could show to outside world, we do an internal development review; and if possible, we release an alpha or beta version to get feedback earlier on in the development process. 
</blockquote> 
<p id="lastElm"></p>
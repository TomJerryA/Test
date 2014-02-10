<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Salesforce.com Woos Windows Developers with New Toolkits for .NET</h3><p>Salesforce.com is attempting to make it easier for .NET developers to consume its web services thanks to a new pair of open-source Toolkits. These Toolkits target the Force.com REST API and Chatter API and are the brainchild of Salesforce Platform Advocate Wade Wegner who talked to InfoQ about the goals and logistics of building these components.</p>
<p>The Salesforce.com platform has over 1.4 million developers and provides a broad API available through <a href="http://www.salesforce.com/us/developer/docs/api/index_Left.htm#CSHID=sforce_api_quickstart_intro.htm|StartTopic=Content%2Fsforce_api_quickstart_intro.htm|SkinName=webhelp" target="_blank">SOAP</a> and <a href="http://www.salesforce.com/us/developer/docs/api_rest/index_Left.htm#CSHID=intro_what_is_rest_api.htm|StartTopic=Content%2Fintro_what_is_rest_api.htm|SkinName=webhelp" target="_blank">REST</a> endpoints. The company offers simpler API access via SDKs for <a href="https://github.com/developerforce/Force.com-JavaScript-REST-Toolkit" target="_blank">JavaScript</a>, <a href="http://wiki.developerforce.com/page/PHP_Toolkit" target="_blank">PHP</a>, and <a href="http://wiki.developerforce.com/page/Mobile_SDK" target="_blank">mobile</a> (iOS and Android) developers. While the company maintains a dedicated <a href="http://events.developerforce.com/en/pages/force-dot-com-dot-net" target="_blank">resource site for .NET developers</a>, those developers have had no libraries to accelerate development. Until now. The new <a href="https://github.com/developerforce/Force.com-Toolkit-for-NET" target="_blank">Force.com&nbsp; Toolkits for .NET</a> – with source code and samples hosted on GitHub – includes native libraries that run on multiple Microsoft platforms including Windows 8, Windows Phone 8, and Silverlight 5.</p>
<p>InfoQ reached out to Wegner to learn more about this Toolkit and what it takes to build and distribute an SDK to developers.</p>
<p><strong>InfoQ: You’ve just released a set of toolkits for .NET developers. What exactly do these toolkits provide and how do you get them?</strong></p>
<blockquote> 
 <p><strong>Wegner</strong>: The Salesforce1 platform provides powerful developer APIs that makes building applications simple, powerful, and secure. To provide a great experience for .NET developers we havereleased to open source the <strong>Force.com Toolkit for .NET</strong> and the <strong>Chatter Toolkit for .NET</strong>.&nbsp; With these toolkits it is now incredibly easy for .NET developers to use these APIs using the skills and tools they are already familiar using today. By simply consuming these resources through published NuGet packages, .NET developers can easily build new applications powered by the Salesforce1 platform and add Salesforce1 platform capabilities into existing applications.</p> 
 <p>The toolkits are comprised of the following resources:</p> 
 <ul> 
  <li>A set of native libraries for the Microsoft .NET Framework.</li> 
  <li>NuGet packages for easy deployment and versioning.</li> 
  <li>Sample applications to get you started.</li> 
 </ul> 
 <p>You can find all the source code in Github:</p> 
 <p style="padding-left: 20px"><a href="https://github.com/developerforce/Force.com-Toolkit-for-NET">https://github.com/developerforce/Force.com-Toolkit-for-NET</a></p> 
 <p style="padding-left: 20px"><a href="https://github.com/developerforce/Chatter-Toolkit-for-NET">https://github.com/developerforce/Chatter-Toolkit-for-NET</a></p> 
 <p style="padding-left: 20px"><a href="https://github.com/developerforce/Common-Libraries-for-NET">https://github.com/developerforce/Common-Libraries-for-NET</a></p> 
 <p>The NuGet packages are published here:</p> 
 <p style="padding-left: 20px"><a href="http://www.nuget.org/packages/DeveloperForce.Force/">http://www.nuget.org/packages/DeveloperForce.Force/</a></p> 
 <p style="padding-left: 20px"><a href="http://www.nuget.org/packages/DeveloperForce.Chatter/">http://www.nuget.org/packages/DeveloperForce.Chatter/</a></p> 
 <p style="padding-left: 20px"><a href="http://www.nuget.org/packages/DeveloperForce.Common/">http://www.nuget.org/packages/DeveloperForce.Common/</a></p> 
</blockquote>
<p><strong>InfoQ: Microsoft and Salesforce aren't known to have the coziest relationship. What demand did you see that led to this toolkit?</strong></p>
<blockquote> 
 <p><strong>Wegner</strong>: We have a lot of joint customers, and our number one priority is making them all successful. Based on our development survey data we know that .NET developers are one of the largest constituents of our developer ecosystem. By making .NET developers more productive and able to connect to customer information and systems in Salesforce1, we believe we can help them deliver value to their business and their customers faster.</p> 
</blockquote>
<p><strong>InfoQ: What were your guiding principles when designing this toolkit, and what should any developer think about when preparing a resource like this?</strong></p>
<blockquote> 
 <p><strong>Wegner</strong>: There were a few key design principles we followed when designing and building these toolkits.</p> 
 <ul> 
  <li>Provide support for as many modern Microsoft platforms as possible with the same core library. To accomplish this, the toolkits makes use of <a href="http://msdn.microsoft.com/en-us/library/gg597391.aspx">Portable Class Libraries</a> to enable use on the following platforms: Windows 7 (.NET 4, .NET 4.5), Windows 8, Windows Phone 8, and Silverlight 5.</li> 
  <li>Avoid performance bottlenecks and application blocking. To accomplish this, the toolkits make use of the <a href="http://msdn.microsoft.com/en-us/library/hh191443.aspx">Async and Await</a> pattern for asynchronous programming.</li> 
  <li>Allow developers to take advantage of <a href="http://msdn.microsoft.com/en-us/library/ee461504.aspx">dynamic objects</a> so that they don’t necessarily have to create classes to represent every Salesforce1 object.</li> 
  <li>Provide the support for key operations and enable the community participate in active development of the toolkits. You will see that our <a href="https://github.com/developerforce/Force.com-Toolkit-for-NET/blob/master/README.md#contributing-to-the-repository">policy for contributions</a> is extremely permissive – we want you to participate!</li> 
  <li>Use NuGet packages as the primary delivery mechanism while allowing access to the underlying source code. Furthermore, give developer’s access to the <a href="https://github.com/developerforce/Force.com-Toolkit-for-NET/blob/master/README.md#devtest-packages">latest development/test packages</a>.</li> 
 </ul> 
 <p>When building your own resources for developers I encourage you to think about these principles.</p> 
 <p>We feel these principles have set us up for success. Already we’ve seen many code contributions from the community through Github pull requests, significant usage of the NuGet packages, and lots of excitement through blog posts and apps built.</p> 
</blockquote>
<p><strong>InfoQ: Explain to us the pipeline you created from source control all the way to distribution of the toolkit.</strong></p>
<blockquote> 
 <p><strong>Wegner</strong>: I’m glad you asked. I’m pleased with how we’ve put all this together. It all starts with our repositories on Github. We have three:</p> 
 <p style="padding-left: 20px"><a href="https://github.com/developerforce/Force.com-Toolkit-for-NET">https://github.com/developerforce/Force.com-Toolkit-for-NET</a></p> 
 <p style="padding-left: 20px"><a href="https://github.com/developerforce/Chatter-Toolkit-for-NET">https://github.com/developerforce/Chatter-Toolkit-for-NET</a></p> 
 <p style="padding-left: 20px"><a href="https://github.com/developerforce/Common-Libraries-for-NET">https://github.com/developerforce/Common-Libraries-for-NET</a></p> 
 <p>For each repository we use the <a href="https://help.github.com/articles/using-pull-requests#fork--pull">Fork &amp; Pull</a> development model. This makes it very easy for us to collaborate - both internally and externally - on the toolkits.</p> 
 <p>In each of the repositories you’ll see a similar folder structure:</p> 
 <p style="font-family: courier">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /nugets</p> 
 <p style="font-family: courier">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /samples</p> 
 <p style="font-family: courier">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /src</p> 
 <p style="font-family: courier">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /&lt;ProjectName&gt;</p> 
 <p style="font-family: courier">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /&lt;ProjectName&gt;.FunctionalTests</p> 
 <p style="font-family: courier">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; /&lt;ProjectName&gt;.UnitTests</p> 
 <p>The <span style="font-family: courier">/nugets</span> folder includes all the files used to create our published NuGet packages. We can easily run <span style="font-family: courier">package.bat &lt;version&gt;</span> to create a NuGet package based on the Nuspec file and then publish directly to NuGet Gallery. Relationships are maintained between the various projects by including references to the published NuGet packages. This makes it easy for developers to manage the dependencies and versions, even after they’ve started using them within their own projects.</p> 
 <p>The <span style="font-family: courier">/samples</span> folder includes sample applications for the respective toolkit. You’ll find samples for Windows Phone 8, Windows 8. and traditional .NET 4 and 4.5 applications.</p> 
 <p>The <span style="font-family: courier">/src</span> folder contains all the source for the toolkits, including functional tests and unit tests. The functional tests are tests that communicate to the Salesforce1 APIs directly and ensure our code is healthy. The unit tests are test that largely mock the various HTTP calls and ensure we’re creating our requests and handling responses appropriately.</p> 
 <p>Anytime we make a commit to the repository it kicks off a build on our TeamCity build server we run in the cloud. We have a set of “Debug CI Build” templates that the following build tasks:</p> 
 <ol> 
  <li>Check and make sure the solutions compile. This includes that sample applications.</li> 
  <li>Run all of our functional tests using a real Salesforce1 Developer Edition organization.</li> 
  <li>Run all of our unit tests.</li> 
  <li>Create and publish a “latest development version” NuGet build to our build server, which also functions as a private NuGet gallery.</li> 
 </ol> 
 <p>All this is done to help us ensure we never break the toolkits. If anything fails two things occur: 1) emails are sent to repository admins, and 2) the little graphic in our repository README.md file turns from green to red.</p> 
 <p>These steps have made it very easy for us to continue to evolve and enhance the toolkits - especially when accepting pull requests from members of the developer community!</p> 
</blockquote>
<p><strong>InfoQ: Now that you've completed this initial release, what advice do you have for others when choosing how to build/license/deploy a toolkit like this?</strong></p>
<blockquote> 
 <p><strong>Wegner</strong>: The #1 piece of advice I can give is to find a great group of people to support and provide feedback throughout the process. I was lucky to pull together a great group of experts in the .NET and Salesforce1 platform communities, and regularly sought out their advice.</p> 
</blockquote><br><br><br><br><br><br></body></html>
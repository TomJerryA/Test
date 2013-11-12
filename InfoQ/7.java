<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>What’s the Problem with Mobile HTML5?</h3><p>A recent research concludes that contrary to the general belief performance is not the main problem with HTML5 but rather the missing of profiling and debugging tools and the lack of certain APIs.</p>
<p>After surveying over 6,000 developers worldwide, analyzing 30,000+ Android Play apps, reviewing 42 HTML5 frameworks and tools, and interviewing 32 top experts on the subject of mobile HTML5 vs. native, VisionMobile has come to a number of conclusions published in the <a href="http://www.developereconomics.com/downloads/can-html5-compete-native/">How can HTML5 compete with Native?</a> research report, the most significant findings being covered in this article. The report distinguishes four main routes to market used for HTML5 applications:</p>
<ol> 
 <li>Mobile Browser – web apps or websites tailored for mobile devices and running in a mobile browser</li> 
 <li>Native Wrapper – web apps packaged in a native wrapper and delivered through an app store</li> 
 <li>Web-to-native Converter – apps written in JavaScript and compiled to native code</li> 
 <li>Native JavaScript API – HTML5 apps written for platforms natively supporting it, such as Firefox OS, Windows 8, Chrome OS</li> 
</ol>
<p>The key findings of the report are:</p>
<ul> 
 <li>61% of the developers write for the mobile browser</li> 
 <li>63% of the US Android Play applications <em>cannot</em> be written in HTML5 for the mobile browser because some APIs are not implemented by the browsers yet</li> 
 <li>the 37% of US Android apps that could be implemented in HTML5 would become 58% if the browsers would add support for Power Management and WiFi APIs</li> 
 <li>39% of the developers create HTML5 apps for the other 3 routes to market beside the mobile browser</li> 
 <li>49% of the US Android apps could be implemented with native wrappers, 63% with web-to-native converters, and 98% with native JavaScript</li> 
</ul>
<p>The following chart shows what makes HTML5 attractive:</p>
<blockquote> 
 <p><a href="/resource/news/2013/11/mobile-html5/en/resources/html5-native-1.png" target="_blank"><img title="image" style="border: 0px currentcolor; border-image: none; display: inline; background-image: none;" alt="image" src="http://www.infoq.com/resource/news/2013/11/mobile-html5/en/resources/html5-native-1.png" border="0" _href="img://html5-native-1.png" _p="true" /></a></p> 
</blockquote>
<p>What developers complain about HTML5 is shown in the next chart:</p>
<blockquote> 
 <p><a href="/resource/news/2013/11/mobile-html5/en/resources/html5-native-2.png" target="_blank"><img title="image" style="border: 0px currentcolor; border-image: none; display: inline; background-image: none;" alt="image" src="http://www.infoq.com/resource/news/2013/11/mobile-html5/en/resources/html5-native-2.png" border="0" _href="img://html5-native-2.png" _p="true" /></a></p> 
</blockquote>
<p>Many developers consider performance as HTML5’s main problem, but interviewing a number experts in the field the authors of the report consider it as a false target because performance is automatically improving by new generations of hardware, better JavaScript compilers, the option of using Asm.js, etc.. The main culprit in their opinion has to do with politics, more exactly the fact that the major browser vendors are also mobile OS vendors, interested in channeling applications through their respective app stores. Google encourages native Chrome apps, Apple seems to be implementing the latest HTML5 standards but “leaves out performance related APIs, e.g. WebGL.” Also, according to the report, one of the HTML5 myths is that development is easy, but actually development is pretty hard because of missing adequate debugging and profiling tools.</p>
<p>The most used APIs by US Google Play apps are:</p>
<blockquote> 
 <p><a href="/resource/news/2013/11/mobile-html5/en/resources/html5-native-3.png" target="_blank"><img title="image" style="border: 0px currentcolor; border-image: none; display: inline; background-image: none;" alt="image" src="http://www.infoq.com/resource/news/2013/11/mobile-html5/en/resources/html5-native-3.png" border="0" _href="img://html5-native-3.png" _p="true" /></a></p> 
</blockquote>
<p>The current HTML5 APIs standardization status and browser adoption is depicted in the following graphic:</p>
<blockquote> 
 <p><a href="/resource/news/2013/11/mobile-html5/en/resources/html5-native-4.png" target="_blank"><img title="image" style="border: 0px currentcolor; border-image: none; display: inline; background-image: none;" alt="image" src="http://www.infoq.com/resource/news/2013/11/mobile-html5/en/resources/html5-native-4.png" border="0" _href="img://html5-native-4.png" _p="true" /></a></p> 
</blockquote>
<p>The next table indicates the APIs that would make the most difference if implemented for their respective route to market, showing how many more apps could be implemented in HTML5 if that happens:</p>
<table width="500" border="1" cellspacing="0" cellpadding="2"> 
 <tbody> 
  <tr> 
   <td width="166" valign="top"> <p style="margin-right: 0px;" dir="ltr">Route to market</p> </td> 
   <td width="166" valign="top">API</td> 
   <td width="166" valign="top">% of apps</td> 
  </tr> 
  <tr> 
   <td width="166" valign="top">Mobile Browser</td> 
   <td width="166" valign="top">Power management</td> 
   <td width="166" valign="top">13%</td> 
  </tr> 
  <tr> 
   <td width="166" valign="top">Native Wrapper</td> 
   <td width="166" valign="top">Power management</td> 
   <td width="166" valign="top">12%</td> 
  </tr> 
  <tr> 
   <td width="166" valign="top">Web-to-native Converter</td> 
   <td width="166" valign="top">WiFi</td> 
   <td width="166" valign="top">21%</td> 
  </tr> 
  <tr> 
   <td width="166" valign="top">Native JavaScript API</td> 
   <td width="166" valign="top">Calendar</td> 
   <td width="166" valign="top"> <p>1.4%</p> </td> 
  </tr> 
 </tbody> 
</table>
<p>The report concludes with a number of observations and recommendations for the HTML5 space:</p>
<ul> 
 <li>Browsers should implement more HTML5 APIs starting with Power Management and WiFi. Developers should push browser vendors to implement more APIs.</li> 
 <li>A standardized packaging solution should be developed for native JavaScript apps, allowing such applications to be packaged once and deployed on any supporting platform</li> 
 <li>A device identity API should be developed to alleviate the fears related to cookies and privacy concerns</li> 
 <li>Developers should be better educated regarding the possibilities offered by HTML5, the real advantages and drawbacks</li> 
 <li>A Debug API should be developed to enable the creation of a set of debugging tools</li> 
</ul><br><br><br><br><br><br></body></html>
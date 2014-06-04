<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Java Currency and Money Standard Forges Ahead</h3><p>The Java standard for Currency and Money (JSR 354) currently under development reached another important milestone this May with the publication of a second Public Review draft.</p>
<p>InfoQ spoke to Anatole Tresch (Credit Suisse) who is leading the standardisation effort.</p>
<p><strong>InfoQ: What's driving the standard? What problems are you solving for developers?</strong></p>
<blockquote> 
 <p><strong>Anatole:</strong> Most developers will sooner or later come into contact with monetary data types. Monetary aspects are not well covered. This was the starting point for Credit Suisse to file a JSR to enable:</p> 
 <ul> 
  <li>more flexible management of currencies in a system</li> 
  <li>an abstraction for monetary amounts, including basic arithmetic functions improved formatting capabilities for amounts</li> 
  <li>support for custom currency schemes and virtual currencies</li> 
  <li>support for higher level operations such as currency conversion and finance mathematics</li> 
 </ul> 
</blockquote>
<p><strong>InfoQ: Why isn't the problem solved by the existing java.util.Currency class?</strong></p>
<blockquote> 
 <p><strong>Anatole:</strong> The current Currency class has several limitations. For example it is based very strictly on the ISO standard (ISO-4217). Whilst we don't think ISO-4217 is bad per se, it does not cover some aspects that we think will be important in the long-term.&nbsp;There are many currencies that are not defined (e.g. historic currencies) or not in scope&nbsp;(virtual, social media, video game currencies) - and so many companies have built their own custom currency schemes to work around these restrictions.</p> 
 <p>Another problem is that there is no model for monetary amounts. You can choose from the various numeric types in Java, but you have to actively manage the corresponding currency amount explicitly in your code.</p> 
 <p>The new abstractions we're introducing allow developers to model currencies and monetary amounts in a flexible, interoperable and secure way. Our model also explicitly supports different implementation types for amounts, which enables framework developers to cover different usage scenarios based on a unified model.</p> 
</blockquote>
<p><strong>InfoQ: This is the second public review in just over eight months - very quick by JSR standards. What factors do you think are helping you to achieve your current velocity?</strong></p>
<blockquote> 
 <p><strong>Anatole:</strong> I think it is due to a combination of things - my employer Credit Suisse has to be given credit, as they give me a lot of time and freedom for driving this forward.</p> 
 <p>Another key piece is that when something is proving difficult to sort out I simply try model it as Java code because at the end of the day &quot;the truth is in the code&quot;. This is sometimes hard, but if you ask the right questions, you also get back the right answers.</p> 
 <p>This does not mean at all that everything worked fine all the time. We had some tough discussions in and outside the standard's Expert Group (EG) - but sometimes you just have to make a decision and move on.</p> 
 <p>Another useful trick I've found is to slice the problem area into pieces, so you can discuss more effectively on the smaller aspects. At the beginning of the JSR I noted the main topic areas - the things I wanted to discuss the most and I was able to be stick on that reasonably effectively, especially in the first year of the JSR.</p> 
</blockquote>
<p><strong>InfoQ: What's left to do? Are there still opportunities for interested community developers to get involved?</strong></p>
<blockquote> 
 <p><strong>Anatole:</strong> The Testing Kit (TCK) needs some more attention. It is not yet in its final delivery state as a truly independent execution artifact. The currency roundings could use extra help. In particular, if someone has good skills in optimization and numeric representations, the FastMoney class is awaiting a volunteer to make it as fast as possible. Similarly, if someone wanted to help with a Java ME compatible version, they would be very welcome.</p> 
 <p>I would also like to specifically mention Stephen Colebourne, who is an EG member and founder of the JodaMoney library. I am sure he'd appreciate help and pull requests for his numerous efforts in this area.</p> 
</blockquote>
<p><strong>InfoQ: Where can developers go to find out more - or to try out the developing standard?</strong></p>
<blockquote> 
 <p><strong>Anatole: </strong>The starting page is:&nbsp;<a href="http://javamoney.org/" target="_blank">http://javamoney.org</a>. The pages there should link to all parts of our initiative.</p> 
</blockquote>
<p><strong>InfoQ: </strong>When do you think the final standard will come out? Are you intending to be a part of Java SE9?</p>
<blockquote> 
 <p><strong>Anatole: </strong>We wanted from the start to include the functionality into the Java platform. However, quite quickly it became clear that we would miss the train for Java 8. The Java 9 timeframe seemed a long way out, so we switched to a pure standalone focus. We would certainly like to be part of a platform release. But right&nbsp;now, we're focused on delivering a good spec for users - and try to be included in Java 9 nearer the release.</p> 
</blockquote>
<p><strong>InfoQ: I understand that this is the first Java standard for which you've been the spec lead. How has the process been?</strong></p>
<blockquote> 
 <p><strong>Anatole:</strong> Early on in the JSR there were some points that were very challenging, such as support for Java Mobile Edition (Java ME) and Java 8. As time passed, things became clearer and I think we are now on track to &nbsp;become final around end of this year. I think some more engagement early on (especially from Oracle) would have helped to solve some conflicts earlier.</p> 
</blockquote>
<p><strong>InfoQ: What advice would you give to other Java developers who want to get involved in the standards process?</strong></p>
<blockquote> 
 <p><strong>Anatole:</strong> For developers that want to get involved, I would like to encourage everyone. If you have a local JUG or regular hacking events, then please support them. We should also mention our friends at the Adopt-a-JSR (<a href="http://adoptajsr.org/" target="_blank">adoptajsr.org</a>) and Adopt-OpenJDK initiatives, who have also been supportive - please contact them if you're interested in standards work - there's always plenty to do.</p> 
</blockquote><br><br><br><br><br><br></body></html>
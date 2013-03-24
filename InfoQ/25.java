<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Has Web Style Worked?</h3><p>In a <a href="http://www.ebpml.org/blog2/index.php/2013/03/20/the-end-of-the-web">recent posting</a>, Jean-Jacques Dubray (JJ) reminds us that it is almost 7 years since <a href="http://www.tbray.org/ongoing/When/200x/2006/04/17/SOA-or-not">Tim Bray predicated the end of SOA</a>:</p> 
<blockquote>
  I did an interview and a podcast [...] and the question came up in both, and in the hallway talk too: “What do you think we should do about SOA?” Which weirdly, nobody had asked me before, and I could find only one answer: “Don’t do anything. ‘SOA’ may have meant something once but it’s just vendor bullshit now.”
</blockquote> 
<p>Tim ended by stating (predicting) that rather than SOA being the future, <a href="http://www.tbray.org/ongoing/When/200x/2006/03/26/On-REST">Web Style</a> was the future. As JJ mentions, that predicting opened the doors for many others to follow over the coming years, including the likes of <a href="http://www.infoq.com/news/2009/01/is-soa-dead;jsessionid=EE2526A3D2BB93D3F1211CB00C60897F">Anne-Thomas Manes</a> and <a href="http://www.infoq.com/news/2007/11/soa-long;jsessionid=EE2526A3D2BB93D3F1211CB00C60897F">others</a>. One of the results was that many SOA projects were slowed or killed, with JJ having his own direct experience of the former:</p> 
<blockquote>
 My manager at the time told me that Tim Bray's post was circulating in our IT department and he didn't know where to start to craft an answer to his management. His team had built their own ESB at a time when hardly anyone had heard of XML and several years of hard work and constantly rising transaction volumes (a respectable 10 M requests/day at the time, in early 2007) &nbsp;were now jeopardized by a single paragraph written by Tim Bray.
</blockquote> 
<p>Well JJ has spent some <a href="http://www.infoq.com/articles/RESTSOAFuture/;jsessionid=EE2526A3D2BB93D3F1211CB00C60897F">considerable time</a> over <a href="http://www.infoq.com/articles/rest-soap;jsessionid=EE2526A3D2BB93D3F1211CB00C60897F">the years</a> on InfoQ and elsewhere, talking about <a href="http://www.infoq.com/news/2011/06/RestAPIs;jsessionid=EE2526A3D2BB93D3F1211CB00C60897F">the problems</a> that <a href="http://www.infoq.com/news/2011/06/trouble-with-apis;jsessionid=EE2526A3D2BB93D3F1211CB00C60897F">Web Style overlooks</a>. In this recent article, he has also been taking a look at many of the services that purport to implement Web Style:</p> 
<blockquote>
 Out of 9000 APIs [in the Programmable Web's directory], my best estimate is that less than 1% are following Tim Bray's&nbsp;
 <a href="http://en.wikipedia.org/wiki/Representational_state_transfer">Web Style</a>. They are all but following an &quot;API&quot; style, short of RPC.
</blockquote> 
<p>And JJ gives some examples of what he means by this by considering what he believes is a representative sample:</p> 
<blockquote> 
 <ul> 
  <li><span style="font-size: 13px; line-height: 19px;"><strong>Ask Ziggy</strong> which offers the ability (sic) </span><a href="http://www.ask-ziggy.com/walkthrough.html#sample" style="font-size: 13px; line-height: 19px;">&nbsp;to define &quot;actions&quot;</a><span style="font-size: 13px; line-height: 19px;"> (such as Play, NextSong, Previous Song, Shuffle...)</span></li> 
  <li><span style="font-size: 13px; line-height: 19px;"><strong>WhatLanguage</strong> explains that <a href="http://www.whatlanguage.net/en/api/language_identification_documentation#detect_text">you can use, as you wish</a>, a GET (if your request is less than 7500 chars) or a POST to the same URI to detect the language of a given string</span></li> 
  <li><span style="font-size: 13px; line-height: 19px;"><strong>Do.com</strong> actually seem to be offering a <a href="https://developers.do.com/docs/tasks">Web Style API</a>, but it does not do much, it is simply CRUDing 5 resources (tasks, project, users,...)</span></li> 
  <li><span style="font-size: 13px; line-height: 19px;"><strong>SkyBuffer</strong> is also following <a href="https://dev.skybuffer.com/version/1">the Web Style</a>, but just like DO.com, this is just some CRUD on a couple of entities</span></li> 
  <li><span style="font-size: 13px; line-height: 19px;"><strong>MaShape</strong> which is a &quot;Cloud API hub&quot; is very interesting because they offer a better way for developers to consumer APIs. <a href="https://www.mashape.com/docs/gettingstarted/overview">How do they do that</a>? They invite developers to &quot;<span>Learn how to describe your API on Mashape to autogenerate client libraries and documentation&quot;. Yes you heard right, after years of bashing, developers start talking about client library code generation.</span></span></li> 
 </ul> 
</blockquote> 
<p>&nbsp;JJ thinks that the API approach is at odds with the pure Web Style that was being pushed by Tim et al:</p> 
<blockquote>
 Wasn't the Web Style all about the &quot;Uniform Interface&quot;, Bookmarks and auto-magic 
 <a href="http://www.infoq.com/articles/hypermedia-api-tutorial-part-one;jsessionid=EE2526A3D2BB93D3F1211CB00C60897F">HATEAOS</a>? not to forget standard IANA types? Yes, you don't hear that kind of argument much these days. APIs rule. People are no longer ashamed to use a verb in their URLs or POST a (complex) query. Most importantly, 
 <a href="http://docs.mongodb.org/manual/reference/javascript/">MongoDB showed us</a> that there is a lot more needed to CRUD than these 4 little verbs and an anemic URL syntax. Developers and Architects are so desperate to go around the &quot;Web Style&quot; that 
 <a href="http://www.infoq.com/presentations/OpenStack-Extensions;jsessionid=EE2526A3D2BB93D3F1211CB00C60897F">they even try to add namespaces to JSON</a>.
</blockquote> 
<p>When looking at these supposedly Web Style services, JJ comes to the conclusion that it has in fact failed to deliver on the hype and is in fact &quot;dead&quot;. However, JJ goes even further than this, declaring the Web itself to be all but dead:</p> 
<blockquote>
 [...] between 
 <a href="http://www.itwriting.com/blog/7249-native-apps-vs-html-5-no-consensus-over-how-to-choose.html">developers who can't figure out how to produce anything of value with HTML5</a> and compete with Native apps and end users finally getting cold at the wonderful idea of being &quot;the product&quot; central to the Web business model.&nbsp;
 <a href="http://www.ebpml.org/blog2/index.php/2010/11/21/soon-the-web-will-die">Tim Berner-Lee which is coming out every six month</a> with a &quot;Long live the Web&quot; message but after 
 <a href="http://www.bbc.co.uk/news/world-asia-21855051">a wrath of security abuses</a>, it seems that even a KBE can no longer save the Web.
</blockquote> 
<p>Fortunately the article doesn't just leave us with a gloomy overview of the past and the &quot;technical debt&quot; that has wraught. JJ looks at where we are today and the influence of new waves such as mobile, which he believes represents possibly the biggest paradigm shift computing has ever seen:</p> 
<blockquote>
 Few people would remember, but software engineering was built on an old, very old paradigm of &quot;file processing&quot; which culminated with UFS. The desktop metaphor and the main usage patterns of PCs remained anchored in &quot;file processing&quot;. Mobile is no longer about files, mobile terminals assist us in pretty much any activity we do. If nothing else, future operating systems will be activity centric.
</blockquote> 
<p>However, he believes that we must also leave Web technologies behind in order to succeed:</p> 
<blockquote>
 The best user experience will win, anyone who has, is or will be betting against it will lose. The Web rose, because it too, once, provided a better user experience. It didn't rise because it was &quot;the Web&quot;. 
</blockquote> 
<p>And finally, JJ states that we have to be far more pragmatic about how we approach problems and really learn from the past:</p> 
<blockquote>
 More CRUD is not going to cut it, even with an API as superbly designed as the MongoDB API. We also have to grow up an understand that, OO is the wrong paradigm to represent interactions between distributed components. Hence we have to stop reifying everything we do into stateless singleton method calls. Annotations on a class are simply too weak to drive the semantic revolution that SOA started and we now need to finish.
</blockquote> 
<p>But even taking on board all of these changes that JJ suggests, what is the ultimate goal? Well JJ thinks it is a robust Composite Programming Model where the model and view are free from one another but still properly connected, following an activity/action/lifecycle paradigm. Unfortunately JJ doesn't go into a lot of detail in this article on that model, but perhaps the intent is to follow up with some related publications.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
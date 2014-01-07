<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Klaus Olsen Elaborates on Bug Hunting</h3><p>Following his talk at the Testing Portugal 2013 conference, InfoQ contacted Klaus Olsen of the <a href="http://www.tmmi.org/">TMMi</a> to get further details about the <a href="http://www.infoq.com/news/2013/12/testing-bug-hunting">bug hunting</a> technique.</p>
<p>InfoQ: Can you please explain some more about the origins of bug hunting?</p>
<blockquote> 
 <p>I read about it in James Whittaker’s book &quot;How to Break Software&quot; from 2003 where he on one page explained the set-up he used at Florida Institute of Technology. I was inspired by the description and made a workshop at a local Danish SIGIST (Special Interest Group for Software Testing back in 2003) to try the concept and I then presented the idea as a workshop at EuroSTAR 2003 in Amsterdam with success.</p> 
 <p>I have subsequently worked with several companies where we have used bug hunting and I have built upon these experience and later presented my result and experience at conferences in New Delhi, India, Sydney and Canberra in Australia and Praha and Helsinki as well as Lisbon in Europe.</p> 
</blockquote>
<p>InfoQ: When did you feel attracted by this technique and why?</p>
<blockquote> 
 <p>I felt attracted immediately because of the mix of applying test techniques to your testing, working in pairs which encourages knowledge sharing within both testing and domain areas, and on top of this you get team building all at the same time.</p> 
 <p>And the big benefit: you get knowledge about the software under test, and most often the team will identify a list of defects within the software, which we can fix and by this improve the software once we have done some re-test of the defects to make sure the fix works correctly and regressions test of the software in general, to document the overall quality.</p> 
</blockquote>
<p>InfoQ: What are, in your opinion, the main advantages of using it?</p>
<blockquote> 
 <p>It is a very fast way to ensure the quality of any piece of software. If a well-planned bug hunt executed during two hours with 10 to 16 people doesn't find any defects or finds very few defects, depended on the size and complexity of the software we are testing, then my experience tells me that the quality of this software probably is above the average of the software I&acute;am usually involved in testing.</p> 
 <p>It works very well as an effective smoke test, when you receive software from another company and your company will plan and execute acceptance testing. Then a bug hunt prior to the acceptance test can work as a quality check ensuring to see if it's good enough for you to involve your business people to help execute test<ins cite="mailto:Microsoft%20account" datetime="2013-12-28T13:46"> </ins>cases during the acceptance testing.</p> 
 <p>If you find a large number of defects and high priority defects, you know you must postpone the acceptance test and get the quality improved before you involve your business people to help.</p> 
</blockquote>
<p>InfoQ: You referred to it as &quot;no silver bullet&quot; so, what techniques do you suggest to use along with bug hunting? Can you give some examples?</p>
<blockquote> 
 <p>Bug Hunting is built on exploratory testing which I think is a good method or approach to testing, but it has a weakness if you are building your test upon what you can see when running the software.</p> 
 <p>The problem exists if there are some requirements which have not been implemented in the software you are testing then you will probably not be able to identify these missing parts in a test where you only apply exploratory testing. For this reason you need to have some level of structural test planned with traceability between the requirements and test cases you plan and execute.</p> 
 <p>This will provide a better approach to ensure that all requirements will be covered during test.</p> 
</blockquote><br><br><br><br><br><br></body></html>
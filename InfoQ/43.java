<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Producer/Consumer Processing with TPL Dataflow</h3><p>In the simplest case, producer-consumer scenarios are quite easy to deal with. The producer pushes messages into a thread-safe queue and the consumer pulls them back out. A thread can be dedicated to each side of the equation and we’re done. At least until the complications arise.</p>
<p>These complications are many fold. Rather than one consumer you may have multiples that need to distribute or broadcast the message to. For performance reasons you may need to batch up requests before performing some operations. You may have multiple steps where the overhead of having a dedicated thread for each step is onerous. Or perhaps the context switching as the message jumps from thread to thread is impacting latency.</p>
<p>These are the kinds of issues that <a href="http://msdn.microsoft.com/en-us/library/hh228603(v=vs.110).aspx">TPL Dataflow</a> was designed to address. Rather than using threads, the lightweight blocks that make up a dataflow use and share thread pool threads as needed. But like any new framework, there is a lot to learn and many of the more advanced options can obscure the basics.</p>
<p><img alt="" src="http://www.infoq.com/resource/news/2014/01/Dataflow-PC/en/resources/diagram[1].png" _href="img://diagram[1].png" _p="true" /></p>
<p>To make it easier to get started, Dave Marini of Taskmatics has written an article titled <a href="http://taskmatics.com/blog/simplifying-producer-consumer-processing-with-tpl-dataflow-structures/">Going with the Flow: Simplifying Producer/Consumer Processing with TPL Dataflow Structures</a>. Using an order shipping workflow (shown above), Dave introduces the basic blocks that you’ll need for most scenarios.</p>
<ul> 
 <li>BufferBlock</li> 
 <li>BroadcastBlock</li> 
 <li>BatchBlock</li> 
 <li>TransformManyBlock</li> 
 <li>ActionBlock</li> 
</ul>
<p>The article also covers some of the more easily overlooked pitfalls such as flushing batches and completing workflows.</p><br><br><br><br><br><br></body></html>
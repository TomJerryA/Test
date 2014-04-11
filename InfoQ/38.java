<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Hydra Takes On Hadoop</h3><p>The social-networking company&nbsp;<a href="http://www.addthis.com/">AddThis</a>&nbsp;open-sourced&nbsp;<a href="http://projecthydra.org/">Hydra</a>&nbsp;under the Apache version 2.0 License in a recent&nbsp;<a href="https://www.addthis.com/blog/2014/01/23/hydra-is-now-open-source/#.UzB2cV7LEz0">announcement</a>. Hydra grew from an in-house platform created to process semi-structured social data as live streams and do efficient query processing on those data sets.</p>
<p>The Hadoop ecosystem has flourished but alternatives for Hadoop itself remain elusive. Even Doug Cutting the creator of Hadoop remarked recently that he expected to see multiple systems like Hadoop and lamented that there was none.</p>
<p>The Hydra framework comprises of four main components:</p>
<ul> 
 <li><b>Fedora</b> – a repository layer for persisting digital assets</li> 
 <li><b>Solr</b> – a search layer that stores indexes for text-based search to the assets</li> 
 <li><b>Backlight</b> – a Ruby on Rails plugin that provides faceted searching and browsing</li> 
 <li><b>Hydra Head</b> – A Ruby on Rails plugin that works in conjunction with Fedora for content management actions</li> 
</ul>
<p>Matt Abrams the CTO at AddThis who outlined the <a href="https://www.addthis.com/blog/2014/02/18/getting-started-with-hydra/#.Uz2JLK1dU54">Hello World</a> program for Hydra and Ian Barfield, engineer at AddThis spoke to InfoQ about comparisons between Hydra and Hadoop.</p>
<p><strong>InfoQ: Does Hydra provide a generic framework to express the solution to a problem via a paradigm similar to MapReduce? What are the key differences in the frameworks from a developer perspective?</strong></p>
<blockquote> 
 <p>The intuition behind Hydra is something like this, &quot;I have a lot of data, and there are a lot of things I could try to learn about it -- so many that I'm not even sure what I want to know.” It's about the curse of dimensionality -- more dimensions means exponentially more cost for exhaustive analysis. Hydra tries to make it easy to reduce the number of dimensions, or the cost of watching them (via probabilistic data structures), to just the right point where everything runs quickly but can still answer almost any question you think you might care about.</p> 
 <p>Hydra processing is similar to MapReduce, but it doesn't have quite as many restrictions. Job state is hard to manage but it gives a lot of performance and a lot of flexibility. We don't require data to be perfectly sorted (though you certainly can if you feel it necessary). Jobs almost never need to &quot;reprocess all data&quot;. Components (native Hydra ones anyway) don't need to think about network protocols to write files -- just the normal local filesystem.</p> 
 <p>The canonical word-count example in Hydra most directly translates to: write a split job that shards on keys and a tree job that creates the simplest of tree structures (a database of strings to hits).</p> 
 <p>Though Hydra is flexible. You don't have to make the split job. You could go straight to the tree and worry about sharding issues at query time (it frequently costs almost nothing to make this trade -- Hydra is all about good trades). This capability is a first-class feature -- not necessarily because it is hard to make or run the split job (although why waste the time or resources), but because you can only shard or sort on so many values (usually only one unless you are okay with tuples or your keys have a strict correlation).</p> 
</blockquote>
<p><strong>InfoQ: Does Hydra always emit trees as output? What is the reasoning behind this?</strong></p>
<blockquote> 
 <p>No, Hydra has a highly composable job system. It can write to log files for additional processing, or export to more exotic places like Kafka, Cassandra, or HDFS.</p> 
 <p>The higher-level components try to know as little about each other as possible. They mostly do their own thing and just happen to fit together. It is a leaky abstraction with a few shims to keep things harmonious, but it keeps things flexible.</p> 
 <p>For instance, there is nothing stopping you from replacing the text in a job config with Python code and changing the command to <i>exec python job.config</i> -- timer settings with still start/stop the Python process, local data will still be replicated, output will still be available on the cluster mesh, server failures will be recovered from, and so forth.</p> 
</blockquote>
<p><strong>InfoQ: What use case(s) is Hydra better suited for compared to Hadoop. When would Hadoop be a better choice?</strong></p>
<blockquote> 
 <p>Hydra is better at data exploration. You can follow a number of interesting leads from the results of a single, probably rather fast, map job. Queries on the resultant tree usually take on the order of seconds (or milliseconds).</p> 
 <p>Non-programmers can produce functioning products with a small amount of guidance. The web UI provides most everything that might be needed; it might be as simple as pressing clone on an existing job, changing the tree to use a couple different features and hitting go. In minutes they have a new URL endpoint to show your impressive new KPI on your company home page.</p> 
 <p>Hadoop has a few advantages though. It has stronger native support for very large, one-off joins. Technically speaking this just means more implicit sorting of files. Sorting huge numbers of things is expensive so we try pretty hard to avoid it, and as a result first order support for it is a little lacking. On the other hand, you might find that you don't really need the full, perfect join and are instead content with a Bloom-filter-based probabilistic hybrid -- in which case Hydra will once again save you some sweet cycles.</p> 
</blockquote>
<p><strong>InfoQ: Can Hadoop and Hydra be used together? Can you give some examples of where this might be a good idea?</strong></p>
<blockquote> 
 <p>Yes, Hydra jobs can read and write to HDFS. HDFS plays nice with a lot of other tools, formats, and services. You might have that one data scientist who is a whiz with drill queries or a product of low-mid priority that uses HDFS. Sometimes it is just easier to export certain subsets of data to let them do their thing than to try to teach them something else.</p> 
</blockquote>
<p><strong>InfoQ: What was the goal behind open-sourcing Hydra? Which companies are key contributors to Hydra?</strong></p>
<blockquote> 
 <p>Hydra has been under development at AddThis for over six years. It is something that we think is very powerful and differentiated in the distributed-data-processing product space. By open-sourcing Hydra, we hope to build a community of users and developers who can help us advance the product further.</p> 
 <p>We also feel that we owe a debt to the open-source community. AddThis as a company would not be feasible without the heavy use of open-source projects and open-sourcing Hydra is one way we are repaying this debt. There are a few companies that are using Hydra in production and making contributions back to the project but we are not at liberty to name them at this time.</p> 
</blockquote>
<p><strong>InfoQ: Finally, given everything today, is it reasonable to characterize Hydra as an alternative to Hadoop?</strong></p>
<blockquote> 
 <p>Certainly. There are probably quite a few people using Hadoop for things Hydra would be better suited for. It's not a simple change though, so I imagine you'd have to have the right intersection of data size and constraints for it to be worth it.</p> 
</blockquote>
<p>You can get more information on the <a href="http://projecthydra.org/">Hydra website</a> including a <a href="http://projecthydra.org/technical-2/getting-started/">getting started guide</a> and a <a href="http://projecthydra.org/technical-2/webinar-hydra-technical-deep-dive/">technical deep dive</a>.</p><br><br><br><br><br><br></body></html>
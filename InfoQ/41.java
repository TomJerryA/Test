<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>JCACHE Specification Finalized</h3><p>Oracle <a href="https://blogs.oracle.com/theaquarium/entry/jcache_is_final_i_repeat" target="_blank">announced this month</a> that the <a href="https://jcp.org/en/jsr/detail?id=107" target="_blank">JCACHE specification</a> is now final. JSR-107 was the oldest living on the books, and was initiated on March 6, 2001. After thirteen years of evolution and development, the &quot;Java Temporary Caching API&quot; will bring Java a common interface for interacting with caching systems.</p>
<p>Oracle had received <a href="https://blogs.oracle.com/reza/entry/java_ee_7_survey_results" target="_blank">high levels of interest</a> for JCACHE to be included in last year's Java EE 7 release, but after missing &quot;a few critical deadlines&quot;, <a href="https://blogs.oracle.com/theaquarium/entry/jcache_to_miss_java_ee" target="_blank">the JSR was dropped from the candidate list</a>. Following Oracle's recent <a href="https://java.net/downloads/javaee-spec/JavaEE8_Community_Survey_Results.pdf" target="_blank">Java EE 8 survey</a>, nearly two-thirds of all respondents expressed an interest in having JCACHE be included as part of the language's next Enterprise Edition. With the announcement of the specification's finalization, Oracle made note that the project's <a href="https://github.com/jsr107/RI" target="_blank">reference implementation</a> can be used as a drop-in to a Java EE 6 or Java EE 7 application, without having to wait for Java EE 8.</p>
<p>In itself, JCACHE provides a Map-like API for accessing caches, SPIs for spooling caches to persistent disk, an API for retrieving a named cache, and an API for registering event listeners. It does not, however, specify strategies for evictions, replication, or transactions. The work for defining those characteristics of caching is being done as part of <a href="https://jcp.org/en/jsr/detail?id=347" target="_blank">JSR-347 - JGRID</a>, to which JCACHE is a preceding and foundational component.</p>
<p>InfoQ caught up with Ben Cotton, who is a member of both the JSR-107 and JSR-347 expert groups, to ask some questions about JCACHE and the future of caching on the JVM:</p>
<p>InfoQ: Why JCACHE?</p>
<blockquote>
  JCACHE will do for the Java Caching community exactly what JDBC did for the Java RDBMS community. 
 <br />
 <br /> It promises to give Java a standard API with which JCACHE programmers can transparently operate on their data operands, independent of their data locality. With explicit join points to hibernate and JPA L2 views, It won't matter if the data operand is a column in a data base, or a Map.Entry
</blockquote>
<p>InfoQ: What do you have planned for the future?</p>
<blockquote>
  1. Transactions 
 <br /> 2. Interaction with JGRID (JSR-347). JCACHE is the &quot;tree&quot;. JGRID is the forest. 
 <br /> 3. Opening up transparent API join-points to ultra-premium Java locality libraries' data operands (ie. Peter's OpenHFT SHM) 
</blockquote>
<p>In addition to the open source reference implementation, the JSR-107 specification is freely available on the <a href="https://github.com/jsr107/jsr107spec" target="_blank">project's GitHub page</a>, including issue and commit history.</p><br><br><br><br><br><br></body></html>
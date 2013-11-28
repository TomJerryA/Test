<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>YourKit Released the 2013 Version of its Profilers</h3><p>For the recent 2013 version release of their Java Profiler, YourKit focused on improving its high level data collection features. The intention of the so called J2EE high level profiling is to get insight into the logical processing, rather than just providing timing information.</p>
<div>
 The data needed for high level profiling, like SQL statements, JNDI calls or JSP invocations, are gathered using so called probes. In previous versions, these probes were attached to and removed from the code by using byte code retransformation. This process created some load and required class retransformation, a feature which might be disabled on the used JVM.
</div>
<div>
 As of the 2013 version, probes are now always attached to the code, but the activation and deactivation are controlled by simple checks inside the probe code.
</div>
<div>
 Additionally to reduce overhead, this will cause changes to the probe state be effective immediately.
</div>
<div>
 There are 3 states for probes: 
 <em>on</em>, 
 <em>off</em> and 
 <em>auto</em>, where auto will activate probes when in CPU profiling mode.
</div>
<div>
 &nbsp;
</div>
<div>
 The main new feature, Performance Charts, is visualizing and correlating the data gathered by probes. It allows for example to correlate a high CPU load with the number of database calls, or the memory consumption with number of servlet calls. Those types of high level analysis are usually provided by APM tools and not present in profilers, which work on a much more detailed level. However, it gives a good starting point for seeing which parts of the system might interact with each other.
</div>
<div>
 &nbsp;
</div>
<div>
 CPU profiling received additions to configuration:
</div>
<ul> 
 <li>It is now possible to also instrument methods which are normally excluded, like getters and setters.</li> 
 <li>The UI can optionally display methods which are executing in less then a millisecond.&nbsp;</li> 
</ul>
<div>
 For memory profiling, there are also additions:
</div>
<ul> 
 <li>For simple objects like <em>Date</em>, or the primitive type wrappers, the corresponding value is displayed. This removes the need to drill into them to discover what value they carry, which speeds up analysis.</li> 
 <li>Self references in the are no longer expandable in the object tree, which prevents from accidentally drilling down reference paths which will indefinitely recurse.</li> 
</ul>
<div>
 Of course support for Java 8 has been extended to include default method profiling, and newer versions of all IDEs are supported for integration. Executing tests with TestNG can now also be profiled easier.
</div>
<div>
 &nbsp;
</div>
<div>
 YourKit is starting at $499 per developer, or $2,499 per floating license. Upgrading is free if the purchase was less than a year ago, otherwise it enables to use a 40% discount.&nbsp;
</div><br><br><br><br><br><br></body></html>
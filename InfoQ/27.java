<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Continuous Security Testing With Gauntlt</h3><p>James Wickett, from <a href="http://gauntlt.org/">Gauntlt</a> core team, gave a <a href="http://www.slideshare.net/wickett/gauntlt-velocity-eu2013">tutorial</a> at <a href="http://velocityconf.com/velocityeu2013">Velocity Conf London</a> about integrating security testing in the continuous integration cycle for early feedback on application security level. James stressed the importance of regularly checking for security as release delivery rates increase with continuous delivery. Post-release security checks and lengthy reports from external audits are no longer good enough, according to James. Continuous feedback both for Ops and Devs is required to keep applications safe and avoid security regressions.</p>
<p class="MsoNormal">
 <o:p></o:p></p>
<p class="MsoNormal"><span lang="EN-GB"><a href="http://github.com/GAUNTLT/GAUNTLT"><span lang="EN-US">Gauntlt</span></a></span> is thus meant to put this idea into practice by providing an automated security test framework based on the popular <a href="http://cukes.info/">Cucumber</a> tool typically used for <a href="http://en.wikipedia.org/wiki/Behavior-driven_development">behaviour-driven-development</a> and a set of open source security testing tools. Gauntlt is available as a <a href="http://rubygems.org/gems/gauntlt">Ruby gem</a> so tests can be run as part of a continuous integration/<a href="http://www.infoq.com/articles/preparing-for-cd-in-the-enterprise">delivery pipeline</a> with a Ruby environment. This example generates an HTML test report similar to <a href="http://cukes.info/reports.html">Cucumber’s</a>:
 <o:p></o:p></p>
<p class="MsoNormal"><span style="font-family:" courier=""><code>bundle exec gauntlt --format html &gt; out.html</code>
  <o:p></o:p></span></p>
<p class="MsoNormal">Gauntlt comes packaged with a set of pre-canned attacks using a pre-defined set of “attack adapters” that rely map the steps to the security tools that can run each type of attack:
 <o:p></o:p></p>
<ul> 
 <li>
  <!--[endif]--><span lang="EN-GB"><a href="http://www.arachni-scanner.com/">Arachni</a> (testing for <a href="http://en.wikipedia.org/wiki/Cross-site_scripting">XSS</a>)</span></li> 
 <li>
  <!--[endif]--><span lang="EN-GB"><a href="https://github.com/mozilla/Garmr">Garmr</a> (testing for new login pages or insecure references in login flows)</span></li> 
 <li>
  <!--[endif]--><span lang="EN-GB"><a href="http://sqlmap.org/">SQLmap</a> (testing for <a href="http://en.wikipedia.org/wiki/SQL_injection">SQL injection</a> attacks) </span></li> 
 <li>
  <!--[endif]--><span lang="EN-GB"><a href="http://dirb.sourceforge.net/about.html">dirb</a> (testing for misconfigured web objects)</span></li> 
 <li>
  <!--[endif]--><span lang="EN-GB"><a href="https://github.com/iSECPartners/sslyze">SSlyze</a> (testing for misconfigured SSL servers)</span><span lang="EN-GB" style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
    Symbol"><span style="font-size: 7pt; font-family: 'Times New Roman';">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;</span></span></li> 
 <li>
  <!--[endif]--><span lang="EN-GB"><a href="http://nmap.org/">NMap</a> (testing for unexpected open ports)</span></li> 
</ul>
<p class="MsoNormal">At the moment the tool set can only be extended by indicating a binary command line invocation using a special pre-canned step and checking the output of its execution.
 <o:p></o:p></p>
<p class="MsoNormal">
 <o:p>
  &nbsp;
 </o:p>Under the hoods Gauntlt is running Cucumber. Thus Gauntlt attack files are transformed into Cucumber feature files where each scenario is a specific attack. An example attack file <code>port-check.attack</code> might use <code>nmap</code> for verifying that there are no unexpected ports open in a given host:
 <o:p></o:p></p>
<blockquote> 
 <pre><code> <p class="MsoNormal"><span style="font-family:" courier="">Feature: nmap attacks for example.com 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;</span><span style="font-family:" courier="">&nbsp;&nbsp; Background: 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Given &quot;nmap&quot; is installed 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; And the following profile: 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | name &nbsp;&nbsp;&nbsp;&nbsp;| value &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | hostname | example.com |
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;</span><span style="font-family:" courier="">&nbsp;&nbsp; Scenario: Verify that there are no unexpected ports open 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; When I launch an &quot;nmap&quot; attack with: 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;&quot;&quot; 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; nmap -F &lt;hostname&gt; 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;&quot;&quot; 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Then the output should not contain: 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;&quot;&quot; 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 25/tcp 
     <o:p></o:p></span></p> <p class="MsoNormal"><span style="font-family:" courier="">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &quot;&quot;&quot;
     <o:p></o:p></span></p> </code></pre> 
</blockquote>
<p class="MsoNormal">James sums up <span lang="EN-GB">Gauntlt as an opinionated framework for application security testing inspired by the <a href="http://www.infoq.com/news/2010/06/rugged-software-manifesto">Rugged software manifesto</a>. Its ultimate goal is to promote communication between Dev, Ops and Security teams. The need to include security concerns and monitoring within <a href="http://en.wikipedia.org/wiki/DevOps">DevOps</a> was also mentioned by <a href="http://devopsweekly.com/">DevOps Weekly</a> founder <a href="http://www.infoq.com/author/Gareth-Rushgrove">Gareth Rushgrove</a>’</span>s in his <a href="http://velocityconf.com/velocityeu2013/public/schedule/detail/33016">talk</a> on <a href="http://vimeo.com/75665772">security monitoring</a>.
 <o:p></o:p></p><br><br><br><br><br><br></body></html>
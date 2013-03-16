<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Stripe Open Sources Abba, an A/B Testing Framework</h3><p>&nbsp;<a href="https://stripe.com/">Stripe</a> has open sourced their JavaScript A/B testing framework called <a href="https://github.com/maccman/abba">Abba</a>. In order to set up a web application for testing, the following code snippet needs to be inserted in main page:</p> 
<pre>
&lt;script&gt;
  Abba('test name')
    .control('Test A', function(){ /* ... */ })
    .variant('Test B', function(){ /* ... */ })
    .start();
&lt;/script&gt;</pre> 
<p>This script defines a control test called <code>Test A</code>, against which all results are reported, and another test variant, <code>Test B</code>. There can be multiple variants. For each test a handler is specified, being called by the framework when necessary. The control test may lack a handler.</p> 
<p>When the test is started, Abba randomly calls the handlers associated with different tests. This usually results in serving different pages to site users, and the framework keeps track of each user and their test start and completion status. If set accordingly, Abba can make sure a user sees the same page when visiting the website again.</p> 
<p>Data is stored in MongoDB and can be visualized in a graph displaying&nbsp; daily visitors and conversion rates (visitors that completed the test) for a certain period of time. Values for different variants are weighted and a <a href="http://en.wikipedia.org/wiki/Standard_score">standard score</a> is computed to evaluate the accuracy of the test. The results can be filtered by date and/or browser.</p> 
<p>Abba can be run locally or on a server, instructions being provided to run it on Heroku. The framework requires Ruby 1.9.3 and MongoDB.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
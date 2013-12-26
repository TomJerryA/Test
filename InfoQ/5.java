<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Splitforce A/B Testing for Mobile Applications</h3><p>As mobile applications are becoming a more central part of companies' IT strategies, testing and analyzing those applications also becomes more important. Whereas functional testing of code - for example with the help of unit tests - is probably part of every software project, analyzing user behavior and optimizing conversion rates is still very new to the mobile sector.</p>
<p><a href="http://www.splitforce.com">Splitforce</a> offers A/B testing for mobile apps, so application developers can optimize their apps' features and user experiences for their key business metrics. Essentially, variations of native applications can be tested without the need to re-submit the app in the app-store, and each variation's effect on user behavior is tracked and analyzed so developers can make product and design decisions based on data. Splitforce currently supports native iOS applications and games based on the <a href="http://unity3d.com/">Unity</a> application engine. According to Splitforce, Android support is planned for the first quarter of 2014.</p>
<p>With the help of Splitforce's SDK and web services, developers can create experiments that influence the way their mobile apps are experienced on the users' mobile devices. Hard-coded components in the application code are replaced by dynamic components that can be controlled by Splitforce's servers via a web interface. It is possible to create new and tweak existing variations on-the-fly, including what portion of users will experience one variation of the application and what portion another variation. The success of those variations can be analyzed with regard to three different categories:</p>
<ul> 
 <li><strong>Rates:</strong> Rates are used to analyze how often a certain goal like a purchase or a sign-up is reached as a percentage of total users.</li> 
 <li><strong>Timing:</strong> Timing goals can be used to find out much time a user spends in certain areas of the application or how long it took until the user purchased a product.</li> 
 <li><strong>Quantities:</strong> Quantities offer information about how many times users completed a task like attempting to finish a game level.</li> 
</ul>
<p>&nbsp;</p>
<p>Experiments can be based on variations of text, numbers, colors, booleans or custom subjects. After signing up and defining an experiment, Splitforce creates code-snippets that can be copied and pasted by the application developer into the app's source code. An experiment that tests different button colors and counts purchase events could be added to an iOS application using the following code:</p>
<blockquote> 
 <code> <pre>
[[SFManager currentManager] experimentNamed:@&quot;Experiment #1&quot; applyVariationBlock:^(SFVariation *variation) {
  // Configuration for 'Test Button Colors'
  UIColor *testSubject = [SFUtils colorFromHexString:variation.variationData[@&quot;Test Button Colors&quot;]];
  // set special button color  
} applyDefaultBlock:^(NSError *error) {
  if (error) NSLog(@&quot;Splitforce Error: %@&quot;, error);
  // set default button color
}];  
</pre> </code> 
</blockquote>
<p>In a subsequent section of the application code, the Splitforce server has to be notified, when the desired goal is reached:</p>
<blockquote> 
 <code> <pre>
SFVariation *variation = [SFManager.currentManager variationForExperimentNamed:@&quot;Experiment #1&quot;];

[variation goalResultNamed:@&quot;Item Purchased&quot;];
[variation variationEnded]; 
</pre> </code> 
</blockquote>
<p>Besides inserting pre-generated code snippets, the application developer only has to include libraries in his or her software project and initialize Splitforce during application startup.</p>
<p>&nbsp;</p>
<p><a href="https://www.splitforce.com/pricing">Service plans</a> for using Splitforce depend on the number of daily users included in tests of the instrumented applications. Up to 500 daily users are free, up to 5.000 daily users are covered by the entry plan for $299 per month and the pro plan lets developers test up to 75.000 daily active users for a monthly fee of $2.499, with overages ranging from $0.01-$0.05 per 10 daily active users tested. Companies that need to test with more than 75.000 users can apply for the enterprise plan which also offers more support and services than the pre-defined plans.</p><br><br><br><br><br><br></body></html>
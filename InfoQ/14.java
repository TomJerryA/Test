<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Facebook Unveils Jest for JavaScript Unit Testing, Automatic Mocking</h3><p>Facebook has released <a href="http://facebook.github.io/jest/">Jest</a>, an open source&nbsp;Unit Testing tool for JavaScript, built on top of <a href="http://jasmine.github.io/">Jasmine</a>.</p>
<p>Jest was originally conceived by Facebook two years ago as a way to solve the need for writing fast, reliable tests for the web chat application. As it gained interest internally the project was picked up six months ago by Jeff Morrison, a software engineer for Facebook, who set out to make performance improvements and take Jest open source.</p>
<p>At its most basic level, Jest is designed to make it faster and easier to write idiomatic JavaScript tests. Jest automatically mocks <a href="http://www.commonjs.org/">CommonJS</a> modules returned by require(), and other features include built-in support for DOM APIs in test environments, sensible defaults, support for pre-processing code, and parallel test execution by default.&nbsp;By running tests concurrently in parallel processes, Jest has test runs finish sooner.</p>
<p>Morrison said:</p>
<blockquote> 
 <p>The goal for Jest is to reduce the time spent and cognitive load necessary to get started with testing a project -- and so it provides most of the things you need out of the box: A fast CLI, a set of mocking utilities, and its automatic module mocking system.</p> 
 <p>Additionally, if you're looking for isolation tools like mocking libraries, most other tools will leave you writing quite an unsatisfactory bit of boilerplate in your tests (and often even in your main code) just to get going.</p> 
 <p>We've seen first-hand at Facebook how important it is to spend more time writing your app (vs time spent getting set up to write your app) -- and so this is the problem Jest is focused on solving.</p> 
</blockquote>
<p>Jest differs from the Jasmine framework by adding several layers on top. Most notably, Jest automatically mocks dependencies when running tests. Jest automatically generates mocks for each of a module's depenedencies, and provides those mock by default -- making it easier to&nbsp;isolate a module from its dependencies. Morrison said that isolation is the default for new tests, and developers would now have &quot;complete control&quot; over how much isolation is needed. Each test indicates which modules should or should not be mocked.</p>
<p>Facebook's documentation goes into <a href="http://facebook.github.io/jest/docs/automatic-mocking.html">further detail</a> on Automatic Mocking:</p>
<blockquote>
 Jest actually implements its own version of the require() function in the testing environment. Jest's custom require() function loads the real module, inspects what it looks like, and then makes a mocked version based on what it saw and returns that. 
 <p>This means Jest is going to give you an object with the same shape as the real module, but with mocks for each of the exported values instead of the real values.</p> 
</blockquote>
<p>Although Jest introduces automatic mocking, it is also noted that it is still possible for developers to control what is and is not mocked by providing jest.mock() and jest.dontMock() APIs for customization.</p>
<p>Reaction from the community was mostly positive. On Hacker News, user Cthulu <a href="https://news.ycombinator.com/item?id=7748886">said</a>:</p>
<blockquote>
 Looks interesting: the test suite for our current AngularJS project is slowly slowing down, in part because there's just more tests, but the major performance bottlenecks are: 
 <ul> 
  <li>No parallelisation, even if test suites are all independent</li> 
  <li>DOM tests, which cause a lot of GC pauses</li> 
  <li>(Probably) PhantomJS startup and initialisation (not measured)</li> 
 </ul> I've done a simple optimization where my tests get split in the middle and run in two separate terminals (during development, continuous testing), but it's kinda iffy.
 <br /> 
</blockquote>
<p>Directly addressing dependency injection and AngularJS, Facebook <a href="http://facebook.github.io/jest/docs/common-js-testing.html#content">says</a>&nbsp;&quot;Jest&nbsp;achieves the same result using a different approach.&quot; With Angular, code is written by passing dependencies as arguments, making it very easy to write a test. However, Facebook notes that in order to have a testable function in Angular, developers conform to its specific pattern and pass it into Angular's dependency injection framework. The solution in Jest is slightly different:</p>
<blockquote>
 Jest allows for mocking dependencies in the same way that Angular does, but instead of building a proprietary module loader, it uses CommonJS. This enables you to test any existing code that already uses CommonJS without having to heavily refactor it to make it compatible with another module system.
 <br /> 
</blockquote>
<p>User Caiob agreed with the positive sentiment about Jest and was a fan of the approach to dependency injection,&nbsp;<a href="https://news.ycombinator.com/item?id=7745011">saying</a>: &quot;It's great that Facebook are improving an existing/familiar tool like Jasmine. Also, I love the way they treat CommonJS modules.&quot;</p>
<p>With Jest, Morrison says Facebook want to start of a trend toward making testing easy, leaving developers more time to writing their app. InfoQ readers who would like to contribute to the project can check out the<a href="http://github.com/facebook/jest"> github repo </a>and send pull requests, or join in #jestjs on freenode.</p><br><br><br><br><br><br></body></html>
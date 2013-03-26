<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Git in JavaScript Kickstarter Project Funded in 28 Hours</h3><p><a href="http://creationix.com/">Tim Caswell</a>, a well-known member of the JavaScript and <a href="http://nodejs.org">Node.js</a> communities, came up with the idea to reimplement <a href="http://git-scm.com/">Git</a> in JavaScript and <a href="http://www.kickstarter.com/projects/creationix/js-git">managed to get the project funded on Kickstarter within 28 hours</a> with over 360 backers. The project is another example of <a href="http://www.codinghorror.com/blog/2007/07/the-principle-of-least-power.html">Atwood's Law</a>: &quot;any application that can be written in JavaScript, will eventually be written in JavaScript.&quot;</p> 
<p>InfoQ spoke to Tim to learn more about the project.</p> 
<p><b>Where did the idea for JSGit come from?</b></p> 
<blockquote> 
 <p>I'm always looking for new ways to program the devices I own. I was recently sent a <a href="http://www.microsoft.com/Surface/en-US/surface-with-windows-rt/windows-rt">Surface RT</a> by the nice people at Microsoft, had a couple <a href="http://www.apple.com/ipad/">iPads</a> from a previous project and just bought a <a href="http://www.google.com/intl/en/chrome/devices/chromebook-pixel/">ChromeBook Pixel</a>. They were interesting devices, but I was rather frustrated that they were so locked down and very hostile to development <em>on</em> the device. The one platform that nobody dares to lock down, not even Apple, is the JavaScript in the browser environment. You can generate and then execute code there, you can access local storage, and you can upload and download data on the internet.</p> 
 <p>After working on <a href="http://c9.io">Cloud9</a> for a year, I realized that a browser-based IDE is possible today. The only problem that Cloud9 didn't solve well was the offline story. I wished that I could clone my Git repos locally to my device, work offline while flying overseas (or hanging out in the far end of my backyard), and then when I'm back within reach of internet, pushing my changes back to my public Git repo.</p> 
 <p>Since JavaScript was the one platform that was available everywhere, I decided I really wanted to have Git ported to it.</p> 
</blockquote> 
<p><b>What do you see as use-cases for JSGit, is it just browser-based IDEs and editors or are there more broad applications?</b></p> 
<blockquote>
 My primary use case is browser-based programming environments, but many people have expressed interest in other uses, such as a pure JavaScript Git clients and servers for Node.js. Git is a common component in many deployment systems and having finer grained control of Git for Node.js servers and clients would be very useful to a lot of people.
</blockquote> 
<p><b>Do you have any sense of what the performance will be like?</b></p> 
<blockquote>
 JavaScript itself is fairly fast, I recently wrote some very fast hash functions (MD5, SHA1, SHA256) in JavaScript and was able to get up to 500,000 MD5 hashes per second on my desktop browser. Since cloning a Git repo is slow even using the native client on a fast laptop for large repos, I don't expect this to handle that case well. But for small repos, I expect it to be plenty fast.
</blockquote> 
<p><b>Why not take the approach of cross-compiling the existing C implementation of Git with something like <a href="https://github.com/kripken/emscripten">Emscripten</a> rather than reimplementing everything from scratch in JavaScript?</b></p> 
<blockquote>
 I plan to look into this, but from initial research into this area, there are two problems I foresee. First, Emscripten is a code generator. It generates fairly large code-bases and ends up being a direct port unless you manually tweak lots of code. Second, looking at the Git implementations in C they often are tightly coupled with the underlying filesystem and network calls. These would need heavy customization in a browser-based version of Git. I will need hand-written filesystem abstractions for the various web platforms since each has its own API for file storage.
</blockquote> 
<p><b>There are implementations of Git in C, Java and other languages, what do you think will be the challenges in implementing it in JavaScript specifically?</b></p> 
<blockquote>
 I'm fairly experienced implementing crypto stuff in JavaScript, so I don't expect that to be a problem. But the sheer amount of code that needs implementing will be a problem. I plan on working in the bare essentials first and going up from there till I run out of time.
</blockquote> 
<p><b>Why do this project now? Is there any particular HTML5 technology that makes this possible today?</b></p> 
<blockquote>
 It's more about hardware. There are more and more devices that have long battery life and great screens, but crappy development experiences.
</blockquote> 
<p><b>Your project got funded in little over a day, what features do you expect to be able to build for the funds you will be receiving?</b></p> 
<blockquote>
 Like I estimated in my 
 <a href="http://www.kickstarter.com/projects/creationix/js-git/posts">stretch goals</a>, I hope to have the essential Git features implemented and if there is time, some integration with various platforms.
</blockquote> 
<p><b>Why Kickstarter?</b></p> 
<blockquote>
 It sounded like a good idea at the time. So far it's working out, though after reading through all the Kickstarter rules, I'm feeling like this kind of project barely fits into their ideal for a project.
</blockquote> 
<p><b>Do you think more (JavaScript) open source projects should try to get funding on Kickstarter?</b></p> 
<blockquote>
 I don't know yet, this is an experiment. I do like the idea of screening ideas for support before spending months of time working on them. I've spend hundreds of hours of my free time on past projects only to find out that there is little interest from the community for them. I really like the idea of working full-time on cool projects that people wish existed. I don't know if Kickstarter will work out long term, but I'll keep looking for other ideas if it doesn't.
</blockquote> 
<p>JSGit is not the first JavaScript-related project to successfully reach its funding goal on Kickstarter. Previous projects include <a href="http://www.kickstarter.com/projects/869786663/async-savascript-book?ref=live">a book on asynchronous JavaScript programming</a> and <a href="http://www.kickstarter.com/projects/188988365/lets-code-test-driven-javascript?ref=live">a screencast series on test-driven JavaScript</a>. However, JSGit is the first Kickstarter project to produce a JavaScript library.</p> 
<p>The <a href="http://www.kickstarter.com/projects/creationix/js-git">project is open to pledges</a> until March 30, 2013. Tim expects to start working on the project soon after the pledge deadline expires.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
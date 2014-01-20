<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Math.js: Versatile Math Library For JavaScript</h3><p>&nbsp;<a href="http://mathjs.org/">Math.js</a> is an open source Math library for JavaScript and Node.js for working with numbers, big numbers, complex numbers, units and matrices. It also features a flexible expression parser. InfoQ got in touch with the project founder, <a href="http://josdejong.com/">Jos De Jong</a>, to know more.</p>
<p align="justify">Jos explains the motivation behind the project –</p>
<blockquote> 
 <p align="justify">For JavaScript there are nice libraries out there to work with matrices, complex numbers, statistics, etc. What is lacking though is an integrated solution to do advanced mathematics.&nbsp;Most of the existing libraries come with a&nbsp;<i>chained</i>&nbsp;API, which works very intuitive, but only accepts data types&nbsp;known by the library itself.&nbsp;Hence the integration issue: matrix libraries can't handle complex numbers, and vice versa. You can't combine them.&nbsp;The API of math.js is the same as that of JavaScript's Math object and built in operators: static functions accepting various types of input. Math.js extends this API with support for advanced data types, functions, and constants.</p> 
 <p align="justify">I hope math.js will help making maths in application development trivial and more fun, and helps bridging the gap between the the world of developers and the academic world.</p> 
</blockquote>
<p align="justify">Math.js can be used in three ways&nbsp;–</p>
<ol> 
 <li> 
  <div>
   Using static functions and constants (like JavaScript's Math object) 
   <pre>
math.add(2, 3); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;// 5 
math.sqrt(-4); &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; // 2i 
math.pow([[-1, 2], [3, 1]], 2); &nbsp;// [[7, 0], [0, 7]]</pre> 
  </div> </li> 
 <li> 
  <div align="justify">
   Evaluate string expressions 
   <pre>
math.eval('1.2 * (2 +  4.5)'); //7.8
math.eval('5.08 cm to inch'); //2 inch </pre> 
  </div> </li> 
 <li> 
  <div align="justify">
   Using chaining operations
   <br /> 
   <pre>
math.select(3)
    .add(4)
    .multiply(2)
    .done();      //14</pre> 
  </div> </li> 
</ol>
<p align="justify">There are several examples on the <a href="http://mathjs.org/">math.js website</a> as well as in <a href="https://github.com/josdejong/mathjs/tree/master/examples/">the documentation</a>.&nbsp;</p>
<p align="justify">Jos is hoping to reach the first stable version 1.0 within a couple of months.</p>
<blockquote> 
 <p align="justify">What's left before 1.0 is writing a reference documentation, reaching 100% code coverage with the unit tests and resolving some rough edges here and there.</p> 
</blockquote>
<p align="justify">1.0 will also see the API getting stabilized, after which&nbsp;the focus might shift to optimization. Jos identifies several possibilities such as using typed arrays, parallelization, asm.js for potential performance improvements.</p>
<p align="justify">On why Jos chose JavaScript instead of something like Python which already has libraries such as NumPi/SciPi -</p>
<blockquote> 
 <p align="justify">Latest years we have seen an enormous push towards the cloud and web applications, and I'm fully into this myself too.&nbsp;Browsers and JavaScript engines are becoming faster and faster. Since a couple of years you can run JavaScript server side using&nbsp;<a href="http://nodejs.org/">node.js</a>. This opens up a lot of new possibilities, which has resulted in an&nbsp;<a href="http://resin.io/happy-18th-birthday-javascript/">explosion</a>&nbsp;of the JavaScript ecosystem and its popularity. It looks like JavaScript is becoming the most ubiquitous language&nbsp;<i>ever</i>. JavaScript is far from the perfect language, but I like JavaScript and its community a lot.</p> 
</blockquote>
<p align="justify">There are already several end-user projects using math.js. Jos’s own project, <a href="http://mathnotepad.com/">mathnotepad</a>&nbsp;is&nbsp;powered by math.js and in early stages of development. Math.js is also used by&nbsp;<a href="http://numerics.info/">numerics</a>, a popular calculator project.&nbsp;</p>
<p align="justify">To get started with Math.js, head over to <a href="https://github.com/josdejong/mathjs/blob/master/docs/getting_started.md">the documentation</a>.&nbsp;</p><br><br><br><br><br><br></body></html>
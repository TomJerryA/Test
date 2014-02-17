<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Simplified CSS Preprocessing with restyle.js</h3><p>Andrea Giammarchi's <a href="https://github.com/WebReflection/restyle">restyle.js</a> is a new, JavaScript-based, CSS preprocessor that can run on either the server (via Node.js) or in the browser. It touts itself as &quot;a simplified CSS approach&quot;, generating all prefixed variations of CSS rules and properties and, if applicable, inserting them into the DOM.</p>
<p>There's no shortage of CSS preprocessors around, but Andrea claims there are <a href="http://webreflection.blogspot.co.uk/2014/02/restylejs-simplified-css-approach.html">none as lightweight</a> that work in both the server and the client:</p>
<blockquote> 
 <p>Before you think about &quot;yet another CSS preprocessor&quot;, I'd like to inform you that I've asked around to few common, well known, CSS or general web developers and it looks like this little script was still missing ... once you'll realize what is this about, you'll probably wonder yourself &quot;how come nobody has done this already?&quot; My idea is that somebody probably did but I am not sure in 0.8KB minzipped and compatible with both server and client down to IE6 ... so here I am talking about restyle.</p> 
</blockquote>
<p>The library exposes a solitary method, restyle() , which accepts two arguments. The first is expected to be a JavaScript object, with a grammar familiar to both CSS and DOM style editing. For example,</p>
<pre>
 restyle({
    'body &gt; div.my-div': {
        backgroundColor: 'goldenrod',
        backgroundImage: 'url(mybg.png)'
    }
}); </pre>
<p>This will produce the following CSS:</p>
<pre>
 body &gt; div.my-div {
    background-color: goldenrod;
    background-url: url(mybg.png);
} </pre>
<p>We could also specify the JavaScript object in a different manner to achieve the same output:</p>
<pre>
 restyle({
    'body &gt; div.my-div': {
        background: {
            color: 'goldenrod',
            image: 'url(mybg.png)'
        }
    }
}); </pre>
<p>Of course, this is nothing special and the reduction in markup so far, if any, is tiny. But restyle.js shines brighter when you're trying something that would be a little more tedious with standard CSS, like vendor prefixes. The second argument allows you to specify the vendor prefixes that will be generated in the output, for example:</p>
<pre>
 restyle({
    '.my-div': {
        transition: 'background-color 500ms ease';
        backgroundColor: '#00f';
    }
}, ['moz', 'webkit']); </pre>
<p>This results in the following generated CSS:</p>
<pre>
 .my-div {
    -webkit-transition: background-color 500ms ease;
    -moz-transition: background-color 500ms ease;
    transition: background-color 500ms ease;
    background-color: #00f;
} </pre>
<p>This comes especially in handy when writing animation rules; a few lines of code can be transformed into many lines of vendor prefixed at-rules and CSS properties with so little effort. On the server, omitting the second argument will result in no prefixes, while restyle.js run in the browser would generate all common vendor prefixes regardless of which browser is executing the code.</p>
<p>The restyle() function also returns a different result depending on the environment. In a Node.js script, it returns a string containing the resulting CSS. In the browser, however, the CSS is automatically inserted into the DOM to take immediate effect, and the return value is a handy little object containing the properties node (the resulting style element), css (a string containing the generated CSS), and a single method, remove() , which can be called to immediately remove the inserted styles from the DOM.</p>
<p>A basic example page <a href="http://webreflection.github.io/restyle/">is available</a> that lets you play around with restyle.js by writing your own code and generating the result. As <a href="http://webreflection.blogspot.co.uk/2014/02/restylejs-simplified-css-approach.html#comments">some comments</a> on Andrea's blog pointed out, restyle.js is based on the same idea as a similar library, the larger and more full-featured <a href="https://github.com/krasimir/absurd">AbsurdJS</a>. At barely one tenth of the size, though, restyle is certainly lightweight and interesting enough to be worth a look. Take a look at <a href="https://github.com/WebReflection/restyle/blob/master/README.md">the readme</a> to get started using it.</p><br><br><br><br><br><br></body></html>
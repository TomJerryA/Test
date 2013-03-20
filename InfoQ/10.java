<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Canvas-Based Chart.js Version 0.1 Released</h3><p><a href="http://www.chartjs.org/">Chart.js</a>, a canvas-driven Javascript charting library, was released under the MIT open source license by <a href="http://www.nickdownie.com/">Nick Downie</a> on March 17th as an alternative to SVG-based charting libraries.</p> 
<p>“I wanted to create an out-of-the-box charting solution that gave web designers the ability to achieve the aesthetics they're after with a simple API that's easy to understand, and be lightweight and portable enough for developers to include in complex web applications,” Downie says.</p> 
<p>Chart.js exposes <a href="http://www.chartjs.org/docs/">six different charting types</a> atop an api that knits together the data and options to render the chart. Downie spent a month building the library and the supporting documentation for his final university project. Since open-sourcing the code on the 17th, “I've been totally overwhelmed with the response so far - I posted a link up on Hacker news, and a day later I've had tens of thousands of visitors to the site, and an inbox full of Github issues and contributions,” Downie says.</p> 
<p>Unlike SVG charting libraries, chart.js uses a single canvas node instead of rendering multiple DOM nodes per chart element. Because of this single-node rendering, chart.js only has one hook for event listeners, which consequently “involves keeping track of any areas requiring interaction in memory, and iterating through these while checking against the current mouse position. It's a whole load of looping every time a user moves their mouse. It also means regular clearing/redrawing of the canvas if we draw the tooltips directly onto the canvas itself.” Downie says. “When it comes to customisation of this, it's difficult to come up with a simple API which accomplishes everyone’s needs - some people may want tooltips, others might want to draw lines on the chart, or highlight data points etc. It starts to get very complex very quickly,” Downie says. While he might be amenable to adding tooltips, Downie prefers to promote chart.js as an alternative to “overly complicated [charting SVG] solutions, with a large load overhead for developers wanting to include simple, static graphs in their sites and applications.”</p> 
<p>While a simplified API is one benefit to the canvas-approach, chart.js loses the scalability inherent in vector-based SVG charting tools because of its dependence on canvas-produced raster images. In these cases, “declare percent based CSS widths [on the canvas] for responsive layouts. For hi-DPI displays, Chart.js automatically scales to the correct devicePixelRatio and scales back down to the right device pixel size with CSS,” says Downie.</p> 
<p>Native to canvas is its ability to export a base64 image via <a href="https://developer.mozilla.org/en-US/docs/DOM/HTMLCanvasElement">toDataUrl</a>. “I'm hoping in future releases to add some utility functions to the charts after they have been created, so users can clear, update and export charts easily - essentially Chart.js would provide a wrapper for this function,” Downie says.</p> 
<p>Graduating in the spring, Downie hopes to add a handful of more features to chart.js as well as concentrate on his full-time job after graduation. “[Chart.js] gave me a nice excuse to mix design and development to create something quite elegant and (hopefully) useful for people in the web design community.”</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
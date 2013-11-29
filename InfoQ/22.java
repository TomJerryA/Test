<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>List & Label 19 Adds Report Parameters, Collection Variables, OData and REST Data Providers</h3><p><a href="http://www.combit.net/en/">List &amp; Label 19</a> has been released with support for report parameters, collection variables, expandable regions, interative sorting in addition to the introduction of new charts such as combined, stacked, funnel, pipeline, shapefile and donut. It also provides support for OData and REST data providers including legends with fixed widths.<br /> <br /> List &amp; Label 19 has an ability to produce user interfaces which support high resolution portable devices such as tablet PCs. This feature ensures that text does not appear blurred and prevents fonts to appear in small size. Moreover, LL19 is compatible with Windows 8.1 and Visual Studio 2013 including a third party IDE, Embarcadero RAD Studio XE5. With the help of the latest release, it is possible to display SVG export format in any HTML5 compatible browser. <br /> <br /> In an interview to InfoQ, Jochen Bartlau, Managing Director and Head of Development, List &amp; Label shared more about the features included with the new release.</p>
<p><strong>InfoQ: What is the significance of report parameters and collection variables?</strong></p>
<blockquote>
  Both are important features of 
 <a href="http://www.combit.net/en/reporting-tool/report-generator-List-Label-new-version/">List &amp; Label 19</a> and set a sound foundation for extensions in the coming versions of the reporting tool. Collection variables are a true innovation that I haven't seen in any other reporting product before. They allow the addition of attributes based on conditions - you can easily define a color variable named &quot;CategoryColor&quot; that can be used in any conditional formatting just based e.g. on the first two characters of your serial number if these encode the required information. This is of great help if the data hasn't been optimized for reporting beforehand.
 <br /> 
 <br /> Report parameters enable flexible reports - instead of having to design a separate report for each customer, product or year, it's now easily possible to offer a drop-down list for each of these and allow the end user to choose from any parameter permutation. Of course, the data available in these drop-down lists can be read from the database. List &amp; Label has a very thorough support for parameters, offering different types like date, boolean or text and even dependent parameters where one gets filtered depending on the choice for the other. 
</blockquote>
<p><strong>InfoQ: Can you share with us the usage of shapefile chart?</strong></p>
<blockquote>
  Shapefiles are the de-facto standard to visualize data on maps. The internet is full of free shapefiles that enable showing data distributions on Country, State or even Subsidiary scale. The shapefile chart is tightly integrated with the other charts in LL. 
 <p>It consumes the same data as any other chart type, integrating it into existing reports is a piece of cake. We even support the attribute databases that usually come with shapefiles. That way, the data from the report can easily be linked to the attributes of a country (e.g. its ISO code).</p> 
</blockquote>
<p><strong>InfoQ: What is the difference between shapefile and geovisualization?</strong></p>
<blockquote>
  Shapefiles go way beyond geovisualization. While the latter is one important use case for them, users can easily create their own shapefiles showing floor or seating plans or any other arbitrary shape data. Given that the format is standardized, many CAD applications support exporting to shapefiles. We ship an example of a huge cinema seat plan that shows the potential of this feature. Any application that requires displaying data distribution on a global or local scale can immediately benefit from this feature. 
</blockquote>
<p><strong>InfoQ: Can you elaborate one usage scenario where Donut chart is used?</strong></p>
<blockquote>
  The donut chart is a very pretty addition to the List &amp; Label chart family. Basically, it is a lightweight variant of the already existing pie charts. It allows for full customization - the size of the &quot;hole&quot; can just as easily be set as labels, values, fonts and colors. 
</blockquote>
<p><strong>InfoQ: Can you explain the importance of OData data provider?</strong></p>
<blockquote>
  OData has become a quite common data format for web databases. Microsoft decided to push it even further by adding OData support to LightSwitch. While it was possible before to bind to OData sources (e.g. using the JSON data provider), it was a somehow cumbersome process. The new data provider now even offers metadata parsing support - all tables, relations and data types are parsed automatically. Relational data is queried on demand only, ensuring an optimal performance. 
</blockquote>
<p><strong>InfoQ: What purpose does REST data provider serve in List &amp; Label 19?</strong></p>
<blockquote>
  The REST provider opens a whole new world of data sources - content management systems, ticketing systems and many other web services offer REST support for querying data. By adding support for REST, using cloud based data has just become a breeze. 
</blockquote>
<p><strong>InfoQ: Can you share with us the future roadmap of List &amp; Label?</strong></p>
<blockquote>
  We'll likely continue down the road we’ve taken in the past versions - keeping a close eye on the market and try to follow trends as early as possible. I expect to see more and more Desktop as a Service offerings in the coming months. These enable the usage of &quot;classic&quot; applications on modern devices like tablets or phablets. We'll make sure to offer optimum support in these scenarios - our high DPI support in 19 was just one first step in that direction. Besides working on cloud/web features, we'll likely be further improving on our strengths. Our report designer is a signature feature that desires some care from time to time to make sure we set usability standards just once again. 
</blockquote><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Concurrent Releases Lingual, a SQL DSL for Hadoop</h3><p>
 <!--[if gte mso 9]><xml>
<o:OfficeDocumentSettings>
<o:AllowPNG />
</o:OfficeDocumentSettings>
</xml><![endif]--></p> 
<p>
 <!--[if gte mso 9]><xml>
<w:WordDocument>
<w:View>Normal</w:View>
<w:Zoom>0</w:Zoom>
<w:TrackMoves />
<w:TrackFormatting />
<w:PunctuationKerning />
<w:ValidateAgainstSchemas />
<w:SaveIfXMLInvalid>false</w:SaveIfXMLInvalid>
<w:IgnoreMixedContent>false</w:IgnoreMixedContent>
<w:AlwaysShowPlaceholderText>false</w:AlwaysShowPlaceholderText>
<w:DoNotPromoteQF />
<w:LidThemeOther>EN-US</w:LidThemeOther>
<w:LidThemeAsian>X-NONE</w:LidThemeAsian>
<w:LidThemeComplexScript>X-NONE</w:LidThemeComplexScript>
<w:Compatibility>
<w:BreakWrappedTables />
<w:SnapToGridInCell />
<w:WrapTextWithPunct />
<w:UseAsianBreakRules />
<w:DontGrowAutofit />
<w:SplitPgBreakAndParaMark />
<w:EnableOpenTypeKerning />
<w:DontFlipMirrorIndents />
<w:OverrideTableStyleHps />
<w:UseFELayout />
</w:Compatibility>
<w:DoNotOptimizeForBrowser />
<m:mathPr>
<m:mathFont m:val="Cambria Math" />
<m:brkBin m:val="before" />
<m:brkBinSub m:val="&#45;-" />
<m:smallFrac m:val="off" />
<m:dispDef />
<m:lMargin m:val="0" />
<m:rMargin m:val="0" />
<m:defJc m:val="centerGroup" />
<m:wrapIndent m:val="1440" />
<m:intLim m:val="subSup" />
<m:naryLim m:val="undOvr" />
</m:mathPr></w:WordDocument>
</xml><![endif]-->
 <!--[if gte mso 9]><xml>
<w:LatentStyles DefLockedState="false" DefUnhideWhenUsed="true"
DefSemiHidden="true" DefQFormat="false" DefPriority="99"
LatentStyleCount="267">
<w:LsdException Locked="false" Priority="0" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Normal" />
<w:LsdException Locked="false" Priority="9" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="heading 1" />
<w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 2" />
<w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 3" />
<w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 4" />
<w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 5" />
<w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 6" />
<w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 7" />
<w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 8" />
<w:LsdException Locked="false" Priority="9" QFormat="true" Name="heading 9" />
<w:LsdException Locked="false" Priority="39" Name="toc 1" />
<w:LsdException Locked="false" Priority="39" Name="toc 2" />
<w:LsdException Locked="false" Priority="39" Name="toc 3" />
<w:LsdException Locked="false" Priority="39" Name="toc 4" />
<w:LsdException Locked="false" Priority="39" Name="toc 5" />
<w:LsdException Locked="false" Priority="39" Name="toc 6" />
<w:LsdException Locked="false" Priority="39" Name="toc 7" />
<w:LsdException Locked="false" Priority="39" Name="toc 8" />
<w:LsdException Locked="false" Priority="39" Name="toc 9" />
<w:LsdException Locked="false" Priority="35" QFormat="true" Name="caption" />
<w:LsdException Locked="false" Priority="10" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Title" />
<w:LsdException Locked="false" Priority="1" Name="Default Paragraph Font" />
<w:LsdException Locked="false" Priority="11" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Subtitle" />
<w:LsdException Locked="false" Priority="22" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Strong" />
<w:LsdException Locked="false" Priority="20" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Emphasis" />
<w:LsdException Locked="false" Priority="59" SemiHidden="false"
UnhideWhenUsed="false" Name="Table Grid" />
<w:LsdException Locked="false" UnhideWhenUsed="false" Name="Placeholder Text" />
<w:LsdException Locked="false" Priority="1" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="No Spacing" />
<w:LsdException Locked="false" Priority="60" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Shading" />
<w:LsdException Locked="false" Priority="61" SemiHidden="false"
UnhideWhenUsed="false" Name="Light List" />
<w:LsdException Locked="false" Priority="62" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Grid" />
<w:LsdException Locked="false" Priority="63" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 1" />
<w:LsdException Locked="false" Priority="64" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 2" />
<w:LsdException Locked="false" Priority="65" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 1" />
<w:LsdException Locked="false" Priority="66" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 2" />
<w:LsdException Locked="false" Priority="67" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 1" />
<w:LsdException Locked="false" Priority="68" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 2" />
<w:LsdException Locked="false" Priority="69" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 3" />
<w:LsdException Locked="false" Priority="70" SemiHidden="false"
UnhideWhenUsed="false" Name="Dark List" />
<w:LsdException Locked="false" Priority="71" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Shading" />
<w:LsdException Locked="false" Priority="72" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful List" />
<w:LsdException Locked="false" Priority="73" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Grid" />
<w:LsdException Locked="false" Priority="60" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Shading Accent 1" />
<w:LsdException Locked="false" Priority="61" SemiHidden="false"
UnhideWhenUsed="false" Name="Light List Accent 1" />
<w:LsdException Locked="false" Priority="62" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Grid Accent 1" />
<w:LsdException Locked="false" Priority="63" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 1 Accent 1" />
<w:LsdException Locked="false" Priority="64" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 2 Accent 1" />
<w:LsdException Locked="false" Priority="65" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 1 Accent 1" />
<w:LsdException Locked="false" UnhideWhenUsed="false" Name="Revision" />
<w:LsdException Locked="false" Priority="34" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="List Paragraph" />
<w:LsdException Locked="false" Priority="29" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Quote" />
<w:LsdException Locked="false" Priority="30" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Intense Quote" />
<w:LsdException Locked="false" Priority="66" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 2 Accent 1" />
<w:LsdException Locked="false" Priority="67" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 1 Accent 1" />
<w:LsdException Locked="false" Priority="68" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 2 Accent 1" />
<w:LsdException Locked="false" Priority="69" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 3 Accent 1" />
<w:LsdException Locked="false" Priority="70" SemiHidden="false"
UnhideWhenUsed="false" Name="Dark List Accent 1" />
<w:LsdException Locked="false" Priority="71" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Shading Accent 1" />
<w:LsdException Locked="false" Priority="72" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful List Accent 1" />
<w:LsdException Locked="false" Priority="73" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Grid Accent 1" />
<w:LsdException Locked="false" Priority="60" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Shading Accent 2" />
<w:LsdException Locked="false" Priority="61" SemiHidden="false"
UnhideWhenUsed="false" Name="Light List Accent 2" />
<w:LsdException Locked="false" Priority="62" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Grid Accent 2" />
<w:LsdException Locked="false" Priority="63" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 1 Accent 2" />
<w:LsdException Locked="false" Priority="64" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 2 Accent 2" />
<w:LsdException Locked="false" Priority="65" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 1 Accent 2" />
<w:LsdException Locked="false" Priority="66" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 2 Accent 2" />
<w:LsdException Locked="false" Priority="67" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 1 Accent 2" />
<w:LsdException Locked="false" Priority="68" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 2 Accent 2" />
<w:LsdException Locked="false" Priority="69" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 3 Accent 2" />
<w:LsdException Locked="false" Priority="70" SemiHidden="false"
UnhideWhenUsed="false" Name="Dark List Accent 2" />
<w:LsdException Locked="false" Priority="71" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Shading Accent 2" />
<w:LsdException Locked="false" Priority="72" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful List Accent 2" />
<w:LsdException Locked="false" Priority="73" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Grid Accent 2" />
<w:LsdException Locked="false" Priority="60" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Shading Accent 3" />
<w:LsdException Locked="false" Priority="61" SemiHidden="false"
UnhideWhenUsed="false" Name="Light List Accent 3" />
<w:LsdException Locked="false" Priority="62" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Grid Accent 3" />
<w:LsdException Locked="false" Priority="63" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 1 Accent 3" />
<w:LsdException Locked="false" Priority="64" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 2 Accent 3" />
<w:LsdException Locked="false" Priority="65" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 1 Accent 3" />
<w:LsdException Locked="false" Priority="66" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 2 Accent 3" />
<w:LsdException Locked="false" Priority="67" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 1 Accent 3" />
<w:LsdException Locked="false" Priority="68" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 2 Accent 3" />
<w:LsdException Locked="false" Priority="69" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 3 Accent 3" />
<w:LsdException Locked="false" Priority="70" SemiHidden="false"
UnhideWhenUsed="false" Name="Dark List Accent 3" />
<w:LsdException Locked="false" Priority="71" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Shading Accent 3" />
<w:LsdException Locked="false" Priority="72" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful List Accent 3" />
<w:LsdException Locked="false" Priority="73" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Grid Accent 3" />
<w:LsdException Locked="false" Priority="60" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Shading Accent 4" />
<w:LsdException Locked="false" Priority="61" SemiHidden="false"
UnhideWhenUsed="false" Name="Light List Accent 4" />
<w:LsdException Locked="false" Priority="62" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Grid Accent 4" />
<w:LsdException Locked="false" Priority="63" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 1 Accent 4" />
<w:LsdException Locked="false" Priority="64" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 2 Accent 4" />
<w:LsdException Locked="false" Priority="65" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 1 Accent 4" />
<w:LsdException Locked="false" Priority="66" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 2 Accent 4" />
<w:LsdException Locked="false" Priority="67" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 1 Accent 4" />
<w:LsdException Locked="false" Priority="68" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 2 Accent 4" />
<w:LsdException Locked="false" Priority="69" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 3 Accent 4" />
<w:LsdException Locked="false" Priority="70" SemiHidden="false"
UnhideWhenUsed="false" Name="Dark List Accent 4" />
<w:LsdException Locked="false" Priority="71" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Shading Accent 4" />
<w:LsdException Locked="false" Priority="72" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful List Accent 4" />
<w:LsdException Locked="false" Priority="73" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Grid Accent 4" />
<w:LsdException Locked="false" Priority="60" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Shading Accent 5" />
<w:LsdException Locked="false" Priority="61" SemiHidden="false"
UnhideWhenUsed="false" Name="Light List Accent 5" />
<w:LsdException Locked="false" Priority="62" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Grid Accent 5" />
<w:LsdException Locked="false" Priority="63" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 1 Accent 5" />
<w:LsdException Locked="false" Priority="64" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 2 Accent 5" />
<w:LsdException Locked="false" Priority="65" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 1 Accent 5" />
<w:LsdException Locked="false" Priority="66" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 2 Accent 5" />
<w:LsdException Locked="false" Priority="67" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 1 Accent 5" />
<w:LsdException Locked="false" Priority="68" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 2 Accent 5" />
<w:LsdException Locked="false" Priority="69" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 3 Accent 5" />
<w:LsdException Locked="false" Priority="70" SemiHidden="false"
UnhideWhenUsed="false" Name="Dark List Accent 5" />
<w:LsdException Locked="false" Priority="71" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Shading Accent 5" />
<w:LsdException Locked="false" Priority="72" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful List Accent 5" />
<w:LsdException Locked="false" Priority="73" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Grid Accent 5" />
<w:LsdException Locked="false" Priority="60" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Shading Accent 6" />
<w:LsdException Locked="false" Priority="61" SemiHidden="false"
UnhideWhenUsed="false" Name="Light List Accent 6" />
<w:LsdException Locked="false" Priority="62" SemiHidden="false"
UnhideWhenUsed="false" Name="Light Grid Accent 6" />
<w:LsdException Locked="false" Priority="63" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 1 Accent 6" />
<w:LsdException Locked="false" Priority="64" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Shading 2 Accent 6" />
<w:LsdException Locked="false" Priority="65" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 1 Accent 6" />
<w:LsdException Locked="false" Priority="66" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium List 2 Accent 6" />
<w:LsdException Locked="false" Priority="67" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 1 Accent 6" />
<w:LsdException Locked="false" Priority="68" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 2 Accent 6" />
<w:LsdException Locked="false" Priority="69" SemiHidden="false"
UnhideWhenUsed="false" Name="Medium Grid 3 Accent 6" />
<w:LsdException Locked="false" Priority="70" SemiHidden="false"
UnhideWhenUsed="false" Name="Dark List Accent 6" />
<w:LsdException Locked="false" Priority="71" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Shading Accent 6" />
<w:LsdException Locked="false" Priority="72" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful List Accent 6" />
<w:LsdException Locked="false" Priority="73" SemiHidden="false"
UnhideWhenUsed="false" Name="Colorful Grid Accent 6" />
<w:LsdException Locked="false" Priority="19" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Subtle Emphasis" />
<w:LsdException Locked="false" Priority="21" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Intense Emphasis" />
<w:LsdException Locked="false" Priority="31" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Subtle Reference" />
<w:LsdException Locked="false" Priority="32" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Intense Reference" />
<w:LsdException Locked="false" Priority="33" SemiHidden="false"
UnhideWhenUsed="false" QFormat="true" Name="Book Title" />
<w:LsdException Locked="false" Priority="37" Name="Bibliography" />
<w:LsdException Locked="false" Priority="39" QFormat="true" Name="TOC Heading" />
</w:LatentStyles>
</xml><![endif]-->
 <!--[if gte mso 10]>
<style>
/* Style Definitions */
table.MsoNormalTable
{mso-style-name:"Table Normal";
mso-tstyle-rowband-size:0;
mso-tstyle-colband-size:0;
mso-style-noshow:yes;
mso-style-priority:99;
mso-style-parent:"";
mso-padding-alt:0in 5.4pt 0in 5.4pt;
mso-para-margin:0in;
mso-para-margin-bottom:.0001pt;
mso-pagination:widow-orphan;
font-size:12.0pt;
font-family:"Cambria","serif";
mso-ascii-font-family:Cambria;
mso-ascii-theme-font:minor-latin;
mso-hansi-font-family:Cambria;
mso-hansi-theme-font:minor-latin;}
</style>
<![endif]--> </p>
<p style="margin-bottom:12.0pt"><a href="http://www.cascading.org/about/"><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:
bold">Cascading</span></a><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-bidi-font-weight:bold"> is a popular application framework - a </span><a href="http://www.patternlanguage.com/"><span style="font-size:10.0pt;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:bold">pattern language</span></a><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:
bold"> for enterprise data workflows. Cascading allows to define complex data processing flows and create sophisticated data oriented frameworks. These frameworks can be used as </span><a href="http://en.wikipedia.org/wiki/Domain-specific_language"><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:
bold">Domain Specific Languages (DSLs)</span></a><span style="font-size:10.0pt;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:bold"> for scripting. </span></p> 
<p style="margin-bottom:12.0pt"><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-bidi-font-weight:bold">The </span><a href="http://www.concurrentinc.com/posts/%20"><span style="font-size:10.0pt;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:bold">latest addition</span></a><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:
bold"> to </span><a href="http://www.cascading.org/extensions/"><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:
bold">Cascading extensions</span></a><span style="font-size:10.0pt;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:bold"> is </span><a href="http://www.cascading.org/lingual/%20"><span style="font-size:10.0pt;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:bold">Lingual</span></a><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:
bold">, the new SQL - based DSL combining power of </span><a href="https://github.com/julianhyde/optiq"><span style="font-size:10.0pt;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:bold">Optiq</span></a><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-bidi-font-weight:
bold"> - a dynamic data management framework - and cascading Hadoop-based execution. The purpose of Lingual is to ease Hadoop entrance barrier for developers and data analysts familiar with SQL, JDBC and traditional BI tools. It provides what the company calls “true SQL for Cascading and Hadoop”.</span></p> 
<p style="margin-bottom:12.0pt"><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-bidi-font-weight:bold">According to Cascading</span><span style="font-size:
10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;"> CTO and Founder<span style="mso-bidi-font-weight:bold"> </span>Chris Wensel<span style="mso-bidi-font-weight:
bold">, the Lingual’s goal is to provide an ANSI-standard SQL interface that is designed to play well with all of the big name Hadoop distributions running on site or in cloud environments. This will allow a “cut and paste” capability for existing ANSI SQL code from traditional data warehouses so users can access data that’s locked away on a Hadoop cluster. It’s also possible to query and export data from Hadoop right into a wide range of BI tools.</span></span></p> 
<p style="margin-bottom:12.0pt"><span style="font-size:10.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;">With Lingual<span style="color:#323232">, </span>companies can now leverage existing skill sets and product investments by carrying them over to Hadoop via a standards-based technology. Analysts and developers familiar with SQL, JDBC or traditional BI tools, can now instantly and easily create and run Big Data applications on Hadoop while gaining significant productivity and time-to-market benefits. </span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-fareast-font-family:&quot;Times New Roman&quot;">Lingual is not going to provide sub-second response times on a petabyte of data on a Hadoop cluster. Rather, the company’s goal is to provide the ability to easily move applications onto Hadoop—the challenge there is really around moving from a relational or MPP database over to Hadoop.</span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-fareast-font-family:&quot;Times New Roman&quot;">Lingual distribution </span><a href="http://www.slideshare.net/pacoid"><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-fareast-font-family:&quot;Times New Roman&quot;">includes</span></a><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-fareast-font-family:&quot;Times New Roman&quot;">: </span></p> 
<p style="text-indent:-.25in;mso-list:l0 level1 lfo1" class="MsoListParagraphCxSpFirst"><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">&middot;<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><span style="font-size:10.0pt;line-height:115%;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-fareast-font-family:&quot;Times New Roman&quot;">ANSI standard SQL parser and optimizer build on top of Cascading framework</span></p> 
<p style="text-indent:-.25in;mso-list:l0 level1 lfo1" class="MsoListParagraphCxSpMiddle"><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">&middot;<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><span style="font-size:10.0pt;line-height:115%;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-fareast-font-family:&quot;Times New Roman&quot;">Relational catalog view into large-scale unstructured data</span></p> 
<p style="text-indent:-.25in;mso-list:l0 level1 lfo1" class="MsoListParagraphCxSpMiddle"><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">&middot;<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><span style="font-size:10.0pt;line-height:115%;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-fareast-font-family:&quot;Times New Roman&quot;">SQL shell to test and submit queries to Hadoop</span></p> 
<p style="text-indent:-.25in;mso-list:l0 level1 lfo1" class="MsoListParagraphCxSpLast"><span style="font-family:Symbol;mso-fareast-font-family:Symbol;mso-bidi-font-family:
Symbol"><span style="mso-list:Ignore">&middot;<span style="font:7.0pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><span style="font-size:10.0pt;line-height:115%;
font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-fareast-font-family:&quot;Times New Roman&quot;">JDBC driver to integrate with the existing BI tools and application servers.<span style="mso-spacerun:yes">&nbsp; </span></span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">InfoQ had a chance to discuss Lingual with Chris K Wensel, CTO and Founder of Concurrent, Inc. </span></p> 
<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">InfoQ: </span></b><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">Lingual looks very similar to Apache Hive. Can you describe the main advantages of Lingual compared to Hive?</span></p> 
<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">Wensel: </span></b><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">The primary goal of Lingual is to focus on ANSI compatibility. Hadoop is never used alone, you either need to get data off the HDFS bit-bucket into alternative tools like R or Mondrian, or you need to move existing workloads onto Hadoop to leverage its cost/performance benefits. In both cases you likely already know SQL, the “app” or query you are migrating is in SQL or, if not more importantly, the tools you are using only know SQL. So it’s very important to offer a standards-based SQL interface. </span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">To achieve this we have lots of tests. We currently have extracted 6,000 complex SQL queries from the Mondrian test suite, and we already have 90% coverage and plan to add more from popular tools.</span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">Lingual is not intended to be an ad-hoc query tool that provides human scale response times. For that, we recommend using a proper distributed MPP style database. I don’t recommend using Hadoop for what it wasn’t intended for.</span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">That said, we do offer a standards compliant JDBC Driver, and ways to test queries against local data using Cascading’s “local mode” which has no Hadoop dependencies to speed up testing.</span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">Above the goal of ANSI compliance, Lingual runs on top of Cascading, so any improvements to Cascading, or any new “planners” other than those provided for Hadoop and local in memory processing will be inherited by Lingual along with Cascading’s existing robustness, flexibility, extensibility, and familiarity by those companies that have already standardized on Cascading for computation.</span></p> 
<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">InfoQ: </span></b><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">From the existing description it is not clear how Lingual defines and maintains a relational catalog. Can you describe some of the implementation details? Does it require a special prepared files or uses mechanisms similar to Hive SerDe to provide mapping between existing data and table definitions?</span></p> 
<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">Wensel: </span></b><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">There will be a built in “single user” catalog in initial release. HCatalog integration and/or an alternative will be provided in the near term. Currently the meta-data catalog is a trivial (optionally human editable) JSON document that can be stored on a local file system or on HDFS (even S3), which allows for basic sharing.</span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">As for reading/writing data, Lingual will support all the integrations Cascading supports (and Cascalog, Scalding, etc). This is all managed by the Lingual “catalog “ command line interface. </span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">There is no need to use any “proprietary to Cascading“ format to query data. </span></p> 
<p class="MsoNormal"><span style="font-size:10.0pt;line-height:115%;font-family:
&quot;Calibri&quot;,&quot;sans-serif&quot;;mso-ascii-theme-font:major-latin;mso-hansi-theme-font:
major-latin;mso-bidi-font-family:&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">A user simply registers a file from the command line as a Table, and any meta-data (columns and types) will be discovered from the file if possible. Moving forward we will make it trivial to add new supported data formats from the catalog tool as well.</span></p> 
<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">InfoQ: </span></b><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">What is a security model for Lingual? Is it based on file access permissions? Is it supported by the JDBC driver?<b style="mso-bidi-font-weight:normal"> </b></span></p> 
<p class="MsoNormal"><b style="mso-bidi-font-weight:normal"><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">Wensel: </span></b><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;
mso-ascii-theme-font:major-latin;mso-hansi-theme-font:major-latin;mso-bidi-font-family:
&quot;Times New Roman&quot;;mso-bidi-theme-font:minor-bidi">There are no current plans to extend Hadoop’s current security model. </span></p> 
<p></p> 
<p id="lastElm"></p></body></html>
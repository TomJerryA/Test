<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ConcurrentがHadoop用SQL DSLをリリース</h3><div class="clearer-space">
 &nbsp;
</div> 
<div id="newsContent"> 
 <p>
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
<![endif]--></p> 
 <p><a target="_blank" href="http://www.infoq.com/news/2013/02/Lingual;jsessionid=E4066B2285F17609956A77574E0F0019"><em>原文(投稿日：2013/02/28)へのリンク</em></a></p> 
 <p style="margin-bottom: 12pt"><a target="_blank" href="http://www.cascading.org/about/"><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">Cascading</span></a><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">は、人気のあるアプリケーションフレームワークで、企業データワークフロー向けの</span><a target="_blank" href="http://www.patternlanguage.com/"><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">パターン言語</span></a><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">である。 Cascadingにより、複雑なデータ処理フローを定義し、洗練されたデータ指向フレームワークを作成できる。これらのフレームワークは、スクリプト用の</span><a target="_blank" href="http://en.wikipedia.org/wiki/Domain-specific_language"><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">Domain Specific Languages (DSLs)</span></a><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">として使うことができる。</span></p> 
 <p style="margin-bottom: 12pt"><a target="_blank" href="http://www.cascading.org/extensions/"><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">Cascading拡張機能</span></a>に<a target="_blank" href="http://www.concurrentinc.com/posts/%20"><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">最近追加された</span></a><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">のが、</span><a target="_blank" href="http://www.cascading.org/lingual/%20"><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">Lingual</span></a><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">、新しいSQLで、DSLをベースにし、</span><a target="_blank" href="https://github.com/julianhyde/optiq"><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">Optiq</span></a><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold"> （動的データ管理フレームワーク）のパワーと CascadingのHadoopベースの実行を組み合わせている。 Lingualの目的は、SQL,JDBC,従来のBIツールに精通している開発者とデータ分析家に対して、Hadoop活用のハードルを下げることである。同社は、自分たちが言っている「Cascading と Hadoop向けの真のSQL」を提供する。</span></p> 
 <p style="margin-bottom: 12pt"><span style="font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-weight: bold">CascadingのCTOで設立者である Chris Wensel氏によれば、 Lingualの目標は、サイトやクラウド環境で走っている有名なHadoopディストリビューション全てと上手く連携するように設計されたANSI標準のSQLインターフェースを提供することである。これにより、従来のデータウェアハウスから既存のANSI　SQLコードを「カット＆ペースト」できるので、Hadoopクラスタ上に仕舞われているデータにユーザーがアクセスできるようになる。またHadoopにあるデータをクエリし、即座に様々なBIツールにエクスポートすることが可能である。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">Lingualにより、企業は、標準ベースの技術を介してHadoopで、既存のスキルセットと製品投資を活用できるようになった。SQL,JDBC,あるいは従来のBIツールに精通している分析家や開発者は、著しい生産性とタイムツーマーケットの便益を得ながら、即座に、そして容易にHadoop上でビッグデータアプリケーションを作成し、走らせることができるようになる。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">Lingualは、Hadoopクラスタ上のテラバイトのデータに対して一秒未満の応答時間を提供しようとするものではない。そうではなく、同社のゴールは、アプリケーションをHadoop上に簡単に移す機能を提供することである。課題は、リレーショナルあるいはMPPデータベースからHadoopへの移動に関する周りに本当に存在する。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">Lingualディストリビューションには以下のものが<span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">含まれる。</span><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">: </span></span></p> 
 <p style="text-indent: -0.25in; mso-list: l0 level1 lfo1" class="MsoListParagraphCxSpFirst"><span style="font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol"><span style="mso-list: Ignore">&middot;<span style="font: 7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">Cascading フレームワークの上に作られたANSI標準のSQLパーサーとオプティマイザー</span></p> 
 <p style="text-indent: -0.25in; mso-list: l0 level1 lfo1" class="MsoListParagraphCxSpMiddle"><span style="font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol"><span style="mso-list: Ignore">&middot;<span style="font: 7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">大規模な非構造化データに対するリレーショナルカタログビュー</span></p> 
 <p style="text-indent: -0.25in; mso-list: l0 level1 lfo1" class="MsoListParagraphCxSpMiddle"><span style="font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol"><span style="mso-list: Ignore">&middot;<span style="font: 7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">Hadoopのテストとクエリを発行するためのSQLシェル</span></p> 
 <p style="text-indent: -0.25in; mso-list: l0 level1 lfo1" class="MsoListParagraphCxSpLast"><span style="font-family: Symbol; mso-fareast-font-family: Symbol; mso-bidi-font-family: Symbol"><span style="mso-list: Ignore">&middot;<span style="font: 7pt &quot;Times New Roman&quot;">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></span></span><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-fareast-font-family: 'Times New Roman'">既存のBIツールとアプリケーション・サーバーを統合するためのJDBCドライバー<span style="mso-spacerun: yes">&nbsp; </span></span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">InfoQは、Concurrent, Inc.のCTOであり、設立者であるChris K Wensel氏とLingualを議論する機会があった。 </span></p> 
 <p class="MsoNormal"><b style="mso-bidi-font-weight: normal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">InfoQ: </span></b><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">Lingualは、 Apache Hiveに大変似てますね。LingualのHiveに対する優位性は何ですか？</span></p> 
 <p class="MsoNormal"><b style="mso-bidi-font-weight: normal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">Wensel: </span></b><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">Lingualの第一の目標は、ANSIとの互換性にフォーカスすることです。Hadoopは決して単独では使われません、 HDFSの bit-bucketからデータを取得して R やMondrianのような代替ツールに移す必要があるか、既存のワークロードをHadoop上に移して、そのコストパフォーマンスの恩恵を利用できるする必要があります。両方の場合で、あなたはおそらく、既にSQL,「アプリ」、あなたが移行しているクエリがSQLにあることを知っています。あるいは、もしそうでなければ、もっと重要なのは、あなたが使っているツールは、SQLだけ知っていることです。なので、標準ベースのSQLインターフェースを提供することは非常に重要です。 </span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">このことを達成するために、我々はたくさんのテストを持っています。我々は現在、 Mondrianテストスイートから6000の複雑なSQLクエリを抽出し、既に90％のカバレッジを達成し、人気のあるツールからもっと追加する計画です。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">Lingualは、人間規模の応答時間を提供する、アドホックなクエリツールを目指してはいません。そのために、我々は、適切に分散されたMPPスタイルのデータベースを使うことを進めています。私は、Hadoopに向かないところには、Hadoopを使うことを進めません。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">すなわち、我々が提供するのは、標準準拠のJDBCドライバーとテストを速くするためにHadoopに依存しない、Cascadingの「ローカルモード」使って、ローカルなデータに対してクエリをテストする方法です。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">ANSI準拠の目標の他に、 Lingualは Cascading上で走るので、Cascadingへのあらゆる改善、Hadoopとメモリ処理でのローカルに提供されている以外のあらゆる新規の「プラナー」は、 Lingualに引き継がれます。一緒に、Cascadingの既存の堅牢さ、柔軟性、拡張性、 Cascading上に計算用の標準化を既に行なっている会社への親和性も引き継がれます。</span></p> 
 <p class="MsoNormal"><b style="mso-bidi-font-weight: normal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">InfoQ: </span></b><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">既存の説明からは、Lingualがどのようにリレーショナルカタログを定義し、維持しているのかはっきりしません。ある程度実証の詳細をお話しくださいますか？既存のデータとテーブル定義間のマッピングを提供するのに、て区別用意したファイルを使うのですか、それとも Hive SerDeに似たメカニズムを使うのですか？</span></p> 
 <p class="MsoNormal"><b style="mso-bidi-font-weight: normal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">Wensel: </span></b><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">最初のリリースには、「シングルユーザー」カタログが組み込まれています。近い内に HCatalog統合と/か代替が提供されるでしょう。現在、メタデータカタログは、簡単な（オプションで人が編集可能）JSONドキュメントでローカルなファイルシステムか基本的な共有ができるHDFS（S3でも）上に保存できる。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">データの読み書きに関しては、 Lingualは、Cascadingサポートする全ての組み込みモジュール（と Cascalog, Scaldingなど）をサポートする。これらは全てLingual “catalog “コマンドラインインターフェースによって管理される。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">データのクエリにいかなる「 Cascadingプロプライエタリ」なフォーマットを使う必要がない。</span></p> 
 <p class="MsoNormal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">ユーザーは、単にコマンドラインからファイルをテーブルとして登録すれば、あらゆるメタデータ（列と型）は、可能であればファイルから発見できる。更に進んで、我々はカタログツールから新しくサポートするデータフォーマットを追加するのも簡単にするつもりです。</span></p> 
 <p class="MsoNormal"><b style="mso-bidi-font-weight: normal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">InfoQ: </span></b><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">Lingualのセキュリティモデルは、何ですか？それはファイルのアクセスパーミッションに基づいていますか？それは、JDBCドライバーによってサポートされていますか？<b style="mso-bidi-font-weight: normal"> </b></span></p> 
 <p class="MsoNormal"><b style="mso-bidi-font-weight: normal"><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">Wensel: </span></b><span style="line-height: 115%; font-family: &quot;Calibri&quot;,&quot;sans-serif&quot;; font-size: 10pt; mso-bidi-font-family: 'Times New Roman'; mso-ascii-theme-font: major-latin; mso-hansi-theme-font: major-latin; mso-bidi-theme-font: minor-bidi">現在、Hadoopの現行のセキュリティモデルを拡張する計画はありません。</span></p> 
 <p>&nbsp;</p> 
 <p id="lastElm">&nbsp;</p> 
</div> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
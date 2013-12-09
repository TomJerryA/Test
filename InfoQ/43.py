<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Cascading 2.5がHadoop 2をサポート</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/cascading"><em>原文(投稿日：2013/11/19)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
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
</w:Compatibility>
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
mso-para-margin-top:0in;
mso-para-margin-right:0in;
mso-para-margin-bottom:10.0pt;
mso-para-margin-left:0in;
line-height:115%;
mso-pagination:widow-orphan;
font-size:11.0pt;
font-family:"Calibri","sans-serif";
mso-ascii-font-family:Calibri;
mso-ascii-theme-font:minor-latin;
mso-hansi-font-family:Calibri;
mso-hansi-theme-font:minor-latin;}
</style>
<![endif]--></p> 
  <p class="MsoNormal">Hadoopは順調に普及しているが，企業にはまだ，Hadoopベースのアプリケーション開発を迅速かつコスト効率よく行うための適切なアプローチを見つけ出すという，直面した課題が残っている。この目標を達成する手段のひとつが<a href="http://en.wikipedia.org/wiki/Domain-specific_language">DSL(Domain Specific Language)</a>を採用することだ。これによってHadoop実装の相当な簡略化が達成できることも少なくない。</p> 
  <p class="MsoNormal">低レベルのMapReduce API上に構築された代表的なJava DSLのひとつとして<a href="http://www.cascading.org/">Cascading</a>がある。大規模なデータワークフローを関数型プログラミングで実装するDSLとして2007年に公開されたCascadingは，&quot;配管工事&quot; のメタフォに基づいている。データ処理を馴染み深いもの – パイプ，栓，タプル列，フィルタ，継ぎ手(Join)，トラップなど –で組み上げられたワークフローとして定義するのである。</p> 
  <p>Cascadingは今週，製品の新バージョン – Cascading 2.5 – を公開した。YARNを含むHadoop 2のサポートが提供されている。同社のプレスリリースによれば，この新リリースには次のような機能がある:</p> 
  <blockquote> 
   <ul> 
    <li>YARNを含むHadoop 2の新機能サポート。Hadoop 2へのアップグレードを計画中のCascadingユーザはこれにより，アプリケーションのシームレスな移行と，YARNなど新しい高度な機能の利用が可能になる。</li> 
    <li>複雑な表結合(Join)操作のパフォーマンス改善，動的パーティションの最適化，およびHDFSへのデータ格納の効率性向上。</li> 
    <li>Cloudera, Hortonworks, MapR, Intel, Altiscale, Qubole, Amazon EMRなど，他のHadoopベンダやHadoop・アズ・ア・サービスのプロバイダに対する幅広い互換性の追加。その中にはCascadingユーザに対して，より豊富なデプロイメントオプションや利用可能なサービスをオンプレミス，クラウド上を問わず提供可能なものもある。</li> 
   </ul> 
  </blockquote> 
  <p class="MsoNormal">これと同時にConcurrentも，<a href="http://www.infoq.com/news/2013/02/Lingual">Cascading Lingual</a>の一般提供を発表している。Hadoopベースのデータにアクセスするための包括的ANSI SQLインターフェースを提供する，オープンソースの開発プロジェクトである。このプロジェクトでは高度な業界標準OLAPツールから引用した，7,000以上のSQL-99ステートメントをカバーする。Cascadingによれば:</p> 
  <blockquote> 
   <p class="MsoNormal">Hadoopエコシステム内の任意のツールを対象に，幅広いSQLのカバレッジを提供します。Hadoopをシンプルで扱いやすいものにするとともに，たったひとつのSQL文を使うだけで，複数のデータストアを対象とするHadoopへのシステム統合を簡単に実現するという意味で，これは革新的なものです。</p> 
  </blockquote> 
  <p class="MsoNormal" style="line-height:normal"><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">InfoQではCascadingの最新リリースについて，Concurrent Inc.のCTOで創設者のChris K Wensel氏と議論する機会を得た。</span></p> 
  <p class="MsoNormal" style="line-height:normal"><b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">InfoQ: </span></b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Cascading 2.5でYARNをサポートするというのは，正確にはどのようなことなのでしょう - MapReduceコードがYARNのリソースマネージャを使っているという事実を言っているのでしょうか，あるいはCascading独自のアプリケーションマネージャを新たに開発する上で，実際にYARNを利用しているのですか？</span></p> 
  <p class="MsoNormal" style="line-height:normal"><b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Wensel: </span></b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Cascading 2.5がYARNを暗黙的にサポートしている，つまりCascading 2.5がHadoop 2をサポートしているためにYARNの機能もサポートされる，という意味です。</span><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Cascadingのアプリケーション開発で，実際にYARNを利用している訳ではありません。</span></p> 
  <p class="MsoNormal" style="line-height:normal"><b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">InfoQ: </span></b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Cascadingアプリケーションのパフォーマンスをさらに改善する目的で，Apache Tezを利用する予定はありますか？</span></p> 
  <p class="MsoNormal" style="line-height:normal"><b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Wensel: </span></b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">はい，そのつもりです。</span><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Tezの計画は私たちのロードマップにありますので，適切な時期になればアップデートを連絡する予定でいます。</span></p> 
  <p class="MsoNormal" style="line-height:normal"><b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">InfoQ: </span></b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">複雑な表結合のパフォーマンス向上と最適化について，さらに取り組む予定はありますか？</span></p> 
  <p class="MsoNormal" style="line-height:normal"><b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Wensel: </span></b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">従来よりも複雑で特別な結合対応が利用できるように，APIをアップデートしました。</span><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">ある特定の状況下では，この機能を活用することが可能になるでしょう。</span></p> 
  <p class="MsoNormal" style="line-height:normal"><b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">InfoQ: </span></b><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">あなたの意見として，SQLベースの処理が重視されている現状が，Hadoopで開発されたアプリケーションの範囲を限定していると思いますか？</span><span style="font-size:10.0pt;font-family:&quot;Cambria&quot;,&quot;serif&quot;">極めて大きな勢力でありながら，SQLが解決可能な問題の範囲はごく限られています。このことが企業がHadoopを活用する上で，アプリケーションの範囲を限定しているように思うのです。</span></p> 
  <p class="MsoNormal"><b><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Cambria&quot;,&quot;serif&quot;">Wensel: </span></b><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Cambria&quot;,&quot;serif&quot;;color:#222222;background:white">SQLはその他99%の開発者，アナリスト，あるいはレガシシステムでHadoopの利用を可能にします。</span><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Cambria&quot;,&quot;serif&quot;;color:#222222;background:white">SQLのせいで壁に当たることはあるかも知れません。ですがおよそ90%の問題は，SQLで合理的に表現することができます。Cascadingは戦い方の選択肢を提供するものなのです。</span><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Cambria&quot;,&quot;serif&quot;;color:#222222;background:white">例えば，SQLならば１行でできるようなことのために，まとまったJavaコードを書きたいと思う人がいるでしょうか。</span><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Cambria&quot;,&quot;serif&quot;;color:#222222;background:white">同じように，Javaで記述してテストするのがベストであることをするのに数百行のSQLを書く人もいないはずです。</span><span style="font-size:10.0pt;line-height:115%;font-family:&quot;Cambria&quot;,&quot;serif&quot;;color:#222222;background:white">Cascadingは開発者にフレキシビリティを提供するのです。</span></p> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
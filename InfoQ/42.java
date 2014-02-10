<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Improved Object Inspection with Visual Studio 2013 Update 2</h3><p><a href="http://www.microsoft.com/en-us/download/details.aspx?id=41699">Visual Studio 2013 Update 2 CTP 1</a> has introduced a new feature which enable developers to inspect values of objects and instances, which ultimately improve diagnostic capabilities. This feature makes use of dumps with heap to fetch information required for object inspection.</p>
<p>The type summary page included with Visual Studio 2013 displays an icon which enables you to navigate through the new instance view instead of displaying a drop down expansion of instances in a type. This action will open a new instance view with which you can dig deeper into the dump. Furthermore, the default value can be edited by adding a DebuggerDisplayAttribute.</p>
<p><img src="http://www.infoq.com/resource/news/2014/02/object-inspection-vs2013-update2/en/resources/Figure_1_VS_2013_Update_1.png" alt="" _href="img://Figure_1_VS_2013_Update_1.png" _p="true" /></p>
<p>Moreover, if you hover over the items displayed inside instance view, you will view a tip which enables you to inspect values for the selected instance. It is also possible to expand objects to inspect the data in the subfields in addition to the usage of quick watch.</p>
<p>After performing the above object inspection workaround, you will view that all user entries contained the same ID and the BinaryData will have an excessively large bulk of the allocation of the user object. You can easily work out the previous type overview by either selecting Type from the breadcrumbs at the top, hit the Back button or Backspace key.</p><br><br><br><br><br><br></body></html>
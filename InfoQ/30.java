<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Xamarin’s Rough Transition to 64-bit iOS/OSX</h3><p>When Xamarin started their iOS project the devices were only available in a 32-bit mode, which meant 32-bit versions of NSInteger and CGFloat. When they started looking into 64-bit OSX they realized that their assumptions about those data types was wrong. <a href="http://tirania.org/monomac/archive/2013/Nov-11.html">Miguel continues</a>,</p>
<blockquote> 
 <p>We would need to audit all of our APIs to do the proper type mapping and we would break source code compatibility, with code like this:</p> 
 <pre><p>var foo = new Xxx ();</p><p>int count = foo.GetRowCount ();</p><p>// oops, can not cast a long into an int.</p></pre> 
 <p>When we combined source code breakage with the fact that Apple had a 32-bit compatibility story and we had some legacy libraries that depended on 32-bit only APIs meant that we were in no rush to move to a 64-bit world.</p> 
</blockquote>
<p>With the introduction of 64-bit only libraries in Mountain Lion they saw a need to change this design. It was further compounded by Apple’s decision to offer 32-bit and 64-bit versions of the iPhone 5. To deal with these new challenges Xamarin has created three new data types:</p>
<ul> 
 <li>nint</li> 
 <li>nuint</li> 
 <li>nfloat</li> 
</ul>
<p>These new structs are defined as 32-bit or 64-bit depending on which platform the code is being compiled to. But there is more to the story than that. Primitive math uses special IL instructions for operations such as addition while user defined structs need to call the op_Addition method.</p>
<p>This can cause a small but noticeable impact in performance sensitive code. Since these types are so fundamental to working with native libraries, the AOT compiler was modified to reinterpret operations with these typee. Miguel continues,</p>
<blockquote> 
 <p>The call op_Addition ends up being the same as the native ECMA CIL add instructions. The IL might look scarier, but the native code is identical.</p> 
</blockquote>
<p>Some may wonder why Xamarin didn’t just go with IntPtr, the CLR data type that supports platform-specific integers. Miguel writes,</p>
<blockquote> 
 <p>We chose the names nint, nuint over the built-in IntPtr and UIntPtr, because they felt natural &quot;native integers&quot; as opposed to the cultural association that IntPtr has with pointer or a native token. Additionally, we did not have the equivalent native floating point type.</p> 
 <p>We chose to stay away from using the names NSInteger and CGFloat for a couple of reasons: the functionality is general enough that it might be worth using in Mono in places beyond Mac and iOS and because it feels like these are real VM supported types as opposed to some type definition or alias. In an ideal world, these would eventually be part of the C# standard.</p> 
</blockquote><br><br><br><br><br><br></body></html>
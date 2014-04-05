<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>SIMD Support in .NET</h3><p>Six years after Mono, Microsoft’s implementation of the CLR has finally gained support for SIMD via RyuJIT. Still in community preview, RyuJIT is the next generation JIT compiler for .NET.</p>
<p>SIMD stands for Single Instruction, Multiple Data. It is a special set of CPU instructions that performs the same operation on each element in a 2, 4, 8, or 16 element array simultaneously. When <a href="http://www.infoq.com/news/2008/11/Mono-SMID">Mono announced their SIMD support</a> back in 2008 we reported,</p>
<blockquote> 
 <p>The performance gains are remarkable. Using a Spring-Gravity algorithm, a naive C++ program takes 9.5 seconds to run. By comparison, a literal conversion into Mono takes a pitiful 17.7 seconds. But by switching from standard operators to SIMD functions, the time to run Mono drops to 1.7 seconds.</p> 
</blockquote>
<p>The obvious uses for this includes physics engines in games and scientific research. It can also be used in financial applications that perform the same calculations across a series of stocks or bonds.</p>
<p>Enabling SIMD support in .NET requires more than just installing RyuJIT and using the correct vector types. Here are the steps outlined by <a href="http://blogs.msdn.com/b/clrcodegeneration/archive/2014/04/03/ryujit-ctp3-how-to-use-simd.aspx">Kevin Frei</a> of Microsoft,</p>
<blockquote> 
 <p>1. Go get <a href="http://aka.ms/RyuJIT">RyuJIT CTP3</a> and install it (requires x64 Windows 8.1 or Window Server 2012R2, same as before)</p> 
 <p>2. Set the &quot;use RyuJIT&quot; environment variable: set COMPLUS_AltJit=*</p> 
 <p>3. Now pay attention, because things diverge here a bit:</p> 
 <p>4. Set a new (and temporary) “enable SIMD stuff” environment variable: set COMPLUS_FeatureSIMD=1</p> 
 <p>5. Add the Microsoft.Bcl.Simd NuGet package to your project (you must select “include Prerelease” or use the –Pre option)</p> 
 <p>6. Tricky thing necessary until RyuJIT is final: Add a reference to Microsoft.Numerics.Vectors.Vector&lt;T&gt; to a class constructor that will be invoked BEFORE your methods that use the new Vector types. I’d suggest just putting it in your program’s entry class’s constructor. It must occur in the class constructor, not the instance constructor.</p> 
 <p>7. Make sure your application is actually running on x64. If you don't see protojit.dll loaded in your process (tasklist /M protojit.dll) then you've missed something here.</p> 
</blockquote>
<p>It should be noted that there is more than one type of SIMD available. Kevin writes,</p>
<blockquote> 
 <p>One quick detail, for those of you that are trying this stuff out immediately: our plan (and we've already prototyped this) is to have Vector&lt;T&gt; automatically use AVX SIMD types on hardware where the performance of AVX code should be better than SSE2. Doing that properly, however, requires some changes to the .NET runtime. We're only able to support SSE2 for the CTP release because of that restriction (and time wasn't really on our side, either).</p> 
</blockquote>
<p>RyuJIT itself is designed primarily to improve application startup time on 64-bit machines. Previously Microsoft assumed that x86 was being used by consumers while x64 was solely in the hands of IT departments running servers where startup time wasn’t a serious concern. This allowed them to choose a fast JIT compiler for x86 and a slower, but more efficient, JIT compiler for x64. Fast forward roughly a decade and that is no longer the case.</p>
<blockquote> 
 <p>The .NET Code Generation team has been working on a new, next-generation x64 compiler, codenamed RyuJIT. This new JIT is twice as fast, meaning apps compiled with RyuJIT start up to 30% faster (Time spent in the JIT compiler is only one component of startup time, so the app doesn’t start twice as fast just because the JIT is twice as fast.) Moreover, the new JIT still produces great code that runs efficiently throughout the long run of a server process.</p> 
</blockquote>
<p>-- <a href="http://blogs.msdn.com/b/dotnet/archive/2013/09/30/ryujit-the-next-generation-jit-compiler.aspx">.NET Framework Blog, September 2013</a></p><br><br><br><br><br><br></body></html>
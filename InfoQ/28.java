<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Mono JIT, GC Get Better</h3><p><a href="http://news.mono-project.com/2014/02/25/mono-3-2-7-is-out/">Mono 3.2.7 is out</a>, with a lot of new features such as an improved JIT, new interpreter for LINQ, use of native instructions for 64 bits, and more.</p>
<p>This is a major feature release, accumulating about 5 months of development. Most improvements seem to be under-the-hood performance improvements, optimizations and better compatibility. Some of the highlights -</p>
<ul> 
 <li>Initial support for the HardFP ABI (Application Binary Interface) on ARM. This enables mono to be used on more recent versions of linux and produce better code on those targets. Read more to understand the <a href="http://www.gurucoding.com/en/rpi_cross_compiler/diff_hardfp_softfp.php">difference between HardFP and SoftFP</a>.</li> 
 <li>The ABCREM (<a href="https://github.com/mono/mono/blob/master/mono/mini/abcremoval.c">array bound checks removal</a>) optimization now <a href="https://github.com/mono/mono/commit/6c0fa0d567f69e58bba4603f5b14435a7d827ab4">works much better on 64 bit systems</a></li> 
 <li>Two new optimizations - a <a href="http://en.wikipedia.org/wiki/Loop-invariant_code_motion">Loop Invariant Code Motion</a> pass and <a href="http://llvm.org/docs/AliasAnalysis.html">Alias Analysis</a>. Can lead upto 20% performance gains in some functions</li> 
 <li>64-bit CAS instructions now supported on 32 bit systems leading to significant boost on PLINQ workloads with multi core.</li> 
 <li>More recent version of LLVM is used, and it can now generate fast TLS (Thread Local Storage) access</li> 
 <li>Micro-optimizations for the GC - optimizations in internal data structures and use of intrinsics to speed up core loops</li> 
 <li>An interpreter for LINQ and dynamic statements that can be used by <a href="http://www.mono-project.com/AOT">FullAOT</a> runtimes</li> 
 <li>Better support for custom task schedulers with <a href="https://github.com/mono/mono/commit/3b664f331fe8a1920e88437d91b715775dc789f6">task awaiters</a></li> 
 <li>Significantly improved reachability and flow analysis in the C# compiler - this leads to better code warnings</li> 
</ul>
<p>The release also includes several bug fixes. To see a full list of improvements, have a look at the <a href="http://www.mono-project.com/Release_Notes_Mono_3.2#New_in_Mono_3.2.7">release notes</a>.&nbsp;</p><br><br><br><br><br><br></body></html>
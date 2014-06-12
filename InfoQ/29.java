<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Swift Might Not Be As Fast As Apple Claims It To Be: First Benchmarks</h3><p>Performance is one of the benefits that <a href="https://developer.apple.com/swift/">Apple claims</a> its new Swift programming language should bring to OS X and iOS developers. First experiments and benchmarks executed by independent developers show that in some cases Swift performance is not yet satisfactory, though.</p>
<p>Developer <a href="https://stackoverflow.com/questions/24101718/swift-performance-sorting-arrays">Jukka Suomela wrote a post on Stack Overflow</a> describing its findings when implementing an algorithm in Swift and noticing that it had very poor performance. Narrowing down his analysis, Jukka has been able to find out that the major bottleneck in his code came from a task as simple as sorting an array.</p>
<p>Indeed, sorting a 1 million random integers array took 6 seconds when using Swift, versus 0.06 seconds when using C++, and 0.6 seconds when using Python. Those results were obtained compiling with the <code>-O3</code> optimization level, which is commonly used by Xcode for release builds. When compiler optimizations where disabled altogether, corresponding to the <code>-O0</code> flag used by Xcode for debug builds, the above described test took 88 seconds, according to Jukka.</p>
<p>Jukka's findings where confirmed by other developers joining in the conversation on Stack Overflow. Developer <a href="https://stackoverflow.com/users/1905712/sjeohp">sjeohp</a> implemented the <a href="en.wikipedia.org/wiki/Quicksort">quicksort algorithm</a> to find out that Swift was about 1000 times slower than C with no compiler optimizations enabled (<code>-Onone</code>). On the other hand, he found that Swift was slightly faster than C when aggressive compiler optimizations (<code>-Ofast</code>) were enforced. Similar findings were highlighted in a <a href="http://stackoverflow.com/questions/24102609/why-swift-is-100-times-slower-than-c-in-this-image-processing-test">second post on Stack Overflow</a>, describing an image processing test.</p>
<p>Aggressive optimizations, according to <a href="http://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html#Optimize-Options">LLVM documentation</a>, disregard strict standard compliance. <code>-Ofast</code> enables all -O3 optimizations and additionally turns on <code>-ffast-math</code>, which relaxes IEEE or ISO specifications for math functions, leading to possible incorrect output for programs that require the guarantees of those specifications. Furthermore, <code>-Ofast</code> disables the checks for integer overflows and array indexing overflows, thus harshly reducing Swift safety features.</p>
<p>Going deeper into the analysis, Jukka inspected the assembly code generated by the compiler in a different test and found out that a simple loop over an array would generate a lot of memory management (retain and release) calls that were completely unnecessary. No math was involved in this test, showing thus that the main performance bottleneck likely came from those astray calls.</p>
<p><a href="http://www.reddit.com/r/programming/comments/27slp5/swift_might_not_be_as_fast_as_apple_touts_it_to">Several developers pointed out</a> that Swift is still in beta and this could be a good enough explanation of the current behaviour of Swift programs. Specifically, the described behaviour with unnecessary release/retain calls <a href="https://stackoverflow.com/questions/24101718/swift-performance-sorting-arrays#comment37183103_24102237">hints at some ARC optimizer bugs that could be fixed without requiring aggressive optimizations</a>.</p>
<p>While the language is in beta, Apple will not allow developers to submit apps for review that have been built using Swift. <a href="http://www.infoq.com/news/2014/06/apple-ios8-sdk">The final Xcode release is expected next fall</a>.</p><br><br><br><br><br><br></body></html>
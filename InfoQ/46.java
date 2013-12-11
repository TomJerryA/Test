<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>TypedMVVM Uses TypeScript to Build Windows Store Apps with WinJS</h3><p><a href="http://typedmvvm.codeplex.com/">TypedMVVM</a> developed by Davide Zordan is a collection of samples and libraries for writing Windows Store apps using WinJS, <a href="http://www.typescriptlang.org/">TypeScript</a> and <a href="http://en.wikipedia.org/wiki/Model_View_ViewModel">MVVM</a>. It enable developers to make use of TypeScript in a real world scenario by applying separation of concerns via the MVVM pattern in a simple Windows Store navigation app developed with <a href="http://msdn.microsoft.com/en-us/library/windows/apps/br229773.aspx">WinJS</a>.</p>
<p>According to Davide, all the .js source files has been converted to TypeScript with new folder structure including classes/interface implementations. While designData provides implementation for design-time data to enable Blendability, libs include TypeScript definitions and TypedMVVM core classes, particularly RelayCommand&lt;T&gt; and ViewModelBase. The package also includes interfaces for Services, ViewModels and ViewModelFactory in addition to concrete ViewModels implementations and views definitions.</p>
<p>InfoQ had a chat with <a href="http://www.davidezordan.net/blog">Davide</a>, Software Architect, Developer and Microsoft MVP to know more about TypedMVVM. <br /> <br /> <strong>InfoQ: Can you share with us the purpose behind the development of TypedMVVM?</strong></p>
<blockquote>
  I like writing code in a structured way and embracing best practices like separation of concerns, object orientation, modularization, testability, extensibility.
 <br /> 
 <br /> TypeScript is providing developers with a lot of features that are, in my opinion, fundamental for writing professional application. In particular, the possibility to perform type checking and inference, refactoring and full intellisense support is a must need when writing complex and large applications. For these reasons I decided to implement a simple set of classes for illustrating how the MVVM design pattern could be applied in a WinJS navigation application using TypeScript. 
</blockquote>
<p><strong>InfoQ: What is the difference between Windows store apps built with and without TypedMVVM? </strong></p>
<blockquote>
  Traditional Windows Store apps built with WinJS use JavaScript as a core language. TypedMVVM uses TypeScript as a core language which provides support for static typing, interfaces, classes (just to name a few) but, at the end, compiles to plain JavaScript. It also contains some helper classes to help the developer for getting started with the ViewModel pattern in order to write code which is properly architected and testable. 
</blockquote>
<p><strong>InfoQ: What kind of applications cn be developed using TypedMVVM?</strong></p>
<blockquote>
  The current target is Windows Store apps using the WinJS framework. 
</blockquote>
<p><strong>InfoQ: Are you aware of any real world application where TypedMVVM has been implemented?</strong></p>
<blockquote>
  The project has just been released so I don't have, at the moment, information about real projects.
 <br type="_moz" /> 
</blockquote>
<p><strong>InfoQ: Can you share the future roadmap of TypedMVVM?</strong></p>
<blockquote>
  I'm still in the process of defining the roadmap, however I'm thinking about features like inversion of control, loose coupling messaging and application specific services: these ones would be really useful.
 <br type="_moz" /> 
</blockquote><br><br><br><br><br><br></body></html>
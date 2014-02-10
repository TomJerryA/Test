<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Google's Java Coding Standards</h3><p> Google has recently released their complete definition of <a href="http://google-styleguide.googlecode.com/svn/trunk/javaguide.html">coding standards for Java</a> source code. These are hard-and-fast rules that are clearly enforceable, and are followed universally within Google. It covers not only formatting, but other types of conventions and coding standards. </p>
<p> The document is broken up into 6 main sections: Source File Basics, Source File Structure, Formatting, Naming, Programming Practices, and Javadoc. <i>Source File Basics</i> talks about filenames, file encoding, whitespace characters, and special characters. <i>Source File Structure</i> talks about license information, package and import statements, and class member ordering. <i>Formatting</i> talks about braces, indents, line wrapping, whitespace, parentheses, enums, arrays, switch statements, annotations, comments, and modifiers. <i>Naming</i> talks about identifiers (package, class, method, constant, field, local variable, type variable) and defines CamelCase. <i>Programming Practices</i> talks about @Override, exceptions, static members and finalizers. <i>Javadoc</i> talks about how to format Javadoc and where it is required. </p>
<p> Here are a few items contained in the guide. </p>
<ul> 
 <li>No wildcard imports.</li> 
 <li>Overloads appear sequentially.</li> 
 <li>Braces are used even when the body is empty or contains a single statement.</li> 
 <li>2 spaces indentation.</li> 
 <li>Column limit can be 80 or 100 characters.</li> 
 <li>No C-style array declarations.</li> 
 <li>The default statement in switch statements are required.</li> 
 <li>Modifiers appear in the order recommended by the Java Language Specification.</li> 
 <li>Constants use CONSTANT_CASE. Note that every constant is a static final field, but not all static final fields are constants.</li> 
</ul>
<p> For further reading, please read the <a href="http://google-styleguide.googlecode.com/svn/trunk/javaguide.html">Google Java Style</a>. There is also the official <a href="http://www.oracle.com/technetwork/java/javase/documentation/codeconvtoc-136057.html">Code Conventions for the Java Programming Language</a> from Oracle. Google also has <a href="https://code.google.com/p/google-styleguide/">style guides</a> for other languages like C++, Objective-C, Python, Shell, HTML/CSS, JavaScript, and Lisp. </p><br><br><br><br><br><br></body></html>
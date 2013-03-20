<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Xtend 2.4 Adds Active Annotations, Android Support and More</h3><p>Today, the Eclipse Foundation announced the release of <a href="http://www.eclipse.org/xtend/">Xtend 2.4</a>, a statically-typed Java-esque programming language that compiles down to Java and runs on the JVM (and JVM like systems such as Android).</p> 
<p>Unlike other JVM-based compiled languages such as Scala and Kotlin, Xtend is translated to Java source and then compiled with the standard Java compiler, so there are no backward compatibility issues with the resulting output.</p> 
<p>Xtend differs from interpreted languages such as Groovy and JRuby/Jython in that the language is statically typed but has type inference to support simple coding, which means refactorings and type-specific completions are possible in the IDE.</p> 
<p>InfoQ covered the <a href="http://www.infoq.com/news/2012/06/xtend-release-10;jsessionid=9B0EF572666163B70F1B33A7D96CBC13">1.0 release</a> last year, but a lot has changed in the interim. The <a href="http://www.eclipse.org/xtend/release_notes_2_4_0.html">new features in 2.4</a> include active annotations, collection literals, Android support and improved refactoring and content assist in the tooling.</p> 
<p>InfoQ caught up with Sven Efftinge, project lead of Xtend, to find out more about the release, and started by asking:</p> 
<p><b>InfoQ</b>: One of the new features in Xtend 2.4 is the addition of active annotations. Can you explain what they are, and how they cut down on boilerplate code?</p> 
<blockquote> 
 <p><b>Sven Efftinge</b>: You basically declare an annotation and tell the compiler how annotated elements should be translated to Java code. Typical use cases are generating getters and setters, observers or other common design patterns such as visitors – but you can do much more with them. We've focussed on making it super easy to develop and deploy active annotations.</p> 
 <p>As an example, consider the JavaBean pattern for properties. This requires the creation of a get/set method pair, which contributes to what some refer to as 'Java code bloat'. In Xtend, you just need to declare that your field should be a property and Xtend does the rest:</p> 
 <pre>
@Property String name
</pre> 
 <p>This is translated into the following Java code:</p> 
 <pre>
private String name;
public String getName() {
  return this.name;
}
public void setName(String name) {
  this.name = name;
}
</pre> 
 <p>There are other annotations, such as <code>@Data</code>, which generates <code>hashCode()</code> and <code>equals()</code> for you automatically, and <code>@Observable</code> which can be applied to a data class to get automatic support for property change listeners, as described in <a href="http://www.eclipse.org/xtend/release_notes_2_4_0.html#active_annotations">the release notes</a>.
  <!--?p--></p> 
 <p>The coolest thing is that the IDE and the compiler are aware of your changes. So all the typing, linking as well as stuff like navigation and content assist just work as expected, as changes are applied on the fly.</p> 
 <p>It's how code generation should be.</p> 
</blockquote> 
<p><b>InfoQ</b>: Another new feature is that of literal collections. What is the syntax for using literal arrays, sets and maps? Can these be nested?</p> 
<blockquote> 
 <p><b>Sven Efftinge</b>: The syntax is a hash followed by either curly braces or squared brackets. For lists you use:</p> 
 <pre>
val myList = #[1,2,3,4]
</pre> 
 <p>And for sets it is:</p> 
 <pre>
val mySet = #{1,2,3}
</pre> 
 <p>Maps are created using the tuple operator:</p> 
 <pre>
val mySet = #{1-&gt;&quot;one&quot;,2-&gt;&quot;two&quot; }
</pre> 
 <p>The list literal can also be used as an array literal when the expected type is an array, as in:</p> 
 <pre>
val int[] myArray = #[1,2,3,4]
</pre> 
 <p>And yes, they can be nested as they are just expressions.</p> 
</blockquote> 
<p><b>InfoQ</b>: Are literal collection types mutable or immutable? How can you seed a mutable collection with a literal one?</p> 
<blockquote> 
 <p><b>Sven Efftinge</b>: Yes, they are immutable. If you want a mutable one you use one of the factory methods:</p> 
 <pre>
val myArrayList = newArrayList(1,2,3,4)
</pre> 
 <p>Of course you can also construct them with existing immutable lists.</p> 
</blockquote> 
<p><b>InfoQ</b>: Speaking of literals, what are extension providers and how do they compare to extension methods?</p> 
<blockquote> 
 <p><b>Sven Efftinge</b>: Extension providers are objects on the scope of your program which provide extension methods. This is best explained by example. Consider you have a Data Access Object (DAO) class, with methods like <code>save(Entity)</code>.</p> 
 <p>In Java you have to write:</p> 
 <pre>
myDao.save(myEntity)
</pre> 
 <p>In Xtend you could make the DAO object an extension provider which lets you use its methods as member methods on their first argument type. So instead you can write:</p> 
 <pre>
myEntity.save()
</pre> 
 <p>This is an important enhancement over C# extension methods (where only static methods can be used as extensions). Extension providers let you exchange the actual implementation easily.</p> 
</blockquote> 
<p><b>InfoQ</b>: JDK 8 has the concept of converting Lambdas into Single Access Method (SAM) types. Is this possible on Java 6 or Java 7 with Xtend today?</p> 
<blockquote> 
 <p><b>Sven Efftinge</b>: In JDK8 lambdas can only be converted to so called functional interfaces. This is done in Xtend in the same way. The new addition is that you can now also use abstract classes with a SAM type. They are frequently used by frameworks such as &quot;Functional Java&quot;.</p> 
 <p>With Xtend, you don't need to wait for JDK8 to be able to do this; you can do it in Java 6 or Java 7 today. In fact, Xtend is compatible with Java 5.</p> 
</blockquote> 
<p><b>InfoQ</b>: Speaking of backward compatibility, what's the story with Xtend? Can programs compiled against Xtend 1.0 still be used against Xtend 2.4 today?</p> 
<blockquote> 
 <p><b>Sven Efftinge</b>: They are binary compatible, so programs compiled against Xtend 1.0 will work with Xtend 2.4 without any recompilation or changes needed.</p> 
 <p>At the source level there are no breaking changes, although we have improved the compiler's error reporting which can highlight semantic errors where before the compiler wouldn't have warned you.</p> 
 <p>We take compatibility seriously, both at the compiled level and at the source level.</p> 
</blockquote> 
<p><b>InfoQ</b>: Being able to compile Xtend projects and install onto Android seems like a great win for the framework. Given that compiling Android applications with Scala or Kotlin add many megabytes to the package, what is the average size increase of compiling an Android application with Xtend versus coding directly in Java?</p> 
<blockquote> 
 <p><b>Sven Efftinge</b>: Xtend compiles to Java source code which in turn is compiled to Java byte code. This ensures that the created byte code works nicely with Android. Also Xtend doesn't have its own fat library. There are only a couple of classes adding extension methods to existing JDK types (&lt;40K) and Google Guava, which is 1.3M.</p> 
 <p>You can write pretty efficient Android apps with Xtend.</p> 
</blockquote> 
<p><b>InfoQ</b>: One of the success criteria for a language is that it has excellent IDE support. How is Xtend's support in Eclipse evolving?</p> 
<blockquote> 
 <p><b>Sven Efftinge</b>: The IDE has many new features like formatter, new quick fixes, new refactorings and much improved content assist.</p> 
 <p>Also the compiler performance has been improved a lot, too. We have a strong focus on enabling a good flow when working with Xtend and the IDE.</p> 
 <p>Unlike other JVM based languages, Xtend works with rather than against the JDT. You don't need to replace the JDT or enable weaving to use it. In addition, you can use any version of the Java compiler to be able to compile the project; you're not limited to just the version installed as the plug-in.</p> 
</blockquote> 
<p>Xtend 2.4 is available for <a href="http://www.eclipse.org/xtend/download.html&gt;download&lt;/a&gt;, as are the &lt;a href=" www.eclipse.org="" xtend="">release notes for 2.4</a>. For more information on Xtend, see the <a href="http://www.eclipse.org/xtend/">Xtend</a> home page.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
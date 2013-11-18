<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>An Interview with Greg Finzer of Compare .NET Objects</h3><p>Writing code to compare objects can be tedious, especially when dealing with large objects or deep graphs. And when the classes change errors often slip in. One way to reduce the potential for error is to rely on a library such as Greg Finzer’s <a href="http://comparenetobjects.codeplex.com/">Compare .NET Objects</a>. This library offer reasonable performance for up to 10,000 objects.</p>
<p>InfoQ: What first inspired you to create the Compare .NET Objects library?</p>
<blockquote> 
 <p>When Microsoft Released the Developer Tools for Windows Phone 7 there was a great outcry on the Windows Phone 7 forums against Microsoft for not providing a database. I decided that this would be a great opportunity to create a database for Windows Phone 7 since there was no competition and there was clear demand. I had always wanted to create an object database to bypass years of pain dealing with ORMs. Back then Windows Phone 7 only allowed a maximum of 90MB for application data. The data needed to be saved in the least space possible, even smaller than JSON. I found out early on that no binary serializer was available in the .NET Framework for Windows Phone 7. There was an open source binary serializer on CodePlex: https://slserializelzo.codeplex.com/. I signed up to be the tester on that project. Rather than writing several hundred reflection tests by hand, I created Compare .NET Objects to verify the serialization/deserialization. In the end, we didn’t leverage the CodePlex serialization library to create Ninja Database Pro. However we did use Compare .NET Objects for all the integration tests for our own binary serializer. I spun off Compare .NET Objects into its own open source project as a benefit for the developer community.</p> 
</blockquote>
<p>InfoQ: What other ways do you see people using your library?</p>
<blockquote> 
 <p>I think Compare .NET Objects is well suited for writing integration tests to verify ORM mappings. I work for Sogeti for my day job. I used Compare .NET Objects this past year in integration tests for a project at Office of Aviation for the State of Ohio. On that project we used Compare .NET Objects to verify Spring Framework .NET mappings. I have seen other people using Compare .NET Objects to determine if an object is dirty and needs to be saved to a database, for auditing purposes, and in power shell scripts.</p> 
</blockquote>
<p>InfoQ: Do you support any other .NET platforms (e.g. Windows Phone, Windows Store)?</p>
<blockquote> 
 <p>There is a compiler constant for Silverlight in the code so it should work with Windows Phone and Silverlight. I haven’t looked at making it compatible with Windows Store yet. Eventually I plan to make separate projects and builds for each of the different platforms similar to what I have done with our commercial products.</p> 
</blockquote>
<p>InfoQ: If there anything that Compare .NET Objects not do that you want to add?</p>
<blockquote> 
 <p>Although people have sent me emails thanking me that it is a single class, I think it is time to refactor Compare .NET Objects into more maintainable classes. After years of adding features, it has a lot of code smells. It definitely violates S.O.L.I.D. design principles especially SRP. There has also been a great deal of merge pain caused by having everything all in one class. I would like to add a thread safe option while maintaining backward compatibility.</p> 
</blockquote>
<p>InfoQ: Do you find that the use of reflection causes performance problems? If so, what have you done to mitigate it?</p>
<blockquote> 
 <p>As much as people harp on reflection causing performance problems, I have never actually seen a large impact. I think back to a project where a client asked for 9000 items to be loaded into a drop down on a web page. It took 20 seconds to load the drop down. We used NHibernate to load the data from an Oracle database. NHibernate uses reflection. So where was the performance problem? The database? NHibernate? Internet Explorer? No, the performance problem was the network bandwidth. We ended up implementing an Ajax autocomplete dropdown loading only 20 at a time. If you are dealing with large numbers of objects, reflection will be the least of your worries comparatively.</p> 
</blockquote>
<blockquote> 
 <p>I have added reflection caching in Compare .NET Objects which does help with the performance. See the CachingTest in the test project. On my machine with reflection caching disabled it takes 319 milliseconds to compare 10,000 objects. With reflection caching enabled it takes 224 milliseconds. I would say that if you are comparing more than 10,000 objects at once, I would not use Compare .NET Objects. In that case I would override Equals and GetHashCode for those classes.</p> 
</blockquote>
<p>InfoQ: Are you currently looking for volunteers to work on Compare .NET Objects?</p>
<blockquote> 
 <p>Sure. There is a lot of work to do:</p> 
 <ul> 
  <li>Refactor comparers into separate classes for each type</li> 
  <li>Thread safe configuration and comparison</li> 
  <li>Separate projects for each platform: Mono, Silverlight, Windows Phone, Windows Store</li> 
 </ul> 
</blockquote><br><br><br><br><br><br></body></html>
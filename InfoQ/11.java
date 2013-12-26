<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Oracle Tunes Java's Internal String Representation</h3><p>&nbsp;In an ongoing effort to improve Java performance, Oracle has announced a change in the internal representation of strings in the String class as of Java 1.7.0_06.</p>
<p class="MsoNormal">
 <o:p></o:p></p>
<p class="MsoNormal">The change, removing two non-static fields from the underlying String implementation, was done to help prevent memory leaks. 
 <o:p></o:p></p>
<p class="MsoNormal">The original String implementation is based on four non-static fields. The first is char[] value, which contains the characters comprising the String. The second is int offset which holds the index of the first character from the value array. The third is int count storing the number of characters to be used. Fourth is int hash, which holds a cached value of the String hash code.
 <o:p></o:p></p>
<p class="MsoNormal">Oracle reported that a performance issue could arise in the original implementation when a String is created using the String.substring() call. Substring() is called internally by many other API calls like Pattern.split(). When String.substring() is called, it refers to the internal char[] value from the original String characters. 
 <o:p></o:p></p>
<p class="MsoNormal">The previous implementation was designed that way in order to produce a memory savings, since the substring would still refer to the original character data. In addition String.substring() would run in constant time (O (1)) unlike the new implementation that runs in linear (O(n)) time. 
 <o:p></o:p></p>
<p class="MsoNormal">However the old implementation had the possibility of producing a memory leak in cases where an application would extract a small String from an originally large String and then discard the original String. In such a scenario, a live reference to the underlying original large char [] value from the original String is still retained, holding on to possibly many unused bytes of data.
 <o:p></o:p></p>
<p class="MsoNormal">To avoid this situation in earlier versions, Oracle suggests calling the new String(String) constructor on the small String. That API copies only the required section of the underlying char[] thereby unlinking the new smaller String from the original large parent String.
 <o:p></o:p></p>
<p class="MsoNormal">In the new paradigm, the String offset and count fields have been removed, so substrings no longer share the underlying char [] value.
 <o:p></o:p></p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>More on Indexes in In-Memory OLTP</h3><p>Indexes in SQL Server’s In-Memory OLTP don’t work exactly like normal indexes. This isn’t necessarily a bad thing, but the differences need to be kept in mind to avoid performance problems.</p>
<p>Memory-optimized non-clustered indexes differ from disc-based non-clustered indexes in that they are always covering. You don’t need to specify which columns you want to include, “all columns are virtually included” in addition to the actual index columns.</p>
<p>An interesting limitation of non-clustered indexes is that they can only be scanned in one direction. For example, if your index is &quot;OrderDate ASC” then you cannot use the index to retrieve rows based on the order date in descending order.</p>
<p>Another new type of index is the memory-optimized hash. This type of index is designed for “point-lookup operations” and full scans. It cannot be used for ordered scans or inequality seek operations. Microsoft has these <a href="http://blogs.technet.com/b/dataplatforminsider/archive/2013/11/12/sql-server-2014-in-memory-oltp-nonclustered-indexes-for-memory-optimized-tables.aspx">guidelines for choosing between non-clustered and hash indexes</a>,</p>
<blockquote> 
 <ul> 
  <li>If you need to perform only point lookups, meaning you need to retrieve only the rows corresponding to a single index key value, use a hash index.</li> 
  <li>If you need to retrieve ranges of rows, or need to retrieve the rows in a particular sort-order, use a nonclustered index.</li> 
  <li>If you need to do both, particularly if point lookups are frequent, you can consider creating two indexes: it is possible to create both a hash and a nonclustered index with the same index key.</li> 
 </ul> 
</blockquote>
<p>Hash indexes also require the use of a <a href="http://msdn.microsoft.com/en-us/library/dn494956(v=sql.120).aspx">bucket count</a>. The bucket count should be set between N and 2N where N is the expected number of rows. Operationally a range of 0.2N and 5N is considered to be “usable”. Internally bucket counts are always rounded up to the next power of 2.</p>
<p>High than necessary bucket counts are wasteful for memory, which is a sensitive issue when talking about memory optimized tables that must fit entirely in RAM. A bucket count that is too low causes other problems,</p>
<blockquote> 
 <p>If the bucket count is significantly (ten times) lower than the number of unique index keys, there will be many buckets that have multiple index keys. This degrades performance of most DML operations, particularly point lookups (lookups of individual index keys). For example, you may see poor performance of SELECT queries and UPDATE and DELETE operations with equality predicates matching the index key columns in the WHERE clause.</p> 
</blockquote>
<p>Another problem that can occur with hash indexes is duplicate values. If multiple rows have the same value for the index column(s) then naturally there is going to be a hash collision for those rows. If this happens a lot, say more than ten times per distinct value, then performance can suffer.</p>
<p>For hash indexes the recommendation from the <a href="http://blogs.technet.com/b/dataplatforminsider/archive/2014/01/30/in-memory-oltp-index-troubleshooting-part-ii.aspx">SQL Server team</a> is to convert the hash index into a non-clustered index.</p>
<blockquote> 
 <p>In most cases you will want to use a NONCLUSTERED index instead, as NONCLUSTERED indexes generally perform better in case of duplicates. If you go for this option, consider uniquifying the index key, as indicated below.</p> 
 <p>For NONCLUSTERED indexes with a lot of duplicates, consider adding additional columns to the index key. For example, you can add the primary key columns to the index key to make it unique, in other words to uniquify the index.</p> 
</blockquote>
<p>If the values actually are distinct and you want to continue using a hash index, then you can “over-size the index” by using a bucket count that is “20 – 100 times the number of unique index key values” to reduce the chance of hash collisions.</p><br><br><br><br><br><br></body></html>
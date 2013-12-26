<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>ORMs e a Ignorância da Persistência</h3><p><a href="http://www.google.com/url?q=http%3A%2F%2Fthedatafarm.com%2Fblog%2Fabout-me%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNFV6bnN1QRXGn4t7XCzWaV5e7Bz2g">Julie Lerman</a> notou recentemente que o Entity Framework pode trabalhar <a href="http://thedatafarm.com/blog/data-access/entity-framework-private-constructors-and-private-setters/">possuindo construtores e setters privados</a>.</p>
<p>No <a href="https://github.com/julielerman/EF_and_Private_CTORs_n_Setters">teste</a> publicado por Julie, pode-se ver que o Entity Framework (EF) &eacute; capaz de popular uma propriedade com setters privados e invocar um construtor privado sem grandes dificuldades. &Eacute; poss&iacute;vel observar como o EF realiza esta tarefa se referindo ao <a href="http://entityframework.codeplex.com/SourceControl/latest#src/EntityFramework/Core/Objects/Internal/EntityProxyFactory.cs">EntityProxyFactory</a> e classes relacionadas, mas na ess&ecirc;ncia, trata-se de uma combina&ccedil;&atilde;o de reflection e IL Emits. O NHibernate ainda vai um passo al&eacute;m ao suportar <a href="https://github.com/nhibernate/nhibernate-core/blob/master/src/NHibernate.Test/PropertyTest/FieldAccessorFixture.cs">acesso a atributos privados</a> (o que tamb&eacute;m j&aacute; sendo discutido para o EF). No entanto, atualmente ambos obrigam a exist&ecirc;ncia de um construtor padr&atilde;o (mesmo que este n&atilde;o seja p&uacute;blico).</p>
<p>&nbsp;De forma geral esta dire&ccedil;&atilde;o &eacute; boa pois, como Julie comenta, isso <a href="http://gorodinski.com/blog/2012/08/10/toward-persistence-ignorance-with-nhibernate-in-domain-driven-design/">promove</a> <a href="http://stackoverflow.com/a/906094/297964">ignor&acirc;ncia da persist&ecirc;ncia</a>. De forma arquitetural, tanto o Entity Framework quanto o NHibernate suportam estes padr&otilde;es que auxiliam a alcan&ccedil;ar a ignor&acirc;ncia da persist&ecirc;ncia:</p>
<ul class="c13 lst-kix_65mlc1p19goj-0 start"> 
 <li><a href="http://soren.skovsboll.com/2008/10/using-repository-pattern-to-achieve.html">Reposit&oacute;rio;</a></li> 
 <li><a href="http://msdn.microsoft.com/en-us/magazine/dd882510.aspx">Unidade de trabalho</a>.</li> 
</ul>
<p>O Entity framework possui respectivamente o <a href="http://msdn.microsoft.com/en-us/library/system.data.entity.dbset%28v=vs.103%29.aspx">DBSet</a> e o <a href="http://msdn.microsoft.com/en-us/library/system.data.entity.dbcontext%28v=vs.103%29.aspx">DBContext</a>, enquanto o NHibernate possui a API de <a href="http://nhforge.org/blogs/nhibernate/archive/2009/12/17/queryover-in-nh-3-0.aspx">QueryOver</a> e o <a href="http://nhforge.org/wikis/reference2-0en/context-sessions.aspx">SessionContext</a>. Apesar disso, para suportar lazy loading, atualmente ambos tamb&eacute;m suportam o padr&atilde;o <a href="http://en.wikipedia.org/wiki/Proxy_pattern">virtual proxy</a> que contraria esse princ&iacute;pio (exigindo que as propriedades sejam marcadas como <em>virtual</em>).</p>
<p>A ignor&acirc;ncia da persist&ecirc;ncia &eacute; geralmente considerada como boa pr&aacute;tica; regras de neg&oacute;cio podem ser isoladas da l&oacute;gica de persist&ecirc;ncia, ao contr&aacute;rio de quando se utiliza o padr&atilde;o <a href="http://en.wikipedia.org/wiki/Active_record_pattern">Active Record</a>. Esta caracter&iacute;stica mant&eacute;m seu design mais simples e mais test&aacute;vel.</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Planos futuros para o C#</h3><p>No <a href="http://ndc-london.com/">NDC Londres</a>, Mads Torgersen, membro do time de design do C#, prop&ocirc;s mudan&ccedil;as para a linguagem C#. Deve ser ressaltado que s&atilde;o apenas propostas e que n&atilde;o existem garantias de que ir&atilde;o aparecer em alguma vers&atilde;o espec&iacute;fica da linguagem. <a href="http://damieng.com/blog/2013/12/09/probable-c-6-0-features-illustrated">Damien Guard</a> postou um resumo e uma breve an&aacute;lise dessas propostas e aqui v&atilde;o alguns dos principais t&oacute;picos.</p>
<h2>Propriedades somente leitura</h2>
<p>Propriedades somente leitura v&atilde;o permitir que desenvolvedores declarem propriedades e os valores que elas armazenam em uma &uacute;nica linha.</p>
<pre>

<p>public int X { get; } = x;</p>

</pre>
<h2>&nbsp;</h2>
<h2>Uso de tipos est&aacute;ticos</h2>
<p>Visual Basic e Java j&aacute; permitem que desenvolvedores importem m&oacute;dulos (classes est&aacute;ticas em C#) no namespace. Isso permite remover c&oacute;digos repetitivos como &quot;Math.&quot; na frente de fun&ccedil;&otilde;es comumente utilizadas.</p>
<h2>Construtores prim&aacute;rios</h2>
<p>Colocando par&acirc;metros ap&oacute;s o nome da classe, os desenvolvedores n&atilde;o precisar&atilde;o explicitamente criar construtores. Isso elimina a necessidade de copiar os valores dos par&acirc;metros dos construtores nos campos privados.</p>
<pre>

<p>public class Point(int x, int y) {</p>

<p>private int x, y;</p>

<p>}</p>

</pre>
<h2>Express&otilde;es de propriedade e m&eacute;todo</h2>
<p>Express&otilde;es de propriedade eliminariam alguns clich&ecirc;s necess&aacute;rios para propriedades somente leitura.</p>
<pre>

<p>public double Distance =&gt; Math.Sqrt((X * X) + (Y * Y));</p>

</pre>
<p>Propriedades de m&eacute;todo fariam o mesmo, exceto que obviamente aceitariam par&acirc;metros.</p>
<p>Perceba que propriedades parametrizadas ainda n&atilde;o est&atilde;o sendo consideradas. Para um futuro pr&oacute;ximo, isso continua sendo uma funcionalidade apenas do VB.</p>
<h2>Par&acirc;metros de fun&ccedil;&atilde;o</h2>
<p>Nos dias de hoje, a maioria dos desenvolvedores n&atilde;o utilizam arrays, exceto quando precisam para a palavra-chave params. Assim, uma proposta &eacute; que a interface IEnumerable&lt;T&gt; tamb&eacute;m suporte params. Se isso for feito, outras linguagens como Visual Basic tamb&eacute;m precisariam dar suporte &agrave; essa funcionalidade.</p>
<p>Outra proposta &eacute; permitir que vari&aacute;veis locais sejam declaradas utilizando a palavra chave out. Por exemplo,</p>
<pre>

<p>int.TryParse(&quot;123&quot;, out int x);</p>

</pre>
<h2>Propaga&ccedil;&atilde;o de null</h2>
<p>Quando est&atilde;o trabalhando com dados confusos, os desenvolvedores freq&uuml;entemente precisam escrever uma s&eacute;rie de valida&ccedil;&otilde;es de nulo antes de ler uma propriedade ou invocar um m&eacute;todo. A sintaxe ?. eliminaria a necessidade de valida&ccedil;&atilde;o, invocando o m&eacute;todo se o valor que a procede n&atilde;o for nulo.</p>
<pre>

<p>var bestValue = points?.FirstOrDefault()?.X;</p>

</pre>
<p>Nesse caso, se points for nulo, ou points.FirstOrDefault() retornar nulo, ent&atilde;o .X &eacute; ignorado e a express&atilde;o retorna nulo. Isso pode ser encadeado com ?? para fornecer um valor padr&atilde;o alternativo.</p>
<pre>

<p>var bestValue = points?.FirstOrDefault()?.X ?? -1;</p>

</pre>
<p>Essa sem&acirc;ntica &eacute; encontrada em linguagens de &quot;passagem de mensagens&quot;, como Objective-C e Smalltalk. &Eacute; comumente citada como sendo problem&aacute;tica porque o que poderia ser uma exce&ccedil;&atilde;o de refer&ecirc;ncia nula, &eacute; silenciosamente ignorada.</p>
<p>Por fim, essas propostas de novas funcionalidades para o C# ajudariam a diminuir o ru&iacute;do e a repeti&ccedil;&atilde;o de c&oacute;digo, mas ainda precisam ser melhor estudadas e detalhadas para uma an&aacute;lise mais concreta dos pr&oacute;s e contras de cada abordagem.</p><br><br><br><br><br><br></body></html>
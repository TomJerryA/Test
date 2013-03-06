<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>JSONiq: A linguagem de consulta em JSON</h3><p>A <a href="http://jsoniq.org/index.html">JSONiq</a> &eacute; uma nova linguagem de consulta baseada em XQuery. De forma semelhante &agrave; SQL ou LINQ, a nova linguagem apresenta conceitos de suporte sint&aacute;tico como: let, for, where, group by e select. Vejamos um exemplo:</p> 
<pre>
let $stats := db:find(&quot;stats&quot;)
for $access in $stats
where $access(&quot;response_time&quot;) &gt; 5
group by $url := $access(&quot;url&quot;)
return
{
    &quot;url&quot;: $url,
    &quot;avg&quot;: avg($access(&quot;response_time&quot;)),
    &quot;hits&quot;: count($access)
}
</pre> 
<p>A linguagem JSONiq suporta mais que apenas transforma&ccedil;&otilde;es de JSON para JSON. Pode-se us&aacute;-la para gerar ou fazer <em>parser</em> de XML, e at&eacute; criar consultas que combinem as duas opera&ccedil;&otilde;es. Neste <a href="http://jsoniq.org/docs/use-cases/en-US/html/ch01.html#html.example">exemplo da documenta&ccedil;&atilde;o</a>, podemos ver a JSONiq sendo utilizada como linguagem de template para gerar tabelas HTML.</p> 
<p><img src="/resource/news/2013/03/JSONiq/pt/resources/6image00.png;jsessionid=A2BEA1B054C4154DD371CA710AAD463C" alt="" _href="img://6image00.png" _p="true" /></p> 
<p>Semelhante &agrave; linguagem XQuery, a JSONiq suporta janelas sobrepostas e n&atilde;o-sobrepostas. Esta funcionalidade &eacute; usada para quebrar os dados em partes de tamanho iguais, ou para que sejam usados em c&aacute;lculos estat&iacute;sticos, como as tr&ecirc;s &uacute;ltimas m&eacute;dias. Pode-se aprender mais sobre janelas em cascata e deslizantes na <a href="http://www.w3.org/TR/2008/WD-xquery-11-20080711/#id-windows">especifica&ccedil;&atilde;o da XPath</a>.</p> 
<p>Outra caracter&iacute;stica da JSONiq &eacute; a sua capacidade de atualizar dados em formato JSON. <a href="http://jsoniq.org/docs/use-cases/en-US/html/ch01.html#update.example">Neste exemplo</a>, pode-se observar a propriedade <em>status</em> sendo adicionada nos registros em que nome &quot;Deadbeat Jim&quot; incide.</p> 
<p><img src="/resource/news/2013/03/JSONiq/pt/resources/image01.png;jsessionid=A2BEA1B054C4154DD371CA710AAD463C" alt="" _href="img://image01.png" _p="true" /></p> 
<p>A JSONiq est&aacute; dispon&iacute;vel como parte do processador Zorba XQuery, que &eacute; distribu&iacute;do sob a licen&ccedil;a Apache 2. J&aacute; a JSONiq baseia-se na licen&ccedil;a <a href="http://creativecommons.org/licenses/by-sa/3.0/deed.pt">Atribui&ccedil;&atilde;o-CompartilhaIgual 3.0 N&atilde;o Adaptada</a>.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
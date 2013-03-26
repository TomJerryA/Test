<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Wikimedia adota geração de templates baseada em Lua</h3><p>A Wikimedia <a href="https://blog.wikimedia.org/2013/03/11/lua-templates-faster-more-flexible-pages/">adotou</a> a linguagem de programa&ccedil;&atilde;o <a href="http://www.lua.org/portugues.html">Lua</a> para gera&ccedil;&atilde;o dos templates de p&aacute;ginas utilizados em diversos sites como o Wikipedia em ingl&ecirc;s. A altera&ccedil;&atilde;o tem como finalidade facilitar a cria&ccedil;&atilde;o de templates e a utiliza&ccedil;&atilde;o de tabelas, caixas de informa&ccedil;&otilde;es e outros componentes utilizados na plataforma <a href="https://www.mediawiki.org/wiki/MediaWiki">MediaWiki</a> (a base da Wikipedia e de muitos projetos e <a href="http://wikistats.wmflabs.org/display.php?t=mw">empresas</a>).</p> 
<p>Sumana Harihareswara, gerente de engenharia da comunidade da Wikimedia, <a href="http://www.google.com/url?q=https%3A%2F%2Fblog.wikimedia.org%2F2013%2F03%2F14%2Fwhat-lua-scripting-means-wikimedia-open-source%2F&amp;sa=D&amp;sntz=1&amp;usg=AFQjCNEvCplNiVd6XjA3PWGxhipau2515Q">resumiu</a> os problemas relacionados aos templates das p&aacute;ginas, que motivaram a mudan&ccedil;a:</p> 
<blockquote> 
 <p>Quando come&ccedil;amos a procurar a causa da lentid&atilde;o no carregamento das p&aacute;ginas alguns anos atr&aacute;s, vimos que as CPUs passavam muito tempo interpretando os templates. ... Como nunca planejamos usar o wikitext, as tags de marca&ccedil;&atilde;o do MediaWiki, como uma linguagem de programa&ccedil;&atilde;o, os templates ficaram ineficientes e complexos, sem poder contar com o uso de recurs&otilde;es e loops, e com performance terr&iacute;vel.</p> 
</blockquote> 
<p>Foi criada uma extens&atilde;o que facilita a cria&ccedil;&atilde;o dos templates:</p> 
<blockquote> 
 <p>Nossa equipe e volunt&aacute;rios trabalharam no <a href="https://www.mediawiki.org/wiki/Extension:Scribunto">Scribunto</a> (que em Latin significa &quot;eles escreveram&quot;), uma extens&atilde;o do MediaWiki que permitir aos editores adicionarem scripts Lua ao inv&eacute;s de wikitext nos templates.</p> 
</blockquote> 
<p>Atualmente, o Scribunto suporta apenas o uso da linguagem Lua, e atrav&eacute;s da nova extens&atilde;o, a Wikimedia espera facilitar a gera&ccedil;&atilde;o de novos templates e melhorar a performance principalmente de c&aacute;lculos matem&aacute;ticos, e da manipula&ccedil;&atilde;o e convers&atilde;o de strings e de &aacute;rvores de decis&atilde;o.</p> 
<p>Os scripts em Lua ser&atilde;o armazenados como m&oacute;dulos com o namespace Module e podem conter diversas fun&ccedil;&otilde;es que podem ser chamadas atrav&eacute;s da seguinte sintaxe:</p> 
<pre>
{{#invoke: Module_name | function_name | arg1 | arg2 | arg3 ... }}
</pre> 
<p>Um <a href="https://en.wikipedia.org/wiki/Template%3ALua_hello_world">exemplo de template &quot;ol&aacute; mundo&quot; com Lua</a> dispon&iacute;vel no site do Wikipedia e mostra como chamar a fun&ccedil;&atilde;o &quot;hello&quot; do m&oacute;dulo &quot;bananas&quot;:</p> 
<pre>
{{#invoke:bananas|hello}}
</pre> 
<p>Para mais informa&ccedil;&otilde;es confira o <a href="https://www.mediawiki.org/wiki/Extension:Scribunto/Lua_reference_manual">manual</a> disponibilizado pela Wikimedia, que mostra como criar os templates com Lua utilizando as bibliotecas b&aacute;sicas e o Scribunto.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
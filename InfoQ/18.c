<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Modern C++ e o Visual Studio</h3><p>Herb Sutter deu uma palestra sobre o status do <a href="http://channel9.msdn.com/Events/Build/2014/2-661">Modern C++</a> durante a confer&ecirc;ncia Microsoft Build. O C++ passa por uma esp&eacute;cie de renascimento nesses &uacute;ltimos anos na Microsoft, e Sutter tem participado diretamente desse aumento de foco.</p>
<p><strong>Pr&oacute;ximas</strong> <strong>vers&otilde;es do C++</strong></p>
<p>Sutter come&ccedil;ou sua palestra fornecendo um r&aacute;pido resumo de como est&atilde;o os padr&otilde;es ISO do C++ no momento. Em Fevereiro completou-se a discuss&atilde;o t&eacute;cnica para o C++ 14, e o comit&ecirc; est&aacute; revendo o processo com a inten&ccedil;&atilde;o de votar na aprova&ccedil;&atilde;o desse padr&atilde;o para ser o padr&atilde;o oficial ISO ainda este ano.</p>
<p>O release C++14 &eacute; considerado um <i>minor release</i>, enquanto que o pr&oacute;ximo padr&atilde;o C++17 (ainda em projeto e em discuss&otilde;es) &eacute; considerado um <i>major release</i>. A vers&atilde;o mais recente do compilador Microsoft (CTP) foi liberada em Novembro. De acordo com Sutter, o pr&oacute;ximo CTP (data ainda n&atilde;o definida) dever&aacute; conter as seguintes caracter&iacute;sticas:</p>
<blockquote> 
 <ul class="c10 lst-kix_b58776h0l2no-0 start"> 
  <li>Literais user-defined;</li> 
  <li>C++14 generalized lambda capture;</li> 
  <li>C++14 libs: std:: literais user-defined;</li> 
  <li>Inline namespaces.</li> 
 </ul> 
</blockquote>
<p>Existem ainda algumas caracter&iacute;sticas que podem estar presentes neste CTP (o que significa que podem ser adiadas para uma vers&atilde;o posterior):</p>
<blockquote> 
 <ul class="c10 lst-kix_vpoakfbycin2-0 start"> 
  <li>Universal character names nas literais;</li> 
  <li>noexcept (incl. conditional);</li> 
  <li>char16_t, char32_t, attributes;</li> 
  <li>thread_local;</li> 
  <li>unrestricted unions;</li> 
  <li>consexpr (except ctors, literal types);</li> 
  <li>constexpr (incl. ctors, literal types).</li> 
 </ul> 
</blockquote>
<p>O Parallel STL (a converg&ecirc;ncia de PPL, TBB, Amp, CUDA, Thrust) foi lan&ccedil;ado no <a href="https://parallelstl.codeplex.com/">CodePlex</a>. Sutter anunciou que a confer&ecirc;ncia C++ que a Microsoft patrocinou nos &uacute;ltimos dois anos (<a href="http://channel9.msdn.com/Events/GoingNative/2013">GoingNative</a>) foi substitu&iacute;da pela <a href="http://www.cppcon.org/">CPPCon</a>, que est&aacute; programada para ocorrer de 7 a 12 de Setembro de 2014.</p>
<p><strong>Casos de uso do Modern C++</strong></p>
<p>A pr&oacute;xima parte da sua palestra migrou de discuss&otilde;es sobre lan&ccedil;amentos para uma conversa sobre os casos de uso do Modern C++ no desenvolvimento de aplica&ccedil;&otilde;es de hoje. Na opini&atilde;o de Sutter, C++ deve ser usado quando as seguintes metas ou objetivos s&atilde;o necess&aacute;rios:</p>
<blockquote> 
 <ul class="c10 lst-kix_1gx2fgnqjwj3-0 start"> 
  <li>Portabilidade e compatibilidade entre plataformas;</li> 
  <li>Alto desempenho e controle total;</li> 
  <li>Acesso total ao hardware e recursos do SO;</li> 
  <li>Destaques da linguagem C++: value types por padr&atilde;o, determinismo por padr&atilde;o, cont&iacute;guo por padr&atilde;o.</li> 
 </ul> 
</blockquote>
<p>Sutter observa que Modern C++ n&atilde;o &eacute; C++98-- Modern C++ &eacute; mais limpo e mais seguro enquanto se mant&eacute;m r&aacute;pido e flex&iacute;vel. Isso n&atilde;o quer dizer que o velho C++ n&atilde;o &eacute; suportado, como em muitos casos ele vai compilar com avisos e sugest&otilde;es do compilador de como ele pode ser melhorado.</p>
<p>Uma das caracter&iacute;sticas que o Modern C++ oferece &eacute; simplificar (da perspectiva do programador) o gerenciamento de mem&oacute;ria quando se utiliza new-&gt; make_unique ou new-&gt;make_shared. N&atilde;o h&aacute; necessidade de exclus&atilde;o, o gerenciamento do ciclo de vida &eacute; autom&aacute;tico e exception-safe.</p>
<p>Outra &aacute;rea &eacute; como values types s&atilde;o tratados de forma mais eficiente para opera&ccedil;&otilde;es de movimenta&ccedil;&atilde;o. O C++11 adicionou a ideia de mover tipos objeto. Com base nessa abordagem, existe a possibilidade de se tornar dono ao inv&eacute;s de fazer c&oacute;pias que dever&atilde;o ser exclu&iacute;das. A sem&acirc;ntica melhorada de movimenta&ccedil;&atilde;o pode melhorar a velocidade de c&oacute;digo legado simplesmente recompilando com um compilador C++14.</p>
<p><strong>Escrevendo c&oacute;digo r&aacute;pido</strong></p>
<p>Arrays cont&iacute;guos s&atilde;o importantes e muitas vezes esquecidos, se est&aacute; percorrendo muitos objetos, ent&atilde;o &eacute; muito importante orden&aacute;-los para fazer um acesso aos endere&ccedil;os adjacentes. Se h&aacute; uma preocupa&ccedil;&atilde;o com o desempenho ent&atilde;o &eacute; melhor usar arrays, e n&atilde;o apenas lists e arraylists.</p>
<p>Continuando nesse tema, Sutter disponibilizou benchmarks indicando que o uso de vector &eacute; muito mais eficiente que o uso de lists para inser&ccedil;&otilde;es e exclus&otilde;es. Um list pr&eacute;-alocado &eacute; mais r&aacute;pido do que um list regular, mas ambos permanecem muito piores do que o Vector.</p>
<p>A palestra de Sutter &eacute; muito informativa e ele continua sendo um orador envolvente. Consulte o site <a href="http://channel9.msdn.com/Events/Build/2014/2-661">Channel9</a> para assistir a palestra completa.</p><br><br><br><br><br><br></body></html>
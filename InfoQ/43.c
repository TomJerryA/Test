<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>CoffeeScript 1.7: encadeamento sem parênteses, Strings de múltiplas linhas e mais</h3><p>Jeremy Ashkenas liberou a <a href="https://gist.github.com/aseemk/8637896">vers&atilde;o 1.7 do CoffeeScript</a> introduzindo algumas mudan&ccedil;as que antecipam o popular conversor do JavaScript.</p>
<p>A vers&atilde;o 1.7 inclu&iacute; uma das mais populares solicita&ccedil;&otilde;es da linguagem, o suporte ao encadeamento sem par&ecirc;nteses. Antes da vers&atilde;o 1.7, se o desenvolvedor quisesse encadear fun&ccedil;&otilde;es era necess&aacute;rio o uso de par&ecirc;nteses, que n&atilde;o s&atilde;o mais obrigat&oacute;rios nas fun&ccedil;&otilde;es em CoffeeScript.</p>
<pre>
// anterior ao 1.7 - os par&ecirc;nteses s&atilde;o necess&aacute;rios no encadeamento.
$('#element').addClass('active').css({ left: 5 });

// com o 1.7 - n&atilde;o precisa de par&ecirc;nteses.
$ '#element'
.addClass 'active'
.css { left: 5 }
</pre>
<p>Essa vers&atilde;o tamb&eacute;m introduziu um suporte adequado para Strings de m&uacute;ltiplas linhas. Nas vers&otilde;es anteriores do CoffeeScript, embora as herestrings, ou strings literais, tentem preservar as linhas novas e espa&ccedil;os em branco, ignoraria o operador `\` que &eacute; usado para indicar que duas strings devem ser preservadas na mesma linha. Com a vers&atilde;o 1.7 isso foi corrigido, permitindo que o desenvolvedor possa formatar claramente m&uacute;ltiplas linhas de strings no CoffeeScript.</p>
<pre>
console.log '''The quick brown fox jumped over the \
lazy dog'''

// sa&iacute;da anterior ao 1.7.
The quick brown fox jumped \nover the lazy dog

// sa&iacute;da agora com o 1.7.
The quick brown fox jumped over the lazy dog
</pre>
<p>Tamb&eacute;m foi ampliado a desestrutura&ccedil;&atilde;o dos arrays, que foi o <a href="https://github.com/jashkenas/coffee-script/pull/3268">problema aberto de maior dura&ccedil;&atilde;o</a> no reposit&oacute;rio do CoffeeScript.</p>
<pre>
# para obter o &uacute;ltimo item do array de animais.
animals = [ 'cat', 'dog', 'hippopotamus' ]

# antes do 1.7
hippo = animals[animal.length - 1]

# a partir do 1.7
[..., hippo] = animals

# … sendo depois convertido para:
hippo = animals[animals.length - 1];
</pre>
<p>A nova conven&ccedil;&atilde;o dos operadores matem&aacute;ticos est&aacute; presente at&eacute; na fun&ccedil;&atilde;o de adi&ccedil;&atilde;o. H&aacute; o novo operador de pot&ecirc;ncia, divis&atilde;o base e operador de m&oacute;dulo (retorna o resto de uma opera&ccedil;&atilde;o de divis&atilde;o).</p>
<pre>
# elevado
2 ** 2
# transcrito para...
Math.pow(2, 2);

# divis&atilde;o
2 // 3
# transcrito para...
Math.floor(2 / 3)

# modulo
2 %% 3
# transcrito para...
var __modulo = function(a, b) { return (a % b + +b) % b; };
__modulo(2, 1);
</pre>
<p>Outras melhorias inclu&iacute;das tamb&eacute;m trazem o CoffeeScript alinhado com o Node.js, dessa forma nenhum procedimento ser&aacute; necess&aacute;rio para executar automaticamente todos os arquivos de um diret&oacute;rio, mas se comportar&aacute; como Node e somente executar&aacute; o arquivo index.coffee.</p>
<p>A maior parte do trabalho desenvolvido na vers&atilde;o 1.7 do CoffeeScript (e de fato, grande parte do CoffeeScript nos &uacute;ltimos anos) tem sido feita por membros da comunidade. Segundo Ashkenas &quot;h&aacute; mais de 100 desenvolvedores que contribuem e atualizam o CoffeeScript&quot;. &quot;Seja qual for a ado&ccedil;&atilde;o que o CoffeeScript tenha criado foi acontecendo por causa do apelo pela ideia dos programadores JavaScript&quot;. No que diz respeito ao trabalho realizado na vers&atilde;o 1.7, Ashkenas enviou <a href="https://twitter.com/jashkenas/status/428243869487362048">agradecimentos em especial</a> a <a href="https://github.com/xixixao">Michael Srb</a> pela sua contribui&ccedil;&atilde;o.</p>
<p>O CoffeeScript aprecia o fato da imensa popularidade, chegando ao ponto de ser o <a href="http://en.wikipedia.org/wiki/CoffeeScript">10&ordm; projeto mais popular do GitHub</a>. Tamb&eacute;m sendo suportado por frameworks como o Ruby on Rails (desde a vers&atilde;o 3.1), e &eacute; suportado pelo Visual Studio da Microsoft atrav&eacute;s do <a href="http://vswebessentials.com/">plugin Web Essentials</a>. Para complementar, o criador do JavaScript <a href="http://en.wikipedia.org/wiki/Brendan_Eich">Brenden Eich</a> expressou como o CoffeeScript influenciou seus pensamentos sobre <a href="https://brendaneich.com/tag/javascript-ecmascript-harmony-coffeescript/">o futuro do JavaScript</a>.</p>
<p>O usu&aacute;rio do GitHub <a href="https://gist.github.com/stefanpenner">stefanpenner</a> comentou que no CoffeeScript &quot;... a importa&ccedil;&atilde;o e exporta&ccedil;&atilde;o do ES6 ser&aacute; destruidora ...&quot;.</p>
<p>Ashkenas direcionou as funcionalidades do <a href="http://www.frontendjournal.com/javascript-es6-learn-important-features-in-a-few-minutes">ES6</a> no CoffeeScript dizendo que:</p>
<blockquote> 
 <p>O CoffeeScript est&aacute; praticamente pronto - estando muito est&aacute;vel por v&aacute;rios anos - mas continuar&aacute; a crescer em pequenos caminhos no futuro. Alguns exemplos s&atilde;o: suporte &agrave;s novas funcionalidades da linguagem JavaScript, aprimoramento no suporte a fonte de mapas, maior eleg&acirc;ncia da leitura do estilo de programa&ccedil;&atilde;o e mais simplifica&ccedil;&atilde;o nas partes internas do compilador.</p> 
</blockquote>
<p>Nesse momento, h&aacute; um <a href="https://www.kickstarter.com/projects/michaelficarra/make-a-better-coffeescript-compiler">projeto criado no Kickstarter</a> para reescrever o compilador do CoffeeScript. O projeto tem sido financiado com sucesso e foi apelidado de <a href="http://github.com/michaelficarra/CoffeeScriptRedux">CoffeeScriptRedux</a>. Ashkenas v&ecirc; a cria&ccedil;&atilde;o do novo compilador como um benef&iacute;cio para o CoffeeScript e tamb&eacute;m disse que &quot;mais compiladores determinam o sucesso de uma determinada linguagem - sendo a sa&uacute;de da linguagem. E &eacute; um beneficio para o CoffeeScript ter m&uacute;ltiplos compiladores independentes&quot;.</p>
<p>A vers&atilde;o 1.7 est&aacute; dispon&iacute;vel atrav&eacute;s do <a href="https://github.com/jashkenas/coffee-script">GitHub</a> ou <a href="http://coffeescript.org/">pelo site oficial do CoffeeScript</a>.</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Android 4.4 KitKat: Diversas novidades para os desenvolvedores</h3><p>O Google lan&ccedil;ou o Android 4.4 (KitKat) com: menor uso de mem&oacute;ria, modo de imers&atilde;o, estilos transl&uacute;cidos, impress&atilde;o da tela, diversos frameworks (impress&atilde;o, armazenamento, transi&ccedil;&otilde;es), e o Chromium WebView.</p>
<p>Como parte da iniciativa do Projeto Svelte, o Google reduziu o consumo de mem&oacute;ria em ambos os n&uacute;cleos do Android, os frameworks e os servi&ccedil;os associados, e as pr&oacute;prias aplica&ccedil;&otilde;es, fazendo o poss&iacute;vel para executar o KitKat em dispositivos de baixa capacidade com no m&iacute;nimo 512MB de mem&oacute;ria RAM, usando diversas melhorias, boas pr&aacute;ticas e ferramentas:</p>
<ul class="c6 lst-kix_ka0scoq46t1g-0 start"> 
 <li>Os fabricantes de dispositivos OEM podem usar o &quot;c&oacute;digo para ajuste fino do cache da Dalvik JIT, mesclagem de <i>kernel</i> (KSM), <i>swap</i> para o zRAM, e outras otimiza&ccedil;&otilde;es&quot; para diminuir o consumo de mem&oacute;ria;</li> 
 <li>Agora os processos do sistema consomem menos <i>heap</i>;</li> 
 <li>A mem&oacute;ria do sistema foi agressivamente mais protegida contra as aplica&ccedil;&otilde;es que consomem grandes quantidades de mem&oacute;ria;</li> 
 <li>Os servi&ccedil;os s&atilde;o lan&ccedil;ados em s&eacute;rie para evitar picos de requisi&ccedil;&otilde;es na mem&oacute;ria;</li> 
 <li>O ActivityManager.isLowRamDevice() permite que aplica&ccedil;&otilde;es fiquem atentas ao serem executadas em dispositivos com pouca quantidade de mem&oacute;ria, o que as permitem desativar algumas das funcionalidades que consomem grande quantidade de mem&oacute;ria;</li> 
 <li><a href="http://developer.android.com/training/articles/memory.html">O Gerenciamento da mem&oacute;ria da aplica&ccedil;&atilde;o</a> &eacute; um guia detalhado que conduz os desenvolvedores interessados em reduzir o consumo de mem&oacute;ria de suas aplica&ccedil;&otilde;es;</li> 
 <li>A ferramenta <a href="http://developer.android.com/about/versions/kitkat.html#44-tools">procstats</a> fornece detalhes do uso da mem&oacute;ria ao longo do tempo, incluindo o tempo de execu&ccedil;&atilde;o, fazendo a distin&ccedil;&atilde;o entre as aplica&ccedil;&otilde;es em primeiro plano e os servi&ccedil;os em <i>background</i>. A ferramenta meminfo foi aperfei&ccedil;oada para delimitar as tend&ecirc;ncias de mem&oacute;rias, e agora informa os casos de consumo de mem&oacute;ria que n&atilde;o foram relatados anteriormente.</li> 
</ul>
<p>Outra funcionalidade do Android 4.4 &eacute; o novo &quot;modo de imers&atilde;o&quot;, que permite executar as aplica&ccedil;&otilde;es usando a tela cheia, incluindo a &aacute;rea dos tr&ecirc;s bot&otilde;es (Back, Home e Menu) atrav&eacute;s do uso das <i>flags</i> View.SYTEM_UI_FLAG_IMMERSIVE e View.SYTEM_UI_FLAG_IMMERSIVE_STICKY. A &uacute;ltima <i>flag</i> esconde novamente as barras do sistema ap&oacute;s terem sido apresentadas por um curto per&iacute;odo de tempo, ao ocorrer um evento especifico. O KitKat tamb&eacute;m inclui estilos para janelas transl&uacute;cidas e temas para renderizar uma aplica&ccedil;&atilde;o na camada do topo, sobre o <i>background</i>.</p>
<p>Para criar tutoriais, demos, material para marketing, para prop&oacute;sitos de testes, entre outros; os desenvolvedores podem agora gravar toda a tela do telefone e salv&aacute;-la como um v&iacute;deo no formato MP4 atrav&eacute;s do adb shell screenrecord, ou no painel DDMS do Eclipse ou do Android Studio. Os interessados em proteger seus conte&uacute;dos para que n&atilde;o sejam gravados, podem faz&ecirc;-lo com uma chamada ao m&eacute;todo useSurfaceView.setSecure().</p>
<p>O KitKat cont&eacute;m diversos novos frameworks, tais como:</p>
<p><strong>Framework de Impress&atilde;o</strong> - fornece suporte embutido, API e caixa de di&aacute;logo de impress&atilde;o para encontrar, configurar e imprimir atrav&eacute;s do WiFi, em uma impressora local ou impress&atilde;o em nuvem, e permite a impress&atilde;o de quase &quot;qualquer tipo de documento, imagem ou arquivo&quot; a partir de todas as aplica&ccedil;&otilde;es.</p>
<p><strong>Framework para acesso ao armazenamento</strong> - integra as instala&ccedil;&otilde;es de armazenamento local ou baseadas na nuvem do usu&aacute;rio, e oferece uma maneira padronizada de acesso a documentos entre aplicativos e fornecedores de armazenagem. O fornecedor de armazenagem pode incluir um provedor de documentos em sua pr&oacute;pria aplica&ccedil;&atilde;o Android, sendo automaticamente integrado no framework quando a aplica&ccedil;&atilde;o for instalada no dispositivo, disponibilizando o servi&ccedil;o para todas as aplica&ccedil;&otilde;es. Uma aplica&ccedil;&atilde;o cliente precisa usar os novos intents CREATE_DOCUMENT ou OPEN_DOCUMENT para ter acesso as facilidades do armazenamento integrado.</p>
<p><strong>Framework de transi&ccedil;&atilde;o</strong> - os desenvolvedores podem usar este novo framework para animar as transi&ccedil;&otilde;es entre v&aacute;rias cenas das suas interfaces de usu&aacute;rio, escolhendo a transi&ccedil;&atilde;o de um conjunto predefinido de transi&ccedil;&otilde;es, ou criando as suas pr&oacute;prias anima&ccedil;&otilde;es.</p>
<p><strong>Fornecedor de SMS/MMS</strong> - padroniza&ccedil;&atilde;o na API para todas as aplica&ccedil;&otilde;es tratarem as mensagens SMS/MMS.</p>
<p>Outras funcionalidades novas ou melhoradas de destaque s&atilde;o:</p>
<p><strong>Chromium WebView</strong> - a nova WebView &eacute; feita a partir do Chromium, fornecendo suporte e melhor desempenho para os novos padr&otilde;es da web: HTML5, CSS e JavaScript. A &uacute;ltima vers&atilde;o V8 tamb&eacute;m permite a depura&ccedil;&atilde;o remota com o Chrome DevTools.</p>
<p><strong>RenderScript NDK -</strong> O RenderScript agora pode ser acessado diretamente do c&oacute;digo nativo atrav&eacute;s da API C++ NDK.</p>
<p>A <a href="http://developer.android.com/about/versions/kitkat.html">p&aacute;gina do desenvolvedor Android KitKat</a> cont&eacute;m um resumo das novas funcionalidades e melhorias, a lista &eacute; bem grande para mencionar tudo aqui. Al&eacute;m disso, o <a href="http://www.youtube.com/playlist?list=PLWz5rJ2EKKc_XOgcRukSoKKjewFJZrKV0">Android DevBytes</a> cont&eacute;m v&iacute;deos curtos voltados para desenvolvedores, apresentando algumas dessas novas funcionalidades.</p><br><br><br><br><br><br></body></html>
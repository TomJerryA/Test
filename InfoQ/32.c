<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>iOS vs Android: Resultados e opiniões sobre o desenvolvimento nas duas plataformas</h3><p>Cameron Henneke, fundador e desenvolvedor do <a href="https://www.gqueues.com/">GQueues</a>, um gerenciador de tarefas online integrado a diversos servi&ccedil;os do Google, migrou a vers&atilde;o em HTML5 de seu aplicativo m&oacute;vel para iOS e Android. Durante o processo, Henneke registrou todo o esfor&ccedil;o de desenvolvimento envolvido em ambas as plataformas e comparou os resultados em <a href="http://blog.gqueues.com/2013/07/android-vs-ios-comparing-development.html">seu blog</a>. A seguir &eacute; apresentado um resumo dos resultados obtidos e trechos de uma entrevista conduzida pelo InfoQ.com.</p>
<p><strong>Experi&ecirc;ncia pr&eacute;via</strong></p>
<p>Embora possua mais de 12 anos de experi&ecirc;ncia em desenvolvimento de software, Henneke diz que tinha pouca ou nenhuma experi&ecirc;ncia com desenvolvimento iOS e Android, fato que coloca ambas as plataformas em p&eacute; de igualdade sob sua perspectiva:</p>
<blockquote> 
 <p>Eu era absolutamente iniciante em Android quando comecei a desenvolver o aplicativo. N&atilde;o tinha nem mesmo instalado o SDK em meu computador antes de iniciar o projeto. Da mesma forma, era praticamente um novato em rela&ccedil;&atilde;o ao iOS. Em 2010 havia criado dois jogos b&aacute;sicos para iPhone, mas a complexidade de ambos n&atilde;o chegava nem perto do aplicativo GQueues, al&eacute;m de terem utilizado um conjunto de APIs completamente diferente. Depois disso n&atilde;o me envolvi mais com desenvolvimento para iOS at&eacute; come&ccedil;ar o projeto GQueues.</p> 
</blockquote>
<p><strong>Desenvolvimento</strong></p>
<p><u>Android</u></p>
<ul> 
 <li>Uma semana lendo livros, assistindo tutoriais e criando aplicativos de teste;</li> 
 <li>Uma semana para a fase inicial de design do aplicativo;</li> 
 <li>Iniciou codifica&ccedil;&atilde;o real do aplicativo que levou cerca de 870 horas.</li> 
</ul>
<p><u>iOS</u></p>
<ul> 
 <li>Duas semanas de aprendizado, na maior parte do tempo se acostumando com as <a href="http://developer.apple.com/library/ios/#documentation/DataManagement/Conceptual/iPhoneCoreData01/Introduction/Introduction.html">APIs Core Data</a>, usando o <a href="https://developer.apple.com/library/ios/#documentation/Cocoa/Reference/CoreDataFramework/Classes/NSPersistentStoreCoordinator_Class/NSPersistentStoreCoordinator.html">PersistentStoreCoordinators</a> e <a href="https://developer.apple.com/library/ios/#documentation/Cocoa/Reference/CoreDataFramework/Classes/NSManagedObjectContext_Class/NSManagedObjectContext.html">ManagedObjectContexts</a>, e desenvolvendo uma &quot;arquitetura escal&aacute;vel para o <a href="http://developer.apple.com/library/ios/#DOCUMENTATION/CoreData/Reference/NSFetchedResultsController_Class/Reference/Reference.html">FetchedResultsControllers</a>&quot;;</li> 
 <li>Mais duas semanas para &quot;se sentir confort&aacute;vel ao escrever c&oacute;digo para iOS&quot;.</li> 
</ul>
<p>Como um todo, Henneke disse que gastou o dobro do tempo na curva de aprendizado do iOS comparado ao Android.</p>
<p>A respeito do material de estudo e aprendizado dispon&iacute;vel, Henneke considera que a qualidade da documenta&ccedil;&atilde;o do Android &eacute; &quot;muito maior&quot; que a do iOS. O fato de o Android ser open source tamb&eacute;m o ajudou, possibilitando que olhasse exemplos de c&oacute;digo e aprendesse a partir deles. Em rela&ccedil;&atilde;o &agrave; documenta&ccedil;&atilde;o do iOS, Henneke observa que:</p>
<blockquote> 
 <p>Embora seja crescente a documenta&ccedil;&atilde;o sobre o iOS, a maioria se tornou obsoleta com as mudan&ccedil;as feitas nas vers&otilde;es 5 e 6 do iOS, incluindo a introdu&ccedil;&atilde;o da funcionalidade <a href="http://developer.apple.com/library/ios/#releasenotes/ObjectiveC/RN-TransitioningToARC/Introduction/Introduction.html">Automatic Reference Counting (ARC)</a>. Muitos exemplos de c&oacute;digo (incluindo os oficiais da Apple) e maneiras para tratar problemas tornaram-se problem&aacute;ticos e devem ser ignorados em prol de novos m&eacute;todos. Filtrar tudo isso demandou mais tempo ainda.</p> 
</blockquote>
<p>O desenvolvimento da vers&atilde;o Android envolveu uma reescrita completa do c&oacute;digo de sincroniza&ccedil;&atilde;o com os servidores de backend que era utilizado com o aplicativo web em HTML5, mas Henneke precisou de 10% a menos de tempo para escrever a mesma aplica&ccedil;&atilde;o para Android comparado ao iOS. As estat&iacute;sticas gerais do desenvolvimento est&atilde;o na tabela a seguir:</p>
<blockquote> 
 <table cellpadding="0" cellspacing="0"> 
  <tbody> 
   <tr> 
    <td> <p>&nbsp;</p> </td> 
    <td> <p><strong>Android</strong></p> </td> 
    <td> <p><strong>iOS</strong></p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Data de in&iacute;cio</strong></p> </td> 
    <td> <p>21/09/2012</p> </td> 
    <td> <p>02/03/2013</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Vers&atilde;o beta pronta para testes</strong></p> </td> 
    <td> <p>22/12/2012</p> </td> 
    <td> <p>10/06/2013</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Publica&ccedil;&atilde;o do aplicativo</strong></p> </td> 
    <td> <p>31/01/2013</p> </td> 
    <td> <p>18/07/2013</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Tempo total de projeto</strong></p> </td> 
    <td> <p>4,25 meses</p> </td> 
    <td> <p>4,5 meses</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Tempo de prepara&ccedil;&atilde;o para iniciar</strong></p> </td> 
    <td> <p>1 semana</p> </td> 
    <td> <p>2 semanas</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Tempo de desenvolvimento</strong></p> </td> 
    <td> <p>870 horas (aprox.)</p> </td> 
    <td> <p>960 horas (aprox.)</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Testes beta e corre&ccedil;&otilde;es</strong></p> </td> 
    <td> <p>34 dias</p> </td> 
    <td> <p>38 dias</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>N&uacute;mero de testadores beta</strong></p> </td> 
    <td> <p>92 pessoas</p> </td> 
    <td> <p>48 pessoas</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Linhas de c&oacute;digo</strong></p> </td> 
    <td> <p>26.981 linhas</p> </td> 
    <td> <p>23.872 linhas</p> </td> 
   </tr> 
   <tr> 
    <td> <p><strong>Tamanho do download do aplicativo</strong></p> </td> 
    <td> <p>1,1 MB</p> </td> 
    <td> <p>3,5 MB</p> </td> 
   </tr> 
  </tbody> 
 </table> 
</blockquote>
<p><strong>Ferramentas</strong></p>
<p>Pessoalmente Henneke prefire o editor <a href="http://pt.wikipedia.org/wiki/Vim">Vim</a>, mas comentou o seguinte sobre algumas das ferramentas que utilizou no projeto:</p>
<ul> 
 <li>A pesquisa no Eclipse &eacute; ridiculamente lenta e pesada;</li> 
 <li>A filtragem por <a href="http://developer.android.com/reference/android/util/Log.html">log tags</a> no Eclipse (com integra&ccedil;&atilde;o do logcat no <a href="http://developer.android.com/sdk/installing/installing-adt.html">plugin Android</a>) &eacute; muito &uacute;til;</li> 
 <li>A interface Builder no Xcode &eacute; in&uacute;til;</li> 
 <li>As ferramentas <a href="http://developer.apple.com/library/ios/#documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/Introduction/Introduction.html">Xcode Instruments</a> s&atilde;o muito &uacute;teis para profilling, medi&ccedil;&otilde;es e depura&ccedil;&atilde;o;</li> 
 <li>Os emuladores de Android s&atilde;o um completo desperd&iacute;cio de tempo (parece uma piada como s&atilde;o lentos). Em meu ciclo de desenvolvimento, sempre implantei o aplicativo em dispositivos Android reais para testes. Era muito mais r&aacute;pido;</li> 
 <li>O iOS Simulator &eacute; muito r&aacute;pido e tornou o ciclo de desenvolvimento muito mais eficiente. Para cada trecho de c&oacute;digo novo eu iniciava os testes com o simulador e somente trocava para o dispositivo quando estivesse mais completo;</li> 
 <li>Eu tinha dispositivos Android de teste para cada vers&atilde;o do sistema operacional que o aplicativo suportava (exceto o Gingerbread), ent&atilde;o confiava fortemente em meus testadores beta para atingir uma cobertura de testes suficiente;</li> 
 <li>Para os testes no iOS foram usados os mais velhos e mais novos dispositivos suportados.</li> 
</ul>
<p><strong>Design do aplicativo</strong></p>
<p>Henneke planejou criar o design de seu aplicativo de forma que se adaptasse facilmente a diversos tamanhos de tela, pois descobriu que a plataforma Android possui &quot;componentes maduros para ajudar os desenvolvedores a suportar a variedade de dimens&otilde;es existente&quot;. Ele utilizou o <a href="http://developer.android.com/guide/topics/ui/layout/relative.html">RelativeLayouts</a>, percebendo que &quot;todos os layouts s&atilde;o especificados em XML, o que &eacute; uma maneira bastante limpa, simples e eficiente de projetar telas&quot; (uma caracter&iacute;stica que s&oacute; foi apreciar totalmente ap&oacute;s a cria&ccedil;&atilde;o dos layouts para o iOS).</p>
<p>Nesse contexto, perguntamos a Henneke o que ele pensa a respeito da fragmenta&ccedil;&atilde;o do Android:</p>
<blockquote> 
 <p>Penso que a fragmenta&ccedil;&atilde;o do Android &eacute; muito sensacionalista. Isso realmente existe? Certamente isso &eacute; um fato. Isso &eacute; necessariamente um aspecto ruim do desenvolvimento para Android? Na verdade, n&atilde;o. O Google e a comunidade Android adotaram muitas abordagens para enfrentar esse desafio e isso est&aacute; funcionando. A <a href="http://developer.android.com/tools/support-library/index.html">biblioteca de suporte oficial</a> &eacute; bastante abrangente e continua crescendo. A biblioteca <a href="http://actionbarsherlock.com/">ActionBarSherlock</a> &eacute; bastante poderosa para acrescentar novas funcionalidades a dispositivos antigos. Al&eacute;m disso, a introdu&ccedil;&atilde;o recente do <a href="http://developer.android.com/google/play-services/index.html">Google Play Services</a> tiraram as operadoras para fora da equa&ccedil;&atilde;o da fragmenta&ccedil;&atilde;o. Os usu&aacute;rios n&atilde;o t&ecirc;m mais que confiar em suas operadoras para baixar a &uacute;ltima vers&atilde;o do Android e ter acesso &agrave;s novas funcionalidades. Isso &eacute; um passo enorme, tanto para os usu&aacute;rios Android quanto para os desenvolvedores.</p> 
</blockquote>
<p>Curiosamente, a experi&ecirc;ncia de Henneke com layouts no iOS n&atilde;o foi t&atilde;o boa:</p>
<blockquote> 
 <p>O <a href="http://developer.apple.com/library/ios/#documentation/UserExperience/Conceptual/AutolayoutPG/Articles/Introduction.html">Auto Layout</a>, a ferramenta da Apple an&aacute;loga ao RelativeLayouts, &eacute; bastante nova (introduzida no iOS 6) e sua integra&ccedil;&atilde;o com o Interface Builder (IB) &eacute; horr&iacute;vel. Gastei dias lutando contra o Auto Layout no IB - assim como todo desenvolvedor iOS 6 (<a href="http://inessential.com/2013/03/06/how_much_or_how_little_i_use_interface">1</a>, <a href="http://carpeaqua.com/2012/11/02/issues-with-achieving-auto-layout-zen/">2</a>, <a href="http://floriankugler.com/blog/2013/4/15/interface-builder-ndash-curse-or-convenience">3</a>), para construir restri&ccedil;&otilde;es precisas para <i>views</i> e tendo que ver o IB mudar completamente todas as minhas especifica&ccedil;&otilde;es por causa de seu sistema &quot;inteligente&quot; de manter os layouts constantemente n&atilde;o-amb&iacute;guos. Aprendi sem sucesso todas as <a href="http://ideveloper.co/auto-layout-interface-builder-tutorial/">dicas</a> e <a href="http://oleb.net/blog/2013/03/things-you-need-to-know-about-cocoa-autolayout/">truques</a> para lidar com essa parte fr&aacute;gil do IB. Finalmente acabei com o sofrimento ao tirar todos os layouts do IB e simplesmente escrev&ecirc;-los &agrave; m&atilde;o com p&aacute;ginas e p&aacute;ginas de c&oacute;digo repetitivo. Se evitar o IB e o <a href="http://www.infoq.com/br/news/2013/11/">estilo art&iacute;stico de codificar layouts baseado em ASCI</a><a href="http://www.infoq.com/br/news/2013/11/">I</a>, a implementa&ccedil;&atilde;o do Auto Layout &eacute; na verdade muito poderosa e simples de usar. Acredito que a Apple melhorou bastante isso no iOS 7, mas ainda preciso testar.</p> 
</blockquote>
<p>O Auto Layout limitou apenas o desenvolvimento para iOS 6 (iPhone 4 e 5), mas n&atilde;o os mais antigos, como Henneke contou:</p>
<blockquote> 
 <p>O aplicativo GQueues n&atilde;o pode ser de fato instalado ou executado em dispositivos antigos da Apple. Esse &eacute; o motivo de eu n&atilde;o ter testado neles. Quando um aplicativo &eacute; desenvolvido, um passo inicial &eacute; decidir quais vers&otilde;es do sistema operacional ser&atilde;o suportadas. O iOS 6 introduziu uma nova funcionalidade chamada Auto Layout que foi uma grande melhoria sobre as t&eacute;cnicas de layout anteriores. Mas, &eacute; claro, essa funcionalidade somente funcionou em dispositivos que rodam a &uacute;ltima vers&atilde;o do sistema operacional. Decidi que, em vez de criar layouts usando tanto o antigo m&eacute;todo quanto o Auto Layout, iria usar apenas este &uacute;ltimo, reduzindo drasticamente o tempo de desenvolvimento. Isso significa, &eacute; claro, que o aplicativo GQueues somente funciona em dispositivos que rodam o iOS 6, ou seja, em todos os dispositivos da Apple lan&ccedil;ados nos &uacute;ltimos dois anos. Imagino que qualquer pessoa com um telefone com mais de dois anos provavelmente ir&aacute; troc&aacute;-lo em breve de qualquer forma. Ent&atilde;o, fazendo isso, eu n&atilde;o estava realmente limitando muito o meu mercado.</p> 
</blockquote>
<p>Outras conclus&otilde;es sobre design foram:</p>
<ul> 
 <li>&quot;Suportar rota&ccedil;&atilde;o de dispositivos no Android requer bastante trabalho e &eacute; fonte de muitos bugs&quot;;</li> 
 <li>Quando um dispositivo Android &eacute; rotacionado, ele essencialmente <a href="http://developer.android.com/guide/components/activities.html#ConfigurationChanges">finaliza toda a pilha de views e recria cada uma delas</a> quando a rota&ccedil;&atilde;o se completa. Ent&atilde;o, para suportar rota&ccedil;&atilde;o com o aplicativo GQueues, precisei garantir que o estado atual de todas as coisas pudesse ser armazenado a qualquer momento e restaurado ao retomar&quot;;</li> 
 <li>&quot;[Para rota&ccedil;&atilde;o] o iOS requer apenas um pequeno esfor&ccedil;o enquanto a plataforma faz o resto&quot;;</li> 
 <li>&quot;Com iOS, a plataforma <a href="http://developer.apple.com/library/ios/#featuredarticles/ViewControllerPGforiPhoneOS/RespondingtoDeviceOrientationChanges/RespondingtoDeviceOrientationChanges.html">gerencia quase todas as preocupa&ccedil;&otilde;es com rota&ccedil;&atilde;o</a> para voc&ecirc;&quot;;</li> 
 <li>Tanto o Android quanto o iOS precisam de c&oacute;digo adicional para simular um Flow Layout.</li> 
</ul>
<p>Em rela&ccedil;&atilde;o aos testes beta e publica&ccedil;&atilde;o, Henneke faz os seguintes coment&aacute;rios:</p>
<ul class="c12 lst-kix_zdmgp0ibcbg4-0 start"> 
 <li>&quot;Testar direto no Android foi t&atilde;o simples quanto postar um link para um APK (Android Package) que pudesse ser baixado para o dispositivo&quot;;</li> 
 <li>&quot;O Google tornou ainda mais f&aacute;cil testar aplicativos com usu&aacute;rios reais ao <a href="https://support.google.com/googleplay/android-developer/answer/3131213?hl=en">suportar testes de vers&otilde;es alpha e beta no Developers Console e lan&ccedil;amento gradual (staged rollout)</a>&quot;;</li> 
 <li>&quot;Os testes beta no iOS foram muito mais dif&iacute;ceis, embora estivesse usando o servi&ccedil;o <a href="http://testflightapp.com/">TestFlight</a>, o qual simplifica bastante o processo. Alinhado ao apetite insaci&aacute;vel da Apple por controle, o UDID de cada dispositivo utilizado para testes deve ser adicionado ao certificado usado para assinar a vers&atilde;o beta do aplicativo. Consequentemente, cada vez que precisava adicionar novos testadores beta, seja uma &uacute;nica pessoa ou um novo grupo, tive que criar e distribuir uma nova compila&ccedil;&atilde;o do aplicativo. Al&eacute;m disso, a Apple limita a 100 a quantidade de dispositivos de teste registrados por ano. Por esse motivo, tive que alocar cuidadosamente minhas vagas, que &eacute; a raz&atilde;o pela qual possuia apenas a metade do n&uacute;mero de testadores iOS comparado com Android&quot;;</li> 
 <li>&quot;Publicar o aplicativo GQueues no ​​Google Play foi uma verdadeira alegria. Fui capaz de lan&ccedil;ar o aplicativo assim que decidi que estava pronto. Cliquei no bot&atilde;o e em 30 minutos j&aacute; estava dispon&iacute;vel no Google Play para os clientes de todo o mundo instalarem em seus aparelhos&quot;;</li> 
 <li>&quot;A publica&ccedil;&atilde;o de aplicativos na App Store, como quase todos os desenvolvedores de iOS podem atestar, &eacute; uma experi&ecirc;ncia desmoralizante. Depois de meses de intensa e rigorosa codifica&ccedil;&atilde;o, fui for&ccedil;ado a submeter minha cria&ccedil;&atilde;o para a Apple e esperar sete dias para que o revisor (em dois minutos) olhasse para o aplicativo e desse a &quot;quase obrigat&oacute;ria&quot; rejei&ccedil;&atilde;o inicial. Depois disso, passei um dia fazendo as altera&ccedil;&otilde;es necess&aacute;rias, submeti novamente e esperei mais oito dias antes de finalmente obter aprova&ccedil;&atilde;o&quot;.</li> 
</ul>
<p>Henneke tamb&eacute;m fez uma s&eacute;rie de anota&ccedil;&otilde;es sobre o uso de armazenamento e gerenciamento de dados, busca, express&otilde;es regulares, pagina&ccedil;&atilde;o, entrada de voz, compartilhamento e <i>widgets</i> em ambas as plataformas e podem ser encontradas no <a href="http://blog.gqueues.com/2013/07/android-vs-ios-comparing-development.html">blog do GQueues</a>.</p>
<p>Como conclus&atilde;o, Henneke n&atilde;o considera uma plataforma melhor que a outra. Cada uma possui &quot;&aacute;reas nas quais s&atilde;o realmente mais fortes e maduras, e outros aspectos que definitivamente precisam de melhorias&quot;.</p>
<p>Tamb&eacute;m perguntamos a Henneke sobre quais funcionalidades ele gostaria de ver no iOS e no Android:</p>
<blockquote> 
 <p>Eu adoraria ver no iOS uma API para SIRI, ou pelo menos reconhecimento de voz. Em rela&ccedil;&atilde;o ao Android, algumas integra&ccedil;&otilde;es mais profundas com o Google Now seria muito legal.</p> 
</blockquote>
<p>Por fim, mas n&atilde;o menos importante, perguntamos a Henneke o qu&ecirc; motivou a mudan&ccedil;a de HTML5 para aplica&ccedil;&atilde;o nativa. Em sua experi&ecirc;ncia, o HTML5 ainda n&atilde;o est&aacute; maduro o suficiente:</p>
<blockquote> 
 <p>Considerando que fui um <a href="http://googlecode.blogspot.com.br/2011/05/gqueues-mobile-case-for-html5-web-app.html">defensor p&uacute;blico</a> do HTML5, decidi escrever um <a href="http://blog.gqueues.com/2013/02/eating-my-own-words-gqueues-switches.html">post</a> explicando minha mudan&ccedil;a dr&aacute;stica na estrat&eacute;gia para construir aplicativos nativos. Em suma, o HTML5 ainda tem que fornecer as funcionalidades e velocidade necess&aacute;rias para torn&aacute;-lo uma alternativa competitiva para aplicativos nativos. Al&eacute;m disso, para melhor ou pior, as pessoas gostam de baixar aplicativos. O usu&aacute;rios do GQueues estavam exigindo aplicativos nativos, ent&atilde;o me propus a atender essa necessidade.</p> 
</blockquote>
<p>Considerando que este post reflete somente a experi&ecirc;ncia de apenas uma pessoa desenvolvendo aplicativos para Android e iOS, ele n&atilde;o pode ser generalizado e servir de base para tirar conclus&otilde;es definitivas sobre o desenvolvimento nas respectivas plataformas, especialmente sobre qual &eacute; melhor ou pior. No entanto, muitos dos coment&aacute;rios de Henneke s&atilde;o v&aacute;lidos, expressando algumas das alegrias e tristezas que acompanham o desenvolvimento de aplicativos m&oacute;veis nas duas plataformas mais populares do mercado.</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Masonry: Auto Layout no iOS</h3><p>Masonry &eacute; um projeto open source que pretende tornar o c&oacute;digo do Auto Layout mais leg&iacute;vel e conciso.</p>
<p>O <a href="https://github.com/cloudkite/Masonry">Masonry</a>, &quot;um framework de layout leve que encapsula o Auto Layout com uma sintaxe mais agrad&aacute;vel&quot;, permitindo uma nova experi&ecirc;ncia no XIB ou Storyboard-free. Jonas Budelmann, criador do Masonry, <a href="https://github.com/cloudkite/Masonry#whats-wrong-with-nslayoutconstraints">argumenta</a> que apesar do Auto Layout ser poderoso tamb&eacute;m pode se tornar verboso e ileg&iacute;vel.</p>
<p>O Masonry &eacute; uma linguagem espec&iacute;fica de dom&iacute;nio (Domain Specific Language - DSL) que oferece todas as capacidades do Auto Layout com a conveni&ecirc;ncia de m&eacute;todos para fazer e atualizar restri&ccedil;&otilde;es, acessando os atributos, definindo prioridades e suporte a depura&ccedil;&atilde;o.</p>
<p>O exemplo de c&oacute;digo a seguir est&aacute; dispon&iacute;vel no GitHub e apresenta um <a href="https://github.com/cloudkite/Masonry#prepare-to-meet-your-maker">uso normal e sucinto da sintaxe do Masonry</a>:</p>
<pre>
UIEdgeInsets padding = UIEdgeInsetsMake(10, 10, 10, 10);
[view1 mas_makeConstraints:^(MASConstraintMaker *make) {
  make.edges.equalTo(superview).with.insets(padding);
}];
</pre>
<p>O principal do Auto Layout &eacute; a <a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/AutolayoutPG/AutoLayoutConcepts/AutoLayoutConcepts.html#//apple_ref/doc/uid/TP40010853-CH14-SW2">restri&ccedil;&atilde;o</a>: uma representa&ccedil;&atilde;o matem&aacute;tica do relacionamento entre elementos de interface gr&aacute;fica (UI). As restri&ccedil;&otilde;es compreendem tamanho, gerenciamento de posicionamento relativo por prioridade e limiares. As restri&ccedil;&otilde;es <a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/AutolayoutPG/AutoLayoutConcepts/AutoLayoutConcepts.html#//apple_ref/doc/uid/TP40010853-CH14-SW2">adicionadas</a> podem causar poss&iacute;veis <a href="https://developer.apple.com/library/ios/documentation/userexperience/conceptual/AutolayoutPG/ResolvingIssues/ResolvingIssues.html#//apple_ref/doc/uid/TP40010853-CH17-SW5">conflitos</a> de restri&ccedil;&otilde;es e tratamento insuficiente das restri&ccedil;&otilde;es trazendo <a href="https://developer.apple.com/library/ios/documentation/userexperience/conceptual/AutolayoutPG/ResolvingIssues/ResolvingIssues.html#//apple_ref/doc/uid/TP40010853-CH17-SW7">ambiguidade</a>, sendo que ambos cen&aacute;rios podem ocasionar lan&ccedil;amento de exce&ccedil;&otilde;es.</p>
<p>A cria&ccedil;&atilde;o pragm&aacute;tica das restri&ccedil;&otilde;es sem o uso do Masunry &eacute; poss&iacute;vel atrav&eacute;s da cria&ccedil;&atilde;o de um <a href="https://developer.apple.com/library/ios/documentation/AppKit/Reference/NSLayoutConstraint_Class/NSLayoutConstraint/NSLayoutConstraint.html">NSLayoutConstraint</a> com refer&ecirc;ncia para a vis&atilde;o e especificando atributos e relacionamentos. A Apple fornece o <a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/AutolayoutPG/VisualFormatLanguage/VisualFormatLanguage.html#//apple_ref/doc/uid/TP40010853-CH3-SW1">Visual Format Language</a>; outra DSL para descrever os relacionamentos no formato texto.</p>
<p>O Auto Layout n&atilde;o &eacute; obrigat&oacute;rio nem exclusivo com o &quot;springs e struts&quot; para realizar uma abordagem v&aacute;lida. Os &quot;springs e struts&quot;, ou m&aacute;scaras de <a href="https://developer.apple.com/library/ios/documentation/UIKit/Reference/UIView_Class/UIView/UIView.html#//apple_ref/doc/uid/TP40006816-CH3-SW6">auto redimensionamento</a>, determinam como uma view responde quando seu componente pai muda suas dimens&otilde;es.</p>
<p>A Apple fornece algumas <a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/TransitionGuide/index.html#//apple_ref/doc/uid/TP40013174">raz&otilde;es para adotar o Auto Layout</a>:</p>
<ul class="c7 lst-kix_1xn1beq4grmg-0 start"> 
 <li>&quot;Springs e struts&quot; necessitam que o <a href="https://developer.apple.com/library/ios/documentation/WindowsViews/Conceptual/ViewPG_iPhoneOS/CreatingViews/CreatingViews.html#//apple_ref/doc/uid/TP40009503-CH5-SW35">c&oacute;digo</a> suporte m&uacute;ltiplas orienta&ccedil;&otilde;es, diferentes tamanhos de telas e conte&uacute;do din&acirc;mico;</li> 
 <li>O <a href="https://developer.apple.com/library/ios/documentation/userexperience/conceptual/transitionguide/AppearanceCustomization.html">Dynamic Types</a> dos iOS 7 permite que os usu&aacute;rios especifiquem um tamanho de texto preferido nas aplica&ccedil;&otilde;es;</li> 
 <li>O suporte das vers&otilde;es iOS 6 e 7; e seus diferentes elementos de m&eacute;tricas.</li> 
</ul>
<p>O Auto Layout n&atilde;o &eacute; nada sem os problemas fundamentais. A Apple fornece um <a href="https://developer.apple.com/library/ios/technotes/tn2154/_index.html#//apple_ref/doc/uid/DTS40013309">guia</a> de como usar o Auto Layout com o UIScrollView. Matt Neuburg fornece um argumento convincente do <a href="http://stackoverflow.com/questions/12943107/how-do-i-adjust-the-anchor-point-of-a-calayer-when-auto-layout-is-being-used/14105757#14105757">porque o &quot;Auto Layout n&atilde;o funciona totalmente nas transforma&ccedil;&otilde;es das views&quot;</a> sugerindo um grande uso das camadas de transforma&ccedil;&otilde;es para compensar.</p>
<p>Qualquer tipo de c&oacute;digo de Auto Layout significa que <a href="https://developer.apple.com/library/ios/documentation/DeveloperTools/Conceptual/WhatsNewXcode/Articles/xcode_5_0.html#//apple_ref/doc/uid/TP40012953-SW25">n&atilde;o haver&aacute; os ganhos fornecidos pelas melhorias dispon&iacute;veis no Interface Builder do Xcode 5</a>. Principalmente a habilidade para <a href="https://developer.apple.com/library/ios/documentation/UserExperience/Conceptual/AutolayoutPG/ResolvingIssues/ResolvingIssues.html#//apple_ref/doc/uid/TP40010853-CH17-SW1">resolver visualmente os problemas do Auto Layout</a> e <a href="https://developer.apple.com/library/ios/documentation/userexperience/conceptual/transitionguide/SupportingEarlieriOS.html">pr&eacute; visualizar o c&oacute;digo no assistente de edi&ccedil;&atilde;o</a> que deixa visualizar como o layout ficar&aacute; em tempo de execu&ccedil;&atilde;o em diferentes orienta&ccedil;&otilde;es, diferentes vers&otilde;es do iOS e diferentes tamanhos de dispositivos.</p><br><br><br><br><br><br></body></html>
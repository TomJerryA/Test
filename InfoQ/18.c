<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Tudo sobre o Java 8</h3><p>A <a href="http://www.techempower.com/">TechEmpower</a>, uma empresa de desenvolvimento de aplica&ccedil;&otilde;es customizadas com sede em El Segundo, Calif&oacute;rnia, postou recentemente um post chamado &quot;<a href="http://www.techempower.com/blog/2013/03/26/everything-about-java-8/">Tudo sobre o Java 8</a>&quot;. No post h&aacute; um resumo completo das mudan&ccedil;as que o desenvolvedor encontrar&aacute; no Java 8. Aqui est&aacute; uma vis&atilde;o geral do post.</p>
<p>&nbsp;</p>
<h2>Melhorias nas interfaces</h2>
<p>Agora as interfaces podem definir m&eacute;todos static. Por exemplo, a classe java.util.Comparator agora possui o m&eacute;todo static naturalOrder:</p>
<pre>
  public static &lt;T extends Comparable&lt;? super T&gt;&gt; Comparator&lt;T&gt; naturalOrder() {
    return (Comparator&lt;T&gt;) Comparators.NaturalOrderComparator.INSTANCE;
  }
</pre>
<p>Agora as interfaces podem fornecer m&eacute;todos padr&otilde;es. Isso permite que o desenvolvedor adicione novos m&eacute;todos sem quebrar os c&oacute;digos existentes que implementam a interface. Por exemplo, o padr&atilde;o forEach foi inclu&iacute;do na interface java.lang.Iterable:</p>
<pre>
  public default void forEach(Consumer&lt;? super T&gt; action) {
    Objects.requireNonNull(action);
    for (T t : this) {
      action.accept(t);
    }
  }
</pre>
<p><span><br /> </span>Vale ressaltar uma interface n&atilde;o pode fornecer uma implementa&ccedil;&atilde;o padr&atilde;o para os m&eacute;todos da classe Object.</p>
<p>&nbsp;</p>
<h2>Interfaces funcionais</h2>
<p>Uma interface funcional &eacute; uma interface que define apenas um m&eacute;todo abstrato. A anota&ccedil;&atilde;o <a href="http://download.java.net/jdk8/docs/api/java/lang/FunctionalInterface.html">FunctionalInterface</a> foi adicionada para indicar que uma interface tem a inten&ccedil;&atilde;o de ser uma interface funcional. Por exemplo, a interface java.lang.Runnable &eacute; uma interface funcional.</p>
<pre>
  @FunctionalInterface
  public interface Runnable {
    public abstract void run();
  }
</pre>
<p>Note que o compilador do Java ir&aacute; tratar qualquer interface que atenda &agrave; defini&ccedil;&atilde;o de interface funcional mesmo que n&atilde;o possua a anota&ccedil;&atilde;o FunctionalInterface. Por&eacute;m quando anotada com FunctionalInterface o compilador verifica se h&aacute; apenas um m&eacute;todo.</p>
<p>&nbsp;</p>
<h2>Lambdas</h2>
<p>A caracter&iacute;stica mais importante das interfaces funcionais &eacute; que elas podem ser instanciadas por meio de lambdas. As <a href="http://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html">express&otilde;es lambdas</a> permitem tratar funcionalidades como argumento de m&eacute;todo, ou c&oacute;digo como dados. Abaixo est&atilde;o alguns exemplos de lambdas. As entradas est&atilde;o &agrave; esquerda e o c&oacute;digo &agrave; direita. Os tipos de entrada podem ser inferidos e s&atilde;o opcionais:</p>
<pre>
  (int x, int y) -&gt; { return x + y; }

  (x, y) -&gt; x + y

  x -&gt; x * x

  () -&gt; x

  x -&gt; { System.out.println(x); }
</pre>
<p>Aqui est&aacute; um exemplo de instancia&ccedil;&atilde;o da interface funcional Runnable:</p>
<pre>
  Runnable r = () -&gt; { System.out.println(&quot;Running!&quot;); }
</pre>
<p>&nbsp;</p>
<h2>Refer&ecirc;ncias de m&eacute;todos</h2>
<p>As <a href="http://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html">refer&ecirc;ncias de m&eacute;todos</a> s&atilde;o express&otilde;es lambdas compactas para m&eacute;todos que j&aacute; possuem um nome. Aqui est&atilde;o alguns exemplos de refer&ecirc;ncias de m&eacute;todos, com o seu equivalente em express&atilde;o lambda &agrave; direita:</p>
<pre>
  String::valueOf     x -&gt; String.valueOf(x)
  Object::toString    x -&gt; x.toString()
  x::toString         () -&gt; x.toString()
  ArrayList::new      () -&gt; new ArrayList&lt;&gt;()
</pre>
<p>&nbsp;</p>
<h2>Lambdas capturantes ou n&atilde;o capturantes</h2>
<p>As lambdas s&atilde;o ditas como &quot;capturantes&quot; se acessarem uma vari&aacute;vel n&atilde;o static ou objeto que estavam definidos fora do corpo da lambda. Por exemplo, a express&atilde;o lambda a seguir est&aacute; acessando uma vari&aacute;vel x:</p>
<pre>
  int x = 5;
  return y -&gt; x + y;
</pre>
<p>Uma express&atilde;o lambda pode apenas acessar vari&aacute;veis locais e par&acirc;metros dentro de blocos que s&atilde;o final ou efetivamente final.</p>
<p>&nbsp;</p>
<h2>java.util.function</h2>
<p>Um grande n&uacute;mero de novas interfaces funcionais foi adicionado no pacote <a href="http://download.java.net/jdk8/docs/api/java/util/function/package-summary.html">java.util.function</a>. A seguir temos alguns exemplos:</p>
<ul class="c7 lst-kix_pd8dc28z61hu-0 start"> 
 <li>Function&lt;T, R&gt; − recebe T como entrada, retorna R como sa&iacute;da;</li> 
 <li>Predicate&lt;T&gt; − recebe T como entrada, retorna um valor booleano como sa&iacute;da;</li> 
 <li>Consumer&lt;T&gt; − recebe T como entrada, n&atilde;o retorna nada como sa&iacute;da;</li> 
 <li>Supplier&lt;T&gt; − n&atilde;o recebe entrada, retorna T como sa&iacute;da;</li> 
 <li>BinaryOperator&lt;T&gt; − recebe duas entradas T, retorna um T como sa&iacute;da.</li> 
</ul>
<p>&nbsp;</p>
<h2>java.util.stream</h2>
<p>O novo pacote <a href="http://download.java.net/jdk8/docs/api/java/util/stream/package-summary.html">java.util.stream</a> fornece classes para apoiar opera&ccedil;&otilde;es no estilo funcional sobre os fluxos de dados. Uma maneira comum de obter um fluxo ser&aacute; por meio de uma cole&ccedil;&atilde;o (collection):</p>
<pre>
  Stream&lt;T&gt; stream = collection.stream();
</pre>
<p>Aqui est&aacute; um exemplo do pacote Javadocs:</p>
<pre>
  int sumOfWeights = blocks.stream().filter(b -&gt; b.getColor() == RED)
                                    .mapToInt(b -&gt; b.getWeight())
                                    .sum();
</pre>
<p>Aqui usamos um bloco de Collection como fonte de fluxo, e ent&atilde;o otimizamos um filtro de redu&ccedil;&atilde;o de mapa (filter-map-reduce) no fluxo para obter a soma dos pesos dos blocos vermelhos.</p>
<p>Os fluxos podem ser infinitos e manter o estado (stateful), tamb&eacute;m podem ser sequenciais ou em paralelo. Para se trabalhar com fluxos, primeiro deve-se obter um de alguma fonte, realizar uma ou mais opera&ccedil;&otilde;es intermediarias, e ent&atilde;o executar uma opera&ccedil;&atilde;o terminal. As opera&ccedil;&otilde;es intermediarias incluem filter, map, flatMap, peel, distinct, sorted, limit e substream.</p>
<p>As opera&ccedil;&otilde;es terminais incluem forEach, toArray, reduce, collect, min, max, count, anyMatch, allMatch, noneMatch, findFirst e findAny. Uma classe muito &uacute;til &eacute; a <a href="http://download.java.net/jdk8/docs/api/java/util/stream/Collectors.html">java.util.stream.Collectors</a> que implementa v&aacute;rias opera&ccedil;&otilde;es de redu&ccedil;&atilde;o, tal como convers&atilde;o de fluxos em cole&ccedil;&otilde;es e elementos de agrega&ccedil;&atilde;o.</p>
<p>&nbsp;</p>
<h2>Melhoras na infer&ecirc;ncia dos tipos gen&eacute;ricos</h2>
<p>Isso melhora a habilidade do compilador Java para inferir tipos gen&eacute;ricos e reduzir os argumentos de tipos informados nas chamadas dos m&eacute;todos gen&eacute;ricos. No Java 7 o c&oacute;digo &eacute; parecido com o exemplo a seguir:</p>
<pre>
  foo(Utility.&lt;Type&gt;bar());
  Utility.&lt;Type&gt;foo().bar();
</pre>
<p>No Java 8, foi aprimorada a infer&ecirc;ncia de argumentos e o encadeamento de chamadas permite escrever um c&oacute;digo como este:</p>
<pre>
  foo(Utility.bar());
    Utility.foo().bar();
</pre>
<p>&nbsp;</p>
<h2>java.time</h2>
<p>A nova API de data e hora est&aacute; dentro do pacote <a href="http://download.java.net/jdk8/docs/api/java/time/package-summary.html">java.time</a>. Todas as classes s&atilde;o imut&aacute;veis e thread-safe. Os tipos de data e hora inclusos s&atilde;o: Instant, LocalDate, LocalTime, LocalDateTime e ZonedDateTime. Al&eacute;m das datas e horas, tamb&eacute;m existem os tipos Duration e Period. Para completar tamb&eacute;m foram inclu&iacute;dos os tipos Month, DayOfWeek, Year, Month, YearMonth, MonthDay, OffsetTime e OffsetDateTime. A maioria das novas classes de data e hora s&atilde;o suportadas pelo JDBC.</p>
<p>&nbsp;</p>
<h2>Complementando a API Collections</h2>
<p>A habilidade das interfaces de terem m&eacute;todos padr&atilde;o permitiu que o Java 8 adicionasse uma grande quantidade de m&eacute;todos novos na API Collections. As implementa&ccedil;&otilde;es padr&otilde;es s&atilde;o fornecidas em todas as interfaces e implementa&ccedil;&otilde;es mais eficientes ser&atilde;o adicionadas &agrave;s classes completas quando apropriado. A seguir temos uma lista dos novos m&eacute;todos:</p>
<ul class="c7 lst-kix_5tsk7a3a6t6y-0 start"> 
 <li>Iterable.forEach(Consumer)</li> 
 <li>Iterator.forEachRemaining(Consumer)</li> 
 <li>Collection.removeIf(Predicate)</li> 
 <li>Collection.spliterator()</li> 
 <li>Collection.stream()</li> 
 <li>Collection.parallelStream()</li> 
 <li>List.sort(Comparator)</li> 
 <li>List.replaceAll(UnaryOperator)</li> 
 <li>Map.forEach(BiConsumer)</li> 
 <li>Map.replaceAll(BiFunction)</li> 
 <li>Map.putIfAbsent(K, V)</li> 
 <li>Map.remove(Object, Object)</li> 
 <li>Map.replace(K, V, V)</li> 
 <li>Map.replace(K, V)</li> 
 <li>Map.computeIfAbsent(K, Function)</li> 
 <li>Map.computeIfPresent(K, BiFunction)</li> 
 <li>Map.compute(K, BiFunction)</li> 
 <li>Map.merge(K, V, BiFunction)</li> 
 <li>Map.getOrDefault(Object, V)</li> 
</ul>
<p>&nbsp;</p>
<h2>Complementando a API Concurrency</h2>
<p>Houve algumas adi&ccedil;&otilde;es na API Concurrency, algumas das quais ser&atilde;o discutidas brevemente aqui. O ForkJoinPool.commonPool() &eacute; uma estrutura que trata as opera&ccedil;&otilde;es de fluxo em paralelo. A fila comum &eacute; utilizada por qualquer ForkJoinTask que n&atilde;o apresentar explicitamente uma fila especifica. A ConcurrentHashMap est&aacute; sendo reescrita complemente. A StampedLock &eacute; a nova implementa&ccedil;&atilde;o de bloqueio que pode ser utilizada como uma alternativa para o ReentrantReadWriteLock. A CompletableFuture &eacute; uma implementa&ccedil;&atilde;o da interface Future que fornece m&eacute;todos para executar e encadear tarefas ass&iacute;ncronas.</p>
<p>&nbsp;</p>
<h2>Complementando a API IO/NIO</h2>
<p>H&aacute; novos m&eacute;todos de IO/NIO, que s&atilde;o utilizados para obter um java.util.stream.Stream de arquivos ou fluxos de entrada:</p>
<ul> 
 <li>BufferedReader.lines()</li> 
 <li>Files.list(Path)</li> 
 <li>Files.walk(Path, int, FileVisitOption...)</li> 
 <li>Files.walk(Path, FileVisitOption...)</li> 
 <li>Files.find(Path, int, BiPredicate, FileVisitOption...)</li> 
 <li>Files.lines(Path, Charset)</li> 
 <li>DirectoryStream.stream()</li> 
</ul>
<p>H&aacute; uma nova UncheckedIOException, que &eacute; uma IOException que estende a RuntimeException. H&aacute; tamb&eacute;m o CloseableStream, um stream que pode e deve ser fechado.</p>
<p>&nbsp;</p>
<h2>Mudan&ccedil;as no Reflection e nas anota&ccedil;&otilde;es</h2>
<p>Com os <a href="http://types.cs.washington.edu/jsr308/">anota&ccedil;&otilde;es de tipos</a>, as anota&ccedil;&otilde;es poder&atilde;o ser escritas em mais locais, como um argumento de tipos gen&eacute;ricos como List&lt;@Nullable String&gt;. Isso aprimora a detec&ccedil;&atilde;o de erros pelas ferramentas de an&aacute;lise est&aacute;ticas o que fortalecer&aacute; e refinar&aacute; o sistema de tipos embarcados no Java.</p>
<p>&nbsp;</p>
<h2>Nashorn: mecanismo de JavaScript</h2>
<p>O Nashorn &eacute; a implementa&ccedil;&atilde;o mais nova, leve e de alto desempenho de JavaScript integrado no JDK. O Nashorn &eacute; o sucessor do Rhino com desempenho aprimorado e melhor uso de mem&oacute;ria. Ele contar&aacute; com a API javax.script, mas n&atilde;o incluir&aacute; o suporte a DOM/CSS e tamb&eacute;m n&atilde;o incluir&aacute; API de plugins para navegadores.</p>
<p>&nbsp;</p>
<h2>Outros complementos adicionados no java.lang, java.util e em outros locais.</h2>
<p>H&aacute; outros complementos adicionados em outros pacotes que n&atilde;o foram mencionados. Aqui est&atilde;o alguns dos mais not&aacute;veis: A ThreadLocal.withInitial(Supplier) permite a declara&ccedil;&atilde;o de uma vari&aacute;vel thread-local mais compacta. As muito atrasadas StringJoiner e String.join(...) s&atilde;o finalmente parte do Java 8. O Comparator oferece alguns m&eacute;todos novos para executar o encadeamento e compara&ccedil;&atilde;o baseada em campos (atributos). O tamanho do pool padr&atilde;o do mapa de String est&aacute; maior, por volta de 25 a 50K.</p>
<p>Para mais informa&ccedil;&otilde;es visite o post <a href="http://www.techempower.com/blog/2013/03/26/everything-about-java-8/">Tudo sobre Java 8</a>. A &uacute;ltima atualiza&ccedil;&atilde;o desse post foi dia 10 de Setembro de 2013.</p><br><br><br><br><br><br></body></html>
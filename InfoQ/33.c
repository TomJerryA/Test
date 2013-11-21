<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Processamento em lote no Java EE 7 e melhorias no Spring Batch</h3><p>O Java EE 7 foi lan&ccedil;ado em junho trazendo um conjunto de novas especifica&ccedil;&otilde;es, entre elas a JSR-352. Essa nova especifica&ccedil;&atilde;o define um modelo de programa&ccedil;&atilde;o para processamento em lote dentro da plataforma Java EE e baseia-se fortemente no projeto <a href="http://www.springsource.org/spring-batch">Spring Batch</a> da VMware. O Spring Batch tamb&eacute;m recebeu aten&ccedil;&atilde;o recentemente por conta de um lan&ccedil;amento importante que traz configura&ccedil;&otilde;es mais enxutas e simplifica o acesso a dados.</p>
<p>A JSR-352 (Batch Applications for the Java Platform) oferece aos desenvolvedores um modelo de programa&ccedil;&atilde;o para desenvolver sistemas de processamento em lote robustos. O ponto central desse modelo de programa&ccedil;&atilde;o &eacute; um padr&atilde;o de desenvolvimento emprestado do Spring Batch: o <i>Reader-Processor-Writer</i>. Esse pattern incentiva os desenvolvedores a adotar um estilo padr&atilde;o de processamento orientado a peda&ccedil;os (chunks).</p>
<p><img src="http://www.infoq.com/resource/news/2013/11/javaee7-spring-batch/pt/resources/jsr-352.jpg" alt="" _href="img://jsr-352.jpg" _p="true" /></p>
<p>O padr&atilde;o <i>Reader-Processor-Writer</i> &eacute; composto por um fluxo de trabalho de tr&ecirc;s passos que os desenvolvedores devem seguir:</p>
<ul> 
 <li>Uma classe <a href="http://javaee-spec.java.net/nonav/javadocs/javax/batch/api/chunk/ItemReader.html">ItemReader</a> que consome um peda&ccedil;o do dado a ser processado (normalmente um &uacute;nico registro);</li> 
 <li>Um <a href="http://javaee-spec.java.net/nonav/javadocs/javax/batch/api/chunk/ItemProcessor.html">ItemProcessor</a> que processa cada um dos peda&ccedil;os, aplicando a l&oacute;gica de neg&oacute;cio e de dom&iacute;nio;</li> 
 <li>E, finalmente, um <a href="http://javaee-spec.java.net/nonav/javadocs/javax/batch/api/chunk/ItemWriter.html">ItemWriter</a> para o qual os registros ser&atilde;o delegados ap&oacute;s o processamento e agregados.</li> 
</ul>
<p>De acordo com a especifica&ccedil;&atilde;o, os <i>Jobs</i> (tarefas) s&atilde;o descritos atrav&eacute;s de documentos XML e cont&eacute;m <i>Steps</i> (passos) no fluxo de processamento. Cada <i>Step</i> &eacute; respons&aacute;vel por descrever como cada peda&ccedil;o de dado ser&aacute; processado e qual o intervalo entre os commits. Requisitos mais complexos para se processar determinados <i>Steps</i> do fluxo de trabalho podem ser implementados com um <a href="http://javaee-spec.java.net/nonav/javadocs/javax/batch/api/Batchlet.html">batchlet</a>. Um <i>batchlet</i> &eacute; a vers&atilde;o da JSR-352 para o <a href="http://static.springsource.org/spring-batch/apidocs/org/springframework/batch/core/step/tasklet/Tasklet.html">tasklet</a> do Spring Batch, o qual oferece estrat&eacute;gias para processar <i>Steps</i>.</p>
<p>A JSR-352 tamb&eacute;m emprega o padr&atilde;o do Spring Batch para acessar e controlar <i>jobs</i>. <i>Jobs</i> s&atilde;o invocados atrav&eacute;s de um <a href="http://javaee-spec.java.net/nonav/javadocs/javax/batch/operations/JobOperator.html">JobOperator</a> e os resultados s&atilde;o acess&iacute;veis atrav&eacute;s de um <i>JobRepository</i>. No Spring Batch o nome <a href="http://static.springsource.org/spring-batch/apidocs/org/springframework/batch/core/repository/JobRepository.html">JobRepository</a>permanece o mesmo, enquanto o <i>JobOperator</i> &eacute; chamado de <a href="http://static.springsource.org/spring-batch/apidocs/org/springframework/batch/core/launch/JobLauncher.html">JobLauncher</a>.</p>
<p>A forma de defini&ccedil;&atilde;o de jobs no Java EE 7 &eacute; um pouco diferente do Spring Batch. Os desenvolvedores s&atilde;o obrigados a colocar os documentos XML de configura&ccedil;&atilde;o de jobs no diret&oacute;rio <strong>META-INF/batch-jobs</strong> dos projetos. Com o Spring Batch, os desenvolvedores podem colocar as configura&ccedil;&otilde;es de jobs em qualquer local do contexto do Spring para torn&aacute;-las dispon&iacute;veis no container.</p>
<p>Os arquivos XML de configura&ccedil;&atilde;o de jobs no Java EE 7 definem classes concretas para as interfaces <i>ItemReader</i>, <i>ItemProcessor</i> e <i>ItemWriter</i>, al&eacute;m de especificar o tamanho do <i>buffer</i>, o intervalo entre commits e a pol&iacute;tica de <i>checkpoints</i>. A pol&iacute;tica de checkpoints indica como os commits ser&atilde;o tratados. O valor padr&atilde;o &eacute; &quot;item&quot;, mas os desenvolvedores podem optar por usar &quot;time&quot; (tempo) como estrat&eacute;gia. O primeiro caso especifica o n&uacute;mero de registos processados, enquanto o &uacute;ltimo descreve os segundos decorridos entre um commit e outro.</p>
<pre>
&lt;job xmlns=&quot;http://batch.jsr352/jsl&quot;&gt;
    &lt;step id=&quot;myStep&quot;&gt;
        &lt;chunk
                reader=&quot;MyItemReader&quot;
                writer=&quot;MyItemWriter&quot;
                processor=&quot;MyItemProcessor&quot;
                buffer-size=&quot;5&quot;
                checkpoint-policy=&quot;item&quot;
                commit-interval=&quot;10&quot; /&gt;
    &lt;/step&gt;
&lt;/job&gt;
</pre>
<p>A configura&ccedil;&atilde;o de jobs no Spring Batch &eacute; quase id&ecirc;ntico ao Java EE 7. A exce&ccedil;&atilde;o &eacute; que os passos (steps) s&atilde;o colocados em uma diretiva <i>tasklet</i>. Os atributos reader, process e writer de configura&ccedil;&atilde;o dos chunks (peda&ccedil;os) s&atilde;o refer&ecirc;ncias para beans que existem no contexto da aplica&ccedil;&atilde;o. A partir da vers&atilde;o 2.2.0, o intervalo de commits na configura&ccedil;&atilde;o de chunks indica quantos itens devem ser processados ​​antes de se efetivar um commit.</p>
<pre>
&lt;job id=&quot;myJob&quot;&gt;
    &lt;step id=&quot;myStep&quot;&gt;
        &lt;tasklet&gt;
            &lt;chunk
                    reader=&quot;myItemReader&quot;
                    processor=&quot;myItemProcessor&quot;
                    writer=&quot;myItemWriter&quot;
                    commit-interval=&quot;2&quot; /&gt;
        &lt;/tasklet&gt;
    &lt;/step&gt;
&lt;/job&gt;  

&lt;bean class=&quot;...MyItemReader&quot; /&gt;
&lt;bean class=&quot;...MyItemProcessor&quot; /&gt;
&lt;bean class=&quot;...MyItemWriter&quot; /&gt;
</pre>
<p>Embora o Spring Batch esteja atualmente sendo trabalhado para se tornar aderente &agrave; JSR-352, ele vai al&eacute;m da especifica&ccedil;&atilde;o para oferecer aos desenvolvedores uma perfeita integra&ccedil;&atilde;o com outros componentes do ecossistema Spring. No caso do processamento em lote, o Spring Data pode ser aproveitado diretamente como uma inst&acirc;ncia de <i>ItemReader</i> no padr&atilde;o <i>Reader-Processor-Writer</i>, para permitir que os desenvolvedores recuperem <i>chunks</i> de um reposit&oacute;rio de dados do <a href="http://www.springsource.org/spring-data">Spring Data</a>. A vers&atilde;o 2.2.0 do Spring Batch oferece interface simplificada para bancos de dados MongoDB e Neo4J usando o Spring Data.</p>
<p>Al&eacute;m da interface simplificada para leitura de v&aacute;rias fontes de dados, a &uacute;ltima vers&atilde;o do Spring Batch disponibiliza uma extens&atilde;o para configura&ccedil;&atilde;o do Spring Java, de forma a simplificar as funcionalidades de processamento em lote. Para habilitar essa configura&ccedil;&atilde;o simplificada, os desenvolvedores s&oacute; precisam fornecer a anota&ccedil;&atilde;o @EnableBatchProcessing em uma classe anotada com @Configuration. A partir dessa classe, qualquer recurso de processamento em lote, como a JobRepository e JobLauncher, pode ser diretamente injetado sem nenhuma configura&ccedil;&atilde;o adicional.</p>
<pre>
@Configuration
@EnableBatchProcessing
public class AppConfig {
    @Autowired
    private JobBuilderFactory jobs;

    @Bean
    public Job job() {
        return jobs.get(&quot;myJob&quot;).start(step1()).next(step2()).build();
    }

    @Bean
    protected Step step1() {
       ...
    }

    @Bean
    protected Step step2() {
     ...
    }
}
</pre>
<p>Al&eacute;m das melhorias no Spring Batch 2.2.0 para recupera&ccedil;&atilde;o de dados e configura&ccedil;&atilde;o, esse lan&ccedil;amento tamb&eacute;m atualizou sua depend&ecirc;ncia com o framework Spring. Agora os desenvolvedores que quiserem utilizar a &uacute;ltima vers&atilde;o do Spring Batch ter&atilde;o que atualizar a vers&atilde;o do Spring para a 3.1.2 (m&iacute;nima).</p><br><br><br><br><br><br></body></html>
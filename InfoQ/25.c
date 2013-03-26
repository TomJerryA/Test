<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Spring para Apache Hadoop 1.0: Big Data mais perto do Spring</h3><p>A SpringSource lan&ccedil;ou a <a href="http://www.springsource.org/spring-data/hadoop">vers&atilde;o 1.0 do Spring para Apache Hadoop</a>. Esse projeto permite que desenvolvedores escrevam aplica&ccedil;&otilde;es <a href="http://pt.wikipedia.org/wiki/Hadoop">Hadoop</a> de forma integrada ao Spring Framework; tamb&eacute;m facilita a integra&ccedil;&atilde;o com o Spring Batch e o Spring Integration. O Spring para Apache Hadoop &eacute; um subprojeto do Spring Data e &eacute; lan&ccedil;ado sob a licen&ccedil;a open source Apache 2.0.</p> 
<p>Aplica&ccedil;&otilde;es Hadoop normalmente s&atilde;o compostas de uma cole&ccedil;&atilde;o de utilit&aacute;rios de linha de comando, scripts e c&oacute;digo. O Spring para Apache Hadoop fornece um modelo de programa&ccedil;&atilde;o consistente e um modelo de configura&ccedil;&atilde;o declarativa para desenvolver aplica&ccedil;&otilde;es Hadoop.</p> 
<p>As aplica&ccedil;&otilde;es Hadoop agora podem ser implementadas utilizando o modelo de programa&ccedil;&atilde;o do Spring (inje&ccedil;&atilde;o de depend&ecirc;ncias, POJOs, Helper Templates), e rodar como uma aplica&ccedil;&atilde;o Java padr&atilde;o, em vez de como utilit&aacute;rios de linha de comando. O Spring para Apache Hadoop suporta leitura e escrita no sistema de arquivos <a href="http://en.wikipedia.org/wiki/Hadoop_Distributed_File_System#Hadoop_Distributed_File_System">HDFS</a>, execu&ccedil;&atilde;o de <a href="http://en.wikipedia.org/wiki/MapReduce">MapReduce</a>, jobs <a href="http://hadoop.apache.org/docs/stable/streaming.html">Streaming</a> (utilit&aacute;rio para criar e rodar tarefas MapReduce com qualquer execut&aacute;vel ou script atuando como mapper e/ou reducer) ou <a href="http://en.wikipedia.org/wiki/Cascading">Cascading</a> (framework que permite criar e executar fluxos de processamento de dados em qualquer linguagem baseada na JVM, como Java e JRuby), al&eacute;m de interagir com <a href="http://pt.wikipedia.org/wiki/HBase">HBase</a>, <a href="http://en.wikipedia.org/wiki/Apache_Hive">Hive</a> e <a href="http://en.wikipedia.org/wiki/Pig_(programming_tool)">Pig</a>.</p> 
<p>Entre as principais funcionalidades do projeto est&atilde;o:</p> 
<ul> 
 <li>Configura&ccedil;&atilde;o declarativa para criar, configurar e parametrizar a conectividade do Hadoop e dos jobs MapReduce, Streaming, Hive, Pig e Cascading. H&aacute; tamb&eacute;m classes &quot;runner&quot; que executam os diferentes tipos de intera&ccedil;&atilde;o Hadoop: JobRunner, ToolRunner, JarRunner, HiveRunner, PigRunner, CascadeRunner e HdfsScriptRunner.</li> 
 <li>Suporte abrangente para acesso de dados HDFS utilizando qualquer linguagem de script baseada na JVM, como Groovy, JRuby, Jython e Rhino.</li> 
 <li>Classes de template para Pig (PigTemplate) e Hive (HiveTemplate). Essas classes utilit&aacute;rias oferecem tradu&ccedil;&atilde;o de exce&ccedil;&otilde;es, gerenciamento de recursos e funcionalidades leves de mapeamento de objetos.</li> 
 <li>Configura&ccedil;&atilde;o declarativa para HBase e introdu&ccedil;&atilde;o do HBaseTemplate para suporte DAO.</li> 
 <li>Suporte declarativo e program&aacute;tico para Hadoop Tools, incluindo <a href="http://hadoop.apache.org/docs/stable/file_system_shell.html">File System Shell</a> (FsShell) e <a href="http://hadoop.apache.org/docs/stable/distcp.html">Distributed Copy</a> (DistCp).</li> 
 <li>Suporte a seguran&ccedil;a. O Spring para Apache Hadoop leva em conta requisitos de seguran&ccedil;a de um ambiente de execu&ccedil;&atilde;o do Hadoop. Sendo assim, a mudan&ccedil;a de um ambiente de desenvolvimento local para um cluster Hadoop totalmente protegido por Kerberos &eacute; feita de forma transparente.</li> 
 <li>Suporte ao Spring Batch. Com o Batch, m&uacute;ltiplos passos podem ser coordenados de maneira <em>statefull</em> (com estado) e administrados por meio de uma API REST. Por exemplo, a habilidade do Spring Batch em gerenciar o processamento de grandes arquivos pode ser usada para importar e exportar arquivos de um sistema HDFS.</li> 
 <li>Suporte ao Spring Integration. O Spring Integration permite o processamento de fluxos de eventos que podem ser transformados ou filtrados antes de serem lidos e escritos em um sistema HDFS ou outro tipo de armazenamento.</li> 
</ul> 
<p>A seguir s&atilde;o mostrados alguns exemplos de configura&ccedil;&otilde;es e trechos de c&oacute;digo, a maioria obtida no <a href="http://blog.springsource.org/2012/02/29/introducing-spring-hadoop/">blog</a> ou no <a href="http://static.springsource.org/spring-hadoop/docs/current/reference/html/">manual de refer&ecirc;ncia</a> do Spring para Hadoop.</p> 
<p>MapReduce:</p> 
<pre>
    &lt;!-- utiliza a configura&ccedil;&atilde;o padr&atilde;o --&gt;
    &lt;hdp:configuration /&gt;

    &lt;!-- cria o job --&gt;
    &lt;hdp:job id=&quot;word-count&quot;
        input-path=&quot;/input/&quot; output-path=&quot;/ouput/&quot;
        mapper=&quot;org.apache.hadoop.examples.WordCount.TokenizerMapper&quot;
        reducer=&quot;org.apache.hadoop.examples.WordCount.IntSumReducer&quot; /&gt;

    &lt;!-- roda o job --&gt;
    &lt;hdp:job-runner id=&quot;word-count-runner&quot; pre-action=&quot;cleanup-script&quot; post-action=&quot;export-results&quot; job=&quot;word-count&quot; run-at-startup=&quot;true&quot; /&gt;
</pre> 
<p>HDFS:</p> 
<pre>
    &lt;!-- copia um arquivo utilizando Rhino --&gt;
    &lt;hdp:script id=&quot;inlined-js&quot; language=&quot;javascript&quot; run-at-startup=&quot;true&quot;&gt;
        importPackage(java.util)
       
        name = UUID.randomUUID().toString()
        scriptName = &quot;src/main/resources/hadoop.properties&quot;
        // fs - FileSystem instance based on 'hadoopConfiguration' bean
        fs.copyFromLocalFile(scriptName, name)
    &lt;/hdp:script&gt;
</pre> 
<p>HBase:</p> 
<pre>
    &lt;!-- utiliza a configura&ccedil;&atilde;o padr&atilde;o do HBase --&gt;
    &lt;hdp:hbase-configuration /&gt;
       
    &lt;!-- faz a liga&ccedil;&atilde;o com a configura&ccedil;&atilde;o hbase --&gt;
    &lt;bean id=&quot;hbaseTemplate&quot; class=&quot;org.springframework.data.hadoop.hbase.HbaseTemplate&quot; p:configuration-ref=&quot;hbaseConfiguration&quot; /&gt;

    // l&ecirc; cada linha de uma HBaseTable (Java)
    List rows = template.find(&quot;HBaseTable&quot;, &quot;HBaseColumn&quot;, new RowMapper() {
        @Override
        public String mapRow(Result result, int rowNum) throws Exception {
            return result.toString();
        }
    }));
</pre> 
<p>Hive:</p> 
<pre>
    &lt;!-- configura a fonte de dados --&gt;
    &lt;bean id=&quot;hive-driver&quot; class=&quot;org.apache.hadoop.hive.jdbc.HiveDriver&quot; /&gt;
    &lt;bean id=&quot;hive-ds&quot; class=&quot;org.springframework.jdbc.datasource.SimpleDriverDataSource&quot; c:driver-ref=&quot;hive-driver&quot; c:url=&quot;${hive.url}&quot; /&gt;

    &lt;!-- configura a declara&ccedil;&atilde;o JdbcTemplate padr&atilde;o --&gt;
    &lt;bean id=&quot;hiveTemplate&quot; class=&quot;org.springframework.jdbc.core.JdbcTemplate&quot; c:data-source-ref=&quot;hive-ds&quot;/&gt;
</pre> 
<p>Pig:</p> 
<pre>
    &lt;!-- roda um script pig externo --&gt;
    &lt;hdp:pig-runner id=&quot;pigRunner&quot; run-at-startup=&quot;true&quot;&gt;
        &lt;hdp:script location=&quot;pig-scripts/script.pig&quot;/&gt;
    &lt;/hdp:pig-runner&gt;
</pre> 
<p>Para come&ccedil;ar com o Spring para Apache Hadoop, baixe o <a href="http://www.springsource.com/download/community?project=Spring%20Data%20Hadoop">projeto</a> ou utilize o artefato Maven <em>org.springframework.data:spring-data-hadoop:1.0.0.RELEASE</em><em>.</em> H&aacute; um exemplo dispon&iacute;vel (<a href="http://static.springsource.org/spring-hadoop/docs/current/reference/html/batch-wordcount.html">Wordcount</a>) no site oficial e tamb&eacute;m um webinar no YouTube (<a href="http://www.youtube.com/watch?v=wlTnBzQ6KDU">Introducing Spring Hadoop</a>).</p> 
<p>O Spring para Apache Hadoop requer o JDK 6.0 ou superior, Spring Framework 3.0 ou mais recentec (recomenda-se a vers&atilde;o 3.2) e o Apache Hadoop 0.20.2 (recomenda-se a vers&atilde;o 1.0.4). As vers&otilde;es Hadoop YARN, NextGen ou 2.x n&atilde;o s&atilde;o suportadas. Qualquer distribui&ccedil;&atilde;o do Apache Hadoop 1.0.x deve ser suportada; isso inclui distribui&ccedil;&otilde;es como Apache Hadoop padr&atilde;o, Cloudera CDH3 e CDH4, e Greenplum HD.</p> 
<p>Para informa&ccedil;&otilde;es mais detalhadas, consulte o <a href="http://static.springsource.org/spring-hadoop/docs/1.0.0.RELEASE/reference/html/">Manual de Refer&ecirc;ncia</a> e o <a href="http://static.springsource.org/spring-hadoop/docs/current/api/">Javadoc</a> do projeto. O <a href="https://github.com/SpringSource/spring-hadoop">c&oacute;digo-fonte</a> e <a href="https://github.com/SpringSource/spring-hadoop-samples">exemplos</a> est&atilde;o dispon&iacute;veis no GitHub.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
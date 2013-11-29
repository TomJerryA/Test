<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>AWS anuncia três novos tipos de instâncias</h3><p>Durante a segunda edi&ccedil;&atilde;o do seu evento <a href="http://reinvent.awsevents.com/">re:invent</a> a Amazon Web Services (AWS) anunciou tr&ecirc;s novos tipos de inst&acirc;ncia para o seu servi&ccedil;o Elastic Compute Cloud (EC2), que oferece infraestrutura como servi&ccedil;o. S&atilde;o as <a href="http://aws.typepad.com/aws/2013/11/coming-soon-the-i2-instance-type-high-io-performance-via-ssd.html">inst&acirc;ncias do tipo I2</a>, apropriadas para aplica&ccedil;&otilde;es que possuam fortes requisitos de leitura e escrita de dados que usam discos de estado s&oacute;lido (SSD: Solid State Disk), <a href="http://aws.typepad.com/aws/2013/11/a-generation-of-ec2-instances-for-compute-intensive-workloads.html">inst&acirc;ncias do tipo C3</a> nas quais cada CPU virtual est&aacute; diretamente ligada a uma hyper-thread para situa&ccedil;&otilde;es nas quais haja maior carga de processamento (workload) e, finalmente, as <a href="http://aws.typepad.com/aws/2013/11/build-3d-streaming-applications-with-ec2s-new-g2-instance-type.html">inst&acirc;ncias do tipo G2</a> que oferecem processamento em GPUs Nvidia aplic&aacute;veis em projetos que requeiram processamento gr&aacute;fico (3D por exemplo).</p>
<p>As maiores inst&acirc;ncias do tipo I2 (i2.8xlarge) ir&atilde;o combinar 32 vCPUs (CPUs virtuais), 244 Gb de RAM e oito drives SSD de 720 Gb. S&atilde;o capazes de processar 350.000 opera&ccedil;&otilde;es de leitura e grava&ccedil;&atilde;o por segundo (IOPS) e 320.000 opera&ccedil;&otilde;es de escrita por segundo. O foco s&atilde;o aplica&ccedil;&otilde;es que necessitam de alto desempenho em opera&ccedil;&otilde;es de acesso rand&ocirc;mico de I/O como, por exemplo, sistemas transacionais e bancos de dados NoSQL. Esta fam&iacute;lia possu&iacute; uma vers&atilde;o menos poderosa, a i2.large, que &eacute; dezesseis vezes menor que a vers&atilde;o top de linha em todas as caracter&iacute;sticas. O hardware usado por estas inst&acirc;ncias &eacute; baseado em processadores Intel Xeon E5-2670v2 com clock de 2.5 Ghz. O arquiteto da Netflix, Adrian Cockroft comentou que &quot;voc&ecirc; facilmente anula um benchmark baseado em inst&acirc;ncias m1.small ao compar&aacute;-lo com os resultados que obtemos com as inst&acirc;ncias i2.8xlarge&quot;.</p>
<p>J&aacute; as inst&acirc;ncias C3 usam CPUs mais r&aacute;pidas que as usadas pelas I2, no caso, baseadas nos processadores Intel Xeon E5-2680v2 com clock de 2.8Ghz por&eacute;m oferecendo menos mem&oacute;ria RAM e espa&ccedil;o de armazenamento em SSD. Esta fam&iacute;lia de inst&acirc;ncias t&ecirc;m como foco aplica&ccedil;&otilde;es que lidem com cargas de trabalho mais pesadas como por exemplo computa&ccedil;&atilde;o de alta performance (HPC) e aplica&ccedil;&otilde;es que precisem analisar uma maior quantidade de dados usando frameworks como o Hadoop. Al&eacute;m de uma maior proximidade entre as CPUs virtuais e f&iacute;sicas, a Amazon tamb&eacute;m est&aacute; oferecendo melhor performance de rede em seu servi&ccedil;o de cloud privada (Virtual Private Cloud - VPC) com maior throughput e menor lat&ecirc;ncia, por&eacute;m para tirar proveito destes recursos o usu&aacute;rio deve habilitar a Hardware Virtual Machine (HVM) com <a href="http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enhanced-networking.html">aperfei&ccedil;oamento de rede</a>. Para facilitar a ado&ccedil;&atilde;o destas inst&acirc;ncias a AWS inclusive j&aacute; oferece algumas imagens (AMIs) pr&eacute;-configuradas.</p>
<p>No caso das inst&acirc;ncias do tipo G2 h&aacute; apenas um tipo ofertado, que &eacute; o g2.2xlarge, que oferece 8 CPUs virtuais (baseadas nos antigos processadores Sandy Bridge da Intel), 15 Gb de RAM e 60 GB de armazenamento em SSD. Seu grande diferencial est&aacute; na presen&ccedil;a da GPU Nvidia GK104 com 1536 n&uacute;cleos e 4 GB de mem&oacute;ria de v&iacute;deo. Seu foco s&atilde;o aplica&ccedil;&otilde;es que requeiram intenso processamento gr&aacute;fico como codifica&ccedil;&atilde;o de v&iacute;deo e renderiza&ccedil;&atilde;o em 3D. &Eacute; importante mencionar que a Amazon alerta que a inst&acirc;ncia do tipo G2 n&atilde;o &eacute; apropriada para o processamento gr&aacute;fico de uso geral, pois n&atilde;o possu&iacute; suporte a ponto flutuante de dupla precis&atilde;o e corre&ccedil;&atilde;o de erros de mem&oacute;ria, tal como, nas inst&acirc;ncias do tipo CG1.</p>
<p>Assim que as inst&acirc;ncias do tipo I2 estiverem dispon&iacute;veis, os clientes da Amazon poder&atilde;o escolher entre 28 <a href="https://aws.amazon.com/ec2/instance-types/">tipos de inst&acirc;ncias</a> divididas em 7 fam&iacute;lias diferentes. &Eacute; sem sombra de d&uacute;vidas um aspecto bem grande de escolhas que ir&aacute; exigir dos seus clientes aten&ccedil;&atilde;o redobrada na hora de optar pelo tipo de inst&acirc;ncia mais adequado &agrave;s necessidades de escalabilidade e desempenho dos projetos.</p>
<p><strong>Nota importante:</strong> at&eacute; a tradu&ccedil;&atilde;o desta not&iacute;cia os tr&ecirc;s tipos de inst&acirc;ncia ainda n&atilde;o estavam dispon&iacute;veis para a regi&atilde;o S&atilde;o Paulo da AWS.</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Armazenamento Offline com o LocalForage</h3><p>A funda&ccedil;&atilde;o Mozilla lan&ccedil;ou o <a href="https://github.com/mozilla/localForage">localForage</a>, uma nova biblioteca JavaScript que promete simplificar o processo de armazenamento de dados offline em aplica&ccedil;&otilde;es web.</p>
<p>Embora n&atilde;o seja uma tecnologia recente nos navegadores, o suporte offline sempre foi muito fragmentado devido &agrave; <a href="http://www.html5rocks.com/en/tutorials/offline/whats-offline/#toc-html5-offline-storage">v&aacute;rias op&ccedil;&otilde;es dispon&iacute;veis</a>. O que torna esta biblioteca &uacute;nica &eacute; o fato que ela tenta combinar o melhor dos mundos: as funcionalidades de algumas das mais recentes tecnologias (assincronismo e suporte ao blob) com uma simples API. Isto oferece uma poderosa capacidade para aplica&ccedil;&otilde;es web offline, tornando-os mais pr&oacute;ximo de seus colegas m&oacute;veis nativos e mais intuitivos para os desenvolvedores trabalharem.</p>
<p>Uma das primeiras alternativas dispon&iacute;veis foi o<a href="http://www.w3schools.com/html/html5_webstorage.asp">localStorage</a> que prov&ecirc; acesso simples a dados para armazenamento offline. Entretanto <a href="http://calendar.perfplanet.com/2011/localstorage-read-performance/">testes de benchmark</a> mostraram que ele &eacute; lento, s&iacute;ncrono e n&atilde;o pode manipular blobs bin&aacute;rios (por exemplo, cach&ecirc; de arquivos mp3 n&atilde;o &eacute; poss&iacute;vel). Desde ent&atilde;o, duas outras op&ccedil;&otilde;es populares surgiram - <a href="https://developer.mozilla.org/en-US/docs/IndexedDB">IndexedDB</a> e <a href="http://html5doctor.com/introducing-web-sql-databases/">Web SQL</a> - que s&atilde;o ass&iacute;ncronos, velozes e suportam grandes conjuntos de dados. A desvantagem destas duas tecnologias &eacute; o fato de suas APIs n&atilde;o serem muito simples de usar e tamb&eacute;m n&atilde;o serem <a href="http://csimms.botonomy.com/2011/05/html5-storage-wars-localstorage-vs-indexeddb-vs-web-sql.html">suportados pela maioria dos navegadores</a>.</p>
<p>O recente lan&ccedil;amento do localForage tenta resolver esses problemas unificando tecnologias - assincronismo e suporte a blob a partir do IndexedDB e Web SQL com a sintaxe simples do localStorage:</p>
<pre>
var settings = {color: 'black', font: 'Helvetica'};
localForage.setItem('settings', settings, function(result) {  
console.log(result);
});
</pre>
<p>A inclus&atilde;o do suporte ao IndexedDB e Web SQL permite armazenar mais dados para aplica&ccedil;&otilde;es web que o localStorage sozinho poderia armazenar. A natureza sem bloqueios da API torna as aplica&ccedil;&otilde;es web mais r&aacute;pidas pelo fato de n&atilde;o ter que manipular a thread principal e suas chamadas get/set. Adicionalmente, o localForage suporta callbacks e <a href="http://www.promisejs.org/">ES6 Promises</a> deixando a escolha da melhor implementa&ccedil;&atilde;o para o desenvolvedor.</p>
<p>A biblioteca carrega e gerencia automaticamente os drivers para o IndexedDB, Web SQL e localStorage, assim n&atilde;o &eacute; necess&aacute;rio gerenciar isto manualmente (o melhor driver &eacute; escolhido independente do navegador em que a aplica&ccedil;&atilde;o est&aacute; sendo executada). Quando nem o IndexedDB nem o Web SQL est&atilde;o dispon&iacute;veis, localForage volta para o localStorage, assim pelo menos os dados b&aacute;sicos podem ser armazenados offline (embora sem suporte a blob e muito mais lento).</p>
<p>Todos navegadores modernos s&atilde;o suportados pelo localForage. O armazenamento ass&iacute;ncrono est&aacute; dispon&iacute;vel em todos navegadores, com a vers&atilde;o que suporta o localStorage em parenteses:</p>
<ul class="c8 lst-kix_qfhyaauhrc6d-0 start"> 
 <li>Navegador Android 2.1</li> 
 <li>BlackBerry 7</li> 
 <li>Chrome 23 (Chrome 4.0 com localStorage)</li> 
 <li>Chrome para o Android 32</li> 
 <li>Firefox 10 (Firefox 3.5 com localStorage)</li> 
 <li>Firefox para Android 25</li> 
 <li>IE 10 (IE 8 com localStorage)</li> 
 <li>IE Mobile 10</li> 
 <li>Opera 15 (Opera 10.5 com localStorage)</li> 
 <li>Opera Mobile 11</li> 
 <li>PhoneGap/Apache Cordova 1.2.0</li> 
 <li>Safari 3.1</li> 
</ul><br><br><br><br><br><br></body></html>
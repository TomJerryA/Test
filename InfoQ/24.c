<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Cordova 3.3.0: Publicando Aplicações Chrome no Android e iOS</h3><p>Desenvolvedores podem agora publicar aplica&ccedil;&otilde;es Chrome no Android e iOS com o Apache Cordova 3.3.0.</p>
<p>Seis semanas ap&oacute;s a <a href="http://www.infoq.com/br/news/2014/01/PhoneGap-3.3?utm_campaign=infoq_content">Adobe disponibilizar o PhoneGap 3.3</a>, o Cordova 3.3.0 foi disponibilizado no <a href="https://build.phonegap.com/">PhoneGap Build</a>. Al&eacute;m do suporte ao Android KitKat, o Cordova 3.3.0 adicionou suporte para <a href="https://developers.google.com/chrome-developer-tools/docs/remote-debugging">depura&ccedil;&atilde;o remota da webview do Chrome</a> no Android, e <a href="http://moduscreate.com/enable-remote-web-inspector-in-ios-6/">depura&ccedil;&atilde;o remota com o Safari</a> no iOS. A nota de lan&ccedil;amento cont&eacute;m detalhes de cada sistema operacional suportado: <a href="https://github.com/apache/cordova-ios/blob/master/RELEASENOTES.md">iOS</a>,<a href="https://github.com/apache/cordova-android/blob/master/RELEASENOTES.md">Android</a>,<a href="http://cordova.apache.org/announcements/2013/12/16/cordova-330.html#whats_new_in_windows_phone_7__8">Windows</a>. O Cordova 2.5.0 e 2.7.0 se tornar&atilde;o obsoletos no futuro pr&oacute;ximo, desenvolvedores Blackberry, WebOS ou Symbian s&atilde;o convidados a usar a vers&atilde;o 2.9.0.</p>
<p>Em setembro, a Google <a href="http://chrome.blogspot.ro/2013/09/a-new-breed-of-chrome-apps.html">anunciou</a> a possibilidade de criar <a href="https://chrome.google.com/webstore/category/collection/for_your_desktop">aplica&ccedil;&otilde;es Chrome</a> que podem ser publicadas para o desktop. Essas aplica&ccedil;&otilde;es podem ser executadas no Windows, Mac ou Linux em modo online ou offline. Recentemente, a <a href="http://blog.chromium.org/2014/01/run-chrome-apps-on-mobile-using-apache.html">Google ampliou o alcance dos aplicativos do Chrome para plataformas m&oacute;veis</a>, Android e iOS atrav&eacute;s do Cordova 3.3.0.</p>
<p>Para criar uma aplica&ccedil;&atilde;o Chrome para dispositivos m&oacute;veis, os desenvolvedores precisam usar uma s&eacute;rie de ferramentas baseadas no Node.js, JDK 7, Android SDK 4.4.2, e Apache Ant para o Android, ou Xcode 5, ios-deploy, ios-sim para o iOS e usar o Cordova para empacotar a aplica&ccedil;&atilde;o no shell nativo, ent&atilde;o publicar no Google Play ou Apple App Store.</p>
<p>As seguintes APIs Chrome foram disponibilizadas para aplica&ccedil;&otilde;es m&oacute;veis:</p>
<blockquote> 
 <ul> 
  <li><a href="http://developer.chrome.com/apps/identity.html">identity</a> - autentica usu&aacute;rios usando OAuth2 sem perguntar por senhas;</li> 
  <li><a href="http://developer.chrome.com/apps/google_wallet.html">payments</a> (somente no Android atualmente) - vende produtos virtuais dentro de sua aplica&ccedil;&atilde;o m&oacute;vel;</li> 
  <li><a href="http://developer.chrome.com/apps/pushMessaging.html">pushMessaging</a> - envia mensagens de sua aplica&ccedil;&atilde;o para seu servidor;</li> 
  <li><a href="http://developer.chrome.com/apps/socket.html">sockets</a> - envia e recebe dados atrav&eacute;s de uma rede usando TCP e UDP;</li> 
  <li><a href="http://developer.chrome.com/apps/notifications.html">notifications</a> (somente no Android atualmente) - enviar notifica&ccedil;&otilde;es ricas de seu aplicativo m&oacute;vel;</li> 
  <li><a href="https://developer.chrome.com/apps/storage.html">storage</a> - armazena e recupera dados chave-valor localmente;</li> 
  <li><a href="https://developer.chrome.com/apps/syncFileSystem.html">syncFileSystem</a> - armazena e recupera arquivos de backup do Google Drive;</li> 
  <li><a href="http://developer.chrome.com/apps/alarms.html">alarms</a> - executa tarefas periodicamente.</li> 
 </ul> 
</blockquote>
<p>Al&eacute;m desses, os desenvolvedores podem fazer uso de um grande n&uacute;mero de APIs Cordova fornecendo amplo acesso &agrave; funcionalidade nativa.</p><br><br><br><br><br><br></body></html>
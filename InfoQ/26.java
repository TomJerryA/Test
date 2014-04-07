<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Ratchet Becomes a Real Framework, Gets a New Home</h3><p>The mobile application prototyping tool, <a href="http://goratchet.com/">Ratchet</a>, has been promoted to a full application framework. Version 2.0.2 of Ratchet was has been released and is a complete re-write (from version 1) using the <a href="http://sass-lang.com/">SASS</a> CSS pre-processor. Besides the overhaul, Ratchet now sports iOS and Android styles in addition to the existing Base Ratchet theme. A new icon font called &quot;Ratcheticons&quot; is now available, as well as <a href="http://goratchet.com/examples/">three example applications</a> to show off the different themes. The documentation has been overhauled for the new release and the project itself has been moved to become part of the <a href="https://github.com/twbs">Bootstrap GitHub orginization</a>.</p>
<p>Ratchet originated as a set of HTML/CSS prototypes for the Twitter for iOS native application. After seeing how critical these prototypes were to the development process, the team decided to open source it as a mobile prototyping kit. It soon became clear to the team that not only was Ratchet well suited for building mobile prototypes, but also full fledged mobile applications.</p>
<p>Originally written in plain CSS, version 2.0.2 now uses the <a href="http://sass-lang.com/">SASS</a> pre-processor language. Ratchet's co-creator <a href="http://www.twitter.com/connors">Connor Sears</a> said that the SASS re-write came from wanting the &quot;flexibilty of a preprocessor&quot;. Connor notes that he chose SASS simply because it was what he was most familiar with it. The Bootstrap project itself (of which Ratchet is now a part) uses the <a href="http://lesscss.org/">LESS</a> pre-processor for CSS.</p>
<p>Ratchet originally had only one style that could be tweaked with CSS. There are now three styles to support multiple form factors. The original Base style is still present, but there are now iOS and Android styles which better suit their respective operating systems. For the most part, this just involves styling, but there are some components such as the Popover which behave very differently given the specified platform.</p>
<p><img alt="" src="http://www.infoq.com/resource/news/2014/04/ratchet-2-real-framework-new-hom/en/resources/ratchet-themes.jpg" _href="img://ratchet-themes.jpg" _p="true" /></p>
<p>Ratchet does not try and do anything specific in terms of platform or browser with the CSS. It aims to keep things simple so that it is easier to understand and implement.</p>
<p>The new Ratcheticons icon font contains 45 common application icons. These icons are displayed with HTML <a href="https://developer.mozilla.org/en-US/docs/Web/CSS/Pseudo-elements">Pseudo-elements</a>. For instance, a gear icon can be displayed with a simple <small><b>span</b></small> and a CSS class.</p>
<pre>
&lt;span class=&quot;icon icon-gear&quot;&gt;&lt;/span&gt; </pre>
<p>The class for the gear icon contains the Unicode for the designated font character which is displayed in the <small><b>:before</b></small> Pseudo-element.</p>
<pre>
.icon-code:before {     content: '\e812'; } </pre>
<p>Three full fledged application examples are now available with the overhauled Ratchet documentation. These examples allow developer to test Ratchet on their mobile devices as well as provide a starting point for new applications. Right now, Ratchet has <a href="http://goratchet.com/examples/app-movies/">Movie Finder</a>(Base Theme), <a href="http://goratchet.com/examples/app-ios-mail/">iOS Mail</a>(iOS Theme) and <a href="http://goratchet.com/examples/app-android-notes/">Android Notes App</a>(Android Theme) examples.</p>
<p>Ratchet has also now been moved to the Bootstrap GitHub repository. Connor explained this move saying, &quot;Ratchet has always been kind of a 'little brother' to Bootstrap. It just felt natural to move Ratchet into the Bootstrap org.&quot; He pointed out that while Ratchet has been moved into the Bootstrap org, there are no plans to &quot;merge&quot; the frameworks. &quot;we'll continue to bring our [Ratchet and Bootstrap] CSS architecture into parity. Basically, I want people who are familiar with Bootstrap [to] feel at home using Ratchet's CSS.</p>
<p>Ratchet has gained a lot of popularity on Github now with over 7,900 stars. Bootstrap itself has over 66K stars by comparison. It can be downloaded from the <a href="http://goratchet.com/">official Ratchet site</a>, or the <a href="https://github.com/twbs/ratchet">twbs Github repository</a>.</p><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Strengthening HTTP</h3><p>We've reported before about the work going on in the <a href="http://www.infoq.com/news/2012/06/spdy-websockets">HTTPbis Working Group</a> to define <a href="http://www.infoq.com/news/2012/11/http20-first-draft">HTTP 2.0</a>. Recently Mark Nottingham, the chair of the Working Group, posted his <a href="http://www.mnot.net/blog/2014/01/04/strengthening_http_a_personal_view">personal view</a> on the efforts going on in the group around security requirements within the protocol.</p>
<blockquote>
 Recently, one of the hottest topics in the Internet protocol community has been whether the newest version of the Web’s protocol, 
 <a href="http://http2.github.io/">HTTP/2</a>, will require, encourage or indeed say 
 <em>anything</em> about the use of encryption in response to the pervasive monitoring attacks revealed to the world by 
 <a href="http://www.theguardian.com/world/edward-snowden">Edward Snowden</a>.
</blockquote>
<p>Mark gives a brief history of the work so far, particularly as it relates to SPDY and security:</p>
<blockquote>
 When Mike (Belshe) and Roberto (Peon) brought SPDY to us (long before “Snowden” became a household word), its implementations already required use of 
 <a href="http://en.wikipedia.org/wiki/Transport_Layer_Security">TLS</a> for encryption. This was both for pragmatic reasons (it’s really hard to introduce a new version of HTTP if something in the middle doesn’t know about it) and loftier ones.
</blockquote>
<p>Due to use cases at the time that did not require security and the fact that mandating it was contentious ...</p>
<blockquote>
 [...] neither 
 <a href="http://http2.github.io/http2-spec/">the specification</a> nor 
 <a href="http://datatracker.ietf.org/wg/httpbis/charter/">our charter</a> says anything about this issue; the tacit understanding being that we’d make it possible to use HTTP/2 over encrypted or unencrypted connections, and implementations would decide what to support.
</blockquote>
<p>With the advent of Snowden and revelations about <a href="http://www.theguardian.com/world/2013/jul/31/nsa-top-secret-program-online-data">XKeyscore</a>, things took a significant turn within the IETF and they held an <a href="http://www.ietf.org/proceedings/87/slides/slides-87-httpbis-3.pdf">extra session</a> at a Working Group meeting in Berlin which resulted in strong consensus to improving HTTP security through the use of more encryption. There were a lot of further discussions within the IETF over the following months and meetings:</p>
<blockquote>
 It was very clear that we had a shared goal of increasing the use of TLS with HTTP — thereby protecting against pervasive monitoring and other attacks — but the different means of doing so attracted a lot of debate and disagreement over how we could best achieve this goal, and what the appropriate tradeoffs are.
</blockquote>
<p>Mark discussed that there was a lot of support from the Chrome and Firefox developers, such that they would only support HTTP/2 if it was protected by TLS. He also spoke with other browser developers and security experts to formulate what he thought was the best way forward:</p>
<blockquote>
 [...] for the common Web browsing case, HTTP/2 servers will need to use TLS if they want to interoperate with the broadest selection of browsers — just as Mike and Roberto did for SPDY. Importantly, though, we don’t necessarily need to require the use of TLS in the protocol specification itself.
</blockquote>
<p>Mark then goes on to give more details behind his proposal and how whilst some groups want more security, others believe it is not appropriate for the IETF to mandate encryption for all uses of HTTP/2. Under these circumstances it is difficult for the IETF to come to a decision, especially around problems like this which are &quot;political&quot;, in Mark's term:</p>
<blockquote>
 It’s a political decision not because doing so casts governments as attackers, but because HTTP is a deployed protocol with lots of existing stakeholders, like proxy vendors, network operators, corporate firewalls and so on. Requiring encryption with HTTP/2 means that these stakeholders get disenfranchised.
</blockquote>
<p>However, Mark believes that the IETF and the Working Group can facilitate the necessary discussions around the pros and cons of the various options by ensuring that there is flexibility and precision within the HTTP/2 protocol.</p>
<blockquote>
 For example, in the current design of HTTP the decision as to whether to use encryption is completely up to the server; the only thing the user can do is observe whether a URL is “HTTP” or “HTTPS” (or maybe watch a lock icon) and decide whether they can continue surfing. A more balanced Web would allow clients to give input into this decision too, with some carrot to entice servers to support encryption — such as only supporting HTTP/2 when it is encrypted, just as Firefox and Chrome are doing.
</blockquote>
<p>In this situation the decision is made by the browser vendors rather than the standard. So what next? Well there's another HTTPbis Working Group meeting coming up in <a href="https://github.com/http2/wg_materials/blob/master/interim-14-01/arrangements.md">Zurich</a> and Mark has asked for proposals to address the <a href="https://github.com/http2/http2-spec/issues/314">core problem</a>:</p>
<blockquote>
 A number of browser implementers have stated an intent to only implement HTTP/2 over TLS for traffic over the &quot;open&quot; internet. They can achieve that today by only implementing HTTP/2 for https:// URIs, requiring site that wish to use the new protocol to redirect http:// URIs, possibly using HSTS to &quot;pin&quot; that upgrade. As such, we do not necessarily need to specify this with requirements (e.g., with a MUST or MUST NOT); those sites that want to use the new protocol with these browsers will implement the pattern above. However, to promote interoperability, we might want to give guiding language or even requirements to frame this. This issue is specifically for collecting proposals for such text.
</blockquote>
<p>This would mean that the HTTP/2 standard would not require TLS, but browser implementations may do so. However, as Mark points out, those browser implementations which subsequently mandate TLS with HTTP/2 may then feel pressure to allow corporate proxies to inspect traffic etc. and if that happens it is important that responses are handled in a coordinated manner to preseve interoperability of the standard. Mark concludes with the reminder that no decisions have yet been made and that there is still time for some other outcome. Also the Working Group is always interested in <a href="http://lists.w3.org/Archives/Public/ietf-http-wg/">hearing from others</a> on their opinions around this debate. After all, decisions made by the IETF Working Group are likely to impact many of us in the future.</p><br><br><br><br><br><br></body></html>
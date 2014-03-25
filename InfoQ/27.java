<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Docker Index Offers Private Repositories, Webhooks And Other Services</h3><p><a href="http://www.docker.com/">Docker Inc.</a>, the company behind <a href="https://www.docker.io/">Docker</a>, introduced a range of new services, including its first paid offering: <a href="https://index.docker.io/help/docs/#repositories">private repositories</a>. <a href="https://index.docker.io/">Docker index</a> now also offers webhooks, triggers and links for <a href="https://index.docker.io/help/docs/#trustedbuilds">trusted builds</a> and e-mail notifications.</p>
<p>Docker index is a <a href="https://docs.docker.io/en/latest/terms/registry/">registry</a> for Docker <a href="https://docs.docker.io/en/latest/terms/image/#image-def">images</a> <a href="https://docs.docker.io/en/latest/terms/repository/#repository-def">repositories</a>. A repository is the way to share pre-built images, avoiding the need to recreate them every time by everyone. Although a rough analogy, repositories are to Docker what <a href="http://docs.vagrantup.com/v2/boxes.html">boxes</a> are to Vagrant. With the availability of private repositories it is now possible to control who can push or pull into a repository. It is now also possible to browse repositories by image tags and see the file system changes introduced by each.</p>
<p>Successful repository pushes now trigger webhooks, when configured. The webhook URL will receive an HTTP POST with the following JSON payload:</p>
<pre>
{
   &quot;push_data&quot;:{
      &quot;pushed_at&quot;:1385141110,
      &quot;images&quot;:[
         &quot;imagehash1&quot;,
         &quot;imagehash2&quot;,
         &quot;imagehash3&quot;
      ],
      &quot;pusher&quot;:&quot;username&quot;
   },
   &quot;repository&quot;:{
      &quot;status&quot;:&quot;Active&quot;,
      &quot;description&quot;:&quot;my docker repo that does cool things&quot;,
      &quot;is_trusted&quot;:false,
      &quot;full_description&quot;:&quot;This is my full description&quot;,
      &quot;repo_url&quot;:&quot;https://index.docker.io/u/username/reponame/&quot;,
      &quot;owner&quot;:&quot;username&quot;,
      &quot;is_official&quot;:false,
      &quot;is_private&quot;:false,
      &quot;name&quot;:&quot;reponame&quot;,
      &quot;namespace&quot;:&quot;username&quot;,
      &quot;star_count&quot;:1,
      &quot;comment_count&quot;:1,
      &quot;date_created&quot;:1370174400,
      &quot;dockerfile&quot;:&quot;my full dockerfile is listed here&quot;,
      &quot;repo_name&quot;:&quot;username/reponame&quot;
   }
}
</pre>
<p><a href="http://blog.docker.io/2013/11/introducing-trusted-builds/">Trusted Builds</a> is a service which allows to connect a repository to a GitHub account and add a post commit hook to a GitHub repository. This hook triggers a build and updates the image inside Docker index, maintaining a relationship between the image and the corresponding <a href="https://docs.docker.io/en/latest/reference/builder/">Dockerfile</a>.</p>
<p>Trusted Builds received two enhancements: links and triggers. Links give the capability to synchronize Trusted Build repositories so that any update to a linked Trusted Build triggers an update on the other Trusted Build. Triggers give a simple process to start a repository build, without having to commit anything to GitHub, like so:</p>
<pre>
  $ curl --data &quot;build=true&quot; -X POST https://index.docker.io/u/samalba/docker-registry/trigger/b2562468-aea0-11e3-a39e-b6db5999dfec/
</pre>
<p>Finally, Docker index users can now be notified by e-mail on some events: when a Trusted Build or when another user stars or comments a repository.</p>
<p>Docker index's new services increase the choice for Docker registries, since&nbsp;<a href="https://quay.io/">Quay.io</a> already offered similar capabilities to the ones now announced.</p>
<p>Private repositories are the first <a href="https://index.docker.io/plans/">commercial offering</a> of Docker Inc., although there are plans to add more paid services, as <a href="http://blog.docker.io/2014/03/introducing-private-repos-webhooks-and-more/">stated</a> at Docker's blog:</p>
<blockquote>
  All services on Docker.io to this point have been freely available, and we feel this is important in fostering an active, growing community around Docker. For this reason, most of Docker.io's services will continue to be free but, as Ben has already publicly shared, to support continued investment in Docker we will over time offer optional pay-for services. Private repos is the first example of this. 
</blockquote>
<p>The pricing plans start at 7$/month for at most five repositories up to 50$/month for a maximum of fifty repositories.</p><br><br><br><br><br><br></body></html>
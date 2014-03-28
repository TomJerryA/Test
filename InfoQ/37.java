<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Meteor 0.7.1 Release Brings Dev Accounts, Further Improvements</h3><p>Matt DeBergalis has released version 0.7.1 of <a href="http://www.meteor.com">Meteor</a>, with the improvements to <a href="http://docs.mongodb.org/manual/reference/glossary/#term-oplog">oplog</a> and <a href="https://github.com/meteor/meteor/tree/master/packages/minimongo">minimongo,</a> CSS preprocessing, and Meteor developer accounts.</p>
<p>Version 0.7.1 includes added support to minimongo for what DeBergalis refers to on the <a href="https://www.meteor.com/blog">Meteor blog</a> as “more of the ‘estoteric corners’ of the MongoDB query language.&quot; With the new release comes better matching for Mongo's behavior when there are arrays in the document, as well as improved support for $nin, $ne, $not.</p>
<p>Aside from minimongo (Meteor's client-side Mongo emulator) improvements, the new release brings CSS preprocessing and sourcemaps, including:</p>
<ul> 
 <li>Add sourcemap support for CSS stylesheet preprocessors. Use sourcemaps for stylesheets compiled with LESS.</li> 
 <li>Improve CSS minification to deal with @import statements correctly.</li> 
 <li>Lint CSS files for invalid @ directives.</li> 
 <li>Change the recommended suffix for imported LESS files from .lessimport to .import.less. Add .import.styl to allow stylus imports. .lessimport continues to work but is deprecated.</li> 
</ul>
<p>Oplog support has been available since Meteor 0.7.0, and DeBergalis says the 0.7.1 release “extends the set of MongoDB queries supported by the oplog driver to cover most of the common queries needed in production apps.&quot;</p>
<p>Oplog improvements in version 0.7.1 include the oplog tailing implementation for getting real-time database updates from MongoDB. As well as adding optimisations to avoid needless data fetches from MongoDB, Meteor version 0.7.1 also adds “support for all operators except $where and $near.&quot;</p>
<p>Meteor 0.7.1 launches developer accounts, a&nbsp; new login system for developers to manage deployed apps, replacing the old per-application password when deploying apps.</p>
<p>When deploying an app, developers will now be prompted for an email address. DeBergalis says the benefits of the Meteor developer accounts are various, and include being able to log in and log out from the command line, as well as being able to “type meteor whoami for that warm UNIXy feeling, and run meteor authorized to give other Meteor developers permissions to deploy your app and access its database and logs.&quot; Users should type meteor help at the command line to see the full suite of options.</p>
<p>Developers working on apps for the Meteor community are advised that users can sign in with their Meteor developer accounts, in the same way as the accounts-github and accounts-facebook packages allows them to sign in with their GitHub and Facebook accounts.</p>
<p>Version 0.7.1 includes a raft of updated dependencies, among them node: 0.10.25 (updated from 0.10.22), noting the workaround for specific Node versions from 0.7.0 is now removed; 0.10.25+ is supported. Other updated dependencies include coffeescript: 1.7.1 (from 1.6.3), websocket-driver: 0.3.2 (from 0.3.1) and jquery-waypoints: 2.0.4 (from 1.1.7) -- which contains backwards-incompatible changes.</p>
<p>Commenting on DeBergalis’s announcement of the 0.7.1 release on <a href="https://news.ycombinator.com/item?id=7293860">Hacker News</a>, in a discussion around adding realtime to a simple rails app , user iguana <a href="https://news.ycombinator.com/item?id=7294214">responds</a> “meteor.js is really cool, but it is not ready for production.&quot;</p>
<p>DeBergalis <a href="https://news.ycombinator.com/item?id=7294251">replies</a> “Sure it is -- people are using Meteor in production already, and on multiple servers.&quot;</p>
<p>The 0.7.1 release was quickly followed by 0.7.1.2, responding to feedback from the community and fixing a bug that caused meteor to crash on Mac OSX when no computer name is set, and a work around for a bug that caused MongoDB to fail an assertion when using tailable cursors on non-oplog collections.</p>
<p>In a separate update, rc-0 for Meteor's new UI engine “blaze” -- set to completely eliminate Spark in version 0.8 -- has been announced.</p>
<p>On the <a href="https://groups.google.com/forum/#!forum/meteor-talk">meteor talk</a> Google group, user Gadi Cohen <a href="https://groups.google.com/d/msg/meteor-talk/fFPWxgNVFE4/xrokbh9YCw4J">comments</a> on the release “Yes, yes, yes!!! This release, alongside the improvements in 0.7.1, are massive indications of how Meteor has matured, and is both extremely comforting and exciting for startups who took the risk to get on the Meteor train early.&quot;</p>
<p>Meteor’s 0.7.1 release announcement -- and the announcement of Meteor developer accounts -- was met with largely positive reactions from its followers and the wider JavaScript community on Twitter.</p>
<p>Asked his thoughts on the recent updates, Ry Walker, the co-host of <a href="http://www.meteorpodcast.com/">The Meteor Podcast</a> <a href="https://twitter.com/rywalker/status/445665417575415808">said</a>, “0.7.x updates are great, but I'm highly anticipating upcoming 0.8 and 1.0 — it's time more people see @meteorjs.&quot;</p>
<p>With the Meteor community expecting to see the 1.0 release in April or May, Meteor continues to rise in popularity. It was the third most starred GitHub repository in 2012 among open source projects, and its release was the largest in <a href="http://www.infoq.com/news/2014/03/">Hacker News history</a>.</p><br><br><br><br><br><br></body></html>
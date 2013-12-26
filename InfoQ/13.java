<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Android 4.4 KitKat and the Secret Key Factory</h3><p>With the introduction of Android 4.4, developers are being asked to change the way symmetric keys are generated from passphrases via the SecretKeyFactory. This change affects programs that use the PBKDF2WithHmacSHA1 key generation algorithm if their users are allowed to use Unicode passphrases.</p>
<p>Previously the PBKDF2WithHmacSHA1 algorithm only looked at the lower eight bits of each character in the passphrase. This is in conflict with the September 2000 recommendation by RSA Laboratories known as <a href="http://tools.ietf.org/html/rfc2898">PKCS #5: Password-Based Cryptography Specification Version 2.0</a>.</p>
<p>Since this is a breaking change, developers can maintain backwards compatibility by using the old algorithm. This legacy version has been renamed PBKDF2WithHmacSHA1And8bit and can be accessed using this sample code from the <a href="http://android-developers.blogspot.com/2013/12/changes-to-secretkeyfactory-api-in.html">Android Developers Blog</a>.</p>
<pre><p>SecretKeyFactory factory;<br />if (Build.VERSION.SDK_INT &gt;= Build.VERSION_CODES.KITKAT) {<br />    // Use compatibility key factory -- only uses lower 8-bits of passphrase chars<br />    factory = SecretKeyFactory.getInstance(&quot;PBKDF2WithHmacSHA1And8bit&quot;);<br />} else {<br />    // Traditional key factory. Will use lower 8-bits of passphrase chars on<br />    // older Android versions (API level 18 and lower) and all available bits<br />    // on KitKat and newer (API level 19 and higher).<br />    factory = SecretKeyFactory.getInstance(&quot;PBKDF2WithHmacSHA1&quot;);<br />}</p></pre><br><br><br><br><br><br></body></html>
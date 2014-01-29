<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Encrypting Files on Android with Facebook Conceal</h3><p>Facebook has open sourced <a href="http://facebook.github.io/conceal/">Conceal</a>, a set of Java APIs for file encryption and authentication on Android. Conceal uses a subset of <a href="http://www.openssl.org/">OpenSSL</a>’s algorithms and predefined options in order to keep the library smaller, currently being 85KB.</p>
<p>The library targets older Android devices, from Froyo to Jelly Bean, on which the performance is much better than Android’s native support, according to Facebook:</p>
<p><a href="/resource/news/2014/01/encrypt-android-conceal/en/resources/conceal-speed.png" facebook.github.io="" conceal="" a="" set="" of="" java="" apis="" for="" file="" encryption="" and="" authentication="" on="" android.="" uses="" subset="" algorithms="" predefined="" options="" in="" order="" to="" keep="" the="" library="" currently="" being="" targets="" older="" android="" from="" froyo="" jelly="" which="" performance="" is="" much="" better="" than="" native="" according="" title="image" style="border-left-width: 0px; border-right-width: 0px; background-image: none; border-bottom-width: 0px; padding-top: 0px; padding-left: 0px; display: inline; padding-right: 0px; border-top-width: 0px" border="0" alt="image" src="$image_thumb[2].png" width="745" height="253" above="" benchmarks="" compare="" algorithm="" with="" bouncycastle="" galaxy="" y.="" has="" introduced="" support="" openssl="" but="" default="" cipher="" stream="" not="" perform="" replaced="" our="" implementation="" competitive="" against="" following="" code="" snippet="" shows="" how="" encrypt="" files="" creates="" new="" crypto="" object="" implementations="" key="" chain="" as="" well="" library.="" check="" whether="" functionality="" available="" this="" might="" fail="" if="" does="" load="" libraries="" correctly.="" outputstream="" filestream="new" an="" output="" encrypts="" data="" it="" written="" writes="" out="" file.="" write="" plaintext="" it.="" can="" be="" used="" large="" facebook="" using="" images="" phone="" sd="" building="" similar="" based="" found="" github="" target="_blank"><img title="image" style="border-left-width: 0px; border-right-width: 0px; background-image: none; border-bottom-width: 0px; padding-top: 0px; padding-left: 0px; display: inline; padding-right: 0px; border-top-width: 0px" border="0" alt="image" src="http://www.infoq.com/resource/news/2014/01/encrypt-android-conceal/en/resources/conceal-speed.png" _href="img://conceal-speed.png" _p="true" /></a></p>
<p>The above benchmarks compare a native Android algorithm (ES-CTR-HMAC-SHA1) with Bouncycastle (AES-GCM) and Conceal (AES-GCM) on Galaxy Y.</p>
<p>Google has introduced support for OpenSSL in KitKat, but the default Cipher Stream “does not perform well”, <a href="http://facebook.github.io/conceal/faq/">according to Facebook</a>; “when replaced with our Cipher stream (see <a href="https://github.com/facebook/conceal/blob/master/java/com/facebook/crypto/streams/BetterCipherInputStream.java">BetterCipherInputStream</a>), the default implementation is competitive against Conceal.”</p>
<p>The following code snippet shows how to encrypt files with Conceal:</p>
<pre>
// Creates a new Crypto object with default implementations of 
// a key chain as well as native library.
Crypto crypto = new Crypto(
  new SharedPrefsBackedKeyChain(context),
  new SystemNativeCryptoLibrary());

// Check for whether the crypto functionality is available
// This might fail if Android does not load libraries correctly.
if (!crypto.isAvailable()) {
  return;
}

OutputStream fileStream = new BufferedOutputStream(
  new FileOutputStream(file));

// Creates an output stream which encrypts the data as
// it is written to it and writes it out to the file.
OutputStream outputStream = crypto.getCipherOutputStream(
  fileStream,
  entity);

// Write plaintext to it.
outputStream.write(plainText);
outputStream.close();</pre>
<p>Conceal can be used to encrypt large files, Facebook using it to encrypt data and images on phone/tablet’s SD card.</p>
<p><a href="https://github.com/facebook/conceal/tree/master/native/third-party/patches/">Instructions</a> for building a similar library based on OpenSSL can be found on <a href="https://github.com/facebook/conceal">Conceal’s GitHub page</a>.</p><br><br><br><br><br><br></body></html>
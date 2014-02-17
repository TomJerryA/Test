<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Android上のファイルを暗号化するFacebook Conceal</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/encrypt-android-conceal"><em>原文(投稿日：2014/01/29)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Facebookは，Android用のファイル暗号化および認証Java APIのセットである<a href="http://facebook.github.io/conceal/">Conceal</a>をオープンソースとして公開した。ライブラリを小さく保つためにConcealでは，<a href="http://www.openssl.org/">OpenSSL</a>のアルゴリズムと定義済みオプションのサブセットを使用する。現時点でのサイズは85KBだ。</p> 
  <p>ライブラリがターゲットするのは，FroyoからJelly Beanまでの古いAndroidデバイスである。これらの上ではAndroidのネイティブサポートよりはるかにパフォーマンスがよい，とFacebookは述べている。</p> 
  <p><a href="/resource/news/2014/02/encrypt-android-conceal/ja/resources/conceal-speed.png" target="_blank"><img src="http://www.infoq.com/resource/news/2014/02/encrypt-android-conceal/ja/resources/conceal-speed.png" alt="" _href="img://conceal-speed.png" _p="true" /></a></p> 
  <p>上記のベンチマークはGalaxy Y上で，ネイティブのAndroidのアルゴリズム(ES-CTR-HMAC-SHA1)とBouncycastle(AES-GCM)，Conceal(AES-GCM)とを比較したものだ。</p> 
  <p>GoogleはKitKatでOpenSSLのサポートを導入しているが，<a href="http://facebook.github.io/conceal/faq/">Facebookによると</a>}，デフォルトの暗号ストリームの “パフォーマンスはあまりよくない” という。“私たちの暗号ストリーム (<a href="https://github.com/facebook/conceal/blob/master/java/com/facebook/crypto/streams/BetterCipherInputStream.java">BetterCipherInputStream</a>参照)に置き換えれば，Concealと比較できるレベルになります。”</p> 
  <p>以下のコードは，Concealを使ってファイルを暗号化する方法を示したものだ。</p> 
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
  <p>Concealは大規模な暗号化ファイルに使用することができる。Facebookではこれを，スマートフォン/タブレットのSDカード内のデータやイメージの暗号化に利用している。</p> 
  <p><a href="https://github.com/facebook/conceal">ConcealのGitHubのページ</a>には，OpenSSLをベースとした小型ライブラリ作成の<a href="https://github.com/facebook/conceal/tree/master/native/third-party/patches/">手順</a>が公開されている。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
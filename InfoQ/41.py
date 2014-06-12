<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>AppleがSwiftをリリース - iOSとOSXのための高性能かつ高レベルなプログラム言語</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/06/apple-swift"><em>原文(投稿日：2014/06/03)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>本日の<a href="https://developer.apple.com/wwdc/">WWDC 2014</a>でAppleが新プログラム言語<a href="https://developer.apple.com/swift/">Swift</a>の提供を発表した。今年後半，iOS 8およびOSX Yosemiteと合わせてリリースされる。SwiftはJavaScript開発者には馴染みやすい，高レベルなプログラム言語だが，<a href="http://llvm.org">LLVM</a>を使用してコンパイルされることで，OSX およびiOS両プラットフォーム用のハイパフォーマンスな実行コードを生成する。</p> 
  <p>AppleはLLVMに多大な投資をしている。LLVMは特定のアーキテクチャ用に変換可能な抽象インストラクションセットを提供するテクノロジである。CおよびObjective-Cプログラム用に選択されたコンパイラは，GCCからClangに置き換えられている。どちらの言語も，ClangによってLLVMインストラクションに変換された上で，各プラットフォーム用の実行コードに最適化される。新しいプログラム言語のSwiftも，同じようにLLVMバイトコードを生成する。既存のObjective-Cアプリケーションやライブラリとの共存も可能だ。</p> 
  <p>Swiftにはさらに，コードテスト用のREPL環境も付属している。JavaScriptやPythonなどのインタプリタ言語で使用されるのが一般的なREPLは，個々の式や文の評価に使用可能なRead-Evaluate-Print-Loopをコマンドライン上で提供し，デバッグを用意にする。強力なループ，文字列解釈，プリント/デバッグオプションなどを組み合わせることによって，CやJavaのようなプログラム言語には欠けることの多い，対話型の開発スタイルを提供する。</p> 
  <p>Swiftは強い型付けを持った言語だが，型推論を使用して開発者の文字入力を大幅に削減している。明示的な型の指定も可能で，数値型にはUint8やInt32のようなサイズ指定を用いることができる。型エンジンはOptional変数型も提供する。Optionalな値は，その値が存在すると期待されているかどうかによって，?あるいは!を使って参照を外す(dereferenced)ことができる。コレクションでは，配列([]で指定する)とディクショナリ/マップ([:]で指定する)のリテラルがサポートされている。ジェネリック型を含むことも可能だ。</p> 
  <p>関数は言語の第１要素である。変数その他の要素として関数を渡すこともできる。引数は明示的に名前を付ける(Object-Cの名前付き引数と互換性を持つ)ことも，位置引数のみとして指定することも可能だ。パラメータには既定値も指定可能なので，不要な引数は省略することができる。</p> 
  <p>SwiftのインテグレーションではObjective-Cを使用できる。標準ライブラリ(UKitやCocoaなど)の他，ユーザ定義タイプも対象である。クラスもSwiftでネイティブに生成可能(Objective-Cからも使用できる)で，他のObjective-Cのオブジェクトと同じく，参照カウントが実行される。(リファレンスはランタイムによって実行時に自動管理されるので，Swiftではユーザが直接的にメモリ管理を考慮する必要はない。)参照型であるクラスと同じように，値型である構造体も，自身のコピーを値として関数タイプに渡すことができる。</p> 
  <p>そして最後に，Swiftではタプルを使用して複数の値を返すことができる。タプルは(case文を使った)マッチングのシナリオや，変数の代入にも使用可能だ。</p> 
  <p>SwiftはXcode 6 developer previewを通じて使用することができる。今後数ヶ月で一般向けにリリースされる予定だ。現時点では，Swift言語がLLVM側にマージされるという確証はない。しかしARM 64ビットサポートが先日マージされ，SafariのJavaScriptで使用されている高速JITでもその作業が行われていることから，LLVMのホストするClangランタイムに部分的には組み込まれていく可能性はある。これが実現すれば，Clangコンパイラのある他のアーキテクチャでも，Swiftを使ってプログラムを記述できるようになるだろう。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Chefのレシピ作成エクスペリエンスを向上するChef Sugar</h3><p><a target="_blank" href="http://www.infoq.com/news/2014/01/chef-sugar"><em>原文(投稿日：2014/01/13)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p><a href="https://github.com/sethvargo/chef-sugar">Chef Sugar</a>はDSLを使ってレシピの可読性を改善する<a href="http://www.getchef.com/">Chef</a>のエクステンションだ。作者の<a href="https://sethvargo.com/">Seth Vargo</a>氏が実例を示しながら，<a href="https://sethvargo.com/spice-up-your-recipes-with-chef-sugar/">Chef Sugarを開発した動機について説明している</a>。InfoQは氏へのインタビューを通じて，Chefのプラグインアーキテクチャという面から，シンタックスシュガーのメリットに対する氏の見解を聞いた。</p> 
  <p>Chef Sugarはクラウド (<code>cloud?</code>, <code>ec2?</code>など)やプラットフォーム(<code>ubuntu?</code>, <code>centos?</code>など)，<a href="http://code.sethvargo.com/chef-sugar/">いくつかの領域</a>でDSLメソッドを提供する。ヘルパメソッドの導入に関しては<a href="https://github.com/sethvargo/chef-sugar/issues">今も議論が続いている</a>が，氏は自身の記事で，Chef Sugarを使用した場合と使用しない場合の対比を示している。その例によれば，次のレシピを，</p> 
  <pre>
include_recipe 'cookbook::_windows_setup' if platform_family?('windows')  
include_recipe 'cookbook::_ec2_setup' if node['ec2'] || node['eucalyptus']

package 'foo' do  
  action :nothing
end.run_action(:install)

execute 'untar package' do  
  if node['kernel']['machine'] == 'x86_64'
    command 'ARCH_FLAGS=x64 make'
  else
    command 'ARCH_FLAGS=i386 make'
  end
  not_if do
    ::File.exists?('/bin/tool') &amp;&amp;
    ::File.executable?('/bin/tool') &amp;&amp;
    shell_out!('/bin/tool --version').stdout.strip == node['tool']['version']
  end
end

credentials = Chef::EncryptedDataBagItem.load('accounts', 'passwords') 
</pre> 
  <p>このレシピに書き換えることができる。</p> 
  <pre>
include_recipe 'cookbook::_windows_setup' if windows?  
include_recipe 'cookbook::_ec2_setup' if ec2? || eucalyptus?

compile_time do  
  package 'apache2'
end

execute 'untar package' do  
  if _64_bit?
    command 'ARCH_FLAGS=x64 make'
  else
    command 'ARCH_FLAGS=i386 make'
  end
  not_if { installed_at_version?('/bin/tool', node['tool']['version']) }
end

credentials = encrypted_data_bag_item('accounts', 'passwords')	
</pre> 
  <p>Chef Sugarは元々，レシピ内での使用を意図して書かれたものだが，<a href="http://docs.opscode.com/essentials_cookbook_libraries.html">Chefライブラリ</a>としても使用できる。Chefライブラリは，任意のRubyコードをクックブックにインクルード可能なコンセプトである。ライブラリで使用する場合の主な違いは，Chef Sugarのメソッドがパラメータとして<a href="http://docs.opscode.com/essentials_node_object.html">ノードオブジェクト</a>を取ることだ。</p> 
  <pre>
# cookbook/libraries/default.rb
def only_on_windows(&amp;block)  
  yield if Chef::Sugar::PlatformFamily.windows?(@node)
end 
</pre> 
  <p>InfoQ: シンタックスシュガーは不必要で重要性の低いものだという見方がありますが，Chef Sugarというプロジェクトを作成したあなたは当然，必ずしもそうではない，と思っているはずです。シンタックスシュガーが必要，あるいは不要なのは，どのような場合だとお考えですか？</p> 
  <blockquote> 
   <p>私はシンタックスシュガーが，Ruby(とRails)が開発者にこれ程までに受け入れられた大きな理由のひとつだと思っています。例えばActiveSupportは，RubyのIntegerクラスに対して，<code>5.days.ago</code>のようなメソッドコールを可能にするシンタックスシュガーを加えています。複雑さと反復性を軽減する上で，シュガーは非常に有効だと思いますね。あるソフトウェアが特定のバージョンでインストールされているかどうかをチェックする，というように，多くのクックブックに共通するイディオムやパターンがあります。このようなパターンの存在を見つけたとき，シュガーとして実装するべきだ，と思いました。</p> 
   <p>逆に私は，&quot;シュガー化&quot;する対象を積極的に探すようなことはしませんでした(今もしていません)。これはよく間違われる点です。私の意見としては，2つより多い論理的ブランチやコンポーネントのあるシュガーはやり過ぎだと思います。例えば，多数のロジックやリソースをラップするシュガーを書くこともできるかも知れませんが，それならばライブラリやLWRPを使った方がよいでしょう。シュガーはテストもメンテナンスも簡単でなければなりません。経験の浅い開発者でも，シンタックスシュガーを定義したメソッドを分析できることが必要なのです。</p> 
  </blockquote> 
  <p>InfoQ: 一般的にこのような機能は，アプリケーションのコアで利用できるべきであると思われますか，それとも&quot;アドオン&quot;形式が望ましいのでしょうか？ その理由も教えてください。</p> 
  <blockquote> 
   <p>私はプラグインアーキテクチャパターンを固く信じています。Chef Sugarの機能をChefそのものに追加するのは簡単ですが，意識的に分離することにしました。開発者がActiveSupportの使用を強制されたくないのと同じで，Chef開発者にChef Sugarを強制したくはないのです。</p> 
   <p>メンテナンス性の面で言えば，Chef Sugarをgemとして分離することによって，Chefのリリースサイクルから独立したイテレーションでの開発が可能になります。Ruby自体がこのようなプラグインパターンを使って，コアクラスを個別のメンテナのgemに移行していますし，Rubinius 2.0 などは完全にgemで構成されています。ひとつのモノシリックなアプリを止めて分散システムにすることのアドバンテージがありますが，それと同じです。コンポーネントをコアフレームワークにバンドルするのではなく，プラグインベースの&quot;アドイン&quot;を使うことで同じようなメリットがあるのです。Vagrant Knife(Chef用のコマンドインターフェース)やRubygemsのように，ツールにもこのパターンのものがありますね。</p> 
   <p>ですが実はもうひとつ，プラグインをコアの特定バージョンに(従属部品として)ロックしてバンドルしながら，独立したリソースとしてフレームワーク外部におくという，都合のいい方法があるのです。ユーザはプラグインを好きな時に最新バージョンにアップデートすることも，ソフトウェアパッケージ全体のアップグレードまで待つこともできます。Ruby 2.0が採用しているのはこのパターンです。試しにbigdesimalをアンインストールしてみてください。こんなエラーが出るはずです。</p> 
   <pre>
ERROR:  While executing gem ... (Gem::InstallError)
    gem &quot;bigdecimal&quot; cannot be uninstalled because it is a default gem
</pre> 
   <p>それでも新しいバージョンのbigdecimalには，いつでもアップグレードできます。</p> 
   <p>最後に考慮しなくてならないのが(見落とされがちですが)，ライセンシングに関する問題です。Chef Sugarのケースでは，ChefとChef SugarがどちらもApache 2.0でライセンスされているので問題ありませんが，プラグインの再販や特許取得が許可されていないために，コアアプリケーションにバンドルできない場合もあります。</p> 
  </blockquote> 
  <p>InfoQ: Chef Sugarを使ったメソッド追加でメリットのありそうな領域は，他にもありますか？</p> 
  <blockquote> 
   <p>先程話したように，私は積極的に&quot;シュガー化&quot;する分野を探すことはしていません。最初にChef Sugarをリリースした時は，素晴らしい評判がありました。20分と経たないうちに，コミュニティのメンバがFreeBSDサポートを追加してくれたのです。その後２ヶ月間は，何のメンテナンスもなく経過しました (問題なく&quot;動いた&quot;ので)。1ヶ月ほど前には，誰かがCloudstackのサポートを追加してくれています。</p> 
   <p>私自身はプル要求に注意して，可能な限り早く反映していると自負していますから，そういったものはいつでも送ってきてほしいですね。ただし私は，プロジェクトの目標を逸脱したパッチには遠慮なくノーを言うつもりです。 &quot;シュガー化&quot;できそうな領域を知っているコミュニティのメンバがいたら，ぜひ教えてください！</p> 
  </blockquote> 
  <p>InfoQ: コミュニティからの貢献を活用できそうなChefの分野の中で，もっとも重要なものは何でしょう？</p> 
  <blockquote> 
   <p>Chefに関する問題はすべて，<a href="https://tickets.opscode.com">Chef Softwareのチケットシステム</a>で追跡されています。ほとんどの問題はトリアージされて，優先順位が付けられています。コミュニティに新たに参加したのなならば，&quot;trivial&quot;あるいは&quot;minor&quot;でタグ付けされた問題が，Chefのコアに触れるためのよい手がかりになるでしょう。そして何よりも，誤字や文法修正といった成果を過小評価しないことです。Chefの人気が高くなれば，英語以外のバックグラウンドを持ったユーザ用のドキュメントも必要になってくると思います。</p> 
   <p>最後に紹介したいのですが，GitHubプロジェクトに<a href="https://github.com/opscode/chef-rfc">Chef RFCs</a>というエントリがあって，高レベルの機能に関するコミュニティからの提案や，Chefロードマップの変更が紹介されています。このリポジトリに対するプル要求は，コミュニティとして大きく貢献することになります (たとえ単純なものでも :+1:)。</p> 
   <p>Chefのコアプロジェクトとは別ですが，昨年11月のChefコミュニティサミットで，<a href="https://tickets.opscode.com/browse/COOK">COOKプロジェクト</a> (Chefが管理するコミュニティのクックブック) に関する重要な変更がいくつか発表されました。Chefは現在，Chefのコミュニティメンバと，<a href="http://community.opscode.com/cookbooks">コミュニティのクックブック</a>を共同管理するプロセスにあります。</p> 
  </blockquote> 
  <p>&nbsp;</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
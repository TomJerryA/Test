<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Amazon Kinesisでビッグデータをストリーム処理</h3><p><a target="_blank" href="http://www.infoq.com/news/2013/11/aws-kinesis"><em>原文(投稿日：2013/11/25)へのリンク</em></a></p>
<div class="article_page_left news_container text_content_container"> 
 <div class="text_info"> 
  <p>Amazonがさまざまなソースにある大規模データをストリーム処理できるサービス、Kinesisを<a href="http://aws.typepad.com/aws/2013/11/amazon-kinesis-real-time-processing-of-streamed-data.html">発表した</a>。現在、限定プレビューとして利用できる。</p> 
  <p>Kinesisとは何か？ <a href="http://aws.amazon.com/sqs/">SQS</a>とどう違うのか？ <a href="http://www.reddit.com/r/programming/comments/1qzohv/amazon_aws_now_does_massive_streaming_data_kinesis/cdilarh">BuckKniferson</a>氏はこう<a href="http://www.reddit.com/r/programming/comments/1qzohv/amazon_aws_now_does_massive_streaming_data_kinesis/cdisi0a">説明する</a>。</p> 
  <blockquote> 
   <p>KinesisはSQSキューとオートスケーリングのコンピュートインスタンスを新しいプロダクトにまとめたように見えます。Kinesisを使うことで、1秒間に何百万ものPOSTリクエストを受け付け、それらをストリームとしてリアルタイムに処理できます。ストリーム化されたデータを直接S3に送ったり、それを処理するためのアプリケーションやリレーショナルストレージなどへ送ることができます。すべてリアルタイムで。</p> 
  </blockquote> 
  <blockquote> 
   <p>SQSメッセージは256kbのテキストメッセージに限られます（一般的にはJSONですが、好きなものが使えます）。Kinesisストリームは1秒間にメガバイト単位で用意でき、私が知るかぎり、HTTP PUT経由のどんなデータも受け付けます。</p> 
   <p>さらに、SQSメッセージはゾーン依存で永続的ではありませんが、Kinesisストリームデータは複数のアベイラビリティゾーンで24時間、アプリから利用できます。SQSメッセージの場合、ゾーンが機能しなくなったり何らかの異常があると、それはなくなってしまいます。SQSにはKinesisのようなスケーラビリティとIOが備わっていないと思います。私はSQSの公開されているIOPS保証をこれまで目にしたことはありませんが、Kinesisはシャードあたり1秒間に1000のPUTリクエストを受け付けることができます。</p> 
  </blockquote> 
  <p>Kinesisストリームを使って、アプリケーションはデータをキャプチャ、格納、伝送することができる。各ストリームは複数のリーダーとライターを持つことができる。ストリームの容量はシャードという単位で規定される。各シャードは1000書き込みトランザクション、1秒あたり1MBまで書き込める。ユーザはシャードを増減させることで、ダウンタイムなしにストリームの容量を変えることができる。</p> 
  <p>開発者はKinesisクライアントライブラリを使って、Kinesisを利用したアプリケーションを作ることができる。生産者側は<a href="http://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html">PutRecord API</a>を使ってデータをプッシュする。消費者側は<a href="http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-record-processor-app.html">IRecordProcessor</a>に対する実装を用意し、クライアントは新しいレコードが生成されるとそれを「プッシュ」する。<a href="http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html">GetShardIterator</a>や<a href="http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetNextRecords.html">GetNextRecords</a>といった低レベルのインターフェイスもある。消費者側のコードでは、処理したレコードをAWSストレージサービス（S3、RedShift、DynamoDB）の1つに格納したり、別のKinesisストリームに渡すことができる。</p> 
  <p>Kinesisでできるリアルタイム処理は、（Hadoopでできるような）<a href="http://www.datasciencecentral.com/profiles/blogs/batch-vs-real-time-data-processing">バッチ処理とは異なっている</a>。Kinesisの場合、データが到着するとそれは即座に処理される。AmazonはKinesisで実現可能なユースケースとして、ログの処理、ソーシャルメディアデータの処理、ファイナンシャルトランザクションのリアルタイム処理、オンライン機械学習を挙げている。こうした大規模なリアルタイムの複雑な処理を可能にするプロダクトとしては、ほかに<a href="http://storm-project.net/">Storm</a>がある。</p> 
 </div> 
</div><br><br><br><br><br><br></body></html>
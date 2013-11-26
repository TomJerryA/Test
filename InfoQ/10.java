<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>Streaming Big Data With Amazon Kinesis</h3><p>Amazon <a href="http://aws.typepad.com/aws/2013/11/amazon-kinesis-real-time-processing-of-streamed-data.html">recently announced</a> Kinesis, a service that allows developers to stream large amounts of data from different sources and process it. The service is currently in limited preview.</p>
<p>What exactly is Kinesis? And how is it different from <a href="http://aws.amazon.com/sqs/">SQS</a>? <a href="http://www.reddit.com/r/programming/comments/1qzohv/amazon_aws_now_does_massive_streaming_data_kinesis/cdilarh">BuckKniferson</a>&nbsp;<a href="http://www.reddit.com/r/programming/comments/1qzohv/amazon_aws_now_does_massive_streaming_data_kinesis/cdisi0a">explains</a> -</p>
<blockquote> 
 <p>Kinesis seems to wrap up SQS queues and auto-scaling compute instances into a new product. Kinesis gives you the ability to accept millions of POST requests per second and process them all in real time as a stream. You can send the streamed data directly to S3, and send it to your apps for processing, and to relational storage and and and... All in real time.</p> 
</blockquote>
<blockquote> 
 <p>SQS messages are limited to 256kb of text messages (generally JSON, but use whatever you like). Kinesis streams are provisioned in megabytes per second, and as far as I can tell, can accept any kind of data through HTTP PUT.</p> 
 <p>Additionally, Kinesis stream data is available to your apps for 24 hours across multiple availability zones while SQS messages are zone dependent and are not durable. If a zone goes out, or there is some glitch, your SQS messages are gone. And I don't think SQS has the scalability and IO that Kinesis has. I've never seen a published IOPS guarantee for SQS but Kinesis can accept 1000 PUT requests per second, per shard.</p> 
</blockquote>
<p>Applications use Kinesis streams to capture, store and transport data, each of which can have multiple readers and writers. The capacity of a stream is specified&nbsp;in terms of shards; each shard has the ability to write 1000 write transactions, upto 1 MB per second. Users can scale capacity of individual streams by adding or removing shards without downtime.</p>
<p>Developers can use the Kinesis client library to build applications that leverage Kinesis. The producer side uses <a href="http://docs.aws.amazon.com/kinesis/latest/APIReference/API_PutRecord.html">PutRecord API</a> to push data.&nbsp;On the consumer side, you provide an implementation to <a href="http://docs.aws.amazon.com/kinesis/latest/dev/kinesis-record-processor-app.html">IRecordProcessor</a> and the client will “push” new records as they get created. There are also lower level interfaces such as <a href="http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html">GetShardIterator</a> and <a href="http://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetNextRecords.html">GetNextRecords</a>. After processing a record, the consumer code can store it in one of the AWS storage services (S3, RedShift, DynamoDB) or can pass it along to another Kinesis stream.</p>
<p>Real-time processing as enabled by Kinesis <a href="http://www.datasciencecentral.com/profiles/blogs/batch-vs-real-time-data-processing">is different from batch-processing</a> (such as enabled by Hadoop) as data can be processed as soon as it is available, rather than in batches. Amazon lists log processing, processing of social media data, real-time processing of financial transactions and online machine learning as some of the possible use cases for this. Another product which enables large amounts of real-time complex processing is <a href="http://storm-project.net/">Storm</a>.&nbsp;</p><br><br><br><br><br><br></body></html>
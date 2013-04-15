<html><head><meta http-equiv="content-type" content="text/html; charset=utf-8" /></head><body><h3>JSON Validation Roundup</h3><p>Create any “flexible” or “extensible” file format and sooner or later a group of developers will start complaining about validation. There are many this can be handles, but in general they can be categorized as:</p> 
<ul> 
 <li>Assume the data is correctly formatted.</li> 
 <li>Manually check for mal-formed data and attempt to correct.</li> 
 <li>Manually check for mal-formed data and reject where appropriate.</li> 
 <li>Automatically check for mal-formed data.</li> 
</ul> 
<p>The purpose of this article isn’t to debate these options, but rather to summarize the toolkits available for automatic validation.</p> 
<p><b>JSON Schema</b></p> 
<p><a href="http://json-schema.org/implementations.html">JSON Schema</a> is a proposed standard supported by 17 different projects. It is available for JavaScript, Java, Python, Ruby, Perl, PHP, .NET, ActionScript, C, Haskell, and Erlang. The format is more complicated than VeriJSON with the schema bearing little resemblance to the actual data. It is also more comprehensive, with the ability to range-check numbers, limit lists, and prevent duplicate entries in lists. It also supports <a href="http://json-schema.org/example2.html">references to other schemas</a>, allowing you to break down large schemas into smaller components.</p> 
<p><b>Atdgen </b></p> 
<p>Atdgen offers JSON serialization and deserialization support to OCaml. JSON schemas are created using what are known as atd files. These files are run through a code generator to create OCaml class files and matching object/JSON converters. In Atdgen, validation occurs during the deserialization process.</p> 
<p>Validation rules in atd files are open-ended, developers can inject whatever OCaml code they want directly into the atd file. References to secondary schema files are supported.</p> 
<p><a href="http://mjambon.com/atdgen">Atdgen</a> is available under an open source license.</p> 
<p><b>DataContractJsonSerializer</b></p> 
<p>Based on WCF’s DataContractSerializer, the <a href="http://msdn.microsoft.com/en-us/library/system.runtime.serialization.json.datacontractjsonserializer.aspx">DataContractJsonSerializer</a> uses class definitions and data contract attributes to determine how a JSON file is validated and ultimately deserialized. This is suitable for basic tasks, but tends to exhibit performance problems and has difficulty with dictionaries. Validation is pretty much limited to basic structure.</p> 
<p><b>Json.NET </b></p> 
<p>Json.NET by James Newton-King is by far the most comprehensive JSON serializer/deserializer available today. Like the DataContractJsonSerializer, Json.NET can use classes to define its schema. You can either use the standard WCF data contract attributes or <a href="http://james.newtonking.com/projects/json/help/index.html?topic=html/SerializationAttributes.htm">JSON.NET’s serialization attributes</a> and supports a wide variety of types including DataTable and nHibernate entities. And as of this month, <a href="http://james.newtonking.com/archive/2013/04/07/json-net-5-0-release-1-net-4-5-biginteger-read-only-collections.aspx">JSON.NET 5.0</a> supports unlimited size integers (via BigInteger) and read-only collections that expose an IEnumerable constructor.</p> 
<p>JSON.NET also supports validation via JSON Schema.</p> 
<p><b>VeriJSON</b></p> 
<p>VeriJSON is an Objective-C library that relies on pattern-based matching. The patterns themselves are written in JSON. Supported types are “number”, “string”, “bool”, and “url”. Strings can be restricted using a regular expression and urls by schema (e.g. http, ftp). Arrays and objects are represented structurally and optional properties are supported.</p> 
<p><a href="https://bitbucket.org/dcutting/verijson">VeriJSON</a> is available via an open source license.</p> 
<p id="lastElm"></p><br><br><br><br><br><br></body></html>
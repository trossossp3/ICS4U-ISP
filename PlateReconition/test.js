var MongoClient = require('mongodb').MongoClient;
var url = "mongodb://localhost:27017/";

MongoClient.connect(url, (err, db)=> {
	if (err) throw err;
	var dbo = db.db("testDb");
/*
	var myObj = {name:"Tree", car:"supra"};
	dbo.collection("people").insertOne(myObj, (err, res)=> {
		if (err) throw err;
		console.log("1 document inserted");
		
	});
*/
	var myQ = {car:"supra"};
	dbo.collection("people").deleteOne(myQ, (err,obj)=>{
		if(err) throw err;
		console.log("deleted item");
		db.close();
	});

	dbo.collection("people").find({}).toArray((err, result)=> {
		if (err) throw err;
		console.log(result);
		db.close();
  	});
}); 

import pymongo as mongo

client = mongo.MongoClient("mongodb://localhost:27017/")
#a database is not created until it gets content
db = client['testDb']

print(client.list_database_names()) #list all databases

col = db["people"]

#collection arnt created until they have content

print(db.list_collection_names())

#test for specific collection
if "people" in db.list_collection_names():
    print("true")

Mydict = {"name":"temp", "car":"civic"}
# if no _id is specified mongo generartes them
x=col.insert_one(Mydict); #.insert_many() for multiple entrys
print(x.inserted_id)

for x in col.find():
    print(x)

#return only some params
#You get an error if you specify both 0 and 1 values in the same object (except if one of the fields is the _id field):
for x in col.find({},{ "_id": 0, "name": 1, "address": 1 }): #0 means no
  print(x) 


#mycol.delete_one(myquery) 
y=col.delete_many({}) #delets all documents
print(y.deleted_count)
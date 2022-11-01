import pymongo
client = pymongo.MongoClient("mongodb+srv://moreshwar:moreshwar@cluster0.ethq3yc.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={"name":"moreshwar","email":"moreshwarpowar12@gmail.com","surname":"powar"}
d={"name":"moreshwar","email":"moreshwarpowar12@gmail.com","surname":"powar"}
d={"name":"moreshwar","email":"moreshwarpowar12@gmail.com","surname":"powar"}
d={"name":"moreshwar","email":"moreshwarpowar12@gmail.com","surname":"powar"}

db1=client['mongotest']
coll=db1['test1']
coll.insert_one(d)
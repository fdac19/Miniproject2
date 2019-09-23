import pymongo, json
client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac19mp2']
coll = db ['dlee97']

with open('sources.json', 'r') as f:
	di = json.load(f)
	print(di)

import pprint
import re
import pymongo, json

pp = pprint.PrettyPrinter(indent=1, width=65)

# Connect to database
client = pymongo.MongoClient(host='da1.eecs.utk.edu')
db = client['fdac19mp2']

# Connect/Create personal netid collection from database
collection = db['mnb512']

# Still missing collections 

aliu11
apatel79
cscott57
madams56
rbrink1
skitche1
smunira
twinter4

## < 20 entries in the collection
atipton7;18
atutko;19
cbrunet1;1
cwilder8;13
mshoffn2;4


# Data Discovery Project


1. Pick a favorite topic that you care about
2. Find at least 20 datasets for that topic (use, for example,
https://toolbox.google.com/datasetsearch). I for one, collect open
source git repositories, so I searched for "git urls"
3. For each of the 20 datasets you chose determine if the underlying data can be accessed (some of these datasets do not provide public access)
4. Create a mongodb collection YourNetId within the database fdac19mp2
   where you store metadata for each of the 20 datasets: YourTopic, title,
   license, description, url(s) were the data may be retrieved
   
```
import pymongo, json
client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac19mp2']
coll = db ['YourNetId']
# for each dataset
coll.insert_one ( { 'topic':'YourTopic', 'title': 'Data title', 'license': 'license', 'description': 'Brief data description', 'urls': [ 'url1', 'url2', ... ] } )
```


To check what is recorded:
```
import pprint
import pymongo, json
client = pymongo.MongoClient (host="da1.eecs.utk.edu")
db = client ['fdac19mp2']
coll = db ['YourNetId']
pp = pprint.PrettyPrinter(indent=1,width=65)
for r in coll. find():
  print(pp .pformat (r))  
```

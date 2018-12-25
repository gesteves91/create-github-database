import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find({}, {"commit": 1})

for commits in cursor:
  print(commits['commit']['committer']['date'])
    
    
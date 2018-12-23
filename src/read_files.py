import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find({}, {"files": 1})

filenames = []
status = []

x = 1

for commits in cursor:
  for key in commits:
    if key == 'files':
      for files in commits[key]:
          for llave in files:
            if llave == 'status':
              print(files[llave])
            if llave == 'filename':
              print(files[llave])
  #  print(list)
    #for item in list:




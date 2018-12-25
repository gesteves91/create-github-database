import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["repo_labels"]

#cursor = mycol.find({"url": "https://api.github.com/repos/mavam/stat-cookbook"})
cursor = mycol.find({}, {"name": 1, "repo": 1, "owner": 1})

name = "ProjectTemplate"

for repos in cursor:
  if repos["repo"] == name:
    print(repos["name"])
    print(repos["owner"])
    break
    '''for key in repos:
    if key == "url" and repos[key] == modified_url:
      for key in repos:
        if key == 'name':
          print repos[key]
        if key == 'full_name':
          print repos[key]
        if key == 'private':
          print repos[key]
        if key == 'fork':
          print repos[key]
        if key == 'size':
          print repos[key]
        if key == 'watchers_count':
          print repos[key]
        if key == 'language':
          print repos[key]
        if key == 'has_issues':
          print repos[key]
        if key == 'has_downloads':
          print repos[key]
        if key == 'has_wiki':
          print repos[key]
        if key == 'forks_count':
          print repos[key]
        if key == 'open_issues_count':
          print repos[key]
        if key == 'forks':
          print repos[key]
        if key == 'open_issues':
          print repos[key]
        if key == 'watchers':
          print repos[key]
        if key == 'network_count':
          print repos[key]
        if key == 'owner':
          owner = repos[key]
          for data in owner:
            if data == 'type':
              print owner[data]
        if key == 'permissions':
          permission = repos[key]
          for data in permission:
            if data == 'admin':
              print permission[data]
            if data == 'push':
              print permission[data]
            if data == 'pull':
              print permission[data]'''    

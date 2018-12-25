import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["repos"]

#cursor = mycol.find({"url": "https://api.github.com/repos/mavam/stat-cookbook"})
cursor = mycol.find({}, {"name": 1, "full_name": 1, "private": 1,
                         "url": 1, "fork": 1, "size": 1, "watchers_count": 1,
                         "language": 1, "has_issues": 1, "has_downloads": 1,
                         "has_wiki": 1, "forks_count": 1, "open_issues_count": 1,
                         "forks": 1, "open_issues": 1, "forks": 1, "open_issues": 1,
                         "watchers": 1, "network_count": 1, "owner": 1,
                         "permissions": 1})

modified_url = "https://api.github.com/repos/mavam/stat-cookbook"

for repos in cursor:
  if repos["url"] == modified_url:
    print(repos["name"])
    print(repos["full_name"])
    print(repos["private"])
    print(repos["fork"])
    print(repos["size"])
    print(repos["watchers_count"])
    print(repos["language"])
    print(repos["has_issues"])
    print(repos["has_downloads"])
    print(repos["has_wiki"])
    print(repos["forks_count"])
    print(repos["open_issues_count"])
    print(repos["forks"])
    print(repos["open_issues"])
    print(repos["watchers"])
    print(repos["network_count"])
    print(repos["owner"]["type"])
    print(repos["permissions"]["push"])
    print(repos["permissions"]["pull"])
    print(repos["permissions"]["admin"])
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




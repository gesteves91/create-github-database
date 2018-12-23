import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commit_comments"]

def getCommitCount(commit):

  for key in commit:
    message = commit['message'].encode('utf-8')
    comment_count = commit['comment_count']

    return [message, comment_count]

def getCommentBySha(sha):

  bodies = []

  data = mycol.find({"commit_id": sha})

  for comments in data:
    for key in comments:
      if key == 'body':
        bodies.append(comments[key])
  
  return bodies

def getFileNamesAndStatus(commit):

  filenames = []
  status = []
  changes = []
  additions = []
  deletions = []
  
  for files in commit:
    for key in files:
      if key == 'status':
        status.append(files[key])              
      if key == 'filename':
        filenames.append(files[key])
      if key == 'additions':
        additions.append(files[key])
      if key == 'deletions':
        deletions.append(files[key])
      if key == 'changes':
        changes.append(files[key])

  return filenames, status, additions, deletions, changes

def extractURL(url):

  head, sep, tail = url.partition('/commits/')

  return head

def getReposInfo(url):

  dictionaryRepos = {}

  cursor = mydb["repos"].find({"url": url})

  for repos in cursor:
    for key in repos:
      if key == 'name':
        dictionaryRepos.update({'name': repos[key]})
      if key == 'full_name':
        dictionaryRepos.update({'full_name': repos[key]})
      if key == 'private':
        dictionaryRepos.update({'private': repos[key]})
      if key == 'fork':
        dictionaryRepos.update({'fork': repos[key]})
      if key == 'size':
        dictionaryRepos.update({'size': repos[key]})
      if key == 'watchers_count':
        dictionaryRepos.update({'watchers_count': repos[key]})
      if key == 'language':
        dictionaryRepos.update({'language': repos[key]})
      if key == 'has_issues':
        dictionaryRepos.update({'has_issues': repos[key]})
      if key == 'has_downloads':
        dictionaryRepos.update({'has_downloads': repos[key]})
      if key == 'has_wiki':
        dictionaryRepos.update({'has_wiki': repos[key]})
      if key == 'forks_count':
        dictionaryRepos.update({'forks_count': repos[key]})
      if key == 'open_issues_count':
        dictionaryRepos.update({'open_issues_count': repos[key]})
      if key == 'forks':
        dictionaryRepos.update({'forks': repos[key]})
      if key == 'open_issues':
        dictionaryRepos.update({'open_issues': repos[key]})
      if key == 'watchers':
        dictionaryRepos.update({'watchers': repos[key]})
      if key == 'network_count':
        dictionaryRepos.update({'network_count': repos[key]})
      if key == 'owner':
        owner = repos[key]
        for data in owner:
          if data == 'type':
            dictionaryRepos.update({'type': repos[key]})
      if key == 'permissions':
        permission = repos[key]
        for data in permission:
          if data == 'admin':
            dictionaryRepos.update({'admin': repos[key]})
          if data == 'push':
            dictionaryRepos.update({'push': repos[key]})
          if data == 'pull':
            dictionaryRepos.update({'pull': repos[key]})
  
  return dictionaryRepos
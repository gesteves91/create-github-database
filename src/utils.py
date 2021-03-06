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

def getReposLabels(name):

  labels = []

  cursor = mydb["repo_labels"].find({"repo": name})

  for repos in cursor:
    if repos["repo"] == name:
      labels.append(repos["name"])
      labels.append(repos["owner"])
      break

  # Empty list.
  if not labels:
    labels.append(None)
    labels.append(None)

  return labels

def getReposInfo(url):

  cursor = mydb["repos"].find({"url": url})

  dictionaryRepos = {}

  for repos in cursor:
    if repos["url"] == url:
      dictionaryRepos.update({"name": repos["name"]})
      dictionaryRepos.update({"full_name": repos["full_name"]})
      dictionaryRepos.update({"private": repos["private"]})
      dictionaryRepos.update({"fork": repos["fork"]})
      dictionaryRepos.update({"size": repos["size"]})
      dictionaryRepos.update({"watchers_count": repos["watchers_count"]})
      dictionaryRepos.update({"language": repos["language"]})
      dictionaryRepos.update({"has_issues": repos["has_issues"]})
      dictionaryRepos.update({"has_downloads": repos["has_downloads"]})
      dictionaryRepos.update({"has_wiki": repos["has_wiki"]})
      dictionaryRepos.update({"forks_count": repos["forks_count"]})
      dictionaryRepos.update({"open_issues_count": repos["open_issues_count"]})
      dictionaryRepos.update({"forks": repos["forks"]})
      dictionaryRepos.update({"open_issues": repos["open_issues"]})
      dictionaryRepos.update({"watchers": repos["watchers"]})
      dictionaryRepos.update({"network_count": repos["network_count"]})
      dictionaryRepos.update({"type": repos["owner"]["type"]})
      dictionaryRepos.update({"push": repos["permissions"]["push"]})
      dictionaryRepos.update({"pull": repos["permissions"]["pull"]})
      dictionaryRepos.update({"admin": repos["permissions"]["admin"]})
      break

  return dictionaryRepos

def getUsersInfo(name):
  
  cursor = mydb["users"].find({"login": name})

  dictionaryAuthors = {}

  for repos in cursor:
    if repos["login"] == name:
      #dictionaryRepos.update({"hireable": repos["hireable"]})
      dictionaryAuthors.update({"followers": repos["followers"]})
      dictionaryAuthors.update({"following": repos["following"]})
      dictionaryAuthors.update({"public_gists": repos["public_gists"]})
      break

  if not dictionaryAuthors:
    dictionaryAuthors.update({"followers": 0})
    dictionaryAuthors.update({"following": 0})
    dictionaryAuthors.update({"public_gists": 0})

  return dictionaryAuthors
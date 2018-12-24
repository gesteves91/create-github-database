import csv
import pymongo
import codecs
from utils import getCommitCount
from utils import getCommentBySha
from utils import getFileNamesAndStatus
from utils import getReposInfo
from utils import extractURL

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["msr14"]
mycol = mydb["commits"]

cursor = mycol.find(
    {}, {'sha': 1, 'url': 1, 'commit.message': 1, 'commit.comment_count': 1, 
         'stats.deletions': 1, 'stats.additions': 1, 'stats.total': 1, 'files': 1})

'''reposi = mydb["repos"].find({}, {"name": 1, "full_name": 1, "private": 1,
                         "url": 1, "fork": 1, "size": 1, "watchers_count": 1,
                         "language": 1, "has_issues": 1, "has_downloads": 1,
                         "has_wiki": 1, "forks_count": 1, "open_issues_count": 1,
                         "forks": 1, "open_issues": 1, "forks": 1, "open_issues": 1,
                         "watchers": 1, "network_count": 1, "owner": 1,
                         "permissions": 1})'''

with open('total.csv', 'w') as outfile:
    fields = ['sha', 'message', 'comment_count', 'total_deletions', 'total_additions', 
              'total', 'comments', 'additions', 'deletions', 'changes', 'status', 
              'filenames', 'name', 'fullname', 'private', 'fork', 'size', 'watchers_count',
              'language', 'has_issues', 'has_downloads', 'has_wiki', 'forks_count',
              'open_issues_count', 'forks', 'open_issues', 'watchers', 'network_count', 
              'type', 'admin', 'push', 'pull']

    write = csv.DictWriter(outfile, fieldnames=fields)
    write.writeheader()
    for commits in cursor:
        sha = commits['sha']

        body = getCommentBySha(sha)

        extracted_url = extractURL(commits['url'])
        repos = getReposInfo(extracted_url)

        if 'commit' in commits:
            commit = commits['commit']
            messageCount = getCommitCount(commit)

        if 'files' in commits:
            commit = commits['files']
            filenames, status, additions_array, deletions_array, changes = getFileNamesAndStatus(commits['files'])
    
        # Taking care of stats.
        if 'stats' in commits:
            stats = commits['stats']
            for key in stats:
                if key == 'deletions':
                    deletions = stats[key]
                elif key == 'additions':
                    additions = stats[key]
                else:
                    total = stats[key]
            flattened_record = {
                'sha': sha,
                'message': messageCount[0],
                'comment_count': messageCount[1],
                'total_additions': additions,
                'total_deletions': deletions,
                'total': total,
                'comments': body,
                'additions': additions_array,
                'deletions': deletions_array,
                'changes': changes,
                'status': status,
                'filenames': filenames,
                'name': repos['name'],
                'fullname': repos['full_name'],
                'private': repos['private'],
                'fork': repos['fork'],
                'size': repos['size'],
                'watchers_count': repos['watchers_count'],
                'language': repos['language'],
                'has_issues': repos['has_issues'],
                'has_downloads': repos['has_downloads'],
                'has_wiki': repos['has_wiki'],
                'forks_count': repos['forks_count'],
                'open_issues_count': repos['open_issues_count'],
                'forks': repos['forks'],
                'open_issues': repos['open_issues'],
                'watchers': repos['watchers'],
                'network_count': repos['network_count'],
                'type': repos['type'],
                'admin': repos['admin'],
                'push': repos['push'],
                'pull': repos['pull'],
                }
            write.writerow(flattened_record)
    print("Writing complete!!!")
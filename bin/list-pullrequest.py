#!/usr/bin/python

import argparse
import subprocess
import json
import pytz
import dateutil.parser
from datetime import datetime
import re
from config import api

parser = argparse.ArgumentParser(description = 'list closed pull request')
parser.add_argument('date', metavar = 'date', type = str, help = '[ex \'2016-03-01 15:00:00\'] search after this')
parser.add_argument('-branch', default = None, action = 'store', help = 'filtering branch name (default: no filter)')
args = parser.parse_args()

def getPullRequestJson():
    originRE = re.compile('origin\s(.*)')
    originUrl = originRE.search(subprocess.check_output('git remote -v', shell=True)).group(1)

    httpUrlRE = re.compile(':(.*)\/(.*) ')

    originOwner = originUrl.split('/')[3] if originUrl.startswith('http') else httpUrlRE.search(originUrl).group(1)
    originRepo = originUrl.split('/')[4].split('.')[0] if originUrl.startswith('http') else httpUrlRE.search(originUrl).group(2).split('.')[0]

    option = '-u %s:%s' % (api['user'], api['token']) if api['user'] and api['token'] else ''

    command = 'curl %s https://api.github.com/repos/%s/%s/pulls?state=closed' % (option, originOwner, originRepo)
    print command
    return json.loads(subprocess.check_output(command, shell=True))

class PullRequest:
    jst = pytz.timezone('Asia/Tokyo')

    @staticmethod
    def create(row):
        return PullRequest(row['merged_at'], row['title'], row['head']['ref'], row['base']['ref'])

    def __init__(self, mergedAt, title, fromBranch, toBranch):
        self.mergedAt = dateutil.parser.parse(mergedAt).astimezone(self.jst) if mergedAt is not None else None
        self.title = title
        self.fromBranch = fromBranch
        self.toBranch = toBranch

    def isTarget(self, datestring, branch):
        return self.__isTargetDate(datestring) and self._isTargetBranch(branch)

    def __isTargetDate(self, datestring):
        return self.mergedAt > datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S').replace(tzinfo=self.jst) if self.mergedAt is not None else False

    def _isTargetBranch(self, branch):
        return self.toBranch == branch if branch is not None else True

    def output(self):
        print '\n%s %s (%s -> %s)' % (str(self.mergedAt)[:-6], self.title, self.fromBranch, self.toBranch),

pullRequests = [PullRequest.create(row) for row in getPullRequestJson()]
[pr.output() for pr in pullRequests if pr.isTarget(args.date, args.branch)]

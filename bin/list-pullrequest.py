#!/usr/bin/python

import argparse
import subprocess
import json
import pytz
import dateutil.parser
from datetime import datetime

parser = argparse.ArgumentParser(description = 'list closed pull request')
parser.add_argument('date', metavar = 'date', type = str, help = '[ex 2016-03-01 15:00:00] search after this (default: now)')
parser.add_argument('-branch', default = None, action = 'store', help = 'filtering branch name (default: no filter)')
args = parser.parse_args()

def getPullRequestJson():
    originUrl = subprocess.check_output("git remote -v", shell=True)
    originOwner = originUrl.split("/")[3]
    originRepo = originUrl.split("/")[4].split(".")[0]

    command = 'curl https://api.github.com/repos/%s/%s/pulls?state=closed' % (originOwner, originRepo)
    return json.loads(subprocess.check_output(command, shell=True))

class PullRequest:
    jst = pytz.timezone('Asia/Tokyo')

    @staticmethod
    def create(row):
        return PullRequest(row['merged_at'], row['head']['ref'], row['base']['ref'])

    def __init__(self, mergedAt, fromBranch, toBranch):
        self.mergedAt = dateutil.parser.parse(mergedAt).astimezone(self.jst)
        self.fromBranch = fromBranch
        self.toBranch = toBranch

    def isTarget(self, datestring, branch):
        return self.__isTargetDate(datestring) and self._isTargetBranch(branch)

    def __isTargetDate(self, datestring):
        return self.mergedAt > datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S').replace(tzinfo=self.jst)

    def _isTargetBranch(self, branch):
        return self.toBranch == branch if branch is not None else True

    def output(self):
        print '\n%s %s -> %s' % (str(self.mergedAt)[:-6], self.fromBranch, self.toBranch),

pullRequests = [PullRequest.create(row) for row in getPullRequestJson()]
[pr.output() for pr in pullRequests if pr.isTarget(args.date, args.branch)]

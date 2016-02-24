import subprocess
import json

def getPullRequestJson():
    originUrl = subprocess.check_output("git remote -v", shell=True)
    originOwner = originUrl.split("/")[3]
    originRepo = originUrl.split("/")[4].split(".")[0]

    command = "curl https://api.github.com/repos/%s/%s/pulls?state=closed" % (originOwner, originRepo)
    return json.loads(subprocess.check_output(command, shell=True))

json = getPullRequestJson()
filtered = [pr for pr in json if pr["merged_at"] != None]
print filtered


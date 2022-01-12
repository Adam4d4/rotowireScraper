#!/bin/python3

import urllib.request
import urllib.parse
import re
import printUtil
import csvUtil

url = 'https://www.rotowire.com/hockey/nhl-lineups.php'
values = {'s':'python programming',
          'submit':'search'}
   
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read().decode("utf8")

matchUps = re.findall(r'[A-Z][a-z]* {10,}', respData)

printUtil.printMatchups(matchUps)
csvUtil.printMatchups(matchUps)
# # Away was listed first on the rotowire website. Therefor every other team will be an away team.
# away = True
# for team in matchUps:
    # if away == True:
        # print("Away team: " + team)
        # away = False
    # else:
        # print("Home team: " + team)
        # away = True
        # # Used for formatting the output
        # print()
    

									
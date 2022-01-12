import csv

def printMatchups(matchUps):
    f = open('./csv/matchups.csv', 'w') 
    # Away was listed first on the rotowire website. Therefor every other team will be an away team.
    away = True
    for team in matchUps:
        if away == True:
            f.write(team + ",")
            away = False
        else:
            f.write(team)
            away = True
            # Used for formatting the output
            f.write()
    


def printMatchups(matchUps):
    # Away was listed first on the rotowire website. Therefor every other team will be an away team.
    away = True
    for team in matchUps:
        if away == True:
            print("Away team: " + team)
            away = False
        else:
            print("Home team: " + team)
            away = True
            # Used for formatting the output
            print()
    

									

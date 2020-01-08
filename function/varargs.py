#prg of variable length arguments
def game_score(team,*score):
    'to find game score and centuries'
    sum = 0
    century = 0
    for run in score:
        sum += run
        if run >= 100:
            century += 1
    else:
            print("score of %s is % runs with %d centuries: " %(team,sum,century))
#calling function
game_score("IND", 45, 34, 33,110, 109)
game_score("ENG", 45, 34, 33,10, 109)
game_score("WI", 45, 34, 33,10, 190)
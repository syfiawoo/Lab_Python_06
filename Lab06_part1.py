"""
Seth Fiawoo
MIT-AITI 2012
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player        | date        | score
_______________________________________
rooney        | 6/23/2012    | 2
rooney        | 6/25/2012    | 2
ronaldo        | 6/19/2012    | 0
ronaldo        | 6/20/2012    | 3
torres        | 6/21/2012    | 0
torres        | 6/22/2012    | 1
"""

#1
import datetime
## create the player_stats data structure
player_stats={datetime.date(2012,06,24):['rooney',2],
              datetime.date(2012,06,25):['rooney',2],
              datetime.date(2012,06,19):['ronaldo',0],
              datetime.date(2012,06,20):['ronaldo',3],
              datetime.date(2012,06,21):['torres',0],
              datetime.date(2012,06,22):['torres',1]}

print player_stats.itervalues()

#2
#a
## implement highest_score
def highest_score(player_stats):
    highest=0
    high_date=0
    for date in player_stats.keys():
        play_goals=player_stats[date]
        if play_goals[1]>highest:
            highest=play_goals[1]
            high_date=date
    play_goals=player_stats[high_date]
    return (play_goals[0],str(high_date),play_goals[1])
    
print highest_score(player_stats) 

#b         
## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    highest=0
    high_date=0
    players=[]
    for item in player_stats.values():
        if item[0] not in players:
            players.append(item[0])
            
    if player not in players:
        return None
    
    for date in player_stats.keys():
        play_goal=player_stats[date]
        if player in play_goal:
            
            if play_goal[1]>highest:
                highest=play_goal[1]
                high_date=date
    play_goal=player_stats[high_date]
    return (play_goal[0],str(high_date),play_goal[1])

print highest_score_for_player(player_stats,'torres') 

#c
## implement highest_scorer
def highest_scorer(player_stats):
    sum_score=0
    high_scorer=''
    all_play={}
    for date in player_stats.keys():
        play_goals=player_stats[date]
        if play_goals[0] in all_play.keys():
            all_play[play_goals[0]]+=play_goals[1]
        else:
            all_play[play_goals[0]]=play_goals[1]
    for player in all_play.keys():
        if all_play[player]>sum_score:
            sum_score=all_play[player]
            high_scorer=player
    return player
    
print highest_scorer(player_stats)  
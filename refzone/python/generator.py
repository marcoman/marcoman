import datetime
import time
import json
import argparse
from random import randint, random
from weakref import ref

def gen_value(low, high):
    return randint(low, high)

def _sum(arr):
    sum=0
    for i in arr:
        sum += i
    return (sum)

o = open ("results.csv", 'w')

    
# read in ref list
with open("refs.csv", 'r') as refs:
    # process the first line to find the right indices
    line_number = 0
    index_last_name = 0
    index_first_name = 0
    index_rink = 0
    index_rink_number = 0
    index_official_id = 0
    index_home_club = 0
    index_home_team = 0
    index_home_score = 0
    index_away_club = 0
    index_away_team = 0
    index_away_score = 0

    ref_low_value = 1
    ref_high_value = 5
    for line in refs:
        if (line_number == 0):
            firstline = line.split(',')
            index = 0
            for title in firstline:
                if (title=="LastName" ):
                    index_last_name = index
                if (title=="FirstName" ):
                    index_first_name = index
                if (title=="Rink" ):
                    index_rink = index
                if (title=="Rink Number" ):
                    index_rink_number = index
                if (title=="Official ID" ):
                    index_official_id = index
                if (title=="Score Home" ):
                    index_home_score = index
                if (title=="Score Away" ):
                    index_away_score = index
                if (title=="TEAM 1" ):
                    index_home_team = index
                if (title=="TEAM 2" ):
                    index_away_team = index
                if (title=="Club 1" ):
                    index_club_home = index
                if (title=="Club 2" ):
                    index_club_away = index
                index += 1
            print ("First Name, Last Name indices are {}, {}".format(index_first_name, index_last_name))
        else:
            ref_values = []
            currentline = line.split(",")

            # initialize all values
            # Pre-game
            rate_feeling = 3.0 + (randint(-2,2))
            rate_facility = 3.0

            # Post-game
            rate_performance = 3.0
            rate_playing_area = 3.0
            rate_home_team = 3.0
            rate_away_team = 3.0
            rate_home_coach = 3.0
            rate_away_coach = 3.0
            rate_crowd = 3.0

            # Assume rink 1 is best, rink 3 is worst.  Most true for multi-rink clubs.
            if (currentline[index_rink_number] == 3):
                rate_playing_area -= 2
            elif (currentline[index_rink_number] == 2):
                rate_playing_area += 2

            # Club: Haverford-, Hershey+ all teams
            # Team: Delco Phantoms 14UA - team
            # Team: Team Philadelphia 14U AA -team
            if ((currentline[index_home_team] == "Delco Phantoms 14UA") or
                (currentline[index_home_team] == "Team Philadelphia 14U AA") or
                (currentline[index_home_club] == "Haverford Hawks")):
                rate_home_team -= 1
            if ((currentline[index_away_team] == "Delco Phantoms 14UA") or
                (currentline[index_away_team] == "Team Philadelphia 14U AA") or
                (currentline[index_away_club] == "Haverford Hawks")):
                rate_away_team -= 1
            # Team: Delco Phantoms 14UN + team
            # Team: Team Philadelphia 14U A Natonal +team
            if ((currentline[index_home_team] == "Delco Phantoms 14UA") or
                (currentline[index_home_team] == "Delco Phantoms 14U A Nat") or
                (currentline[index_home_club] == "Hershey")):
                rate_home_team += 1
            if ((currentline[index_away_team] == "Delco Phantoms 14UA") or
                (currentline[index_away_team] == "Delco Phantoms 14U A Nat") or
                (currentline[index_away_club] == "Hershey")):
                rate_away_team += 1

            # If Ref's last name is a specific length, penalize their performance
            if (len(currentline[index_last_name])==7):
                rate_performance -= 0.5
            if (currentline[index_last_name][0]=='N'):
                rate_performance += 1
                rate_away_coach -= 1
                rate_away_team -= 1
                rate_home_coach -= 1
                rate_home_team -= 1
                rate_crowd -= 1
                rate_playing_area -= 1
            elif (currentline[index_last_name][0]=='P'):
                rate_performance += 1
                rate_away_coach += 1
                rate_away_team += 1
                rate_home_coach += 1
                rate_home_team += 1
                rate_crowd += 1
                rate_playing_area += 1
            # elif (currentline[index_last_name][0]=='F'):
            #     rate_performance += 0
            else:
                rate_performance += 0

            # Crowd: Grundy-, Genesis+
            if (currentline[index_home_club] == "Grundy Senators"):
                rate_crowd -= 1
            if (currentline[index_home_club] == "Genesis Hockey Club"):
                rate_crowd += 1

            # Ref-specific adjustments.  Use a modulus to pick somebody
            # if Ref E - scores are +0.5
            # If Ref F - scores are -0.5
            # a percentages of refs are negative/positive in demeanor
            if (((int(currentline[index_official_id]) - 1200) % 9) == 5):
                rate_away_coach -= 1.5
                rate_away_team -= 1.5
                rate_home_coach -= 1.5
                rate_home_team -= 1.5
                rate_crowd -= 1.5
                rate_playing_area -= 1.5
            
            if (((int(currentline[index_official_id]) - 1200) % 9) == 6):
                rate_away_coach += 1.5
                rate_away_team += 1.5
                rate_home_coach += 1.5
                rate_home_team += 1.5
                rate_crowd += 1.5
                rate_playing_area += 1.5

            # Correlations
            rate_home_team += randint(-2,2)
            rate_away_team += randint(-2,2)
            rate_performance += randint(-2,2)
            rate_playing_area += randint(-2,2)
            # Facilities 1-5 means a chance to change crowd
            rate_crowd += randint (min (0, int(rate_playing_area-3)),
                                   max (0, int(rate_playing_area-3)))

            # Ref: coach affected
            rate_home_coach += (random() * 2) * (random() * rate_feeling -3 / 5)
            rate_away_coach += (random() * 2) * (random() * rate_feeling -3 / 5)

            # If Home or Visitor, Win, Ref ++, otherwise Lose Ref --, influenced by rink
            #    Rink condition
            #    Win/Lose +10,-10
            #    Score greater than 5: +20,-20
            if (abs(int(currentline[index_home_score]) - int(currentline[index_away_score])) > 10 ):
                rate_crowd -= 2
            elif (abs(int(currentline[index_home_score]) - int(currentline[index_away_score])) > 5 ):
                rate_crowd -= 1
            if (rate_playing_area < 2):
                rate_crowd -= 1

            # no smaller than the Max value, no higher than the min value.
            # How do you feel?
            ref_values.append(min(max(int(rate_feeling), 2),5))
            # How would you rate the facility you are at?
            ref_values.append(min(max(int(rate_facility), 1),5))
            # How would you rate your performance in the game?
            ref_values.append(min(max(int(rate_performance), 2),5))
            # What did you think of the condition of the playing area druing the game?
            ref_values.append(min(max(int(rate_playing_area), 1),5))
            # What did you think of the interaction with the players from Team 1?
            ref_values.append(min(max(int(rate_home_team), 1),5))
            # What did you think of the interaction with the players from Team 2?
            ref_values.append(min(max(int(rate_away_team), 1),5))
            # How was your experience with the coach from Team 1?
            ref_values.append(min(max(int(rate_home_coach), 1),5))
            # How was your experience with the coach from Team 2?
            ref_values.append(min(max(int(rate_away_coach), 1),5))
            # Did you have a negitive experience with the crowd?
            ref_values.append(min(max(int(rate_crowd), 1),5))

            print ("{}: sum {} {} score {}-{} rink {} ref {}.{} ".format(
                line_number,
                _sum(ref_values),
                ref_values,                
                currentline[index_home_score],
                currentline[index_away_score],
                currentline[index_rink_number],
                currentline[index_last_name], (int(currentline[index_official_id]) - 1200) % 9
                ))

            for v in ref_values:
                o.write("{},".format(v))
            o.write('\n')

        line_number += 1

o.close()

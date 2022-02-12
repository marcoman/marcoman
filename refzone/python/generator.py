
import datetime
import time
import json
import argparse
from random import randint
from weakref import ref

def gen_value(low, high):
    return randint(low, high)
    
# read in ref list
with open("refs.csv", 'r') as refs:
    # process the first line to find the right indices
    line_number = 0
    index_lastname = 0
    index_firstname = 0
    ref_low_value = 1
    ref_high_value = 5
    for line in refs:
        if (line_number == 0):
            firstline = line.split(',')
            index = 0
            for title in firstline:
                if (title=="Last Name" ):
                    index_lastname = index
                if (title=="First Name" ):
                    index_firstname = index
                index += 1
            print ("First Name, Last Name indices are {}, {}".format(index_firstname, index_lastname))
        else:
            ref_values = ['Y']

            currentline = line.split(",")
            if (currentline[index_lastname][0]=='N'):
                ref_low_value = 1
                ref_high_value = 4
            elif (currentline[index_lastname][0]=='P'):
                ref_low_value = 2
                ref_high_value = 5
            elif (currentline[index_lastname][0]=='F'):
                ref_low_value = 2
                ref_high_value = 4
            else:
                ref_low_value = 1
                ref_high_value = 5
            # Team: Delco Phantoms 14UA -
            # Team: Delco Phantoms 14UN +
            # Team: Team Philadelphia 14U AA -
            # Team: Team Philadelphia 14U A Natonal +
            # Club: Haverford-, Hershey+
            # Crowd: Grundy-, Genesis+
            # if Ref E - scores are +0.5
            # If Ref F - scores are -0.5
            # If Rink 1 - rink is good +2
            # If Rink 3 - rink is bad -2

            # Correlations
            # Facilities 1-5 means -20, -10, 0, 10, 20% chance to change crowd
            # Ref: coach affected
            # If Home or Visitor, Win, Ref ++, otherwise Lose Ref --, influenced by rink
            #    Rink: -10, -5, 0, 5, 10
            #    Win/Lose +10,-10
            #    Score greater than 5: +20,-20



            ref_values.append(gen_value(ref_low_value, ref_high_value))
            ref_values.append(gen_value(ref_low_value, ref_high_value))
            ref_values.append(gen_value(ref_low_value, ref_high_value))
            ref_values.append(gen_value(ref_low_value, ref_high_value))
            ref_values.append(gen_value(ref_low_value, ref_high_value))
            ref_values.append(gen_value(ref_low_value, ref_high_value))
            ref_values.append(gen_value(ref_low_value, ref_high_value))
            ref_values.append(gen_value(ref_low_value, ref_high_value))
            ref_values.append(gen_value(ref_low_value, ref_high_value))
            print ("{} has {}".format(currentline[index_lastname], ref_values))

        line_number += 1


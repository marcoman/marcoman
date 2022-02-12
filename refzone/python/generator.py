
import datetime
import time
import json
import argparse
from random import randint

def gen_value(low, high):
    return randint(low, high)
    
# read in ref list
with open("refs.csv", 'r') as refs:
    # process the first line to find the right indices
    line_number = 0
    index_lastname = 0;
    index_firstname = 0;
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
            currentline = line.split(",")
            if (currentline[index_lastname][0]=='N'):
                print ("{} is Negative with {},{},{},{},{}".format(currentline[index_lastname],
                gen_value(1,4), gen_value(1,4), gen_value(1,4), gen_value(1,4), gen_value(1,4)))
            elif (currentline[index_lastname][0]=='P'):
                print ("{} is Positive with {},{},{},{},{}".format(currentline[index_lastname],
                gen_value(2,5), gen_value(2,5), gen_value(2,5), gen_value(2,5), gen_value(2,5)))
            elif (currentline[index_lastname][0]=='F'):
                print ("{} is Fair with {},{},{},{},{}".format(currentline[index_lastname],
                gen_value(2,4), gen_value(2,4), gen_value(2,4), gen_value(2,4), gen_value(2,4)))
            else:
                print ("{} is Random with {},{},{},{},{}".format(currentline[index_lastname],
                gen_value(1,5), gen_value(1,5), gen_value(1,5), gen_value(1,5), gen_value(1,5)))
        line_number += 1




    # identify the first string
    # if char is N
        #answer N = fn random plus bias

    # else if char is P
    # else if char is F
    # else char is R



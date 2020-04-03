#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the timeInWords function below.
def timeInWords(h, m):

    number = {0:" o' clock",1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',14:'fourteen',15:'quarter',16:'sixteen',17:'seventeen',18:'eighteen',19:'nineteen',20:'twenty',21:'twenty one',22:'twenty two',23:'twenty three',24:'twenty four',25:'twenty five',26:'twenty six',27:'twenty seven',28:'twenty eight',29:'twenty nine',30:'half'}

    time=''

    if m==0:
        time = time + number.get(h) +number.get(0)
    elif m>=1 and m<=30 :

        if m==15 :
            time = time + number.get(15) + ' past ' + number.get(h)
        elif m==30 :
            time = time + number.get(30) + ' past ' + number.get(h)
        else :
            if m==1:
                time = time + number.get(m) + ' minute past ' + number.get(h)
            else :                 
                time = time + number.get(m) + ' minutes past ' + number.get(h)
    else :

        if h==12:
            h=0

        m=60-m

        if m==15 :
            time = time + number.get(15) + ' to ' + number.get(h+1)
        elif m==30 :
            time = time + number.get(30) + ' to ' + number.get(h+1)
        else :
            if m==1:
                time = time + number.get(m) + ' minute to ' + number.get(h+1)
            else :                 
                time = time + number.get(m) + ' minutes to ' + number.get(h+1)

    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input())

    m = int(input())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()

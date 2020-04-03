#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):

    li=list()

    for i in range(len(s)) :
        if ord(s[i])!=32 :
            li.append(s[i])

    row = math.floor(math.sqrt(len(li)))        
    col = math.ceil(math.sqrt(len(li)))

    if row*col<len(li) :
        row = row + 1

    word = ''    
    for i in range(col) :
        
        j=0
        
        while(i+j<=(len(li)-1)) :
            word += li[i+j]
            j = j+col
        word += ' '    

    return word    
            
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

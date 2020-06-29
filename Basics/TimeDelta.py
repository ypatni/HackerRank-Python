from datetime import datetime
import math
import os
import random
import re
import sys

# Complete the time_delta function below.
def time_delta(t1, t2):
    fmt= '%a %d %b %Y %H:%M:%S %z'
    # %a - abbreviated weekday 
    # %d - day of month 
    # %b - abbreviated month
    # %Y - full year 
    # %H:%M:%S - hour min sec (all full with a zero padding if needed )
    # %z - time zone name
    t1 = datetime.strptime(t1, fmt) 
    t2 = datetime.strptime(t2, fmt) 
    diff = (t2-t1).total_seconds() 

    return abs(int(diff))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(str(delta) + '\n')

    fptr.close()

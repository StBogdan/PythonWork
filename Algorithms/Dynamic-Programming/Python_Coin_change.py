#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getWays function below.
knownWays = {}


def getWays(n, c):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif (n, len(c)) in knownWays:
        return knownWays[(n, len(c))]
    else:
        # Recursive call
        # See how to build smaller with the rest of the coins
        knownWays[(n, len(c))] = sum([getWays(n-c[i], c[i:]) for i in range(len(c))])
        return knownWays[(n, len(c))]


if __name__ == '__main__':

    nm = input().split()
    n = int(nm[0])
    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))
    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'
    ways = getWays(n, c)

    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        fptr.write(str(ways) + '\n')
        fptr.close()
    except KeyError:
        print(str(ways))

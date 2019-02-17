#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the fibonacciModified function below.
def fibonacci_modified(t1, t2, n):
    if n == 1:
        return t1
    elif n == 2:
        return t2
    else:
        antepen = t1
        pen = t2
        for i in range(2, n):
            newTerm = pen*pen + antepen
            antepen = pen
            pen = newTerm
        return pen


if __name__ == '__main__':

    t1T2n = input().split()
    t1 = int(t1T2n[0])
    t2 = int(t1T2n[1])
    n = int(t1T2n[2])

    result = fibonacci_modified(t1, t2, n)

    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        fptr.write(str(result) + '\n')
        fptr.close()
    except KeyError:
        print(str(result))


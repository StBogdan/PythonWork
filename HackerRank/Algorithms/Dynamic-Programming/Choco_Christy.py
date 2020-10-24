#!/bin/python3

import math
import os
import random
import re
import sys

def equal(orignal_arr):
    results = []
    for i in range(5):
        minim =  min(orignal_arr)-i
        results.append(actualEqual(orignal_arr, minim))

    print(results)
    return min(results)


def actualEqual(original_arr,min):
    moves =0
    for x in original_arr:
        x = x-min
        if x > 0:
            # How many substract 5, substract 2 and finnaly ones
            moves += int(x / 5) + int(x % 5 / 2) + int(x % 5 % 2)
    print(f"{original_arr} gets moves {moves}")
    return moves


if __name__ == '__main__':
    t = int(input())
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    for t_itr in range(t):
        n = int(input())
        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)
        try:
            fptr = open(os.environ['OUTPUT_PATH'], 'w')
            fptr.write(str(result) + '\n')
        except KeyError:
            print(str(result))
    fptr.close()


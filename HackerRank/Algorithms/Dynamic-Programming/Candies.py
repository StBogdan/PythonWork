#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the candies function below.

alloc = []
arr = []


def candies(n, arr):
    global alloc
    alloc = [0 for _ in range(n)]

    # Sanity checks
    if n == 1:
        actual_alloc(0, 1)
        return 1

    # Cheeky
    if (sorted(arr) == arr or arr[::-1] == sorted(arr)) and len(set(arr)) == n:
        return sum([x for x in range(1, n + 1)])

    # Detect minima (edges)
    if arr[0] < arr[1]:
        actual_alloc(0, 1)
    else:
        i = 1
        if arr[i] == arr[0]:
            actual_alloc(0, 1)
        while i < n and arr[i] == arr[i - 1] and arr[i] <= arr[i+1]:
            actual_alloc(i, 1, "equality buff start")
            i += 1

    if arr[n - 2] > arr[n - 1]:
        actual_alloc(n - 1, 1)
    else:
        i = n - 2
        if arr[i] == arr[n-1]:
            actual_alloc(n-1, 1)
        while i > 0 and arr[i + 1] == arr[i] and arr[i-1] >= arr[i]:
            actual_alloc(i, 1, "equality buff end")
            i -= 1

    # First pass, detect local minima
    for i in range(1, n - 1):
        if arr[i - 1] == arr[i] and arr[i] == arr[i + 1]:
            actual_alloc(i, 1, "force")
        elif arr[i - 1] >= arr[i] and arr[i] <= arr[i + 1]:
            actual_alloc(i, 1, "local minima maybe equal")

    #  Detec max (edges)
    if arr[0] > arr[1]:
        actual_alloc(0, slope_right(0) + 1, "max at edge start")
    if arr[n - 2] < arr[n - 1]:
        actual_alloc(n - 1, slope_left(n - 1) + 1, "max at edge end")

    # trickle down economics (even though we are doing the opposite)
    for i in range(1, n - 1):
        if arr[i - 1] < arr[i] and arr[i] > arr[i + 1]:
            actual_alloc(i, max(slope_left(i), slope_right(i)) + 1, "top recurse")
        elif arr[i - 1] <= arr[i] and arr[i] >= arr[i + 1] and alloc[i] == 0 :
            if arr[i - 1] == arr[i]:
                actual_alloc(i, slope_right(i) + 1,  f"top recurse maybe right at {i}")
            elif arr[i + 1] == arr[i]:
                actual_alloc(i, slope_left(i) + 1, "top recurse maybe left")

    # for x in range(n):
    #     print(f"[{x}] {alloc[x]} for given val {arr[x]}")

    return sum(alloc)


def actual_alloc(poz, val, force="gentle"):
    if alloc[poz] != 0:
        if alloc[poz] <= val:
            print(f"BAD OOPSIE AT {poz} with {val} over {alloc[poz]}  w/ tag {force}")
        if force == "fortat":
            print(f"Forced write at {poz} with {val} over {alloc[poz]}")
            alloc[poz] = val
    else:
        # print(f"Unoposed at {poz} with {val} over {alloc[poz]} w/ tag {force}")
        alloc[poz] = val


def slope_left(start):
    j = start - 1
    # Run into known (return that)
    if alloc[j] != 0:
        return alloc[j]

    # Run into left edge (return 1)
    if j == 0:
        actual_alloc(j, 1, "slope left edge")
        return 1
    else:
        if arr[j - 1] >= arr[j]:
            actual_alloc(j, 1,  "slope left same")
            return 1
        else:
            actual_alloc(j, slope_left(j) + 1, "slope left recurse continue")
            return alloc[j]

def slope_left(start):
    j = start - 1
    # Run into known (return that)
    if alloc[j] != 0:
        return alloc[j]

    # Run into left edge (return 1)
    if j == 0:
        actual_alloc(j, 1, "slope left edge")
        return 1
    else:
        if arr[j - 1] >= arr[j]:
            actual_alloc(j, 1, "slope left same")
            return 1
        else:
            actual_alloc(j, slope_left(j) + 1, "slope left recurse continue")
            return alloc[j]


def slope_right(start):
    j = start + 1
    # Run into known (return that)
    if alloc[j] != 0:
        return alloc[j]

    # Run into right edge (return 1)
    if j == len(arr):
        actual_alloc(j, 1, "slope right edge")
        return 1
    else:
        if arr[j + 1] >= arr[j]:
            actual_alloc(j, 1, "slope right same or smaller")
            return 1
        else:
            actual_alloc(j, slope_right(j) + 1, "slope right recurse continue")
            return alloc[j]


if __name__ == '__main__':

    n = int(input())
    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)
    print(str(result))

    try:
        fptr = open(os.environ['OUTPUT_PATH'], 'w')
        fptr.write(str(result) + '\n')
        fptr.close()
    except KeyError:
        print(str(result))

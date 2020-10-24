#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))
arr.sort()
aMin = sum(arr[:len(arr)-1])
aMax = sum(arr[1:])
print(str(aMin)+" "+str(aMax))

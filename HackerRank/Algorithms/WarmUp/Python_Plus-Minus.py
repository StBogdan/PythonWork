#!/bin/python3

import sys

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

poz=0
neg=0
zer=0

for i in arr:
    if i>0:
        poz+=1
    elif i<0:
        neg+=1
    else:
        zer+=1

print(float(poz/len(arr)))
print(float(neg/len(arr)))
print(float(zer/len(arr)))

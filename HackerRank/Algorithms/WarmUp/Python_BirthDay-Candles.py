#!/bin/python3

import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

height.sort()
height.reverse()
maxCand =1


while(True):
    
    if(maxCand >= len(height) or height[maxCand-1]!=height[maxCand]):
        break
    maxCand+=1

print(maxCand)

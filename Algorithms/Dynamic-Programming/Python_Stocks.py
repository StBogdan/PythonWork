#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
        N = int(input().strip())
        prices = list(map(int, input().strip().split(' ')))
        profit=0
        currentMax=0
        for i in range(N-1,-1,-1):
            if(prices[i] >= currentMax):
                currentMax = prices[i]
            profit+=currentMax-prices[i]
        print(profit)


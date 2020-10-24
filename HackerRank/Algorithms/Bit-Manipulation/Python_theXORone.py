#!/bin/python3

import sys

def lonelyinteger(a):
    loner = 0
    for i in a:
        loner^=i
    return loner

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
result = lonelyinteger(a)
print(result)

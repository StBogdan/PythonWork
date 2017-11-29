#!/usr/bin/python3
def maxXor(l, r):
    diff = l ^ r
    max = 0
    while (diff > 0):
        diff >>= 1
        max = max*2+1
    return max
if __name__ == '__main__':
  l = int(input())
  r = int(input())
  print(maxXor(l, r))
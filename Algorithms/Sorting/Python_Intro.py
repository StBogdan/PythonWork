import sys

V = int(input())
n = int(input())
arr = [int(temp) for temp in input().strip().split(' ')]

for i in range(n):
    if(arr[i] == V):
        print(i)
        break

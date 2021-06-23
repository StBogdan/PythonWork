#!/bin/python3


def patternCount(s):
    # Complete this function
    ones = 0
    zeroes = 0
    patterns = 0
    for i in s:
        if i == "1":
            ones += 1
            if zeroes > 0 and ones % 2 == 0:
                patterns += 1
                zeroes = 0
                ones = 1
        elif i == "0" and ones > 0:
            zeroes += 1
        elif not i.isdigit():
            zeroes = 0
            ones = 0

    return patterns


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = patternCount(s)
    print(result)

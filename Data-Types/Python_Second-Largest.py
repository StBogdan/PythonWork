if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    ints = list(arr)
    ints.sort()
    ints.reverse()
    toprint = 1
    while ints[toprint - 1] == ints[toprint] and toprint < n - 1:
        toprint += 1
    if toprint < n:
        print(ints[toprint])

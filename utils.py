# Read a file
def readFile(fileName):
    file = open(fileName)
    content = file.read()
    return content


if __name__ == "__main__":
    n, k, m = map(int, input().split())
    sumArr = list(map(int, input().split()))
    sumArr.sort()

    for i in range(n - 2, -1, -1):
        sumArr[i] = sumArr[i] + sumArr[i + 1]

    print(sumArr)
    max_num = (sumArr[0] + min(k * n, m)) / n
    for i in range(1, n):
        if i > m:
            break
        res = (sumArr[i] + min((n - i) * k, m - i)) / (n - i)
        max_num = max(max_num, res)
    print(max_num)

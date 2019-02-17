def split_and_join(line):
    # write your code here
    lineArr = line.split(" ")
    return '-'.join(lineArr)


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

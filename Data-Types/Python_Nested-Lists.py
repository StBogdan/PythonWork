if __name__ == '__main__':
    stIn = []
    for _ in range(int(input())):  # Get N students
        name = input()
        score = float(input())
        stIn.append([name, score])
    for i in range(0, len(stIn) - 1):
        for j in range(i, len(stIn)):
            if stIn[i][1] > stIn[j][1]:
                temp = stIn[i]
                stIn[i] = stIn[j]
                stIn[j] = temp
    index = 1
    while stIn[index][1] == stIn[index - 1][1] and index < len(stIn):
        index += 1

    endName = []
    while True:
        endName.append(stIn[index][0])
        index += 1
        if not (index < len(stIn) and stIn[index][1] == stIn[index - 1][1]):
            break
    endName.sort()
    for name in endName:
        print(name)

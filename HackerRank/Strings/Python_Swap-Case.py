def swap_case(s):
    newStr = list(s)
    for i in range(0, len(newStr)):
        if newStr[i].islower():
            newStr[i] = newStr[i].upper()
        elif newStr[i].isupper():
            newStr[i] = newStr[i].lower()
    return ''.join(newStr)


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

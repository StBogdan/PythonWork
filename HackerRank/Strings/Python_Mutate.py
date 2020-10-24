def mutate_string(string, position, character):
        newStr = list(string)
        newStr[position]=character
        return ''.join(newStr)



if __name__ == '__main__':
        s = input()
        i, c = input().split()
        s_new = mutate_string(s, int(i), c)
        print(s_new)

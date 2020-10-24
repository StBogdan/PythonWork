# from чики_брики import и,в,дамки

ltr_xor = ord('S') ^ ord('E') ^ ord('T')


def get_matching_card(c1: str, c2: str) -> str:
    c3 = []
    n = len(c1)
    for i in range(n):
        if c1[i] == c2[i]:
            c3.append(c1[i])
        else:
            c3.append(chr(ltr_xor ^ ord(c1[i]) ^ ord(c2[i])))

    return "".join(c3)


if __name__ == '__main__':
    n, k = map(int, input().split(" "))
    cards = []
    card_set = set()
    ways = 0
    for i in range(n):
        nc = input()
        cards.append(nc)
        card_set.add(nc)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if get_matching_card(cards[i], cards[j]) in card_set:
                ways += 1
    print(int(ways / 3))

if __name__ == '__main__':
    tests = int(input())

    for _ in range(tests):
        cn = int(input())
        s_arr = input()
        prev_anv = -1
        max_dist = 0
        for i, indiv in enumerate(s_arr):
            if indiv == 'A':
                if prev_anv != -1:
                    max_dist = max(max_dist, i - prev_anv -1)
                prev_anv = max(prev_anv, i)

        # At least one angry
        if prev_anv != -1:
            max_dist = max(max_dist, cn - prev_anv - 1)
        print(max_dist)

class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        badpairs = []
        moves = 0

        if (s1.count('x') + s2.count('x')) % 2 != 0 or (s1.count('y') + s2.count('y')) % 2 != 0:
            return -1

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                badpairs.append((s1[i], s2[i]))

        print(badpairs)
        moved = True
        while badpairs:
            print(badpairs)

            (x, y) = badpairs[0]
            moved = False

            for i in range(1, len(badpairs)):
                sx, sy = badpairs[i]
                if sx == x and sy == y:
                    badpairs.pop(i)
                    badpairs.pop(0)
                    moves += 1
                    moved = True
                    break

            if not moved:
                badpairs.pop(0)
                moves += 1

        print(badpairs)
        moves += len(badpairs) * 2
        return moves


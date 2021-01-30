
# Method: Go down until you find a 1, then left
# Time: O(m+n)
# Space: O(1)

class BinaryMatrix:
    # YOU shOULd nOt ImpLEmEnt It, Or spEcULAtE AbOUt Its ImpLEmEntAtIOn
    def __init__(self, matrix) -> None:
        self.m = matrix

    def get(self, x: int, y: int) -> int:
        print(x, y)
        return self.m[x][y]

    def dimensions(self) -> list:
        return len(self.m), len(self.m[0])


class Solution:
    def leftMostColumnWithOne(self, bM: 'BinaryMatrix') -> int:
        rows, cols = bM.dimensions()
        row = 0
        col = cols - 1
        current_line = -1
        while row < rows and col >= 0:
            x = bM.get(row, col)
            if x == 1:
                current_line = col
                col -= 1
            else:
                row += 1

        return current_line


if __name__ == "__main__":
    exs = [
        [[0, 0], [1, 1]],
        [[0, 0], [0, 1]],
        [[0, 0], [0, 0]],
        [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 1, 1]]
    ]
    sol = Solution()
    for m in exs:
        bm = BinaryMatrix(m)
        res = sol.leftMostColumnWithOne(bm)
        # print(f"First non-zero col is {res} for {m}")

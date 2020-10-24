from typing import List


class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        up = [0 for _ in range(n)]
        down = [0 for _ in range(n)]

        for i in range(n):
            x = colsum[i]
            print(f"{i} {x} up= {up}\tdown={down}, limits up: {upper} down: {lower}")
            if x == 0:
                continue
            elif x == 2:
                up[i] = 1
                down[i] = 1
                upper -= 1
                lower -= 1

        for i in range(n):
            x = colsum[i]
            print(f"{i} {x} up= {up}\tdown={down}, limits up: {upper} down: {lower}")
            if x != 1:
                continue

            if upper > 0:
                up[i] = 1
                upper -= 1
            elif lower > 0:
                down[i] = 1
                lower -= 1
            else:  # Wait, that's illegal
                return []
        if upper != 0 or lower != 0:
            return []
        return [up, down]


if __name__ == '__main__':
    upper = 5
    lower = 5
    colsum = [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]
    sol = Solution()
    print(f"Ans: {sol.reconstructMatrix(upper,lower,colsum)}")
from typing import List

# Link: https://leetcode.com/problems/largest-submatrix-with-rearrangements/
# Method: Ones-ending at, sort and find largest rectangle for each row
# Time: O(n*m*log(m))
# Space: O(n*m)

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ones_to = [[0 for _ in range(cols)] for _ in range(rows)]
        for col in range(cols):
            ones_now = 0
            for row in range(rows):
                elem = matrix[row][col]
                if elem == 1:
                    ones_now += 1
                else:
                    ones_now = 0
                ones_to[row][col] = ones_now

        max_area = max(self.find_max_rect(ones_to[row]) for row in range(rows))
        return max_area

    def find_max_rect(self, arr: List[int]) -> int:
        sarr = sorted(arr, reverse=True)
        max_now = sarr[0]
        for i in range(1, len(sarr)):
            # All the prev values can also create the rectangle of current height
            multiplier = i + 1
            max_now = max(max_now, multiplier * sarr[i])

        return max_now


if __name__ == "__main__":
    exs = (
        [[0, 0, 1], [1, 1, 1], [1, 0, 1]],
        [[1, 0, 1, 0, 1]],
        [[1, 1, 0], [1, 0, 1]],
        [[0, 0], [0, 0]],
        [[1, 1, 1, 0, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1, 1, 1], [1, 0, 1, 0, 0, 0, 1, 1], [0, 1, 1, 0, 1, 1, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1], [1, 1, 1, 1, 1, 1, 0, 0], [1, 1, 1, 1,
                                                                                                                                                                                                1, 1, 1, 0], [1, 1, 1, 1, 0, 1, 0, 1], [1, 0, 0, 1, 1, 1, 1, 1], [1, 1, 1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 0, 1, 1], [1, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 0, 1]]
    )

    for ex_matrix in exs:
        sol = Solution()
        print(
            f"Result {sol.largestSubmatrix(ex_matrix)} for matrix {ex_matrix}")
        print("-"*50)

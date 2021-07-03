from typing import List

# Name: Number of Submatrices That Sum to Target
# Link: https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/
# Method: Pairwise check for rows, apply nr of subarrays with target on it
# Time: O(n^2\*m)
# Space: O(n\*m)
# Difficulty: Hard
# Note: feel free to do the check on the minimal dimension


class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        prefix_sums = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        # Build prefix sum
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                matrix_elem = matrix[r - 1][c - 1]
                prefix_sums[r][c] = (
                    prefix_sums[r - 1][c]
                    + prefix_sums[r][c - 1]
                    - prefix_sums[r - 1][c - 1]
                    + matrix_elem
                )

        # For every parir of rows, do the O(m) check for "subarray" sums
        target_matrix_count = 0
        for r_up in range(1, rows + 1):
            for r_down in range(r_up, rows + 1):
                matrix_count = 0
                sum_now = 0
                prev_sums = {0: 1}
                for col in range(1, cols + 1):
                    sum_now = prefix_sums[r_down][col] - prefix_sums[r_up - 1][col]
                    if sum_now - target in prev_sums:
                        matrix_count += prev_sums[sum_now - target]

                    prev_sums[sum_now] = prev_sums.get(sum_now, 0) + 1

                target_matrix_count += matrix_count

        return target_matrix_count

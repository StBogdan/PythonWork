from typing import List, Tuple
from collections import defaultdict

def find_max_diag(m: List[List[int]]) -> int:
    rows = len(m)  # NxN matrix
    diag_sum_dict = defaultdict(int)
    for i in range(rows):
        for j in range(rows):
            diag_sum_dict[i-j] += m[i][j]

    return max(diag_sum_dict.values())


if __name__ == "__main__":
    n = int(input())
    for case_num in range(1, n+1):
        matrix_size = int(input())
        matrix = [list(map(int, input().split(" "))) for _ in range(matrix_size)]
        res = find_max_diag(matrix)
        print("Case #" + str(case_num) + ": " + str(res))

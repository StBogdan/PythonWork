from typing import DefaultDict, List, Tuple

# Link: https://leetcode.com/problems/tuple-with-same-product/
# Method: Counter of previous products
# Time: O(n^2)
# Sapce: O(n^2)

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prods_so_far = DefaultDict(int)
        tuples = 0
        for i in range(n-1):
            for j in range(i+1, n):
                now_prod = nums[i] * nums[j]

                # how many times we have previously seen this products (default 0)
                tuples += prods_so_far[now_prod]

                prods_so_far[now_prod] += 1

        return tuples * 8

    def tupleSameProduct_old(self, nums: List[int]) -> int:
        sarr = sorted(nums)
        n = len(sarr)

        tuple_set = set()
        for i in range(n-1):
            for j in range(i+1, n):
                prod = sarr[i] * sarr[j]
                matches = self.find_prod_in_rest(sarr, prod, i, j)
                for match_i, match_j in matches:
                    tuple_set.add((i, match_i, match_j, j))

        # print(f"Found tuples {tuple_set}")
        return len(tuple_set) * 8

    def find_prod_in_rest(self, sarr: List[int], prod: int,
                          i: int, j: int) -> List[Tuple[int, int]]:
        start = i+1
        end = j-1
        matches = []

        while start < end:
            if start == i or start == j:
                start += 1
                continue

            if end == i or end == j:
                end -= 1
                continue

            s_elem = sarr[start]
            e_elem = sarr[end]
            prod_now = s_elem * e_elem

            if prod_now == prod:
                matches.append((start, end))
                start += 1
                end -= 1
            elif prod_now > prod:
                end -= 1
            else:
                start += 1

        # print(f"For target {prod}, avoiding {i} and {j}, "
            #   "got matches {matches}")
        return matches


if __name__ == "__main__":
    exs = (
        [],
        [1, 2, 3],
        [2, 6, 4, 3],
        [10, 5, 4, 2, 1],
        [2, 12, 4, 6, 8, 3],
        [7, 3, 5, 2],
    )
    sol = Solution()
    for ex in exs:
        tuple_combos = sol.tupleSameProduct(ex)
        tuple_old = sol.tupleSameProduct_old(ex)
        print(f"in {ex} found tuple nums {tuple_combos} vs {tuple_old}")
        print("-" * 50)

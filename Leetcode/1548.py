import collections
from typing import DefaultDict, List, Mapping, Tuple


# Method: Dynamic programming, solve subproblem of partial paths
# Time: O(n*m*E), where E is the number of edges
# Space: O(n*m) where n is len(names) and is len(targetPath) or O(n^2) is graph storage bigger

class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph = DefaultDict(set)
        for (a, b) in roads:
            graph[a].add(b)
            graph[b].add(a)

        # Construct matrix with len(targetPath) cols and len(names) rows
        # With dp[i][j] := The minimum cost of path subset targetPath[:j+1], starting from city names[i]
        dp = [[(None, None) for _ in range(len(targetPath))]
              for _ in range(len(names))]

        for name_ind in range(n):
            dp[name_ind][0] = (int(names[name_ind] != targetPath[0]), name_ind)

        for col_tp_elem in range(1, len(targetPath)):
            for row_city_index in range(n):
                extra_cost = 1 if names[row_city_index] != targetPath[col_tp_elem] else 0

                # Cost of the subproblem: getting the rest of the path sorted
                vecin_options = ((dp[vecin][col_tp_elem-1][0] + extra_cost, vecin)
                                 for vecin in graph[row_city_index])
                dp[row_city_index][col_tp_elem] = min(vecin_options)
                # print(f"At col: {col_tp_elem} row: {row_city_index}, set as {dp[row_city_index][col_tp_elem]}, looked at values {list(vecin_options)}, vecini {graph[row_city_index]} ")

        return self.reconstruct_path(n, dp, targetPath)

    def reconstruct_path(self, n: int, dp: List[List[tuple]], targetPath: List[str]) -> List[int]:
        start_city = None
        last_city = None

        last_cost = float('inf')
        for i in range(n):
            if dp[i][-1][0] < last_cost:
                last_cost, _ = dp[i][-1]
                last_city = i
                start_city = i

        res_path = [start_city]
        # print(f"Last hop is {last_hop}, res: {res_path}")

        for i in range(len(targetPath)-1, 0, -1):
            # print(f"Looking at {dp[last_hop][i]}")
            _,  city_hop = dp[last_city][i]
            res_path.append(city_hop)
            last_city = city_hop
        return res_path[::-1]


# def edit_distance(path_a, path_b):
#     dis = 0
#     a = len(path_a)
#     b = len(path_b)

#     if a != b:
#         return 10**9

#     for i in range(a):
#         if path_a[i] == path_b[i]:
#             dis += 1
#     return dis


if __name__ == "__main__":
    exs = (
        (5, [[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],  [
         "ATL", "PEK", "LAX", "DXB", "HND"], ["ATL", "DXB", "HND", "LAX"]),
        (4, [[1, 0], [2, 0], [3, 0], [2, 1], [3, 1], [3, 2]],
         ["ATL", "PEK", "LAX", "DXB"], ["ABC", "DEF", "GHI", "JKL", "MNO", "PQR", "STU", "VWX"]),
    )

    sol = Solution()
    for n, road_list, names, target_p in exs:
        my_found_route = sol.mostSimilar(n, road_list, names, target_p)
        print(
            f"Found route for target {target_p} is {my_found_route}")
        print("-"*50)

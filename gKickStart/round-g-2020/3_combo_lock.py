from typing import List, Tuple
from functools import partial


def same_value_ify(wheels: List[int], lock_max: int) -> int:
    distances = sorted(list(map(
        lambda x: dist_to_wrap(x, lock_max),
        wheels)))
    median = distances[len(distances) // 2]
    # print(distances, median)
    req_rots = 0
    for w in wheels:
        distance = min(
            abs(median - w),  # Go straight
            dist_to_wrap(w, lock_max) + dist_to_wrap(median, lock_max)
        )
        req_rots += distance
        # print(f"To get from {w} to {median}, rots are {distance}, max {lock_max}")

    median_inv = lock_max - median
    req_rots_inv = 0
    for w in wheels:
        distance_inv = min(
            abs(median_inv - w),  # Go straight
            dist_to_wrap(w, lock_max) + dist_to_wrap(median_inv, lock_max)
        )
        req_rots_inv += distance_inv
        # print(f"To get from {w} to {median}, rots are {distance}, max {lock_max}")

    
    return min(req_rots, req_rots_inv)


def dist_to_wrap(start_from: int,  limit: int) -> int:
    return min(abs(limit - start_from), start_from)


if __name__ == "__main__":
    n = int(input())
    for case_num in range(1, n+1):
        n, lock_max = list(map(int, input().split(" ")))
        wheels = list(map(int, input().split(" ")))
        res = same_value_ify(wheels, lock_max)
        print("Case #" + str(case_num) + ": " + str(res))

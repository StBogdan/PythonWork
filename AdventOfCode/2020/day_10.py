import heapq
from typing import DefaultDict


def ways_to_arrange(input_arr):
    known_adapters = DefaultDict(int)
    known_adapters[0] = 1
    elem_now = 0

    heapq.heapify(input_arr)
    while input_arr:
        elem_now = heapq.heappop(input_arr)
        known_adapters[elem_now] = \
            known_adapters[elem_now-3] + \
            known_adapters[elem_now-2] + \
            known_adapters[elem_now-1]

    return known_adapters[elem_now]


def get_1_3_diffs(input_arr):
    heapq.heapify(input_arr)

    prev = 0
    diffs = {1: 0, 3: 1}
    while input_arr:
        new = heapq.heappop(input_arr)

        jolt_diff = new - prev
        if jolt_diff in diffs:
            diffs[jolt_diff] += 1

        prev = new

    return diffs[1] * diffs[3]


if __name__ == "__main__":
    with open("inputs/day_10.in") as raw_input:
        input_lines = list(map(int, raw_input.read().split('\n')))

    print(ways_to_arrange(input_lines))

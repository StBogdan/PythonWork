

from os import read
from typing import Counter, List


def two_sum(nums: List[int], target=2020):
    num_counter = Counter(nums)
    for x in nums:
        if target-x == x and num_counter[x] > 2:  # Halfway point
            return (x, x)
        elif target - x in num_counter:
            return (x, target-x)

    return None


def three_sum(nums: List, target=2020):
    snums = sorted(nums)

    for i in range(len(snums)-2):
        start = i+1
        end = len(snums)-1

        while start < end:
            run_sum = snums[i] + snums[start] + snums[end]
            if run_sum == target:
                return (snums[i], snums[start], snums[end])
            elif run_sum > target:
                end -= 1
            else:
                start += 1
    return None


if __name__ == "__main__":
    with open("inputs/day_01.in") as raw_input:
        input_arr = list(map(int, raw_input.read().split('\n')))

    a, b = two_sum(two_sum(input_arr))
    a2, b2, c2 = three_sum(three_sum(input_arr))
    print("Two sum", a, b, a*b)
    print("Three sum", a2, b2, c2, a2*b2*c2)

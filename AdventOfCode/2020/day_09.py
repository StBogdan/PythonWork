
from typing import Counter, List, Optional, Tuple


def two_sum(nums, start, end, target=2020):
    num_counter = Counter(nums[start:end+1])
    # print(f"For nums of start {start} and {end}, being {nums[start:end+1]}")
    for i in range(start, end+1):
        x = nums[i]
        if target-x == x and num_counter[x] > 2:  # Halfway point
            return (x, x)
        elif target - x in num_counter:
            return (x, target-x)

    return None


def find_first_non_xmas(arr: List[int], preamble_size: int) -> Optional[int]:
    for i in range(preamble_size, len(arr)):
        # print(f"For {i} of {arr[i]}, 2sum is {two_sum(arr, i-preamble_size, i-1, arr[i])}")
        if not two_sum(arr, i-preamble_size, i-1, arr[i]):
            return arr[i]

    print("All are good, this is bad.")


def find_subarr_sum(arr: List[int], target):
    csum = arr[0]
    start = 0
    for i in range(1, len(arr)):
        x = arr[i]
        csum += x
        while csum > target and i - start > 2:
            csum-=arr[start]
            start +=1
        
        if csum == target:
            return (start ,i)


if __name__ == "__main__":
    with open("inputs/day_09.in") as raw_input:
        input_lines = list(map(int, raw_input.read().split('\n')))

    cont_sum_target = find_first_non_xmas(input_lines, 25)
    start, end = find_subarr_sum(input_lines, cont_sum_target)
    print(min(input_lines[start:end+1]), max(input_lines[start:end+1]), sum(input_lines[start:end+1]))


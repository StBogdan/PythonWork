from typing import List


def subarraySort(arr: List[int]) -> List[int]:
    n = len(arr)
    head_sorted_end = 0
    while head_sorted_end < n - 1 and arr[head_sorted_end] <= arr[head_sorted_end + 1]:
        head_sorted_end += 1

    if head_sorted_end == n - 1:  # Fully sorted
        return [-1, -1]

    mor = min(arr[head_sorted_end + 1 :])

    start_poz = 0
    while arr[start_poz] <= mor:
        start_poz += 1

    tail_sorted_end = n - 1
    while tail_sorted_end > 1 and arr[tail_sorted_end - 1] <= arr[tail_sorted_end]:
        tail_sorted_end -= 1

    mor = max(arr[:tail_sorted_end])
    end_poz = n - 1
    while arr[end_poz] >= mor:
        end_poz -= 1
    return [start_poz, end_poz]

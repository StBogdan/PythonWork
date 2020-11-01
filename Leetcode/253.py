from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = zip(*intervals)
        start_sorted = sorted(starts)
        ends_sorted = sorted(ends)

        start_ptr = 0
        end_ptr = 0
        max_conc = 0
        happening_now = 0

        while start_ptr < len(start_sorted) and end_ptr < len(ends_sorted):
            happening_now += 1
            while ends_sorted[end_ptr] < start_sorted[start_ptr]:
                end_ptr += 1
                happening_now -= 1

            max_conc = max(happening_now, max_conc)
            start_ptr += 1

        return max_conc


if __name__ == "__main__":
    exs = [
        [[0, 30], [5, 10], [15, 20]],
        [[7, 10], [2, 4]],
        [[1,1],[1,1]],
        [[0,300],[5,255],[10,200],[2,50]],
    ]
    sol = Solution()

    for ex in exs:
        ex_list = ex
        print(f"Input: {ex_list}, solution {sol.minMeetingRooms(ex_list)}")

from typing import Tuple

# Name: My Calendar II
# Link: https://leetcode.com/problems/my-calendar-ii/
# Method: Store all intervals and double booked intervals (no merging)
# Time: O(n^2)
# Space: O(n)
# Difficulty: Medium

Interval = Tuple[int, int]


class MyCalendarTwo:
    def __init__(self):
        self.booked_intervals = []
        self.dbooked_intervals = []

    @staticmethod
    def _intervals_intersect(interval1: Interval, interval2: Interval) -> bool:
        i_start, i_end = interval1
        j_start, j_end = interval2
        if i_end <= j_start or j_end <= i_start:
            return False
        elif i_end > j_start or j_end > i_start:
            return True

    def book(self, start: int, end: int) -> bool:
        # print(f"{(start, end)} ---> {self.booked_intervals=}, {self.dbooked_intervals=}")
        for dbooking in self.dbooked_intervals:
            if self._intervals_intersect((start, end), dbooking):
                return False

        for interval in self.booked_intervals:
            i_start, i_end = interval
            if self._intervals_intersect(interval, (start, end)):
                intesection = max(start, i_start), min(end, i_end)
                self.dbooked_intervals.append(intesection)

        self.booked_intervals.append((start, end))
        return True

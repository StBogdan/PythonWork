import datetime
from typing import List


def to_datetime(input_str: str):
    return datetime.datetime.strptime(input_str, "%Y-%m-%d")


class Solution:
    def days_between_dates(self, date1: str, date2: str) -> int:
        delta = to_datetime(date1) - to_datetime(date2)
        return abs(delta.days)


if __name__ == "__main__":
    sol = Solution()
    assert 1 == sol.days_between_dates("2019-06-29", "2019-06-30")
    assert 15 == sol.days_between_dates("2020-01-15", "2019-12-31")

from typing import List
from collections import deque
import unittest

# Method: Monotonic stack/deque
# Time: O(n)
# Space: O(n-k + 1) Output


class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        if len(arr) < k:
            return None

        m_queue = deque()
        for i in range(k):
            while m_queue and m_queue[-1] < arr[i]:
                m_queue.pop()
            m_queue.append(arr[i])

        res = [m_queue[0]]
        for i in range(k, len(arr)):
            if m_queue[0] == arr[i - k]:
                m_queue.popleft()

            while m_queue and m_queue[-1] < arr[i]:
                m_queue.pop()
            m_queue.append(arr[i])

            res.append(m_queue[0])
            # print(f"Looked at range ({i-k}-{i}], with stack: {m_queue}, {res}")
        return res


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_less_than_k(self):
        arr = [1, 2]
        k = 3
        self.assertEqual(self.sol.maxSlidingWindow(arr, k), None)

    def test_exactly_k(self):
        arr = [1, 2, 3]
        k = 3
        self.assertEqual(self.sol.maxSlidingWindow(arr, k), [3])

    def test_longer(self):
        arr = [1, 3, 4, 20, 34, 20, -1, -5, -2, -3, 20]
        k = 4
        self.assertEqual(
            self.sol.maxSlidingWindow(arr, k), [20, 34, 34, 34, 34, 20, -1, 20]
        )

    def test_dups(self):
        arr = [-7, -8, 7, 5, 7, 1, 6, 0]
        k = 4
        self.assertEqual(self.sol.maxSlidingWindow(arr, k), [7, 7, 7, 7, 7])


unittest.main()

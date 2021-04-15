from typing import List
from collections import Counter
import heapq
import unittest

# Method: Counter, put (count,elem) in heap or size k
# Time: O(n * log(k))
# Space: O(n + k)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []

        for elem, count in count.items():

            heapq.heappush(heap, (count, elem))
            if len(heap) > k:
                heapq.heappop(heap)

        return [y for (_, y) in heap]


    # Bonus: O(n) O(n) Bucket sort solution
    def topKFrequent_bucket(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        buckets = [ set() for _ in range(len(nums) + 1)]
        for elem, count in counts.items():
            buckets[count].add(elem)
        
        flat_buckets = [x for bucket in buckets for x in bucket]
        return flat_buckets[::-1][:k]
        


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_small(self):
        nums = [1]
        k = 1
        self.assertSetEqual(set(self.sol.topKFrequent(nums, k)), {1})
        self.assertSetEqual(set(self.sol.topKFrequent_bucket(nums, k)), {1})

    def test_regular(self):
        nums = [1, 1, 1, 2, 2, 3]
        k = 2
        self.assertSetEqual(set(self.sol.topKFrequent(nums, k)), {1, 2})
        self.assertSetEqual(set(self.sol.topKFrequent_bucket(nums, k)), {1,2})


unittest.main()

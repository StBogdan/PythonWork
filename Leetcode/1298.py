from typing import List


class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]],
                   initialBoxes: List[int]) -> int:

        q = list(initialBoxes)
        locked_boxs = set()
        candies_acc = 0

        while q:
            c_box = q.pop()
            candies_acc += candies[c_box]

            sub_box_set = set(containedBoxes[c_box])
            q.extend(x for x in sub_box_set if status[x]) # Add open boxes

            for key in keys[c_box]:
                status[key] = 1


            locked_boxs.update(x for x in sub_box_set if not status[x]) # Remember locked boxes

            locked_boxs = [x for x in locked_boxs if not status[x]]
            q.extend(x for x in locked_boxs if status[x])

        return candies_acc


if __name__ == '__main__':
    status = [1, 1, 1]
    candies = [2, 3, 2]
    keys = [[], [], []]
    containedBoxes = [[], [], []]
    initialBoxes = [2, 1, 0]
    sol = Solution()
    print(sol.maxCandies(status, candies, keys, containedBoxes, initialBoxes))

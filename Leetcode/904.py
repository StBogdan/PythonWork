
# Name: Fruit Into Baskets
# Link: https://leetcode.com/problems/fruit-into-baskets/
# Method: Keep track of start of seq of prev element (if a third seen, restart from there)
# Time: O(n)
# Space: O(1)
# Difficulty: Medium


class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        current_fruits = {}

        prev = tree[0]
        start = 0
        max_collect = 0

        for i, fruit in enumerate(tree):
            if len(current_fruits) < 2:
                current_fruits[fruit] = i

            elif fruit in current_fruits:
                if fruit != prev:
                    current_fruits[fruit] = i
            else:
                max_collect = max(max_collect, i - start)
                start = current_fruits[prev]
                current_fruits = {
                    fruit: i,
                    prev: current_fruits[prev]
                }

            prev = fruit

        max_collect = max(max_collect, len(tree) - start)
        return max_collect

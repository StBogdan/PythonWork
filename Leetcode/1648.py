from typing import List

# Name: Sell Diminishing-Valued Colored Balls
# Link: https://leetcode.com/problems/sell-diminishing-valued-colored-balls/
# Method: Sort desc. by number, sell by levels, if not full level, check the rest
# Time: O(n\* log(n))
# Space: O(n)
# Difficulty: Medium


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.sort(reverse=True)
        value = 0
        idx = 0
        width = 0
        inventory.append(0)

        while orders > 0:
            width += 1
            diff_to_next = inventory[idx] - inventory[idx + 1]

            sold = min(orders, width * diff_to_next)

            whole_lines, rest = divmod(sold, width)
            value += (
                width
                * whole_lines
                * (inventory[idx] + inventory[idx] - (whole_lines - 1))
                // 2
            ) + rest * (inventory[idx] - whole_lines)

            idx += 1
            orders -= sold

        return value % (10 ** 9 + 7)

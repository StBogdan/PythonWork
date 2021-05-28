from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:

        combo_list = [set()]
        for x in arr:
            if len(set(x)) != len(x):
                continue  # duplicates smh
            x_l = set(x)
            for combo in combo_list:
                # If no letters in common
                if len(set(combo & x_l)) == 0:
                    combo_list.append(combo | x_l)

        return len(max(combo_list, key=len))


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxLength(["cha", "r", "act", "ers"]))

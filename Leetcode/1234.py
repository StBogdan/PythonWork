from typing import List


class Solution:

    def balancedString(self, s: str) -> int:
        n = len(s)
        budget = {'Q': s.count("Q"), 'W': s.count("W"), 'E': s.count("E"), 'R': s.count("R")}

        start = 0
        min_win = n + 1
        for w_end in range(n):
            budget[s[w_end]] -= 1

            while start < n and all(x <= n / 4 for x in budget.values()):
                min_win = min(w_end - start + 1, min_win)
                budget[s[start]] += 1
                start += 1

        return min_win


if __name__ == '__main__':
    sol = Solution()
    ans = sol.balancedString("QQQW")
    print(f"Ans: {ans}")
    print(sol.balancedString("QWER"))
    print(sol.balancedString("QQQQ"))
    print(sol.balancedString("QQWE"))

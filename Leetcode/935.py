import unittest

# Method: Dynamic programming, construct ways to reach n-digit cals from previous ways (to build n-1 digits)
# Time: O(n)
# Space: O(1)


class Solution:
    def knightDialer(self, N: int) -> int:
        jump_to = {
            0: (4, 6),
            1: (6, 8),
            2: (7, 9),
            3: (4, 8),
            4: (3, 9, 0),
            5: (),
            6: (0, 1, 7),
            7: (2, 6),
            8: (1, 3),
            9: (2, 4),
        }

        # Way to form n = 0
        # Ways to form n =1, for every prev last digit, jump to others and add ways[to_jump][n] = ways[from_jump][n]
        mod_limit = 10 ** 9 + 7

        ways_now = [1] * 10  # starting poz
        for _ in range(N - 1):
            ways_next = [0] * 10
            for from_jump in range(10):
                for to_jump in jump_to[from_jump]:
                    ways_next[to_jump] += ways_now[from_jump]

            ways_now = ways_next

        return sum(ways_now) % mod_limit


class TestNokiaHorse(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_initial(self):
        self.assertEqual(self.sol.knightDialer(1), 10)

    def test_small(self):
        self.assertEqual(self.sol.knightDialer(2), 20)

    def test_larger(self):
        self.assertEqual(self.sol.knightDialer(4), 104)

    def test_largest(self):
        self.assertEqual(self.sol.knightDialer(3131), 136006598)

    def test_largester(self):
        self.assertEqual(self.sol.knightDialer(5000), 406880451)


unittest.main()

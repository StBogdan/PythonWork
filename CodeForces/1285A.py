# Name: Mezo Playing Zoma
# Link: https://codeforces.com/problemset/problem/1285/A
# Method:Counting
# Time: O(n)
# Space: O(1)
# Difficulty: A


if __name__ == "__main__":
    n = int(input())
    new_str = input()
    print(new_str.count("L") + new_str.count("R") + 1)

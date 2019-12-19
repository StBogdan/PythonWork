from collections import Counter

from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        winrar = lambda c :  "B" if c == "x" else "A"
        board = [[0 for _ in range(3)] for _ in range(3)]
        move = False
        for [x, y] in moves:
            board[x][y] = "x" if move else "o"
            move = not move

        for line in board:
            print(line)

        hasGaps = False
        for line in board:
            ce = Counter(line)
            if 0 in line:
                hasGaps = True
            if len(ce) == 1 and line[0] != 0:
                print(f"Oh yeah result time on line {line}")
                return winrar(line[0])

        for line in list(zip(*board)):  # Magic python transpose
            ce = Counter(line)
            if 0 in line:
                hasGaps = True
            # Win rar
            if len(ce) == 1 and line[0] != 0:
                print(f"Oh yeah result time on line {line}")
                return winrar(line[0])

        if (board[0][0] == board[1][1] == board[2][2] or board[2][0] == board[1][1] == board[0][2]) and board[1][
            1] != 0:
            return winrar(board[1][1])

        return "Pending" if hasGaps else "Draw"

if __name__ == '__main__':
    grid =[[2,0],[1,0],[1,1],[0,2]]
    sol = Solution()
    print(sol.tictactoe(grid))
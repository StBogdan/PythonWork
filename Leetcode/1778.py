DIRS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
REV_DIR = {"U": "D", "L": "D"}

from collections import deque

DIRS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
REV_DIR = {"U": "D", "L": "R", "R": "L", "D": "U"}


class Solution(object):
    @staticmethod
    def move_to_poz(from_poz, to_poz, visited, master):
        to_origin = list(
            map(lambda x: REV_DIR[x], Solution.moves_from_origin(from_poz, visited))
        )
        to_origin = to_origin[::-1]

        from_origin = Solution.moves_from_origin(to_poz, visited)
        move_list = to_origin + from_origin
        for move_dir in move_list:
            master.move(move_dir)

    @staticmethod
    def moves_from_origin(poz, visited):
        poz_now = poz
        moves = []
        while poz_now != (0, 0):
            dir = visited[poz_now]
            moves.append(dir)
            dx, dy = DIRS[REV_DIR[dir]]
            poz_now = (poz_now[0] + dx, poz_now[1] + dy)
        return moves[::-1]

    def findShortestPath(self, master: "GridMaster") -> int:
        points = {(0, 0): None}

        poz_now = (0, 0)
        to_visit = deque()
        to_visit.append((poz_now, 0))

        while to_visit:
            target_poz, dist = to_visit.popleft()
            self.move_to_poz(poz_now, target_poz, points, master)
            poz_now = target_poz

            # print(f"Now at {target_poz=} {dist=}")
            if master.isTarget():
                print(f"Bingo at {target_poz=}")
                return dist
            x, y = target_poz
            for dir, poz_delta in DIRS.items():
                dx, dy = poz_delta
                new_point = x + dx, y + dy
                if master.canMove(dir) and (new_point not in points):
                    to_visit.append((new_point, dist + 1))
                    points[new_point] = dir
        return -1

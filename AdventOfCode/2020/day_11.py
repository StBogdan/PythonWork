from typing import List

DIRS = [(x, y) for x in (-1, 0, 1) for y in (-1, 0, 1) if (x != 0 or y != 0)]


def conway_gol(board: List[List[str]]):
    rows, cols = len(board), len(board[0])

    new_b = board
    old_b = None
    while not are_the_same(new_b, old_b):
        old_b = new_b
        new_b = [[None for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):

                # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                # Otherwise, the seat's state does not change.
                if old_b[row][col] == ".":
                    new_b[row][col] = "."
                else:
                    nearby_occups = sum(old_b[row + d_r][col + d_c] == "#" for (d_r, d_c) in DIRS
                                        if 0 <= row + d_r < rows and 0 <= col + d_c < cols)

                    if old_b[row][col] == 'L' and nearby_occups == 0:
                        new_b[row][col] = '#'
                    elif old_b[row][col] == '#' and nearby_occups >= 4:
                        new_b[row][col] = 'L'
                    else:
                        new_b[row][col] = old_b[row][col]

        for line in new_b:
            print(line)
        print()

    occupied = 0
    for line in new_b:
        occupied += line.count("#")

    return occupied


def conway_gol_farsight(board: List[List[str]]):
    rows, cols = len(board), len(board[0])

    new_b = board
    old_b = None
    while not are_the_same(new_b, old_b):
        old_b = new_b
        new_b = [[None for _ in range(cols)] for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):

                # If a seat is empty (L) and there are no occupied seats adjacent to it, the seat becomes occupied.
                # If a seat is occupied (#) and four or more seats adjacent to it are also occupied, the seat becomes empty.
                # Otherwise, the seat's state does not change.
                if old_b[row][col] == ".":
                    new_b[row][col] = "."
                else:
                    nearby_occups = get_nearby_occups(old_b, row, col)
                    if old_b[row][col] == 'L' and nearby_occups == 0:
                        new_b[row][col] = '#'
                    elif old_b[row][col] == '#' and nearby_occups >= 5:
                        new_b[row][col] = 'L'
                    else:
                        new_b[row][col] = old_b[row][col]

    # for line in new_b:
    #     print(line)
    # print()

    occupied = 0
    for line in new_b:
        occupied += line.count("#")

    return occupied


def get_nearby_occups(board: List[List[str]], r: int, c: int) -> int:
    occupied = 0
    rows, cols = len(board), len(board[0])
    for dr, dc in DIRS:
        row_now, col_now = r + dr, c + dc
        while 0 <= row_now < rows and 0 <= col_now < cols:
            if board[row_now][col_now] == "#":
                occupied += 1
                break
            elif board[row_now][col_now] == "L":
                break

            row_now += dr
            col_now += dc

    return occupied

def are_the_same(b1, b2):
    if not (b1 and b2):
        return False

    rows, cols = len(b1), len(b1[0])

    if rows != len(b2) or cols != len(b2[0]):
        return False

    return all(b1[r][c] == b2[r][c] for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    with open("inputs/day_11.in") as raw_input:
        input_lines = list(map(list, raw_input.read().split('\n')))

    # print(input_lines)
    # print(conway_gol(input_lines))
    print(conway_gol_farsight(input_lines))

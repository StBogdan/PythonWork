
from typing import List, Tuple


DIRS = {
    "N": (0, 1),
    "S": (0, -1),
    "E": (1, 0),
    "W": (-1, 0)
}

DIR_LIST = ["N", "E", "S", "W"]


def ship_steer(command_list: List[Tuple[str, int]]):
    cur_dir = "E"
    cur_dir_ind = 1
    poz_now = (0, 0)
    for dir, span in command_list:
        if dir in DIRS:
            d_x, d_y = DIRS[dir]
        elif dir == "F":
            d_x, d_y = DIRS[cur_dir]
        elif dir == "R":
            if span % 90:
                print(f"PANIK for {span}")

            turns = span // 90
            cur_dir_ind = (cur_dir_ind + turns) % len(DIR_LIST)
            cur_dir = DIR_LIST[cur_dir_ind]
            d_x, d_y = DIRS[cur_dir]
            span = 0
        elif dir == "L":
            if span % 90:
                print(f"PANIK for {span}")

            turns = span // 90
            cur_dir_ind = (cur_dir_ind - turns) % len(DIR_LIST)
            cur_dir = DIR_LIST[cur_dir_ind]
            d_x, d_y = DIRS[cur_dir]
            span = 0

        poz_now = (poz_now[0] + d_x*span, poz_now[1] + d_y*span)

    return abs(poz_now[0]) + abs(poz_now[1])


def compass_to_vector(compass: Tuple[int, int, int, int]) -> Tuple[int, int]:
    # Taken as N, E, S, W
    return compass[1] - compass[3], compass[0] - compass[2]


def ship_waypoint(command_list: List[Tuple[str, int]]):
    cur_dir = "E"

    poz_now = (0, 0)
    waypoint = (1, 10, 0, 0)  # N,E,S,W
    waypoint_dir_int = 0
    for dir, span in command_list:
        w_x, w_y = compass_to_vector(waypoint)
        if dir in DIRS:
            # Modify waypoint
            d_x, d_y = DIRS[dir]

            new_w_x: int = w_x + d_x * span
            new_w_y: int = w_y + d_y * span

            waypoint = (
                new_w_y if new_w_y > 0 else 0,  # N
                new_w_x if new_w_x > 0 else 0,  # E
                abs(new_w_y) if new_w_y < 0 else 0,  # S
                abs(new_w_x) if new_w_x < 0 else 0,  # W
            )

        elif dir == "F":
            # Ship to waypoint
            poz_now = poz_now[0] + w_x * span, poz_now[1] + w_y * span
        elif dir == "R" or "L":
            if span % 90:
                print(f"PANIK for {span}")

            turns = span // 90 * (-1 if dir == "L" else 1)
            new_dir_int = (waypoint_dir_int + turns) % len(DIR_LIST)
            new_waypoint = [0, 0, 0, 0]

            for i in range(4):
                old_index = (waypoint_dir_int + i) % 4
                new_index = (new_dir_int + i) % 4

                new_waypoint[new_index] = waypoint[old_index]

            waypoint = tuple(new_waypoint)
            waypoint_dir_int = new_dir_int

        print(f"After move {dir}:{span:4},"
              f" ship is at poz {str(poz_now):12}, with waypoint {waypoint}")

    return abs(poz_now[0]) + abs(poz_now[1])


if __name__ == "__main__":
    with open("inputs/day_12.in") as raw_input:
        input_lines = raw_input.read().split('\n')

    commands = [(x[:1], int(x[1:])) for x in input_lines]

    print(ship_steer(commands))
    print(ship_waypoint(commands))

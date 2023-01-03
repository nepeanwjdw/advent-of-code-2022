from example_inputs.day_14 import example_input
from real_inputs.day_14 import real_input
import time

start_x = 500
start_y = 0


def get_coords_of_two_points(a: list[int], b: list[int]) -> list[int]:
    range_coords = []
    # check if the rock path is vertical
    if abs(a[1] - b[1]) and a[0] == b[0]:
        sorted_list = sorted([a[1], b[1]])
        for num in range(sorted_list[0], sorted_list[1] + 1):
            range_coords.append([a[0], num])
    # if not, then should be horizontal
    elif abs(a[0] - b[0]) and a[1] == b[1]:
        sorted_list = sorted([a[0], b[0]])
        for num in range(sorted_list[0], sorted_list[1] + 1):
            range_coords.append([num, a[1]])
    # throw an error if neither
    else:
        raise ValueError("neither horizontal or vertical")

    return range_coords


def parse_paths(paths: str) -> list:
    rock_list = []
    for path in paths.split("\n"):
        line = []
        for coords in path.split(" -> "):
            x_and_y = coords.split(",")
            line.append([int(x_and_y[0]), int(x_and_y[1])])

        rock_list.append(line)
    return rock_list


def build_rock_coords(paths: str) -> list:
    rock_list = parse_paths(paths)
    rock_coords = []
    for path in rock_list:
        for idx in range(0, len(path) - 1):
            for new_coords in get_coords_of_two_points(a=path[idx], b=path[idx + 1]):
                if new_coords not in rock_coords:
                    rock_coords.append(new_coords)
    return rock_coords


def main(rock_paths: str):
    rock_coords = build_rock_coords(paths=rock_paths)

    sand_position = [start_x, start_y]
    settled_sand = 0

    max_y = sorted([coord[1] for coord in rock_coords])[-1]
    # print(f"max y: {max_y}")

    while True:
        # print(f"sand position: {sand_position}")
        # check that the sand isn't lower than the lowest rock
        if sand_position[1] > max_y:
            print("the sand will keep falling forever")
            break
        # can we move down one?
        elif [sand_position[0], sand_position[1] + 1] not in rock_coords:
            sand_position[1] += 1
        # can we move diagonally down left?
        elif [sand_position[0] - 1, sand_position[1] + 1] not in rock_coords:
            sand_position[1] += 1
            sand_position[0] -= 1
        # can we move diagonally down right?
        elif [sand_position[0] + 1, sand_position[1] + 1] not in rock_coords:
            sand_position[1] += 1
            sand_position[0] += 1
        # add to settled sand and reset to starting position
        else:
            # print("this piece of sand can't move any further")
            rock_coords.append(sand_position)
            settled_sand += 1
            sand_position = [start_x, start_y]
        # time.sleep(0.1)

    print(f"settled sand: {settled_sand}")


def process(
    sand_position: list[int], rock_coords: list[list], max_y: int, settled_sand: int
) -> int:
    new_ss = settled_sand
    # print(f"sand position: {sand_position}")
    x = sand_position[0]
    y = sand_position[1]
    down = [x, y + 1]
    down_left = [x - 1, y + 1]
    down_right = [x + 1, y + 1]
    while True:
        # time.sleep(0.1)
        # check we haven't hit the ground
        if y + 1 == max_y:
            # print("hit the bottom")
            rock_coords.append(sand_position)
            new_ss += 1
            break
        # can we move down one?
        elif down not in rock_coords:
            # print("can move down")
            temp_ss, rock_coords = process(
                sand_position=[x, y + 1],
                rock_coords=rock_coords,
                max_y=max_y,
                settled_sand=0,
            )
            new_ss += temp_ss
        # can we move diagonally down left?
        elif down_left not in rock_coords:
            # print("can move down left")
            temp_ss, rock_coords = process(
                sand_position=[x - 1, y + 1],
                rock_coords=rock_coords,
                max_y=max_y,
                settled_sand=0,
            )
            new_ss += temp_ss
        # can we move diagonally down right?
        elif down_right not in rock_coords:
            # print("can move down right")
            temp_ss, rock_coords = process(
                sand_position=[x + 1, y + 1],
                rock_coords=rock_coords,
                max_y=max_y,
                settled_sand=0,
            )
            new_ss += temp_ss
        # are we in the starting position?
        elif sand_position == [start_x, start_y]:
            # print(f"we cant move any further {sand_position} {new_ss}")
            new_ss += 1
            break
        # add to settled sand and reset to starting position
        else:
            # print("this piece of sand can't move any further")
            rock_coords.append(sand_position)
            new_ss += 1
            break

    # print(f"settled sand: {settled_sand}")

    return new_ss, rock_coords


def main_two(rock_paths: str):
    rock_coords = build_rock_coords(paths=rock_paths)

    sand_position = [start_x, start_y]

    max_y = sorted([coord[1] for coord in rock_coords])[-1] + 2
    print(f"max y: {max_y}")

    settled_sand, rock_coords = process(
        sand_position=sand_position,
        rock_coords=rock_coords,
        max_y=max_y,
        settled_sand=0,
    )

    print(f"settled sand: {settled_sand}")


# print("example should be 24 at rest")
# main(example_input)
# print("real input should be 737")
# main(real_input)
# print("example II should be 93")
# main_two(example_input)
print("real input")
main_two(real_input)

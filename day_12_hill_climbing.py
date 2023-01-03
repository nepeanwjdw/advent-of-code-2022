from copy import deepcopy
from typing import Any

from example_inputs.day_12 import example_input
from real_inputs.day_12 import real_input


def get_char_value(char: str) -> int:
    number = ord(char)
    if 65 <= number <= 90:
        # Upper case letter
        return number - 38
    elif 97 <= number <= 122:
        # Lower case letter
        return number - 96
    # Unrecognized character
    raise Exception("error")


class Options:
    def __init__(self, x: int, y: int, heightmap_list: list[list[Any]]) -> None:
        self.x = x
        self.y = y
        self.max_x = len(heightmap_list[1]) - 1
        self.max_y = len(heightmap_list) - 1
        self.current_elevation = heightmap_list[y][x]

    def can_move_left(self, hm: list[list[Any]]) -> bool:
        can_move = False
        if self.x > 0 and self.current_elevation >= hm[self.y][self.x - 1] - 1:
            can_move = True
        return can_move

    def can_move_right(self, hm: list[list[Any]]) -> bool:
        can_move = False
        if self.x < self.max_x and self.current_elevation >= hm[self.y][self.x + 1] - 1:
            can_move = True
        return can_move

    def can_move_up(self, hm: list[list[Any]]) -> bool:
        can_move = False
        if self.y > 0 and self.current_elevation >= hm[self.y - 1][self.x] - 1:
            can_move = True
        return can_move

    def can_move_down(self, hm: list[list[Any]]) -> bool:
        can_move = False
        if self.y < self.max_y and self.current_elevation >= hm[self.y + 1][self.x] - 1:
            can_move = True
        return can_move


def parse_heightmap(heightmap: str):
    heightmap_list = []
    starting_points = []
    e_x = None
    e_y = None
    for y, line in enumerate(heightmap.split("\n")):
        line_list = []
        for x, char in enumerate(line):
            if char == "a":
                line_list.append(get_char_value("a"))
                starting_points.append([x, y])
            elif char == "S":
                line_list.append(get_char_value("a"))
                starting_points.append([x, y])
            elif char == "E":
                line_list.append(get_char_value("z"))
                e_x = x
                e_y = y
            else:
                line_list.append(get_char_value(char))
        heightmap_list.append(line_list)

    return heightmap_list, starting_points, e_x, e_y


class StaticVars:
    def __init__(
        self,
        s_x: int,
        s_y: int,
        e_x: int,
        e_y: int,
    ) -> None:
        self.s_x = s_x
        self.s_y = s_y
        self.e_x = e_x
        self.e_y = e_y
        self.starting_coords = f"({s_x},{s_y})"
        self.end_coords = f"({e_x},{e_y})"
        self.all_cords = set()
        self.all_cords.add(self.starting_coords)


class TempVars:
    def __init__(
        self, current_x: int, current_y: int, starting_coords: str, e_x: int, e_y: int
    ) -> None:
        self.current_x = current_x
        self.current_y = current_y
        self.e_x = e_x
        self.e_y = e_y
        self.distance = 5_000
        self.proposed_path = None
        self.proposed_coords = None
        self.current_path = starting_coords
        self.temp_coords_history = set()
        self.temp_coords_history.add(starting_coords)
        self.steps = 0
        self.least_steps = 1_000_000

    def update_path(self):
        self.steps += 1
        self.temp_coords_history.add(self.proposed_coords)
        self.current_path = self.proposed_path
        distance_x = abs(self.e_x - self.current_x)
        distance_y = abs(self.e_y - self.current_y)
        distance = distance_x + distance_y
        self.distance = distance

    def move_left(self):
        self.current_x -= 1
        self.update_path()

    def move_right(self):
        self.current_x += 1
        self.update_path()

    def move_up(self):
        self.current_y -= 1
        self.update_path()

    def move_down(self):
        self.current_y += 1
        self.update_path()

    def reached_end(self):
        new_steps = self.steps + 1
        if new_steps < self.least_steps:
            self.least_steps = new_steps

    def update_proposed(self):
        self.proposed_path = self.current_path + "," + self.proposed_coords


def distance_to_end(tv: TempVars):
    return tv.distance + tv.steps


def get_least_steps(tv: TempVars):
    return tv.steps


def main(heightmap: str):
    heightmap_list, starting_points, e_x, e_y = parse_heightmap(heightmap=heightmap)
    svs: list[StaticVars] = []
    least_steps = None
    for starting_point in starting_points:
        svs.append(
            StaticVars(
                s_x=starting_point[0],
                s_y=starting_point[1],
                e_x=e_x,
                e_y=e_y,
            )
        )
    for sv in svs:
        tv = TempVars(
            current_x=sv.s_x,
            current_y=sv.s_y,
            starting_coords=sv.starting_coords,
            e_x=sv.e_x,
            e_y=sv.e_y,
        )
        queue: list[TempVars] = [tv]
        while queue:
            queue.sort(key=get_least_steps)
            next_square = queue.pop(0)
            if len(queue) > 100:
                queue = queue[:100]
            new_queue, new_least_steps = process_one(
                sv=sv, tv=next_square, heightmap_list=heightmap_list
            )
            queue.extend(new_queue)
            if new_least_steps and (not least_steps or new_least_steps < least_steps):
                least_steps = new_least_steps
                print(f"new steps is now: {least_steps}")

    print(f"least steps is: {least_steps}")


def process_one(sv: StaticVars, tv: TempVars, heightmap_list: list[list]):
    new_queue = []
    least_steps = None
    options = Options(x=tv.current_x, y=tv.current_y, heightmap_list=heightmap_list)
    if options.can_move_left(hm=heightmap_list):
        tv.proposed_coords = f"({tv.current_x-1},{tv.current_y})"
        tv.update_proposed()
        if tv.proposed_coords not in sv.all_cords:
            if tv.proposed_coords == sv.end_coords:
                tv.reached_end()
                if not least_steps or tv.least_steps < least_steps:
                    least_steps = tv.least_steps
            else:
                new_vars = deepcopy(tv)
                new_vars.move_left()
                sv.all_cords.add(tv.proposed_coords)
                new_queue.append(new_vars)
    if options.can_move_right(hm=heightmap_list):
        tv.proposed_coords = f"({tv.current_x+1},{tv.current_y})"
        tv.update_proposed()
        if tv.proposed_coords not in sv.all_cords:
            if tv.proposed_coords == sv.end_coords:
                tv.reached_end()
                if not least_steps or tv.least_steps < least_steps:
                    least_steps = tv.least_steps
            else:
                new_vars = deepcopy(tv)
                new_vars.move_right()
                sv.all_cords.add(tv.proposed_coords)
                new_queue.append(new_vars)
    if options.can_move_up(hm=heightmap_list):
        tv.proposed_coords = f"({tv.current_x},{tv.current_y-1})"
        tv.update_proposed()
        if tv.proposed_coords not in sv.all_cords:
            if tv.proposed_coords == sv.end_coords:
                tv.reached_end()
                if not least_steps or tv.least_steps < least_steps:
                    least_steps = tv.least_steps
            else:
                new_vars = deepcopy(tv)
                new_vars.move_up()
                sv.all_cords.add(tv.proposed_coords)
                new_queue.append(new_vars)
    if options.can_move_down(hm=heightmap_list):
        tv.proposed_coords = f"({tv.current_x},{tv.current_y+1})"
        tv.update_proposed()
        if tv.proposed_coords not in sv.all_cords:
            if tv.proposed_coords == sv.end_coords:
                tv.reached_end()
                if not least_steps or tv.least_steps < least_steps:
                    least_steps = tv.least_steps
            else:
                new_vars = deepcopy(tv)
                new_vars.move_down()
                sv.all_cords.add(tv.proposed_coords)
                new_queue.append(new_vars)

    return new_queue, least_steps


print("example should equal 31")
main(example_input)
print("puzzle input should be 447")
main(real_input)

import re
from collections import Counter
from typing import Optional

from example_inputs.day_15 import example_input
from real_inputs.day_15 import real_input


class SensorBeacon:
    def __init__(self, line: str) -> None:
        coords = [int(num) for num in re.findall(r"-?\d+", line)]
        self.sensor_x = coords[0]
        self.sensor_y = coords[1]
        self.beacon_x = coords[2]
        self.beacon_y = coords[3]
        self.sensor_radius = abs(self.sensor_x - self.beacon_x) + abs(
            self.sensor_y - self.beacon_y
        )
        self.min_y = self.sensor_y - self.sensor_radius
        self.max_y = self.sensor_y + self.sensor_radius

    def get_width(self, row: int) -> int:
        return self.sensor_radius - abs(row - self.sensor_y)

    def get_x_min_max_san(self, row: int, max_coord: int) -> Optional[list[int]]:
        x_range = None
        width = self.get_width(row=row)
        if width < 1:
            return x_range
        min = self.sensor_x - width
        max = self.sensor_x + width
        if min < 0:
            min = 0
        if max > max_coord:
            max = max_coord

        if min <= max_coord and max >= 0:
            x_range = [*range(min, max + 1)]
        return x_range

    def is_relevant_to_row(self, row: int, max_coord: int) -> bool:
        if not (row >= self.min_y and row <= self.max_y):
            return False
        width = self.get_width(row=row)
        if width < 1:
            return False
        min = self.sensor_x - width
        max = self.sensor_x + width
        if min <= max_coord and max >= 0:
            return True
        return False


def build_boundaries(links: list[SensorBeacon], max_coord: int):
    border_coords = {}
    current_x = None
    current_y = None

    for link in links:
        # print(link.sensor_radius)
        current_x = link.sensor_x
        current_y = link.min_y - 1
        if 0 <= current_x <= max_coord and 0 <= current_y <= max_coord:
            if f"({current_x},{current_y})" in border_coords:
                border_coords[f"({current_x},{current_y})"] += 1
            else:
                border_coords[f"({current_x},{current_y})"] = 1
        # go diagonlly down right
        for _ in range(link.sensor_radius + 1):
            current_y += 1
            current_x += 1
            if 0 <= current_x <= max_coord and 0 <= current_y <= max_coord:
                if f"({current_x},{current_y})" in border_coords:
                    border_coords[f"({current_x},{current_y})"] += 1
                else:
                    border_coords[f"({current_x},{current_y})"] = 1
        # go diagonlly down left
        for _ in range(link.sensor_radius + 1):
            current_y += 1
            current_x -= 1
            if 0 <= current_x <= max_coord and 0 <= current_y <= max_coord:
                if f"({current_x},{current_y})" in border_coords:
                    border_coords[f"({current_x},{current_y})"] += 1
                else:
                    border_coords[f"({current_x},{current_y})"] = 1
        # go diagonlly up left
        for _ in range(link.sensor_radius + 1):
            current_y -= 1
            current_x -= 1
            if 0 <= current_x <= max_coord and 0 <= current_y <= max_coord:
                if f"({current_x},{current_y})" in border_coords:
                    border_coords[f"({current_x},{current_y})"] += 1
                else:
                    border_coords[f"({current_x},{current_y})"] = 1
        # go diagonlly up right
        for _ in range(link.sensor_radius + 1):
            current_y -= 1
            current_x += 1
            if 0 <= current_x <= max_coord and 0 <= current_y <= max_coord:
                if f"({current_x},{current_y})" in border_coords:
                    border_coords[f"({current_x},{current_y})"] += 1
                else:
                    border_coords[f"({current_x},{current_y})"] = 1

    row_counts = Counter(
        list(re.findall(r"-?\d+", k)[1] for k, v in border_coords.items() if v > 3)
    )

    return [
        int(k)
        for k, v in sorted(row_counts.items(), key=lambda item: item[1], reverse=True)
    ]


def parse_input(input: str) -> list[SensorBeacon]:
    return [SensorBeacon(line=line) for line in input.split("\n")]


def process_row(links: list[SensorBeacon], row: int) -> int:
    beacons_and_sensors = set()
    no_beacons = set()
    for link in links:
        if link.sensor_y == row:
            beacons_and_sensors.add(link.sensor_x)
        if link.beacon_y == row:
            beacons_and_sensors.add(link.beacon_x)
        on_row_width = link.get_width(row=row)
        if on_row_width > 0:
            no_beacons.update(
                [*range(link.sensor_x - on_row_width, link.sensor_x + on_row_width + 1)]
            )

    for square in beacons_and_sensors:
        if square in no_beacons:
            no_beacons.remove(square)

    return len(no_beacons)


def process_row_two(
    links: list[SensorBeacon], row: int, max_coord: int
) -> Optional[int]:
    hidden_beacon = None
    filled_squares = set()

    for link in links:
        if link.sensor_y == row and 0 <= link.sensor_y <= max_coord:
            filled_squares.add(link.sensor_x)
        if link.beacon_y == row and 0 <= link.beacon_y <= max_coord:
            filled_squares.add(link.beacon_x)
        x_range = link.get_x_min_max_san(row=row, max_coord=max_coord)
        if x_range is not None:
            filled_squares.update(x_range)

    if len(filled_squares) < max_coord + 1:
        hidden_beacon = sorted(set(range(0, max_coord + 1)).difference(filled_squares))[
            0
        ]

    return hidden_beacon


def main(closest_beacons: str, row_to_check: int):
    parsed_input = parse_input(closest_beacons)
    no_beacons_count = process_row(links=parsed_input, row=row_to_check)

    print(f"places where no beacons can be present: {no_beacons_count}")


def main_two(closest_beacons: str, most_coords: int):
    parsed_input = parse_input(closest_beacons)
    rows = build_boundaries(links=parsed_input, max_coord=most_coords)
    print(
        f"{len(rows)} rows to search through where there are four border intersections"
    )
    for row in rows:
        links = [
            link
            for link in parsed_input
            if link.is_relevant_to_row(row=row, max_coord=most_coords)
        ]
        print(row)
        hidden_beacon = process_row_two(links=links, row=row, max_coord=most_coords)
        if hidden_beacon:
            print(f"hidden beacon at ({hidden_beacon},{row})")
            print(f"tuning frequency: {hidden_beacon*4000000 + row}")
            break


print("example should return 26")
main(closest_beacons=example_input, row_to_check=10)
print("puzzle input should be 4886370")
main(closest_beacons=real_input, row_to_check=2000000)
print("example part II should be 56000011")
main_two(closest_beacons=example_input, most_coords=20)
print(
    "puzzle input part II should be 11374534948438 hidden beacon at (2843633,2948438)"
)
main_two(closest_beacons=real_input, most_coords=4000000)

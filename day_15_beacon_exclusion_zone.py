import re
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

    def get_width(self, row: int) -> int:
        return self.sensor_radius - abs(row - self.sensor_y)


def parse_input(input: str) -> list[SensorBeacon]:
    return [SensorBeacon(line=line) for line in input.split("\n")]


def process_row(
    links: list[SensorBeacon], row: int, max_coord: int
) -> tuple[int, Optional[int]]:
    hidden_beacon = None
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

    no_beacons_in_range = [square for square in no_beacons if 0 <= square <= max_coord]
    beac_sens_in_range = [
        square for square in beacons_and_sensors if 0 <= square <= max_coord
    ]
    no_beacons_in_range.extend(beac_sens_in_range)
    if len(no_beacons_in_range) < max_coord + 1:
        hidden_beacon = sorted(
            set(range(0, max_coord + 1)).difference(no_beacons_in_range)
        )[0]

    return len(no_beacons), hidden_beacon


def main(closest_beacons: str, row_to_check: int):
    parsed_input = parse_input(closest_beacons)
    no_beacons_count, hidden_beacon = process_row(
        links=parsed_input, row=row_to_check, max_coord=20
    )

    print(f"places where no beacons can be present: {no_beacons_count}")


def main_two(closest_beacons: str, most_coords: int):
    parsed_input = parse_input(closest_beacons)
    for row in range(0, most_coords + 1):
        print(row)
        no_beacons_count, hidden_beacon = process_row(
            links=parsed_input, row=row, max_coord=20
        )
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
# print("puzzle input")
# main_two(closest_beacons=real_input, most_coords=4000000)

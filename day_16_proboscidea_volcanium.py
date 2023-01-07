import re

from example_inputs.day_16 import example_input
from real_inputs.day_16 import real_input


class Valve:
    def __init__(self, line: str) -> None:
        all_valves = re.findall(r"[A-Z]{2}", line)
        self.valve = all_valves.pop(0)
        self.leads_to = all_valves
        self.flow_rate = int(re.findall(r"\d+", line)[0])


def parse_input(scan: str) -> list[Valve]:
    valves = []
    for line in scan.split("\n"):
        valves.append(Valve(line=line))

    return valves


def main(scan: str):
    valves = parse_input(scan=scan)
    for valve in valves:
        print(valve.valve)
        print(valve.leads_to)
        print(valve.flow_rate)


print("example should return ")
main(scan=example_input)
# print("puzzle input should be ")
# main()

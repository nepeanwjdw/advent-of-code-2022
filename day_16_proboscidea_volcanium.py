import re

from example_inputs.day_16 import example_input
from real_inputs.day_16 import real_input


def parse_input(scan: str) -> list:
    return scan.split("\n")


def main(scan: str):
    print(parse_input(scan=scan))


print("example should return ")
main(scan=example_input)
# print("puzzle input should be ")
# main()

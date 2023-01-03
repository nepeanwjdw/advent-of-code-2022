import re

from example_inputs.day_5 import example_input
from real_inputs.day_5 import real_input


def build_crates_onto_stacks(stack_numbers: list[str], rows_in_reverse: list[str]) -> dict:
    line = 1
    stacks_with_crates = {}
    for stack in stack_numbers:
        stacks_with_crates[stack] = []
    
    for row in rows_in_reverse:
        line = 1
        for stack in stack_numbers:
            if row[line] != " ":
                stacks_with_crates[stack].insert(0, row[line])
            line += 4
    
    return stacks_with_crates

def get_rows_in_reverse(stacks: str) -> list[str]:
    stacks_list = list(reversed(stacks.split("\n")))
    del stacks_list[0]
    return stacks_list

def crates_on_top(stack_numbers: list[str], stacks_with_crates: dict) -> str:
    first_crate_per_stack = ""
    for stack in stack_numbers:
        first_crate_per_stack = "".join([first_crate_per_stack, stacks_with_crates[stack][0]])
    
    return first_crate_per_stack

def get_stack_numbers(stacks: str) -> list[str]:
    return re.findall(r"\d", stacks)

def parse_orders(orders: str) -> list[dict]:
    orders_by_row = orders.split("\n")
    parsed_orders = []
    for row in orders_by_row:
        row_by_part = row.split(" ")
        parsed_orders.append({
            "move": row_by_part[1],
            "from": row_by_part[3],
            "to": row_by_part[5],
        })

    return parsed_orders


def split_stacks_from_orders(stacks_and_orders: str) -> tuple[str, str]:
    as_list = stacks_and_orders.split("\n\n")
    return as_list[0], as_list[1]

def process_orders_old(parsed_stacks: dict, parsed_orders: list[dict]) -> dict:
    for order in parsed_orders:
        move_times = int(order["move"])
        for _ in range(0, move_times):
            parsed_stacks[order["to"]].insert(0, parsed_stacks[order["from"]][0])
            del parsed_stacks[order["from"]][0]
    
    return parsed_stacks

def process_orders(parsed_stacks: dict, parsed_orders: list[dict]) -> dict:
    crane = []
    for order in parsed_orders:
        move_times = int(order["move"])
        for _ in range(0, move_times):
            crane.insert(0, parsed_stacks[order["from"]][0])
            del parsed_stacks[order["from"]][0]
        for crate in crane:
            parsed_stacks[order["to"]].insert(0, crate)
        crane = []
    
    return parsed_stacks

def main(stacks_and_orders: str) -> str:
    stacks, orders = split_stacks_from_orders(stacks_and_orders)
    stack_numbers = get_stack_numbers(stacks)
    rows_in_reverse = get_rows_in_reverse(stacks)
    stacks_with_crates = build_crates_onto_stacks(stack_numbers, rows_in_reverse)
    orders_as_dicts = parse_orders(orders)
    processed_stacks = process_orders(stacks_with_crates, orders_as_dicts)
    print(crates_on_top(stack_numbers, processed_stacks))


main(example_input)
main(real_input)

import re
from math import prod

from example_inputs.day_11 import example_input
from real_inputs.day_11 import real_input


def build_monkeys(monkeys_split: list[str]) -> list:
    monkeys = []
    for monkey in monkeys_split:
        lines_for_monkey = monkey.split("\n")
        starting_items_str = lines_for_monkey[1]
        operation_str = lines_for_monkey[2]
        test_str = lines_for_monkey[3]
        if_true_str = lines_for_monkey[4]
        if_false_str = lines_for_monkey[5]

        divisible_by = int(re.findall(r"\d+", test_str)[0])

        true_monkey = int(re.findall(r"\d", if_true_str)[0])
        false_monkey = int(re.findall(r"\d", if_false_str)[0])

        items_as_list = re.findall(r"\d+", starting_items_str)
        items = [int(item) for item in items_as_list]

        expression = None
        if "old * old" in operation_str:
            expression = "**2"
        else:
            expression = re.findall(r"\W\s\d+", operation_str)[0]
        
        is_multiply = True
        if "+" in expression:
            is_multiply = False
        
        expr_num = 0
        if expression != "**2":
            expr_num = int(expression.split(" ")[1])

        monkeys.append({
            "items": items,
            "expression": expression,
            "is_multiply": is_multiply,
            "expr_num": expr_num,
            "test": divisible_by,
            "true_monkey": true_monkey,
            "false_monkey": false_monkey,
            "inspections": 0,
        })
    
    return monkeys


def main(monkey_notes: str, reduce_worry: bool = True, rounds: int = 20):
    monkeys_split = monkey_notes.split("\n\n")
    monkeys = build_monkeys(monkeys_split)
    mod = prod([a["test"] for a in monkeys])
    for _ in range(0, rounds):
        for i in range(0, len(monkeys)):
            for item in monkeys[i]["items"]:
                # monkey inspects item
                monkeys[i]["inspections"] += 1
                # multiply worry level
                if monkeys[i]["expression"] == "**2":
                    new_val = item * item
                else:
                    if monkeys[i]["is_multiply"]:
                        new_val = item * monkeys[i]["expr_num"]
                    else:
                        new_val = item + monkeys[i]["expr_num"]
                # monkey gets bored
                if reduce_worry:
                    new_val = int(new_val / 3)
                # apply test
                new_val = new_val % mod
                if new_val % monkeys[i]["test"] == 0:
                    throw_to_monkey = monkeys[i]["true_monkey"]
                else:
                    throw_to_monkey = monkeys[i]["false_monkey"]
                # throw item to another monkey
                monkeys[throw_to_monkey]["items"].append(new_val)
            
            # once all items have been thrown by the current monkey, reset items
            monkeys[i]["items"] = []
        
    all_inspections = [monkey["inspections"] for monkey in monkeys]
    inspections = sorted(all_inspections)

    print(inspections[-1] * inspections[-2])

                
    


print("example input should return 10605")
main(example_input)

print("real input should be 58794")
main(real_input)

print("example input with 10000 rounds should return 2713310158")
main(example_input, False, 10000)

print("real input with 10000 rounds")
main(real_input, False, 10000)

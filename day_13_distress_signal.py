from typing import Union

from example_inputs.day_13 import example_input
from real_inputs.day_13 import real_input


def is_right_order(left: Union[int, list], right: Union[int, list]) -> bool:
    i = 0
    while True:
        # print(f"i is {i}")
        left_last_item = i + 1 > len(left)
        right_last_item = i + 1 > len(right)
        # if not left and not right:
        #     i += 1
        #     continue
        if not left or left_last_item:
            # print("left ran out of items, in order")
            return True
        if not right or right_last_item:
            # print("right ran out of items, not in order")
            return False
        # print(f"comparing left {left[i]} right {right[i]}")
        if type(left[i]) == list and type(right[i]) == list:
            # print("both sides are lists")
            if not left[i] and not right[i]:
                # print("both lists are empty")
                i += 1
                continue
            recursion = is_right_order(left=left[i], right=right[i])
            if recursion == None:
                if i + 1 == len(left) and i + 1 == len(right):
                    # print("we're at the last item of left and right")
                    return None
                i += 1
                continue
            else:
                return recursion
        elif type(left[i]) == int and type(right[i]) == int:
            if left[i] == right[i]:
                if i + 1 == len(left) and i + 1 == len(right):
                    # print("we're at the last item of left and right")
                    return None
                # print("both sides are equal, moving forwards")
                i += 1
                continue
            # print(f"return value: {left[i] < right[i]}")
            return left[i] < right[i]
        elif type(left[i]) == int:
            recursion = is_right_order(left=[left[i]], right=right[i])
            if recursion == None:
                if i + 1 == len(left) and i + 1 == len(right):
                    # print("we're at the last item of left and right")
                    return None
                i += 1
                continue
            else:
                return recursion
        elif type(right[i]) == int:
            recursion = is_right_order(left=left[i], right=[right[i]])
            if recursion == None:
                if i + 1 == len(left) and i + 1 == len(right):
                    # print("we're at the last item of left and right")
                    return None
                i += 1
                continue
            else:
                return recursion
        raise Exception("this code should not be executed")


def parse_packets_all(signal: str) -> list:
    packets = []
    for pair_str in signal.split("\n\n"):
        lines = pair_str.split("\n")
        for line in lines:
            packets.append(eval(line))

    return packets


def parse_packets_pairs(signal: str) -> list:
    packets = []
    for pair_str in signal.split("\n\n"):
        lines = pair_str.split("\n")
        pair = []
        for line in lines:
            pair.append(eval(line))
        packets.append(pair)

    return packets


def main(signal: str):
    packets = parse_packets_pairs(signal=signal)

    pairs_in_right_order = []

    for index, pair in enumerate(packets):
        # print(f"== Pair {index+1} ==")
        left = pair[0]
        # print(f"left is {left}")
        right = pair[1]
        # print(f"right is {right}")
        result = is_right_order(left=left, right=right)
        if result == None:
            raise Exception("exception")
        if result:
            pairs_in_right_order.append(index + 1)

    # print(pairs_in_right_order)
    print(sum(pairs_in_right_order))


def apply_sort(sorted_packets: list[list], new_item: list) -> list[list]:
    i = 0
    while True:
        # print(f"attempting to introduce {new_item} at position {i}")
        result = is_right_order(left=sorted_packets[i], right=new_item)
        if result == None:
            raise Exception("exception")
        elif result:
            if i == len(sorted_packets) - 1:
                sorted_packets.append(new_item)
                break
            else:
                i += 1
                continue
        else:
            sorted_packets.insert(i, new_item)
            break

    return sorted_packets


def main_part_two(signal: str):
    packets = parse_packets_all(signal=signal)
    first_divider = [[2]]
    second_divider = [[6]]
    packets.append(first_divider)
    packets.append(second_divider)

    first_item = packets.pop(0)
    packets_in_right_order = [first_item]

    for line in packets:
        packets_in_right_order = apply_sort(packets_in_right_order, line)

    # for line in packets_in_right_order:
    #     print(line)

    first_index = packets_in_right_order.index(first_divider) + 1
    second_index = packets_in_right_order.index(second_divider) + 1
    decoder_key = first_index * second_index

    print(f"index {first_index} * {second_index} = {decoder_key}")


# print("example should equal 13")
# main(example_input)
# print("puzzle input:")
# main(real_input)

print("example part II should equal 140")
main_part_two(example_input)
print("puzzle input part II")
main_part_two(real_input)

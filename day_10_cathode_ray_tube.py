from example_inputs.day_10 import example_input
from real_inputs.day_10 import real_input


def main(program: str):
    instructions = program.split("\n")
    cycle = 0
    register = 1
    row = 0
    check_for = [20, 60, 100, 140, 180, 220]
    cycles_to_move_down = [40, 80, 120, 160, 200, 240]
    signal_strengths = []
    output = ""
    hash = "██"
    dot = "░░"
    # hash = "#"
    # dot = "."

    for line in instructions:
        line_as_list = line.split(" ")
        instruction = line_as_list[0]
        if instruction == "noop":
            cycle += 1
            add_length = 40 * row
            reg_range = [register -1 + add_length, register + add_length, register + 1 + add_length]
            if cycle-1 in reg_range:
                output += hash
            else:
                output += dot
            if cycle in check_for:
                signal_strengths.append(cycle * register)
            if cycle in cycles_to_move_down:
                row += 1
                output += "\n"
            
        else:
            value = line_as_list[1]
            # start first cycle
            cycle += 1
            add_length = 40 * row
            reg_range = [register -1 + add_length, register + add_length, register + 1 + add_length]
            if cycle-1 in reg_range:
                output += hash
            else:
                output += dot
            if cycle in check_for:
                signal_strengths.append(cycle * register)
            if cycle in cycles_to_move_down:
                row += 1
                output += "\n"
            # start second cycle
            cycle += 1
            add_length = 40 * row
            reg_range = [register -1 + add_length, register + add_length, register + 1 + add_length]
            if cycle-1 in reg_range:
                output += hash
            else:
                output += dot
            if cycle in check_for:
                signal_strengths.append(cycle * register)
            if cycle in cycles_to_move_down:
                row += 1
                output += "\n"
            register += int(value)
        


    print(sum(signal_strengths))
    print(output)


print("example should return 13140")
main(example_input)

print("real")
main(real_input)

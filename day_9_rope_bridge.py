from example_inputs.day_9 import example_input, example_input_2
from real_inputs.day_9 import real_input

def tail_needs_to_move(head_x, head_y, tail_x, tail_y) -> bool:
    distance_x = abs(head_x - tail_x)
    distance_y = abs(head_y - tail_y)

    if distance_x < 2 and distance_y < 2:
        return False
    
    return True
    

def get_tail_new_position(head_x, head_y, tail_x, tail_y) -> tuple[int, int]:
    final_x = tail_x
    final_y = tail_y

    if head_x > tail_x:
        final_x += 1
    
    if head_x < tail_x:
        final_x -= 1

    if head_y > tail_y:
        final_y += 1
    
    if head_y < tail_y:
        final_y -= 1

    return final_x, final_y


def main(movements: str, knots_count: int):
    mov_list = movements.split("\n")
    tail_has_been = set()

    knots = []

    for _ in range(0, knots_count):
        knots.append([0, 0])
    

    tail_has_been.add(f"{knots[-1][0]},{knots[-1][1]}")

    for action in mov_list:
        action_list = action.split(" ")
        direction = action_list[0]
        distance = action_list[1]

        if direction == "L":
            for _ in range(0, int(distance)):
                knots[0][0] -= 1
                # head_x -= 1
                for knot in range(0, knots_count-1):
                    head_x = knots[knot][0]
                    head_y = knots[knot][1]
                    tail_x = knots[knot + 1][0]
                    tail_y = knots[knot + 1][1]
                    
                    if tail_needs_to_move(head_x, head_y, tail_x, tail_y):
                        knots[knot + 1][0], knots[knot + 1][1] = get_tail_new_position(head_x, head_y, tail_x, tail_y)
                        tail_has_been.add(f"{knots[-1][0]},{knots[-1][1]}")
        
        if direction == "R":
            for _ in range(0, int(distance)):
                knots[0][0] += 1
                # head_x += 1
                for knot in range(0, knots_count-1):
                    head_x = knots[knot][0]
                    head_y = knots[knot][1]
                    tail_x = knots[knot + 1][0]
                    tail_y = knots[knot + 1][1]

                    if tail_needs_to_move(head_x, head_y, tail_x, tail_y):
                        knots[knot + 1][0], knots[knot + 1][1] = get_tail_new_position(head_x, head_y, tail_x, tail_y)
                        tail_has_been.add(f"{knots[-1][0]},{knots[-1][1]}")
        
        if direction == "U":
            for _ in range(0, int(distance)):
                knots[0][1] += 1
                # head_y += 1
                for knot in range(0, knots_count-1):
                    head_x = knots[knot][0]
                    head_y = knots[knot][1]
                    tail_x = knots[knot + 1][0]
                    tail_y = knots[knot + 1][1]
                    
                    if tail_needs_to_move(head_x, head_y, tail_x, tail_y):
                        knots[knot + 1][0], knots[knot + 1][1] = get_tail_new_position(head_x, head_y, tail_x, tail_y)
                        tail_has_been.add(f"{knots[-1][0]},{knots[-1][1]}")
        
        if direction == "D":
            for _ in range(0, int(distance)):
                knots[0][1] -= 1
                # head_y -= 1
                for knot in range(0, knots_count-1):
                    head_x = knots[knot][0]
                    head_y = knots[knot][1]
                    tail_x = knots[knot + 1][0]
                    tail_y = knots[knot + 1][1]
                    
                    if tail_needs_to_move(head_x, head_y, tail_x, tail_y):
                        knots[knot + 1][0], knots[knot + 1][1] = get_tail_new_position(head_x, head_y, tail_x, tail_y)
                        tail_has_been.add(f"{knots[-1][0]},{knots[-1][1]}")
        

    print(len(tail_has_been))



print("example should return 13")
main(example_input, 2)

print("example 2 should return 36")
main(example_input_2, 10)

print("real: 6357")
main(real_input, 2)

print("real but with 10 knots")
main(real_input, 10)
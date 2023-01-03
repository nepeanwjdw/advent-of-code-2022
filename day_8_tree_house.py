from example_inputs.day_8 import example_input
from real_inputs.day_8 import real_input

def is_outside_tree(x_axis: int, y_axis: int, row_len: int, col_len: int) -> bool:
    if x_axis == 0 or y_axis == 0 or x_axis == row_len-1 or y_axis == col_len-1:
        return True
    return False

def is_visible_left(x_index: int, tree_height: int, tree_row: str) -> bool:
    next_tree_index = x_index - 1
    while next_tree_index >= 0:
        if int(tree_row[next_tree_index]) >= tree_height:
            return False
        else:
            next_tree_index -= 1
    return True


def is_visible_right(x_index: int, tree_height: int, tree_row: str, row_len: int) -> bool:
    next_tree_index = x_index + 1
    while next_tree_index < row_len:
        if int(tree_row[next_tree_index]) >= tree_height:
            return False
        else:
            next_tree_index += 1
    return True

def is_visible_up(
    x_index: int,
    y_index: int,
    trees_long_str: str,
    row_len: int,
) -> bool:
    original_position = row_len * y_index + x_index
    position = original_position - row_len
    while position >= 0:
        if trees_long_str[position] >= trees_long_str[original_position]:
            return False
        else:
            position -= row_len
    
    return True

def is_visible_down(
    x_index: int,
    y_index: int,
    trees_long_str: str,
    row_len: int,
    # total_trees_count: int,
) -> bool:
    original_position = row_len * y_index + x_index
    position = original_position + row_len
    while position < len(trees_long_str):
        if trees_long_str[position] >= trees_long_str[original_position]:
            return False
        else:
            position += row_len
    
    return True

def calculate_scenic_score(
    x_index: int,
    y_index: int,
    trees_long_str: str,
    tree_height: int,
    tree_row: str,
    row_len: int
):
    left = count_trees_visible_to_left(x_index, tree_height, tree_row)
    right = count_trees_visible_to_right(x_index, tree_height, tree_row)
    up = count_trees_visible_up(x_index, y_index, trees_long_str, tree_height, row_len)
    down = count_trees_visible_down(x_index, y_index, trees_long_str, tree_height, row_len)
    return left * right * up * down

def count_trees_visible_to_left(x_index: int, tree_height: int, tree_row: str) -> int:
    next_tree_index = x_index - 1
    trees_visible = 0
    while next_tree_index >= 0:
        trees_visible += 1
        next_tree_height = int(tree_row[next_tree_index])
        next_tree_index -= 1
        if next_tree_height >= tree_height:
            break

    return trees_visible

def count_trees_visible_to_right(x_index: int, tree_height: int, tree_row: str) -> int:
    next_tree_index = x_index + 1
    trees_visible = 0
    while next_tree_index < len(tree_row):
        trees_visible += 1
        next_tree_height = int(tree_row[next_tree_index])
        next_tree_index += 1
        if next_tree_height >= tree_height:
            break

    return trees_visible
    
def count_trees_visible_up(x_index: int, y_index: int, trees_long_str: str, tree_height: int, row_len: int) -> int:
    original_position = row_len * y_index + x_index
    position = original_position - row_len
    trees_visible = 0
    while position >= 0:
        trees_visible += 1
        next_tree_height = int(trees_long_str[position])
        position -= row_len
        if next_tree_height >= tree_height:
            break

    return trees_visible

def count_trees_visible_down(x_index: int, y_index: int, trees_long_str: str, tree_height: int, row_len: int) -> int:
    original_position = row_len * y_index + x_index
    position = original_position + row_len
    trees_visible = 0
    while position < len(trees_long_str):
        trees_visible += 1
        next_tree_height = int(trees_long_str[position])
        position += row_len
        if next_tree_height >= tree_height:
            break

    return trees_visible

def main(trees: str):
    trees_list = trees.split("\n")
    trees_long_str = "".join(trees_list)
    row_len = len(trees_list[0])
    col_len = len(trees_list)
    visible_tree_count = 0

    

    for y_index, tree_row in enumerate(trees_list):
        for x_index, tree in enumerate(tree_row):
            if (
                is_outside_tree(x_index, y_index, row_len, col_len) or
                is_visible_left(x_index, int(tree), tree_row) or
                is_visible_right(x_index, int(tree), tree_row, row_len) or
                is_visible_up(x_index, y_index, trees_long_str, row_len) or
                is_visible_down(x_index, y_index, trees_long_str, row_len)
            ):
                visible_tree_count += 1
    
    print(f"visible trees {visible_tree_count}")

    highest_scenic_score = 0

    for y_index, tree_row in enumerate(trees_list):
        for x_index, tree in enumerate(tree_row):
            score = calculate_scenic_score(x_index, y_index, trees_long_str, int(tree), tree_row, row_len)
            if score > highest_scenic_score:
                highest_scenic_score = score

    print(f"highest scenic score: {highest_scenic_score}")

print("example")
main(example_input)
print("real")
main(real_input)

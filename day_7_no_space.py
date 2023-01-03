from real_inputs.day_7 import real_input
from example_inputs.day_7 import example_input
import re

TOTAL_DISK_SPACE = 70_000_000
REQUIRED_UNUSED_SPACE = 30_000_000

def get_current_path(path_list: list[str]) -> str:
    return path_list[0] + "/".join(path_list[1:])

def determine_new_path(path_list: list[str], new_dir) -> str:
    path = get_current_path(path_list)
    if path[-1] == "/":
        return path + new_dir
    else:
        return path + "/" + new_dir

def main(lines: str):
    current_path_list = []
    all_dirs = set("/")
    filesystem = {"/": {"size": 0}}
    lines_list = lines.split("\n")
    for line in lines_list:
        numbers = re.findall(r"\d+", line)
        if numbers:
            current_path = get_current_path(current_path_list)
            for dir in all_dirs:
                if current_path.startswith(dir):
                    filesystem[dir]["size"] += int(numbers[0])
        elif re.search(r"\$ cd ", line):
            line_list = line.split(" ")
            cd_arg = line_list[2]
            if cd_arg == "..":
                del current_path_list[-1]
            else:
                if cd_arg == "/":
                    current_path_list = ["/"]
                else:
                    new_path = determine_new_path(current_path_list, cd_arg)
                    current_path_list.append(cd_arg)
                    all_dirs.add(new_path)
                    filesystem[new_path] = {"size": 0}

    
    sum_dirs = 0
    for dir in all_dirs:
        size = filesystem[dir]["size"]
        if size < 100_000:
            sum_dirs += size
    
    print(sum_dirs)

    free_space = TOTAL_DISK_SPACE - filesystem["/"]["size"]
    still_need_to_delete = REQUIRED_UNUSED_SPACE - free_space
    print(f"still need: {still_need_to_delete}")

    size_of_directory_to_delete = TOTAL_DISK_SPACE
    
    for dir in all_dirs:
        size = filesystem[dir]["size"]
        if size > still_need_to_delete and size < size_of_directory_to_delete:
            print(f"changing minimum size needed to delete to: {size}")
            size_of_directory_to_delete = size
    
    print(f"answer: {size_of_directory_to_delete}")

print("should be 95437")
main(example_input)
main(real_input)

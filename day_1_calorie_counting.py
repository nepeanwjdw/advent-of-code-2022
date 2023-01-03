from real_inputs.day_1 import real_input

def get_most_calories_from_elves(calories: str):
    calories_list = calories.split("\n")
    elves_with_sum_calories = []
    elf_counter = 0
    for calories in calories_list:
        if calories:
            if len(elves_with_sum_calories) == elf_counter:
                elves_with_sum_calories.append(int(calories))
            else:
                elves_with_sum_calories[elf_counter] = elves_with_sum_calories[elf_counter] + int(calories)
        else:
            elf_counter += 1
    


    return max(elves_with_sum_calories)


def get_three_most_calories_from_elves(calories: str):
    calories_list = calories.split("\n")
    elves_with_sum_calories = []
    elf_counter = 0
    for calories in calories_list:
        if calories:
            if len(elves_with_sum_calories) == elf_counter:
                elves_with_sum_calories.append(int(calories))
            else:
                elves_with_sum_calories[elf_counter] = elves_with_sum_calories[elf_counter] + int(calories)
        else:
            elf_counter += 1
    
    first_max = max(elves_with_sum_calories)
    final_calories = first_max
    elves_with_sum_calories.remove(first_max)
    
    second_max = max(elves_with_sum_calories)
    final_calories = final_calories + second_max
    elves_with_sum_calories.remove(second_max)
    
    third_max = max(elves_with_sum_calories)
    final_calories = final_calories + third_max

    return final_calories


print(get_most_calories_from_elves(real_input))
print(get_three_most_calories_from_elves(real_input))

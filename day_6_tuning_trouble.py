from real_inputs.day_6 import real_input
from example_inputs.day_6 import example_input_1, example_input_2, example_input_3, example_input_4, example_input_5

def check_chars_unique(chars: str) -> bool:
    return len(chars) == len(set(chars))

def main(signal: str, length_of_unique_chars: int):
    iterator = 0
    while not check_chars_unique(signal[iterator:iterator+length_of_unique_chars]):
        iterator += 1

    print(iterator+length_of_unique_chars)




print("should be 7")
main(example_input_1, 4)
print("should be 5")
main(example_input_2, 4)
print("should be 6")
main(example_input_3, 4)
print("should be 10")
main(example_input_4, 4)
print("should be 11")
main(example_input_5, 4)

print("real input")
main(real_input, 14)

print("should be 19")
main("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14)
print("should be 23")
main("bvwbjplbgvbhsrlpgdmjqwftvncz", 14)
print("should be 23")
main("nppdvjthqldpwncqszvftbrmjlhg", 14)
print("should be 29")
main("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14)
print("should be 26")
main("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14)

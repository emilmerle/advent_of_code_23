import re

# idea:
# find all numbers that are adjacent to a gear
# then store gear indices in a dict with the adjacent numbers
# finally calculate the gear ratios and add them up

filename = "./../input_data"
regex_number_pattern = "([0-9]+)"
gear_index_list = []


def main():
    gear_index_dict = {}
    with open(filename, "r") as f:
        line_counter = 0
        # find all indices of gears ("*")
        for line in f:
            gear_index_list.append(find_indices_of_gears(line))
        f.seek(0)

        for line in f:
            numbers = re.finditer(regex_number_pattern, line)
            for item in numbers:
                indices_to_be_searched = indices_to_search(
                    item.start(), item.end(), line_counter
                )
                # find the index of the gear and add it with the number to the dict
                position_of_gear = find_position_of_gear(indices_to_be_searched)
                if position_of_gear != (-1, -1):
                    if position_of_gear in gear_index_dict:
                        gear_index_dict[position_of_gear].append(item.group())
                    else:
                        gear_index_dict[position_of_gear] = [item.group()]
            line_counter += 1

        gear_index_dict = clean_gear_index_dict(gear_index_dict)
        final_sum = calculate_gear_ratio_sum(gear_index_dict)

        print(f"The final sum is {final_sum}.")


def find_indices_of_gears(line: str) -> list:
    return [index for index, symbol in enumerate(line) if symbol == "*"]


def indices_to_search(start: int, end: int, line: int) -> list:
    index_list = []
    for row in range(line - 1, line + 2):
        for index in range(start - 1, end + 1):
            if -1 < row < 140 and -1 < index < 140:
                index_list.append((row, index))
    return index_list


def find_position_of_gear(indices_to_search: tuple) -> tuple:
    for index in indices_to_search:
        if index[1] in gear_index_list[index[0]]:
            return index
    return (-1, -1)


# remove all gear with only one number adjacent
def clean_gear_index_dict(gear_dict: dict) -> dict:
    for gear, numbers in list(gear_dict.items()):
        if len(numbers) < 2:
            del gear_dict[gear]
    return gear_dict


def calculate_gear_ratio_sum(gear_index_dict: dict) -> int:
    sum = 0
    for gear, numbers in gear_index_dict.items():
        gear_ratio = int(numbers[0]) * int(numbers[1])
        sum += gear_ratio
    return sum


if __name__ == "__main__":
    main()

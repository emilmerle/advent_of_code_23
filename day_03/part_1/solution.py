import re


# numbers that are adjacent to a symbol count towards the sum
# for row r with number on indices i to j:
# [r-1][i-1] to [r-1][j+1]
# [r][i-1] and [r][j+1]
# [r+1][i-1] to [r+1][j+1]

# "matrix" is 140*140
# no symbols on first and last line
# no symbols at first and last index

# first idea:
# loop through every line and number and search the adjacent indices for a symbol

# second idea:
# loop through lines and note only the indices of symbols
# loop again and check for every number
# -> less memory needed but two loops

filename = "./../input_data"
# only numbers, "." and the newline character do not count as symbols, all other are symbols here
NO_SYMBOLS = "1234567890.\n"
regex_pattern = "([0-9]+)"
symbol_index_list = []


def main():
    with open(filename, "r") as f:
        line_counter = 0
        sum = 0
        for line in f:
            symbol_index_list.append(find_indices_of_symbols(line))
        f.seek(0)

        for line in f:
            numbers = re.finditer(regex_pattern, line)
            for item in numbers:
                indices_to_be_searched = indices_to_search(
                    item.start(), item.end(), line_counter
                )
                valid_number = number_adjacent_to_symbol(indices_to_be_searched)
                if valid_number:
                    sum += int(item.group())
            line_counter += 1

        print(f"The final sum is {sum}.")


def find_indices_of_symbols(line: str) -> list:
    return [index for index, symbol in enumerate(line) if symbol not in NO_SYMBOLS]


def indices_to_search(start: int, end: int, line: int) -> list:
    index_list = []
    for row in range(line - 1, line + 2):
        for index in range(start - 1, end + 1):
            if -1 < row < 140 and -1 < index < 140:
                index_list.append((row, index))
    return index_list


def number_adjacent_to_symbol(indices_to_search: tuple) -> bool:
    for index in indices_to_search:
        if index[1] in symbol_index_list[index[0]]:
            return True
    return False


if __name__ == "__main__":
    main()

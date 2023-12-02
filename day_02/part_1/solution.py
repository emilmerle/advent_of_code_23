import re

# Configuration:
# 12 red cubes, 13 green cubes, 14 blue cubes
MAX_CUBES_DICT = {
    "red": 12,
    "green": 13,
    "blue": 14
}

game_id_regex_pattern = "(Game [0-9]+)"
sets_regex_pattern = r"(?=[;:]+ (.+?)[;\n])"

filename = "./input_data"

def main():
    with open(filename, "r") as f:
        sum = 0
        for line in f:
            line_game_id = get_game_id(line)
            sets = get_sets(line)
            possible_game = is_game_possible(sets)
            print(f"Game {line_game_id} is {'possible!' if possible_game else 'not possible!'}")

            if possible_game:
                sum += line_game_id

    print(f"The total sum of the possible games is {sum}.")
    return


def get_game_id(line: str) -> int:
    return int(re.search(game_id_regex_pattern, line)[0][5:])

def get_sets(line: str) -> str:
    return re.findall(sets_regex_pattern, line)

def is_game_possible(sets: list) -> bool:
    possible_game = True
    for set in sets:
        cube_list = strToList(set)
        # writing the cubes into a dict to directly compare to the MAX_CUBES_DICT
        cubes_dict = {x.split()[1]: int(x.split()[0]) for x in cube_list}
        for cube in cubes_dict:
            if cubes_dict[cube] > MAX_CUBES_DICT[cube]:
                possible_game = False
    return possible_game
        
        
def strToList(cubes: str) -> list:
    return [x.strip() for x in cubes.split(",")]

if __name__ == "__main__":
    main()
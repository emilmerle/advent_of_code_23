import re


game_id_regex_pattern = "(Game [0-9]+)"
sets_regex_pattern = r"(?=[;:]+ (.+?)[;\n])"

filename = "./input_data"

def main():
    with open(filename, "r") as f:
        sum = 0
        for line in f:
            sets = find_sets(line)
            max_cubes_dict = max_cubes_for_set(sets)
            # power of the sets equals to red*green*blue
            power_of_sets = 1
            for cube in max_cubes_dict:
                power_of_sets *= max_cubes_dict[cube]
            sum += power_of_sets

    print(f"The total sum of the power of the sets is {sum}.")
    return

def find_sets(line: str) -> list:
    return re.findall(sets_regex_pattern, line)

def strToList(cubes: str) -> list:
    return [x.strip() for x in cubes.split(",")]

def max_cubes_for_set(sets: str) -> dict:
    max_cubes_dict_for_set = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for cubes_string in sets:
        cubes_list = strToList(cubes_string)
        # turn every set into a dict with dict comprehension 
        cubes_dict = {x.split()[1]: int(x.split()[0]) for x in cubes_list}
        # write highest number of every color into the max_cubes_dict_for_set dict:
        # this equals to the minimum number of cubes needed for this game to be possible
        for cube in cubes_dict:
            if cubes_dict[cube] > max_cubes_dict_for_set[cube]:
                max_cubes_dict_for_set[cube] = cubes_dict[cube]
    return max_cubes_dict_for_set

if __name__ == "__main__":
    main()

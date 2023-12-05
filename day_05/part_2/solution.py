filename = "./../input_data"

# now the list of seeds describe ranges of seeds


# [5, 15]
# [10, 15] -> [20,25] [0,6] -> [40,46] 
# ==> [5,6] [7,9] [10,15] 
# ==> [45,46] [7,9] [20,25]

def main():
    map_dict = {}
    with open(filename, "r") as f:
        seed_ranges = get_seeds(f.readline())
        # print(seed_ranges)
        map_order = []

        for line in f:
            line_list = line.split()
            if len(line_list) < 2:
                continue
            elif len(line_list) == 2:
                # maps into dict
                map_dict[line_list[0]] = {}
                map_order.append(line_list[0])
                continue
            elif len(line_list) == 3:
                # source interval with distance for shifting into dict
                destination_range = (
                    int(line_list[0]),
                    int(line_list[0]) + int(line_list[2]) - 1,
                )
                source_range = (
                    int(line_list[1]),
                    int(line_list[1]) + int(line_list[2]) - 1,
                )
                shift_distance = get_distance_for_shifting(source_range, destination_range)
                map_dict[map_order[-1]][source_range] = shift_distance
                continue
            else:
                exit("Edge Case found!!!")
        # print(map_dict)
        # print(combine_two_intervals_and_shift((5,15), (10,20), 7))

        current_seeds = seed_ranges
        for map in map_order:
            print(map)
            temp_values = []
            print(len(current_seeds))
            for seed in current_seeds:
                for interval in map_dict[map]:
                    # print(interval)
                    # print(map, seed, interval)
                    temp_values += [x for x in combine_two_intervals_and_shift(seed, interval, map_dict[map][interval]) if x not in temp_values]
                    # print(temp_values)
            current_seeds = temp_values
        
        print(current_seeds)
        print(min([min(x[0], x[1]) for x in current_seeds]))
        return 

            


        # print(f"The lowest location number is {min(final_values)}.")

def get_distance_for_shifting(source: tuple, destination: tuple) -> int:
    return destination[0] - source[0]

def remap_interval(interval: tuple, shift_value: int):
    return (interval[0] + shift_value, interval[1] + shift_value)

def combine_two_intervals_and_shift(first: tuple, second: tuple, shifting_distance: int) -> list:
# case 1: no overlapping tuple
# case 2: overlap on "left" side of second tuple
# case 3: overlap on "right" side of second tuple
# case 4: first interval overlaps second completely -> this should cover the case when intervals match
# case 5: first interval completely in second interval

    # case 1
    if first[1] < second[0] or first[0] > second[1]:
        return [first] # this tuple can stay as it is

    # case 2
    elif first[0] < second[0] and (first[1] >= second[0] or first[1] <= second[1]) :
        left_tuple = (first[0], second[0] - 1) # left tuple can stay as it is
        right_tuple = (second[0] + shifting_distance, first[1] + shifting_distance) # right tuple has to be mapped
        return [left_tuple, right_tuple]
    # case 3:
    elif first[0] >= second[0] and (first[0] <= second[1] or first[1] > second[1]):
        left_tuple = (first[0] + shifting_distance, second[1] + shifting_distance) # left tuple has to be mapped
        right_tuple = (second[1] + 1, first[1]) # right tuple can stay as it is
        return [left_tuple, right_tuple]
    # case 4:
    elif first[0] <= second[0] and first[1] >= second[1]:
        left_tuple = (first[0], second[0] - 1) # left tuple can stay as it is
        middle_tuple = (second[0] + shifting_distance, second[1] + shifting_distance) # middle tuple has to be mapped
        right_tuple = (second[1] + 1, first[1]) # right tuple can stay as it is
        return [left_tuple, middle_tuple, right_tuple]
    
    # case 5:
    elif first[0] > second[0] and first[1] < second[1]:
        return [(first[0] + shifting_distance, first[1] + shifting_distance)] # this has to be mapped
    else:
        print(first, second, shifting_distance)
        exit("ERROR!")
    return

def get_seeds(seed_line: str) -> list:
    seed_list = seed_line[7:].split()
    seed_ranges = []
    for x in range(len(seed_list) // 2):
        range_tuple = (int(seed_list[2*x]), int(seed_list[2*x]) + int(seed_list[2*x+1]) - 1)
        seed_ranges.append(range_tuple)
    return seed_ranges


if __name__ == "__main__":
    main()

filename = "./../test_input_data"

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
        
        current_values = seed_ranges
        for map in map_order:
            print(f"MAP {map} STARTING")
            next_values = []
            print("Starting with:", current_values)
            print("Map values:", map_dict[map])
            for tuple in current_values:
                tuple_altered = False
                # Mistake found: If one interval has to be mapped multiple times, too many intervals are returned
                # TODO: fix
                for map_value in map_dict[map]:
                    all_tuples = combine_two_intervals_and_shift(tuple, map_value, map_dict[map][map_value])
                    if all_tuples != [tuple]:
                        # print(tuple, all_tuples)
                        tuple_altered = True
                    next_values += [x for x in all_tuples if x not in next_values]
                # print("Before:", next_values)
                # Mistake found: Remove original interval if the interval was combined at some time
                if tuple in next_values and tuple_altered:
                    next_values.pop(next_values.index(tuple))
                # print("After:", next_values)

                current_values = next_values

        lowest_location = min([min(x) for x in current_values])
        print(f"The lowest location number is {lowest_location}.")

        # test_combine()
        
        return 

            


        # print(f"The lowest location number is {min(final_values)}.")

def test_combine():
    x = 3
    test_intervals = [
        ((5,24), (25,30), x), # (5,24)
        ((11,30), (5,10), x), # (11,30)

        ((5,15), (10,20), x), # (5,9) (13,18)
        ((5,15), (15,20), x), # (5,14) (18,18)

        ((10, 20), (5,15), x), # (13,18), (16,20)
        ((15, 20), (10,15), x), # (18,18) (16,20)

        ((5, 25), (10,15), x), # (5,9) (13,18) (16,25)
        ((5,15), (10,15), x), # (5,9) (13,18)
        ((10,20), (10,15), x), # (13,18) (16,20)

        ((10,15), (5,20), x), # (13, 18)
        ((10,15), (10,15), x), # (13,18)
        ((10,15), (10,20), x), # (13,18)
        ((10,15), (5,15), x) # (13,18)
    ]

    for triple in test_intervals:
        print(combine_two_intervals_and_shift(triple[0], triple[1], triple[2]))

def get_distance_for_shifting(source: tuple, destination: tuple) -> int:
    return destination[0] - source[0]

def remap_interval(interval: tuple, shift_value: int):
    return (interval[0] + shift_value, interval[1] + shift_value)

def combine_two_intervals_and_shift(first: tuple, second: tuple, shifting_distance: int) -> list:
# case 1: no overlapping tuple
# case 2: overlap on "left" side of second tuple
# case 3: overlap on "right" side of second tuple
# case 4: first interval overlaps second completely 
# case 5: first interval completely in second interval -> this should cover the case when intervals match

# Mistake found: case 5 didnt cover the case when the start or end of the intervals matches

    START = 0
    END = 1
    # case 1
    # Mistake found: first[END] was first[START]
    if first[END] < second[START] or first[START] > second[END]:
        return [first] # this tuple can stay as it is

    # 
    elif first[START] < second[START] and first[END] >= second[START] and first[END] <= second[END] :
        left_tuple = (first[START], second[START] - END) # left tuple can stay as it is
        right_tuple = (second[START] + shifting_distance, first[END] + shifting_distance) # right tuple has to be mapped
        return [left_tuple, right_tuple]
    # case 3:
    elif first[START] >= second[START] and first[START] <= second[END] and first[END] > second[END]:
        left_tuple = (first[START] + shifting_distance, second[END] + shifting_distance) # left tuple has to be mapped
        right_tuple = (second[END] + 1, first[END]) # right tuple can stay as it is
        return [left_tuple, right_tuple]
    # case 4:
    elif (first[START] < second[START] and first[END] >= second[END]) or (first[START] <= second[START] and first[END] > second[END]):
        left_tuple = (first[START], second[START] - END) # left tuple can stay as it is
        middle_tuple = (second[START] + shifting_distance, second[END] + shifting_distance) # middle tuple has to be mapped
        right_tuple = (second[END] + 1, first[END]) # right tuple can stay as it is
        return [left_tuple, middle_tuple, right_tuple]
    
    # case 5:
    elif first[START] >= second[START] and first[END] <= second[END]:
        return [(first[START] + shifting_distance, first[END] + shifting_distance)] # this has to be mapped
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

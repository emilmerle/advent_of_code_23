START = 0
END = 1

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
        not_calculated = seed_ranges
        for map in map_order:
            print("Starting Map:", map)
            print("With values:", not_calculated)
            fertige_tuple = []
            counter = 0
            while len(not_calculated) > 1:
                print(not_calculated)
                tuple = not_calculated.pop(0) # erstes tuple poppen
                # für jedes Tuple in der map tabelle die destination tuples ausrechnen
                for map_tuple in map_dict[map]:
                    shifting_distance = map_dict[map][map_tuple]
                    fertiges, todo_tuple = combine_two_intervals_and_shift(tuple, map_tuple, shifting_distance) # die map tuple dafür ausrechnen
                    fertige_tuple += [x for x in fertiges if x not in fertige_tuple] # die fertigen in fertig liste
                    not_calculated += [x for x in todo_tuple if x not in not_calculated] # die weiteren in not_calculated_wieder
                    counter += 1
            not_calculated = fertige_tuple

        print(not_calculated)
        # print(other_combine_and_shift((10,20), (15,25)))
        
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

def shift_interval(interval: tuple, shift_value: int):
    return (interval[0] + shift_value, interval[1] + shift_value)

def other_combine_and_shift(first: tuple, second: tuple):
    before = (first[START], min(first[END], second[START]-1))
    inter = (max(first[START], second[START]), min(second[END], first[END]))
    after = (max(second[END], first[START]), first[END])
    return before, inter, after

def combine_two_intervals_and_shift(first: tuple, second: tuple, shifting_distance: int):
# case 1: no overlapping tuple
# case 2: overlap on "left" side of second tuple
# case 3: overlap on "right" side of second tuple
# case 4: first interval overlaps second completely 
# case 5: first interval completely in second interval -> this should cover the case when intervals match

# Mistake found: case 5 didnt cover the case when the start or end of the intervals matches

    START = 0
    END = 1
    muss_nochmal = []
    wurde_schon = []
    # case 1
    # Mistake found: first[END] was first[START]
    if first[END] < second[START] or first[START] > second[END]:
        muss_nochmal.append(first) # this tuple can stay as it is

    # 
    elif first[START] < second[START] and first[END] >= second[START] and first[END] <= second[END] :
        left_tuple = (first[START], second[START] - END) # left tuple can stay as it is
        right_tuple = (second[START] + shifting_distance, first[END] + shifting_distance) # right tuple has to be mapped
        muss_nochmal.append(left_tuple)
        wurde_schon.append(right_tuple)
    # case 3:
    elif first[START] >= second[START] and first[START] <= second[END] and first[END] > second[END]:
        left_tuple = (first[START] + shifting_distance, second[END] + shifting_distance) # left tuple has to be mapped
        right_tuple = (second[END] + 1, first[END]) # right tuple can stay as it is
        wurde_schon.append(left_tuple)
        muss_nochmal.append(right_tuple)
    # case 4:
    elif (first[START] < second[START] and first[END] >= second[END]) or (first[START] <= second[START] and first[END] > second[END]):
        left_tuple = (first[START], second[START] - END) # left tuple can stay as it is
        middle_tuple = (second[START] + shifting_distance, second[END] + shifting_distance) # middle tuple has to be mapped
        right_tuple = (second[END] + 1, first[END]) # right tuple can stay as it is
        wurde_schon.append(middle_tuple)
        muss_nochmal.append(left_tuple, right_tuple)
    
    # case 5:
    elif first[START] >= second[START] and first[END] <= second[END]:
        wurde_schon.append([(first[START] + shifting_distance, first[END] + shifting_distance)]) # this has to be mapped
    else:
        print(first, second, shifting_distance)
        exit("ERROR!")
    return wurde_schon, muss_nochmal

def get_seeds(seed_line: str) -> list:
    seed_list = seed_line[7:].split()
    seed_ranges = []
    for x in range(len(seed_list) // 2):
        range_tuple = (int(seed_list[2*x]), int(seed_list[2*x]) + int(seed_list[2*x+1]) - 1)
        seed_ranges.append(range_tuple)
    return seed_ranges


if __name__ == "__main__":
    main()

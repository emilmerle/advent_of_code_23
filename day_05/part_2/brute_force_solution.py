import sys


filename = "./../input_data"


def main():
    map_dict = {}
    with open(filename, "r") as f:
        seed_ranges = get_seeds(f.readline())
        print(seed_ranges)
        map_order = []

        for line in f:
            line_list = line.split()
            if len(line_list) < 2:
                continue
            elif len(line_list) == 2:
                # map into dict
                map_dict[line_list[0]] = []
                map_order.append(line_list[0])
                continue
            elif len(line_list) == 3:
                # ranges into map in dict
                shifting_distance = int(line_list[0]) - int(line_list[1])
                source_range = (
                    int(line_list[1]),
                    int(line_list[1]) + int(line_list[2]) - 1,
                )
                map_dict[map_order[-1]].append((source_range, shifting_distance))
                continue
            else:
                exit("Edge Case found!!!")

        
        # für jede Seed range:
        #       für jeden Seed
        #           currentvalue = seed
        #           für jede Map:
        #               für jede range in der map:
        #                   ist der currentvalue in der range:
        #                       ja: currentvalue mappen und nächste map

        lowest_location = sys.maxsize
        for seed_range in seed_ranges:
            print("Starting input seed range:", seed_range)
            for seed in range(seed_range[0], seed_range[1]):
                current_value = seed
                print("Current value:", current_value)
                for map in map_order:
                    for single_range in map_dict[map]:
                        if single_range[0][0] <= current_value < single_range[0][1]:
                            current_value = current_value + single_range[1]
                            break
                        
                if current_value < lowest_location:
                    lowest_location = current_value
            print("Current lowest location:", lowest_location)
        
        print("Lowest location:", lowest_location)

        """ for seed in seeds:
            # print(seed)
            current_value = seed
            for map in map_order:
                counter = 0
                for single_range in map_dict[map]["source_ranges"]:
                    if single_range[0] <= current_value <= single_range[1]:
                        distance = current_value - single_range[0]
                        current_value = (
                            map_dict[map]["destination_ranges"][counter][0] + distance
                        )
                        # Mistake found: did not break but continue loop first
                        break
                    else:
                        current_value = current_value
                    counter += 1
            final_values.append(current_value) """

        # print(f"The lowest location number is {min(final_values)}.")


def get_seeds(seed_line: str) -> list:
    seed_list = seed_line[7:].split()
    seed_ranges = []
    for x in range(len(seed_list) // 2):
        range_tuple = (
            int(seed_list[2 * x]),
            int(seed_list[2 * x]) + int(seed_list[2 * x + 1]),
        )
        seed_ranges.append(range_tuple)
    return seed_ranges


if __name__ == "__main__":
    main()

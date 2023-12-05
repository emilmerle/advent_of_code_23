filename = "./../input_data"


def main():
    map_dict = {}
    with open(filename, "r") as f:
        seeds = get_seeds(f.readline())
        map_order = []

        for line in f:
            line_list = line.split()
            if len(line_list) < 2:
                continue
            elif len(line_list) == 2:
                # map into dict
                map_dict[line_list[0]] = {"source_ranges": [], "destination_ranges": []}
                map_order.append(line_list[0])
                continue
            elif len(line_list) == 3:
                # ranges into map in dict
                destination_range = (
                    int(line_list[0]),
                    int(line_list[0]) + int(line_list[2]) - 1,
                )
                source_range = (
                    int(line_list[1]),
                    int(line_list[1]) + int(line_list[2]) - 1,
                )
                map_dict[map_order[-1]]["destination_ranges"].append(destination_range)
                map_dict[map_order[-1]]["source_ranges"].append(source_range)
                continue
            else:
                exit("Edge Case found!!!")

        final_values = []
        for seed in seeds:
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
            final_values.append(current_value)

        print(f"The lowest location number is {min(final_values)}.")


def get_seeds(seed_line: str) -> list:
    return [int(x) for x in seed_line[7:].split()]


if __name__ == "__main__":
    main()

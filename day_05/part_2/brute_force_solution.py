import sys


filename = "./../input_data"
START = 0
END = 1


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
                    int(line_list[0]) + int(line_list[2]),
                )
                source_range = (
                    int(line_list[1]),
                    int(line_list[1]) + int(line_list[2]),
                )
                shift_distance = get_distance_for_shifting(
                    source_range, destination_range
                )
                map_dict[map_order[-1]][source_range] = shift_distance
                continue
            else:
                exit("Edge Case found!!!")

        lowest_value = sys.maxsize
        for seed_range in seed_ranges:
            print("Starting seed range:", seed_range)
            for seed in range(seed_range[0], seed_range[1]):
                if seed % 10_000_000 == 0:
                    print("Seed:", seed)
                current_value = seed
                for map in map_order:
                    value_after_map = return_mapped_value(current_value, map_dict[map])
                    current_value = value_after_map
                if current_value < lowest_value:
                    lowest_value = current_value

        print(lowest_value)


def return_mapped_value(number: int, map_mapping_ranges: dict) -> int:
    for range, shifting_value in map_mapping_ranges.items():
        if number >= range[START] and number < range[END]:
            return number + shifting_value
    return number


def get_distance_for_shifting(source: tuple, destination: tuple) -> int:
    return destination[0] - source[0]


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

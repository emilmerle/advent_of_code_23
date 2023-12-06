# First idea:
# calculate for every possible way

filename = "./../input_data"


def main():
    with open(filename, "r") as f:
        times = [int(x) for x in f.readline().split()[1:]]
        distances = [int(x) for x in f.readline().split()[1:]]

        product_of_races_won = 1
        for race_number in range(len(times)):
            time = times[race_number]
            record_distance = distances[race_number]
            races_won = 0

            for timer in range(time + 1):
                button_time = timer
                moving_time = time - button_time

                travel_distance = calc_travel_distance(button_time, moving_time)
                if race_won(travel_distance, record_distance):
                    races_won += 1
            product_of_races_won *= races_won

        print(f"The product of the number to win the races is {product_of_races_won}.")


def race_won(travelled_distance: int, record_distance: int) -> bool:
    return travelled_distance > record_distance


def calc_travel_distance(button_time: int, moving_time: int) -> int:
    return button_time * moving_time


if __name__ == "__main__":
    main()

from math import floor

# First idea:
# dividing the record through the time gives an estimate on the "edges" of the times

filename = "./../input_data"


def main():
    with open(filename, "r") as f:
        time = int("".join(f.readline()[6:].split()))
        record_distance = int("".join(f.readline()[10:].split()))

        edge = floor(record_distance / time)

        while not calc_race(edge, time, record_distance):
            edge += 1

        last_game = time - edge
        number_of_races_won = last_game - edge + 1
        print(f"The race can be beaten in {number_of_races_won} ways.")


def calc_race(button_time: int, race_time: int, record_distance: int) -> bool:
    moving_time = race_time - button_time
    travel_distance = calc_travel_distance(button_time, moving_time)
    return race_won(travel_distance, record_distance)


def race_won(travelled_distance: int, record_distance: int) -> bool:
    return travelled_distance > record_distance


def calc_travel_distance(button_time: int, moving_time: int) -> int:
    return button_time * moving_time


if __name__ == "__main__":
    main()

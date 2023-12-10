filename = "./../input_data"


def main():
    with open(filename, "r") as f:
        maze = []
        starting_point = (-1, -1)
        line_counter = 0
        for line in f:
            if "S" in line:
                starting_point = (line_counter, line.index("S"))
            maze.append(line[:-1])
            line_counter += 1

        step_counter = 0
        current_position = get_starting_direction(starting_point, maze)
        previous_position = starting_point
        while current_position != starting_point or step_counter == 0:
            step_counter += 1
            temp_prev_pos = previous_position
            previous_position = current_position
            current_position = find_next_position(
                temp_prev_pos,
                current_position,
                maze[current_position[0]][current_position[1]],
            )

        print(
            f"The farthest point from the starting position is {(step_counter // 2) + 1} away."
        )

        # current_position = find_next_position()


def get_starting_direction(maze_position: tuple, maze: list) -> tuple:
    # not covering edge cases when starting position is on edge of maze
    if min(maze_position) != 0 and min(maze_position) != len(maze) - 1:
        if maze[maze_position[0]][maze_position[1] + 1] in ["-", "J", "7"]:  # right
            return (maze_position[0], maze_position[1] + 1)
        elif maze[maze_position[0] + 1][maze_position[1]] in ["|", "J", "L"]:  # bottom
            return (maze_position[0] + 1, maze_position[1])
        elif maze[maze_position[0]][maze_position[1] - 1] in ["-", "F", "L"]:  # left
            return (maze_position[0], maze_position[1] - 1)
        elif maze[maze_position[0] - 1][maze_position[1]] in ["|", "F", "7"]:  # top
            return (maze_position[0] - 1, maze_position[1])


def find_possible_positions(maze_position: tuple, symbol) -> list:
    match symbol:
        case "F":
            return [
                (maze_position[0], maze_position[1] + 1),
                (maze_position[0] + 1, maze_position[1]),
            ]
        case "7":
            return [
                (maze_position[0], maze_position[1] - 1),
                (maze_position[0] + 1, maze_position[1]),
            ]
        case "J":
            return [
                (maze_position[0] - 1, maze_position[1]),
                (maze_position[0], maze_position[1] - 1),
            ]
        case "L":
            return [
                (maze_position[0], maze_position[1] + 1),
                (maze_position[0] - 1, maze_position[1]),
            ]
        case "|":
            return [
                (maze_position[0] - 1, maze_position[1]),
                (maze_position[0] + 1, maze_position[1]),
            ]
        case "-":
            return [
                (maze_position[0], maze_position[1] - 1),
                (maze_position[0], maze_position[1] + 1),
            ]
        case default:
            exit("Impossible symbol found!!!")


def find_next_position(
    previous_position: tuple, maze_position: tuple, symbol: str
) -> tuple:
    next_positions = find_possible_positions(maze_position, symbol)
    next_positions.remove(previous_position)
    return next_positions[0]


if __name__ == "__main__":
    main()

filename = "./../input_data"


def main():
    with open(filename, "r") as f:
        instructions = f.readline()[:-1]

        node_dict = {}
        for line in f:
            if line == "\n":
                continue
            node = line[:3]
            places_to_go = (line[7:10], line[12:15])
            node_dict[node] = places_to_go

        current_node = "AAA"
        end_node = "ZZZ"
        steps = 0
        original_instructions = instructions
        while current_node != end_node:
            steps += 1
            if not len(instructions):
                instructions = original_instructions
            instruction = instructions[0]
            instructions = instructions[1:]
            if instruction == "L":
                current_node = node_dict[current_node][0]
            elif instruction == "R":
                current_node = node_dict[current_node][1]

        print(steps, "are required to get to ZZZ")


if __name__ == "__main__":
    main()

from math import lcm

filename = "./../input_data"


def main():
    with open(filename, "r") as f:
        instructions = f.readline()[:-1]

        node_dict = {}
        starting_nodes = []
        ending_nodes = []
        for line in f:
            if line == "\n":
                continue
            node = line[:3]
            places_to_go = (line[7:10], line[12:15])
            node_dict[node] = places_to_go
            if node[2] == "A":
                starting_nodes.append(node)
                continue
            if node[2] == "Z":
                ending_nodes.append(node)

        original_instructions = instructions
        step_list = []
        for start_node in starting_nodes:
            steps = 0
            instructions = original_instructions
            current_node = start_node
            while current_node not in ending_nodes:
                steps += 1
                if not len(instructions):
                    instructions = original_instructions
                instruction = instructions[0]
                instructions = instructions[1:]
                if instruction == "L":
                    current_node = node_dict[current_node][0]
                elif instruction == "R":
                    current_node = node_dict[current_node][1]
            step_list.append(steps)

        print(f"The number of steps to get to the end nodes is: {lcm(*step_list)}.")


if __name__ == "__main__":
    main()

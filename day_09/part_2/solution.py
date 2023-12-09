filename = "./../input_data"


def main():
    with open(filename, "r") as f:
        input_sequences = []
        for line in f:
            seq = [int(x) for x in line.split()]
            input_sequences.append(seq)

        final_sum = 0
        for sequence in input_sequences:
            next_value = analyze_sequence(sequence)
            final_sum += next_value

        print(f"The final sum of all next values is {final_sum}.")


def analyze_sequence(sequence: list):
    sequences = []
    current_sequence = sequence
    while len([x for x in current_sequence if x != 0]):
        next_sequence = []
        sequences.append(current_sequence)

        for index in range(1, len(current_sequence)):
            next_value = current_sequence[index] - current_sequence[index - 1]
            next_sequence.append(next_value)

        current_sequence = next_sequence

    for index in range(len(sequences) - 2, -1, -1):
        prev_value = sequences[index][0] - sequences[index+1][0]
        sequences[index].insert(0, prev_value)

    return sequences[0][0]


if __name__ == "__main__":
    main()

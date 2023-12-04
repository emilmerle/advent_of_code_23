# First Idea:
# Get numbers with regex

# Second idea:
# Also possible with pure python, string manipulation


# First 10 characters are Card identifiers, not needed here
# Then there are the winning number until a |
# last the card numbers

filename = "./../input_data"


def main():
    with open(filename, "r") as f:
        final_sum = 0
        for line in f:
            seperator_index = line.index("|")
            winning_numbers = [int(x) for x in line[10:seperator_index].split()]
            card_numbers = [int(x) for x in line[seperator_index + 2 :].split()]
            cards_won_counter = len(
                [True for card_number in card_numbers if card_number in winning_numbers]
            )
            card_worth = 2 ** (cards_won_counter - 1) if cards_won_counter > 0 else 0
            final_sum += card_worth

        print(f"The final sum is {final_sum}.")


if __name__ == "__main__":
    main()

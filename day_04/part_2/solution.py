# First Idea:
# Get numbers with regex

# Second idea:
# Also possible with pure python, string manipulation
# because the structure is well known for every line

# First 10 characters are Card identifiers, not needed here
# Then there are the winning number until a |
# last the card numbers

filename = "./../input_data"


def main():
    with open(filename, "r") as f:
        final_sum = 0
        line_counter = 1
        card_dict = {1: 1}
        for line in f:
            seperator_index = line.index("|")
            # the multiplier equals the times the card has been won
            multiplier = card_dict[line_counter] if line_counter in card_dict else 1
            winning_numbers = [int(x) for x in line[10:seperator_index].split()]
            card_numbers = [int(x) for x in line[seperator_index + 2 :].split()]
            # There may be an easier solution for the calculation of the number of cards won
            cards_won_counter = len(
                [True for card_number in card_numbers if card_number in winning_numbers]
            )
            cards_won = [line_counter + x for x in range(1, cards_won_counter + 1)]

            for won_card in cards_won:
                if won_card in card_dict:
                    card_dict[won_card] += multiplier
                else:
                    # Mistake corrected: did not consider original card
                    card_dict[won_card] = multiplier + 1
            # Mistake corrected: did not add cards to dict if they were never won
            if line_counter not in card_dict:
                card_dict[line_counter] = 1
            line_counter += 1

        final_sum = sum(card_dict.values())
        print(f"The final sum is {final_sum}.")


if __name__ == "__main__":
    main()

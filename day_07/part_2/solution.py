from functools import cmp_to_key

filename = "./../input_data"
order_list = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def main():
    with open(filename, "r") as f:
        hands_dict = {}
        value_dict = {
            7: [],
            6: [],
            5: [],
            4: [],
            3: [],
            2: [],
            1: [],
        }

        for line in f:
            hand, bid = line.split()[0], line.split()[1]
            remapped_hand = remap_joker_value(hand)
            hand_value = calculate_value_of_hand(remapped_hand)
            hands_dict[hand] = (int(bid), hand_value)
            if hand_value in value_dict:
                value_dict[hand_value].append(hand)

        full_sorted_hands = []
        for value in value_dict:
            value_dict[value] = sorted(
                value_dict[value], key=cmp_to_key(sorter), reverse=True
            )
            for hand in value_dict[value]:
                full_sorted_hands.append(hand)

        highest_multiplier = len(full_sorted_hands)
        final_sum = 0
        for hand in full_sorted_hands:
            final_sum += hands_dict[hand][0] * highest_multiplier
            highest_multiplier -= 1

        print(f"The total winnings of the games is {final_sum}.")


# Idea:
# Replace the Joker always with the symbol that is in the hand most often
def remap_joker_value(hand: str) -> str:
    if hand == "JJJJJ":
        return "AAAAA"
    if "J" in hand:
        symbols = []
        for symbol in set(hand):
            if symbol != "J":
                occurences = hand.count(symbol)
                symbols.append((symbol, occurences))
        return hand.replace("J", max(symbols, key=lambda x: x[1])[0])
    return hand


def calculate_value_of_hand(hand: str) -> int:
    # 7 cases: five + four + three + two of a kind + full house + two pairs + high card
    s = set(hand)
    match len(s):
        case 5:  # high card
            return 1
        case 4:  # one pair
            return 2
        case 3:  # three of a kind or two pairs
            for symbol in s:
                if hand.count(symbol) == 3:  # three of a kind
                    return 4
            return 3  # two pairs
        case 2:  # full house or four of a kind
            if 2 <= hand.count(hand[0]) <= 3:  # full house
                return 5
            else:  # four of a kind
                return 6
        case 1:  # five of a kind
            return 7
        case default:
            exit("IMPOSSIBLE HAND FOUND!!!")


def sorter(first_hand: str, second_hand: str):
    # every hand is 5 symbol long
    for index in range(5):
        if order_list.index(first_hand[index]) < order_list.index(second_hand[index]):
            return 1
        elif order_list.index(first_hand[index]) > order_list.index(second_hand[index]):
            return -1
    print("SAME HANDS DETECTED!")
    return 0


if __name__ == "__main__":
    main()

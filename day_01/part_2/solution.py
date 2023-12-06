import re
import sys


def main():
    # Tricky pattern: We also need to find overlapping cases:
    # for example: in "threeight" we should find "three" AND "eight"
    # The ?=... in the pattern assures overlapping words are found
    regex_pattern = "(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))"
    filename = "./../input_data_ole"

    with open(filename, "r") as f:
        sum = 0
        counter = 0
        matches = []
        for line in f:
            counter += 1
            line_sum = 0
            matches = re.findall(regex_pattern, line)
            if len(matches) == 0:
                sys.exit(f"No match in line {counter}")
            if len(matches) >= 2:
                # String concatenation also possible for two-digit-numbers but cast to int necessary later anyway:
                # line_sum = int(wordToDigitStr(matches[0]) + wordToDigitStr(matches[-1]))

                first_digit = strToInt(matches[0])
                second_digit = strToInt(matches[-1])
                line_sum = first_digit * 10 + second_digit
            else:
                digit = strToInt(matches[0])
                line_sum = digit * 11

            sum += line_sum

        print(f"{counter} lines read.")
        print(f"Final sum is: {sum}")


def strToInt(digit: str) -> int:
    if digit.isnumeric():
        return int(digit)
    else:
        return wordToInt(digit)


def wordToInt(digit: str) -> int:
    match digit:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case other:
            sys.exit("Unknown case found while converting words to digits.")


def wordToDigitStr(word: str) -> str:
    if word.isnumeric():
        return word
    else:
        match word:
            case "one":
                return "1"
            case "two":
                return "2"
            case "three":
                return "3"
            case "four":
                return "4"
            case "five":
                return "5"
            case "six":
                return "6"
            case "seven":
                return "7"
            case "eight":
                return "8"
            case "nine":
                return "9"
            case other:
                sys.exit("Unknown case found while converting words to digits.")


if __name__ == "__main__":
    main()

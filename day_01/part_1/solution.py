import re


def main():
    filename = "./input_data"
    with open(filename, "r") as f:
        counter = 0
        sum = 0
        for line in f:
            counter += 1
            line_sum = 0
            digits = re.findall("[0-9]", line)
            if len(digits) >= 2:
                line_sum = int(digits[0]) * 10 + int(digits[-1])
            else:
                line_sum = int(digits[0]) * 11

            sum += line_sum

        print(f"{counter} lines read.")
        print(f"Final sum is: {sum}.")


if __name__ == "__main__":
    main()

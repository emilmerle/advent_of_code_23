import re

with open("./input_data", "r") as f:
    sum = 0
    for line in f:
        line_sum = 0
        digits = re.findall("[0-9]", line)
        if len(digits) >= 2:
            line_sum = int(digits[0]) * 10 + int(digits[-1])
        else:
            line_sum = int(digits[0]) * 11
        
        sum += line_sum

    print(sum)
                
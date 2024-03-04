def romanizer(numbers):

    roman_num = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    converted = []

    for i in numbers:
        # transfer int to str
        str_num = str(i)

        if len(str_num) > 2:
            if str_num[0] >= 1 and str_num[0] < 4:
                three_bit = int(str_num[0]) * roman_num[100]
                return three_bit
            elif str_num[0] == 4:
                three_bit = roman_num[400]
                return three_bit
            elif str_num[0] == 5:
                three_bit = roman_num[500]
                return three_bit
            elif str_num[0] > 5 and str_num[0] < 9:
                three_bit = roman_num[500] + (int(str_num[0] - 5) * roman_num[500])
                return three_bit
            elif str_num[0] == 9:
                three_bit = roman_num[900]
                return three_bit


romanizer([1, 60, 561])
# print(romanizer([1, 60, 561]))

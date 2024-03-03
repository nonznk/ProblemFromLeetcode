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

    def convert_roman(num):
        if num >= 1 and num <= 100:
            if num >= 1 and num <= 10:
                new_roman = roman_num[num]
                # converted.append(roman_num[num])
            elif num > 10 and num < 40:
                two_bit = num // 10
                one_bit = num % 10
                new_roman = two_bit * roman_num[10] + roman_num[one_bit]
                # converted.append(new_roman)
            elif num == 40:
                new_roman = roman_num[40]
                # converted.append(new_roman)
            elif num > 40 and num < 50:
                one_bit = num % 10
                new_roman = roman_num[40] + roman_num[one_bit]
                # converted.append(new_roman)
            elif num == 50:
                new_roman = roman_num[50]
                # converted.append(new_roman)
            elif num > 50 and num < 90:
                two_bit = (num - 50) // 10
                one_bit = num % 10
                new_roman = roman_num[50] + two_bit * roman_num[10] + roman_num[one_bit]
                # converted.append(new_roman)
            elif num == 90:
                new_roman = roman_num[90]
                # converted.append(new_roman)
            elif num > 90 and num < 100:
                one_bit = num % 10
                new_roman = roman_num[90] + roman_num[one_bit]
                # converted.append(new_roman)
            elif num == 100:
                new_roman = roman_num[100]
                # converted.append(new_roman)
        return new_roman

    for i in numbers:
        if i >= 1 and i <= 100:
            converted.append(convert_roman(i))
        elif i > 100 and i < 400:
            if i // 100 == 1:
                three_bit = roman_num[100]
            else:
                three_bit = (i // 100) * roman_num[100]
            two_bit = convert_roman(i % 100)
            new_roman = three_bit + two_bit
            converted.append(new_roman)
        elif i == 500:
            new_roman = roman_num[500]
            converted.append(new_roman)
        elif i > 500 and i < 900:
            three_bit = roman_num[500] + ((i - 500) // 100) * roman_num[100]
            two_bit = convert_roman(i % 100)
            new_roman = three_bit + two_bit
            converted.append(new_roman)
        elif i == 900:
            new_roman = roman_num[900]
            converted.append(new_roman)
        elif i > 900 and i < 1000:
            three_bit = roman_num[900]
            two_bit = convert_roman(i % 100)
            new_roman = three_bit + two_bit
            converted.append(new_roman)
        else:
            new_roman = roman_num[1000]
            converted.append(new_roman)

    return converted


print(romanizer([1, 61, 561]))

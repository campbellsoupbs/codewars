#!/usr/bin/python3

# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
# For example, take 153 (3 digits), which is narcisstic:
#     1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narcissistic( value ):
    s_value = str(value)
    length_value = len(s_value)
    l = [int(x) for x in s_value]
    answer = sum([y**length_value for y in l])
    return answer == value


# x = narcissistic(153)
# print(x)

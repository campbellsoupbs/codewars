#!/usr/bin/python3 

class RomanNumerals:

    def to_roman(val):
        units = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX"}
        tens = {0:"", 1:"X", 2:"XX", 3:"XXX", 4:"XL", 5:"L", 6:"LX", 7:"LXX", 8:"LXXX", 9:"XC"}
        hund = {0:"", 1:"C", 2:"CC", 3:"CCC", 4:"CD", 5:"D", 6:"DC", 7:"DCC", 8:"DCCC", 9:"CM"}
        thousand = {0:"", 1:"M", 2:"MM", 3:"MMM"}

        sn = str(val)

        try:
            n_units = int(sn[-1])
            roman_units = units[n_units]
        except:
            roman_units = ""

        try:
            n_tens = int(sn[-2])
            roman_tens = tens[n_tens]
        except:
            roman_tens = ""

        try:
            n_hund = int(sn[-3])
            roman_hund = hund[n_hund]
        except:
            roman_hund = ""

        try:
            n_tho = int(sn[-4])
            roman_tho = thousand[n_tho]
        except:
            roman_tho = ""


        return f'{roman_tho}{roman_hund}{roman_tens}{roman_units}'



    def from_roman(roman_num):
        answer = 0

        roman = {0:"", 1:"I", 2:"II", 3:"III", 4:"IV", 5:"V", 6:"VI", 7:"VII", 8:"VIII", 9:"IX",
                10:"X", 20:"XX", 30:"XXX", 40:"XL", 50:"L", 60:"LX", 70:"LXX", 80:"LXXX", 90:"XC",
                100:"C", 200:"CC", 300:"CCC", 400:"CD", 500:"D", 600:"DC", 700:"DCC", 800:"DCCC", 900:"CM",
                1000:"M", 2000:"MM", 3000:"MMM"}

        revroman = dict((v,k) for k,v in roman.items())

        tho = ["MMM", "MM", "M"]
        hun = ["CM","DCCC", "DCC", "DC", "CD", "CCC", "CC", "C", "D"]
        tens = ["XC", "LXXX", "LXX", "LX", "XL", "XXX", "XX", "X", "L"]
        units = ["IX", "VIII", "VII", "VI", "IV", "V", "III", "II", "I"]

        for numeral in tho:
            if numeral in roman_num:
                answer += revroman[numeral]
                break
            else:
                continue

        for numeral in hun:
            if numeral in roman_num:
                answer += revroman[numeral]
                break
            else:
                continue

        for numeral in tens:
            if numeral in roman_num:
                answer += revroman[numeral]
                break
            else:
                continue

        for numeral in units:
            if numeral in roman_num:
                answer += revroman[numeral]
                break
            else:
                continue
        return answer 

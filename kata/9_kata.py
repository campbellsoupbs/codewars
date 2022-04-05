#!/usr/bin/python3

"""""
See this property again: 135 = 1^1 + 3^2 + 5^3

We need a function to collect these numbers, that may receive two integers a, b that defines the 
range [a, b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property described above.

"""""

def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    alist = []
    for x in range(a, b+1):
        xstr = str(x)
        xlist = [int(number) for number in xstr]
        sum = 0
        for index, num in enumerate(xlist, start=1):
            sum += num**index
        if sum == x:
            alist.append(x)
    if len(alist) > 0:
        return alist
    return []


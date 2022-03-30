#!/usr/bin/python3

#Given an array of integers, find the one that appears an odd number of times.


def find_it(seq):
    num_dict = {}
    for num in seq:
        num_dict[num] = num_dict.get(num, 0) +1
    for key, value in num_dict.items():
        if value%2 == 1:
            return key
        else:
            pass 


# x = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]

# y = find_it(x)
# print(y)

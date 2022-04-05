#!/usr/bin/python3

"""""
Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p

we want to find a positive integer k, if it exists, such that the sum of the digits of n taken to the successive powers of p is equal to k * n.
#In other words:

Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
"""""

def dig_pow(n, p):
    n_str = str(n)
    n_list = [int(x) for x in n_str]
    power_sum = 0
    
    for number in n_list:
        power_sum += number**p
        p += 1
    
    k = power_sum/n

    if float(k).is_integer() == True:
        return k
    return -1

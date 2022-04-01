#!/usr/bin/python3

def max_sequence(arr):
    iter_items = iter(arr)
    try:
        temp_sum = next(iter_items)
    except StopIteration:
        temp_sum = 0
    max_sum = temp_sum
    for item in iter_items:
        temp_sum += item
        if item > temp_sum:
            temp_sum = item
        if temp_sum > max_sum:
            max_sum = temp_sum
    return max_sum if max_sum > 0 else 0
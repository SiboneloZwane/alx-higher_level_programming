#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return None
    for n in range(len(my_list)):
        if n == 0:
            largestNum = my_list[n]
            n = n + 1
        if n < len(my_list) and my_list[n] > largestNum:
            largestNum = my_list[n]
    return largestNum

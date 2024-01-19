#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        new = list(my_list)
        for n in range(len(my_list)):
            if my_list[n] % 2 == 0:
                new[n] = True
            else:
                new[n] = False
        return new

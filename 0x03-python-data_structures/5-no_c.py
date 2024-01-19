#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for n in range(len(my_string)):
        if my_string[n] == 'C' or my_string[n] == 'c':
            pass
        else:
            new_str += my_string[n]
    return new_str

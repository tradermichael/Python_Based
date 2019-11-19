# Author: Michael Le
# Date: 11/12/2019
# Description: Function that takes in a list and iterates over it to reverse the list values

def reverse_list(list_val):
    """
    :param list_val: list of values
    :return: does not return - transforms the actual input
    """
    length_list = len(list_val)
    i = 0
    list_val_rev = list_val[::-1]
    while i < length_list:
        list_val[i] = list_val_rev[i]
        i+=1

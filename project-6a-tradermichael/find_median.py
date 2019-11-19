# Author: Michael Le
# Date: 11/03/2019
# Description: Function that takes a list of numbers, and returns the median value

def find_median(input_array):
    """
    :param input_array: this is a input list of values
    :return: the return value is a median number of the values within the list from input_array
    """
    numberset = [x for x in input_array]
    numberset.sort()
    len_array = len(numberset)
    if (len_array%2) == 0:
        valueone = numberset[(len_array//2)-1]
        valuetwo = numberset[(len_array // 2)]
        median_value = (valueone+valuetwo)/2
    else:
        median_value = numberset[(len_array//2)]
    return median_value
# end of function find_median


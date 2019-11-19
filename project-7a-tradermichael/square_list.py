# Author: Michael Le
# Date: 11/11/2019
# Description: Function that takes a list of values and squares each value in that list


def square_list(list_val):
    """

    :param lst: lst is a list of integers
    :return: does not return. transforms list entered only
    """
    for i in range(len(list_val)):
        list_val[i] = list_val[i]**2
#end
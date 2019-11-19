# Author: Michael Le
# Date: 10/27/2019
# Description: Function that takes two positive integers and finds the product

def multiply(frst_int, scnd_int):
    """
    :param frst_int: a positive integer
    :param scnd_int: a positive integer
    :return: product of the two positive integers
    """
    if (frst_int == 1 or scnd_int == 1):
            if (frst_int == 1):
                result = scnd_int
            if (scnd_int == 1):
                result = frst_int
    else:
        result = frst_int + multiply(frst_int, scnd_int - 1)
    return result

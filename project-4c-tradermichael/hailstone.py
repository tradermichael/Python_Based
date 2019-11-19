# Author: Michael Le
# Date: 10/22/2019
# Description: Hailstone sequence function to find when first value of 1 occurs

def hailstone(start_int):
    '''
    Function takes in an integer (start_int) and multiplies it by 3, then adds one if odd, or divides by 2 if even.
    The function stops when the integer is transformed to 1 and returns how many actions it took to get to 1.
    '''
    hs_value = start_int
    iterations= 0
    while hs_value != 1:
        if (hs_value%2 == 0):
            hs_value = hs_value/2
            iterations += 1
        else:
            hs_value = (hs_value*3)+1
            iterations += 1
    print(iterations)
    return iterations





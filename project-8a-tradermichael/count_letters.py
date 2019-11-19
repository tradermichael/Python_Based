# Author: Michael Le
# Date: 11/17/2019
# Description: Function named count_letters that takes as a parameter a string and returns
# a dictionary that tabulates how many of each letter is in that string

def count_letters(str_val):
    """
    :param str_val: string of alpha/numerical values
    :return: dictionary with count of each distinct alpha value
    """
    count_dict = dict()
    str_val = str_val.upper()
    for x in (str_val):
        if (x not in count_dict and x.isalpha() == True):
            count_dict[x] =1
        else:
         if (x.isalpha() == True):
            count_dict[x] +=1
    return(count_dict)
#end of function count_letters

#testing script
#print(count_letters("Quis custodiet ipsos custodes?"))

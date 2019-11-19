# Author: Michael Le
# Date: 11/18/2019
# Description:  Function named words_in_both that takes two strings as parameters and returns a set of the words contained in both strings


def words_in_both(str1, str2):
    """
    :param str1: String
    :param str2: String
    :return: List of matching strings from str1 and str2
    """
    words1 = str1.lower().split(" ")
    words2 = str2.lower().split(" ")
    result_words = set()
    for x in words1:
        if (x in words2) and (x not in result_words):
            result_words.add(x)
    return result_words
#end of function

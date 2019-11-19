# Author: Michael Le
# Date: 11/05/2019
# Description: Function that takes in a list of names, and returns a list if if name starts with character "K"

def add_surname(list_name):
    """
    :param list_name: list of names
    :return: returns a list with only the names that start with "K" and appends "Kardashian" as the last name to each item in list
    that fit criteria - First name starts with "K"
    """
    k_names = [names + " Kardashian" for names in list_name if names[0] == "K"]
    return k_names

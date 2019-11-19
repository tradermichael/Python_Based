# Author: Michael Le
# Date: 11/05/2019
# Description: class for Person that initiates variables name and age, and function std_dev that finds standard deviation of age list

class Person:

    def __init__(self, name,age):
        """
        :param name: String of Person's name
        :param age: Integer of persons age
        """
        self.name_person = name
        self.age_person = age

def std_dev(input_class):
    """
    :param input_class: variable that contains list of class members
    :return: returns standard deviation of age associated to each class member
    """
    Ages = [x.age_person for x in input_class]
    Count = len(Ages)
    mean_value = sum(Ages)/len(Ages)
    sd_numerator = sum([(x - mean_value)**2 for x in Ages])
    sd_pop = (sd_numerator/Count)**(1/2)
    return sd_pop


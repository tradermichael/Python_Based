# Author: Michael Le
# Date: 11/18/2019
# Description:  Class for Employee, then function that creates dictionary with id as key for employee object

class Employee:

    """
    Employee class to create employee object
    """

    def __init__(self, name = "", ID_number = 0, salary = 0, email_address = ""):
        """
        :param name: name of employee - string
        :param ID_number: ID number of employee - int or string
        :param salary: Salary of employee - int
        :param email_address: Email address of Employee - string
        """
        self.name = name
        self.ID_number = ID_number
        self.salary = salary
        self.email_address = email_address


def make_employee_dict(nameslist,ID_numbers,salaries,email_addresses):
    """
    :param nameslist: list of employee names
    :param ID_numbers: list of ID numbers for employees
    :param salaries: list of employee salaries
    :param email_addresses: list of employee email address
    :dataformat: data should be in same order for each list/employee
    :return: returns dictionary with ID number as key and employee object as lookup
    """
    employee_dict = dict()
    emp = Employee()
    for x in range(len(nameslist)):
        emp.name = nameslist[x]
        emp.ID_number = ID_numbers[x]
        emp.salary = salaries[x]
        emp.email_address = email_addresses[x]
        employee_dict[ID_numbers[x]] = emp
        emp = Employee()
    return employee_dict

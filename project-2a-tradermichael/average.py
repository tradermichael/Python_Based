# Author: Michael Le
# Date: 10/2/2019
# Description: Asks the user for five numbers, then takes the average
print("Please enter five numbers.")
number_1 = float(input("Enter 1st number and press enter:"))
number_2 = float(input("Enter 2nd number and press enter:"))
number_3 = float(input("Enter 3rd number and press enter:"))
number_4 = float(input("Enter 4th number and press enter:"))
number_5 = float(input("Enter 5th number and press enter:"))
average_all = (number_1+number_2+number_3+number_4+number_5)/5
print("The average of those numbers is:")
print(average_all)

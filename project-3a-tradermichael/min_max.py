# Author: Michael Le
# Date: 10/12/2019
# Description: Asks user to enter positive integer, then asks for number, number of times, and prints out min and max of inputs.

iteration = int(input("How many integers would you like to enter?\n"))
if (iteration == 1):
    print("Please enter " + str(iteration) + " integer.")
else:
    print("Please enter " + str(iteration) + " integers.")
min_int = 0
max_int = 0
for i in range(0,iteration):
    number = int(input())
    if (iteration == 1):
        min_int = number
        max_int = number
    else:
        if (number < min_int):
            min_int = number
        if (number > max_int):
            max_int = number
print("min: " + str(min_int))
print("max: " + str(max_int))


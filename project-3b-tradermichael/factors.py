# Author: Michael Le
# Date: 10/14/2019
# Description: Asks user for positive integer, then prints factors of that integer

positive_integer = int(input("Please enter a positive integer:"))
print("The factors of ", str(positive_integer)," are:")
answer = ""
for i in range(2,positive_integer-1):
    if(positive_integer%i == 0 and answer == ""):
        answer += (str(i))
    elif (positive_integer%i == 0):
        answer += ("\n"+str(i))

print(answer)
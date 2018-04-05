#Michael Le - CS 161
#Change to Dollars
print("Please let me know how much change you have")
pennies = int(input("How many pennies?"))
nickels = int(input("How many nickels?"))
dimes = int(input("How many dimes?"))
quarters = int(input("How many quarters?"))
#half_dollars = input("How many half dollars?")
dollar_bills = int(input("How many dollar bills?"))

d = (pennies * .01 + nickels * .05 + dimes * .10 + quarters * .25 + dollar_bills)

print("Total Value of your change is", round(d,2), "dollars")
print("This means, you have" , int(round(d,2)-d%1) , "dollars and" , round((d%1)*100), "cents")
print("If the McChicken was stil one dollar each, you could buy", int(round(d,2)-d%1), "of them!")

#alternatively
'''

Total = 0

print("Please let me know how much change you have")
pennies = int(input("How many pennies?"))
Total = Total + (pennies * .01)
print(Total)
nickels = int(input("How many nickels?"))
Total = Total + (nickels * .05)
print(Total)
dimes = int(input("How many dimes?"))
Total = Total + (dimes * .10)
print(Total)
quarters = int(input("How many quarters?"))
Total = Total + (quarters * .25)
print(Total)
#half_dollars = input("How many half dollars?")
dollar_bills = int(input("How many dollar bills?"))
Total = Total + (dollar_bills)
print("Final Value", Total)

print("Total Value of your change is", round(Total,2), "dollars")
print("This means, you have" , int(round(Total,2)-Total%1) , "dollars and" , round((d%1)*100), "cents")
print("If the McChicken was stil one dollar each, you could buy", int(round(Total,2)-Total%1), "of them!")
'''

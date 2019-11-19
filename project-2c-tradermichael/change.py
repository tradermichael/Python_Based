cents = int(input("Please enter an amount in cents less than a dollar.\n"))
quarters=cents//25
leftover=cents
leftover=(cents%25)
dimes = leftover//10
leftover=(leftover%10)
nickels = leftover//5
leftover = (leftover%5)
pennies = leftover
print("Your change will be:")
print("Q: "+str(quarters))
print("D: "+str(dimes))
print("N: "+str(nickels))
print("P: "+str(pennies))


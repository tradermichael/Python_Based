#Michael Le - CS161
#Age

print("hello, please enter your age in years")
age = int(input("Please enter your age in years:"))
if (age > 100):
  print("amazing! you must be young at heart") 
else:
  print("you're still young!")

age = str(age)

if age == '1': 
  print("you are " + age + " year old")
else:
  print("you are " + age + " years old")

#print with auto space is print("you are", age, "years old")

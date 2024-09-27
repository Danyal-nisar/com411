# Ask user to enter their name
name = input("What is your name? ")
print(f"Nice to meet you, {name}.")
eye = input("Please enter a character for the robots eye.")
print("The robot's expression is now as follows:")
print("######################")
print(f"#  ({eye})   ({eye})         #")
print("#                     #")
print("#                     #")
print("#                     #")
print("#   ______________    #")
print("######################")



name = input("What is your name? ")
print(f"{name}.")

age = input("how old are you (in years?) ")
print(f"{age}.")

height = float(input("how tall are you (in meters)? "))
print(f"{height}.")
# have to add float or it wont work
weight = float(input("how much do you weigh (in kilograms)?"))
print(f"{weight}.")

# this is where it shold calculate BMI
bmi = weight / (height ** 2)

# this is where it should show the BMI and the age
print(f"{name}, your BMI is {bmi:.2f} and you are {age} years old.")


book = input("What kind of book is this? ")

if book == "adventure":
    print("i love adventure books!")

print("Finished reading book!")

print("")
#use input function to allow activity to be saved
activity = input("Please enter the activity to be performed: ")
#if function is used to tell system that if activity is
#calculated then print performing calculate or else something else
if activity == "calculate":
    print("Performing calculations...")
else:
    print("Performing the activity...")

print("Activity completed!")

# using direction as the input to have a question.
direction= input("Please enter the name of the direction i should travel: ")
if direction == "upwards":
  print("i am moving in an upwards direction ")
#having if as a way to make sure that multiple directions can be picked and are printed as being their.
if direction == "downwards":
    print("i am moving in an downwards direction ")

if direction == "left":
  print("i am moving in an left direction ")

if direction == "right":
    print("i am moving in an right direction ")

number=(int(input ("Please enter a whole number: ")))
if number % 2 == 0:
       print(f"your number {number} is  even number")

else:
        print(f"your number {number} is odd number")

number1 = int(input("please enter a first number: "))
number2 = int(input("please enter a second number: "))

if number1>number2:
    print("your second number is the smallest number")

elif number2>number1:
    print("your first number is the smallest number")

if number1 == number2:
    print("both are equal")

print("")
print("")



number4 = int(input("Please enter the first whole number:"))
number5 = int(input("Please enter the second whole number:"))
number6 = int(input("Please enter the third whole number:"))

evencount = 0
oddcount = 0

if number4 % 2 == 0:
    evencount += 1
else:
    oddcount += 1

if number5 % 2 == 0:
    evencount += 1
else:
    oddcount += 1

if number6 % 2 == 0:
    evencount += 1
else:
    oddcount += 1

print(f"There were {evencount} even and {oddcount} odd numbers.")



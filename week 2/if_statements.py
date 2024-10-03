book = input("What kind of book is this? ")

if book == "adventure":
    print("i love adventure books!")

print("Finished reading book!")

print("")
#use input function to allow activity to be saved
activity = input("Please enter the activity to be performed: ")
#if function is used to tell system that if activity is calculate then print performing calculate or else something else
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



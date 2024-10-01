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
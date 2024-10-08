covertype = input("Enter the type of cover of the book : ") #ask user what the cover type is
if covertype == "soft":  #if

    perfect_bound = input("Is the book perfect bound? : ")
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft cover, not perfect bound books can still be very appealing!")
elif covertype == "hard":
    print("Books with hard covers can be more expensive!")

print("")
print("")

where = input("Where should I look? ")
#the begining location where check is taking place
if where == "in the bedroom":
    # their must be a prompt to search a specific area within the bedroom
    where = input("Where in the bedroom should I look? ")
    if where == "under the bed":

        print("Found some shoes but no phone.")
    elif where == "on the dresser":

        print("Found some old magazines but no phone.")
    else:

        print("Found some bedroom stuff but no phone.")


elif where == "in the bathroom":
    where = input("Where in the bathroom should I look? ")
    if where == "in the bathtub":
        print("Found a rubber duck but no phone.")
    else:
        print("Found bathroom stuff but no phone.")


elif where == "in the living room":
    where = input("Where in the living room should I look? ")
    if where == "on the table":
        print("Yes, I found my phone!")
    else:
        print("I do not know where that is, but I will keep looking.")

else:
    print("I don't know where that is but I will keep looking.")

print("")


covertype = input("Enter the type of cover of the book : ")

if covertype == "soft":
    perfect_bound = input("Is the book perfect bound? : ")
    if perfect_bound == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft cover, not perfect bound books can still be very appealing!")
elif covertype == "hard":
    print("Books with hard covers can be more expensive!")



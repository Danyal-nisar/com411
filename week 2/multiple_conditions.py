adventure = input("what type of adventure should i have :")

if adventure in ["scary", "short"]:
    print("Entering the dark forest!")

elif adventure in ["safe", "long"]:
    print("Taking the safe route.")

else:
    print("Not sure which route to take.")

print("")
print("")


noise = input("What did I hear?")
see = input("What did I see?")

if noise in ["grr"] and see in ["two red eyes"]:
    print("There's a scary creature. I should get out of here!")

else:
        print("I am a little scared but I will continue.")

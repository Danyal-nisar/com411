def listen():
    # Ask the user to enter a word representing a sound
    sound = input("What sound did you hear?\n")
    # Display the message with the entered sound
    print(f"That was a loud {sound}!")

# Call the listen function
listen()

print("")

def identify():
 # Ask user for what lies ahead
 print("What lies before us?")
 response = input()
 # Display message
 if response == "a large boulder":
    print("It's time to run!")
 else:
    print("We will be fine.")
# Call to function
identify()

print("")

def escape_by(plan):
    # Determine which message to display
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running around":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "cross bridge ahead":
        print("That might just work! Let's go!")
    else:
        print("Not sure about that plan!")

# Calls to the function
escape_by("jumping over")
escape_by("running around")
escape_by("cross bridge ahead")

Print("")

def cross_bridge(steps):
 for step in range (steps):
    print("Crossed step.")
 if steps > 5:
    print("The bridge is collapsing!")
 else:
     print("We must keep going!")
cross_bridge(3)
cross_bridge(6)

print("")

def climb_ladder(steps_remaining, steps_crossed):
 # Compare and display a suitable message
 if steps_remaining > steps_crossed:
     print("Still some way to go!")
 else:
     print("We are almost there!")
# calls to function
climb_ladder(5, 2)
climb_ladder(2, 5)

print("")


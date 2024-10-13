num_of_mountains = int(input("how many mountains should i show")) #ask user how many mountains to display
for i in range(num_of_mountains): #create loop to recreate this as many times needed
    print("     /\\            ")
    print("    /  \\            ")
    print("   /____\\               ")
    print("")

print("")


#  Ask the user how far they are from the target
num_of_steps = int(input("How far are we from the target? "))
# Step 2: Initialize the step count
step_count = 0
# Step 3: Use a for loop to count down to the target
for i in range(num_of_steps):
    step_count += 1  # Increment the step count
    print(f"{num_of_steps - step_count} steps remaining")  # Print remaining steps
# Step 4: Print the target achieved message after counting
print("Target achieved!")

print("")

# Step 1: Ask the user for the required brightness level
brightness_level = int(input("What level of brightness is required? "))
# Step 2: Print adjusting message
print("Adjusting brightness...")
# Step 3: Use a for loop to print the brightness levels
for i in range(1, brightness_level + 1):  # Start from 1 to match output format
    print(f"Brightness level: {'*' * i}")  # Print the current brightness level as asterisks



which_word = input("What word do you see? ")
# Step 2: Print a message indicating the start of the index display
print("Displaying index positions...")
# Step 3: Use a for loop to display the index positions and corresponding characters
for i in range(len(which_word)):  # Loop through each index of the word
    print(f"index {i}: {which_word[i]}")  # Print the index and the character at that index
# Step 4: Print "Done!" after displaying all indices
print("Done!")

print("")

 #Ask the user for a phrase
phrase = input("What phrase do you want to see in reverse? ")

#Print a message indicating reversing process
print("Reversing...")

#  Initialize an empty string to hold the reversed phrase
reversed_phrase = ""

# Use a for loop to reverse the phrase
for char in phrase:  # Iterate over each character in the original phrase
    reversed_phrase = char + reversed_phrase  # Prepend each character to the reversed string

print(f"The phrase is: {reversed_phrase}")

print("")

#  Ask the user for a phrase
phrase = input("What phrase do you see? ")

#Print a message indicating the output process
print("Outputting...")

#Print the phrase header
print("The phrase is:")

#  Use a for loop to output each character on a new line
for char in phrase:  # Loop through each character in the phrase
    print(char)  # Print the current character on a new line




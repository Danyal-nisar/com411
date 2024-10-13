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

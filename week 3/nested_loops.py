# Ask the user for the number of rows and columns
num_rows = int(input("How many rows should I have?\n"))  # Number of rows input
num_columns = int(input("How many columns should I have?\n"))  # Number of columns input

print("\nHere I go:")  # Print the starting message

# Create the grid of smiley faces
for i in range(num_rows):  # Loop for each row
    for j in range(num_columns):  # Loop for each column
        print(":-)", end=" ")  # Print smiley face without a new line
    print()  # Move to the next line after each row is printed

print("Done!")  # Print the ending message

print("")


# Function to calculate distance between markers
def calculate_distance(sequence, marker):
    positions = []  # List to store positions of markers

    # Loop through the sequence to find markers
    for index in range(len(sequence)):
        if sequence[index] == marker:  # If the current character is the marker
            positions.append(index)  # Store its position

    # Calculate the distance between the last two markers
    if len(positions) < 2:  # If there are less than 2 markers
        return 0  # Distance is 0
    else:
        return positions[-1] - positions[-2]  # Return distance between last two markers


# Main loop for user input
while True:
    sequence = input("Please enter a sequence\n")  # Get sequence from user
    marker = input("Please enter the character for the marker\n")  # Get marker from user

    distance = calculate_distance(sequence, marker)  # Calculate distance

    print(f"The distance between the markers is {distance}.")  # Print result

    # Ask if the user wants to continue
    another = input("Do you want to enter another sequence? (yes/no): ")
    if another.lower() != 'yes':  # If not continuing
        break  # Exit loop

num_apples_to_remove = int(input("how many apples should i remove"))
#use while loop
apples_to_remove = 0
while apples_to_remove < num_apples_to_remove:
    print("removed apple") #to show that the apples have been removed
    apples_to_remove += 1






objects_to_avoid = int(input("How many obstacles must I avoid? "))
num_of_obstacles = 0
while num_of_obstacles < objects_to_avoid: # Use a while loop to simulate avoiding obstacles. It runs until all obstacles are avoided.
    num_of_obstacles += 1    # Increment the number of obstacles avoided.
    print(f"Avoiding... Done! {num_of_obstacles} obstacle{'s' if num_of_obstacles > 1 else ''} avoided.")
print("All obstacles have been avoided.", end="")
print(" second message is on the same line ")


needed_charge_bars = int(input("how many bars should be charged ?"))
#input is needed to make ti a queestion to the user and to integrate the response
charged_bars = 0 #this is to set the intial count of charged bars to 0
while charged_bars < needed_charge_bars: #while loop to make action repeat until fulfilled
    charged_bars += 1 #makes sure the charge bars by one
    print("Charging:", '█' * charged_bars)
    print("the battery is fully charged ")


repeated_word = input("please enter a phrase")
num_characters = len(repeated_word) #calculating number of highs in a phrase
for _ in range(num_characters): #print hi number of times to be equal to the number of characters
    print("Hi,", end=' ')

print("")

# Display the initial message indicating the start of the calculation.
print("Calculating the sum of the first 100 numbers...")
# Initialize variables for the sum and the counter.
sum_of_numbers = 0
current_number = 1
# Use a while loop to calculate the sum of numbers from 1 to 100 (inclusive).
while current_number <= 100:
    sum_of_numbers += current_number
    current_number += 1
# Once the sum is calculated, display the final message along with the answer.
print(f"...Done! The answer is {sum_of_numbers}")

print("")


numbers_to_sum = int(input("How many numbers do you want to sum? "))
sum_of_numberss = 0
num_count = 1
while num_count <= numbers_to_sum:
    number = int(input(f"Please enter number {num_count} of {numbers_to_sum}: "))  # Prompt for the actual number
    sum_of_numberss += number  # Add the entered number to the sum
    num_count += 1  # Increment the counter

print(f"The answer is {sum_of_numberss}.")  # Print the total sum

print("")



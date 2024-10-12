num_apples_to_remove = int(input("how many apples should i remove"))
#use while loop
apples_to_remove = 0
while apples_to_remove < num_apples_to_remove:
    print("removed apple") #to show that the apples have been removed
    apples_to_remove += 1






objects_to_avoid = int(input("How many obstacles must I avoid? "))
num_of_obstacles = 0

while num_of_obstacles < objects_to_avoid:
    num_of_obstacles += 1
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

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
charged_bars = 0
while charged_bars < needed_charge_bars:
    charged_bars += 1
    print("Charging:", '█' * charged_bars)
    print("the battery is fully charged ")


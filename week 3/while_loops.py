num_apples_to_remove = int(input("how many apples should i remove"))
#use while loop
apples_to_remove = 0
while apples_to_remove < num_apples_to_remove:
    print("removed apple") #to show that the apples have been removed
    apples_to_remove += 1



objects_to_avoid = int(input("how many obstacles must i avoid"))

num_of_obstacles = 0

while num_of_obstacles < objects_to_avoid:

    print("avoiding")

num_of_obstacles += 1

print(f"...done{objects_to_avoid}obstacles avoided")

print("all obstacles have been avoided")
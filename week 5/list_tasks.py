
def directions():

    steps = []

    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")

    return steps

def run_task1():

    steps_list = directions()

    print(steps_list)

if __name__ == "__main__":
    run_task1()

print("")

print("Moving...")

def movements():
    path = []
    path.append("Move Forward for 10 steps")
    path.append("Move Backward for 5 steps")
    path.append("Move Left for 3 steps")
    path.append("Move Right for 1 step")
    return path

def run_task():
    steps_list = movements()
    for step in steps_list:
        print(step)

if __name__ == "__main__":
    run_task()


print("")

def steps():
    steps = []
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")
    return steps

def directions():
    steps = []
    steps.append("Move Forward")
    steps.append("Move Backward")
    steps.append("Turn Left")
    steps.append("Turn Right")
    return steps

def menu():
    print("Please select a direction:")
    for i, step in enumerate(directions(), start=1):
        print(f"{i}. {step}")

    choice = int(input("Enter the number of your choice: "))
    return choice

if __name__ == "__main__":
    user_choice = menu()
    print(f"You selected: {directions()[user_choice - 1]}")

print("")


def steps():
    # List of movement options
    return ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]


def menu():
    # Display options and get user input
    print("Please enter a direction:")
    for i, step in enumerate(steps()):
        print(f"{i}: {step}")

    choice = int(input())  # Get the user's choice
    return choice


def escape_route():
    route = []  # Initialize the escape route
    while True:
        choice = menu()  # Show menu and get choice
        if 0 <= choice < len(steps()):  # Check if choice is valid
            route.append(steps()[choice])  # Add choice to route
            print(f"Current escape route: {route}")
        else:
            print("Invalid choice. Please try again.")

        if len(route) >= 5:  # Stop after 5 selections
            break

    return route

print("")

def directions():
    steps = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return steps

def menu_and_input():
    print("Please select a direction:")
    directions_list = directions()
    for index, direction in enumerate(directions_list):
        print(f"{index}: {direction}")
    user_choice = int(input("Enter the number corresponding to your choice: "))
    return directions_list[user_choice]

def run_task4():
    route = []
    print("Working out escape route...")
    for _ in range(5):
        selected_direction = menu_and_input()
        route.append(selected_direction)
    print(f"Escape route: {route}")

run_task4()

print("")

def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return min(likelihoods)

def run_task1():
    min_likelihood = likelihood()
    print(f"Minimum likelihood of falling: {min_likelihood}%")

if __name__ == "__main__":
    run_task1()

print("")

def steps():
    likelihoods = [
        ("step 1", 50),
        ("step 2", 38),
        ("step 3", 27),
        ("step 4", 99),
        ("step 5", 4)
    ]
    return likelihoods

def run_task3():
    step_list = steps()
    good_steps = []
    bad_steps = []

    for step in step_list:
        if step[1] >= 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)

    print(f"Good steps: {len(good_steps)}, Bad steps: {len(bad_steps)}")

if __name__ == "__main__":
    run_task3()




































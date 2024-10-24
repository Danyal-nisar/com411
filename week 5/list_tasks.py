
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







































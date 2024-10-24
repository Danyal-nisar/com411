
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




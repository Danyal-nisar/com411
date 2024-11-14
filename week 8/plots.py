import matplotlib.pyplot as plt

def display_line(x_values, y_values):
    plt.plot(x_values, y_values)
    plt.xlabel("X Values")
    plt.ylabel("Y Values")
    plt.title("Line Plot of x vs. y")
    plt.grid(True)
    plt.show()

def run_task1():

    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]

    display_line(x_values, y_values)


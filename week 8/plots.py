
import matplotlib.pyplot as plt
def display_line(x_values, y_values):
    plt.plot(x_values, y_values, label='y = x^2')
    plt.title("Basic Line Plot")
    plt.xlabel("x values")
    plt.ylabel("y values")
    plt.grid(True)
    plt.legend()
    plt.show()

def run_task1():
    x_values = [1, 2, 3, 4, 5]
    y_values = [1, 4, 9, 16, 25]
    display_line(x_values, y_values)

if __name__ == "__main__":
    run_task1()

print("")

import matplotlib.pyplot as plt


def small():
    x = [0, 1, 1, 0, 0]
    y = [0, 0, 1, 1, 0]

    plt.plot(x, y, 'r:', marker='o')
    plt.show()


def medium():
    x = [-1, 2, 2, -1, -1]
    y = [-1, -1, 2, 2, -1]

    # Plot the medium square
    plt.plot(x, y, 'g--', marker='s')  # Green dashed line with square markers
    plt.show()

def large():
    x = [-2, 3, 3, -2, -2]
    y = [-2, -2, 3, 3, -2]

    plt.plot(x, y, 'b-', marker='p')  # Blue solid line with pentagon markers
    plt.show()


# Call the functions
small()
medium()
large()

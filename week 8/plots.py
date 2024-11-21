# plots.py
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



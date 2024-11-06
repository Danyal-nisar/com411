import os

def cwd():
    path = os.getcwd()
    print(f"The current working directory is {path}")
    print("The directory contains the following files:")
    for file_name in os.listdir(path):
        print(file_name)

def run():
    print("Processing...")
    cwd()

run()

print("")


def display_chars(file_path, num_chars):
    with open(file_path, 'r') as file:
        text = file.read(num_chars)
        print("The first", num_chars, "characters are:")
        print(text)

def display_line(file_path):
    with open(file_path, 'r') as file:
        line = file.readline()
        print("The first line is:")
        print(line)

def display_text(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        print("The full text is:")
        print(text)

def run_task2():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")

if __name__ == "__main__":
    run_task2()

print("")

def search(file_name):
    print("Searching...")
    with open(file_name, 'r') as file:
        for line in file:
            print(f"Looked in {line.strip()}.")
    print("...Done!")

def run_task3():
    search("library.txt")

if __name__ == "__main__":
    run_task3()

print("")


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


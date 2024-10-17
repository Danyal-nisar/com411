def get_ascii_code():
    letter = input("Please enter a letter: ")

    ascii_code = ord(letter)
    print(f"The ASCII code for {letter} is: {ascii_code}")


print("Program Started!")

get_ascii_code() #function being called

print("Program Ended!")

def get_ascii_code():
    letter = input("Please enter a letter: ")

    ascii_code = ord(letter)
    print(f"The ASCII code for {letter} is: {ascii_code}")


print("Program Started!")

get_ascii_code() #function being called

print("Program Ended!")

print("")


def ascii_program():
    print("Program Started!")

    ascii_code = abs(int(input("Please enter an ASCII code: ")))

    if ascii_code in range(32, 127):
        print(f"The character represented by the ASCII code {ascii_code} is: {chr(ascii_code)}")
    else:
        print("Error: The entered code is not within the printable ASCII range (32-126).")

    print("Program Ended!")

ascii_program()

print("")


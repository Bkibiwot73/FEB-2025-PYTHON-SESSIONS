# error_handling.py

filename = input("Enter the filename to read: ")

try:
    with open(filename, "r") as file:
        print(file.read())
except FileNotFoundError:
    print("Error: The file does not exist.")
except IOError:
    print("Error: The file could not be read.")

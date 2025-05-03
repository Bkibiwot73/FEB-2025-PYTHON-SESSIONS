# file_read_write.py

try:
    with open("input.txt", "r") as infile:
        lines = infile.readlines()
except FileNotFoundError:
    print("Error: 'input.txt' not found. Please ensure the file exists in the script's directory.")
    exit(1)

try:
    with open("output.txt", "w") as outfile:
        for i, line in enumerate(lines, start=1):
            outfile.write(f"{i}: {line.upper()}")
except IOError as e:
    print(f"Error writing to 'output.txt': {e}")
    exit(1)
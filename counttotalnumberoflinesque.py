# File paths
input_filename = "input.txt"
output_filename = "output.txt"

# 1. Read all lines from input.txt
with open(input_filename, "r") as infile:
    lines = infile.readlines()

# 2. Count the total number of lines
total_lines = len(lines)

# 3. Extract the first two lines
first_two_lines = lines[:2]

# 4. Write the extracted lines to output.txt
with open(output_filename, "w") as outfile:
    outfile.writelines(first_two_lines)

# 5. Print the required messages to the screen
print(f"Total number of lines: {total_lines}")
print(f"First two lines written to {output_filename}")